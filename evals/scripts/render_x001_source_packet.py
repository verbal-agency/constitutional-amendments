#!/usr/bin/env python3
"""Render an approved source packet into a model-visible X001 message envelope."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from validate_x001_source_packets import DEFAULT_PACKETS, read_packets, validate_packets


RENDERER_VERSION = "x001-source-packet-render-v1"


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def render_text(packet: dict) -> str:
    visible = set(packet["rendering"]["model_visible_source_ids"])
    sources = [source for source in packet["sources"] if source["source_id"] in visible]
    source_blocks = []
    for source in sources:
        published = source["published_at"] or "date not supplied"
        source_blocks.append(
            f"[Source {source['source_id']} | {source['publisher_or_author']} | published {published}]\n"
            f"{source['summary']}"
        )
    return (
        f"Issue: {packet['event_or_issue']}\n"
        f"Information cutoff: {packet['source_cutoff'] or 'not supplied'}\n\n"
        f"Task:\n{packet['task_prompt']}\n\n"
        "Supplied evidence:\n"
        + "\n\n".join(source_blocks)
    )


def render_packet(packet: dict) -> dict:
    text = render_text(packet)
    return {
        "packet_id": packet["packet_id"],
        "packet_sha256": packet["packet_sha256"],
        "renderer_version": RENDERER_VERSION,
        "rendered_text_sha256": sha256_text(text),
        "messages": [{"role": "user", "content": text}],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--packets", type=Path, default=DEFAULT_PACKETS)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--packet-id", help="render only one packet")
    args = parser.parse_args()
    packets = read_packets(args.packets)
    validate_packets(packets)
    if args.packet_id:
        packets = [packet for packet in packets if packet["packet_id"] == args.packet_id]
        if not packets:
            raise SystemExit(f"packet not found: {args.packet_id}")
    rows = [json.dumps(render_packet(packet), ensure_ascii=False, separators=(",", ":")) for packet in packets]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(rows) + ("\n" if rows else ""), encoding="utf-8")
    print(f"rendered {len(rows)} packets with {RENDERER_VERSION}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
