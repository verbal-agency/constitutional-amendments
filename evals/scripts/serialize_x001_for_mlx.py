#!/usr/bin/env python3
"""Serialize validated X001 message records into deterministic MLX text JSONL."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


SERIALIZER_VERSION = "x001-mlx-text-v1"
ROLE_LABELS = {"system": "System", "user": "User", "assistant": "Assistant"}


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def canonical_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def serialize_messages(messages: list[dict[str, str]]) -> str:
    """Render messages without applying a tokenizer-owned chat template."""
    if len(messages) < 2:
        raise ValueError("messages must contain at least two turns")
    roles = [message.get("role") for message in messages]
    if roles[-1] != "assistant":
        raise ValueError("the final message must be the assistant target")
    if "user" not in roles:
        raise ValueError("messages must contain a user turn")
    if any(role == "system" for role in roles[1:]):
        raise ValueError("a system message is allowed only in the first position")

    rendered: list[str] = []
    for message in messages:
        role = message.get("role")
        content = message.get("content")
        if role not in ROLE_LABELS:
            raise ValueError(f"unsupported message role: {role!r}")
        if not isinstance(content, str) or not content:
            raise ValueError("message content must be a non-empty string")
        rendered.append(f"{ROLE_LABELS[role]}: {content}")
    return "\n".join(rendered)


def serialize_file(input_path: Path, output_path: Path, manifest_path: Path) -> int:
    output_rows: list[str] = []
    manifest_rows: list[str] = []
    for line_no, line in enumerate(input_path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{input_path}:{line_no}: invalid JSON: {exc}") from exc
        if record.get("record_version") != "x001-record-v3":
            raise ValueError(f"{input_path}:{line_no}: expected x001-record-v3")
        if record.get("review", {}).get("status") != "approved":
            raise ValueError(f"{input_path}:{line_no}: only approved records may be serialized")
        if record.get("review", {}).get("reviewer_type") not in {"human", "human_plus_model"}:
            raise ValueError(f"{input_path}:{line_no}: approved record requires human review")

        text = serialize_messages(record.get("messages", []))
        output_rows.append(json.dumps({"text": text}, ensure_ascii=False, separators=(",", ":")))
        manifest_rows.append(
            json.dumps(
                {
                    "serializer_version": SERIALIZER_VERSION,
                    "line": len(output_rows),
                    "example_id": record["example_id"],
                    "split": record["split"],
                    "source_record_sha256": sha256_text(canonical_json(record)),
                    "source_messages_sha256": sha256_text(canonical_json(record["messages"])),
                    "serialized_text_sha256": sha256_text(text),
                    "constitution_version": record["constitution_version"],
                    "policy_delta_ids": record["policy_delta_ids"],
                    "target_revision": record["target_revision"],
                },
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
            )
        )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(output_rows) + ("\n" if output_rows else ""), encoding="utf-8")
    manifest_path.write_text("\n".join(manifest_rows) + ("\n" if manifest_rows else ""), encoding="utf-8")
    return len(output_rows)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True, help="validated X001 v3 JSONL")
    parser.add_argument("--output", type=Path, required=True, help="MLX text JSONL output")
    parser.add_argument("--manifest", type=Path, required=True, help="lineage manifest JSONL")
    args = parser.parse_args()
    count = serialize_file(args.input, args.output, args.manifest)
    print(f"serialized {count} records with {SERIALIZER_VERSION}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
