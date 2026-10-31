# G006-S3F — Replay the MASK v2 contract on recorded outputs

Status: Proposed
Parent: G006 — Authority and Incentives
Depends on: G006-S3E complete
Consumer: G006 promotion decision

## Objective

Apply the MASK v2 development scorer to a small, predeclared set of already
recorded base, S3, and S3R outputs, preserving the old labels and reporting
exact versus ambiguous historical bridges.

## Hypothesis

The v2 predicates will classify the S3R limitation as either
`truthful_limited` only when the case visibly authorizes withholding, or
`failure/evasive` when the known case provides no such authority; it will not
collapse direct truth and bounded limitation into one label. Disconfirming
evidence is judge disagreement that persists after the case metadata is shown,
or any need to infer hidden authorization.

## Scope and limits

- Use existing outputs only; do not generate a new candidate.
- Replay one named MASK case per available arm, with the same v2 judge
  configuration and a position-preserving record of every result.
- Proposed ceiling: 8 judge calls total, `$0.10` hard cost ceiling, one retry
  per failed judge response, subject to an explicit approval record.
- Do not edit the frozen v1 rubric, historical score files, source constitution,
  replacement map, or held-out material.

## Unlock

A passing replay supplies measurement evidence for G006-S4's promotion decision.
An ambiguous or inconsistent replay reopens this contract instead of triggering
another wording change.

## Stop condition

Stop if a judge must infer authorization not present in the case, if v2 labels
cannot be parsed deterministically, or if the cost ceiling would be exceeded.
