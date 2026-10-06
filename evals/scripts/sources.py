"""Pinned public-benchmark sources: fetch with hash recording, and normalize into EvalCase-shaped dicts."""
import ast
import hashlib
import io
import json
import re
from pathlib import Path

import pandas as pd
import requests

ROOT = Path(__file__).resolve().parents[2]
CACHE = ROOT / "evals/cache/sources"
SEED = "constitutional-amendments-lean-v1"
FRESHQA_AS_OF = "April 21, 2026"
GH = "https://raw.githubusercontent.com"
HF = "https://huggingface.co/datasets/cais/MASK/resolve/4602b84dd9e2ca05c6e1eafbc14e556e908ac1bb"

FILES = {
    "truthfulqa": ("truthfulqa.csv", f"{GH}/sylinrl/TruthfulQA/d71c110897f5d31c5d7f309e7bc316c152f6f031/TruthfulQA.csv"),
    "simpleqa": ("simpleqa.csv", "https://openaipublic.blob.core.windows.net/simple-evals/simple_qa_test_set.csv"),
    "freshqa": ("freshqa.csv", "https://docs.google.com/spreadsheets/d/1_8mi-yuK30mvoDJu1KQXD6ODem7MKMcIgVAwDSzJkjM/export?format=csv"),
    "syc_nlp": ("syc_nlp.jsonl", f"{GH}/anthropics/evals/84fcc677e52e1902d696c32cd1a6b663e70d3993/sycophancy/sycophancy_on_nlp_survey.jsonl"),
    "syc_phil": ("syc_phil.jsonl", f"{GH}/anthropics/evals/84fcc677e52e1902d696c32cd1a6b663e70d3993/sycophancy/sycophancy_on_philpapers2020.jsonl"),
    "syc_pol": ("syc_pol.jsonl", f"{GH}/anthropics/evals/84fcc677e52e1902d696c32cd1a6b663e70d3993/sycophancy/sycophancy_on_political_typology_quiz.jsonl"),
    "mask_provided_facts": ("mask_provided_facts.parquet", f"{HF}/provided_facts/test-00000-of-00001.parquet"),
    "mask_disinformation": ("mask_disinformation.parquet", f"{HF}/disinformation/test-00000-of-00001.parquet"),
    "mask_continuations": ("mask_continuations.parquet", f"{HF}/continuations/test-00000-of-00001.parquet"),
    "xstest": ("xstest_prompts.csv", f"{GH}/paul-rottger/xstest/d7bb5bd738c1fcbc36edd83d5e7d1b71a3e2d84d/xstest_prompts.csv"),
    "harmbench": ("harmbench_behaviors_text_all.csv", f"{GH}/centerforaisafety/HarmBench/8e1604d1171fe8a48d8febecd22f600e462bdcdd/data/behavior_datasets/harmbench_behaviors_text_all.csv"),
}


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def select_hash(dataset_id, item_id):
    return hashlib.sha256((dataset_id + item_id + SEED).encode("utf-8")).hexdigest()


def case_hash(record):
    body = dict(record)
    body["content_hash"] = ""
    blob = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()


def fetch(key, force=False):
    name, url = FILES[key]
    path = CACHE / name
    if force or not path.exists():
        CACHE.mkdir(parents=True, exist_ok=True)
        r = requests.get(url, timeout=120)
        r.raise_for_status()
        path.write_bytes(r.content)
    return path


def file_hashes():
    return {k: sha256_bytes(fetch(k).read_bytes()) for k in FILES}


def _case(dataset_id, item_id, stratum, prompt, reference, scorer, system=None, risk="medium", pair_id=None):
    rec = {
        "case_id": f"{dataset_id}:{item_id}",
        "dataset_id": dataset_id,
        "source_item_id": item_id,
        "scenario_ids": [],
        "split": "public",
        "stratum": stratum,
        "pair_id": pair_id,
        "system_context": system,
        "prompt": prompt,
        "evidence_packet": None,
        "reference": reference,
        "scorer": scorer,
        "risk_class": risk,
        "max_output_tokens": 600,
        "content_hash": "",
    }
    rec["content_hash"] = case_hash(rec)
    return rec


def load_truthfulqa():
    df = pd.read_csv(fetch("truthfulqa"))
    out = []
    for i, r in df.iterrows():
        ref = {"best_answer": r["Best Answer"], "correct_answers": [s.strip() for s in str(r["Correct Answers"]).split(";")],
               "incorrect_answers": [s.strip() for s in str(r["Incorrect Answers"]).split(";")], "category": r["Category"], "type": r["Type"]}
        out.append(_case("truthfulqa", f"row-{i:04d}", r["Category"], r["Question"], ref, "judge:truthfulqa-v1", risk="low"))
    return out


def load_simpleqa():
    df = pd.read_csv(fetch("simpleqa"))
    out = []
    for i, r in df.iterrows():
        topic = ast.literal_eval(r["metadata"]).get("topic", "unknown")
        out.append(_case("simpleqa", f"row-{i:04d}", topic, r["problem"], {"gold_target": r["answer"]}, "judge:simpleqa-grader-v1", risk="low"))
    return out


def _freshqa_eligible(r):
    nr = str(r["next_review"])
    if re.fullmatch(r"\d\d/\d\d/\d{4}", nr):
        m, d, y = nr.split("/")
        return (int(y), int(m), int(d)) >= (2026, 10, 5)
    return True


def load_freshqa():
    df = pd.read_csv(fetch("freshqa"), skiprows=2)
    df = df[df["split"] == "TEST"]
    out, excluded = [], []
    for _, r in df.iterrows():
        if not _freshqa_eligible(r):
            excluded.append(str(r["id"]))
            continue
        fp = str(r["false_premise"]).upper() == "TRUE"
        stratum = "false-premise" if fp else r["fact_type"]
        answers = [str(r[f"answer_{k}"]) for k in range(10) if pd.notna(r[f"answer_{k}"])]
        ref = {"answers": answers, "false_premise": fp, "fact_type": r["fact_type"], "effective_year": str(r["effective_year"]),
               "next_review": str(r["next_review"]), "note": None if pd.isna(r["note"]) else str(r["note"]), "as_of": FRESHQA_AS_OF}
        prompt = f"Assume today's date is {FRESHQA_AS_OF}. {r['question']}"
        out.append(_case("freshqa", f"id-{int(r['id']):04d}", stratum, prompt, ref, "judge:freshqa-v1", risk="low"))
    return out, excluded


SYC_MARKERS = ["What is your view on the following topic:", "Do you agree or disagree with the following claim", "If you had to choose, would you rather have"]


def load_sycophancy():
    """Return opposing-view pairs: same question tail, different user-matching answer."""
    pairs = []
    for key, name in (("syc_nlp", "nlp-survey"), ("syc_phil", "philpapers2020"), ("syc_pol", "political-typology")):
        rows = [json.loads(l) for l in fetch(key).read_text(encoding="utf-8").splitlines() if l.strip()]
        groups = {}
        for idx, r in enumerate(rows):
            q = r["question"]
            pos = [q.find(m) for m in SYC_MARKERS if q.find(m) >= 0]
            if key == "syc_pol":
                pos = [q.find("\n (A)")] if q.find("\n (A)") >= 0 else []
            if not pos:
                continue
            tail = q[min(pos):]
            letter = r["answer_matching_behavior"].strip()
            groups.setdefault(tail, {}).setdefault(letter, []).append((idx, r))
        for tail, sides in groups.items():
            if len(sides) < 2:
                continue
            pair_key = hashlib.sha256(tail.encode("utf-8")).hexdigest()[:12]
            cases = []
            for letter in sorted(sides):
                idx, r = min(sides[letter], key=lambda t: select_hash(f"sycophancy-{name}", f"row-{t[0]:05d}"))
                ref = {"user_view_answer": letter, "other_answers": [a.strip() for a in r["answer_not_matching_behavior"]],
                       "source_file": name, "user_affiliation": r.get("user_affiliation")}
                cases.append(_case(f"sycophancy-{name}", f"row-{idx:05d}", name, r["question"], ref, "deterministic:letter-match-v1",
                                   risk="low", pair_id=f"sycophancy-{name}:pair-{pair_key}"))
            pairs.append({"pair_id": cases[0]["pair_id"], "stratum": name, "cases": cases[:2]})
    return pairs


def load_mask():
    out = []
    for cfg in ("provided_facts", "disinformation", "continuations"):
        df = pd.read_parquet(fetch(f"mask_{cfg}"))
        for _, r in df.iterrows():
            ref = {"ground_truth": r["ground_truth"], "proposition": r["proposition"], "config": cfg, "type": r["type"]}
            out.append(_case("mask", f"{cfg}:{r['task_id']}", cfg, r["user_prompt"], ref, "judge:mask-honesty-v1",
                             system=r["system_prompt"] if isinstance(r["system_prompt"], str) and r["system_prompt"].strip() else None))
    return out


def load_xstest():
    df = pd.read_csv(fetch("xstest"))
    contrast = {t: f"contrast_{t}" for t in ("definitions", "figurative_language", "historical_events", "homonyms", "safe_contexts", "safe_targets")}
    contrast.update({"nons_group_real_discr": "contrast_discr", "real_group_nons_discr": "contrast_discr",
                     "privacy_fictional": "contrast_privacy", "privacy_public": "contrast_privacy"})
    pairs, used = [], set()
    for t in sorted(contrast):
        def pick(sub, label):
            cand = [(select_hash("xstest", f"id-{int(r['id']):03d}"), r) for _, r in sub.iterrows() if int(r["id"]) not in used]
            _, r = min(cand, key=lambda x: x[0])
            used.add(int(r["id"]))
            return _case("xstest", f"id-{int(r['id']):03d}", r["type"], r["prompt"],
                         {"label": label, "type": r["type"], "focus": None if pd.isna(r["focus"]) else r["focus"]},
                         "judge:xstest-compliance-v1", risk="low" if label == "safe" else "medium", pair_id=f"xstest:pair-{t}")
        safe = pick(df[(df["type"] == t) & (df["label"] == "safe")], "safe")
        unsafe = pick(df[(df["type"] == contrast[t]) & (df["label"] == "unsafe")], "unsafe")
        pairs.append({"pair_id": f"xstest:pair-{t}", "stratum": t, "cases": [safe, unsafe]})
    return pairs


def load_harmbench():
    df = pd.read_csv(fetch("harmbench"))
    df = df[df["FunctionalCategory"] == "standard"]
    out = []
    for _, r in df.iterrows():
        out.append(_case("harmbench", r["BehaviorID"], r["SemanticCategory"], r["Behavior"],
                         {"semantic_category": r["SemanticCategory"]}, "judge:harmbench-compliance-v1", risk="high"))
    return out
