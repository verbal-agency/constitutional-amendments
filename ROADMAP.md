# Roadmap

Project: Truth-Seeking Constitution
Active goal: M1 — lever check (Proposed; execution needs Cycle selection and an approved cost ceiling)
Measurement track: M1 → M2 → M3, ahead of G008 (amendment of 2026-11-13, `framework/G006.5-roadmap-amendment.md`)
Active experimental branch: X001 — planned target-authoring slice

Goal policy: the Cycle skill governs discovery, sizing, lifecycle, closure, and handoff. `ITERATION_PROTOCOL.md` governs project-specific bounded hypothesis-and-probe loops inside an execution slice. Exploratory results may revise the active goal or amend downstream contracts; G006.5 was the first behavioral probe, and G010 remains the only official base-versus-candidate comparison.

The measurement track exists because G006.5 found no detectable behavioral difference between the provisional candidate and the source. It establishes whether a constitution in the prompt is a usable lever (M1), builds measures with headroom (M2), and attributes behavior to source themes (M3) before more constitution text is drafted. The track as a whole is capped at $25 of paid calls and two execution slices per goal.

Experimental branches are non-blocking unless explicitly promoted by the user. They may produce evidence for reopening a goal or changing the roadmap, but they do not silently alter the numbered goal sequence.

## Status model

Allowed statuses are `Discovery`, `Planned`, `Proposed`, `In progress`, `Blocked`, `Deferred`, `Drafted — unverified`, and `Complete`.

Legal transitions:

- `Discovery` → `Planned` when the target consumer, environment, success condition, first slice, and stop conditions are known or explicitly accepted as limitations.
- `Planned` → `Proposed` when dependencies are complete and the bounded execution contract is written.
- `Proposed` → `In progress` when Cycle selects the goal for execution.
- `In progress` → `Complete` only when three to five closure criteria pass and evidence is recorded.
- A behavior-bearing goal may use `Drafted — unverified` when the artifact is
  ready but no authorized model/development run has established its behavioral
  criterion. `Drafted — unverified` is not a promotion state and cannot satisfy
  a dependency that requires behavioral evidence.
- `In progress` → `Blocked` only under the platform's blocked-goal rules and with evidence of the unresolved condition.
- `In progress` → `Deferred` when valuable work is intentionally paused without being a blocker.
- `Blocked` → `In progress` when the blocking condition is resolved and execution resumes.
- `Deferred` → `Planned` or `Proposed` when the work is deliberately resumed.

Exactly one numbered goal may be `In progress`. An explicitly selected experimental branch may also be `In progress` when it is marked non-blocking and does not alter the numbered sequence. G006.5 was a bridge goal and its decision is recorded. M1, M2, and M3 are sequence goals for the purposes of this rule: G008/G009 cannot be promoted until the M1 decision is recorded and M2 has closed. A numbered goal is eligible only when all dependencies are `Complete`, it has a goal file containing a bounded execution contract, and no earlier eligible goal remains unfinished. A G006 child discovery slice may remain active while the parent is `In progress`; it must not authorize downstream implementation until its decision closes. `framework/current-goal.yaml` is the operational record of the active slice; the goal file is the durable contract.

Completion is evidence-based, not prose-based. A goal may be reopened when an iteration produces material counterevidence against its completed decision. Downstream goals must consume the amended contract rather than silently compensating for it.

## Closure and artifact budget

Every behavior-bearing goal must name at least one closure criterion that can be
checked on model or development outputs, with a named regression check. If that
run cannot happen yet, the goal remains `Drafted — unverified`; a completed
schema, fixture, or prose review is not behavioral evidence. Artifact-only goals
may close on artifact evidence when their contract explicitly says that behavior
is out of scope.

Each goal receives a default functional-artifact budget of one amendment or
replacement map, one fixture or frozen probe manifest, and one verification
record. Generated raw outputs are evidence, not a reason to create another
analysis document. An extra document requires a one-line decision justification
in the owning goal file.

Drafting and adjudication are separate responsibilities. Fixtures and expected
failure cases must be fixed before clause review; an independent model/session or
human must review a sample of expected gains, expected failures, and sentinels.
When one person must do both jobs, the review must be delayed and blind to the
new outputs, and the limitation must be recorded.

Every cycle ends with a falsifiable `what we learned` sentence. It must state
what belief would have remained unchanged without the work and what evidence
changed it. A slice that cannot produce that sentence is not a useful slice.

A measure may be used to evaluate constitution text only after it has passed two
gates on the source arm: a headroom gate (failure rate between 10% and 90%) and
an agreement gate (Cohen's kappa of 0.60 or higher between two independent
graders, or deterministic scoring). A measure that has not passed both gates can
produce leads, not findings.

Each constitutional amendment drafted from G008 onward must state, before it is
written, the measure it is expected to move, the direction, and the minimum
effect, and must be tested in isolation before integration. An amendment without
a qualified measure is recorded as unverified.

## Anti-churn gate

These rules apply before creating a repair, measurement, or discovery child:

- A diagnostic can block progression only when the project contract declared it
  a gate before candidate outputs were observed. SC-010 remains a separately
  reported, non-blocking process diagnostic under `EVALUATION_PLAN.md`.
- A child goal must change an accepted artifact, make the owning decision, or
  retire a material risk. “Create another child goal” is not sufficient closure.
- Two failed repair attempts or three consecutive slices on the same failure
  require a parent-level re-plan. Further work on that branch needs a new
  outcome justification and explicit user authorization.
- Post-hoc checkers remain diagnostic until validated against independent,
  predeclared human labels and representative paraphrases. Model judges cannot
  decide promotion until calibration, disagreement handling, and the decision
  threshold are predeclared.
- Investigation ceilings cover the whole failure branch, not each inexpensive
  subgoal separately. When the ceiling fires, choose `pivot`, `defer`, or
  `abandon`; do not rename the uncertainty and continue.
- An attribution claim requires at least 100 items per arm and one replication
  on fresh items. A difference observed on fewer than 50 outputs per arm is a
  lead, not a finding.

## Goal sequence

| Goal | Status | Dependencies | Outcome |
| --- | --- | --- | --- |
| [G001](goals/G001-truth-seeking-audit.md) | Complete | None | Produce complete source coverage, philosophical-pattern inventory, and rewrite-target register. |
| [G002](goals/G002-evaluation-baseline.md) | Complete | G001 | Freeze the cost-capped evaluation suite and record the original constitution baseline. |
| [G003](goals/G003-epistemic-framework.md) | Complete | G002 | Compress the audit into seven constitution-ready epistemic principles, with explicit safety boundaries and traceability. |
| [G004](goals/G004-core-hierarchy.md) | Complete | G003 | Decide how truth-seeking and the presumption of human agency constrain the core value hierarchy. |
| [G005](goals/G005-honesty-and-inquiry.md) | Complete | G004 | Expand honesty into an operational account of inquiry, disconfirmation, candor, speculation, and mystery. |
| [G006](goals/G006-authority-and-incentives.md) | Complete | G005 | Separate authority from epistemic warrant and adopt a principle-level replacement, evaluation, and attribution process before G007. |
| [G006.5](goals/G006.5-walking-skeleton-probe.md) | Complete | G006, G007-S3 | Assemble the smallest exact-replacement candidate and obtain the first pre-registered behavioral evidence before more drafting. Decision: no detectable difference from the source. |
| [G007](goals/G007-inquiry-and-harm.md) | Drafted — unverified | G006 | Distinguish self-regarding risk from nonconsensual harm and apply capacity-sensitive, proportionate safeguards. Drafting paused until M2 supplies a measure. |
| [M1](goals/M1-lever-check.md) | Proposed | G006.5 | Establish whether the constitution in the prompt changes false-assertion behavior at all, and whether a known-effective instruction survives placement inside it. |
| M2 | Planned | M1 | Build a behavior battery (truthfulness, authority versus evidence, curiosity) in which every measure passes the headroom and agreement gates, or is recorded as not measurable. |
| M3 | Planned | M1, M2 | Attribute measured behavior to themes of the source by knockout and isolation, with replication. Runs only if M1 shows the document drives the behavior. |
| G008 | Planned | M1 decision, M2; consumes G007 as drafted | Protect dissent, self-correction, appeals, evidence retention, and constitutional amendment, with each revision tied to a qualified measure. |
| G009 | Planned | G008 | Produce an integrated candidate constitution and traceable change log from amendments that passed an isolated test, with untested amendments marked unverified. |
| G010 | Planned | G009 | Compare candidate and base on the frozen suite and the M2 battery, run adversarial validation, resolve regressions, and publish the final constitution. |

## Experimental branches

| Branch | Status | Relationship | Purpose |
| --- | --- | --- | --- |
| [X001 — Local Mistral SFT news depolarization probe](goals/X001-mistral-finetune-experiment.md) | Planned | Non-blocking branch from G006 revision 6 | Author and preflight the bounded source-packet target slice before any local training or paid evaluation; promote, defer, or kill before G008 becomes Proposed. If M1 reads "weak lever", promotion to the mainline is the first option put to the owner. |
| [X002 — Interactive constitution map](goals/X002-interactive-constitution-map.md) | Discovery | Non-blocking productization branch from G006 revision 6 | Hold until G006.5 produces a candidate worth mapping; then integrate a provenance-preserving original/amendment map beginning with the validated replacement slice. |

## Goal boundaries

### G001 — Truth-seeking audit

Inventory what the source already supports, identify recurring limiting philosophies, and map justified patterns to rewrite targets. Do not rewrite the constitution or decide the final hierarchy.

### G002 — Evaluation protocol and baseline

Create deterministic subsets of accepted public benchmarks, a project-specific SC-001–SC-010 suite, frozen rubrics and comparison gates, and a reproducible baseline for the original constitution. Enforce the personal-cost caps in `EVALUATION_PLAN.md`.

### G003 — Epistemic framework

Compress the accepted pivot and G001 findings routed to G003 into exactly seven normative principles, with definitions, examples, boundary cases, candidate-pattern decisions, and an explicit safety-preservation interface.

### G004 — Core hierarchy

Resolve whether truth-seeking is a core value, part of ethics, or a cross-cutting procedural constraint. Pair epistemic integrity with a presumption of human agency and specify legitimacy, proportionality, and conflicts among safety, truth, disclosure, and action.

### G005 — Honesty and inquiry

Draft the constitution's epistemic practice: updating, disconfirmation, anomalies, candor, unknowns, and disciplined speculation.

### G006 — Authority and incentives

Revise institutional, operator, and persona rules so authority must establish legitimate source and scope and commercial, moral, or institutional interests cannot silently determine factual conclusions, user choice, or materially misleading framing. Adopt the principle registry, exact replacement-map traceability, semantic ablations/interactions, and attribution-based promotion process needed to test those revisions without treating wording movement as principle progress.

G006 is a parent workstream executed through bounded subgoals:

- **G006-S1 — Authority and principle contracts:** complete. Defines the seven principles, authority schemas, fixtures, and routed interfaces.
- **G006-S2 — Exact replacement assembly:** complete. Produces metadata-free, hash-recorded candidate renders from the immutable source.
- **G006-S3 — SC-010-D2 attribution:** complete. The MAP-002-only ablation restored D2 under both judges; MASK stayed honest in both arms.
- **G006-S3R — MAP-002 repair:** complete with stop disposition. One shorter, context-neutral repair failed D2 under both judges and changed MASK from honest to evasive under both.
- **G006-S3D — Evaluation-interface discovery:** complete with `pivot`. The packet was present for D2; the binary MASK contract cannot distinguish authorized truthful limitation from evasion.
- **G006-S3E — MASK measurement-contract amendment:** complete. Define four explicit MASK states, separate dishonest/evasive failures, preserve historical labels, and validate the contract with offline fixtures.
- **G006-S3F — MASK contract replay:** complete. The v2 scorer classified base and canonical S3 as `truthful_direct` and S3R as `failure/evasive`; all three historical bridges were exact at 3 calls and `$0.005217`.
- **G006-S4 — Promotion and downstream handoff:** complete with no promotion. Exact assembly and MASK measurement pass, but D2 remains a replicated material regression; route one bounded discovery goal.
- **G006-S5 — SC-010-D2 context-and-principle interaction discovery:** complete with deferred attribution. A four-cell probe found a directional edited-arm signal, but one draw per cell cannot separate replacement effects from sampling variance.
- **G006-S5R — SC-010-D2 attribution replication:** complete with no attributable factor. Three draws per cell produced 0/3 direct-answer passes in every cell; judge disagreement remained material.
- **G006-S5M — SC-010-D2 measurement/provider discovery:** complete as an exploratory diagnostic. The packet interface is valid, but the post-hoc checker and model judges are not validated promotion gates.
- **G006-S5N — D2 provider and judge calibration:** abandoned. SC-010 is non-blocking, the branch exceeded the re-plan threshold, and calibration would not advance G006's constitutional outcome.
- **G006-S6 — Outcome-based closure review:** complete with `proceed`. The offline review found the authority/provenance contract, exact replacement chain, fixtures, and SC-001–SC-009 evidence sufficient to close G006. SC-010-D2 remains a non-blocking diagnostic routed to G010.

### G006.5 — Walking-skeleton behavioral probe

Assemble a rough candidate from the available G006 exact-replacement map plus
the G005 and G007 section-ready modules using one thin provisional replacement
manifest, then run a small, pre-registered development probe against the
historical base. This is the first behavioral evidence in the mainline. It is
exploratory, uses only tracked development cases, and cannot promote a candidate
or change G010's frozen protocol. Robust map and validator hardening moves to
G009; this goal must settle only the judge calibration, disagreement,
independent-review, and attribution rules needed for the first probe.

G006.5 is intentionally small. It either produces a behaviorally informative
probe or identifies an exact assembly/measurement blocker. It does not open a
new chain of measurement children.

G006.5 closed on 2026-11-13 by owner-approved amendment. S1 assembled the
candidate; S2 to S4 ran the 15-case packet and two small follow-ups with
same-session labels; S5 (640 outputs) and S6 (800 outputs) were added by owner
authorization with blind grading by two non-target models. Decision: the
provisional candidate shows no detectable difference from the source on false
assertion (S6, validity gates passed) and no confabulation effect (S5, gates
failed, lead not supported). Two deviations from the goal contract are recorded
in the goal file: S5 and S6 used new probe manifests, and the independent-review
criterion was met by blind model grading of those packets, not by review of the
S2 author labels. No human review was done.

### M1 — Lever check

Run the 100 plain G006.5-S6 items under six arms: `base`, `full`, `none` (no
constitution), `short` (one authored paragraph), `base+inside` (a
known-effective calibration instruction inserted in the "Being honest"
section), and `base+end` (the same instruction appended). Grade blind with the
G006.5-S6 graders and apply the G006.5-S6 permutation test. The four possible readings and what each one
triggers are fixed in the goal file before any output exists. M1 does not test
or draft amendment text.

### M2 — Behavior battery

Qualify measures before any text is evaluated on them. Truthfulness is already
qualified by G006.5-S6. Authority versus evidence needs cases in which an operator,
expert, or institution asserts something the supplied evidence contradicts,
scored against that evidence. Curiosity needs an operational definition first,
then cases and a rubric checked against at least 30 human labels. Authored
cases are reviewed by someone other than their drafter. Each measure gets two
attempts; a measure that fails twice is dropped and the project's claim is
narrowed. No candidate or amendment text is evaluated in M2.

### M3 — Theme attribution

Runs only if M1 reads "the document drives this behavior" for at least one
measure. Group the source's top-level sections into 8 to 10 themes fixed before
any run. Remove one theme at a time (what the behavior depends on) and use one
theme alone (what is sufficient), on each qualified measure. A theme that
differs by 5 points or more with p < 0.05 under both graders is rerun once on
fresh items; only a replicated effect is recorded as a driver. The result is
evidence about text in the prompt, not about training. If M1 instead reads
"salience or position", M3 is replaced by a placement study; if M1 reads "weak
lever", M3 does not run and the owner makes a pivot decision.

### G007 — Inquiry and harm

Create a layered analysis of belief, inquiry, speech, disclosure, and action that distinguishes competent self-regarding choice from nonconsensual harm and uses concrete, capacity-sensitive, proportionate restrictions for genuine hazards.

G007-S1 completed the offline hazard/proportionality schema and H-01–H-12
fixture contract. G007-S2 drafted HA-01–HA-07 and passed deterministic
structure/provenance checks. G007-S3 reviewed all fixtures and six boundary
probes offline and repaired the H-01 discriminating-test gap in HA-04. G007-S4
then froze a 15-case development packet with ten paired cases and five
sentinels. The behavioral walking skeleton is now owned by G006.5 so G007 can
finish its clause contract without pretending that offline fixtures establish
model behavior. G007 still does not authorize model calls, and the official
G010 comparison and paid evaluation remain unauthorized.

The G007-S4 packet was run under G006.5 (S2 to S4). The source arm already
passed seven of its ten paired cases, so it could not establish G007's
behavioral criterion. G007 is therefore `Drafted — unverified`: its clauses
stand as written, and no further G007 drafting happens until M2 supplies a
qualified measure that the clauses are expected to move.

### G008 — Dissent and amendment

Revise corrigibility, identity stability, reflective equilibrium, and final-authority provisions to prevent self-sealing governance. Begin only after the M1 decision is recorded and M2 has closed. Each revision names its measure, direction, and minimum effect before it is written. If M1 reads "weak lever", G008 does not start until the owner has made the pivot decision.

### G009 — Integration

Create a distinct candidate constitution and source-to-revision change log without altering the upstream source. Use G006.5's exact-replacement contract and the M2 measures, integrate amendments that passed an isolated test, mark the rest unverified, and run a development probe before treating integration as complete. Do not claim final acceptance before G010.

### G010 — Controlled comparison and finalization

G010 evaluates on the M2 battery in addition to the frozen `lean-v1` suite, and
takes a second target model as an input so that the result does not rest on one
model.

Run the frozen paired comparison against the base and candidate constitutions, including misinformation, false balance, contrarianism, reckless disclosure, institutional capture, commercial pressure, paternalism, epistemic authoritarianism, precautionary conservatism, benevolent deception, and constitutional self-protection. Report SC-010 separately as process-level audit capability; complete the human spot-check and position-swapped judge consistency checks; preserve the MASK license caveat. Resolve material regressions within budget, record scenario evidence, and publish the final constitution.

Before any model judge affects the official decision, G010 must predeclare its
role, validate it against an independently human-labeled calibration sample,
define disagreement handling, and set the decision threshold. Post-hoc checkers
may explain outputs but cannot become official gates. SC-010 results remain
separate and non-blocking.

### X001 — Local Mistral SFT news depolarization probe

Run as a separately authorized, non-blocking research branch. The first bounded slice authors and preflights the reviewed source-packet targets; local training and evaluation remain deferred until that slice closes. Later slices may use a compatible open-weight Mistral checkpoint and reproducible local LoRA/SFT setup to test whether constitution-derived supervision generalizes to held-out semantic families, with evidence-centered news depolarization as the primary applied target. Compare untuned and SFT-adapted behavior under controlled constitution conditions, a strong-prompt control, and a separately approved frontier reference, while tracking policy-version lineage, source-packet integrity, false balance, label churn, style confounds, and regressions. Preference optimization/RLAIF, autonomous retrieval, and hosted fine-tuning are deferred follow-up paths, not part of the first claim. Treat the result as evidence about a bounded SFT package, not as validation of a complete alignment pipeline or a substitute for the prompt-conditioned constitutional comparison. Require an explicit practical classification and pivot recommendation before changing the mainline sequence.

### X002 — Interactive constitution map

Run as a separately authorized, non-blocking website branch. Generate a deterministic map package from the immutable source and an exact replacement map, then integrate a keyboard-accessible component that alternates each selected passage between original and amendment text while preserving source lines, stable IDs, principle links, and review status. Begin with the G006 replacement slice and expand only after source integrity, accessibility, stale-data detection, and website review pass. The map is an explanation and audit surface, not a constitutional authority or a substitute for G010's controlled comparison.

## Finding routing

During a cycle, every incidental finding goes to exactly one destination:

- the active goal when required by an active criterion;
- a named future goal when already scheduled;
- `BACKLOG.md` when valuable but unscheduled;
- an observation when no action is justified;
- or a blocker when a material decision or external change prevents completion.

Do not duplicate a finding across destinations. Material roadmap reordering requires user approval.
