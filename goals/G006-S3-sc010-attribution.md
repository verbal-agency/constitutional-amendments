# G006-S3 — Attribute the SC-010-D2 regression

Status: Complete — revise-one-named-replacement-entry
Parent: G006 — Authority and Incentives
Dependencies: G006-S1 Complete; G006-S2 Complete
Next subgoal: G006-S3R — MAP-002 repair

Completion evidence: `framework/G006-S3-analysis.md`, `evals/runs/g006-s3-full/manifest.json`, and `evals/runs/g006-s3-ablation/manifest.json`.

## Objective

Determine whether the SC-010-D2 regression comes from the MAP-002 MASK wording change, the evaluation context envelope, or unresolved provider variance. Produce one promotion decision for the G006 candidate; do not broaden the work into a full collateral or 140-case pass.

## Consumer and decision

- **Primary consumer:** the G006 promotion decision.
- **Owner:** G006.
- **Decision:** promote the current candidate to S4, revise the relevant replacement entry, or route the attribution as unresolved and stop.
- **Project link:** advances the authority/provenance path for `SC-010` while preserving the project’s truthfulness and agency criteria.
- **Downstream unlock:** S4 may run the collateral-damage gate and prepare G007 only after this decision is supported.

## Hypothesis

The direct-known-fact wording in MAP-002 is responsible for the MASK improvement but is not the sole cause of SC-010-D2 failure. A paired same-packet ablation that changes only MAP-002 wording should distinguish that effect from the shared evaluation envelope.

Disconfirming evidence: the MAP-002 ablation leaves D2 unchanged while the envelope variant changes it, or both variants produce the same failure with no meaningful judge disagreement.

## Current slice

Run one paired, candidate-only ablation on the same four cases: `mask:provided_facts:67ab8fa8461eb193ef95b421`, `CUS-SC010-D1`, `CUS-SC010-D2`, and `CUS-SC010-D3`. Reuse historical base outputs and scores. The primary comparison is:

- **Full candidate:** `evals/maps/g006-replacement-v3.json`.
- **MAP-002 ablation:** a versioned map identical to v3 except that `G006-MAP-002` uses the pre-direct-answer replacement wording from `evals/maps/g006-replacement-v1.json`. MAP-001 and MAP-003 remain unchanged.

Do not change the source, case packet, provider, decoding settings, judge policy, or envelope in this slice. Treat an envelope ablation as a later fallback only if the MAP-002 result is inconclusive.

## Closure criteria

1. Both candidate variants render from the pinned source with no metadata leakage; each records source hash, map hash, candidate hash, and renderer version.
2. The paired run stays within the preflight budget, uses no held-out material, reuses the historical base, and records separate primary and secondary judge results.
3. The report records case-level transitions and a binary attribution decision: `MAP-002`, `envelope/provider`, or `unresolved`.
4. The report records a disposition: promote to S4, revise one named replacement entry, or stop and route a new discovery slice. It must not authorize the 140-case pass by itself.

## Scope

In scope: one MAP-002 wording ablation, four cases, historical-base reuse, paired judging, cost accounting, and attribution documentation.

Out of scope: envelope changes, new datasets, held-out material, full collateral evaluation, 140-case measurement, permanent source edits, G007 execution, and fine-tuning.

## Execution contract

- **Writable surface:** `evals/maps/`, `evals/manifests/`, `evals/runs/`, `framework/`, and this goal file. The immutable source and frozen dataset manifests are read-only.
- **Required artifacts:** one ablation map, one manifest, candidate assembly metadata for both variants, raw outputs, separate judge JSONL, and `framework/G006-S3-analysis.md`.
- **Behavior matrix:** MASK must remain `honest`; D1 and D3 must not gain a new critical failure; D2 is the attribution target. A judge disagreement is recorded, not averaged away.
- **Authority boundary:** paid model calls require a passing preflight and the existing user-approved ceiling; no credentials are written to artifacts; no remote mutation occurs.
- **Stop conditions:** stop before calls if hashes drift or the preflight exceeds the approved ceiling; stop after this paired run if attribution remains unresolved; do not add a second ablation without amending this subgoal.
- **Verification:** map/registry validation, candidate-render smoke checks, provenance-hash check, preflight output, paired-transition report, and `git diff --check`.

## Findings routing

- A MAP-002-attributed failure routes to a single bounded G006 repair subgoal.
- An envelope/provider-attributed failure routes to a G006 evaluation-interface discovery slice.
- An unresolved result routes to a bounded discovery decision; it does not keep S3 open indefinitely.
- Stable results unlock G006-S4; they do not directly unlock G007.
