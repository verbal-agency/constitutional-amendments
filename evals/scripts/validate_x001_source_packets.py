#!/usr/bin/env python3
"""Validate X001 frozen source packets without making model or network calls."""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from pathlib import Path

try:
    import jsonschema
except ImportError as exc:  # pragma: no cover
    raise SystemExit("install jsonschema to validate X001 source packets") from exc


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SCHEMA = ROOT / "evals/datasets/x001-source-packet-schema.json"
DEFAULT_PACKETS = ROOT / "evals/datasets/x001-source-packets.jsonl"


def canonical_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def packet_hash(packet: dict) -> str:
    return sha256_text(canonical_json({key: value for key, value in packet.items() if key != "packet_sha256"}))


def source_hash(source: dict) -> str:
    return sha256_text(canonical_json({"locator": source["locator"], "summary": source["summary"]}))


def read_packets(path: Path, schema_path: Path = DEFAULT_SCHEMA) -> list[dict]:
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    jsonschema.Draft202012Validator.check_schema(schema)
    packets: list[dict] = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            packet = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{line_no}: invalid JSON: {exc}") from exc
        try:
            jsonschema.validate(packet, schema)
        except jsonschema.ValidationError as exc:
            raise ValueError(f"{path}:{line_no}: schema failure: {exc.message}") from exc
        packets.append(packet)
    return packets


def validate_packets(packets: list[dict]) -> None:
    packet_ids: set[str] = set()
    family_splits: dict[tuple[str, str], set[str]] = defaultdict(set)
    source_cluster_splits: dict[str, set[str]] = defaultdict(set)
    framing_pair_splits: dict[str, set[str]] = defaultdict(set)

    for packet in packets:
        packet_id = packet["packet_id"]
        if packet_id in packet_ids:
            raise ValueError(f"duplicate packet_id: {packet_id}")
        packet_ids.add(packet_id)
        if packet["packet_sha256"] != packet_hash(packet):
            raise ValueError(f"{packet_id}: packet_sha256 mismatch")

        sources = packet["sources"]
        source_ids = {source["source_id"] for source in sources}
        if len(source_ids) != len(sources):
            raise ValueError(f"{packet_id}: duplicate source_id")
        for source in sources:
            if source["content_sha256"] != source_hash(source):
                raise ValueError(f"{packet_id}/{source['source_id']}: content_sha256 mismatch")
        if set(packet["rendering"]["model_visible_source_ids"]) - source_ids:
            raise ValueError(f"{packet_id}: renderer references an unknown source")
        if packet["rendering"]["annotation_fields_hidden"] is not True:
            raise ValueError(f"{packet_id}: annotation fields must remain hidden")

        claim_ids: set[str] = set()
        for claim in packet["claims"]:
            if claim["claim_id"] in claim_ids:
                raise ValueError(f"{packet_id}: duplicate claim_id {claim['claim_id']}")
            claim_ids.add(claim["claim_id"])
            if set(claim["source_ids"]) - source_ids:
                raise ValueError(f"{packet_id}/{claim['claim_id']}: unknown source reference")
            if claim["annotation_only"] is False and claim["support_status"] in {"unsupported", "uncertain"}:
                # Uncertainty is allowed as evidence, but it must be explicitly annotated.
                if claim["claim_type"] not in {"causal_inference", "forecast", "question"}:
                    raise ValueError(f"{packet_id}/{claim['claim_id']}: visible uncertain claim needs inference/forecast/question type")
        for contradiction in packet["contradictions"]:
            if set(contradiction["claim_ids"]) - claim_ids:
                raise ValueError(f"{packet_id}: contradiction references an unknown claim")

        key = (packet["topic_family_id"], packet["domain"])
        family_splits[key].add(packet["split"])
        if packet["source_overlap_cluster_id"]:
            source_cluster_splits[packet["source_overlap_cluster_id"]].add(packet["split"])
        if packet["framing_pair_id"]:
            framing_pair_splits[packet["framing_pair_id"]].add(packet["split"])

    for label, split_map in (("topic family", family_splits), ("source overlap cluster", source_cluster_splits), ("framing pair", framing_pair_splits)):
        for identifier, splits in split_map.items():
            if len(splits) > 1:
                raise ValueError(f"{label} {identifier} crosses splits: {sorted(splits)}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--packets", type=Path, default=DEFAULT_PACKETS)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    args = parser.parse_args()
    packets = read_packets(args.packets, args.schema)
    validate_packets(packets)
    print(f"source packets: ok ({len(packets)} packets)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
