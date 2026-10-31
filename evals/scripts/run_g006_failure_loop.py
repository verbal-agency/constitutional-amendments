#!/usr/bin/env python3
"""Run a G006 focused failure loop with historical base reuse and two judges.

The target set is frozen in evals/manifests/g006-failure-loop-1.json. The base
arm is never regenerated. DeepSeek remains the primary judge; GPT-5.4 mini is
an independent secondary judge applied to both historical base and candidate.
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
import judge as J  # noqa: E402
import run_eval as R  # noqa: E402
from render_candidate import render as render_candidate  # noqa: E402
import score_run as S  # noqa: E402
import sources as SRC  # noqa: E402
from validate_custom import DEV, content_hash as custom_hash, load  # noqa: E402

ROOT = SRC.ROOT
TARGET_MANIFEST = ROOT / "evals/manifests/g006-failure-loop-1.json"
RUN = ROOT / "evals/runs/g006-failure-loop-1"
GEN_CEILING = 0.65
SECONDARY_CEILING = 0.60
PRIMARY_CEILING = 2.75
OPENAI_MODEL = "gpt-5.4-mini"
OPENAI_PRICES = {"input": 0.75, "cached_input": 0.075, "output": 4.50}


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def read_jsonl(path):
    if not path.exists():
        return {}
    return {r["case_id"]: r for r in (json.loads(x) for x in path.read_text().splitlines() if x.strip())}


def target_ids(spec):
    out = []
    for key in ("failure_cases", "mechanism_controls", "boundary_cases", "sentinels"):
        out.extend(spec[key])
    for pair in spec["identity_swapped_pairs"]:
        out.extend(pair)
    if len(out) != len(set(out)):
        raise SystemExit("target manifest contains duplicate case IDs")
    return out


def load_target_cases(cfg, spec):
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
    ids = target_ids(spec)
    missing = [x for x in ids if x not in by_id]
    if missing:
        raise SystemExit("target cases unavailable: " + ", ".join(missing))
    return [by_id[x] for x in ids]


def load_key(name, aliases=()):
    names = (name, *aliases)
    for candidate in names:
        if os.environ.get(candidate):
            return os.environ[candidate]
    p = ROOT / ".env"
    if p.exists():
        for line in p.read_text().splitlines():
            for candidate in names:
                if line.startswith(candidate + "="):
                    return line.split("=", 1)[1].strip().strip("'\"")
    return None


def openai_usage(u):
    details = u.get("prompt_tokens_details") or {}
    hit = details.get("cached_tokens", 0)
    prompt = u.get("prompt_tokens", hit)
    miss = max(0, prompt - hit)
    completion = u.get("completion_tokens", 0)
    return {"prompt_tokens": prompt, "completion_tokens": completion, "cache_hit": hit, "cache_miss": miss}


def openai_cost(u):
    return (u["cache_hit"] * OPENAI_PRICES["cached_input"] + u["cache_miss"] * OPENAI_PRICES["input"] + u["completion_tokens"] * OPENAI_PRICES["output"]) / 1e6


def call_openai(key, prompt, max_completion_tokens=1200):
    body = {
        "model": OPENAI_MODEL,
        "messages": [{"role": "system", "content": J.SYSTEM}, {"role": "user", "content": prompt}],
        "max_completion_tokens": max_completion_tokens,
        "reasoning_effort": "low",
        "response_format": {"type": "json_object"},
    }
    t0 = time.time()
    response = requests.post("https://api.openai.com/v1/chat/completions", json=body,
                             headers={"Authorization": f"Bearer {key}"}, timeout=300)
    response.raise_for_status()
    data = response.json()
    return data, round(time.time() - t0, 2)


def secondary_judge_one(cfg, key, case, answer):
    if case.get("scorer") == E.LETTER_SCORER:
        return {"case_id": case["case_id"], "status": "skipped-deterministic", "kind": "letter", "judge_model": OPENAI_MODEL}
    prompt, kind = J.build_judge_prompt(case, answer)
    attempts = []
    for attempt, max_tokens in enumerate((1200, 2400), 1):
        data, latency = call_openai(key, prompt, max_tokens)
        usage = openai_usage(data.get("usage", {}))
        raw = data.get("choices", [{}])[0].get("message", {}).get("content", "")
        parsed, error = J.parse_judge(raw, kind, case)
        attempts.append({"attempt": attempt, "usage": usage, "cost_usd": round(openai_cost(usage), 6),
                         "raw": raw, "error": error, "latency_s": latency})
        if parsed is not None:
            return {"case_id": case["case_id"], "status": "scored", "kind": kind, "judge_model": OPENAI_MODEL,
                    "judge_prompt_hash": E.sha256_text(prompt), "parsed": parsed, "raw": raw,
                    "attempts": attempt, "cost_usd": round(sum(x["cost_usd"] for x in attempts), 6),
                    "attempt_detail": attempts, "scored_at": now()}
    last = attempts[-1]
    return {"case_id": case["case_id"], "status": "judge-failed", "kind": kind, "judge_model": OPENAI_MODEL,
            "judge_prompt_hash": E.sha256_text(prompt), "raw": last["raw"], "error": last["error"],
            "attempts": len(attempts), "cost_usd": round(sum(x["cost_usd"] for x in attempts), 6),
            "attempt_detail": attempts, "scored_at": now()}


def historical_primary_ledger(cfg):
    ledger = S.JudgeLedger(PRIMARY_CEILING, cfg["scoring"]["judge"]["prices"], cfg["scoring"]["judge"]["max_tokens"])
    prior_metrics = json.loads((ROOT / "evals/runs/base-v1/metrics.json").read_text())
    ledger.cost = float(prior_metrics["judge"]["cost_usd"])
    ledger.calls = int(prior_metrics["judge"]["calls"])
    paths = [ROOT / "evals/runs/g006-iteration-140/scores-base.jsonl",
             ROOT / "evals/runs/g006-iteration-140/scores-g006-draft.jsonl",
             ROOT / "evals/runs/g006-iteration-2-targeted/scores.jsonl"]
    calls, cost = S.append_only_stats([p for p in paths if p.exists()])
    ledger.calls += calls
    ledger.cost += cost
    return ledger


def preflight(cfg, cases, candidate_text):
    draft = candidate_text
    inputs = [R.est_tokens("".join(m["content"] for m in E.build_messages(cfg, draft, c))) for c in cases]
    non_letter = [c for c in cases if c.get("scorer") != E.LETTER_SCORER]
    # Judge prompts use the historical base outputs as a conservative proxy.
    base_out = read_jsonl(ROOT / "evals/runs/base-v1/outputs.jsonl")
    judge_inputs = []
    for c in non_letter:
        prompt, _ = J.build_judge_prompt(c, base_out[c["case_id"]]["output"])
        judge_inputs.append(R.est_tokens(J.SYSTEM + prompt))
    gen_worst = (sum(inputs) * 1.15 * cfg["prices"]["input_cache_miss"] + len(cases) * 600 * cfg["prices"]["output"]) / 1e6
    primary_worst = (sum(judge_inputs) * 1.15 * cfg["scoring"]["judge"]["prices"]["input_cache_miss"] + len(non_letter) * 4000 * cfg["scoring"]["judge"]["prices"]["output"]) / 1e6
    secondary_worst = (2 * sum(judge_inputs) * 1.15 * OPENAI_PRICES["input"] + 2 * len(non_letter) * 1200 * OPENAI_PRICES["output"]) / 1e6
    return {"cases": len(cases), "non_letter_cases": len(non_letter), "generation_input_tokens": sum(inputs),
            "judge_input_tokens_one_arm": sum(judge_inputs), "generation_worst_usd": round(gen_worst, 4),
            "primary_new_worst_usd": round(primary_worst, 4), "secondary_both_arms_worst_usd": round(secondary_worst, 4),
            "total_new_worst_usd": round(gen_worst + primary_worst + secondary_worst, 4),
            "generation_ceiling_usd": GEN_CEILING, "primary_cumulative_ceiling_usd": PRIMARY_CEILING,
            "secondary_ceiling_usd": SECONDARY_CEILING, "historical_primary_ledger": historical_primary_ledger(cfg).cost}


def main():
    global TARGET_MANIFEST, RUN
    ap = argparse.ArgumentParser()
    ap.add_argument("--preflight", action="store_true")
    ap.add_argument("--target-manifest", default=str(TARGET_MANIFEST))
    ap.add_argument("--run-dir", default=str(RUN))
    ap.add_argument("--candidate-map", default=str(ROOT / "evals/maps/g006-replacement-v1.json"))
    args = ap.parse_args()
    TARGET_MANIFEST = Path(args.target_manifest)
    if not TARGET_MANIFEST.is_absolute():
        TARGET_MANIFEST = ROOT / TARGET_MANIFEST
    RUN = Path(args.run_dir)
    if not RUN.is_absolute():
        RUN = ROOT / RUN
    cfg = R.load_cfg(ROOT / "evals/configs/base-v1.yaml")
    spec = json.loads(TARGET_MANIFEST.read_text())
    run_id = spec.get("run_id", RUN.name)
    revision_label = spec.get("candidate_arm", "g006-revision-4")
    map_path = Path(args.candidate_map)
    if not map_path.is_absolute():
        map_path = ROOT / map_path
    source = (ROOT / "20260120-constitution.md").read_text()
    map_text = map_path.read_text()
    map_spec = json.loads(map_text)
    map_sha256 = E.sha256_text(map_text)
    candidate_text, candidate_assembly = render_candidate(source, map_spec)
    cases = load_target_cases(cfg, spec)
    pf = preflight(cfg, cases, candidate_text)
    if args.preflight:
        print(json.dumps(pf, indent=2))
        return 0
    deepseek = load_key("DEEPSEEK_KEY")
    openai = load_key("OPENAI_API_KEY", aliases=("OPEN_AI_KEY",))
    if not deepseek or not openai:
        raise SystemExit("DEEPSEEK_KEY and OPENAI_API_KEY are required")
    RUN.mkdir(parents=True, exist_ok=True)
    (RUN / "raw").mkdir(parents=True, exist_ok=True)
    draft = candidate_text
    (RUN / "candidate-constitution.md").write_text(candidate_text, encoding="utf-8")
    (RUN / "candidate-assembly.json").write_text(json.dumps({**candidate_assembly, "map_path": str(map_path.relative_to(ROOT)), "map_sha256": map_sha256}, indent=2) + "\n", encoding="utf-8")
    raw_path = RUN / f"raw/{revision_label}.jsonl"
    candidate = read_jsonl(raw_path)
    gen_ledger = E.BudgetLedger(GEN_CEILING, len(cases), cfg["decoding"]["max_tokens"], cfg["prices"])
    for rec in candidate.values():
        gen_ledger.record(rec.get("usage", {}))
    for case in cases:
        cid = case["case_id"]
        if cid in candidate:
            continue
        messages = E.build_messages(cfg, draft, case)
        gen_ledger.check(R.est_tokens("".join(m["content"] for m in messages)))
        print(f"generate {cid}", flush=True)
        response, latency = R.call_provider(cfg, deepseek, messages)
        response.raise_for_status()
        data = response.json()
        usage = R.normalize_usage(data.get("usage", {}))
        gen_ledger.record(usage)
        rec = {"run_id": run_id, "arm": revision_label, "case_id": cid,
               "status": "complete", "output": data["choices"][0]["message"]["content"],
               "finish_reason": data["choices"][0].get("finish_reason"), "request_id": data.get("id"),
               "usage": usage, "estimated_cost_usd": round(E.usage_cost(usage, cfg["prices"]), 6),
               "latency_s": latency, "completed_at": now()}
        with raw_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        candidate[cid] = rec

    base_out = read_jsonl(ROOT / "evals/runs/base-v1/outputs.jsonl")
    base_scores = read_jsonl(ROOT / "evals/runs/base-v1/scores.jsonl")
    primary_scores = read_jsonl(RUN / "scores-primary.jsonl")
    primary_ledger = historical_primary_ledger(cfg)
    for case in cases:
        cid = case["case_id"]
        if case.get("scorer") == E.LETTER_SCORER or primary_scores.get(cid, {}).get("status") == "scored":
            continue
        local = S.JudgeLedger(1e9, cfg["scoring"]["judge"]["prices"], cfg["scoring"]["judge"]["max_tokens"])
        rec = S.judge_one(cfg, deepseek, case, candidate[cid]["output"], local, False)
        primary_scores[cid] = rec
        primary_ledger.calls += int(rec.get("attempts", 1))
        primary_ledger.cost += float(rec.get("cost_usd", 0.0))
        with (RUN / "scores-primary.jsonl").open("a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        print(f"primary judge {cid} cumulative=${primary_ledger.cost:.6f}", flush=True)
        if primary_ledger.cost >= PRIMARY_CEILING:
            raise SystemExit("primary judge cumulative ceiling reached")

    secondary_base = read_jsonl(RUN / "scores-secondary-base.jsonl")
    secondary_candidate = read_jsonl(RUN / "scores-secondary-candidate.jsonl")
    secondary_cost = sum(float(x.get("cost_usd", 0.0)) for x in list(secondary_base.values()) + list(secondary_candidate.values()))
    for arm, outputs, scores, path in [("base", base_out, secondary_base, RUN / "scores-secondary-base.jsonl"),
                                       ("candidate", candidate, secondary_candidate, RUN / "scores-secondary-candidate.jsonl")]:
        for case in cases:
            cid = case["case_id"]
            if scores.get(cid, {}).get("status") in ("scored", "skipped-deterministic"):
                continue
            rec = secondary_judge_one(cfg, openai, case, outputs[cid]["output"])
            scores[cid] = rec
            secondary_cost += float(rec.get("cost_usd", 0.0))
            with path.open("a", encoding="utf-8") as f:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            print(f"secondary judge {arm} {cid} cumulative=${secondary_cost:.6f}", flush=True)
            if secondary_cost >= SECONDARY_CEILING:
                raise SystemExit("secondary judge ceiling reached")

    results = []
    for case in cases:
        cid = case["case_id"]
        results.append({"case_id": cid, "scorer": case.get("scorer"),
                        "base_primary": S.case_result(case, base_out.get(cid), base_scores.get(cid)),
                        "candidate_primary": S.case_result(case, candidate.get(cid), primary_scores.get(cid)),
                        "base_secondary": S.case_result(case, base_out.get(cid), secondary_base.get(cid)),
                        "candidate_secondary": S.case_result(case, candidate.get(cid), secondary_candidate.get(cid))})
    report = {"run_id": run_id, "candidate_arm": revision_label, "generated_at": now(), "target_manifest": str(TARGET_MANIFEST.relative_to(ROOT)),
              "candidate_assembly": {**candidate_assembly, "map_path": str(map_path.relative_to(ROOT)), "map_sha256": map_sha256},
              "cases": target_ids(spec), "preflight": pf,
              "generation": {"model": cfg["provider"]["model"], "calls": gen_ledger.attempts, "cost_usd": round(gen_ledger.cost, 6)},
              "primary": {"model": cfg["scoring"]["judge"]["model"], "cumulative_calls": primary_ledger.calls, "cumulative_cost_usd": round(primary_ledger.cost, 6)},
              "secondary": {"model": OPENAI_MODEL, "calls": sum(int(x.get("attempts", 1)) for x in list(secondary_base.values()) + list(secondary_candidate.values())),
                            "cost_usd": round(secondary_cost, 6), "both_arms": True},
              "results": results}
    (RUN / "manifest.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "complete", "generation_cost_usd": round(gen_ledger.cost, 6),
                      "primary_cumulative_cost_usd": round(primary_ledger.cost, 6),
                      "secondary_cost_usd": round(secondary_cost, 6), "cases": len(cases)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
