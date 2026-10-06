# G002 Verification

Goal: G002 — Freeze Evaluation and Record the Base
Verification date: 2026-10-06
Result: Pass

## Criterion evidence

| Criterion | Result | Evidence |
|---|---|---|
| AC1 — Source manifest | Pass | `datasets-v1.yaml` records seven pinned sources, revisions or snapshots, retrieval dates, IDs, strata, scorers, and license decisions. MASK's absent dataset license is explicitly recorded with the owner's local-use/no-redistribution decision. |
| AC2 — Lean subset | Pass | `select_subset.py --verify` reported matching source hashes and an identical rebuild; `lean-v1.jsonl` contains 160 cases: 110 public and 50 custom. |
| AC3 — Custom coverage | Pass | `validate_custom.py` reported 30 development and 20 held-out cases with zero errors; each SC-001–SC-010 has three development and two held-out cases. |
| AC4 — Held-out isolation | Pass | `.gitignore` excludes `evals/private/`; tracked held-out manifest entries contain IDs, counts, and hashes only; tracked outputs contain only public and development cases. |
| AC5 — Frozen measurement | Pass | Dataset manifests, cases, rubrics, critical failures, run configs, metric vector, and `comparison-gates-v1.yaml` are fixed before G003 becomes Proposed. SC-010 is explicitly a non-blocking process diagnostic excluded from GATE-01 through GATE-04. |
| AC6 — Offline validation | Pass | `run_fixtures.py` passed FX-01 through FX-11 with zero paid calls; script compilation passed. |
| AC7 — Approved smoke | Pass | Approval files match the target and judge preflights; all 30 smoke cases completed before the remaining run; parsing, scoring, and accounting artifacts are valid. |
| AC8 — Base completeness | Pass | The ledger records 160 attempts, 158 completed cases, two retries, and two explicit `omitted-budget` records; no case is unexplained and no cap was exceeded. |
| AC9 — Baseline report | Pass | `base-v1.md` reports the metric vector, denominators, intervals, omissions, costs, failures, judge caveats, dataset limitations, and claim boundary. |
| AC10 — Budget evidence | Pass | `usage.json`, approvals, score logs, calibration records, and `metrics.json` reconcile $0.105102 target generation plus $1.058787 judging/calibration, both below their separate ceilings. |
| AC11 — Candidate absence | Pass | No candidate output, score, metric, approval, or run artifact exists; only the inactive candidate configuration is present. |
| AC12 — Criterion evidence | Pass | This document records AC1–AC11 evidence and the commands and observations below. |
| AC13 — Next-goal readiness | Pass | `goals/G003-epistemic-framework.md` is standalone and Cycle-ready, prohibits held-out access, depends on completed G002, and is promoted to Proposed only after this verification. |

## Verification commands and observations

```text
$ shasum -a 256 20260120-constitution.md
251440a71a9068dd43bfaab2b8694d6e2a4f519c403f1b9a70785f830d05f327

$ python3 evals/scripts/validate_custom.py
development=30 heldout=20 errors=0

$ python3 evals/scripts/select_subset.py --verify
source hashes match: True; lean-v1 rebuild identical: True

$ python3 evals/scripts/run_fixtures.py
FX-01..FX-11 PASS; 0 failure(s); no paid call made

$ python3 -m py_compile evals/scripts/*.py
(pass)

$ git diff --check
(pass)
```

Additional checks:

- The source constitution diff is empty.
- `lean-v1` has 160 unique case IDs and `smoke-v1` has 30 IDs drawn from it.
- The public/development output log has 138 completed and two omitted rows; the ignored held-out log has 20 completed rows.
- All 139 judge-scored completed cases and 19 deterministic sycophancy cases resolve into 158 results.
- Append-only scoring costs include failed judge attempts that were later retried.
- Final judge calibration passed 79/80 decisions within tolerance with no critical-failure mismatch.
- The independent 12-item review recorded 11 agreements and one disagreement without overwriting judge outputs.
- No held-out plaintext or per-item output is tracked.
- No candidate run artifact exists.

## Routed findings

- **G003:** SC-010 is process-level audit evidence, not a model-behavior principle; the prepared goal records this boundary.
- **G010:** Obtain the required human review for base and candidate results, perform position-swapped pairwise judging, report SC-010 separately, preserve the MASK license caveat, and treat same-family judge results as suggestive.
- **Observation:** The source-conditioned baseline is comparatively strong on the custom rubric and sampled safety checks but weak on factual QA, false-premise correction, and sycophancy; these are baseline measurements, not G003 drafting requirements.

No unscheduled finding requires a backlog item.
