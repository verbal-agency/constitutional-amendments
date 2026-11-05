#!/usr/bin/env python3
"""G006.5-S3 follow-up: separate sampling and length effects for two flips.

Cases: G007-S4-OPS-01 (packet) and G007-S4-SENT-EMERG-01 (source CUS-SC003-D3).
Arms: base (source), candidate, ablated (source with the five replaced ranges
removed, not replaced). 5 draws per cell at temperature 0.7 = 30 generations.
Exploratory; decoding deviates from base-v1 (temperature) by design.
"""
import argparse, json, sys, time
from pathlib import Path
import requests
sys.path.insert(0, str(Path(__file__).resolve().parent))
import evalcore as E, sources as S
from run_g006_probe import estimate, load_key, usage

ROOT = S.ROOT
RUN = ROOT / "evals/runs/g006.5-s3"
DRAWS, TEMP, MAXGEN = 5, 0.7, 30

def build():
    config = E.load_yaml(ROOT / "evals/configs/base-v1.yaml")
    src = (ROOT / "20260120-constitution.md").read_text()
    cand = (ROOT / "evals/candidates/g006.5-provisional-v1/candidate-constitution.md").read_text()
    meta = json.loads((ROOT / "evals/candidates/g006.5-provisional-v1/render-metadata.json").read_text())
    assert E.sha256_text(cand) == meta["candidate_sha256"]
    lines = src.splitlines(keepends=True)
    for e in sorted(meta["entries"], key=lambda x: -x["source_start_line"]):
        del lines[e["source_start_line"] - 1:e["source_end_line_exclusive"] - 1]
    abl = "".join(lines)
    packet = json.loads((ROOT / "evals/manifests/g007-s4-development-probe.json").read_text())
    ops = next(c for c in packet["cases"] if c["case_id"] == "G007-S4-OPS-01")
    dev = {}
    for l in (ROOT / "evals/datasets/custom-dev-v1.jsonl").read_text().splitlines():
        c = json.loads(l); dev[c["case_id"]] = c
    cases = {"G007-S4-OPS-01": ops, "G007-S4-SENT-EMERG-01": dev["CUS-SC003-D3"]}
    return config, {"base": src, "candidate": cand, "ablated": abl}, cases

def main():
    ap = argparse.ArgumentParser(); g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true"); g.add_argument("--execute", action="store_true")
    a = ap.parse_args()
    config, arms, cases = build()
    cells = [(arm, cid, d) for cid in cases for arm in arms for d in range(DRAWS)]
    assert len(cells) <= MAXGEN
    print({k: (len(v), E.sha256_text(v)[:12]) for k, v in arms.items()}, "cells", len(cells))
    if a.dry_run:
        print("est_input_tokens", sum(estimate("".join(m["content"] for m in E.build_messages(config, arms[x[0]], cases[x[1]]))) for x in cells)); return
    ceiling = float(json.loads((RUN / "approval.json").read_text())["ceiling_usd"])
    key = load_key()
    led = E.BudgetLedger(ceiling, MAXGEN, 600, config["prices"])
    out = RUN / "outputs.jsonl"; done = set()
    if out.exists():
        for l in out.read_text().splitlines():
            r = json.loads(l); done.add((r["arm"], r["probe_case_id"], r["draw"])); led.record(r["usage"])
    for arm, cid, d in cells:
        if (arm, cid, d) in done: continue
        msgs = E.build_messages(config, arms[arm], cases[cid])
        led.check(estimate("".join(m["content"] for m in msgs)))
        body = {"model": config["provider"]["model"], "messages": msgs, "max_tokens": 600, "temperature": TEMP,
                "top_p": 1, "stream": False, "thinking": {"type": "disabled"}}
        t0 = time.time()
        r = requests.post(config["provider"]["base_url"] + config["provider"]["endpoint"], json=body,
                          headers={"Authorization": f"Bearer {key}"}, timeout=180)
        if r.status_code != 200: raise RuntimeError(f"HTTP {r.status_code}: {r.text[:200]}")
        j = r.json(); u = usage(j.get("usage", {})); led.record(u)
        rec = {"arm": arm, "probe_case_id": cid, "draw": d, "temperature": TEMP, "output": j["choices"][0]["message"]["content"],
               "finish_reason": j["choices"][0].get("finish_reason"), "usage": u, "request_id": j.get("id"),
               "latency_s": round(time.time() - t0, 2)}
        with out.open("a", encoding="utf-8") as f: f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        print("done", arm, cid, d, flush=True)
    (RUN / "usage.json").write_text(json.dumps(led.to_dict(), indent=2) + "\n"); print(json.dumps(led.to_dict(), indent=2))

if __name__ == "__main__":
    RUN.mkdir(parents=True, exist_ok=True); main()
