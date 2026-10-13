#!/usr/bin/env python3
"""Validate X001 principle-derived JSONL records without making model calls."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    import jsonschema
except ImportError as exc:  # pragma: no cover - clear operator-facing failure
    raise SystemExit("install jsonschema to validate X001 records") from exc


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SCHEMA = ROOT / "evals/datasets/x001-mistral-record-schema.json"


def read_records(path: Path, schema: dict) -> list[dict]:
    records = []
    for line_no, line in enumerate(path.read_text().splitlines(), start=1):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as exc:
            raise SystemExit(f"{path}:{line_no}: invalid JSON: {exc}") from exc
        try:
            jsonschema.validate(record, schema)
        except jsonschema.ValidationError as exc:
            raise SystemExit(f"{path}:{line_no}: schema failure: {exc.message}") from exc
        records.append(record)
    return records


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", type=Path, help="train/validation/heldout JSONL files")
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument("--allow-pending-review", action="store_true")
    args = parser.parse_args()

    schema = json.loads(args.schema.read_text())
    if not args.paths:
        print(f"schema: ok ({args.schema})")
        return 0

    seen: set[str] = set()
    split_counts: dict[str, int] = {"train": 0, "validation": 0, "heldout": 0}
    for path in args.paths:
        rows = read_records(path, schema)
        for row in rows:
            if row["example_id"] in seen:
                raise SystemExit(f"duplicate example_id: {row['example_id']}")
            seen.add(row["example_id"])
            if row["review"]["status"] != "approved" and not args.allow_pending_review:
                raise SystemExit(f"{row['example_id']}: record is not human-approved")
            split_counts[row["split"]] += 1
        print(f"{path}: {len(rows)} records")
    print(f"total: {len(seen)}; splits: {split_counts}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
