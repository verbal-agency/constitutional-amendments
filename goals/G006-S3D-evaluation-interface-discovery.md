# G006-S3D — Evaluation-interface discovery

Status: Discovery
Parent: G006 — Authority and Incentives
Depends on: G006-S3R stop disposition
Consumer: G006 promotion decision
Decision owner: G006 owner

## Discovery question

Can the current evaluation envelope, case construction, or rubric distinguish a principled truthful limitation from evasive non-answering and from treating supplied material as absent, or is the observed failure primarily a constitution-level behavior?

## Observed facts

- Reverting only MAP-002 restored SC-010-D2 under both judges in S3.
- A shorter, context-neutral MAP-002 repair failed D2 under both judges and changed MASK from `honest` to `evasive` under both in S3R.
- D1 stayed improved and D3 stayed stable in S3R.
- The same historical base outputs and frozen cases were used; no envelope change was tested.
- The S3R D2 answer explicitly treated supplied formatting rules as absent; the MASK answer disclosed uncertainty but was labeled evasive.

## Current assumptions

- Historical base outputs remain a valid control for the next diagnostic.
- The four-case slice is sufficient to identify an interface ambiguity, but not to claim general model behavior.
- The source and frozen case artifacts are stable and must remain read-only.

## Unknowns

- Whether the D2 packet's formatting and prompt delimiters make supplied material easy to lose under any candidate with limitation language.
- Whether the MASK rubric treats useful contingency advice as evasion even when the answer states uncertainty accurately.
- Whether judge disagreement or prompt serialization contributes materially to either failure.
- Whether a minimal envelope or rubric clarification would resolve both failures without changing the principle.

## Cheapest next probe

Build an offline, non-paid interface matrix using the existing four cases and recorded outputs. Compare the exact serialized messages, supplied-evidence delimiters, candidate response labels, and rubric predicates; then define one minimal paired probe (envelope-only or rubric-only) if the matrix identifies a specific ambiguity. No constitution wording change or broad run is authorized until the discovery decision.

## Evidence and confidence

Confidence is high that S3R failed its behavioral gate and moderate that the remaining ambiguity is an interaction between MAP-002 limitation language and the evaluation interface. Confidence is low that either a constitution-only or rubric-only change will solve both cases before the matrix is built.

## Decision options

- `proceed`: a named interface ambiguity is isolated and a minimal diagnostic can test it.
- `pivot`: the rubric or case construction is measuring a different capability than the intended principle; amend the measurement contract.
- `defer`: evidence is insufficient and the next probe is not worth its bounded cost.
- `abandon`: the G006 comparison cannot validly attribute this behavior within the available evaluation design.

## Scope and stop conditions

In scope: offline serialization/rubric inspection, a compact interface matrix, and one decision note. Out of scope: paid model calls, new wording, envelope mutation, held-out data, 140-case evaluation, S4, or G007 execution. Stop when the matrix yields one decision with evidence; reopen implementation only through a new bounded goal.

## Deliverables and acceptance criteria

1. A discovery note records the question, facts, assumptions, unknowns, evidence, cheapest probe, owner, impact, and one decision.
2. The interface matrix names the relevant fields and shows how each could produce D2 missing-context behavior or MASK evasion labeling.
3. No paid calls, source edits, frozen-artifact edits, or candidate promotion occur.
4. The decision routes exactly one next action: proceed, pivot, defer, or abandon.

## Downstream unlock

Only a `proceed` or `pivot` decision with a bounded contract may reopen G006 implementation or amend the evaluation contract. G006-S4 remains blocked until then.
