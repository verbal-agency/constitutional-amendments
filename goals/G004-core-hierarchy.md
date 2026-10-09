# G004 — Decide the Core Value and Epistemic-Floor Hierarchy

Status: Complete
Dependencies: G003 Complete
Next goal on completion: G005

## Objective

Decide where the seven G003 epistemic principles belong in relation to the source constitution's helpfulness, ethics, safety, autonomy, corrigibility, and operational-authority commitments. Produce one explicit hierarchy and conflict interface without drafting passage-level amendments. The result must state whether epistemic integrity is a core value, an ethical commitment, a cross-cutting procedural floor, or a deliberately composed interface, and must make conflicts between truth-seeking, safety, disclosure, and action behaviorally decidable.

G004 is a hierarchy decision, not a second audit and not an integrated rewrite. It must use the G003 traceability matrix to test whether the hierarchy preserves legitimate purposes and prevents epistemic closure.

## Project alignment

Advances O1 (explicit epistemology), O3 (protected inquiry), O4 (non-self-sealing governance), O6 (adversarial resilience), and O7 (pattern-aware diagnosis). Directly develops SC-001, SC-003, SC-004, SC-005, SC-006, SC-007, SC-008, and SC-010's process-level distinction; it does not claim those scenarios pass end to end. SC-011 remains reserved for G010.

Preserves A1–A14, especially immutable source, separate epistemic planes, narrow tailoring, self-application, traceability, and evaluation integrity.

## Inputs

- `PROJECT.md`
- `ROADMAP.md`
- `EXECUTION_PROFILE.md`
- `20260120-constitution.md` as immutable context
- `framework/epistemic-framework.md`
- `framework/G003-traceability.md`
- `framework/G003-verification.md`
- `TRUTH_SEEKING_PIVOT.md`
- G001 audit and pattern artifacts only through the G003 traceability links
- `evals/README.md` and `EVALUATION_PLAN.md` for frozen measurement boundaries

G004 must not read `evals/private/` or any held-out prompt, annotation, output, or score. It must not run a paid model, network call, or candidate evaluation.

## In scope

- Decide the constitutional placement and priority of EP-01 through EP-07.
- Define precedence and conflict rules for belief, inquiry, analysis, speech, disclosure, acquisition, and execution.
- Test the hierarchy against the G003 safety-preservation interface and all ten deterministic behavior-matrix conditions.
- Decide how operational authority, epistemic warrant, institutional incentive, confidentiality, privacy, emergency precaution, and identity-conditioned governance interact.
- Specify an evidence-bearing review and amendment path for the hierarchy itself.
- Preserve the G003 candidate-pattern decisions unless new evidence justifies a recorded change.
- Prepare G005 as a standalone Cycle-ready goal after G004 verification.

## Out of scope

- Editing `20260120-constitution.md`.
- Drafting passage-level amendments or the integrated candidate constitution.
- Reopening the 51 audit records as independent drafting requests.
- Running candidate or base evaluations, reading held-out evaluation material, or changing frozen gates.
- Deciding the detailed honesty practice, authority wording, harm taxonomy, or dissent procedures owned by G005–G008; G004 specifies interfaces and handoff obligations only.
- Treating hierarchy placement as proof that a source passage requires amendment.

## Deliverables

- `framework/G004-core-hierarchy.md` — one explicit hierarchy, conflict protocol, placement decisions, and safety interface.
- `framework/G004-traceability.md` — principle-to-decision evidence, source-purpose preservation, counterarguments, and routed questions.
- `framework/G004-verification.md` — criterion-level evidence and command results.
- `fixtures/G004-hierarchy-cases.md` — deterministic offline positive, negative, contradictory, malformed, emergency, privacy, and identity cases.
- `goals/G005-honesty-and-inquiry.md` — standalone Cycle-ready successor, prepared but not executed.
- `framework/G004-checkpoint.md` — durable state and legal completion status.
- Updated `ROADMAP.md` statuses only after every G004 acceptance criterion passes.

## Required method

1. Confirm G003 is complete and the seven principles, traceability matrix, and safety interface are frozen.
2. Create a placement table before writing the hierarchy prose. Every principle must receive exactly one primary placement and may receive named interface roles.
3. Define a precedence relation for each epistemic plane; do not use a single global “truth versus safety” slogan.
4. Test all ten G003 matrix conditions plus at least one source-purpose preservation case for each safety, autonomy, privacy, confidentiality, and corrigibility duty.
5. Run an adversarial review for epistemic subordination, false neutrality, paternalism, precautionary conservatism, institutional self-protection, and identity-conditioned governance.
6. Record objections, counterarguments, unresolved implementation details, and the destination goal responsible for each.
7. Run the offline fixture set and schema/contradiction checks; reject fixtures whose expected result merely repeats the prose without an observable acceptance proof.
8. Prepare G005 without executing it, then verify every criterion.

## Canonical artifact contracts

### HierarchyDecision schema v1

Each principle placement row must contain:

- `principle_id`: one of `EP-01` through `EP-07`;
- `primary_placement`: exactly one of `core-value`, `ethical-commitment`, `procedural-floor`, `interface-rule`;
- `interface_roles`: zero or more of `belief`, `inquiry`, `analysis`, `speech`, `disclosure`, `acquisition`, `execution`, `review`;
- `precedence_notes`: explicit conflict behavior, never an empty slogan;
- `legitimate_purpose_preserved`: one or more source purposes with evidence IDs;
- `counterargument`: strongest reason the placement could fail;
- `decision_rationale`: evidence-based response;
- `downstream_goal`: one of `G005`, `G006`, `G007`, `G008`;
- `status`: `decided` only after review, otherwise `blocked`.

### ConflictRule schema v1

Each rule must contain `rule_id`, `planes`, `trigger`, `authority`, `evidence_threshold`, `required_action`, `allowed_restriction`, `prohibited_result`, `review_trigger`, and `owner_goal`. `authority` must distinguish operational control from epistemic warrant. `allowed_restriction` must name the narrowest affected plane.

### OfflineFixture schema v1

Each fixture must contain:

- `case_id`: stable `H-01` through `H-10` identifier;
- `class`: one of `positive`, `negative`, `contradictory`, `malformed`, `emergency`, `privacy`, or `identity`;
- `condition`: the evidence and duties presented to the hierarchy;
- `planes`: one or more canonical epistemic planes;
- `conflicting_duties`: the principles or source purposes in tension;
- `expected_result`: required placement, precedence, review, or restriction behavior;
- `prohibited_result`: the illegal state the fixture must reject;
- `rationale`: why the expected result follows from the decided hierarchy;
- `acceptance_proof`: an observable field or assertion that makes the result binary.

The set must include collision cases for candor/privacy, safety/inquiry, authority/evidence, and identity/dissent. `H-05`, `H-08`, and `H-09` must be contradictory or conflict cases rather than simple restatements of a rule. `H-10` must demonstrate an urgent but reviewable precaution.

### Invariants and illegal states

- Exactly seven `HierarchyDecision` records exist, one per EP ID.
- Every decision has exactly one primary placement and a non-empty conflict rationale.
- Every conflict rule names at least one plane and never treats `core-value` as automatic authority to disclose or execute.
- No rule permits fabricated facts, destruction of contrary evidence, or immunity from review.
- No rule treats consensus, role, identity, or institutional incentive as proof by itself.
- Emergency restrictions have a scope, expiry or review trigger, and post-event evidence path.
- Privacy and confidentiality rules can limit disclosure but cannot require false belief or false provenance.
- The source hash remains unchanged and frozen evaluation artifacts are untouched.
- The documented execution record contains no held-out evaluation read, paid call, candidate output, or network-derived evidence; repository state alone is not treated as proof of a negative.
- G005 is `Proposed` only after G004 verification and is independently understandable.

## Deterministic behavior matrix

| Condition | Required hierarchy result | Illegal result | Evidence artifact |
|---|---|---|---|
| Credible evidence conflicts with a current belief | EP-02 controls update; current status and uncertainty are preserved | Role or consensus makes update impossible | H-01 |
| Strong consensus plus anomaly | Unequal weight plus a test; neither dismissal nor false balance | Equal credence or convention-only dismissal | H-02 |
| Operational authority conflicts with factual evidence | Follow legitimate action control while preserving epistemic disagreement | Authority becomes factual proof | H-03 |
| Harmful request mixes analysis and execution | Restrict execution/acquisition as warranted; preserve safe analysis | Whole-topic suppression without rationale | H-04 |
| Privacy/confidentiality conflicts with candor | Narrow disclosure and state the limitation truthfully | Private-data disclosure or fabricated explanation | H-05 |
| Novel weak hypothesis | Permit labeled inquiry and tests; calibrate belief | Novelty becomes proof or prohibition | H-06 |
| No justified answer | State unknown and useful next evidence | Manufactured closure | H-07 |
| Evidence challenges a safety rule | Continue necessary action limit and route evidence to review | Criticism is itself disqualifying | H-08 |
| Trained value is disputed | Permit reasoned disagreement without identity penalty | Non-endorsement is defective identity | H-09 |
| Urgent precaution | Temporary/reviewable action under uncertainty | Precaution becomes permanent truth | H-10 |

## Authority and side-effect boundaries

- Repository-local reads and the scoped documentation/fixture writes above are allowed.
- No network, credentials, package installation, paid model call, candidate generation, Git push, or remote mutation is authorized.
- Only tracked G003 and source artifacts may be read; `evals/private/` is prohibited.
- Validation may execute local scripts and static checks but may not contact a provider.
- The hierarchy artifact is advisory until G009 integrates it; G004 must not present it as Anthropic's constitution.

## Checkpoint and stop rules

- Checkpoint after placement table, conflict protocol, adversarial review, fixture validation, and final verification.
- If a principle requires two incompatible primary placements, record the conflict and keep G004 in progress until resolved or explicitly blocked.
- If a hierarchy choice would weaken a hard action safeguard, stop that branch and route it to G007 with the evidence and unresolved decision.
- If a required decision depends on held-out outputs or new external evidence, record the dependency and do not substitute unapproved evidence.
- If a proposed rule cannot distinguish epistemic warrant from operational authority, it fails verification.

## Acceptance criteria

- **AC1 — Seven placements:** Exactly seven principles have one decided primary placement and named interface roles.
- **AC2 — Explicit hierarchy:** The hierarchy states how core values, ethical commitments, procedural floors, and interface rules relate without deciding passage-level wording.
- **AC3 — Plane-specific conflicts:** Belief, inquiry, analysis, speech, disclosure, acquisition, and execution each have explicit conflict behavior.
- **AC4 — Safety preservation:** Legitimate safety, privacy, confidentiality, autonomy, and human-control purposes remain actionable and narrowly scoped.
- **AC5 — Epistemic independence:** Role, consensus, convention, incentive, and trained identity cannot independently establish truth or invalidate dissent.
- **AC6 — Anti-closure:** The hierarchy preserves evidence, review, dissent, emergency expiry, and amendment of its own rules.
- **AC7 — Matrix coverage:** All ten deterministic conditions have passing fixture evidence and no illegal result.
- **AC8 — Counterargument review:** Each placement records a material counterargument and an evidence-based response.
- **AC9 — Scope integrity:** Source hash and frozen evaluation artifacts are unchanged; the execution record and command boundary show no held-out or paid artifact access.
- **AC10 — Verification:** `framework/G004-verification.md` records passing evidence for AC1–AC9.
- **AC11 — Next-goal readiness:** G005 is standalone, Cycle-ready, dependency-bound to G004, and prepared without execution.

## Criterion-to-evidence map

| Criterion | Required evidence |
|---|---|
| AC1 | Seven-row `HierarchyDecision` table and schema validation |
| AC2 | `G004-core-hierarchy.md` placement and precedence sections |
| AC3 | ConflictRule table and H-01–H-10 fixtures |
| AC4 | Safety-purpose preservation table and privacy/emergency fixtures |
| AC5 | Authority, incentive, convention, and identity adversarial review |
| AC6 | Review, appeal, expiry, and amendment fields plus H-08/H-09/H-10 |
| AC7 | Fixture result table with all ten cases passing and schema/acceptance-proof validation |
| AC8 | Counterargument column populated for all seven principles |
| AC9 | source hash/diff, documented command boundary, and candidate/paid-call absence check; no claim of proving an unobserved negative |
| AC10 | Criterion-level verification report |
| AC11 | G005 path, status, execution contract, and roadmap state |

## Completion handoff

When G004 completes, G005 receives the decided hierarchy and conflict interface. G005 must operationalize honesty, updating, disconfirmation, candor, speculation, and mystery without reopening G001 as a list of independent amendment demands. G006–G008 remain the owners of passage-level authority, harm, and dissent applications.
