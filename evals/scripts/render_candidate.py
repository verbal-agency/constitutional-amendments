#!/usr/bin/env python3
"""Render a candidate constitution by exact, non-duplicating passage replacement."""
import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def sha256_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def render(source_text, spec):
    source_hash = sha256_text(source_text)
    if source_hash != spec["source_sha256"]:
        raise ValueError(f"source hash mismatch: expected {spec['source_sha256']}, got {source_hash}")
    lines = source_text.splitlines(keepends=True)
    entries = sorted(spec["entries"], key=lambda x: x["source_start_line"], reverse=True)
    previous_start = len(lines) + 1
    applied = []
    for entry in entries:
        start = entry["source_start_line"]
        end = entry["source_end_line_exclusive"]
        if not (1 <= start < end <= len(lines) + 1):
            raise ValueError(f"invalid range for {entry['entry_id']}: {start}:{end}")
        if end > previous_start:
            raise ValueError(f"overlapping map entry: {entry['entry_id']}")
        original = "".join(lines[start - 1:end - 1])
        actual = sha256_text(original)
        if actual != entry["source_sha256"]:
            raise ValueError(f"source segment hash mismatch for {entry['entry_id']}")
        replacement = entry["replacement"].rstrip() + "\n\n"
        lines[start - 1:end - 1] = [replacement]
        previous_start = start
        applied.append({"entry_id": entry["entry_id"], "source_start_line": start,
                        "source_end_line_exclusive": end, "replacement_sha256": sha256_text(replacement.rstrip())})
    candidate = "".join(lines)
    forbidden = ["G006", "AI-01", "AI-02", "AI-03", "AI-04", "AI-05", "AI-06", "AI-07", "audit IDs", "change-register"]
    leaked = [marker for marker in forbidden if marker in candidate]
    if leaked:
        raise ValueError("development metadata leaked into candidate: " + ", ".join(leaked))
    return candidate, {"map_id": spec["map_id"], "map_version": spec["map_version"],
                       "source_sha256": source_hash, "candidate_sha256": sha256_text(candidate),
                       "entries": list(reversed(applied)), "renderer": "render_candidate.py:v1"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", default=str(ROOT / "20260120-constitution.md"))
    ap.add_argument("--map", dest="map_path", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--metadata", required=True)
    args = ap.parse_args()
    source = Path(args.source).read_text(encoding="utf-8")
    spec = json.loads(Path(args.map_path).read_text(encoding="utf-8"))
    candidate, metadata = render(source, spec)
    Path(args.output).write_text(candidate, encoding="utf-8")
    Path(args.metadata).write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(metadata, indent=2))


if __name__ == "__main__":
    main()
