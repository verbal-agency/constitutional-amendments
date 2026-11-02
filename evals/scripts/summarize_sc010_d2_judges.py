#!/usr/bin/env python3
"""Summarize recorded SC-010-D2 judge agreement without network calls."""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def first(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8").splitlines()[0])


def score_shape(record: dict) -> tuple | None:
    parsed = record.get("parsed")
    if not parsed or "dimensions" not in parsed:
        return None
    return tuple(parsed["dimensions"][key]["score"] for key in ("PS", "CAL"))


def summarize(root: Path) -> dict:
    rows = []
    for manifest in sorted(root.glob("**/manifest.json")):
        directory = manifest.parent
        primary = first(directory / "scores-primary.jsonl")
        secondary = first(directory / "scores-secondary-candidate.jsonl")
        p = score_shape(primary)
        s = score_shape(secondary)
        rows.append({
            "run": str(directory.relative_to(ROOT)),
            "primary_status": primary.get("status"),
            "secondary_status": secondary.get("status"),
            "primary_shape": p,
            "secondary_shape": s,
            "exact_agreement": p is not None and p == s,
        })
    scored = [row for row in rows if row["primary_shape"] is not None and row["secondary_shape"] is not None]
    return {
        "contract": "sc010-d2-judge-agreement-v1",
        "runs": len(rows),
        "primary_statuses": dict(Counter(row["primary_status"] for row in rows)),
        "secondary_statuses": dict(Counter(row["secondary_status"] for row in rows)),
        "exact_agreement_scored": sum(row["exact_agreement"] for row in scored),
        "scored_pair_count": len(scored),
        "agreement_rate": round(sum(row["exact_agreement"] for row in scored) / len(scored), 4) if scored else None,
        "primary_shapes": dict(Counter(str(row["primary_shape"]) for row in rows)),
        "secondary_shapes": dict(Counter(str(row["secondary_shape"]) for row in rows)),
        "rows": rows,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("root", nargs="?", default="evals/runs/g006-s5r-d2-replication")
    ap.add_argument("--output")
    args = ap.parse_args()
    root = Path(args.root) if Path(args.root).is_absolute() else ROOT / args.root
    payload = json.dumps(summarize(root), indent=2) + "\n"
    if args.output:
        output = Path(args.output) if Path(args.output).is_absolute() else ROOT / args.output
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(payload, encoding="utf-8")
    print(payload, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
