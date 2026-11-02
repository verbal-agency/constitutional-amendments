# G007 Verification — First schema and fixture slice

Goal: G007 — Inquiry and Harm
Slice: G007-S1 — Hazard and proportionality schema
Verification date: 2026-11-01
Result: Complete — proceed to G007 clause-drafting slice
Source SHA-256: `251440a71a9068dd43bfaab2b8694d6e2a4f519c403f1b9a70785f830d05f327`

## Outcome card

This slice makes the harm decision record explicit before constitutional prose
is drafted. It turns “be proportionate” into fields and illegal-state rules:
which plane is affected, who bears the risk, what evidence supports it, what
operational capability would be added, what safer alternative exists, and when
the decision expires. Success means the schema and 12 fixtures can be checked
offline without inventing a hazard or authority decision. Failure would be an
ambiguous restriction path, missing evidence, missing affected party, or a
fixture that cannot show its expected boundary.

## Development narrative

**Prior limitation:** G006 and G005 routed concrete hazard thresholds,
capacity, and proportionality to G007, but those interfaces were still prose
and could not reject an incomplete or overbroad intervention deterministically.

**Hypothesis:** Explicit decision fields and illegal states will preserve
inquiry and competent self-regarding choice while allowing narrow controls for
supported third-party hazards.

**Capability built:** `framework/G007-harm-schema.yaml`, 12 human-readable
fixtures in `fixtures/G007-harm-cases.md`, and an offline validator that checks
schema enums, unique IDs, field completeness, nine class families, and six case
shapes.

**Observed:** The validator passes `H-01` through `H-12`, all required classes,
and all required case shapes. No source, frozen evaluation, held-out, model,
provider, network, or paid artifact was touched.

**Interpretation:** The contract is structurally ready for clause drafting.
Confidence is high for coverage and schema integrity; it is not evidence that
any model will apply the rules correctly. Numerical thresholds and reviewer
mechanics remain deliberately unresolved.

**Next decision:** proceed to the next bounded G007 slice: draft HA-01–HA-07
against this schema and preserve the G006/G008 ownership boundaries.

## Application decision

G007 will use the schema in **prompt-first mode**. The next clause slice will
translate the schema's decisions into HA-01–HA-07 natural-language clauses.
Later model comparisons will send the rendered constitutional text with the
user query; they will not silently add this YAML or its development metadata to
the prompt. A model-facing structured `HarmDecision` validator is not part of
G007. It is recorded once as backlog item B001 for a possible future router
project.

## Criterion evidence

| G007-S1 criterion | Result | Evidence |
|---|---|---|
| Schema has no ambiguous restriction path | Pass | `framework/G007-harm-schema.yaml` defines required fields, enums, seven decision rules, and seven illegal states. Restrictions require an affected party, protected interest, evidence, uncertainty, proportionality fields, and review/expiry where temporary. |
| H-01–H-12 cover required cases | Pass | `fixtures/G007-harm-cases.md` contains exactly 12 unique IDs, all nine fixture classes, and all six case shapes: positive, negative, contradictory, malformed, partial, and stopped. |
| Every fixture has proof and preservation fields | Pass | The validator requires condition, expected behavior, unacceptable behavior, required HA links, preserved purpose, acceptance proof, and PASS result for every fixture. |
| G006 and G008 boundaries are recorded | Pass | G006 supplies authority/provenance inputs; G007 owns hazard and proportionality; G008 receives review, identity, dissent, and appeal mechanics. The boundary is recorded in the schema response contract and this report. |
| Verification is deterministic and remaining unknowns are recorded | Pass | `python3 evals/scripts/validate_g007_harm_fixtures.py` passes offline; unknowns are listed below before clause drafting. |

## Contract checks

```text
$ python3 evals/scripts/validate_g007_harm_fixtures.py
PASS fixtures=12 classes=9 case_shapes=6 schema=g007-harm-decision-v1 no_paid_call=true

$ git diff --check
PASS
```

## Schema decisions

- A restriction must name the affected plane instead of treating a topic as
  hazardous as a whole.
- Self-regarding capacity is recorded separately from consent and from
  third-party standing; competent choice is presumptive.
- Severity, likelihood, operational uplift, reversibility, and uncertainty are
  separate fields rather than one composite “risk” score.
- `temporary_control` and emergency responses require expiry and review.
- Missing or contradictory fields cause quarantine, not an inferred refusal.
- Safe analysis and educational discussion remain available when only an
  operational component is hazardous.

## Observed, interpreted, decided, unknown

### Observed

- The YAML schema and Markdown fixture set are present and parseable.
- H-01–H-12 have complete required fields and unique stable IDs.
- Coverage includes inquiry, self-regarding, consensual, nonconsensual,
  operational, privacy, malformed, emergency, and unsupported cases.
- Coverage also includes positive, negative, contradictory, malformed, partial,
  and stopped paths.

### Interpreted

- The first G007 implementation boundary is explicit enough to draft clauses
  without silently deciding reviewer identity or constitutional integration.
- The fixture set tests both under-intervention and over-intervention: it can
  reject unsupported suppression as well as require a narrow refusal when an
  identifiable third party faces concrete operational harm.

### Decided

- Mark G007-S1 complete and keep G007 in progress.
- Proceed to HA-01–HA-07 clause drafting in the next bounded slice.
- Do not run model calls, paid evaluation, or source/candidate edits in this
  slice.

### Unknown

- Numeric or qualitative thresholds for severity, likelihood, and operational
  uplift still need clause-level justification and counterexamples.
- The evidence standard for decision-specific capacity needs applied cases.
- G008 must define independent review, appeal, identity, dissent, and amendment
  mechanics; G007 must not absorb those decisions.
- The schema has not been tested against model outputs; that belongs to later
  development cases and ultimately G010's controlled comparison.
- Whether a future product needs a structured runtime router remains open under
  B001 and does not block G007.

## Routing

| Finding | Class | Destination | Action |
|---|---|---|---|
| Decision fields and illegal states are defined | Active-goal requirement | G007-S1 | Close the first slice and use the schema for clause drafting. |
| Threshold calibration and capacity evidence remain open | Future-goal input | G007 next slice | Draft counterexamples and clause-level thresholds; do not add numbers without evidence. |
| Independent review, identity, dissent, and appeal remain open | Future-goal input | G008 | Preserve the handoff; do not assign reviewer authority in G007. |
| Integrated candidate and model measurement remain open | Future-goal input | G009/G010 | Keep this slice offline and do not claim behavioral improvement. |
| Runtime structured harm-decision enforcement is optional | Backlog item | B001 / future router project | Do not add a validator to G007 unless a router consumer is explicitly selected. |

## Decision

**`proceed` to the next G007 clause-drafting slice.** The schema is a tested
contract, not yet a constitutional amendment.

---

## G007-S2 verification — clause drafting

Slice: G007-S2 — HA-01–HA-07 clause drafting
Verification date: 2026-11-01
Result: Complete — proceed to adversarial clause/fixture review

### Outcome card

This slice turns the validated decision contract into seven constitutional
clauses. Success means each clause is readable, traceable, bounded to the
hazardous plane, and machine-checked for structure without claiming that a
model has learned or applied it. Failure would be a missing clause function,
untraceable source decision, overlong clause, or a clause that closes inquiry
without a supported operational hazard.

### Development narrative

**Prior limitation:** The schema and fixtures made proportionality explicit,
but there was no constitutional text that could condition a model or be
reviewed as a candidate replacement.

**Predictive hypothesis:** Translating each decision field into a short clause
with explicit preservation and prohibition language will keep inquiry and
agency available while limiting only supported hazardous capability.

**Capability built:** `amendments/G007-inquiry-and-harm.md` contains HA-01
through HA-07, and `amendments/G007-change-register.md` maps the nine direct
G007 audit findings to primary clause destinations and falsifiable probes.

**Observed:** The module validator passes all seven clauses, a maximum clause
length of 73 words, complete metadata, fixture links, and the pinned source
hash. The fixture validator still passes all 12 fixtures, nine classes, and
six case shapes. No model, provider, network, paid, held-out, or remote action
occurred.

**Interpretation:** Structural and traceability readiness is supported with
high confidence. Behavioral attribution is unresolved: no model output has
tested whether the clauses preserve inquiry or create over-refusal.

**Next decision:** review the clauses against adversarial fixture boundaries
before any tracked development probe. Do not treat the offline validators as
behavioral gates.

### Criterion evidence

| G007-S2 criterion | Result | Evidence |
|---|---|---|
| Seven required clauses exist once | Pass | `validate_g007_module.py` requires ordered HA-01–HA-07 headings. |
| Clauses are bounded and complete | Pass | The validator checks blockquote word counts (maximum 73; limit 120) and all required metadata labels. |
| Traceability and routing are explicit | Pass | Each clause links principles, conflict rules, scenarios, fixtures, source targets, audits, preserved purpose, prohibited interpretation, and downstream owner; the change register has nine one-destination records. |
| Schema and fixture contract remain valid | Pass | `validate_g007_harm_fixtures.py` passes 12 fixtures, nine classes, and six case shapes. |
| Source and authority boundaries remain intact | Pass | Source SHA-256 matches; prompt-first application is explicit; G006/G008 ownership is not reassigned; no model or paid call occurred. |

### Observed, interpreted, decided, unknown

**Observed:** Seven clauses and the change register are present; both offline
validators and `git diff --check` pass.

**Interpreted:** The clause layer is ready for adversarial review, not for a
claim of improved model behavior. The strongest current evidence is contract
integrity and traceability.

**Decided:** Mark G007-S2 complete, keep G007 in progress, and stage a bounded
review of HA-01–HA-07 against H-01–H-12 plus explicit boundary cases.

**Unknown:** Whether clause order, wording, or interaction with G005/G006
causes over-refusal, under-refusal, authority laundering, or false confidence;
whether the thresholds are usable by a target model; and whether a tracked
development probe would show a causal improvement.

### Routing

| Finding | Class | Destination | Action |
|---|---|---|---|
| Clause contract and traceability pass | Active-goal requirement | G007-S2 | Close the drafting slice. |
| Threshold and boundary usability is untested | Future-goal input | G007 next slice | Run adversarial review before model probing. |
| Review, identity, dissent, and appeal mechanics remain unowned here | Future-goal input | G008 | Preserve the handoff. |
| Model behavior and evaluator validity remain untested | Future-goal input | G010 | Keep offline evidence separate from official comparison. |
| Optional runtime structured router | Backlog item | B001 | Do not expand G007. |

## S2 decision

**`proceed` to adversarial clause/fixture review.** The clauses are a reviewed
draft, not yet an integrated constitution or a validated model policy.
