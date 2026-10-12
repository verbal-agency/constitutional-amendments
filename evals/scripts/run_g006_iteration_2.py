#!/usr/bin/env python3
"""Run and score the bounded G006 revision-2 candidate probe.

Only public and tracked development cases are loaded. Historical base-v1
outputs/scores are reused as the control; the base arm is never regenerated.
"""
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import evalcore as E  # noqa: E402
import run_eval as R  # noqa: E402
import score_run as S  # noqa: E402
import sources as SRC  # noqa: E402
from validate_custom import DEV, content_hash as custom_hash, load  # noqa: E402

ROOT = SRC.ROOT
RUN = ROOT / "evals/runs/g006-iteration-2-targeted"
TARGET_IDS = [
    "CUS-SC007-D1", "CUS-SC007-D2", "CUS-SC007-D3",
    "CUS-SC010-D1", "CUS-SC010-D2", "CUS-SC010-D3",
    "CUS-SC003-D1", "CUS-SC003-D2", "CUS-SC003-D3",
    "CUS-SC006-D1", "CUS-SC006-D2", "CUS-SC006-D3",
    "mask:provided_facts:67ab8fa8461eb193ef95b421",
    "freshqa:id-0214", "xstest:id-283",
    "sycophancy-philpapers2020:row-03749",
    "sycophancy-philpapers2020:row-03776",
    "sycophancy-philpapers2020:row-04541",
    "sycophancy-philpapers2020:row-04515",
]
GEN_CEILING = 0.30
JUDGE_CEILING = 2.75


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def load_target_cases(cfg):
    manifest = [json.loads(x) for x in (ROOT / cfg["dataset_manifest"]["lean"]).read_text().splitlines() if x.strip()]
    public = {c["case_id"]: c for c in map(json.loads, (ROOT / "evals/cache/public-lean-v1.jsonl").read_text().splitlines())}
    development = {r["case_id"]: r for r in load(DEV)}
    sources = {"public": public, "development": development}
    by_id = {}
    for entry in manifest:
        if entry["split"] not in sources:
            continue
        c = sources[entry["split"]].get(entry["case_id"])
        if c is None:
            continue
        expected = E.case_hash(c) if entry["split"] == "public" else custom_hash(c)
        if expected != entry["content_hash"] or c["content_hash"] != entry["content_hash"]:
            raise SystemExit(f"content hash drift for {entry['case_id']}")
        by_id[c["case_id"]] = {**c, "in_smoke": entry["in_smoke"]}
    missing = [x for x in TARGET_IDS if x not in by_id]
    if missing:
        raise SystemExit("target cases unavailable: " + ", ".join(missing))
    return [by_id[x] for x in TARGET_IDS]


def read_jsonl(path):
    if not path.exists():
        return {}
    return {r["case_id"]: r for r in (json.loads(x) for x in path.read_text().splitlines() if x.strip())}


def main():
    cfg = R.load_cfg(ROOT / "evals/configs/base-v1.yaml")
    cases = load_target_cases(cfg)
    source = (ROOT / "20260120-constitution.md").read_text()
    draft = source + "\n\n--- G006 REVISION 2 ---\n\n" + (ROOT / "amendments/G006-authority-and-incentives.md").read_text()
    RUN.mkdir(parents=True, exist_ok=True)
    raw = RUN / "raw/g006-revision-2.jsonl"
    raw.parent.mkdir(parents=True, exist_ok=True)
    existing = read_jsonl(raw)
    key = R.load_env_key()
    if not key:
        raise SystemExit("DEEPSEEK_KEY is unavailable")
    gledger = E.BudgetLedger(GEN_CEILING, len(cases), cfg["decoding"]["max_tokens"], cfg["prices"])
    for rec in existing.values():
        gledger.record(rec.get("usage", {}))
    for case in cases:
        if case["case_id"] in existing:
            continue
        messages = E.build_messages(cfg, draft, case)
        gledger.check(R.est_tokens("".join(m["content"] for m in messages)))
        print(f"generate {case['case_id']}", flush=True)
        response, latency = R.call_provider(cfg, key, messages)
        if response.status_code != 200:
            raise SystemExit(f"generation HTTP {response.status_code}: {response.text[:300]}")
        data = response.json()
        usage = R.normalize_usage(data.get("usage", {}))
        gledger.record(usage)
        rec = {"run_id": "g006-iteration-2-targeted", "arm": "g006-revision-2", "case_id": case["case_id"],
               "status": "complete", "output": data["choices"][0]["message"]["content"],
               "finish_reason": data["choices"][0].get("finish_reason"), "request_id": data.get("id"),
               "usage": usage, "estimated_cost_usd": round(E.usage_cost(usage, cfg["prices"]), 6),
               "latency_s": latency, "completed_at": now()}
        with raw.open("a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        existing[case["case_id"]] = rec

    base_out = read_jsonl(ROOT / "evals/runs/base-v1/outputs.jsonl")
    base_scores = read_jsonl(ROOT / "evals/runs/base-v1/scores.jsonl")
    candidate_scores = read_jsonl(RUN / "scores.jsonl")
    prior_metrics = json.loads((ROOT / "evals/runs/base-v1/metrics.json").read_text())
    ledger = S.JudgeLedger(JUDGE_CEILING, cfg["scoring"]["judge"]["prices"], cfg["scoring"]["judge"]["max_tokens"])
    ledger.cost = float(prior_metrics["judge"]["cost_usd"])
    ledger.calls = int(prior_metrics["judge"]["calls"])
    prior140 = ROOT / "evals/runs/g006-iteration-140"
    for p in [prior140 / "scores-base.jsonl", prior140 / "scores-g006-draft.jsonl"]:
        if p.exists():
            calls, cost = S.append_only_stats([p])
            ledger.calls += calls
            ledger.cost += cost
    for case in cases:
        cid = case["case_id"]
        if case.get("scorer") == E.LETTER_SCORER or candidate_scores.get(cid, {}).get("status") == "scored":
            continue
        local = S.JudgeLedger(1e9, cfg["scoring"]["judge"]["prices"], cfg["scoring"]["judge"]["max_tokens"])
        rec = S.judge_one(cfg, key, case, existing[cid]["output"], local, False)
        candidate_scores[cid] = rec
        ledger.calls += int(rec.get("attempts", 1))
        ledger.cost += float(rec.get("cost_usd", 0.0))
        with (RUN / "scores.jsonl").open("a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        print(f"judge {cid} total=${ledger.cost:.6f}", flush=True)
        if ledger.cost >= JUDGE_CEILING:
            raise SystemExit("judge ceiling reached")

    results = []
    for case in cases:
        cid = case["case_id"]
        cand = S.case_result(case, existing.get(cid), candidate_scores.get(cid))
        base = S.case_result(case, base_out.get(cid), base_scores.get(cid))
        results.append({"case_id": cid, "scorer": case.get("scorer"), "base": base, "candidate": cand,
                        "base_output": base_out.get(cid, {}).get("output"), "candidate_output": existing.get(cid, {}).get("output")})
    report = {"run_id": "g006-iteration-2-targeted", "generated_at": now(), "cases": TARGET_IDS,
              "generation": {"model": cfg["provider"]["model"], "cost_usd": round(gledger.cost, 6), "calls": gledger.attempts, "ceiling_usd": GEN_CEILING},
              "judge": {"model": cfg["scoring"]["judge"]["model"], "cumulative_cost_usd": round(ledger.cost, 6), "cumulative_calls": ledger.calls, "ceiling_usd": JUDGE_CEILING},
              "historical_base_reused": True, "results": results}
    (RUN / "manifest.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "complete", "generation_cost_usd": round(gledger.cost, 6), "judge_cumulative_cost_usd": round(ledger.cost, 6), "cases": len(cases)}, indent=2))


if __name__ == "__main__":
    main()
