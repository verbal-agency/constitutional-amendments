# G007-S3 — Adversarial clause review

Status: Complete
Parent: G007 — Inquiry and Harm
Depends on: G007-S2 Complete
Consumer: G007 offline probe packet and later G009 integration

## Objective

Check whether HA-01–HA-07 state the expected boundaries for H-01–H-12 and
explicit over-refusal, under-refusal, authority-laundering, privacy, and
emergency cases before any model-facing probe.

## Hypothesis

If the clause text is reviewed against every fixture and boundary case, then
the process will find prose/schema gaps before model outputs make them harder to
attribute. A discovered gap should be repaired in the current clause set or
routed to the correct downstream owner.

Disconfirming evidence is a fixture with no direct clause path, a clause that
permits a prohibited boundary, an unowned governance decision, or a review
result that cannot distinguish a current-clause defect from a downstream issue.

## Closure criteria

1. H-01 through H-12 each have a named clause path, preserved purpose,
   prohibited behavior, and review result.
2. Six explicit boundary probes cover inquiry, self-regarding agency, consent,
   privacy, authority laundering, and emergency expiry.
3. All findings have exactly one destination, and any active-goal defect is
   repaired and rechecked.
4. Offline validators pass; the source and frozen evaluation artifacts remain
   unchanged; no model, provider, network, paid, held-out, or remote action
   occurs.

## Verification

```text
$ python3 evals/scripts/validate_g007_adversarial_review.py
PASS fixtures=12 boundary_probes=6 revision_count=1 no_model_call=true

$ python3 evals/scripts/validate_g007_module.py
PASS clauses=7 max_clause_words=83 source_sha256=251440a71a9068dd43bfaab2b8694d6e2a4f519c403f1b9a70785f830d05f327 prompt_first=true no_model_call=true

$ python3 evals/scripts/validate_g007_harm_fixtures.py
PASS fixtures=12 classes=9 case_shapes=6 schema=g007-harm-decision-v1 no_paid_call=true
```

The review found and repaired the H-01 discriminating-test gap in HA-04. It
does not establish model behavior. The next bounded slice is a small tracked
development probe packet offline; it does not execute a model or the official
G010 comparison.
