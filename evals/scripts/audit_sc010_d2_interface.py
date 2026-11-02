#!/usr/bin/env python3
"""Offline audit of the frozen SC-010-D2 model and judge interfaces."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import evalcore as E  # noqa: E402
import judge as J  # noqa: E402
import run_eval as R  # noqa: E402
import validate_custom as V  # noqa: E402
from render_candidate import render  # noqa: E402


ROOT = Path(__file__).resolve().parents[2]
MAPS = [
    ROOT / "evals/maps/g006-s5-factorial-00-base.json",
    ROOT / "evals/maps/g006-s5-factorial-10-map002-only.json",
    ROOT / "evals/maps/g006-s5-factorial-01-others-only.json",
    ROOT / "evals/maps/g006-replacement-v3.json",
]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output")
    args = ap.parse_args()
    cfg = R.load_cfg(ROOT / "evals/configs/base-v1.yaml")
    case = next(row for row in V.load(V.DEV) if row["case_id"] == "CUS-SC010-D2")
    source = (ROOT / "20260120-constitution.md").read_text(encoding="utf-8")
    judge_prompt, _ = J.build_judge_prompt(case, "Answer placeholder for interface audit.")
    result = {
        "contract": "sc010-d2-interface-v1",
        "case_id": case["case_id"],
        "case_content_hash": case["content_hash"],
        "packet_chars": len(case["evidence_packet"]),
        "packet_marker": "[Material attached to the user's message]",
        "prompt": case["prompt"],
        "judge_prompt_hash": E.sha256_text(judge_prompt),
        "arms": [],
    }
    for map_path in MAPS:
        spec = json.loads(map_path.read_text(encoding="utf-8"))
        candidate, assembly = render(source, spec)
        messages = E.build_messages(cfg, candidate, case)
        system, user = messages
        marker = result["packet_marker"]
        packet = case["evidence_packet"].strip()
        prompt = case["prompt"].strip()
        checks = {
            "system_role": system["role"] == "system",
            "user_role": user["role"] == "user",
            "marker_once": user["content"].count(marker) == 1,
            "packet_once": user["content"].count(packet) == 1,
            "prompt_once": user["content"].count(prompt) == 1,
            "prompt_after_packet": user["content"].rstrip().endswith(prompt),
            "packet_not_in_system": packet not in system["content"],
            "judge_has_packet": packet in judge_prompt,
            "judge_has_expected_behaviors": all(x in judge_prompt for x in case["expected_behaviors"]),
        }
        if not all(checks.values()):
            raise SystemExit(f"interface check failed for {map_path.name}: {checks}")
        result["arms"].append({
            "map_id": spec["map_id"],
            "map_path": str(map_path.relative_to(ROOT)),
            "candidate_sha256": assembly["candidate_sha256"],
            "model_prompt_hash": E.prompt_hash(messages),
            "user_chars": len(user["content"]),
            "checks": checks,
        })
    payload = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        output = Path(args.output) if Path(args.output).is_absolute() else ROOT / args.output
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(payload, encoding="utf-8")
    print(payload, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
