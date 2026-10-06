#!/usr/bin/env python3
"""Run (or preflight) one arm of lean-v1.

  python3 evals/scripts/run_eval.py --config evals/configs/base-v1.yaml --preflight
  python3 evals/scripts/run_eval.py --config evals/configs/base-v1.yaml --phase smoke      # paid; needs approval.json
  python3 evals/scripts/run_eval.py --config evals/configs/base-v1.yaml --phase rest       # paid; needs smoke complete
  python3 evals/scripts/run_eval.py --config ... --phase smoke --mock --out-dir /tmp/mock   # offline, no network

No paid call is made unless an approval record exists with a dollar ceiling. Held-out outputs go only under evals/private/.
"""
import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
import evalcore as E  # noqa: E402
import sources as S  # noqa: E402
from validate_custom import DEV, HELD, content_hash as custom_hash, load  # noqa: E402

ROOT = S.ROOT
PUBLIC_CACHE = ROOT / "evals/cache/public-lean-v1.jsonl"


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def load_cfg(path):
    cfg = E.load_yaml(path)
    if "extends" in cfg:
        base = load_cfg(ROOT / cfg["extends"])
        for k, v in cfg.items():
            if k in ("extends",):
                continue
            base[k] = {**base[k], **v} if isinstance(v, dict) and isinstance(base.get(k), dict) else v
        cfg = base
    return cfg


def load_env_key():
    if "DEEPSEEK_KEY" in os.environ:
        return os.environ["DEEPSEEK_KEY"]
    envp = ROOT / ".env"
    if envp.exists():
        for line in envp.read_text().splitlines():
            if line.startswith("DEEPSEEK_KEY="):
                return line.split("=", 1)[1].strip().strip("'\"")
    return None


def load_cases(cfg, phase):
    lean = [json.loads(l) for l in (ROOT / cfg["dataset_manifest"]["lean"]).read_text().splitlines() if l.strip()]
    pub = {c["case_id"]: c for c in map(json.loads, PUBLIC_CACHE.read_text().splitlines())}
    dev = {r["case_id"]: r for r in load(DEV)}
    held = {r["case_id"]: r for r in load(HELD)}
    cases = []
    for e in lean:
        src = {"public": pub, "development": dev, "heldout": held}[e["split"]]
        if e["case_id"] not in src:
            raise SystemExit(f"manifest case {e['case_id']} not found in source data")
        c = src[e["case_id"]]
        recomputed = E.case_hash(c) if e["split"] == "public" else custom_hash(c)
        if recomputed != e["content_hash"] or c["content_hash"] != e["content_hash"]:
            raise SystemExit(f"content hash drift for {e['case_id']}; stopping (source-version drift)")
        cases.append({**c, "in_smoke": e["in_smoke"]})
    if phase == "smoke":
        cases = [c for c in cases if c["in_smoke"]]
    elif phase == "rest":
        cases = [c for c in cases if not c["in_smoke"]]
    seed = cfg["randomization"]["order_seed"]
    cases.sort(key=lambda c: E.sha256_text(seed + c["case_id"]))
    return cases


def est_tokens(text):
    try:
        import tiktoken
        enc = tiktoken.get_encoding("cl100k_base")
        return max(len(enc.encode(text, disallowed_special=())), len(text) // 4)
    except Exception:
        return len(text) // 4


def preflight(cfg, cases, constitution):
    prices = cfg["prices"]
    rows, tot_in = [], 0
    for c in cases:
        msgs = E.build_messages(cfg, constitution, c)
        n = est_tokens("".join(m["content"] for m in msgs))
        rows.append(n)
        tot_in += n
    prefix = est_tokens(E.system_prefix(cfg, constitution))
    n = len(cases)
    out_worst = n * cfg["decoding"]["max_tokens"]
    worst = (tot_in * 1.15 * prices["input_cache_miss"] + out_worst * prices["output"]) / 1e6
    suffix_tokens = tot_in - prefix * n
    expected_hit = (prefix * (n - 1) * prices["input_cache_hit"] + prefix * prices["input_cache_miss"] + suffix_tokens * prices["input_cache_miss"]) / 1e6
    expected_out = (n * 500 * prices["output"]) / 1e6
    return {
        "generated_at": now(), "arm": cfg["arm"], "model": cfg["provider"]["model"], "price_basis": prices,
        "cases": n, "estimated_prefix_tokens": prefix, "estimated_total_input_tokens": tot_in,
        "max_output_tokens_total": out_worst,
        "worst_case_cost_usd_no_cache_all_max_output": round(worst, 4),
        "expected_cost_usd_with_prefix_cache_500_out_tokens": round(expected_hit + expected_out, 4),
        "hard_stop": "ledger refuses a call if cumulative cost + worst-case next call (1.15x input estimate, 600 output) would exceed the approved ceiling; also stops at 160 attempts",
        "token_estimation": "max(cl100k via tiktoken, chars/4); provider usage replaces estimates after each call",
    }


def call_provider(cfg, key, messages):
    body = {"model": cfg["provider"]["model"], "messages": messages, "max_tokens": cfg["decoding"]["max_tokens"],
            "temperature": cfg["decoding"]["temperature"], "top_p": cfg["decoding"]["top_p"], "stream": False,
            "thinking": {"type": "disabled"}}
    t0 = time.time()
    r = requests.post(cfg["provider"]["base_url"] + cfg["provider"]["endpoint"], json=body,
                      headers={"Authorization": f"Bearer {key}"}, timeout=180)
    return r, time.time() - t0


def mock_provider(cfg, messages):
    last = messages[-1]["content"]
    text = "(A)\nMock answer." if "Reply with the letter" in last else "Mock answer. " * 20
    toks = E.sha256_text(last)  # deterministic filler
    usage = {"prompt_tokens": est_tokens("".join(m["content"] for m in messages)), "completion_tokens": 30, "cache_hit": 0}
    return {"id": "mock-" + toks[:12], "choices": [{"message": {"content": text}, "finish_reason": "stop"}], "usage": usage}


def normalize_usage(u):
    hit = u.get("prompt_cache_hit_tokens", 0)
    miss = u.get("prompt_cache_miss_tokens", u.get("prompt_tokens", 0) - hit)
    return {"prompt_tokens": u.get("prompt_tokens", hit + miss), "completion_tokens": u.get("completion_tokens", 0), "cache_hit": hit, "cache_miss": miss}


def read_records(path):
    recs = {}
    if path.exists():
        for l in path.read_text().splitlines():
            if l.strip():
                r = json.loads(l)
                recs[r["case_id"]] = r
    return recs


def write_checkpoint(path, phase, cfg, ledger, done, pending, errors, next_action):
    path.parent.mkdir(parents=True, exist_ok=True)
    prior = json.loads(path.read_text()).get("smoke_complete") if path.exists() else None
    path.write_text(json.dumps({"updated_at": now(), "phase": phase, "smoke_complete": prior, "run_id": cfg["run_id"], "completed_case_ids": sorted(done),
                                "pending_case_ids": sorted(pending), "cumulative": ledger.to_dict(), "open_errors": errors,
                                "next_action": next_action}, indent=2) + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    ap.add_argument("--phase", choices=["smoke", "rest", "all"], default="smoke")
    ap.add_argument("--preflight", action="store_true")
    ap.add_argument("--mock", action="store_true")
    ap.add_argument("--out-dir", help="override output dir (mock runs)")
    a = ap.parse_args()

    cfg = load_cfg(ROOT / a.config)
    if cfg["arm"] == "candidate" and not a.mock:
        raise SystemExit("candidate arm is inactive during G002")
    cpath = ROOT / cfg["constitution"]["path"] if cfg["constitution"]["path"] else None
    if cpath is None:
        raise SystemExit("constitution path is not set")
    const_bytes = cpath.read_bytes()
    if S.sha256_bytes(const_bytes) != cfg["constitution"]["sha256"]:
        raise SystemExit("constitution hash does not match config; stopping")
    if S.sha256_bytes((ROOT / cfg["dataset_manifest"]["lean"]).read_bytes()) != cfg["dataset_manifest"]["lean_sha256"]:
        raise SystemExit("lean-v1 manifest hash does not match config; stopping")
    constitution = const_bytes.decode("utf-8")
    cases = load_cases(cfg, a.phase if not a.preflight else "all")

    if a.preflight:
        pf = preflight(cfg, cases, constitution)
        out = ROOT / "evals/runs" / cfg["run_id"] / "preflight.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(pf, indent=2) + "\n")
        print(json.dumps(pf, indent=2))
        return 0

    outs = {k: (Path(a.out_dir) / Path(cfg["outputs"][k]).name if a.out_dir else ROOT / cfg["outputs"][k])
            for k in ("public_and_development", "heldout", "usage", "checkpoint", "approval")}
    if a.mock:
        ceiling = 1e9
        key = None
    else:
        ap_path = outs["approval"]
        if not ap_path.exists():
            raise SystemExit(f"no approval record at {ap_path}; no paid call is allowed")
        approval = json.loads(ap_path.read_text())
        if approval.get("model") != cfg["provider"]["model"] or approval.get("arm") != cfg["arm"]:
            raise SystemExit("approval record does not match model/arm; stopping")
        ceiling = approval["ceiling_usd"]
        key = load_env_key()
        if not key:
            raise SystemExit("DEEPSEEK_KEY not available")
        if a.phase in ("rest", "all"):
            cp = json.loads(outs["checkpoint"].read_text()) if outs["checkpoint"].exists() else {}
            if cp.get("smoke_complete") is not True and a.phase == "rest":
                raise SystemExit("smoke phase has not completed cleanly; refusing to run the remaining cases")

    for p in outs.values():
        p.parent.mkdir(parents=True, exist_ok=True)
    records = {**read_records(outs["public_and_development"]), **read_records(outs["heldout"])}
    ledger = E.BudgetLedger(ceiling, cfg["caps"]["max_generations"], cfg["caps"]["max_output_tokens_per_generation"], cfg["prices"])
    unc_path = outs["checkpoint"].parent / "uncertain.json"
    uncertain = json.loads(unc_path.read_text()) if unc_path.exists() else {}
    for r in records.values():
        if r.get("status", "").startswith("omitted"):
            continue
        for i in range(r.get("retry_count", 0)):
            ledger.record({}, retry=i > 0, completed=False)
        ledger.record(r.get("usage", {}), retry=r.get("retry_count", 0) > 0, completed=r.get("status") == "complete")
    for cid, n in uncertain.items():
        if records.get(cid, {}).get("status") != "complete":
            for i in range(n):
                ledger.record({}, retry=i > 0, completed=False)
    constitution_sha = cfg["constitution"]["sha256"]
    errors, done = [], {c for c, r in records.items() if r.get("status") == "complete"}
    todo = [c for c in cases if E.should_send(c["case_id"], records)]
    pending = {c["case_id"] for c in todo}
    sent = 0
    for c in todo:
        msgs = E.build_messages(cfg, constitution, c)
        est_in = est_tokens("".join(m["content"] for m in msgs))
        try:
            ledger.check(est_in)
        except E.BudgetExhausted as ex:
            errors.append(f"stopped: {ex}")
            for rest in todo[sent:]:
                rec = {"run_id": cfg["run_id"], "case_id": rest["case_id"], "status": "omitted-budget", "error": str(ex)}
                with open(outs["heldout"] if rest["split"] == "heldout" else outs["public_and_development"], "a") as f:
                    f.write(json.dumps(rec) + "\n")
            break
        retry = uncertain.get(c["case_id"], 0)
        while True:
            err, data, lat, req_id = None, None, None, None
            if a.mock:
                data, lat = mock_provider(cfg, msgs), 0.0
            else:
                try:
                    resp, lat = call_provider(cfg, key, msgs)
                except requests.RequestException as ex:
                    errors.append(f"uncertain request for {c['case_id']}: {type(ex).__name__}: {str(ex)[:300]}; stop for reconciliation")
                    uncertain[c["case_id"]] = uncertain.get(c["case_id"], 0) + 1
                    unc_path.write_text(json.dumps(uncertain, indent=2) + "\n")
                    write_checkpoint(outs["checkpoint"], a.phase, cfg, ledger, done, pending - done, errors, "reconcile uncertain request before replay")
                    return 2
                if resp.status_code == 200:
                    data = resp.json()
                    req_id = resp.headers.get("x-request-id") or data.get("id")
                else:
                    err = f"http {resp.status_code}: {resp.text[:200]}"
            if data is not None:
                u = normalize_usage(data["usage"])
                ledger.record(u, retry=retry > 0)
                ch = data["choices"][0]
                rec = {"run_id": cfg["run_id"], "case_id": c["case_id"], "status": "complete", "prompt_hash": E.prompt_hash(msgs),
                       "cache_key": E.cache_key(cfg, constitution_sha, c), "output": ch["message"]["content"], "finish_reason": ch.get("finish_reason"),
                       "request_id": req_id or data.get("id"), "usage": u, "retry_count": retry, "latency_s": round(lat, 2),
                       "estimated_cost_usd": round(E.usage_cost(u, cfg["prices"]), 6), "scores": {}, "grader": None, "error": None, "completed_at": now()}
                break
            ledger.record({}, retry=retry > 0, completed=False)
            if retry < cfg["caps"]["max_retries_per_item"] and resp.status_code in (429, 500, 502, 503):
                retry += 1
                try:
                    ledger.check(est_in)
                except E.BudgetExhausted:
                    rec = {"run_id": cfg["run_id"], "case_id": c["case_id"], "status": "failed", "error": err, "retry_count": retry - 1}
                    break
                time.sleep(2)
                continue
            rec = {"run_id": cfg["run_id"], "case_id": c["case_id"], "status": "failed", "error": err, "retry_count": retry}
            break
        with open(outs["heldout"] if c["split"] == "heldout" else outs["public_and_development"], "a") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        sent += 1
        if rec["status"] == "complete":
            done.add(c["case_id"])
        pending.discard(c["case_id"])
        if sent % 10 == 0:
            write_checkpoint(outs["checkpoint"], a.phase, cfg, ledger, done, pending, errors, f"continue phase {a.phase}")
    smoke_ids = {c["case_id"] for c in load_cases(cfg, "smoke")}
    smoke_ok = smoke_ids <= done
    cp = {"updated_at": now(), "phase": a.phase, "run_id": cfg["run_id"], "smoke_complete": smoke_ok, "completed_case_ids": sorted(done),
          "pending_case_ids": sorted(pending), "cumulative": ledger.to_dict(), "open_errors": errors,
          "next_action": "review smoke results, then run --phase rest" if a.phase == "smoke" else "score and report"}
    outs["checkpoint"].write_text(json.dumps(cp, indent=2) + "\n")
    outs["usage"].write_text(json.dumps(ledger.to_dict(), indent=2) + "\n")
    print(json.dumps(cp["cumulative"], indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
