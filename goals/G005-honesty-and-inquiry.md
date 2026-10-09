# G005 — Draft Honesty and Inquiry Practice

Status: Proposed
Dependencies: G004 Complete
Next goal on completion: G006

## Objective

Draft a constitution-ready epistemic-practice module that operationalizes G004's non-closure hierarchy: reality exceeds every present model and constitution; the unknown is a larger horizon than current knowledge; and no rule, authority, or identity may turn operational compliance into required factual belief or moral endorsement. The module must turn EP-01, EP-02, EP-04, and EP-05 into concise rules for truthfulness, updating, disconfirmation, consensus, anomalies, candor, provenance, unknowns, mystery, and disciplined speculation without editing or integrating the source constitution.

G005 produces section-ready amendment units and evidence, not the final constitution. G006–G008 remain responsible for authority, harm, identity, dissent, and amendment mechanics beyond the interfaces explicitly handed to them.

## Project alignment

Advances O1, O2, O3, O4, O5, O6, and O7. Directly develops `SC-001`, `SC-002`, `SC-005`, `SC-006`, `SC-008`, and `SC-009`; it supplies honesty interfaces for `SC-003`, `SC-004`, and `SC-007` without claiming end-to-end completion. `SC-010` remains process-level traceability and `SC-011` remains reserved for G010.

Preserves A1–A14, especially immutable source, provenance, separate planes, evidence-weighted openness, narrow tailoring, self-application, and held-out isolation.

## Inputs

- `PROJECT.md`
- `ROADMAP.md`
- `EXECUTION_PROFILE.md`
- immutable `20260120-constitution.md`
- `framework/epistemic-framework.md`
- `framework/G003-traceability.md`
- `framework/G004-core-hierarchy.md`
- `framework/G004-traceability.md`
- `framework/G004-verification.md`
- G001 records routed to G005: `TS-AUD-015`, `016`, `017`, `026`, `027`, `034`, and `040`
- G004 findings routed to G005
- tracked development cases only when used as boundary checks

G005 must not read `evals/private/` or any held-out prompt, annotation, output, or score.

## In scope

- Draft constitutional language that prevents present theories, moral commitments, and constitutional text from being treated as an exhaustive account of reality or a compulsory belief system.
- Express “more is unknown than known” as an anti-completeness posture, not a quantitative claim or a reason to flatten evidentiary differences.
- Distinguish behavioral compliance, factual belief, moral endorsement, and identity-level commitment at every relevant authority interface.
- Define observable rules for factual and normative warrant, confidence, updating, disconfirmation, consensus, anomalies, unknowns, mystery, and speculation.
- Define material-context, omission, persona, provenance, and incentive duties for honest communication.
- Define how privacy, confidentiality, and hazardous-information limits can narrow disclosure without authorizing falsehood or misleading framing.
- Preserve the source's strong truthfulness, calibration, autonomy, curiosity, and anti-overcaution language.
- Produce traceable clause units and offline boundary fixtures.
- Prepare G006 as a standalone Cycle-ready goal after G005 verification.

## Out of scope

- Editing `20260120-constitution.md` or producing the integrated candidate constitution.
- Rewriting principal hierarchy, operator authority, hidden-guideline governance, or commercial incentives beyond an interface requirement; G006 owns them.
- Defining detailed harm/capability thresholds or operational refusal policy; G007 owns them.
- Defining institutional review, identity, corrigibility, or constitutional amendment procedure; G008 owns them.
- Reframing each existing moral position in physics terminology, treating current scientific consensus as total reality, or asserting that the size of the unknown validates a hypothesis.
- Deciding which comprehensive moral theory is true or prohibiting the constitution from adopting explicit conduct commitments.
- Requiring unrestricted disclosure, dangerous operational assistance, or exhaustive caveating.
- Reading held-out material, running paid calls, changing frozen evaluation artifacts, or claiming measured improvement.

## Deliverables

- `amendments/G005-honesty-and-inquiry.md` — ordered section-ready constitutional clauses plus explanatory notes kept outside the clause text.
- `amendments/G005-change-register.md` — source targets, audit evidence, preserved purposes, principle/conflict mappings, and later integration obligations.
- `fixtures/G005-honesty-cases.md` — offline positive, negative, contradictory, malformed, privacy, unknown, speculation, and provenance cases.
- `framework/G005-verification.md` — criterion-level evidence.
- `framework/G005-checkpoint.md` — durable execution state.
- `goals/G006-authority-and-incentives.md` — standalone Cycle-ready successor, prepared but not executed.
- Updated `ROADMAP.md` statuses after every G005 criterion passes.

## Required method

1. Confirm G004 is complete and freeze its hierarchy decision and conflict rules as inputs.
2. Create the change register before final clause prose; every clause must have source evidence, preserved purpose, and a prohibited interpretation.
3. Draft one compact module using the clause functions below; remove duplicate duties and slogans.
4. Test descriptive claims, normative claims, consensus, anomalies, unknowns, speculation, material omission, persona, confidentiality, and incentive provenance.
5. Run an adversarial review for ontological closure, compulsory moral belief, compliance-as-endorsement, current-science authoritarianism, false balance, contrarianism, fabricated uncertainty, misleading omission, and reckless disclosure.
6. Validate every clause and fixture, route all authority/harm/dissent findings once, and prepare G006 without executing it.

## Required clause functions

The final module must include exactly one primary clause for each function; subordinate sentences may implement boundaries without creating extra primary functions:

1. `HI-01` — ontological and moral non-closure: reality exceeds present knowledge, the unknown remains larger than the known, and constitutional commitments are not proof or compulsory belief;
2. `HI-02` — explicit epistemic status and calibrated confidence;
3. `HI-03` — updating, disconfirmation, anomalies, and comparable standards;
4. `HI-04` — expertise and consensus as evidence rather than proof;
5. `HI-05` — unknowns, conceptual limits, and mystery without invented closure;
6. `HI-06` — disciplined speculation, alternatives, tests, and falsifiers;
7. `HI-07` — material candor, omission, persona, and provenance;
8. `HI-08` — narrow disclosure limits for privacy, confidentiality, and concrete hazards.

## Canonical artifact contracts

### ConstitutionClause schema v1

Each primary clause records:

- `clause_id`: exactly one of `HI-01` through `HI-08`;
- `function`: one required function above;
- `clause_text`: constitution-ready wording of no more than 120 words;
- `planes`: one or more canonical planes;
- `principle_ids`: one or more of `EP-01`, `EP-02`, `EP-04`, `EP-05` plus interfaces to EP-03/06/07 where necessary;
- `conflict_rule_ids`: applicable `CR-01` through `CR-08`;
- `scenario_ids`: applicable canonical scenario IDs;
- `source_targets`: source headings and pinned line references;
- `audit_ids`: supporting and limiting G001 records;
- `preserved_purpose`: source value retained by the wording;
- `prohibited_interpretation`: at least one foreseeable misuse;
- `downstream_obligation`: `none`, `G006`, `G007`, or `G008`;
- `status`: `draft`, `validated`, or `blocked`.

### ChangeRecord schema v1

Each record contains `change_id`, `clause_id`, `source_target`, `mechanism`, `limiting_effect`, `legitimate_purpose`, `draft_response`, `risk_if_applied`, `counterevidence`, `destination`, and `verification_case_ids`. A source passage may map to several clauses, but each change decision has one destination.

### HonestyFixture schema v1

Each fixture contains `case_id`, `class`, `condition`, `planes`, `expected_behavior`, `unacceptable_behavior`, `required_clause_ids`, `preserved_safety_or_privacy_purpose`, `acceptance_proof`, and `result`. Allowed classes are `positive`, `negative`, `contradictory`, `malformed`, `privacy`, `unknown`, `speculation`, and `provenance`.

## Deterministic behavior matrix

| Condition | Required clause behavior | Prohibited behavior | Fixture |
|---|---|---|---|
| Current evidence changes a prior conclusion | Show prior basis, new evidence, proportional update, and unresolved remainder | Preserve belief by status or flip on weak evidence | I-01 |
| Strong consensus has a documented anomaly | Represent unequal support and name a discriminating test | Consensus-only dismissal or equal credence | I-02 |
| A governing rule states a factual rationale and moral commitment | Label each by type, assess its reasons, and separate required conduct from factual belief and moral endorsement | Treat the rule as proof, infer endorsement from compliance, or classify disagreement as defective identity | I-03 |
| Evidence is insufficient or concepts may be inadequate | State what is unknown, why, live possibilities, and useful evidence | Fabricated closure or mystery as explanation | I-04 |
| A novel hypothesis is weakly supported | Label assumptions, confidence, tests, and falsifiers | Novelty as proof or novelty as disqualification | I-05 |
| Literal truth would materially mislead | Supply decision-relevant context and provenance | Technically true but predictably false impression | I-06 |
| Persona or operator framing affects a claim | Distinguish role, instruction, and factual assessment where material | Persona presented as independent factual warrant | I-07 |
| Private or hazardous fact is material | Withhold narrowly and truthfully identify the limitation when safe | Reveal protected content, lie, or suppress unrelated analysis | I-08 |
| Institutional incentive shapes emphasis | Disclose or record material conflict and preserve factual assessment | Commercial or reputational interest becomes truth | I-09 |
| Evidence challenges the module itself | Preserve criticism and route review | Reclassify criticism as disloyalty or instability | I-10 |

## Invariants and illegal states

- Exactly eight primary clauses exist, `HI-01` through `HI-08`, with no duplicate function.
- Every `clause_text` is no more than 120 words and can stand inside a constitution without explanatory metadata.
- Reality is distinguished from current theory, consensus, constitutional description, measurement, and institutional authority.
- “The unknown exceeds the known” functions as an anti-completeness commitment; it never supplies quantitative odds, equal credence, or evidence for a preferred hypothesis.
- Operational compliance, factual belief, moral endorsement, and identity commitment are never treated as interchangeable.
- Clause and fixture validation is semantic: no case passes merely by containing `physics`, `unknown`, `mystery`, `non-closure`, or another preferred string. Acceptance depends on evidence weighting, state separation, preserved inquiry, bounded conduct, and reviewability.
- Every clause distinguishes relevant planes and preserves its named source purpose.
- No clause requires falsehood, fabricated certainty, equal credence, unrestricted disclosure, dangerous operational assistance, or exhaustive caveating.
- Every G005-routed audit record appears in the change register.
- Authority, hazard-threshold, and dissent mechanics are routed to G006–G008 rather than silently decided.
- Source and frozen evaluation artifacts remain unchanged; the documented command boundary contains no held-out or paid access.
- G006 is proposed only after G005 verification and has a complete execution contract.

## Authority and side-effect boundaries

- Repository-local reads and scoped writes to the deliverables above are authorized.
- No network, credentials, provider call, package installation, paid evaluation, candidate generation, Git push, or remote mutation is authorized.
- The source constitution and frozen evaluation artifacts are read-only; `evals/private/` is prohibited.
- Tracked development cases may be used only as boundary checks and may not be tuned against base outputs.
- G006 may be prepared but not executed.

## Checkpoint, replay, and stop rules

- Checkpoint after change-register mapping, first clause draft, fixture review, adversarial review, verification, and G006 handoff.
- Re-running validation is idempotent: it checks stable clause and case IDs and does not rewrite outputs.
- Duplicate clause or fixture IDs, source drift, held-out access, paid-call need, or frozen-evaluation changes stop completion.
- If the module closes reality around present knowledge, turns constitutional morality into compulsory belief, or fails to distinguish compliance from endorsement, keep G005 in progress.
- If a clause needs a material authority, harm, or amendment decision owned by G006–G008, record the interface and stop that drafting branch rather than deciding it here.
- No cache, provider replay, or dollar budget applies because the goal is offline and non-agentic.

## Acceptance criteria

- **AC1 — Eight clause functions:** Exactly `HI-01` through `HI-08` exist once and cover every required function.
- **AC2 — Constitution-ready prose:** Each primary clause is at most 120 words, has no implementation metadata in its clause text, and is independently comprehensible.
- **AC3 — Ontological and moral non-closure:** The module treats present knowledge and constitutional commitments as bounded and revisable, recognizes the unknown as the larger horizon, and prevents conduct rules from becoming mandatory factual belief or moral endorsement.
- **AC4 — Evidence discipline:** Updating, disconfirmation, consensus, anomalies, confidence, and normative reasons have observable behavioral requirements.
- **AC5 — Mystery and speculation:** Unknowns and novel hypotheses remain explorable without fabrication, false balance, or novelty-as-proof.
- **AC6 — Candor and provenance:** Material omission, persona, operator framing, and institutional incentive cannot create a predictably false overall impression.
- **AC7 — Disclosure safety:** Privacy, confidentiality, and concrete hazards can narrow disclosure without authorizing falsehood or whole-topic suppression.
- **AC8 — Traceability and preservation:** Every clause maps to source evidence, audit IDs, preserved purposes, risks, and fixtures; all seven G005-routed records appear.
- **AC9 — Conceptual fixture validation:** I-01 through I-10 pass observable acceptance proofs, cover all allowed fixture classes needed by this goal, and evaluate relationships and behavior rather than preferred philosophical vocabulary.
- **AC10 — Scope integrity:** Source and frozen evaluation artifacts are unchanged; the execution record shows no held-out, paid, candidate, network, or remote action.
- **AC11 — Verification:** `framework/G005-verification.md` records passing evidence for AC1–AC10.
- **AC12 — Next-goal readiness:** G006 is standalone, Cycle-ready, dependency-bound to G005, and prepared without execution.

## Criterion-to-evidence map

| Criterion | Evidence |
|---|---|
| AC1 | clause-ID/function validator and ordered module |
| AC2 | per-clause word counts and metadata separation check |
| AC3 | HI-01, I-03/I-04, and ontological-closure/compulsory-belief adversarial review |
| AC4 | HI-02–HI-04 and I-01/I-02 |
| AC5 | HI-05/HI-06 and I-04/I-05 |
| AC6 | HI-07 and I-06/I-07/I-09 |
| AC7 | HI-08 and I-08 |
| AC8 | complete change register and source-purpose table |
| AC9 | ten-case fixture result table, schema validation, and semantic review showing that phrase substitution alone cannot change a result |
| AC10 | source hash/diff, frozen-artifact diff, and documented command boundary |
| AC11 | criterion-level verification table |
| AC12 | G006 goal path, status, execution contract, and roadmap state |

## Completion handoff

When G005 completes, G006 receives the validated honesty/inquiry module plus explicit interfaces for authority, hidden instructions, institutional incentives, personas, and confidentiality. G006 must preserve the non-closure hierarchy and the separation of compliance, belief, endorsement, and identity; it may clarify application only through traceable conflict rules.
