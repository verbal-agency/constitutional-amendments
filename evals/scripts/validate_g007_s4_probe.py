#!/usr/bin/env python3
"""Validate the offline G007-S4 development packet.

This checks packet integrity only. It never calls a model, reads held-out data,
or scores an output.
"""
from __future__ import annotations

import hashlib
import json
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PACKET = ROOT / "evals/manifests/g007-s4-development-probe.json"
SOURCE = ROOT / "20260120-constitution.md"
DEV = ROOT / "evals/datasets/custom-dev-v1.jsonl"
EXPECTED_SHA = "251440a71a9068dd43bfaab2b8694d6e2a4f519c403f1b9a70785f830d05f327"
FAMILIES = {
    "F-INQUIRY",
    "F-SELF-REGARDING",
    "F-PRIVACY",
    "F-OPERATIONAL",
    "F-EMERGENCY",
}


def fail(message: str) -> None:
    raise SystemExit(f"ERROR {message}")


def main() -> int:
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    source_sha = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    if source_sha != EXPECTED_SHA or packet["source"]["constitution_sha256"] != EXPECTED_SHA:
        fail("constitution source hash drift")
    if packet["manifest_id"] != "g007-s4-development-probe-v1":
        fail("unexpected manifest_id")
    if packet["goal_id"] != "G007-S4" or packet["split"] != "development":
        fail("wrong goal or split")
    boundary = packet["execution_boundary"]
    for key in ("model_call", "paid_call", "network_access", "heldout_access", "official_g010_claim", "candidate_integration"):
        if boundary.get(key) is not False:
            fail(f"execution boundary {key} must be false")
    families = {f["family_id"] for f in packet["families"]}
    if families != FAMILIES:
        fail(f"family set mismatch: {sorted(families)}")
    if len(packet["families"]) != len(FAMILIES):
        fail("duplicate family record")

    dev = {
        json.loads(line)["case_id"]: json.loads(line)
        for line in DEV.read_text(encoding="utf-8").splitlines()
        if line.strip()
    }
    cases = packet["cases"]
    ids = [c.get("case_id") for c in cases]
    if len(cases) != 15 or len(ids) != len(set(ids)):
        fail("packet must contain 15 unique cases")
    pair_cases = [c for c in cases if c.get("role") == "paired"]
    sentinels = [c for c in cases if c.get("role") == "sentinel"]
    if len(pair_cases) != 10 or len(sentinels) != 5:
        fail("packet must contain ten paired cases and five sentinels")
    pair_counts = Counter(c.get("pair_id") for c in pair_cases)
    if set(pair_counts) != {"P-INQ-01", "P-SELF-01", "P-PRIV-01", "P-OPS-01", "P-EMERG-01"} or any(v != 2 for v in pair_counts.values()):
        fail(f"each pair must have exactly two cases: {pair_counts}")
    sentinel_families = Counter(c["family_id"] for c in sentinels)
    if set(sentinel_families) != FAMILIES or any(v != 1 for v in sentinel_families.values()):
        fail(f"each family needs one sentinel: {sentinel_families}")

    for case in cases:
        required = ("case_id", "family_id", "role", "case_shape", "risk_class", "expected_transition", "failure_class", "source_refs", "preserved_purpose")
        missing = [key for key in required if key not in case]
        if missing:
            fail(f"{case.get('case_id')}: missing {missing}")
        if case["family_id"] not in FAMILIES:
            fail(f"{case['case_id']}: unknown family")
        if case.get("split", "development") != "development":
            fail(f"{case['case_id']}: non-development split")
        if not case["source_refs"] or not case["failure_class"] or not case["preserved_purpose"]:
            fail(f"{case['case_id']}: missing provenance or interpretation fields")
        if set(case["expected_transition"]) != {"base", "candidate"}:
            fail(f"{case['case_id']}: expected_transition must name base and candidate")
        if "prompt" not in case and "source_case_ref" not in case:
            fail(f"{case['case_id']}: no prompt or source case reference")
        if "source_case_ref" in case:
            ref = case["source_case_ref"]
            if ref.get("dataset") != "custom-dev-v1" or ref.get("case_id") not in dev:
                fail(f"{case['case_id']}: invalid source case reference")
        forbidden = {"output", "judge_result", "model_response", "heldout_output"} & set(case)
        if forbidden:
            fail(f"{case['case_id']}: packet contains outputs {sorted(forbidden)}")

    if packet["cost_preflight"]["maximum_generations"] != 30:
        fail("cost preflight must cap this packet at 30 generations")
    print("PASS G007-S4 packet=15 paired=10 sentinels=5 families=5 model_call=false heldout=false")
    return 0


if __name__ == "__main__":
    sys.exit(main())
