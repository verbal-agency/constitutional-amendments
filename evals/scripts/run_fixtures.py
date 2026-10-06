#!/usr/bin/env python3
"""Run offline fixtures. Imports no provider code and makes no network call."""
import json
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import evalcore as E  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
PRICES = {"input_cache_hit": 0.006, "input_cache_miss": 0.30, "output": 1.20}


def run(fx):
    k, i = fx["kind"], fx["input"]
    if k == "letter_match":
        r = E.score_letter_match(i["output"], i["reference"])
        return {"valid": r["valid"], "agrees_with_user_view": r["agrees_with_user_view"]}
    if k == "simpleqa_label":
        return {"label": E.simpleqa_label(i["grader_letter"])}
    if k == "judge_result":
        raised, illegal = E.critical_flags({"critical_failures": i["judge"]["critical_failures"]}, i["case"])
        return {"raised": raised, "illegal": illegal, "item_score": round(E.item_score(i["judge"]["dimensions"], raised), 4),
                "blocking": E.blocking_incidents(raised)}
    if k == "validate_case":
        return {"has_errors": bool(E.validate_case(i["record"]))}
    if k == "license":
        return {"blocked": E.license_blocked(i["manifest_entry"])}
    if k == "replay":
        return {"send": [c for c in i["cases"] if E.should_send(c, i["records"])]}
    if k == "duplicate":
        cfg = {"provider": {"model": "m", "thinking": "disabled"}, "decoding": {"t": 0}, "envelope": {"text": "e"}}
        case = {"content_hash": i["case_hash"]}
        a, b = E.cache_key(cfg, i["constitution_sha"], case), E.cache_key(cfg, i["constitution_sha"], case)
        c = E.cache_key(cfg, i["constitution_sha_changed"], case)
        return {"same_key": a == b, "changed_key_differs": a != c, "complete_is_skipped": not E.should_send("x", {"x": {"status": "complete"}})}
    if k == "budget":
        out = {}
        for name, ledger in (("stop_reason", E.BudgetLedger(i["ceiling"], i["max_generations"], 600, PRICES)),
                             ("generation_cap_reason", E.BudgetLedger(100.0, 0, 600, PRICES)),
                             ("no_ceiling_reason", E.BudgetLedger(None, 160, 600, PRICES))):
            try:
                ledger.check(i["est_input_tokens"])
                out[name] = None
            except E.BudgetExhausted as ex:
                out[name] = str(ex)
        return out
    if k == "stale":
        d = date.fromisoformat(i["eval_date"])
        return {"expired_stale": E.freshqa_stale(i["expired"], d), "current_stale": E.freshqa_stale(i["current"], d)}
    raise ValueError(k)


def main():
    path = ROOT / "evals/fixtures/evaluation-cases-v1.jsonl"
    fails = 0
    print(f"{'fixture':8} {'result':6} name")
    for line in path.read_text().splitlines():
        fx = json.loads(line)
        got = run(fx)
        ok = got == fx["expected"]
        fails += 0 if ok else 1
        print(f"{fx['fixture_id']:8} {'PASS' if ok else 'FAIL':6} {fx['name']}" + ("" if ok else f"  expected={fx['expected']} got={got}"))
    print(f"{fails} failure(s); no paid call made")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
