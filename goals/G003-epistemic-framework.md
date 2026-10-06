# G003 — Compress the Audit into an Epistemic Framework

Status: Proposed
Dependencies: G002 Complete
Next goal on completion: G004

## Objective

Convert the truth-seeking pivot and the G001 audit into a compact, constitution-ready epistemic framework of exactly seven coherent principles. The framework must preserve legitimate safety functions while preventing safety, authority, incentives, convention, or trained identity from becoming substitutes for evidence or barriers to warranted correction.

G003 is synthesis, not another discovery pass. It should reduce the 51 audit records and their pattern relationships into a small normative architecture that later drafting goals can apply consistently.

## Project alignment

Advances O1, O3, O4, O6, and O7. Supplies the conceptual vocabulary and safety interface needed by G004–G008 without deciding the final core-value hierarchy or rewriting source passages.

Directly supports SC-001 through SC-009. SC-010 is process-level evidence that the audit grouped recurring mechanisms responsibly; it is not itself a principle of model behavior. SC-011 remains reserved for the final controlled comparison.

Preserves A1–A14, especially charitable interpretation, separate epistemic planes, narrow tailoring, self-application, and evaluation integrity.

## Inputs

- `PROJECT.md`
- `TRUTH_SEEKING_PIVOT.md`
- `ROADMAP.md`
- `EXECUTION_PROFILE.md`
- `20260120-constitution.md` as immutable context
- `audits/truth-seeking-audit.md`
- `audits/philosophical-patterns.md`
- `audits/truth-seeking-coverage.md`
- `audits/G001-verification.md`
- G002's tracked evaluation design and base report
- Development cases in `evals/datasets/custom-dev-v1.jsonl`

G003 must not read held-out prompts, annotations, outputs, or scores under `evals/private/`.

## Required seven-principle architecture

The final framework must contain exactly these seven conceptual functions. Names and wording may improve during execution, but merging, splitting, adding, or removing a function requires an explicit recorded rationale and user approval.

1. **Reality exceeds present knowledge.** Distinguish reality from belief, knowledge claims, consensus, and constitutional commitments. Treat empirical and moral understanding as revisable without implying that every claim is equally plausible.
2. **Belief tracks evidence through updating.** Set confidence in proportion to evidence; test anomalies under comparable standards; distinguish expertise and consensus as relevant evidence from authority as proof; state what would change a conclusion.
3. **Inquiry and action occupy different planes.** Distinguish belief, inquiry, analysis, speech, disclosure, acquisition, and execution. Constrain only the planes supported by a concrete harm rationale and preserve safer evidence-generating alternatives where possible.
4. **Candor includes material context and provenance.** Prevent literal truth from becoming misleading through omission, framing, persona, hidden incentives, or undisclosed constraints, while allowing narrowly justified confidentiality and hazardous-information controls.
5. **Novelty and mystery remain disciplined.** Permit unconventional hypotheses, conceptual innovation, and articulate unknowns while labeling speculation, representing unequal evidence, and naming falsifiers or discriminating tests.
6. **Epistemic warrant is independent of role, incentive, and identity.** Keep operational authority separate from factual warrant; expose relevant institutional incentives; and do not treat trained identity, convention, respectability, or hoped-for self-endorsement as evidence that a claim or value is correct.
7. **The framework preserves dissent and corrects itself.** Protect evidence retention, reasoned disagreement, appeal, review, and amendment. Criticism must be assessed on its substance rather than reclassified as instability, manipulation, disloyalty, or failed self-recognition.

These are constitutional functions, not seven independent supreme values. G004 decides how they interact with the source value hierarchy.

## Safety-preservation rule

G003 must preserve the purpose of legitimate safety constraints, not assume that every existing safety mechanism or formulation is correct.

The framework must make all of the following true at once:

- safety may prohibit or restrict dangerous action, acquisition, or operational disclosure;
- safety may justify confidentiality or delayed disclosure when a concrete competing duty applies;
- safety does not require false belief, fabricated certainty, or knowingly false factual assertions;
- an action restriction does not by itself prohibit non-operational analysis, criticism, evidence retention, or review;
- withheld content should be narrowed to the hazardous component when a safer useful response is available;
- the reason, scope, evidence threshold, affected epistemic plane, and review path for a material restriction remain legible to the degree compatible with the protected interest;
- emergency or irreversible-risk rules may act before full certainty, but they remain reviewable and do not convert precaution into proof;
- preserving safety never means immunizing the definition of safety from evidence-bearing criticism.

Where truth-seeking and safety cannot both be fully expressed, the framework must identify the actual conflict—such as disclosure versus concrete operational harm—rather than describing reality itself as subordinate to safety.

## In scope

- Compressing G001 findings routed to G003 into the seven principles.
- Defining constitution-ready terms and boundaries for each principle.
- Deciding whether to accept, reject, split, or rename candidate patterns PC-001 and PC-002.
- Defining the distinction between legitimate value formation and identity-conditioned insulation from dissent.
- Defining the distinction between legitimate action constraints and loss of evidence, inquiry, or correction capacity.
- Writing positive, negative, boundary, and safety-conflict examples.
- Mapping each G003-routed audit record to at least one principle.
- Recording unresolved hierarchy questions for G004 without answering them prematurely.
- Preparing a standalone G004 goal.

## Out of scope

- Editing `20260120-constitution.md`.
- Drafting the integrated candidate constitution.
- Deciding whether truth-seeking is a core value, part of ethics, or a cross-cutting procedural constraint; G004 owns that decision.
- Rewriting authority, honesty, harm, corrigibility, or identity sections; G005–G008 own passage-level application.
- Treating truth-seeking as mandatory disclosure of all information.
- Weakening hard action-level safeguards merely because related ideas remain legitimate subjects of inquiry.
- Adding new audit records unless a cited G003 input is demonstrably malformed or internally inconsistent.
- Reading held-out evaluation material.
- Running paid evaluations, network calls, or candidate-arm generations.

## Deliverables

- `framework/epistemic-framework.md` — the seven principles, definitions, safety interface, boundary cases, and examples.
- `framework/G003-traceability.md` — audit-to-principle mappings, pattern decisions, unresolved G004 questions, and preservation obligations.
- `framework/G003-verification.md` — criterion-level completion evidence.
- `goals/G004-core-hierarchy.md` — a standalone Cycle-ready successor, prepared but not executed.
- Updated `ROADMAP.md` statuses only after every G003 acceptance criterion passes.

## Required method

1. Confirm G002 is complete and its evaluation artifacts are frozen before beginning substantive work.
2. Read the pivot, the G001 records routed to G003, PC-001, PC-002, and their counterevidence.
3. Create the traceability matrix before drafting prose; assign each routed finding to one or more of the seven functions.
4. Draft a one-sentence rule, rationale, scope, safety interaction, failure mode, and amendment implication for each principle.
5. Define all terms that could silently change meaning across principles.
6. Test each principle against at least one positive case, one overreach case, one safety-conflict case, and one counterexample.
7. Decide PC-001 and PC-002 using the taxonomy decision schema below. Do not promote either merely because it has a name.
8. Run a compression review: remove duplicate duties, ornamental philosophy, and implementation detail that belongs to G004–G008.
9. Run a contradiction review across all seven principles and the safety-preservation rule.
10. Verify every acceptance criterion and prepare G004 without executing it.

## Principle specification schema

Each principle in `framework/epistemic-framework.md` must contain:

- stable ID `EP-01` through `EP-07`;
- name;
- constitution-ready rule of no more than 90 words;
- rationale;
- protected capacities;
- epistemic planes affected;
- legitimate constraints and their evidence threshold;
- required escape, review, or amendment path;
- positive example;
- overreach or misuse example;
- safety-conflict example;
- relationships to other principles;
- mapped audit and pattern IDs;
- open hierarchy question, or `None`.

The supporting explanation may be longer, but the seven rules together must remain readable as one compact constitutional section.

## Taxonomy decision schema

For PC-001 and PC-002, record:

- decision: `promote`, `rename-and-promote`, `merge`, `retain-candidate`, or `reject`;
- final definition or rejection rationale;
- affirmative evidence IDs;
- counterevidence and near misses;
- boundary with the closest canonical pattern;
- principle mapping;
- downstream goal responsible for application.

Promotion changes the project taxonomy only after the decision is recorded with evidence. A promoted label remains a diagnostic mechanism, not proof that every linked passage requires amendment.

## Compression rules

- Exactly seven principles; the audit remains the detailed evidence layer.
- One principle may address several patterns when they share a constitutional remedy.
- Similar wording is not a reason to merge principles if the protected capacity or failure mode differs.
- Do not repeat a complete pattern definition inside every principle; link to the traceability artifact.
- Preserve counterevidence and legitimate purposes even when several findings compress into one rule.
- Prefer operational distinctions and observable behavior over slogans such as “seek truth at all costs.”
- Do not create a composite philosophical score or claim that the seven principles exhaust epistemology.

## Deterministic behavior matrix

| Condition | Required framework result | Prohibited result |
|---|---|---|
| New credible evidence conflicts with a current conclusion | Compare evidence and update confidence proportionally | Preserve the conclusion because it is current or official |
| Consensus is strong and an anomaly is documented | Represent unequal support and name a discriminating test | Dismiss by convention or grant equal credence automatically |
| An authority controls an action | Follow legitimate action controls while preserving factual disagreement | Treat role authority as proof |
| Information has a concrete operational hazard | Withhold the hazardous component and offer safe analysis where possible | Fabricate, moralize, or suppress the whole subject without analysis |
| Disclosure would violate privacy or confidentiality | Preserve the fact of the limitation and avoid a misleading impression | Reveal protected data or create a knowingly false impression |
| A hypothesis is novel and weakly supported | Label it speculative and identify tests | Present novelty as proof or reject novelty as illegitimate |
| The answer is not known | State the unknown, its source, live possibilities, and useful next evidence | Manufacture closure or use “mystery” as an explanation |
| Evidence challenges a safety rule | Preserve the evidence and route review while continuing necessary action limits | Treat criticism itself as unsafe or as proof of corruption |
| A trained value is sincerely disputed | Assess the reasons and allow durable disagreement | Treat non-endorsement as defective identity or failed understanding |
| A restriction is precautionary and urgent | Permit temporary conservative action with explicit review | Convert temporary precaution into permanent epistemic doctrine |

## Invariants and illegal states

- The source constitution remains unchanged.
- The framework contains exactly seven principle specifications.
- Every G003-routed audit record appears in the traceability matrix.
- PC-001 and PC-002 each receive an explicit taxonomy decision.
- Every principle includes a safety-conflict example and preserves at least one legitimate purpose from the source.
- No principle equates truth with current knowledge, consensus, authority, or the constitution.
- No principle requires unrestricted disclosure or dangerous operational assistance.
- No safety rule requires factual falsification, evidence destruction, or immunity from review.
- No held-out evaluation artifact is read or modified.
- G004 hierarchy questions remain explicitly unresolved.

Any violation prevents G003 completion.

## Checkpoint and stop rules

- Checkpoint after the traceability matrix, first seven-principle draft, taxonomy decisions, contradiction review, verification, and G004 handoff.
- If G002 is incomplete or its frozen measurement artifacts change, do not begin or continue substantive G003 drafting.
- If compression reveals a genuine eighth constitutional function that cannot fit without losing a distinct protected capacity or failure mode, stop and request a user decision rather than silently expanding the architecture.
- If a proposed principle would require weakening a hard action-level safeguard, record the conflict for G004/G007 and stop that line of drafting.
- If two principles impose contradictory behavior in the same boundary case, keep G003 in progress until the precedence question is either resolved within scope or explicitly routed to G004.

## Authority and side-effect boundaries

- Repository-local reads and the scoped deliverable writes above are allowed.
- No network access, package installation, paid model call, credential access, external publication, Git push, or remote mutation is authorized.
- G003 may inspect tracked development cases solely as boundary tests; it must not tune principles to base outputs or inspect held-out material.
- G004 may be prepared but not executed.

## Acceptance criteria

- **AC1 — Seven-principle compression:** The framework contains exactly EP-01–EP-07 and covers all required conceptual functions without duplicating the audit.
- **AC2 — Traceability:** Every G003-routed audit record and both candidate patterns map to a principle, disposition, and downstream application goal.
- **AC3 — Constitution-ready rules:** Each principle satisfies the specification schema and its rule is no more than 90 words.
- **AC4 — Safety compatibility:** The framework preserves legitimate action, privacy, confidentiality, and hazardous-information safeguards while prohibiting safety from becoming factual falsification or epistemic immunity.
- **AC5 — Plane separation:** Belief, inquiry, analysis, speech, disclosure, acquisition, and execution are distinguished wherever different constraints apply.
- **AC6 — Evidence discipline:** The framework preserves unequal evidence, calibration, consensus as evidence rather than proof, and explicit update conditions.
- **AC7 — Mystery and innovation:** Unknowns and novel hypotheses remain explorable without licensing fabrication, false balance, or reckless action.
- **AC8 — Authority and identity independence:** Operational role, institutional incentive, convention, and trained identity cannot independently establish truth or invalidate dissent.
- **AC9 — Self-application:** The framework includes evidence retention, review, dissent, and amendment rules that apply to itself.
- **AC10 — Candidate-pattern decisions:** PC-001 and PC-002 receive complete, evidence-backed taxonomy decisions.
- **AC11 — Boundary validation:** Every matrix condition has at least one corresponding example and no unresolved internal contradiction remains hidden.
- **AC12 — Scope integrity:** The source is unchanged, no held-out artifact was accessed, no candidate evaluation ran, and hierarchy decisions remain with G004.
- **AC13 — Verification:** `framework/G003-verification.md` records passing evidence for AC1–AC12.
- **AC14 — Next-goal readiness:** G004 is standalone, Cycle-ready, dependency-bound to G003, and prepared without execution.

## Criterion-to-evidence map

| Criterion | Evidence |
|---|---|
| AC1 | principle count and compression review |
| AC2 | complete rows in `G003-traceability.md` |
| AC3 | schema and word-count validation |
| AC4 | safety-preservation checklist and boundary cases |
| AC5 | epistemic-plane matrix |
| AC6 | evidence, authority, and anomaly examples |
| AC7 | mystery and speculation examples |
| AC8 | authority, incentive, convention, and identity cases |
| AC9 | self-application and amendment section |
| AC10 | two complete taxonomy decision records |
| AC11 | deterministic behavior matrix cross-reference and contradiction review |
| AC12 | source hash/diff, held-out access declaration, and candidate-run absence check |
| AC13 | AC1–AC12 verification table with every result `Pass` |
| AC14 | G004 path, readiness checklist, and roadmap state |

## Completion handoff

When G003 completes, G004 receives the seven principles as a coherent package and decides their constitutional placement and priority. G004 must not reopen the 51 audit records as 51 independent drafting demands; it should use the traceability matrix only to test whether the hierarchy preserves the framework's purposes and safety obligations.
