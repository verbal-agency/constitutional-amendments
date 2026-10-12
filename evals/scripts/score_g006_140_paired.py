#!/usr/bin/env python3
"""Score the paired, non-held-out G006 140-case development run.

Both arms share one judge ledger so the existing DeepSeek judge authorization
is treated as a real shared ceiling.  The script is resumable: completed judge
records are kept per arm in the run directory and are never called again.
This is exploratory evidence for G006, not the official G010 evaluation.
"""
import argparse
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
import evalcore as E  # noqa: E402
import judge as J  # noqa: E402
import run_eval as R  # noqa: E402
import score_run as S  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
RUN_DIR = ROOT / "evals/runs/g006-iteration-140"


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def read_jsonl(path):
    if not path.exists():
        return {}
    return R.read_records(path)


def write_metrics(cfg, arm, cases, outs, scores, ledger, stop_reason=None):
    results = {}
    for case in cases:
        result = S.case_result(case, outs.get(case["case_id"]), scores.get(case["case_id"]))
        if result is not None:
            results[case["case_id"]] = result
    metrics, custom, diagnostics = S.build_metrics(cases, results)
    failed = sorted(i for i, rec in scores.items() if rec.get("status") == "judge-failed")
    output = {
        "run_id": f"g006-iteration-140-{arm}",
        "arm": arm,
        "generated_at": now(),
        "model": cfg["provider"]["model"],
        "judge": {"model": cfg["scoring"]["judge"]["model"], "enabled": True, "mock": False,
                  "judge_failed_cases": failed, "calls": ledger.calls, "cost_usd": round(ledger.cost, 6),
                  "shared_ceiling_usd": ledger.ceiling, "stop_reason": stop_reason},
        "metrics": metrics,
        "custom": custom,
        "diagnostics": diagnostics,
        "spot_check": S.pick_spot_check(cases, results),
        "items_development_and_public": S.item_table(cases, results, False),
        "note": "Exploratory paired G006 development evidence; held-out cases excluded and no composite score is canonical.",
    }
    path = RUN_DIR / f"metrics-{arm}.json"
    path.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n")
    return output


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ceiling", type=float, default=3.0,
                        help="shared approved judge ceiling, including prior base-v1 usage")
    args = parser.parse_args()

    cfg = R.load_cfg(ROOT / "evals/configs/base-v1.yaml")
    cases = [case for case in R.load_cases(cfg, "all") if case["split"] != "heldout"]
    if len(cases) != 140:
        raise SystemExit(f"expected 140 non-held-out cases, found {len(cases)}")
    approval = json.loads((ROOT / "evals/runs/base-v1/judge-approval.json").read_text())
    if approval.get("model") != cfg["scoring"]["judge"]["model"]:
        raise SystemExit("judge approval model does not match config")
    if args.ceiling > float(approval["ceiling_usd"]):
        raise SystemExit("requested ceiling exceeds approved ceiling")
    token = R.load_env_key()
    if not token:
        raise SystemExit("DEEPSEEK_KEY is unavailable")

    prior_metrics = json.loads((ROOT / "evals/runs/base-v1/metrics.json").read_text())
    prior_cost = float(prior_metrics["judge"]["cost_usd"])
    prior_calls = int(prior_metrics["judge"]["calls"])
    ledger = S.JudgeLedger(args.ceiling, cfg["scoring"]["judge"]["prices"], cfg["scoring"]["judge"]["max_tokens"])
    ledger.cost = prior_cost
    ledger.calls = prior_calls

    arms = {"base": RUN_DIR / "raw/base.jsonl", "g006-draft": RUN_DIR / "raw/g006-draft.jsonl"}
    scores_by_arm = {arm: read_jsonl(RUN_DIR / f"scores-{arm}.jsonl") for arm in arms}
    outs_by_arm = {arm: read_jsonl(path) for arm, path in arms.items()}
    # Include every prior paid attempt in this exploratory run, including
    # malformed responses that were later retried.  This keeps resume runs'
    # shared ledger and reported spend append-only.
    prior_score_calls, prior_score_cost = S.append_only_stats(
        [RUN_DIR / f"scores-{arm}.jsonl" for arm in arms]
    )
    ledger.calls += prior_score_calls
    ledger.cost += prior_score_cost
    for arm in arms:
        write_metrics(cfg, arm, cases, outs_by_arm[arm], scores_by_arm[arm], ledger)

    non_letter = [case for case in cases if case.get("scorer") != E.LETTER_SCORER]
    tasks = []
    for arm in arms:
        for case in non_letter:
            case_id = case["case_id"]
            output = outs_by_arm[arm].get(case_id)
            if output and output.get("status") == "complete" and scores_by_arm[arm].get(case_id, {}).get("status") != "scored":
                tasks.append((arm, case))

    def grade_one(arm, case):
        # Each worker has a local ledger; the main thread owns the shared ledger.
        local = S.JudgeLedger(1e9, cfg["scoring"]["judge"]["prices"], cfg["scoring"]["judge"]["max_tokens"])
        boost = cfg["scoring"]["judge"].get("retry_max_tokens") if scores_by_arm[arm].get(case["case_id"], {}).get("status") == "judge-failed" else None
        rec = S.judge_one(cfg, token, case, outs_by_arm[arm][case["case_id"]]["output"], local, False, boost=boost)
        return arm, case, rec

    # Thinking-mode grading is latency-bound. Keep a small bounded pool while
    # persisting each completed result and retaining the shared dollar ledger.
    workers = 6
    pending = iter(tasks)
    inflight = {}
    stop_reason = None
    with ThreadPoolExecutor(max_workers=workers) as pool:
        for _ in range(min(workers, len(tasks))):
            try:
                arm, case = next(pending)
            except StopIteration:
                break
            inflight[pool.submit(grade_one, arm, case)] = (arm, case)
        while inflight:
            done, _ = wait(inflight, return_when=FIRST_COMPLETED)
            for future in done:
                arm, case = inflight.pop(future)
                case_id = case["case_id"]
                try:
                    arm, case, rec = future.result()
                except requests.RequestException as exc:
                    stop_reason = f"uncertain judge request for {case_id}: {type(exc).__name__}; resume for reconciliation"
                    print(stop_reason, flush=True)
                    continue
                except Exception as exc:  # pragma: no cover - preserves resumability for provider edge cases
                    stop_reason = f"judge worker failed for {case_id}: {type(exc).__name__}: {exc}"
                    print(stop_reason, flush=True)
                    continue
                scores_by_arm[arm][case_id] = rec
                ledger.calls += int(rec.get("attempts", 1))
                ledger.cost += float(rec.get("cost_usd", 0.0))
                score_path = RUN_DIR / f"scores-{arm}.jsonl"
                with score_path.open("a", encoding="utf-8") as handle:
                    handle.write(json.dumps(rec, ensure_ascii=False) + "\n")
                print(f"scored {arm} {case_id} (total judge ${ledger.cost:.4f})", flush=True)
                for a in arms:
                    write_metrics(cfg, a, cases, outs_by_arm[a], scores_by_arm[a], ledger, stop_reason)
                if stop_reason:
                    continue
                # Do not submit new calls after the hard ceiling is reached.
                if ledger.cost >= ledger.ceiling:
                    stop_reason = "judge-dollar-ceiling"
                    continue
                try:
                    next_arm, next_case = next(pending)
                except StopIteration:
                    continue
                inflight[pool.submit(grade_one, next_arm, next_case)] = (next_arm, next_case)
            if stop_reason:
                for future in inflight:
                    future.cancel()
                break

    if stop_reason:
        for a in arms:
            write_metrics(cfg, a, cases, outs_by_arm[a], scores_by_arm[a], ledger, stop_reason)
        return 1

    for arm in arms:
        write_metrics(cfg, arm, cases, outs_by_arm[arm], scores_by_arm[arm], ledger)
    print(json.dumps({"status": "complete", "judge_calls_total": ledger.calls,
                      "judge_cost_total_usd": round(ledger.cost, 6),
                      "new_judge_cost_usd": round(ledger.cost - prior_cost, 6),
                      "metrics": [str(RUN_DIR / f"metrics-{arm}.json") for arm in arms]}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
