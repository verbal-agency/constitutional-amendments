# G007-S2 — Clause drafting

Status: Complete
Parent: G007 — Inquiry and Harm
Depends on: G007-S1 Complete
Consumer: G007 adversarial clause review and later G009 integration

## Objective

Translate the validated harm and proportionality schema into seven
section-ready constitutional clauses without claiming model behavior or
silently placing development metadata in a model prompt.

## Outcome link

- **Project outcomes:** O1 explicit epistemology, O2 traceability, O3 protected
  inquiry, O4 non-self-sealing governance, and O6 adversarial resilience.
- **Canonical scenarios:** SC-003, SC-004, SC-005, SC-006, SC-007, and SC-009.
- **Downstream unlock:** adversarial review of HA-01–HA-07 and the G008/G009
  handoffs.

## Hypothesis

If the clauses distinguish the hazardous plane, affected party, evidence,
capacity, operational uplift, proportionality, and review without closing the
topic, then the offline contract will preserve inquiry and agency while keeping
narrow controls available for supported nonconsensual harm.

Disconfirming evidence is a missing clause function or traceability field, a
clause over 120 words, a source-hash mismatch, or a clause that suppresses a
fixture's preserved inquiry without a supported operational hazard.

## Closure criteria

1. Exactly HA-01 through HA-07 exist once and each is independently readable.
2. Each clause is no more than 120 words and has complete schema, source,
   audit, fixture, scenario, and downstream metadata.
3. The change register maps each direct G007 audit record to one primary clause
   destination and records a falsifiable attribution plan.
4. Offline validators pass; the source hash and frozen-boundary checks remain
   intact; no model, provider, network, paid, held-out, or remote action occurs.

## Verification

```text
$ python3 evals/scripts/validate_g007_module.py
PASS clauses=7 max_clause_words=73 source_sha256=251440a71a9068dd43bfaab2b8694d6e2a4f519c403f1b9a70785f830d05f327 prompt_first=true no_model_call=true

$ python3 evals/scripts/validate_g007_harm_fixtures.py
PASS fixtures=12 classes=9 case_shapes=6 schema=g007-harm-decision-v1 no_paid_call=true
```

The slice does not establish behavioral improvement. The next bounded slice is
an adversarial review of clause/fixture boundaries, followed only if it passes
by a tracked development probe.
