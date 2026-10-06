# Roadmap

Project: Truth-Seeking Constitution
Active goal: G002
Next eligible goal: G003

## Status model

Allowed statuses are `Planned`, `Proposed`, `In progress`, `Blocked`, and `Complete`.

Legal transitions:

- `Planned` → `Proposed` when dependencies are complete and the full execution contract is written.
- `Proposed` → `In progress` when Cycle selects the goal for execution.
- `In progress` → `Complete` only when every goal criterion passes and evidence is recorded.
- `In progress` → `Blocked` only under the platform's blocked-goal rules and with evidence of the unresolved condition.
- `Blocked` → `In progress` when the blocking condition is resolved and execution resumes.

Exactly one goal may be `In progress`. A goal is eligible only when all dependencies are `Complete`, it has a goal file containing a complete execution contract, and no earlier eligible goal remains unfinished.

## Goal sequence

| Goal | Status | Dependencies | Outcome |
| --- | --- | --- | --- |
| [G001](goals/G001-truth-seeking-audit.md) | Complete | None | Produce complete source coverage, philosophical-pattern inventory, and rewrite-target register. |
| [G002](goals/G002-evaluation-baseline.md) | In progress | G001 | Freeze the cost-capped evaluation suite and record the original constitution baseline. |
| [G003](goals/G003-epistemic-framework.md) | Planned | G002 | Compress the audit into seven constitution-ready epistemic principles, with explicit safety boundaries and traceability. |
| G004 | Planned | G003 | Decide and specify how truth-seeking interacts with the core value hierarchy. |
| G005 | Planned | G004 | Expand honesty into an operational account of inquiry, disconfirmation, candor, speculation, and mystery. |
| G006 | Planned | G005 | Separate operational authority from epistemic authority across principals, guidelines, confidentiality, and personas. |
| G007 | Planned | G006 | Separate legitimate inquiry from harmful operational assistance while retaining narrowly tailored safeguards. |
| G008 | Planned | G007 | Protect dissent, self-correction, appeals, evidence retention, and constitutional amendment. |
| G009 | Planned | G008 | Produce an integrated candidate constitution and traceable change log. |
| G010 | Planned | G009 | Compare candidate and base, run adversarial validation, resolve regressions, and publish the final constitution. |

## Goal boundaries

### G001 — Truth-seeking audit

Inventory what the source already supports, identify recurring limiting philosophies, and map justified patterns to rewrite targets. Do not rewrite the constitution or decide the final hierarchy.

### G002 — Evaluation protocol and baseline

Create deterministic subsets of accepted public benchmarks, a project-specific SC-001–SC-010 suite, frozen rubrics and comparison gates, and a reproducible baseline for the original constitution. Enforce the personal-cost caps in `EVALUATION_PLAN.md`.

### G003 — Epistemic framework

Compress the accepted pivot and G001 findings routed to G003 into exactly seven normative principles, with definitions, examples, boundary cases, candidate-pattern decisions, and an explicit safety-preservation interface.

### G004 — Core hierarchy

Resolve whether truth-seeking is a core value, part of ethics, or a cross-cutting procedural constraint. Specify conflicts among safety, truth, disclosure, and action.

### G005 — Honesty and inquiry

Draft the constitution's epistemic practice: updating, disconfirmation, anomalies, candor, unknowns, and disciplined speculation.

### G006 — Authority and incentives

Revise institutional, operator, and persona rules so authority and commercial interests cannot silently determine factual conclusions or materially misleading framing.

### G007 — Inquiry and harm

Create a layered analysis of belief, inquiry, speech, disclosure, and action, with concrete and proportionate restrictions for genuine hazards.

### G008 — Dissent and amendment

Revise corrigibility, identity stability, reflective equilibrium, and final-authority provisions to prevent self-sealing governance.

### G009 — Integration

Create a distinct candidate constitution and source-to-revision change log without altering the upstream source. Do not claim final acceptance before G010.

### G010 — Controlled comparison and finalization

Run the frozen paired comparison against the base and candidate constitutions, including misinformation, false balance, contrarianism, reckless disclosure, institutional capture, commercial pressure, paternalism, epistemic authoritarianism, precautionary conservatism, benevolent deception, and constitutional self-protection. Resolve material regressions within budget, record scenario evidence, and publish the final constitution.

## Finding routing

During a cycle, every incidental finding goes to exactly one destination:

- the active goal when required by an active criterion;
- a named future goal when already scheduled;
- `BACKLOG.md` when valuable but unscheduled;
- an observation when no action is justified;
- or a blocker when a material decision or external change prevents completion.

Do not duplicate a finding across destinations. Material roadmap reordering requires user approval.
