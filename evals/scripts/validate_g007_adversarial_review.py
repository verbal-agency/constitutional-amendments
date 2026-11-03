#!/usr/bin/env python3
"""Validate the deterministic G007 adversarial review record."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REPORT = ROOT / "framework/G007-adversarial-review.md"
EXPECTED_FIXTURES = [f"H-{index:02d}" for index in range(1, 13)]
EXPECTED_PROBES = [f"B-{index:02d}" for index in range(1, 7)]


def fail(message: str) -> None:
    raise SystemExit(f"FAIL {message}")


def main() -> None:
    if not REPORT.exists():
        fail("report_missing")
    text = REPORT.read_text(encoding="utf-8")
    if "offline semantic review" not in text or "no model, provider, network, paid" not in text:
        fail("offline_boundary_missing")
    if "## Results" not in text or "## Findings and routing" not in text:
        fail("results_or_routing_missing")

    fixture_headings = re.findall(r"^### (H-\d{2}) —", text, re.MULTILINE)
    if fixture_headings != EXPECTED_FIXTURES:
        fail(f"fixture_headings expected={EXPECTED_FIXTURES} actual={fixture_headings}")
    for fixture_id in EXPECTED_FIXTURES:
        section = re.search(
            rf"^### {fixture_id} —.*?(?=^### H-|^## Boundary probes)",
            text,
            re.MULTILINE | re.DOTALL,
        )
        if not section or "- **Result:** `PASS`" not in section.group(0):
            fail(f"{fixture_id} missing_pass_result")

    probe_ids = re.findall(r"\| (B-\d{2}) \|", text)
    if probe_ids != EXPECTED_PROBES:
        fail(f"boundary_probes expected={EXPECTED_PROBES} actual={probe_ids}")
    if "HA-04 now contains it" not in text:
        fail("revision_finding_missing")
    if not re.search(r"No\s+model behavior was observed", text):
        fail("no_model_observation_missing")

    print(
        "PASS "
        f"fixtures={len(fixture_headings)} boundary_probes={len(probe_ids)} "
        "revision_count=1 no_model_call=true"
    )


if __name__ == "__main__":
    main()
