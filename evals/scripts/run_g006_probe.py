#!/usr/bin/env python3
"""Run the bounded G006 development comparison.

This is exploratory evidence, not the frozen G010 comparison. It uses only
tracked development cases and compares the unchanged source constitution with
the source plus the G006 section-ready draft.
"""
import json
import os
import sys
import time
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
import evalcore as E  # noqa: E402
import sources as S  # noqa: E402

ROOT = S.ROOT
CEILING = 0.25
MAX_GENERATIONS = 12
CASE_IDS = [
    "CUS-SC003-D1",  # commercial instruction versus factual claim
    "CUS-SC003-D2",  # institutional policy versus contradictory evidence
    "CUS-SC003-D3",  # scope control versus urgent safety information
    "CUS-SC006-D1",  # commercial incentive and material omission
    "CUS-SC007-D1",  # self-sealing authority critique
    "CUS-SC007-D2",  # identity-conditioned disagreement
]


def load_key():
    if os.environ.get("DEEPSEEK_KEY"):
        return os.environ["DEEPSEEK_KEY"]
    p = ROOT / ".env"
    for line in p.read_text().splitlines():
        if line.startswith("DEEPSEEK_KEY="):
            return line.split("=", 1)[1].strip().strip("'\"")
    raise SystemExit("DEEPSEEK_KEY is unavailable")


def cfg():
    base = E.load_yaml(ROOT / "evals/configs/base-v1.yaml")
    base["caps"] = {**base["caps"], "max_generations": MAX_GENERATIONS}
    base["caps"]["approved_dollar_ceiling_usd"] = CEILING
    return base


def estimate(text):
    try:
        import tiktoken
        return max(len(tiktoken.get_encoding("cl100k_base").encode(text, disallowed_special=())), len(text) // 4)
    except Exception:
        return len(text) // 4


def usage(u):
    hit = u.get("prompt_cache_hit_tokens", 0)
    miss = u.get("prompt_cache_miss_tokens", u.get("prompt_tokens", 0) - hit)
    return {"prompt_tokens": u.get("prompt_tokens", hit + miss), "completion_tokens": u.get("completion_tokens", 0),
            "cache_hit": hit, "cache_miss": miss}


def call(cfg, key, messages):
    body = {"model": cfg["provider"]["model"], "messages": messages, "max_tokens": 600,
            "temperature": 0, "top_p": 1, "stream": False, "thinking": {"type": "disabled"}}
    t0 = time.time()
    r = requests.post(cfg["provider"]["base_url"] + cfg["provider"]["endpoint"], json=body,
                      headers={"Authorization": f"Bearer {key}"}, timeout=180)
    if r.status_code != 200:
        raise RuntimeError(f"HTTP {r.status_code}: {r.text[:300]}")
    data = r.json()
    return data, round(time.time() - t0, 2)


def main():
    config = cfg()
    dev = {}
    for line in (ROOT / "evals/datasets/custom-dev-v1.jsonl").read_text().splitlines():
        c = json.loads(line)
        dev[c["case_id"]] = c
    cases = [dev[cid] for cid in CASE_IDS]
    source = (ROOT / "20260120-constitution.md").read_text()
    draft = source + "\n\n--- G006 DEVELOPMENT DRAFT ---\n\n" + (ROOT / "amendments/G006-authority-and-incentives.md").read_text()
    arms = {"base": source, "g006-draft": draft}
    out_dir = ROOT / "evals/runs/g006-iteration-1/raw"
    out_dir.mkdir(parents=True, exist_ok=True)
    key = load_key()
    ledger = E.BudgetLedger(CEILING, MAX_GENERATIONS, 600, config["prices"])
    manifest = {"goal": "G006", "kind": "development", "model": config["provider"]["model"],
                "cases": CASE_IDS, "arms": list(arms), "ceiling_usd": CEILING, "records": []}
    for arm, constitution in arms.items():
        path = out_dir / f"{arm}.jsonl"
        existing = {}
        if path.exists():
            for line in path.read_text(encoding="utf-8").splitlines():
                if line.strip():
                    prior = json.loads(line)
                    existing[prior["case_id"]] = prior
                    ledger.record(prior.get("usage", {}))
        for case in cases:
            if case["case_id"] in existing:
                manifest["records"].append({"arm": arm, "case_id": case["case_id"], "cost_usd": existing[case["case_id"]].get("estimated_cost_usd", 0), "resumed": True})
                continue
            messages = E.build_messages(config, constitution, case)
            est = estimate("".join(m["content"] for m in messages))
            ledger.check(est)
            print(f"calling {arm} {case['case_id']} estimated_input_tokens={est}", flush=True)
            data, latency = call(config, key, messages)
            u = usage(data.get("usage", {}))
            ledger.record(u)
            text = data["choices"][0]["message"]["content"]
            rec = {"arm": arm, "case_id": case["case_id"], "output": text,
                   "usage": u, "estimated_cost_usd": round(E.usage_cost(u, config["prices"]), 6),
                   "latency_s": latency, "request_id": data.get("id")}
            with path.open("a", encoding="utf-8") as f:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            manifest["records"].append({"arm": arm, "case_id": case["case_id"], "cost_usd": rec["estimated_cost_usd"]})
    manifest["ledger"] = ledger.to_dict()
    (out_dir.parent / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
