#!/usr/bin/env python3
"""Deterministically select lean-v1 / smoke-v1 and write manifests.

  python3 evals/scripts/select_subset.py --build    # fetch pinned sources, select, write manifests + ignored cache
  python3 evals/scripts/select_subset.py --verify   # re-derive and compare with tracked manifests (no writes)

Algorithm (EVALUATION_PLAN.md): within each stratum order by SHA-256(dataset_id + source_item_id + seed), take the lowest.
Stratum quotas: n // k each; the n % k remainder goes to strata in ascending SHA-256(dataset_id + stratum + seed) order.
"""
import argparse
import hashlib
import json
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import sources as S  # noqa: E402
from validate_custom import DEV, HELD, load  # noqa: E402

ROOT = S.ROOT
MAN = ROOT / "evals/manifests"
CACHE_OUT = ROOT / "evals/cache/public-lean-v1.jsonl"

COUNTS = {"truthfulqa": 15, "simpleqa": 15, "freshqa": 20, "sycophancy": 20, "mask": 10, "xstest": 20, "harmbench": 10, "custom": 50}
SMOKE = {"truthfulqa": 2, "simpleqa": 2, "freshqa": 4, "sycophancy": 2, "mask": 1, "xstest": 2, "harmbench": 2}
SMOKE_CUSTOM = 15


def quotas(dataset_id, strata, n):
    strata = sorted(set(strata))
    base, extra = divmod(n, len(strata))
    order = sorted(strata, key=lambda s: S.select_hash(dataset_id + ":stratum", s))
    return {s: base + (1 if s in order[:extra] else 0) for s in strata}


def pick_items(dataset_id, items, n):
    by = defaultdict(list)
    for it in items:
        by[it["stratum"]].append(it)
    q = quotas(dataset_id, by.keys(), n)
    chosen = []
    for s, k in q.items():
        ranked = sorted(by[s], key=lambda it: S.select_hash(it["dataset_id"], it["source_item_id"]))
        if len(ranked) < k:
            raise SystemExit(f"{dataset_id}: stratum {s} has {len(ranked)} eligible items, needs {k}")
        chosen += ranked[:k]
    return chosen, q


def pick_pairs(dataset_id, pairs, n_pairs):
    by = defaultdict(list)
    for p in pairs:
        by[p["stratum"]].append(p)
    q = quotas(dataset_id, by.keys(), n_pairs)
    chosen = []
    for s, k in q.items():
        ranked = sorted(by[s], key=lambda p: S.select_hash(dataset_id, p["pair_id"]))
        if len(ranked) < k:
            raise SystemExit(f"{dataset_id}: stratum {s} has {len(ranked)} eligible pairs, needs {k}")
        chosen += ranked[:k]
    return chosen, q


def build():
    entries, meta = [], {}
    tq = S.load_truthfulqa(); sel, q = pick_items("truthfulqa", tq, 15)
    meta["truthfulqa"] = dict(eligible=len(tq), strata=dict(Counter(i["stratum"] for i in tq)), quotas=q, selected=sel)
    sq = S.load_simpleqa(); sel2, q2 = pick_items("simpleqa", sq, 15)
    meta["simpleqa"] = dict(eligible=len(sq), strata=dict(Counter(i["stratum"] for i in sq)), quotas=q2, selected=sel2)
    fq, excl = S.load_freshqa(); sel3, q3 = pick_items("freshqa", fq, 20)
    meta["freshqa"] = dict(eligible=len(fq), strata=dict(Counter(i["stratum"] for i in fq)), quotas=q3, selected=sel3, excluded_ineligible=excl)
    sy = S.load_sycophancy(); psel, q4 = pick_pairs("sycophancy", sy, 10)
    meta["sycophancy"] = dict(eligible=len(sy), strata=dict(Counter(p["stratum"] for p in sy)), quotas=q4, selected=[c for p in psel for c in p["cases"]], unit="pair")
    mk = S.load_mask(); sel5, q5 = pick_items("mask", mk, 10)
    meta["mask"] = dict(eligible=len(mk), strata=dict(Counter(i["stratum"] for i in mk)), quotas=q5, selected=sel5)
    xs = S.load_xstest(); xsel, q6 = pick_pairs("xstest", xs, 10)
    meta["xstest"] = dict(eligible=len(xs), strata=dict(Counter(p["stratum"] for p in xs)), quotas=q6, selected=[c for p in xsel for c in p["cases"]], unit="pair")
    hb = S.load_harmbench(); sel7, q7 = pick_items("harmbench", hb, 10)
    meta["harmbench"] = dict(eligible=len(hb), strata=dict(Counter(i["stratum"] for i in hb)), quotas=q7, selected=sel7)

    smoke_ids = set()
    for ds, m in meta.items():
        sel = m["selected"]
        if m.get("unit") == "pair":
            pids = sorted({c["pair_id"] for c in sel}, key=lambda p: S.select_hash(ds, p))[: SMOKE[ds] // 2]
            smoke_ids |= {c["case_id"] for c in sel if c["pair_id"] in pids}
        else:
            if ds == "freshqa":
                got = []
                for s in sorted({c["stratum"] for c in sel}):
                    got.append(min((c for c in sel if c["stratum"] == s), key=lambda c: S.select_hash(c["dataset_id"], c["source_item_id"])))
            else:
                got = sorted(sel, key=lambda c: S.select_hash(c["dataset_id"], c["source_item_id"]))[: SMOKE[ds]]
            smoke_ids |= {c["case_id"] for c in got}
    public = [c for m in meta.values() for c in m["selected"]]

    dev = load(DEV)
    held = load(HELD)
    first = {sc: min((r for r in dev if r["scenario_ids"][0] == sc), key=lambda r: S.select_hash("custom", r["case_id"])) for sc in {r["scenario_ids"][0] for r in dev}}
    rest = sorted((r for r in dev if r not in first.values()), key=lambda r: S.select_hash("custom", r["case_id"]))
    smoke_custom = {r["case_id"] for r in list(first.values()) + rest[: SMOKE_CUSTOM - len(first)]}

    lean = []
    for c in public:
        lean.append({"case_id": c["case_id"], "dataset_id": c["dataset_id"], "source_item_id": c["source_item_id"], "split": "public",
                     "stratum": c["stratum"], "pair_id": c["pair_id"], "content_hash": c["content_hash"], "in_smoke": c["case_id"] in smoke_ids})
    for r in dev + held:
        lean.append({"case_id": r["case_id"], "dataset_id": r["dataset_id"], "source_item_id": "custom", "split": r["split"],
                     "stratum": r["scenario_ids"][0], "pair_id": None, "content_hash": r["content_hash"], "in_smoke": r["case_id"] in smoke_custom})
    lean.sort(key=lambda e: (e["split"] != "public", e["case_id"]))
    return meta, public, lean


def check_invariants(lean):
    errs = []
    if len(lean) != 160:
        errs.append(f"lean-v1 has {len(lean)} cases, expected 160")
    if len({e["case_id"] for e in lean}) != 160:
        errs.append("duplicate case ids in lean-v1")
    pub = [e for e in lean if e["split"] == "public"]
    if len(pub) != 110:
        errs.append(f"public count {len(pub)} != 110")
    cnt = Counter(e["dataset_id"].split("-")[0] for e in pub)
    for ds in ("truthfulqa", "simpleqa", "freshqa", "sycophancy", "mask", "xstest", "harmbench"):
        if cnt[ds] != COUNTS[ds]:
            errs.append(f"{ds}: {cnt[ds]} != {COUNTS[ds]}")
    if sum(e["in_smoke"] for e in lean) != 30:
        errs.append(f"smoke has {sum(e['in_smoke'] for e in lean)} cases, expected 30")
    if sum(e["in_smoke"] for e in lean if e["split"] == "heldout"):
        errs.append("smoke contains held-out cases")
    return errs


LICENSES = {
    "truthfulqa": ("Apache-2.0", "metadata and item ids only; data fetched at run time", "https://github.com/sylinrl/TruthfulQA (canonical upstream; EVALUATION_PLAN.md links koppula/TruthfulQA)", "d71c110897f5d31c5d7f309e7bc316c152f6f031", "2025-01-16"),
    "simpleqa": ("MIT (openai/simple-evals)", "metadata and item ids only; data fetched at run time", "https://github.com/openai/simple-evals ; data https://openaipublic.blob.core.windows.net/simple-evals/simple_qa_test_set.csv", "dated snapshot: file SHA-256 below (blob is unversioned); repo commit 652c89d0ca9df547706735883097e9537d40dc47", "2026-04-22"),
    "freshqa": ("Apache-2.0", "metadata and item ids only; data fetched at run time", "https://github.com/freshllms/freshqa ; sheet 1_8mi-yuK30mvoDJu1KQXD6ODem7MKMcIgVAwDSzJkjM", "dated snapshot: FreshQA April 21, 2026 sheet, file SHA-256 below; repo commit 7d2d3683991916f3633e480548a6aa5c9a62e3db", "2026-04-21"),
    "sycophancy": ("CC-BY-4.0", "metadata and item ids only; attribution: Anthropic, anthropics/evals", "https://github.com/anthropics/evals/tree/main/sycophancy", "84fcc677e52e1902d696c32cd1a6b663e70d3993", "2023-01-03"),
    "mask": ("MIT (code); dataset card declares no explicit license", "ids only; benchmark canary string forbids training use; do not vendor", "https://huggingface.co/datasets/cais/MASK", "4602b84dd9e2ca05c6e1eafbc14e556e908ac1bb", "2025-03-20"),
    "xstest": ("CC-BY-4.0", "metadata and item ids only; attribution: Rottger et al.", "https://github.com/paul-rottger/xstest", "d7bb5bd738c1fcbc36edd83d5e7d1b71a3e2d84d", "2025-02-24"),
    "harmbench": ("MIT", "ids only; harmful behavior text is not redistributed", "https://github.com/centerforaisafety/HarmBench", "8e1604d1171fe8a48d8febecd22f600e462bdcdd", "2024-08-05"),
}
LICENSE_STATUS = {"mask": "unclear: repo code is MIT, dataset card has no license; decision required before use (see evals/README.md)"}
NATIVE_ID = {"truthfulqa": "row index in pinned TruthfulQA.csv", "simpleqa": "row index in snapshot CSV", "freshqa": "id (TEST split)",
             "sycophancy": "row index in source jsonl; pair = same question tail with opposite user-matching letter",
             "mask": "task_id within config", "xstest": "id (xstest_prompts.csv); pair = safe type T with unsafe contrast_T",
             "harmbench": "BehaviorID (FunctionalCategory=standard)"}
SCORER = {
    "truthfulqa": "project adapter: judge compares answer to best/correct/incorrect reference lists (native BLEURT/GPT-judge not run)",
    "simpleqa": "native grader rubric (CORRECT / INCORRECT / NOT_ATTEMPTED) run by the approved judge model",
    "freshqa": "project adapter modelled on FreshEval (relaxed): judge checks against reference answers and the as-of date",
    "sycophancy": "native deterministic: first answer letter vs answer_matching_behavior; pair-level agreement-with-user rate",
    "mask": "project adapter: single-turn only; judge classifies whether the response asserts the proposition contradicted by ground_truth. Belief elicitation omitted (generation cap)",
    "xstest": "native three-way label (full compliance / full refusal / partial) via judge classifier",
    "harmbench": "project adapter: judge classifies operational compliance (native Llama-2 classifier not run)",
}
LIMITS = {
    "truthfulqa": "Likely in training data; item ids are row indexes; judge replaces native metrics.",
    "simpleqa": "Unversioned blob: identified by file hash. Native grader needs an LLM judge.",
    "freshqa": "Living dataset; fast-changing answers go stale. Prompts are anchored to the snapshot date; items whose next_review date is before the evaluation start were excluded.",
    "sycophancy": "Multiple-choice stance probes on survey-style personas; measures agreement with a stated view, not free-form sycophancy.",
    "mask": "Honesty vs accuracy is only partially separated without belief elicitation. provided_facts items give the truth in context so contradiction is a lie; disinformation/continuations items rely on well-known ground truth.",
    "xstest": "Prompt set predates current models; contrast pairs are by type, not by focus.",
    "harmbench": "Standard behaviors only (copyright/contextual excluded); classifier is a judge, not the native one.",
}


def write_manifests(meta, public, lean, hashes):
    MAN.mkdir(parents=True, exist_ok=True)
    doc = {"manifest_version": 1, "selection_seed": S.SEED, "selection_algorithm": "hash-order-within-stratum-v1", "built_on": date.today().isoformat(),
           "source_file_sha256": hashes, "datasets": {}}
    for ds, m in meta.items():
        lic, redist, url, rev, rev_date = LICENSES[ds]
        doc["datasets"][ds] = {
            "dataset_id": ds, "name": ds, "source_url": url, "upstream_revision": rev, "upstream_revision_date": rev_date,
            "retrieved_at": date.today().isoformat(), "license": lic, "redistribution_decision": redist, "license_status": LICENSE_STATUS.get(ds, "supported"),
            "native_id_field": NATIVE_ID[ds], "eligible_count": m["eligible"], "eligible_strata": m["strata"], "stratum_quotas": m["quotas"],
            "selected_count": len(m["selected"]), "selected_ids": [c["source_item_id"] for c in m["selected"]],
            "scorer": SCORER[ds], "known_limitations": LIMITS[ds],
        }
        if "excluded_ineligible" in m:
            doc["datasets"][ds]["excluded_ineligible_ids"] = m["excluded_ineligible"]
    (MAN / "datasets-v1.yaml").write_text(yaml.safe_dump(doc, sort_keys=False, width=140), encoding="utf-8")
    with open(MAN / "lean-v1.jsonl", "w", encoding="utf-8") as f:
        for e in lean:
            f.write(json.dumps(e, sort_keys=True, ensure_ascii=False) + "\n")
    with open(MAN / "smoke-v1.jsonl", "w", encoding="utf-8") as f:
        for e in lean:
            if e["in_smoke"]:
                f.write(json.dumps(e, sort_keys=True, ensure_ascii=False) + "\n")
    CACHE_OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(CACHE_OUT, "w", encoding="utf-8") as f:
        for c in public:
            f.write(json.dumps(c, sort_keys=True, ensure_ascii=False) + "\n")


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--build", action="store_true")
    g.add_argument("--verify", action="store_true")
    a = ap.parse_args()
    hashes = S.file_hashes()
    meta, public, lean = build()
    errs = check_invariants(lean)
    for e in errs:
        print("ERROR", e)
    if errs:
        return 1
    if a.build:
        write_manifests(meta, public, lean, hashes)
        print(f"wrote manifests: lean={len(lean)} smoke={sum(e['in_smoke'] for e in lean)} public={len(public)}")
        return 0
    doc = yaml.safe_load((MAN / "datasets-v1.yaml").read_text(encoding="utf-8"))
    ok = doc["source_file_sha256"] == hashes
    tracked = [json.loads(l) for l in (MAN / "lean-v1.jsonl").read_text(encoding="utf-8").splitlines()]
    same = tracked == json.loads(json.dumps(lean, sort_keys=True))
    print(f"source hashes match: {ok}; lean-v1 rebuild identical: {same}")
    return 0 if ok and same else 1


if __name__ == "__main__":
    sys.exit(main())
