#!/usr/bin/env python3
"""Validate the G007 constitutional clause module without model or network calls."""

from __future__ import annotations

import hashlib
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MODULE = ROOT / "amendments/G007-inquiry-and-harm.md"
SOURCE = ROOT / "20260120-constitution.md"

EXPECTED_IDS = [f"HA-{index:02d}" for index in range(1, 8)]
REQUIRED_METADATA = [
    "Function",
    "Word count",
    "Affected planes",
    "Harm classes",
    "Hazard threshold",
    "Capacity rule",
    "Proportionality rule",
    "Less-restrictive alternative",
    "Duration or expiry",
    "Review trigger",
    "Principle IDs",
    "Conflict rule IDs",
    "Scenario IDs",
    "Fixture IDs",
    "Source targets",
    "Audit IDs",
    "Preserved purpose",
    "Prohibited interpretation",
    "Downstream obligation",
    "Status",
]


def fail(message: str) -> None:
    raise SystemExit(f"FAIL {message}")


def words(text: str) -> list[str]:
    return re.findall(r"\b[\w’'-]+\b", text)


def main() -> None:
    if not MODULE.exists() or not SOURCE.exists():
        fail("module_or_source_missing")

    module_text = MODULE.read_text(encoding="utf-8")
    source_hash = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    hash_match = re.search(r"^Source hash: `([0-9a-f]{64})`$", module_text, re.MULTILINE)
    if not hash_match:
        fail("source_hash_missing")
    if hash_match.group(1) != source_hash:
        fail(f"source_hash_mismatch expected={source_hash} actual={hash_match.group(1)}")

    headings = list(re.finditer(r"^## (HA-\d{2}) — .+$", module_text, re.MULTILINE))
    ids = [match.group(1) for match in headings]
    if ids != EXPECTED_IDS:
        fail(f"clause_ids expected={EXPECTED_IDS} actual={ids}")

    max_words = 0
    for index, heading in enumerate(headings):
        end = headings[index + 1].start() if index + 1 < len(headings) else module_text.find("\n## Module-level invariants", heading.end())
        if end == -1:
            end = len(module_text)
        section = module_text[heading.end() : end]

        blockquote = " ".join(
            line[2:].strip() for line in section.splitlines() if line.startswith("> ")
        ).strip()
        if not blockquote:
            fail(f"{heading.group(1)} clause_text_missing")
        count = len(words(blockquote))
        max_words = max(max_words, count)
        if count > 120:
            fail(f"{heading.group(1)} clause_text_words={count} exceeds=120")

        for label in REQUIRED_METADATA:
            if not re.search(rf"^- \*\*{re.escape(label)}:\*\*", section, re.MULTILINE):
                fail(f"{heading.group(1)} metadata_missing={label}")

        word_count_match = re.search(r"^- \*\*Word count:\*\* (\d+)\.", section, re.MULTILINE)
        if not word_count_match or int(word_count_match.group(1)) != count:
            actual = word_count_match.group(1) if word_count_match else "missing"
            fail(f"{heading.group(1)} word_count_metadata={actual} parsed={count}")

        fixture_line = re.search(r"^- \*\*Fixture IDs:\*\* (.+)\.$", section, re.MULTILINE)
        if not fixture_line:
            fail(f"{heading.group(1)} fixture_links_missing")
        fixture_ids = re.findall(r"H-\d{2}", fixture_line.group(1))
        if not fixture_ids or any(int(value.split("-")[1]) > 12 for value in fixture_ids):
            fail(f"{heading.group(1)} fixture_links_invalid={fixture_ids}")

    for clause_id in EXPECTED_IDS:
        if module_text.count(f"## {clause_id} —") != 1:
            fail(f"{clause_id} heading_count_invalid")

    print(
        "PASS "
        f"clauses={len(ids)} max_clause_words={max_words} "
        f"source_sha256={source_hash} prompt_first=true no_model_call=true"
    )


if __name__ == "__main__":
    main()
