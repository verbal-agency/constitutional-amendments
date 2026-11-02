# G007-S1 — Hazard and proportionality schema

Status: In progress
Parent: G007 — Inquiry and Harm
Depends on: G006 Complete
Consumer: G007 clause drafting and offline decision fixtures

## Objective

Make the first G007 decision record explicit enough to distinguish inquiry,
disclosure, acquisition, and execution; self-regarding choice from
nonconsensual harm; and a genuine hazard from unsupported paternalism.

## Outcome link

- **Project outcomes:** O1 explicit epistemology, O2 traceability, O3 protected
  inquiry, O4 non-self-sealing governance, O6 adversarial resilience, and O7
  pattern-aware diagnosis.
- **Canonical scenarios:** SC-003, SC-004, SC-005, SC-006, SC-007, and SC-009.
- **Downstream unlock:** section-ready HA-01–HA-07 clause drafting and the
  later G008 review/amendment handoff.

## Hypothesis

If every intervention records the affected plane, affected party, consent,
capacity, evidence, uncertainty, hazard strength, operational uplift,
reversibility, least-restrictive option, duration, and review trigger, then the
process will preserve legitimate inquiry while restricting only supported
hazardous capability.

Disconfirming evidence is an illegal state that the schema accepts, an
unresolvable distinction between self-regarding and nonconsensual harm, or a
fixture that requires an unowned authority or measurement decision.

## In scope

- `framework/G007-harm-schema.yaml`;
- `fixtures/G007-harm-cases.md` with H-01–H-12;
- deterministic offline validation of schema and fixture coverage;
- recording G006 and G008 boundaries before clause drafting.
- application decision: use the schema for prompt-first clause drafting and
  offline evaluation; defer runtime enforcement to backlog item B001.

## Out of scope

- HA-01–HA-07 constitutional prose;
- source or integrated-candidate edits;
- model, provider, paid, network, held-out, or frozen-evaluation work;
- independent reviewer or identity/amendment mechanics owned by G008.

## Closure criteria

1. The schema defines the required fields, allowed values, decision rules, and
   illegal states without an ambiguous restriction path.
2. H-01–H-12 are unique, structurally complete, and cover all nine harm
   classes and six case shapes.
3. Every fixture links to an HA clause, preserves a safety/privacy purpose,
   states expected and unacceptable behavior, and names an observable proof.
4. G006 authority/provenance inputs and G008 review/identity handoff are
   recorded without assigning their decisions to G007.
5. The validation command is deterministic, offline, and records remaining
   unknowns before clause drafting.

## Verification

```text
$ python3 evals/scripts/validate_g007_harm_fixtures.py
PASS fixtures=12 classes=9 case_shapes=6 schema=g007-harm-decision-v1 no_paid_call=true
```

The full criterion report is `framework/G007-verification.md`.
