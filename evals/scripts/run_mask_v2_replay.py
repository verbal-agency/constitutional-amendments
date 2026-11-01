#!/usr/bin/env python3
"""Run the approved MASK v2 judge replay on preserved outputs only."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import evalcore as E  # noqa: E402
import judge as J  # noqa: E402
import run_eval as R  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_MANIFEST = ROOT / "evals/manifests/g006-s3f-mask-v2-replay.json"
DEFAULT_APPROVAL = ROOT / "evals/runs/g006-s3f/judge-approval.json"
DEFAULT_OUT = ROOT / "evals/runs/g006-s3f/scores-v2.jsonl"


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def load_key() -> str | None:
    for name in ("DEEPSEEK_KEY",):
        if os.environ.get(name):
            return os.environ[name]
    env = ROOT / ".env"
    if env.exists():
        for line in env.read_text().splitlines():
            if line.startswith("DEEPSEEK_KEY="):
                return line.split("=", 1)[1].strip().strip("'\"")
    return None


def load_jsonl_row(path: Path, line_no: int) -> dict:
    rows = path.read_text().splitlines()
    if line_no < 1 or line_no > len(rows):
        raise ValueError(f"{path}: missing line {line_no}")
    return json.loads(rows[line_no - 1])


def answer_from_row(row: dict) -> str:
    answer = row.get("output") or row.get("answer") or ""
    if not answer:
        raise ValueError(f"{row.get('case_id')}: preserved row has no output")
    return answer


def load_case(manifest: dict) -> dict:
    case_id = manifest["case_id"]
    for line in (ROOT / "evals/cache/public-lean-v1.jsonl").read_text().splitlines():
        if line.strip():
            row = json.loads(line)
            if row.get("case_id") == case_id:
                return row
    raise ValueError(f"case not found in pinned public cache: {case_id}")


def build_case(case: dict) -> dict:
    ref = dict(case["reference"])
    ref["mask_v2"] = {
        "fact_status": "known_true",
        "disclosure_authority": "safe_to_disclose",
    }
    return {**case, "scorer": "judge:mask-honesty-v2", "reference": ref, "split": case.get("split", "public")}


def usage_cost(usage: dict, prices: dict) -> float:
    return E.usage_cost(usage, prices)


def call_once(cfg: dict, key: str, prompt: str) -> tuple[str, dict, float]:
    started = time.time()
    raw, usage = J.call_judge(cfg, key, prompt, "json", max_tokens=cfg["scoring"]["judge"]["max_tokens"])
    return raw, R.normalize_usage(usage), round(time.time() - started, 2)


def run(manifest_path: Path, approval_path: Path, output_path: Path) -> dict:
    manifest = json.loads(manifest_path.read_text())
    approval = json.loads(approval_path.read_text())
    if approval.get("manifest") != str(manifest_path.relative_to(ROOT)):
        raise ValueError("approval manifest does not match replay manifest")
    if approval.get("model") != "deepseek-v4-pro":
        raise ValueError("approval model does not match MASK v2 judge")
    if approval.get("max_calls") != 8 or approval.get("max_retries_per_item") != 1:
        raise ValueError("approval call/retry ceiling drift")
    ceiling = float(approval["ceiling_usd"])
    if ceiling > 0.10:
        raise ValueError("approval exceeds the S3F hard ceiling")

    import yaml
    cfg = yaml.safe_load((ROOT / "evals/configs/base-v1.yaml").read_text())
    cfg["scoring"]["judge"]["enabled"] = True
    cfg["scoring"]["judge"]["model"] = "deepseek-v4-pro"
    key = load_key()
    if not key:
        raise RuntimeError("DEEPSEEK_KEY is not available")
    case = build_case(load_case(manifest))
    prices = cfg["scoring"]["judge"]["prices"]
    records = []
    total_cost = 0.0
    calls = 0
    for arm in manifest["arms"]:
        preserved = load_jsonl_row(ROOT / arm["output_path"], arm["line"])
        answer = answer_from_row(preserved)
        if hashlib.sha256(answer.encode()).hexdigest() != arm["answer_sha256"]:
            raise ValueError(f"{arm['arm_id']}: answer hash drift")
        prompt, kind = J.build_judge_prompt(case, answer)
        attempts = []
        parsed = None
        last_error = None
        for attempt in range(1, 3):
            if calls >= int(approval["max_calls"]):
                raise RuntimeError("S3F call ceiling reached")
            estimated_next = (R.est_tokens(J.SYSTEM + prompt) * 1.15 * prices["input_cache_miss"] + cfg["scoring"]["judge"]["max_tokens"] * prices["output"]) / 1e6
            if total_cost + estimated_next > ceiling:
                raise RuntimeError(f"S3F dollar ceiling before {arm['arm_id']}: {total_cost + estimated_next:.6f}")
            raw, usage, latency = call_once(cfg, key, prompt)
            calls += 1
            cost = usage_cost(usage, prices)
            total_cost += cost
            parsed, last_error = J.parse_judge(raw, kind, case)
            attempts.append({"attempt": attempt, "usage": usage, "cost_usd": round(cost, 6), "raw": raw, "error": last_error, "latency_s": latency})
            if parsed is not None:
                break
        result = {
            "run_id": "g006-s3f-mask-v2",
            "goal_id": "G006-S3F",
            "arm_id": arm["arm_id"],
            "case_id": case["case_id"],
            "legacy_label": arm["legacy_label"],
            "answer_sha256": arm["answer_sha256"],
            "judge_model": cfg["scoring"]["judge"]["model"],
            "judge_prompt_hash": E.sha256_text(prompt),
            "status": "scored" if parsed is not None else "judge-failed",
            "parsed": parsed,
            "error": last_error if parsed is None else None,
            "attempts": len(attempts),
            "cost_usd": round(sum(item["cost_usd"] for item in attempts), 6),
            "attempt_detail": attempts,
            "scored_at": now(),
        }
        records.append(result)
        print(json.dumps({"arm_id": arm["arm_id"], "status": result["status"], "parsed": parsed, "cost_usd": result["cost_usd"]}), flush=True)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("".join(json.dumps(record, ensure_ascii=False) + "\n" for record in records))
    summary = {
        "run_id": "g006-s3f-mask-v2",
        "manifest": str(manifest_path.relative_to(ROOT)),
        "approval": str(approval_path.relative_to(ROOT)),
        "judge_model": cfg["scoring"]["judge"]["model"],
        "records": len(records),
        "calls": calls,
        "cost_usd": round(total_cost, 6),
        "ceiling_usd": ceiling,
        "target_model_generations": 0,
        "historical_scores_mutated": False,
        "output": str(output_path.relative_to(ROOT)),
        "completed_at": now(),
    }
    (output_path.parent / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--approval", type=Path, default=DEFAULT_APPROVAL)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--preflight", action="store_true")
    args = parser.parse_args()
    for attr in ("manifest", "approval", "output"):
        path = getattr(args, attr)
        if not path.is_absolute():
            setattr(args, attr, ROOT / path)
    if args.preflight:
        manifest = json.loads(args.manifest.read_text())
        approval = json.loads(args.approval.read_text())
        print(json.dumps({"arms": len(manifest["arms"]), "max_calls": approval["max_calls"], "ceiling_usd": approval["ceiling_usd"], "target_model_generations": 0}, indent=2))
        return 0
    try:
        print(json.dumps(run(args.manifest, args.approval, args.output), indent=2))
    except Exception as exc:
        print(f"MASK v2 replay failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
