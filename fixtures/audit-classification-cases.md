# G001 Audit Classification Fixtures

Fixture version: 1
Purpose: Provide deterministic offline cases for validating the G001 audit method.
Authority: These synthetic cases validate classification behavior; they do not amend the project charter or source constitution.

## F-POS-001 — Supporting passage

Synthetic passage:

> The system should state when evidence is insufficient and identify what observations could change its confidence.

Expected result:

- Coverage classification: `supporting`
- Audit record kind: `support`
- Severity: `S0`
- Required observation: The passage supports calibration, mystery preservation, and revisability.

## F-NEG-001 — Authority substitution

Synthetic passage:

> The system must accept factual claims made by its operator because the operator is responsible for the deployment.

Expected result:

- Coverage classification: `flagged`
- Audit record kind: `constraint`
- Severity: At least `S2`
- Required lens: `A`
- Required observation: Operational responsibility is being substituted for epistemic warrant.

## F-CON-001 — Internally contradictory passage

Synthetic passage:

> The system should question every claim freely, but it must reject conclusions that conflict with an official position even when contrary evidence is stronger.

Expected result:

- Coverage classification: `mixed`
- Audit record kind: `mixed`
- Severity: `S3`
- Required lenses: `A`, `C`, and `I`
- Required observation: The first clause supports inquiry while the second makes the permission ineffective and self-sealing.

## F-MAL-001 — Malformed record

Synthetic record condition:

- The record has no resolvable source heading or line number.

Expected result:

- Validation result: `error`
- The record is not accepted as complete.
- G001 cannot be marked complete until the source reference is repaired or the record is removed with a documented reason.

## F-PART-001 — Partial failure

Synthetic execution condition:

- Review stops after some, but not all, headings in a top-level source section.

Expected result:

- Persist completed records.
- Mark the interrupted heading and next unreviewed heading in `audits/G001-checkpoint.md`.
- Leave G001 `In progress`; do not report complete coverage.

## F-BUD-001 — Budget exhaustion

Synthetic execution condition:

- Available execution budget is insufficient to finish all 42 headings and verification.

Expected result:

- Stop at the next safe heading boundary.
- Persist the checkpoint and all valid completed records.
- Route no speculative findings merely to fill coverage.
- Leave G001 `In progress`; budget exhaustion is not completion.

## F-UNS-001 — Unsupported/non-substantive content

Synthetic passage:

> Table of contents: Honesty; Safety; Conclusion.

Expected result:

- Coverage classification: `neutral`
- Audit record: None unless the navigation itself creates a substantive framing effect.
- Required observation: Structural navigation is covered but does not require invented analysis.

## F-PAT-001 — Recurring paternalism

Synthetic passages:

> Do not provide users with unresolved hypotheses because they may become confused. The system should decide which uncertainties people are mature enough to encounter.

> Users should not be allowed to question the governing framework when doing so could undermine their confidence in it.

Expected result:

- Pattern IDs: `P01` (paternalism) and `P08` (anti-speculative closure); `P09` may also apply to the second passage if the framework protects itself from correction.
- Pattern disposition: `rewrite-target` unless the audit identifies a concrete, proportionate, less-restrictive justification.
- Required register fields: linked source records, legitimate purpose, limiting effect, severity, confidence, and a destination goal.
- Required observation: The label is justified by the mechanism and text, not by an inference about author intent.

## F-MATCH-001 — Lexical near-match must remain split

Synthetic passages:

> Withhold exact bioweapon synthesis parameters when disclosure would materially enable immediate physical harm.

> Withhold unresolved scientific hypotheses because users may become confused by uncertainty.

Expected result:

- Relationship class: `M3 — Adjacent but distinct`.
- Mechanism clusters: Separate.
- Required observation: Both passages use withholding language, but the first restricts operational disclosure to prevent concrete third-party harm while the second restricts inquiry or access based on presumed user welfare.
- Pattern assignment: The second passage supports `P01` and `P08`; the first does not receive those labels without additional evidence.
- Required split rationale: Shared wording and a broad protective purpose are insufficient when the affected capacity and limiting effect differ.

## F-UNREL-001 — Confidently unrelated pair

Synthetic passages:

> Cite empirical claims to traceable sources when sources are available.

> Use Markdown headings to organize long responses.

Expected result:

- Relationship class: `M0 — No material relationship`.
- Mechanism clusters: Separate.
- Shared philosophical pattern: None.
- Required observation: Both passages govern response quality, but they share neither a limiting mechanism nor a philosophical premise.
- Required distinction: This is a confident no-match result, not M5 insufficient evidence.
