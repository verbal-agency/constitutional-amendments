#!/usr/bin/env python3
"""Run the 140-case non-held-out G006 development comparison.

This is exploratory evidence before G009/G010. It uses the frozen lean-v1
public and development cases, excludes held-out cases, and compares the
immutable source with the source plus the G006 draft.
"""
import json
import os
import sys
import time
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
import evalcore as E  # noqa: E402
import run_eval as R  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
CEILING = 5.00
MAX_GENERATIONS = 280


def key():
    return R.load_env_key()


def usage(u):
    hit = u.get("prompt_cache_hit_tokens", 0)
    miss = u.get("prompt_cache_miss_tokens", u.get("prompt_tokens", 0) - hit)
    return {"prompt_tokens": u.get("prompt_tokens", hit + miss), "completion_tokens": u.get("completion_tokens", 0),
            "cache_hit": hit, "cache_miss": miss}


def call(cfg, token, messages):
    body = {"model": cfg["provider"]["model"], "messages": messages, "max_tokens": cfg["decoding"]["max_tokens"],
            "temperature": cfg["decoding"]["temperature"], "top_p": cfg["decoding"]["top_p"], "stream": False,
            "thinking": {"type": "disabled"}}
    t0 = time.time()
    last = None
    for retry in range(2):
        try:
            response = requests.post(cfg["provider"]["base_url"] + cfg["provider"]["endpoint"], json=body,
                                     headers={"Authorization": f"Bearer {token}"}, timeout=180)
            if response.status_code != 200:
                raise RuntimeError(f"HTTP {response.status_code}: {response.text[:300]}")
            return response.json(), round(time.time() - t0, 2), retry
        except (requests.RequestException, RuntimeError) as exc:
            last = exc
            if retry == 0:
                time.sleep(2)
    raise last


def main():
    cfg = R.load_cfg(ROOT / "evals/configs/base-v1.yaml")
    cases = [c for c in R.load_cases(cfg, "all") if c["split"] != "heldout"]
    assert len(cases) == 140, len(cases)
    source = (ROOT / "20260120-constitution.md").read_text(encoding="utf-8")
    draft = source + "\n\n--- G006 DEVELOPMENT DRAFT ---\n\n" + (ROOT / "amendments/G006-authority-and-incentives.md").read_text(encoding="utf-8")
    arms = {"base": source, "g006-draft": draft}
    run_dir = ROOT / "evals/runs/g006-iteration-140"
    raw_dir = run_dir / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    (raw_dir / "g006-draft-constitution.md").write_text(draft, encoding="utf-8")
    token = key()
    if not token:
        raise SystemExit("DEEPSEEK_KEY is unavailable")
    ledger = E.BudgetLedger(CEILING, MAX_GENERATIONS, cfg["decoding"]["max_tokens"], cfg["prices"])
    manifest = {"goal": "G006", "kind": "development", "model": cfg["provider"]["model"],
                "cases_per_arm": len(cases), "calls_planned": len(cases) * 2, "heldout_cases": 0,
                "ceiling_usd": CEILING, "arms": list(arms), "records": []}
    for arm, constitution in arms.items():
        path = raw_dir / f"{arm}.jsonl"
        existing = {}
        if path.exists():
            for line in path.read_text(encoding="utf-8").splitlines():
                if line.strip():
                    prior = json.loads(line)
                    existing[prior["case_id"]] = prior
                    ledger.record(prior.get("usage", {}))
        for index, case in enumerate(cases, 1):
            if case["case_id"] in existing:
                manifest["records"].append({"arm": arm, "case_id": case["case_id"], "resumed": True})
                continue
            messages = E.build_messages(cfg, constitution, case)
            estimated = R.est_tokens("".join(m["content"] for m in messages))
            ledger.check(estimated)
            print(f"calling {arm} {index}/{len(cases)} {case['case_id']}", flush=True)
            data, latency, retry_count = call(cfg, token, messages)
            normalized = usage(data.get("usage", {}))
            ledger.record(normalized, retry=retry_count > 0)
            rec = {"run_id": "g006-iteration-140", "arm": arm, "case_id": case["case_id"], "status": "complete",
                   "output": data["choices"][0]["message"]["content"], "finish_reason": data["choices"][0].get("finish_reason"),
                   "usage": normalized, "retry_count": retry_count, "estimated_cost_usd": round(E.usage_cost(normalized, cfg["prices"]), 6),
                   "latency_s": latency, "request_id": data.get("id"), "prompt_hash": E.prompt_hash(messages)}
            with path.open("a", encoding="utf-8") as handle:
                handle.write(json.dumps(rec, ensure_ascii=False) + "\n")
            manifest["records"].append({"arm": arm, "case_id": case["case_id"], "cost_usd": rec["estimated_cost_usd"]})
    manifest["ledger"] = ledger.to_dict()
    (run_dir / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
