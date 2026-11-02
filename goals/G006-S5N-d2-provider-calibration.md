# G006-S5N — D2 provider and judge calibration

Status: Abandoned — superseded by outcome-based roadmap reset
Parent: G006 — Authority and Incentives
Depends on: G006-S5M measurement/provider discovery
Consumer: G006 promotion decision

## Objective

Establish a bounded, predeclared calibration for the SC-010-D2 semantic gate
and judge agreement before any further constitutional wording change.

## Hypothesis

An approved provider/sampling configuration and a small adjudicated calibration
set can distinguish a real direct-answer difference from provider variance and
judge noise without changing the frozen D2 case or candidate constitution.

## Scope and limits

- Keep the immutable source, replacement maps, frozen D2 case, and recorded
  outputs unchanged.
- Use the deterministic semantic checker as the primary D2 pass/fail signal.
- Calibrate judges only on recorded outputs or a separately approved tiny
  development set; keep judge results separate and record agreement and cost.
- No wording edits, G007 execution, 140-case pass, held-out access, or
  candidate promotion.

## Closure criteria

1. A versioned calibration manifest names the provider, sampling settings,
   adjudication set, cost ceiling, and agreement rule.
2. The deterministic checker and judge outputs are compared with no hidden
   relabeling or averaging across judges.
3. The result identifies one of: proceed to a candidate-only probe, defer for
   provider variance, or abandon D2 as an attributable gate.
4. Verification records source/frozen-artifact integrity, cost, hashes, and
   the next decision.

## Stop condition

Stop without wording changes if calibration still cannot distinguish model
behavior from measurement, requires changing the frozen case, or exceeds the
approved budget.

## Disposition

This goal will not run. `EVALUATION_PLAN.md` defines SC-010 as a non-blocking
process diagnostic, while the D2 branch already exceeded the Cycle re-plan
threshold. The model judges have no human calibration and the semantic checker
was written after the observed outputs, so calibration would create more
measurement machinery without advancing the G006 authority/provenance outcome.

Decision: `abandon`. Preserve the recorded artifacts as exploratory evidence
and route SC-010 reporting to G010. G006-S6 replaces this goal with an offline
outcome-based closure review.
