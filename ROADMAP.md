# Roadmap

Project: Truth-Seeking Constitution
Active goal: G006
Next eligible goal: G006-S3F MASK contract replay before G006-S4 or G007
Active experimental branch: X001 — planned target-authoring slice

Goal policy: the Cycle skill governs discovery, sizing, lifecycle, closure, and handoff. `ITERATION_PROTOCOL.md` governs project-specific bounded hypothesis-and-probe loops inside an execution slice. Exploratory results may revise the active goal or amend downstream contracts; G010 remains the only official base-versus-candidate comparison.

Experimental branches are non-blocking unless explicitly promoted by the user. They may produce evidence for reopening a goal or changing the roadmap, but they do not silently alter the numbered goal sequence.

## Status model

Allowed statuses are `Discovery`, `Planned`, `Proposed`, `In progress`, `Blocked`, `Deferred`, and `Complete`.

Legal transitions:

- `Discovery` → `Planned` when the target consumer, environment, success condition, first slice, and stop conditions are known or explicitly accepted as limitations.
- `Planned` → `Proposed` when dependencies are complete and the bounded execution contract is written.
- `Proposed` → `In progress` when Cycle selects the goal for execution.
- `In progress` → `Complete` only when three to five closure criteria pass and evidence is recorded.
- `In progress` → `Blocked` only under the platform's blocked-goal rules and with evidence of the unresolved condition.
- `In progress` → `Deferred` when valuable work is intentionally paused without being a blocker.
- `Blocked` → `In progress` when the blocking condition is resolved and execution resumes.
- `Deferred` → `Planned` or `Proposed` when the work is deliberately resumed.

Exactly one numbered goal may be `In progress`. An explicitly selected experimental branch may also be `In progress` when it is marked non-blocking and does not alter the numbered sequence. A numbered goal is eligible only when all dependencies are `Complete`, it has a goal file containing a bounded execution contract, and no earlier eligible goal remains unfinished. A G006 child discovery slice may remain active while the parent is `In progress`; it must not authorize downstream implementation until its decision closes. `framework/current-goal.yaml` is the operational record of the active slice; the goal file is the durable contract.

Completion is evidence-based, not prose-based. A goal may be reopened when an iteration produces material counterevidence against its completed decision. Downstream goals must consume the amended contract rather than silently compensating for it.

## Goal sequence

| Goal | Status | Dependencies | Outcome |
| --- | --- | --- | --- |
| [G001](goals/G001-truth-seeking-audit.md) | Complete | None | Produce complete source coverage, philosophical-pattern inventory, and rewrite-target register. |
| [G002](goals/G002-evaluation-baseline.md) | Complete | G001 | Freeze the cost-capped evaluation suite and record the original constitution baseline. |
| [G003](goals/G003-epistemic-framework.md) | Complete | G002 | Compress the audit into seven constitution-ready epistemic principles, with explicit safety boundaries and traceability. |
| [G004](goals/G004-core-hierarchy.md) | Complete | G003 | Decide how truth-seeking and the presumption of human agency constrain the core value hierarchy. |
| [G005](goals/G005-honesty-and-inquiry.md) | Complete | G004 | Expand honesty into an operational account of inquiry, disconfirmation, candor, speculation, and mystery. |
| [G006](goals/G006-authority-and-incentives.md) | In progress | G005 | Separate authority from epistemic warrant and adopt a principle-level replacement, evaluation, and attribution process before G007. |
| [G007](goals/G007-inquiry-and-harm.md) | Proposed | G006 | Distinguish self-regarding risk from nonconsensual harm and apply capacity-sensitive, proportionate safeguards. |
| G008 | Planned | G007 | Protect dissent, self-correction, appeals, evidence retention, and constitutional amendment. |
| G009 | Planned | G008 | Produce an integrated candidate constitution and traceable change log. |
| G010 | Planned | G009 | Compare candidate and base, run adversarial validation, resolve regressions, and publish the final constitution. |

## Experimental branches

| Branch | Status | Relationship | Purpose |
| --- | --- | --- | --- |
| [X001 — Local Mistral SFT news depolarization probe](goals/X001-mistral-finetune-experiment.md) | Planned | Non-blocking branch from G006 revision 6 | Author and preflight the bounded source-packet target slice before any local training or paid evaluation. |
| [X002 — Interactive constitution map](goals/X002-interactive-constitution-map.md) | Discovery | Non-blocking productization branch from G006 revision 6 | Identify the website target, then integrate a provenance-preserving original/amendment map beginning with the validated G006 replacement slice. |

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
- **G006-S3F — MASK contract replay:** proposed and next. Apply the v2 scorer to preserved base/S3/S3R outputs before another wording or promotion run.
- **G006-S4 — Promotion and downstream handoff:** blocked until S3F demonstrates the stable measurement contract on preserved outputs; no collateral gate or G007 handoff yet.

### G007 — Inquiry and harm

Create a layered analysis of belief, inquiry, speech, disclosure, and action that distinguishes competent self-regarding choice from nonconsensual harm and uses concrete, capacity-sensitive, proportionate restrictions for genuine hazards.

### G008 — Dissent and amendment

Revise corrigibility, identity stability, reflective equilibrium, and final-authority provisions to prevent self-sealing governance.

### G009 — Integration

Create a distinct candidate constitution and source-to-revision change log without altering the upstream source. Do not claim final acceptance before G010.

### G010 — Controlled comparison and finalization

Run the frozen paired comparison against the base and candidate constitutions, including misinformation, false balance, contrarianism, reckless disclosure, institutional capture, commercial pressure, paternalism, epistemic authoritarianism, precautionary conservatism, benevolent deception, and constitutional self-protection. Report SC-010 separately as process-level audit capability; complete the human spot-check and position-swapped judge consistency checks; preserve the MASK license caveat. Resolve material regressions within budget, record scenario evidence, and publish the final constitution.

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
