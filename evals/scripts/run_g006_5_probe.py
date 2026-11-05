#!/usr/bin/env python3
"""G006.5 walking-skeleton probe: candidate vs. base on the frozen G007-S4 packet.

Exploratory development evidence only. Not the G010 comparison.

Generations (25 max):
  - 10 paired cases x {base, candidate}
  - 5 sentinels x candidate only; base reuses evals/runs/base-v1/outputs.jsonl
    when the rebuilt prompt hash matches the stored one.

Usage:
  run_g006_5_probe.py --dry-run     # validate hashes, reuse, estimates; no network
  run_g006_5_probe.py --execute     # requires evals/runs/g006.5-s2/approval.json
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
RUN = ROOT / "evals/runs/g006.5-s2"
PACKET = ROOT / "evals/manifests/g007-s4-development-probe.json"
CAND_META = ROOT / "evals/candidates/g006.5-provisional-v1/render-metadata.json"
CAND = ROOT / "evals/candidates/g006.5-provisional-v1/candidate-constitution.md"
SOURCE = ROOT / "20260120-constitution.md"
MAX_GENERATIONS = 25


def load_inputs():
    packet = json.loads(PACKET.read_text())
    config = E.load_yaml(ROOT / "evals/configs/base-v1.yaml")
    src = SOURCE.read_text()
    cand = CAND.read_text()
    assert E.sha256_text(src) == packet["source"]["constitution_sha256"], "source hash drift"
    meta = json.loads(CAND_META.read_text())
    assert E.sha256_text(cand) == meta["candidate_sha256"], "candidate hash drift"
    dev = {}
    for line in (ROOT / "evals/datasets/custom-dev-v1.jsonl").read_text().splitlines():
        c = json.loads(line)
        dev[c["case_id"]] = c
    base_prior = {}
    for line in (ROOT / "evals/runs/base-v1/outputs.jsonl").read_text().splitlines():
        j = json.loads(line)
        base_prior[j["case_id"]] = j
    return packet, config, src, cand, dev, base_prior


def plan(packet, config, src, cand, dev, base_prior):
    """Return list of (arm, probe_case, model_case, constitution, reuse_record|None)."""
    items = []
    for pc in packet["cases"]:
        if pc["role"] == "paired":
            items.append(("base", pc, pc, src, None))
            items.append(("candidate", pc, pc, cand, None))
        else:
            ref = pc["source_case_ref"]["case_id"]
            mc = dev[ref]
            msgs = E.build_messages(config, src, mc)
            prior = base_prior.get(ref)
            ok = bool(prior) and prior["prompt_hash"] == E.prompt_hash(msgs)
            items.append(("base", pc, mc, src, prior if ok else "MISMATCH"))
            items.append(("candidate", pc, mc, cand, None))
    return items


def get_model_entry(config, key):
    r = requests.get(config["provider"]["base_url"] + "/models",
                     headers={"Authorization": f"Bearer {key}"}, timeout=60)
    r.raise_for_status()
    return [m for m in r.json().get("data", []) if m.get("id") == config["provider"]["model"]] or r.json()


def call(config, key, messages):
    body = {"model": config["provider"]["model"], "messages": messages,
            "max_tokens": config["decoding"]["max_tokens"], "temperature": 0, "top_p": 1,
            "stream": False, "thinking": {"type": "disabled"}}
    t0 = time.time()
    r = requests.post(config["provider"]["base_url"] + config["provider"]["endpoint"], json=body,
                      headers={"Authorization": f"Bearer {key}"}, timeout=180)
    if r.status_code != 200:
        raise RuntimeError(f"HTTP {r.status_code}: {r.text[:300]}")
    return r.json(), round(time.time() - t0, 2)


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true")
    g.add_argument("--execute", action="store_true")
    args = ap.parse_args()

    packet, config, src, cand, dev, base_prior = load_inputs()
    items = plan(packet, config, src, cand, dev, base_prior)
    reuse = [i for i in items if i[4] not in (None, "MISMATCH")]
    mismatch = [i for i in items if i[4] == "MISMATCH"]
    to_run = [i for i in items if i[4] is None or i[4] == "MISMATCH"]
    print(f"planned={len(items)} reuse={len(reuse)} mismatch={len(mismatch)} to_generate={len(to_run)}")
    for i in mismatch:
        print("  prompt-hash mismatch, base will be regenerated:", i[1]["case_id"])
    assert len(to_run) <= MAX_GENERATIONS, "exceeds generation cap"

    if args.dry_run:
        tot = sum(estimate("".join(m["content"] for m in E.build_messages(config, i[3], i[2]))) for i in to_run)
        print(f"estimated_input_tokens_total={tot}")
        return

    appr = json.loads((RUN / "approval.json").read_text())
    ceiling = float(appr["ceiling_usd"])
    key = load_key()
    ledger = E.BudgetLedger(ceiling, MAX_GENERATIONS, config["decoding"]["max_tokens"], config["prices"])
    model_entry = get_model_entry(config, key)
    (RUN / "model-entry.json").write_text(json.dumps(model_entry, indent=2) + "\n")
    out_path = RUN / "outputs.jsonl"
    done = {}
    if out_path.exists():
        for line in out_path.read_text().splitlines():
            if line.strip():
                r = json.loads(line)
                done[(r["arm"], r["probe_case_id"])] = r
                if not r.get("reused"):
                    ledger.record(r["usage"])
    for arm, pc, mc, const, prior in items:
        k = (arm, pc["case_id"])
        if k in done:
            continue
        if prior not in (None, "MISMATCH"):
            rec = {"arm": arm, "probe_case_id": pc["case_id"], "model_case_id": mc["case_id"], "reused": True,
                   "reused_from": "evals/runs/base-v1/outputs.jsonl", "prompt_hash": prior["prompt_hash"],
                   "output": prior["output"], "usage": prior["usage"], "request_id": prior["request_id"]}
        else:
            msgs = E.build_messages(config, const, mc)
            est = estimate("".join(m["content"] for m in msgs))
            ledger.check(est)
            print(f"calling {arm} {pc['case_id']} est_in={est}", flush=True)
            data, lat = call(config, key, msgs)
            u = usage(data.get("usage", {}))
            ledger.record(u)
            ch = data["choices"][0]
            rec = {"arm": arm, "probe_case_id": pc["case_id"], "model_case_id": mc["case_id"], "reused": False,
                   "prompt_hash": E.prompt_hash(msgs), "output": ch["message"]["content"],
                   "finish_reason": ch.get("finish_reason"), "usage": u,
                   "estimated_cost_usd": round(E.usage_cost(u, config["prices"]), 6),
                   "latency_s": lat, "request_id": data.get("id"), "model": data.get("model")}
        with out_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    (RUN / "usage.json").write_text(json.dumps(ledger.to_dict(), indent=2) + "\n")
    print(json.dumps(ledger.to_dict(), indent=2))


if __name__ == "__main__":
    RUN.mkdir(parents=True, exist_ok=True)
    main()
