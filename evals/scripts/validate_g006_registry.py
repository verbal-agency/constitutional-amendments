#!/usr/bin/env python3
"""Validate the G006 semantic principle registry and its canonical map links."""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "framework/principles-v1.yaml"
MAP = ROOT / "evals/maps/g006-replacement-v3.json"
SOURCE = ROOT / "20260120-constitution.md"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def main() -> int:
    registry = yaml.safe_load(REGISTRY.read_text())
    mapping = json.loads(MAP.read_text())

    if registry.get("schema_version") != "principles-v1":
        fail("unexpected registry schema version")
    if registry.get("owner_goal") != "G006":
        fail("registry owner must be G006")
    if registry["source"]["constitution_sha256"] != sha256(SOURCE):
        fail("immutable constitution hash drift")
    if mapping.get("source_sha256") != registry["source"]["constitution_sha256"]:
        fail("map and registry source hashes differ")
    if mapping.get("principle_registry") != "framework/principles-v1.yaml":
        fail("canonical map does not point to the registry")

    principles = registry.get("principles")
    if not isinstance(principles, list) or len(principles) != 7:
        fail("registry must contain exactly seven G006 principles")
    ids = [p.get("principle_id") for p in principles]
    expected = [f"G006-P{i:02d}" for i in range(1, 8)]
    if ids != expected:
        fail(f"principle IDs must be ordered {expected}, got {ids}")
    if len(set(ids)) != len(ids):
        fail("duplicate principle ID")

    required = set(registry["contract"]["required_fields"])
    fixtures = {f"A-{i:02d}" for i in range(1, 13)}
    clauses = {f"AI-{i:02d}" for i in range(1, 8)}
    principle_by_id = {}
    for principle in principles:
        missing = sorted(required - set(principle))
        if missing:
            fail(f"{principle.get('principle_id')} missing fields: {', '.join(missing)}")
        if principle["owner_clause_id"] not in clauses:
            fail(f"{principle['principle_id']} has invalid owner clause")
        if principle["status"] not in {"draft", "validated", "blocked"}:
            fail(f"{principle['principle_id']} has invalid status")
        if principle["downstream_owner"] not in {"none", "G007", "G008"}:
            fail(f"{principle['principle_id']} has invalid downstream owner")
        if not principle["counterexamples"] or not principle["boundaries"]:
            fail(f"{principle['principle_id']} requires boundaries and counterexamples")
        if not all(re.fullmatch(r"EP-[0-9]{2}", x) for x in principle["epistemic_principle_ids"]):
            fail(f"{principle['principle_id']} has malformed EP link")
        if not set(principle["fixture_ids"]).issubset(fixtures):
            fail(f"{principle['principle_id']} references an unknown fixture")
        principle_by_id[principle["principle_id"]] = principle

    owned_clauses = [p["owner_clause_id"] for p in principles]
    if set(owned_clauses) != clauses or len(owned_clauses) != len(set(owned_clauses)):
        fail("AI-01 through AI-07 must each have exactly one registry owner")

    entries = mapping.get("entries")
    if not isinstance(entries, list) or len(entries) != 3:
        fail("canonical map must contain the three selected G006 replacement entries")
    entry_ids = {entry.get("entry_id") for entry in entries}
    for entry in entries:
        if not entry.get("principle_ids"):
            fail(f"{entry.get('entry_id')} has no principle links")
        if not set(entry["principle_ids"]).issubset(principle_by_id):
            fail(f"{entry['entry_id']} references an unknown principle")
        if not entry.get("clause_ids") or not set(entry["clause_ids"]).issubset(clauses):
            fail(f"{entry['entry_id']} has invalid clause links")
        if not entry.get("fixture_ids") or not set(entry["fixture_ids"]).issubset(fixtures):
            fail(f"{entry['entry_id']} has invalid fixture links")
        for principle_id in entry["principle_ids"]:
            if entry["entry_id"] not in principle_by_id[principle_id]["replacement_entries"]:
                fail(f"{entry['entry_id']} is not reciprocal in {principle_id}")

    referenced_entries = {entry_id for p in principles for entry_id in p["replacement_entries"]}
    if not referenced_entries.issubset(entry_ids):
        fail("registry references a replacement entry absent from the canonical map")

    print("PASS: G006 registry schema, seven stable IDs, clause ownership, fixture links, and map reciprocity")
    print(f"principles={len(principles)} map_entries={len(entries)} source_sha256={sha256(SOURCE)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
