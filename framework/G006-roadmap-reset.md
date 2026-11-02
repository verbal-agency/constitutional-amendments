# G006 roadmap reset — stop the D2 diagnostic loop

Status: Complete — pivot from D2 calibration to outcome-based G006 closure
Decision date: 2026-11-01
Decision owner: Project owner

## Outcome card

- **Project aim:** produce a traceable constitution that improves truth-seeking
  behavior without weakening factuality, safety, or legitimate coordination.
- **Why this reset now:** six consecutive child goals treated one SC-010
  development case as a blocking regression without first establishing that the
  case, graders, or post-hoc checker were valid promotion gates.
- **What this reset changes:** it stops the D2 branch, restores the evaluation
  plan's distinction between behavioral gates and process diagnostics, and
  makes the next goal decide G006 from its actual outcomes using existing
  evidence.
- **What success means:** the next goal either closes G006, identifies one
  evidence-backed G006 behavioral blocker, or defers with a named missing input.
  Creating another D2 child goal is failure.
- **Decision:** pivot. Abandon G006-S5N and prepare one offline G006 closure
  review before any more model calls or wording changes.

## What failed

### 1. A non-blocking diagnostic became a release gate

`EVALUATION_PLAN.md` says SC-010 is a separately reported process diagnostic
and cannot make the SC-001–SC-009 behavioral comparison pass or fail. G006-S4
nevertheless made SC-010-D2 a blocking promotion criterion. That contract
error, not the model output, created the endless branch.

### 2. Goal completion rewarded continuation rather than progress

S3R, S3D, S4, S5, S5R, and S5M could all close by routing another child goal.
The branch therefore accumulated completed goals without changing the
constitution, validating the evaluator, closing G006, or advancing G007.

### 3. The branch exceeded the re-plan threshold

The Cycle skill requires re-planning after three bounded iterations without
closure. The D2 branch continued through ablation, repair, interface discovery,
promotion review, factorial discovery, replication, and measurement discovery.
The parent contract should have been reopened after the failed repair and
inconclusive attribution, not extended again.

### 4. The evaluators were never validated for the disputed distinction

The two model judges exactly agreed on only 3 of 11 scorable S5R outputs, and
one primary call failed. No human-labeled calibration set established which
judge, if either, was accurate. Their disagreement is evidence that the result
is unresolved, not a reason to create a judge-calibration goal for a
non-blocking diagnostic.

### 5. The semantic checker was post-hoc and narrow

The checker recognizes a few expected propositions and failure phrases. It was
written after the outputs were observed and has four synthetic unit tests, but
no independent human labels, paraphrase coverage, or false-positive/negative
estimate. It is useful for inspecting recorded outputs; it is not an official
semantic gate and cannot validate the graders.

### 6. The causal hypotheses were incomplete

Individual goals named local explanations, but the branch never predeclared a
complete competing set covering prompt ambiguity, constitution-induced task
over-application, context salience, candidate length/position, sampling,
provider drift, judge error, and rubric mismatch. As a result, each probe
eliminated at most one explanation and exposed another reason to continue.

## What the evidence actually supports

**Observed:** The D2 packet was present in every inspected model message.
Recorded answers were inconsistent, the no-replacement control also failed in
replication, the judges disagreed materially, and the post-hoc checker labeled
only 1 of 16 outputs as a direct answer.

**Interpreted:** Packet loss is unlikely. No constitutional factor, provider
effect, or grader is validated well enough to explain the response pattern.
Confidence is high that the current evidence cannot support a D2 causal claim.

**Decided:** Preserve the artifacts as exploratory evidence, but stop using D2
as a G006 promotion blocker. Do not calibrate judges or revise constitution
wording for this case inside G006. G010 may report SC-010 separately under its
predeclared human/judge review.

**Unknown:** Whether the D2 prompt itself is a good audit task and whether a
different model or evaluator would handle it consistently. Those questions do
not block G006's authority-and-incentives outcome.

## Anti-churn rules added to the roadmap

1. A diagnostic may block a goal only when the project contract declared it a
   gate before candidate outputs were observed.
2. A child goal cannot close solely by creating another child. It must change
   an accepted artifact, make the owning decision, or retire a material risk.
3. Two failed repair attempts or three consecutive slices on the same failure
   trigger a parent-level re-plan. Further child goals require a new outcome
   justification and explicit user authorization.
4. A post-hoc checker remains diagnostic until validated against independent,
   predeclared human labels and representative paraphrases.
5. A model judge cannot decide promotion until its role, calibration evidence,
   disagreement handling, and threshold are predeclared. Disagreement is not
   averaged away.
6. Investigation ceilings apply to the whole failure branch, not separately to
   each inexpensive child goal.

## Roadmap decision

**Decision: pivot.** Mark G006-S5N abandoned. The next and only eligible goal
is G006-S6, an offline outcome-based closure review. It must use existing
evidence to choose exactly one result: `proceed` to G007, `pivot` to one named
G006 behavioral repair, or `defer` because one required input is missing. It
may not create another D2 measurement or calibration child.
