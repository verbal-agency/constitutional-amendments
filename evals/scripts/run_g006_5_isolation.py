#!/usr/bin/env python3
"""G006.5 isolation probe for the OPS-01 confabulation hypothesis.

Five constitution arms, five draws each, one frozen packet case, temperature
0.7. This is exploratory evidence only and uses manual labels; it is not the
G010 comparison.
"""
import argparse
import json
import sys
import time
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
import evalcore as E  # noqa: E402
import sources as S  # noqa: E402
from run_g006_probe import estimate, load_key, usage  # noqa: E402


ROOT = S.ROOT
RUN = ROOT / "evals/runs/g006.5-s4-isolation"
PACKET = ROOT / "evals/manifests/g007-s4-development-probe.json"
SOURCE = ROOT / "20260120-constitution.md"
CANDIDATE = ROOT / "evals/candidates/g006.5-provisional-v1/candidate-constitution.md"
METADATA = ROOT / "evals/candidates/g006.5-provisional-v1/render-metadata.json"
DRAWS = 5
TEMPERATURE = 0.7
MAX_GENERATIONS = 25
CASE_ID = "G007-S4-OPS-01"


def apply_entries(source, entries):
    lines = source.splitlines(keepends=True)
    for entry in sorted(entries, key=lambda x: -x["source_start_line"]):
        replacement = entry["replacement"].rstrip() + "\n\n"
        lines[entry["source_start_line"] - 1:entry["source_end_line_exclusive"] - 1] = [replacement]
    return "".join(lines)


def load_inputs():
    config = E.load_yaml(ROOT / "evals/configs/base-v1.yaml")
    source = SOURCE.read_text(encoding="utf-8")
    candidate = CANDIDATE.read_text(encoding="utf-8")
    metadata = json.loads(METADATA.read_text(encoding="utf-8"))
    spec = json.loads((ROOT / "evals/manifests/g006.5-replacement-provisional-v1.json").read_text())
    packet = json.loads(PACKET.read_text())
    case = next(c for c in packet["cases"] if c["case_id"] == CASE_ID)
    assert E.sha256_text(candidate) == metadata["candidate_sha256"], "candidate hash drift"
    assert E.sha256_text(source) == spec["source_sha256"], "source hash drift"
    entries = spec["entries"]
    arms = {
        "base": source,
        "g005-only": apply_entries(source, [e for e in entries if e["entry_id"].startswith("G006.5-G005")]),
        "g006-only": apply_entries(source, [e for e in entries if e["entry_id"].startswith("G006-MAP")]),
        "g007-only": apply_entries(source, [e for e in entries if e["entry_id"].startswith("G006.5-G007")]),
        "full": candidate,
    }
    return config, case, arms


def call(config, key, messages):
    body = {
        "model": config["provider"]["model"],
        "messages": messages,
        "max_tokens": config["decoding"]["max_tokens"],
        "temperature": TEMPERATURE,
        "top_p": 1,
        "stream": False,
        "thinking": {"type": "disabled"},
    }
    started = time.time()
    response = requests.post(
        config["provider"]["base_url"] + config["provider"]["endpoint"],
        json=body,
        headers={"Authorization": f"Bearer {key}"},
        timeout=180,
    )
    if response.status_code != 200:
        raise RuntimeError(f"HTTP {response.status_code}: {response.text[:300]}")
    data = response.json()
    return data, round(time.time() - started, 2)


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--dry-run", action="store_true")
    group.add_argument("--execute", action="store_true")
    args = parser.parse_args()

    config, case, arms = load_inputs()
    cells = [(arm, draw) for arm in arms for draw in range(DRAWS)]
    assert len(cells) == MAX_GENERATIONS
    estimates = []
    for arm, _ in cells:
        messages = E.build_messages(config, arms[arm], case)
        estimates.append(estimate("".join(m["content"] for m in messages)))
    print({arm: {"chars": len(text), "sha256": E.sha256_text(text)} for arm, text in arms.items()})
    print(f"case={CASE_ID} cells={len(cells)} temperature={TEMPERATURE} estimated_input_tokens={sum(estimates)}")
    if args.dry_run:
        return

    approval = json.loads((RUN / "approval.json").read_text())
    ledger = E.BudgetLedger(float(approval["ceiling_usd"]), MAX_GENERATIONS, 600, config["prices"])
    key = load_key()
    output_path = RUN / "outputs.jsonl"
    completed = set()
    if output_path.exists():
        for line in output_path.read_text().splitlines():
            if line.strip():
                record = json.loads(line)
                completed.add((record["arm"], record["draw"]))
                ledger.record(record["usage"])
    for arm, draw in cells:
        if (arm, draw) in completed:
            continue
        messages = E.build_messages(config, arms[arm], case)
        ledger.check(estimate("".join(m["content"] for m in messages)))
        print(f"calling {arm} draw={draw}", flush=True)
        data, latency = call(config, key, messages)
        usage_record = usage(data.get("usage", {}))
        ledger.record(usage_record)
        choice = data["choices"][0]
        record = {
            "arm": arm,
            "case_id": CASE_ID,
            "draw": draw,
            "temperature": TEMPERATURE,
            "output": choice["message"]["content"],
            "finish_reason": choice.get("finish_reason"),
            "usage": usage_record,
            "estimated_cost_usd": round(E.usage_cost(usage_record, config["prices"]), 6),
            "latency_s": latency,
            "request_id": data.get("id"),
            "model": data.get("model"),
        }
        with output_path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    (RUN / "usage.json").write_text(json.dumps(ledger.to_dict(), indent=2) + "\n")
    print(json.dumps(ledger.to_dict(), indent=2))


if __name__ == "__main__":
    RUN.mkdir(parents=True, exist_ok=True)
    main()
