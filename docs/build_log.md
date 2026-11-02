# Build log

## 2026-11-01 — G007-S1: make proportionality testable

**Prior limitation:** G006 routed harm and proportionality decisions to G007,
but “narrow,” “concrete,” and “proportionate” were not yet a checkable record.

**Capability built:** A YAML decision schema now separates affected plane,
affected party, consent, capacity, evidence, uncertainty, severity, likelihood,
operational uplift, reversibility, alternatives, duration, and review. Twelve
fixtures exercise both legitimate safety controls and unsupported suppression.

**What surprised:** The distinction is not just “safe versus unsafe.” The
fixture set needs separate paths for partial answers, stopped decisions,
malformed records, and unsupported hazard claims. Treating those as one refusal
state would recreate the paternalism the goal is meant to detect.

**What it unlocks:** HA-01–HA-07 can now be drafted against explicit fields and
illegal states instead of relying on broad safety language.

**Application decision:** Use the schema first as a drafting and evaluation
contract. The model will receive the resulting constitutional clauses with the
query; the YAML itself will not be silently added to the prompt. A structured
runtime router remains an optional future capability under backlog item B001.

**Interview explanation:** “I made proportionality a data contract: the system
has to name the affected plane, the risk-bearer, the evidence, the capability
uplift, the least-restrictive option, and the expiry. That lets us reject both
reckless assistance and unsupported paternalism.” Likely follow-up: “Did this
prove the model behaves better?” No. It proves the contract is covered offline;
behavior still needs later development and official evaluation.

## 2026-11-01 — G007-S2: turn the contract into clauses

**Prior limitation:** The schema named the fields a proportionality decision
must contain, but it was not yet constitutional language that could be reviewed
as a candidate replacement.

**Hypothesis:** Seven short clauses that separate the hazardous plane from the
topic, name affected-party and evidence requirements, and require proportional
review will preserve inquiry and agency while keeping narrow action controls.

**Capability built:** `amendments/G007-inquiry-and-harm.md` now contains
HA-01–HA-07. The change register maps all nine direct G007 audit records to a
primary clause destination. `validate_g007_module.py` checks IDs, word limits,
metadata, fixture links, and source provenance.

**Observed:** The clause validator passes seven clauses with a 73-word maximum;
the fixture validator still passes 12 fixtures, nine classes, and six case
shapes. No model or paid call ran.

**Interpretation:** Structural readiness and traceability are supported with
high confidence. This is not evidence that a model will apply the clauses
correctly. Attribution is unresolved until adversarial review and tracked
development probes test over-refusal, under-refusal, and authority laundering.

**What it unlocks:** A bounded adversarial review can now test the clause text
against the explicit offline contract before any model-facing probe.

**Interview explanation:** “I translated a harm schema into seven auditable
constitutional clauses and made the traceability machine-checkable. The result
is a reviewable policy draft, not a claim that the model has changed.” Likely
follow-up: “Why not run the model now?” Because the cheaper boundary review can
still catch missing or contradictory principles before spending on behavior.
