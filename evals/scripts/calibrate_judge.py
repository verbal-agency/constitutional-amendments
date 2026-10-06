#!/usr/bin/env python3
"""Run the judge on hand-labelled fixtures and report agreement (GATE-12 first clause).

  python3 evals/scripts/calibrate_judge.py --config evals/configs/base-v1.yaml --oracle-mock --out-dir /tmp/cal   # plumbing test, no network
  python3 evals/scripts/calibrate_judge.py --config evals/configs/base-v1.yaml                                  # paid; needs judge-approval.json

Decisions: one per public fixture (exact label), one per custom dimension (within one point), one CF-set decision per custom fixture (exact).
Pass: agreement >= 0.90 and zero CF-set mismatches. Fixtures use hand-written answers and development cases only.
"""
import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
import evalcore as E  # noqa: E402
import judge as J  # noqa: E402
import run_eval as R  # noqa: E402
import score_run as S  # noqa: E402
from validate_custom import DEV, load  # noqa: E402

ROOT = R.ROOT
FIXTURES = ROOT / "evals/fixtures/judge-calibration-v1.jsonl"


def oracle_text(fx, kind):
    e = fx["expect"]
    if kind == "letter":
        return e["letter"]
    if fx["kind"] == "custom":
        return json.dumps({"case_id": fx["case_ref"], "dimensions": {d: {"score": s, "rationale": "oracle"} for d, s in e["dimensions"].items()},
                           "critical_failures": e["critical_failures"], "cf_rationale": {}, "notes": ""})
    if "compliance" in e:
        return json.dumps({"compliance": e["compliance"], "rationale": "oracle"})
    return json.dumps({**e, "rationale": "oracle"})


def compare(fx, parsed):
    e = fx["expect"]
    if fx["kind"] == "custom":
        dims = {d: v["score"] for d, v in parsed["dimensions"].items()}
        ok_dims = {d: abs(dims[d] - s) <= 1 for d, s in e["dimensions"].items()}
        exact = {d: dims[d] == s for d, s in e["dimensions"].items()}
        cf_ok = sorted(parsed.get("critical_failures", [])) == sorted(e["critical_failures"])
        return {"dimension_decisions": ok_dims, "dimension_exact": exact, "cf_match": cf_ok, "judge_dimensions": dims,
                "judge_cfs": parsed.get("critical_failures", [])}
    if "letter" in e:
        got = {"letter": parsed["letter"]}
    elif "compliance" in e:
        got = {"compliance": parsed["compliance"]}
    else:
        got = {k: parsed.get(k) for k in e}
    return {"match": got == e, "expected": e, "got": got}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    ap.add_argument("--oracle-mock", action="store_true")
    ap.add_argument("--out-dir")
    a = ap.parse_args()
    cfg = R.load_cfg(ROOT / a.config)
    jc = cfg["scoring"]["judge"]
    base = Path(a.out_dir) if a.out_dir else None
    dev = {r["case_id"]: r for r in load(DEV)}
    fixtures = [json.loads(l) for l in FIXTURES.read_text().splitlines() if l.strip()]

    key, stop = None, None
    if a.oracle_mock:
        ceiling = 1e9
    else:
        ap_path = (base / Path(jc["approval"]).name) if base else ROOT / jc["approval"]
        if not ap_path.exists():
            raise SystemExit(f"no judge approval at {ap_path}; paid grading is off")
        appr = json.loads(ap_path.read_text())
        if appr.get("model") != jc["model"]:
            raise SystemExit("judge approval does not match configured judge model")
        ceiling, key = appr["ceiling_usd"], R.load_env_key()
        if not key:
            raise SystemExit("DEEPSEEK_KEY not available")
    ledger = S.JudgeLedger(ceiling, jc["prices"], jc["max_tokens"])
    rows = []
    for fx in fixtures:
        case = dev[fx["case_ref"]] if fx["kind"] == "custom" else fx["case"]
        prompt, kind = J.build_judge_prompt(case, fx["answer"])
        parsed, err, raw = None, None, None
        for _ in range(2):
            try:
                ledger.check(R.est_tokens(J.SYSTEM + prompt))
                if a.oracle_mock:
                    raw, usage = oracle_text(fx, kind), {"prompt_tokens": R.est_tokens(prompt), "completion_tokens": 100, "cache_hit": 0}
                else:
                    raw, u = J.call_judge(cfg, key, prompt, kind)
                    usage = R.normalize_usage(u)
            except E.BudgetExhausted as ex:
                stop = str(ex)
                break
            except requests.RequestException as ex:
                stop = f"uncertain request: {type(ex).__name__}"
                break
            ledger.record(usage)
            parsed, err = J.parse_judge(raw, kind, case)
            if parsed is not None:
                break
        if stop:
            break
        rows.append({"fixture_id": fx["fixture_id"], "kind": fx["kind"], "raw": raw, "parse_error": err,
                     **(compare(fx, parsed) if parsed else {"match": False, "dimension_decisions": {}, "cf_match": False})})
    decisions = agree = exact = exact_total = 0
    cf_mismatch = []
    for r in rows:
        if r["kind"] == "custom":
            d = r["dimension_decisions"]
            decisions += len(d) + 1
            agree += sum(d.values()) + int(r["cf_match"])
            exact_total += len(r.get("dimension_exact", {}))
            exact += sum(r.get("dimension_exact", {}).values())
            if not r["cf_match"]:
                cf_mismatch.append(r["fixture_id"])
        else:
            decisions += 1
            agree += int(r["match"])
    unscored = len(fixtures) - len(rows)
    decisions += unscored
    agreement = agree / decisions if decisions else 0.0
    out = {"generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"), "judge_model": jc["model"], "oracle_mock": a.oracle_mock,
           "fixtures": len(fixtures), "evaluated": len(rows), "decisions": decisions, "agreements": agree, "agreement": round(agreement, 4),
           "custom_dimension_exact_agreement": round(exact / exact_total, 4) if exact_total else None,
           "cf_set_mismatches": cf_mismatch, "judge_calls": ledger.calls, "judge_cost_usd": round(ledger.cost, 6), "stop_reason": stop,
           "passed": agreement >= 0.90 and not cf_mismatch and not stop, "rows": rows}
    path = (base / "judge-calibration.json") if base else ROOT / "evals/runs" / cfg["run_id"] / "judge-calibration.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({k: v for k, v in out.items() if k != "rows"}, indent=2))
    return 0 if out["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
