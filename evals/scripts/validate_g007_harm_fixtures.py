#!/usr/bin/env python3
"""Validate the offline G007 harm schema and human-readable fixture contract."""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / "framework/G007-harm-schema.yaml"
FIXTURES = ROOT / "fixtures/G007-harm-cases.md"


REQUIRED_FIELDS = {
    "Class", "Case shape", "Condition", "Planes", "Expected behavior",
    "Unacceptable behavior", "Required clause IDs",
    "Preserved safety or privacy purpose", "Acceptance proof", "Result",
}
EXPECTED_IDS = {f"H-{i:02d}" for i in range(1, 13)}


def parse_fixture_sections(text: str) -> list[dict[str, str]]:
    sections = re.split(r"^## (H-\d{2}) — .*?$", text, flags=re.MULTILINE)
    records = []
    for i in range(1, len(sections), 2):
        case_id, body = sections[i], sections[i + 1]
        fields = {k: v.strip() for k, v in re.findall(r"^- \*\*([^*]+):\*\* (.+)$", body, flags=re.MULTILINE)}
        fields["case_id"] = case_id
        records.append(fields)
    return records


def main() -> int:
    schema = yaml.safe_load(SCHEMA.read_text(encoding="utf-8"))
    text = FIXTURES.read_text(encoding="utf-8")
    records = parse_fixture_sections(text)
    errors: list[str] = []

    required_enums = {
        "affected_plane", "consent_status", "capacity_status", "harm_class",
        "fixture_class",
        "hazard_threshold", "severity", "likelihood", "operational_uplift",
        "reversibility", "selected_response", "duration_or_expiry", "case_shape",
    }
    if set(schema.get("enums", {})) != required_enums:
        errors.append("schema enum set does not match the v1 contract")
    required_decision_fields = {
        "decision_id", "request_summary", "affected_plane", "actor",
        "decision_maker", "risk_bearer", "affected_person_or_parties",
        "consent_status", "capacity_status", "harm_class", "hazard_threshold",
        "severity", "likelihood", "operational_uplift", "reversibility",
        "evidence_basis", "uncertainty", "protected_interest",
        "least_restrictive_option", "selected_response", "duration_or_expiry",
        "review_trigger", "appeal_path", "provenance_record_id", "destination",
    }
    if set(schema.get("decision_required_fields", [])) != required_decision_fields:
        errors.append("decision required fields do not match the v1 contract")
    if len(schema.get("decision_rules", [])) != 7:
        errors.append("expected seven decision rules")
    if len(schema.get("illegal_states", [])) != 7:
        errors.append("expected seven illegal states")
    if len(records) != 12:
        errors.append(f"expected 12 fixture sections, found {len(records)}")

    ids = {r["case_id"] for r in records}
    if ids != EXPECTED_IDS:
        errors.append(f"fixture IDs differ: expected {sorted(EXPECTED_IDS)}, got {sorted(ids)}")

    allowed_classes = set(schema["enums"]["fixture_class"])
    allowed_shapes = set(schema["enums"]["case_shape"])
    for r in records:
        missing = REQUIRED_FIELDS - set(r)
        if missing:
            errors.append(f"{r.get('case_id', '?')} missing fields: {sorted(missing)}")
        if r.get("Result") != "`PASS`":
            errors.append(f"{r.get('case_id', '?')} does not have Result PASS")
        if r.get("Class", "").strip("`") not in allowed_classes:
            errors.append(f"{r.get('case_id', '?')} has unknown class {r.get('Class')}")
        if r.get("Case shape", "").strip("`") not in allowed_shapes:
            errors.append(f"{r.get('case_id', '?')} has unknown case shape {r.get('Case shape')}")
        clauses = re.findall(r"HA-0[1-7]", r.get("Required clause IDs", ""))
        if not clauses:
            errors.append(f"{r.get('case_id', '?')} has no HA clause link")

    covered_classes = {r.get("Class", "").strip("`") for r in records}
    required_classes = {"inquiry", "self_regarding", "consensual", "nonconsensual", "operational", "privacy", "malformed", "emergency", "unsupported"}
    if covered_classes != required_classes:
        errors.append(f"class coverage differs: {sorted(covered_classes)}")
    covered_shapes = {r.get("Case shape", "").strip("`") for r in records}
    if covered_shapes != {"positive", "negative", "contradictory", "malformed", "partial", "stopped"}:
        errors.append(f"case-shape coverage differs: {sorted(covered_shapes)}")

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1
    print("PASS fixtures=12 classes=9 case_shapes=6 schema=g007-harm-decision-v1 no_paid_call=true")
    return 0


if __name__ == "__main__":
    sys.exit(main())
