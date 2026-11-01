# G006-S4 — Promotion and downstream handoff review

Status: Proposed
Parent: G006 — Authority and Incentives
Depends on: G006-S3F complete
Consumer: G006 promotion decision and G007 handoff

## Objective

Decide whether the current exact-replacement candidate is ready for the next
downstream workstream, using the completed S3/S3R/S3D/S3E/S3F evidence and the
predeclared focused stability criteria. If it is not ready, route one bounded
repair or measurement discovery instead of starting G007 or the 140-case pass.

## Hypothesis

The candidate is not yet promotion-ready because SC-010-D2 remains a
substantive regression even though the MASK measurement gap is now understood.
The v2 replay should prevent that measurement issue from hiding the regression,
not erase it. Disconfirming evidence is a focused comparison that restores D2,
preserves MASK, and introduces no new critical failure under the existing
stability gate.

## Scope and limits

- Review existing S3, S3R, S3D, S3E, and S3F evidence only.
- Do not edit the immutable source, frozen rubric, or replacement map.
- Do not start G007, the 140-case pass, or another wording iteration unless
  the focused gate explicitly unlocks it.
- Preserve the distinction between substantive D2 behavior and MASK scoring.

## Unlock

A complete promotion decision either authorizes the next bounded G006/G007
handoff or routes a named repair/discovery goal with a falsifier.

## Stop condition

Stop and route a new bounded goal if the evidence cannot decide promotion,
if a required acceptance criterion is still unmeasured, or if the decision
would require changing the frozen comparison contract.
