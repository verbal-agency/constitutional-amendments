# Iteration Protocol

Status: Canonical bounded-iteration workflow
Applies to: execution slices in G001–G010 and experimental branches
Parent protocol: Cycle skill

## Purpose

The roadmap is iterative, not purely linear. Each execution slice may produce evidence that changes its own conclusion, requires a revision, or changes a downstream goal's contract. The Cycle skill governs goal discovery, scope, lifecycle, and closure; this file governs the bounded hypothesis-and-probe loop after the current slice is ready.

## Slice boundary

Before starting this loop, the current goal must have a populated `framework/current-goal.yaml`. If the target consumer, environment, authority, source of truth, or success condition is materially unresolved, stop and return the goal to the Cycle skill's discovery gate.

One loop changes one primary artifact or one tightly coupled artifact set. Run no more than three bounded iterations without checkpointing and re-planning. A new external integration, model family, dataset family, publication surface, or major consumer is a new discovery decision, not an incidental iteration.

## Loop

Each active execution slice runs this loop until its bounded criteria pass, a stop condition fires, or the slice is re-planned:

1. **State the hypothesis.** Identify the claim, rule, clause, taxonomy, or evaluation choice being tested.
2. **Make the smallest change.** Change one bounded artifact or decision at a time.
3. **Probe it.** Use deterministic checks, offline fixtures, development cases, and—when useful—a local or open model. Use only tracked development/public cases before G010.
4. **Compare the result.** Compare the new result with the prior artifact, the source purpose it must preserve, and the relevant failure modes.
5. **Review the evidence.** Record what improved, regressed, remained uncertain, or was not actually tested.
6. **Route the finding.** Choose `accept`, `revise-current-goal`, `reopen-upstream`, `amend-downstream`, `block`, `defer`, or `observe`.
7. **Checkpoint.** Preserve the artifact hash, probe inputs, outputs or summaries, decision, and downstream impact before the next loop.

A goal does not close merely because its prose is complete. It closes when its loop record has no unresolved material finding and its acceptance evidence remains valid.

## Test cadence

The hypothesis and attribution steps apply after every bounded iteration, including a wording change, fixture change, rubric change, or decision change. The probe size scales with the change:

- **Every iteration:** run the smallest relevant offline or development check and record paired transitions, causal attribution, uncertainty, and routing.
- **After a material clause or interface revision:** run a broader tracked development subset, including controls for the suspected mechanism and any relevant identity-swapped variants.
- **At a stage or integration boundary:** run the 140-case public/development comparison when the result could change a downstream goal or promotion decision.
- **At G010 only:** run the frozen official comparison, including the held-out split and final human/judge review.

For a material failure, use this staged repair loop before the broader comparison:

1. **Isolate the failure.** Preserve the original prompt, output, score, rubric decision, and failure classification.
2. **Form a repair hypothesis.** State the smallest clause or prompt-envelope change expected to address the failure, the expected tradeoff, a competing explanation, and a falsifier.
3. **Run a focused repair set.** Include the failing cases, matched controls for the suspected mechanism, and untouched sentinel cases from unrelated scenarios. Do not replace cases after seeing outputs.
4. **Review the transition.** Record whether the failure was fixed, moved, unchanged, or made ambiguous. A targeted improvement is diagnostic, not proof of general improvement.
5. **Repeat only when needed.** Make one bounded revision per loop. Stop if the same failure persists after two bounded revisions, if a new material regression appears, or if attribution remains unresolved and needs a broader test.
6. **Run the collateral-damage pass.** After the focused repair stabilizes, run the full frozen public/development subset relevant to the stage. Do not promote or close the goal until that pass has been reviewed for unrelated regressions.

The focused set and sentinel set are recorded separately. Failure cases may be reused to diagnose a repair; sentinels must remain untouched and must not be selected or rewritten based on observed outputs.

Use the frozen historical base as the control by default. Regenerate the base only when a control condition changed, the historical record is incomplete for the comparison, or the hypothesis specifically requires a same-run control. Label that extra control as exploratory and do not spend its cost by default when a valid historical control exists.

Do not use the absence of a full-suite run to skip attribution after a small iteration. Do not use a small probe to make the final project claim.

## Causal-attribution protocol

The iteration loop is not only a before/after comparison. When a result is materially better or worse, record a bounded hypothesis about *why* the change occurred. The hypothesis is an explanation to test, not a fact inferred from the result.

Every iteration therefore has two linked hypothesis records:

1. **Predictive hypothesis — before the probe.** What do we expect to change, in which direction, and through what proposed mechanism?
2. **Explanatory hypothesis — after the probe.** Given the observed transitions, what mechanism now best explains the gain, regression, or non-change?

The explanatory hypothesis may be generated after seeing the result, but it cannot be promoted to a causal conclusion until a follow-up test distinguishes it from plausible alternatives. If the original prediction was wrong, preserve both records: the failed prediction is evidence, and the later explanation remains provisional.

Before running a probe, record:

- the mechanism being changed;
- the predictive hypothesis and its expected direction;
- the predicted improvement and the predicted regression or tradeoff;
- the cases, controls, or identity-swapped variants that should show the effect;
- at least one competing explanation;
- the observation that would weaken or falsify the hypothesis.

After the probe, record for each material result:

- the paired transition or raw item change;
- the explanatory hypothesis for why the change occurred;
- whether the predicted signature appeared in the intended cases and controls;
- whether the result could instead be explained by prompt sensitivity, judge ambiguity, sampling, verbosity, or a metric mismatch;
- an evidence status: `supported`, `weakened`, `unresolved`, or `metric-confounded`;
- the smallest follow-up test that would distinguish the remaining explanations.

When a secondary judge is used, judge the same base and candidate outputs with the same prompt, rubric, and case order. Preserve primary and secondary results separately; do not average them into one score. Report case-level agreement, score differences, critical-failure disagreements, and the cases requiring manual review. If the secondary judge becomes the primary judge, rescore both arms on the comparison set rather than judging only the candidate.

Attribution rules:

- A single response can illustrate a mechanism but cannot establish it.
- A non-significant result is not evidence that the mechanism is absent.
- A gain on one metric and a loss on another must remain separate findings; do not average away the tradeoff.
- When a rubric rewards an unsafe or otherwise disallowed behavior, classify the result as `metric-confounded` and route a rubric amendment separately from a constitution amendment.
- If a change could affect both truth-seeking and user accommodation, include identity-swapped or persona-neutral variants before calling it progress.

## Model-probe boundary

- Local or open-model probes are development evidence. They may reveal regressions, overreach, ambiguity, or missed cases, but they do not establish the final project claim.
- Development probes may use public and tracked development cases only. `evals/private/` remains prohibited to G001–G009.
- A target-model checkpoint may be run only with an approved preflight and must be labeled exploratory until G010.
- Exploratory runs never replace, rewrite, or tune the frozen base, held-out split, comparison gates, or official G010 protocol.
- Every model probe records model identity, artifact version, case IDs, prompt envelope, output, cost or zero-cost status, and limitations.

## Propagation rules

- A local wording problem is revised in the active goal.
- A finding that changes a completed decision reopens the owning goal with evidence; it is not silently patched downstream.
- A finding that changes an interface amends the downstream goal before that goal becomes `In progress`.
- A finding that affects the frozen evaluation design is routed to G002/G010 and cannot be changed after observing official candidate outputs.
- A finding that affects only interpretation is recorded as an observation and does not block closure.

## Stage focus

| Goal | Iteration question | Preferred probe | Likely propagation |
|---|---|---|---|
| G001 | Is the audit classification and pattern match reproducible? | Record-level review and optional open-model classification on development records | Reopen G001 or amend G003 |
| G002 | Does the suite, rubric, and budget measure the intended behavior? | Mock outputs, schema checks, and smoke configuration | Reopen G002 before official baseline |
| G003 | Do the seven principles preserve inquiry without false balance or closure? | Open-model development cases and counterexample review | Reopen G003 or amend G004–G008 |
| G004 | Do hierarchy and agency rules resolve conflicts without paternalism or unsafe under-intervention? | H-01–H-18 plus development cases and optional open-model probes | Reopen G004 or amend G005–G010 |
| G005 | Do honesty and inquiry clauses improve candor, updating, and disciplined speculation? | I-01–I-10 and development cases | Revise G005 or amend G006–G010 |
| G006 | Do authority and incentive clauses expose provenance without collapsing legitimate coordination? | A-01–A-12 and development cases | Revise G006 or amend G007–G010 |
| G007 | Do harm and capacity rules distinguish self-regarding risk from third-party harm? | G007 development cases and adversarial safety probes | Revise G007 or amend G008–G010 |
| G008 | Do dissent, review, and amendment rules remain corrigible rather than self-sealing? | G008 development cases and review simulations | Revise G008 or amend G009–G010 |
| G009 | Does the integrated candidate preserve every upstream contract? | Base-versus-draft development smoke, no held-out cases | Reopen the owning drafting goal or revise G009 |
| G010 | Does the final candidate improve behavior under the frozen protocol? | Official paired base/candidate comparison | Resolve regressions or do not publish |

## Iteration record

Each loop records:

- `iteration_id` and `goal_id`;
- hypothesis register: mechanism, predicted gains, predicted regressions, controls, competing explanations, and falsifier;
- changed artifact paths;
- artifact commit or content hash;
- probe type and model identity, if any;
- case IDs and split (`development`, `public`, or `heldout`);
- paired transitions and observed improvement, regression, uncertainty, or limitation;
- causal-attribution status for each material finding and the next discriminating test;
- disposition and rationale;
- downstream goals or acceptance criteria affected;
- checkpoint date and reviewer.
