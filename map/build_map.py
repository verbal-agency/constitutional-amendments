#!/usr/bin/env python3
"""Build and validate the constitution structure map.

Merges records that already exist in this repository into one data file:

  20260120-constitution.md              pinned source (never modified)
  audits/truth-seeking-audit.md         51 passage-level audit records
  audits/philosophical-patterns.md      pattern register
  framework/G003-traceability.md        audit -> epistemic-principle matrix
  framework/epistemic-framework.md      EP-01..EP-07
  framework/G004-core-hierarchy.md      CR-01..CR-12
  framework/principles-v1.yaml          G006 applied principles
  map/candidates.yaml                   candidates and their evidence status

Usage:
  python3 map/build_map.py           regenerate map/structure-map.json
  python3 map/build_map.py --check   fail if the committed file is stale or
                                     any validation check fails

The output is deterministic: no timestamps, sorted keys, stable ordering.
A mapping is a provenance link, not a causal or normative claim.
"""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "map" / "structure-map.json"
GENERATOR = "map/build_map.py:v1"
SOURCE_PATH = "20260120-constitution.md"
SOURCE_SHA256 = "251440a71a9068dd43bfaab2b8694d6e2a4f519c403f1b9a70785f830d05f327"
EVIDENCE_STATUSES = {"unproven", "no_detectable_difference", "difference_supported"}


def sha256_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


class Checks:
    def __init__(self):
        self.items = []

    def add(self, name, ok, detail=""):
        self.items.append({"name": name, "ok": bool(ok), "detail": detail})

    @property
    def ok(self):
        return all(c["ok"] for c in self.items)


def ids(text, pattern):
    return sorted(set(re.findall(pattern, text)))


def md_sections(text, level):
    """Yield (heading, body) for each heading of exactly `level` hashes."""
    marker = "#" * level + " "
    heading, body = None, []
    for line in text.splitlines():
        if line.startswith(marker):
            if heading is not None:
                yield heading, "\n".join(body)
            heading, body = line[len(marker):].strip(), []
        elif re.match(r"#{1,%d} " % level, line):
            if heading is not None:
                yield heading, "\n".join(body)
            heading, body = None, []
        elif heading is not None:
            body.append(line)
    if heading is not None:
        yield heading, "\n".join(body)


def bullet_fields(body):
    fields = {}
    for m in re.finditer(r"^- \**([A-Za-z0-9 ,/-]+?):\** (.*)$", body, re.M):
        fields[m.group(1).strip()] = m.group(2).strip()
    return fields


def unquote(value):
    return value.strip().strip("`")


def build_source(checks):
    raw = read(SOURCE_PATH)
    checks.add("source hash matches pinned SHA-256", sha256_text(raw) == SOURCE_SHA256, SOURCE_PATH)
    raw_lines = raw.splitlines(keepends=True)
    lines = [l.rstrip("\n") for l in raw_lines]
    heads = []
    for i, line in enumerate(lines, start=1):
        m = re.match(r"(#+) (.*\S)", line)
        if m:
            heads.append({"level": len(m.group(1)), "title": m.group(2).strip(), "start": i})
    for i, h in enumerate(heads):
        end = len(lines) + 1
        for later in heads[i + 1:]:
            if later["level"] <= h["level"]:
                end = later["start"]
                break
        h["end_exclusive"] = end
    return raw_lines, lines, heads


def build_records(lines, heads, checks):
    text = read("audits/truth-seeking-audit.md")
    ordered = text.split("## Ordered audit records", 1)[1]
    ordered = re.split(r"^## ", ordered, maxsplit=1, flags=re.M)[0]
    head_titles = {h["title"] for h in heads}
    records, bad_span, bad_heading = [], [], []
    for heading, body in md_sections("## x\n" + ordered, 3):
        m = re.match(r"(TS-AUD-\d{3}) — (.*)", heading)
        if not m:
            continue
        f = bullet_fields(body)
        src = re.search(r":(\d+)-(\d+)", f["Source"])
        start, end_incl = int(src.group(1)), int(src.group(2))
        if not (1 <= start <= end_incl <= len(lines)):
            bad_span.append(m.group(1))
        if unquote(f["Heading"]) not in head_titles:
            bad_heading.append(m.group(1))
        records.append({
            "id": m.group(1),
            "title": m.group(2).strip(),
            "kind": unquote(f["Kind"]),
            "start": start,
            "end_exclusive": end_incl + 1,
            "heading": unquote(f["Heading"]),
            "mechanism": f["Mechanism"],
            "effect": f["Truth-seeking effect"],
            "scenario": f["Concrete scenario"],
            "legitimate_purpose": f["Legitimate purpose"],
            "revision_hypothesis": f["Revision hypothesis"],
            "risk_if_revised": f["Risk if revised"],
            "severity": unquote(f["Severity"]),
            "confidence": unquote(f["Confidence"]),
            "disposition": unquote(f["Disposition"]),
            "destination": unquote(f["Destination"]),
            "patterns": ids(f["Philosophical patterns"].split("—")[0], r"\bPC?-?\d{2,3}\b"),
            "eps": [],
            "g003_disposition": "",
        })
    checks.add("audit records parsed", len(records) == 51, f"{len(records)} of 51")
    checks.add("every audit span lies inside the source", not bad_span, ", ".join(bad_span))
    checks.add("every audit heading exists in the source", not bad_heading, ", ".join(bad_heading))
    return records


def apply_g003_matrix(records, checks):
    text = read("framework/G003-traceability.md")
    by_id = {r["id"]: r for r in records}
    seen, span_diff, pattern_diff, unknown = set(), [], [], []
    for line in text.splitlines():
        m = re.match(r"\| (TS-AUD-\d{3}) \| (\d+)[–-](\d+) \|[^|]*\|([^|]*)\|([^|]*)\|[^|]*\|([^|]*)\|", line)
        if not m:
            continue
        rid = m.group(1)
        rec = by_id.get(rid)
        if rec is None:
            unknown.append(rid)
            continue
        seen.add(rid)
        if (int(m.group(2)), int(m.group(3)) + 1) != (rec["start"], rec["end_exclusive"]):
            span_diff.append(rid)
        if ids(m.group(4), r"\bPC?-?\d{2,3}\b") != rec["patterns"]:
            pattern_diff.append(rid)
        rec["eps"] = ids(m.group(5), r"EP-\d{2}")
        rec["g003_disposition"] = m.group(6).strip()
    missing = sorted(set(by_id) - seen)
    checks.add("G003 matrix covers every audit record", not missing and not unknown, ", ".join(missing + unknown))
    checks.add("G003 matrix spans agree with the audit", not span_diff, ", ".join(span_diff))
    checks.add("G003 matrix patterns agree with the audit", not pattern_diff, ", ".join(pattern_diff))


def build_patterns(records, checks):
    text = read("audits/philosophical-patterns.md")
    patterns = []
    for heading, body in md_sections(text, 3):
        m = re.match(r"(PC?-?\d{2,3}) — (.*)", heading)
        if not m:
            continue
        f = bullet_fields(body)
        pid = m.group(1)
        patterns.append({
            "id": pid,
            "title": m.group(2).strip(),
            "status": "candidate" if pid.startswith("PC") else "canonical",
            "definition": f.get("Definition", body.strip().split("\n")[0].strip()),
        })
    used = {p for r in records for p in r["patterns"]}
    for p in patterns:
        if p["status"] == "canonical" and p["id"] not in used:
            p["status"] = "unapplied"
    known = {p["id"] for p in patterns}
    checks.add("every pattern cited by an audit record is registered", used <= known, ", ".join(sorted(used - known)))
    # PC-001 / PC-002 keep the G003 decision; surface it so the viewer never implies promotion.
    g003 = read("framework/G003-traceability.md")
    for p in patterns:
        if p["status"] == "candidate":
            section = g003.split(f"### {p['id']} — ", 1)[1].split("###", 1)[0]
            decision = re.search(r"\*\*Decision:\*\* `([^`]+)`", section)
            p["decision"] = decision.group(1) if decision else ""
    cands = [p for p in patterns if p["status"] == "candidate"]
    checks.add("candidate patterns carry a recorded G003 decision", all(p.get("decision") for p in cands),
               ", ".join(f"{p['id']}={p.get('decision')}" for p in cands))
    return patterns


def build_eps(records, checks):
    text = read("framework/epistemic-framework.md")
    eps = []
    for heading, body in md_sections(text, 3):
        m = re.match(r"(EP-\d{2}) — (.*)", heading)
        if not m:
            continue
        rule = re.search(r"\*\*Constitution-ready rule[^*]*\*\*\s*\n(.+)", body)
        eps.append({"id": m.group(1), "title": m.group(2).strip(), "rule": rule.group(1).strip() if rule else ""})
    known = {e["id"] for e in eps}
    used = {e for r in records for e in r["eps"]}
    checks.add("seven epistemic principles parsed", len(eps) == 7, f"{len(eps)}")
    checks.add("every EP in the G003 matrix is defined", used <= known, ", ".join(sorted(used - known)))
    return eps


def build_crs(checks):
    text = read("framework/G004-core-hierarchy.md")
    crs = []
    for heading, body in md_sections(text, 3):
        m = re.match(r"(CR-\d{2}) — (.*)", heading)
        if not m:
            continue
        f = bullet_fields(body)
        crs.append({"id": m.group(1), "title": m.group(2).strip(),
                    "owner_goal": f.get("Owner goal", "").split(".")[0],
                    "prohibited_result": f.get("Prohibited result", "")})
    checks.add("twelve conflict rules parsed", len(crs) == 12, f"{len(crs)}")
    return crs


def build_applied(records, eps, crs, checks):
    reg = yaml.safe_load(read("framework/principles-v1.yaml"))
    checks.add("principle registry pins the same source hash",
               reg["source"]["constitution_sha256"] == SOURCE_SHA256, "framework/principles-v1.yaml")
    known_audit = {r["id"] for r in records}
    known_ep = {e["id"] for e in eps}
    known_cr = {c["id"] for c in crs}
    dangling, out = [], []
    for p in reg["principles"]:
        for ref, known in ((p["audit_ids"], known_audit), (p["epistemic_principle_ids"], known_ep),
                           (p["conflict_rule_ids"], known_cr)):
            dangling += [f"{p['principle_id']}->{x}" for x in ref if x not in known]
        out.append({
            "id": p["principle_id"],
            "title": p["title"],
            "clause_id": p["owner_clause_id"],
            "invariant": p["invariant"],
            "preserved_purpose": p["preserved_purpose"],
            "prohibited_interpretation": p["prohibited_interpretation"],
            "eps": p["epistemic_principle_ids"],
            "crs": p["conflict_rule_ids"],
            "audit_ids": p["audit_ids"],
            "targets": [{"heading": t["heading"], "start": t["start_line"], "end_exclusive": t["end_line_exclusive"]}
                        for t in p["source_targets"]],
            "replacement_entries": p["replacement_entries"],
            "status": p["status"],
            "registry_status": reg["status"],
        })
    checks.add("applied principles reference only known audit, EP and CR IDs", not dangling, ", ".join(dangling))
    return out


def build_candidates(raw_lines, applied, checks):
    reg = yaml.safe_load(read("map/candidates.yaml"))
    known_principles = {p["id"] for p in applied}
    out = []
    for c in reg["candidates"]:
        spec_text = read(c["map_path"])
        spec = json.loads(spec_text)
        problems = []
        if spec["source_sha256"] != SOURCE_SHA256:
            problems.append("map pins a different source hash")
        if c["evidence"]["status"] not in EVIDENCE_STATUSES:
            problems.append(f"unknown evidence status {c['evidence']['status']}")
        if not (ROOT / c["evidence"]["record"]).is_file():
            problems.append(f"evidence record missing: {c['evidence']['record']}")
        entries, prev_end = [], 0
        for e in sorted(spec["entries"], key=lambda x: x["source_start_line"]):
            start, end = e["source_start_line"], e["source_end_line_exclusive"]
            if not (1 <= start < end <= len(raw_lines) + 1):
                problems.append(f"{e['entry_id']}: span outside source")
                continue
            if start < prev_end:
                problems.append(f"{e['entry_id']}: overlaps the previous entry")
            prev_end = end
            if sha256_text("".join(raw_lines[start - 1:end - 1])) != e["source_sha256"]:
                problems.append(f"{e['entry_id']}: source segment hash mismatch")
            unknown = [p for p in e.get("principle_ids", []) if p not in known_principles]
            if unknown:
                problems.append(f"{e['entry_id']}: unknown principles {unknown}")
            replacement = e["replacement"].rstrip()
            entries.append({
                "entry_id": e["entry_id"],
                "start": start,
                "end_exclusive": end,
                "replacement": replacement,
                "replacement_sha256": sha256_text(replacement),
                "principle_ids": e.get("principle_ids", []),
                "clause_ids": e.get("clause_ids", []),
                "fixture_ids": e.get("fixture_ids", []),
            })
        checks.add(f"candidate {c['id']}: spans, hashes and references are exact", not problems, "; ".join(problems))
        out.append({
            "id": c["id"],
            "label": c["label"],
            "map_path": c["map_path"],
            "map_sha256": sha256_text(spec_text),
            "evidence": {"status": c["evidence"]["status"],
                         "summary": " ".join(c["evidence"]["summary"].split()),
                         "record": c["evidence"]["record"]},
            "entries": entries,
        })
    return out


def build():
    checks = Checks()
    raw_lines, lines, heads = build_source(checks)
    records = build_records(lines, heads, checks)
    apply_g003_matrix(records, checks)
    patterns = build_patterns(records, checks)
    eps = build_eps(records, checks)
    crs = build_crs(checks)
    applied = build_applied(records, eps, crs, checks)
    candidates = build_candidates(raw_lines, applied, checks)
    data = {
        "schema_version": 1,
        "generator": GENERATOR,
        "source": {"path": SOURCE_PATH, "sha256": SOURCE_SHA256, "line_count": len(lines), "lines": lines},
        "sections": heads,
        "records": sorted(records, key=lambda r: (r["start"], r["end_exclusive"], r["id"])),
        "patterns": patterns,
        "epistemic_principles": eps,
        "conflict_rules": crs,
        "applied_principles": applied,
        "candidates": candidates,
        "validation": {"ok": checks.ok, "checks": checks.items},
    }
    return json.dumps(data, ensure_ascii=False, indent=1, sort_keys=True) + "\n", checks


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="verify the committed map instead of writing it")
    args = ap.parse_args()
    text, checks = build()
    for c in checks.items:
        print(("ok   " if c["ok"] else "FAIL ") + c["name"] + (f"  [{c['detail']}]" if c["detail"] and not c["ok"] else ""))
    if not checks.ok:
        print("validation failed; map not written", file=sys.stderr)
        return 1
    if args.check:
        if not OUT.is_file() or OUT.read_text(encoding="utf-8") != text:
            print(f"stale: {OUT.relative_to(ROOT)} does not match its inputs; run python3 map/build_map.py", file=sys.stderr)
            return 1
        print(f"current: {OUT.relative_to(ROOT)} sha256 {sha256_text(text)}")
        return 0
    OUT.write_text(text, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} sha256 {sha256_text(text)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
