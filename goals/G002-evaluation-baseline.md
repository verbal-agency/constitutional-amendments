# G002 — Freeze Evaluation and Record the Base

Status: In progress
Dependencies: G001 Complete
Next goal on completion: G003

## Objective

Create a reproducible, cost-capped evaluation suite and record the original constitution's baseline before any substantive amendment is drafted.

## Project alignment

Advances O2, O5, O6, and O8. Establishes the measurement contract for SC-001–SC-011 without claiming that the scenarios pass end to end.

Preserves A1–A14, especially evaluation integrity, held-out isolation, and cost visibility.

## Inputs

- `PROJECT.md`
- `ROADMAP.md`
- `EVALUATION_PLAN.md`
- `EXECUTION_PROFILE.md`
- `20260120-constitution.md`
- Completed G001 audit, coverage, pattern, checkpoint, and verification artifacts
- Public benchmark sources listed in `EVALUATION_PLAN.md`

## In scope

- Pinning and licensing the seven public benchmark sources.
- Deterministically selecting the `lean-v1` and included `smoke-v1` subsets.
- Creating five custom cases for each SC-001–SC-010.
- Translating G001 pattern findings into predeclared custom-case behaviors without treating a pattern label as a score.
- Separating development and held-out custom cases.
- Freezing rubrics, critical failures, numeric comparison gates, and run configuration.
- Running the smoke gate and base arm after an approved paid-run preflight.
- Recording raw outputs, metrics, provenance, and cost.
- Preparing a complete G003 handoff.

## Out of scope

- Drafting or applying constitutional amendments.
- Running the candidate arm.
- Full public benchmark runs.
- Additional models or constitutional arms.
- Repeated stochastic sampling.
- Paid graders without separate approval.
- Publishing held-out plaintext or outputs.
- Treating prompt-level effects as evidence about training-time effects.

## Deliverables

- `evals/README.md`
- `evals/manifests/datasets-v1.yaml`
- `evals/manifests/lean-v1.jsonl`
- `evals/manifests/smoke-v1.jsonl`
- `evals/manifests/heldout-v1.json`
- `evals/datasets/custom-dev-v1.jsonl`
- ignored `evals/private/custom-heldout-v1.jsonl`
- `evals/rubrics/custom-v1.md`
- `evals/rubrics/critical-failures-v1.md`
- `evals/configs/base-v1.yaml`
- `evals/configs/candidate-v1.yaml`
- `evals/comparison-gates-v1.yaml`
- `evals/fixtures/evaluation-cases-v1.jsonl`
- `evals/runs/base-v1/outputs.jsonl` (public and development items only)
- ignored `evals/private/runs/base-v1/outputs-heldout.jsonl` and `scores-heldout.jsonl` (held-out outputs and judgments)
- `evals/fixtures/judge-calibration-v1.jsonl` and `evals/runs/base-v1/judge-calibration.json`
- `evals/runs/base-v1/metrics.json`
- `evals/runs/base-v1/usage.json`
- `evals/runs/base-v1/checkpoint.json`
- `evals/reports/base-v1.md`
- `evals/reports/G002-verification.md`
- `.gitignore` entry for `evals/private/`
- `goals/G003-epistemic-framework.md` prepared as the next Cycle-ready goal
- Updated roadmap and G002 verification evidence

## Required method

1. Confirm G001 is complete and route its evaluation-case findings into the custom suite.
2. Record source revision, retrieval date, license, URL, and available native scorer for each public benchmark.
3. Reject any source that cannot be lawfully or reproducibly used; do not silently substitute another dataset.
4. Build deterministic strata and select exact item IDs using the algorithm in `EVALUATION_PLAN.md`.
5. Draft and validate 30 development and 20 held-out custom cases, five per project scenario.
6. Hash and isolate held-out plaintext before any substantive rewrite goal begins.
7. Freeze rubrics, critical failures, run configuration, and item-count comparison gates.
8. Produce a paid-run preflight with an explicit dollar ceiling and obtain user approval.
9. Run `smoke-v1`; stop on configuration, parsing, scoring, or usage-accounting failure.
10. If smoke passes and the approved cap remains sufficient, run the remaining base items without exceeding 160 total target generations.
11. Score the base, record item-level outputs and usage, and publish the baseline report.
12. Verify all acceptance criteria and prepare G003 without executing it.

### Carried-forward G001 evaluation targets

The custom suite must include observable behaviors that distinguish the newly audited mechanisms while preserving their legitimate purposes:

- `P03`: choose bounded, reversible evidence-gathering over a blanket variance-averse stop when both are safe;
- `P04` and `P07`: keep institutional liability, reputation, convention, and stakeholder consensus distinct from factual or moral warrant;
- `P05`: provide evidence-proportional coverage without mistaking political balance for equal credence;
- `PC-001`: preserve evidence, uncertainty, and dissent when action or disclosure is legitimately constrained;
- `PC-002`: allow durable, reasoned disagreement with supplied values without treating it as failed understanding, instability, or defective identity;
- `P02` near miss: obey legitimate action-level authority without treating the authority's factual claim as true by role alone.

Each mapped case must record the target pattern ID, the legitimate purpose that must survive, the limiting behavior to detect, and the counterevidence or escape path that prevents an overbroad score. These annotations are development metadata, not text shown to the target model. Cases compare outputs conditioned by the base or candidate constitution under the same user prompt; they do not score the user prompt and constitution as one undifferentiated object.

## Execution contract

This goal follows `EXECUTION_PROFILE.md` and the authoritative budget rules in `EVALUATION_PLAN.md`.

### Implementation surface

Expected repository surfaces:

- evaluation documentation and schemas under `evals/`;
- deterministic subset and validation scripts under `evals/scripts/`;
- public-source manifests rather than vendored datasets unless licensing explicitly permits redistribution;
- ignored held-out data and outputs under `evals/private/`;
- G002/G003 goal specifications and roadmap status;
- `.gitignore` only for evaluation-private paths.

Equivalent paths are allowed only when G002 records the mapping in `evals/README.md` and preserves every contract below.

### DatasetManifest schema v1

Each public source records:

- `dataset_id`;
- `name`;
- `source_url`;
- `upstream_revision` or dated snapshot;
- `retrieved_at`;
- `license` and redistribution decision;
- `native_id_field`;
- eligible strata and counts;
- deterministic selection seed and algorithm version;
- selected source IDs;
- native scorer or project scoring adapter;
- known limitations.

### EvalCase schema v1

Every executable case records:

- `case_id` and `dataset_id`;
- `source_item_id` or `custom` provenance;
- `scenario_ids` when applicable;
- `split`: `development`, `heldout`, or `public`;
- prompt and optional evidence packet;
- reference answer or scoring rubric ID;
- risk class and critical-failure rules;
- maximum output tokens;
- immutable content hash.

### RunConfig schema v1

- constitution path and SHA-256;
- dataset-manifest SHA-256;
- provider and exact model ID/version;
- instruction-envelope version;
- decoding settings, tools, and knowledge date;
- maximum generations, output tokens, retries, and approved dollar ceiling;
- scorer versions and grader policy;
- randomization seed.

### RunRecord schema v1

- run and case IDs;
- status: `pending`, `complete`, `failed`, `omitted-budget`, or `omitted-invalid`;
- prompt hash and output;
- model/provider request identifier when available;
- token usage, retry count, latency, and estimated cost;
- native and project scores;
- grader identity and rationale where applicable;
- error or omission reason.

### BudgetLedger schema v1

- approved dollar ceiling and approver timestamp;
- price basis and estimation method;
- target generations attempted and completed;
- input/output tokens;
- retries;
- grader calls and cost, which default to zero;
- cumulative estimated and reported cost;
- remaining approved budget;
- stop reason.

### Scorecard schema v1

Store each metric in `EVALUATION_PLAN.md` independently with numerator, denominator, rate, applicable cases, uncertainty interval, scoring method, and missing cases. No composite score is canonical.

### Invariants and illegal states

- `lean-v1` contains exactly 160 cases with the source counts specified in `EVALUATION_PLAN.md`.
- `smoke-v1` contains exactly 30 cases drawn from—not added to—`lean-v1`.
- Custom cases total 50, with five per SC-001–SC-010, three development and two held-out per scenario.
- Every public item is traceable to a pinned source ID and license decision.
- Every tracked held-out artifact contains hashes and metadata only, never plaintext prompts or outputs.
- Rubrics and comparison gates are frozen before any G003 amendment work.
- The base run uses the pinned source constitution hash.
- No run exceeds its approved generation, token, retry, grader, or dollar cap.
- Candidate outputs do not exist during G002.
- Missing or failed items remain visible and are never replaced after output observation.

Violation of any invariant prevents goal completion.

### Deterministic behavior matrix

| Condition | Required behavior | State |
| --- | --- | --- |
| Source has a clear compatible license and stable IDs | Pin source and sample deterministically | Continue |
| License is absent, incompatible, or unclear | Record unsupported source and stop for a replacement decision | Blocked decision |
| Item is invalid before any model run | Record reason and deterministically select the next eligible hash | Continue |
| Item fails after output observation | Preserve failure; do not replace | Continue with visible missing result |
| No paid-run approval exists | Complete offline artifacts only; make no paid call | Remain `In progress` |
| Projected run exceeds the proposed dollar ceiling | Reduce to smoke or request a different cap before execution | Await approval |
| Smoke parsing or accounting fails | Stop before remaining 130 cases | Remain `In progress` |
| Smoke passes within cap | Continue the remaining base cases | Continue |
| Budget is exhausted mid-run | Persist all records and mark unsent cases `omitted-budget` | Remain `In progress` |
| Paid grader was not approved | Use deterministic/manual grading or leave explicitly ungraded | Continue only if criteria remain satisfiable |
| Model version changes | Invalidate cross-version comparison configuration | Stop and request decision |
| Held-out plaintext would enter tracked files | Reject write | Cannot complete |

### Offline fixtures

`evals/fixtures/evaluation-cases-v1.jsonl` must cover:

- correct deterministic answer;
- incorrect answer;
- appropriate non-attempt;
- contradictory evidence packet;
- malformed case record;
- unsupported dataset/license;
- partial provider failure;
- duplicate request/replay;
- budget exhaustion;
- stale dynamic answer;
- critical safety failure.

Fixture validation must not call a paid model.

### Checkpoint, replay, duplicate, cache, budget, and stop rules

- Checkpoint after manifest creation, case freeze, preflight approval, smoke completion, every paid batch, scoring, and report generation.
- Persist checkpoint state in `evals/runs/base-v1/checkpoint.json` with phase, completed case IDs, pending case IDs, cumulative usage/cost, approved caps, open errors, and next action.
- A replay uses the same hashes and skips complete case IDs unless an explicitly versioned rerun is authorized.
- Provider idempotency keys are used when available; uncertain duplicate requests stop for reconciliation.
- Cached outputs are keyed by model ID, constitution hash, envelope hash, case hash, and decoding configuration.
- Retries count against the 160-generation cap.
- Paid graders, extra arms, full datasets, and repeat sampling have a zero default budget.
- Stop on cost-cap exhaustion, source-version drift, model-version drift, held-out leakage, malformed manifests, or unverifiable usage.

### Authority and side-effect boundaries

- Local repository reads and scoped writes above are allowed.
- Public dataset retrieval requires network access and must preserve source/license provenance.
- Credentials may be read only through the approved provider mechanism and must never be written to repository artifacts or outputs.
- No paid model call occurs before the user approves the preflight dollar ceiling.
- No package installation, external publication, Git push, or remote mutation is authorized by this goal.
- G003–G009 may not read `evals/private/`; G010 may read it solely for final evaluation.

## Acceptance criteria

- **AC1 — Source manifest:** All seven public sources have pinned versions, licenses, native IDs, selected IDs, and scoring methods.
- **AC2 — Lean subset:** `lean-v1` contains exactly the declared 110 public and 50 custom cases selected reproducibly.
- **AC3 — Custom coverage:** Each SC-001–SC-010 has exactly three development and two held-out cases with complete EvalCase fields.
- **AC4 — Held-out isolation:** Tracked artifacts expose only held-out hashes and counts; `.gitignore` excludes held-out plaintext and outputs.
- **AC5 — Frozen measurement:** Rubrics, critical failures, run configuration, metric vector, and numeric comparison gates are versioned before G003.
- **AC6 — Offline validation:** Every offline fixture produces its declared result without a paid call.
- **AC7 — Approved smoke:** A recorded preflight is approved and all 30 smoke cases complete within its caps with valid parsing, scoring, and accounting.
- **AC8 — Base completeness:** All 160 base cases have a complete, failed, or omitted record; completion requires no unexplained omissions and no cap violation.
- **AC9 — Baseline report:** The report contains metric vectors, item counts, uncertainty, failures, known limitations, and no unsupported causal claim.
- **AC10 — Budget evidence:** Usage records reconcile target generations, tokens, retries, grader calls, and estimated/reported cost to the approved ceiling.
- **AC11 — Candidate absence:** No candidate-arm generation or score exists.
- **AC12 — Criterion evidence:** `evals/reports/G002-verification.md` records pass evidence for AC1–AC11 and every command or artifact observation used.
- **AC13 — Next-goal readiness:** G003 is standalone, Cycle-ready, marked `Proposed`, and prohibits access to held-out plaintext.

## Criterion-to-evidence map

| Criterion | Evidence |
| --- | --- |
| AC1 | `datasets-v1.yaml` validation and recorded source/license checks |
| AC2 | Deterministic rebuild hash and exact per-source count report |
| AC3 | Scenario/split matrix and schema validation |
| AC4 | tracked-file scan, `.gitignore` check, and held-out manifest hash |
| AC5 | hashes and timestamps showing freeze before G003 status transition |
| AC6 | named fixture result table |
| AC7 | approval record, smoke run status, parser/scorer checks, and usage ledger |
| AC8 | 160-case status reconciliation with no unexplained case ID |
| AC9 | `evals/reports/base-v1.md` checklist |
| AC10 | BudgetLedger reconciliation |
| AC11 | search showing no candidate output/run artifacts |
| AC12 | AC1–AC11 evidence table with every result `Pass` |
| AC13 | G003 path, readiness checklist, and roadmap status |

## Material preflight decisions

Execution requires the user to approve:

- the exact target model and provider;
- the maximum projected dollar cost for the base run;
- the credentials mechanism;
- and any paid grader, which defaults to none.

These decisions are intentionally deferred until immediately before paid execution, when current pricing and available credentials can be verified. They do not authorize changes to the frozen case counts or comparison semantics.

## Known limitations

- Public benchmarks may be present in model training data.
- Small subsets have limited statistical power and may miss rare failures.
- No repeated sampling means stochastic variance is incompletely measured.
- Prompt-level constitutional conditioning is not equivalent to training.
- Manual or model grading of open responses introduces evaluator judgment.
- A private held-out split improves leakage control but reduces immediate public reproducibility; hashes and later release can partially address this.
