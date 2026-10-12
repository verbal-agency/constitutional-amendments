# Iteration Protocol

Status: Canonical project workflow
Applies to: G001–G010

## Purpose

The roadmap is iterative, not purely linear. Each goal may produce evidence that changes its own conclusion, requires a revision, or changes a downstream goal's contract. Analysis, drafting, and model probing are separate activities, but they inform one another before a goal closes.

## Loop

Every active goal runs this loop as many times as needed:

1. **State the hypothesis.** Identify the claim, rule, clause, taxonomy, or evaluation choice being tested.
2. **Make the smallest change.** Change one bounded artifact or decision at a time.
3. **Probe it.** Use deterministic checks, offline fixtures, development cases, and—when useful—a local or open model. Use only tracked development/public cases before G010.
4. **Compare the result.** Compare the new result with the prior artifact, the source purpose it must preserve, and the relevant failure modes.
5. **Review the evidence.** Record what improved, regressed, remained uncertain, or was not actually tested.
6. **Route the finding.** Choose `accept`, `revise-current-goal`, `reopen-upstream`, `amend-downstream`, `block`, or `observe`.
7. **Checkpoint.** Preserve the artifact hash, probe inputs, outputs or summaries, decision, and downstream impact before the next loop.

A goal does not close merely because its prose is complete. It closes when its loop record has no unresolved material finding and its acceptance evidence remains valid.

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
- hypothesis and changed artifact paths;
- artifact commit or content hash;
- probe type and model identity, if any;
- case IDs and split (`development`, `public`, or `heldout`);
- observed improvement, regression, uncertainty, or limitation;
- disposition and rationale;
- downstream goals or acceptance criteria affected;
- checkpoint date and reviewer.

