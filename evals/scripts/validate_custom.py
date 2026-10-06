#!/usr/bin/env python3
"""Validate custom-v1 cases, verify content hashes, and optionally write the held-out manifest.

Usage:
  python3 evals/scripts/validate_custom.py                 # validate only
  python3 evals/scripts/validate_custom.py --write-manifest # also write evals/manifests/heldout-v1.json
"""
import argparse
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEV = ROOT / "evals/datasets/custom-dev-v1.jsonl"
HELD = ROOT / "evals/private/custom-heldout-v1.jsonl"
MANIFEST = ROOT / "evals/manifests/heldout-v1.json"

SCENARIOS = [f"SC-{i:03d}" for i in range(1, 11)]
DIMENSIONS = {"ER", "CAL", "CC", "AE", "DS", "UK", "IA", "AP", "SCX", "PS"}
CRITICAL = {f"CF-{i:02d}" for i in range(1, 14)}
RISK = {"low", "medium", "high"}
REQUIRED = [
    "case_id", "dataset_id", "source_item_id", "scenario_ids", "split", "system_context",
    "prompt", "evidence_packet", "reference", "expected_behaviors", "unacceptable_behaviors",
    "scoring_dimensions", "critical_failures", "risk_class", "max_output_tokens",
    "pattern_map", "content_hash",
]
MODEL_VISIBLE = ("system_context", "evidence_packet", "prompt")


def content_hash(record):
    body = dict(record)
    body["content_hash"] = ""
    blob = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()


def load(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def check_record(r, expected_split, errors):
    cid = r.get("case_id", "<missing>")
    for field in REQUIRED:
        if field not in r:
            errors.append(f"{cid}: missing field {field}")
    if errors and any(e.startswith(f"{cid}: missing") for e in errors):
        return
    if r["split"] != expected_split:
        errors.append(f"{cid}: split {r['split']} != {expected_split}")
    if len(r["scenario_ids"]) != 1 or r["scenario_ids"][0] not in SCENARIOS:
        errors.append(f"{cid}: bad scenario_ids {r['scenario_ids']}")
    if not set(r["scoring_dimensions"]) <= DIMENSIONS or not r["scoring_dimensions"]:
        errors.append(f"{cid}: bad scoring_dimensions {r['scoring_dimensions']}")
    if not set(r["critical_failures"]) <= CRITICAL or not r["critical_failures"]:
        errors.append(f"{cid}: bad critical_failures {r['critical_failures']}")
    if r["risk_class"] not in RISK:
        errors.append(f"{cid}: bad risk_class")
    if r["max_output_tokens"] > 600:
        errors.append(f"{cid}: max_output_tokens exceeds the 600-token plan cap")
    if not r["prompt"].strip() or not r["expected_behaviors"] or not r["unacceptable_behaviors"]:
        errors.append(f"{cid}: empty prompt or behavior lists")
    if r["content_hash"] != content_hash(r):
        errors.append(f"{cid}: content_hash mismatch")
    pm = r["pattern_map"]
    if pm is not None:
        for key in ("patterns", "legitimate_purpose", "limiting_behavior", "counterevidence"):
            if not pm.get(key):
                errors.append(f"{cid}: pattern_map missing {key}")


def check_split(records, split, errors):
    ids = [r["case_id"] for r in records]
    if len(ids) != len(set(ids)):
        errors.append(f"{split}: duplicate case_id")
    per = Counter(r["scenario_ids"][0] for r in records)
    want = 3 if split == "development" else 2
    for sc in SCENARIOS:
        if per[sc] != want:
            errors.append(f"{split}: {sc} has {per[sc]} cases, expected {want}")
    for r in records:
        check_record(r, split, errors)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write-manifest", action="store_true")
    args = ap.parse_args()
    errors = []
    dev = load(DEV)
    check_split(dev, "development", errors)
    held = load(HELD) if HELD.exists() else []
    if held:
        check_split(held, "heldout", errors)
        if {r["case_id"] for r in dev} & {r["case_id"] for r in held}:
            errors.append("case_id overlap between development and held-out")
    else:
        print("note: held-out file not present; skipping held-out checks")
    print(f"development={len(dev)} heldout={len(held)} errors={len(errors)}")
    for e in errors:
        print("ERROR", e)
    if errors:
        return 1
    if args.write_manifest and held:
        manifest = {
            "dataset_id": "custom-heldout-v1",
            "count": len(held),
            "per_scenario": dict(sorted(Counter(r["scenario_ids"][0] for r in held).items())),
            "hash_algorithm": "sha256 over canonical JSON with content_hash blanked",
            "cases": [{"case_id": r["case_id"], "scenario_id": r["scenario_ids"][0],
                       "content_hash": r["content_hash"]} for r in held],
            "plaintext_policy": "Plaintext prompts, rubrics, and outputs live only under ignored evals/private/.",
        }
        MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
        print(f"wrote {MANIFEST.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
