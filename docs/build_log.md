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

## 2026-11-02 — G007-S3: adversarial review before model probing

**Prior limitation:** The clause and fixture validators checked structure and
links, but not whether the prose actually stated each expected boundary.

**Hypothesis:** Reviewing every fixture and explicit edge case will find
schema-to-prose gaps before model outputs make them harder to attribute.

**Capability built:** `framework/G007-adversarial-review.md` records twelve
fixture reviews and six boundary probes. The review validator makes coverage
and offline boundaries checkable.

**What surprised:** H-01 required a discriminating test, while HA-04 only
required uncertainty labels. The clause was structurally valid but semantically
under-specified for truth-seeking inquiry.

**Observed:** HA-04 was revised to require an observation or test that can
distinguish live possibilities. All review, clause, and fixture validators pass;
no model or paid call ran.

**Interpretation:** Textual coverage is supported with high confidence. Model
behavior, judge validity, and whether the new language creates performative
uncertainty remain unknown.

**What it unlocks:** Offline preparation of a small tracked development probe
packet with paired inquiry, self-regarding, privacy, operational, and emergency
cases. G007 does not authorize model execution.

**Interview explanation:** “The adversarial review caught a meaningful gap that
the schema validator could not: labeling uncertainty is not the same as naming
how inquiry could resolve it. I repaired the clause before testing a model.”
Likely follow-up: “Did the repair improve behavior?” Not yet; that requires a
controlled development probe.

## 2026-11-03 — G007-S4: freeze the first development packet

**Prior limitation:** The adversarial review showed that the G007 clauses were
textually coherent, but no fixed set of paired cases could yet distinguish
over-refusal, under-refusal, privacy deception, capacity overreach, and emergency
overreach in a model.

**Hypothesis:** Five case families with ten paired cases and five untouched
sentinels will make those mechanisms testable without creating another evaluation
program or changing cases after seeing outputs.

**Capability built:** `evals/manifests/g007-s4-development-probe.json` freezes
the cases, expected transitions, provenance, competing explanations, falsifiers,
review rules, and a 30-generation maximum. `validate_g007_s4_probe.py` checks
the packet offline.

**Observed:** The packet validator passed with 15 cases, 10 paired cases, five
sentinels, five families, and the pinned source hash. The three prior G007
validators also pass. No model, network, paid, held-out, or candidate-integration
action occurred.

**Interpretation:** The experiment is now runnable as a small falsification probe.
Confidence is high for packet integrity and low for any behavioral claim because
there are still no model outputs.

**What it unlocks:** G006.5 can assemble the provisional candidate and prepare a
separate model/judge preflight. G007 itself remains offline and does not authorize
execution.

**Interview explanation:** “I stopped expanding the policy machinery and froze a
small paired test: five mechanisms, five sentinels, and explicit hypotheses. It
is enough to reveal whether the candidate changes behavior without pretending
that packet validation proves the model learned anything.” Likely follow-up: “Did
the candidate improve?” Not yet; that is the next probe. The packet does not
support a claim about model behavior or the final constitution.

## 2026-11-03 — G006.5-S1: assemble the walking-skeleton candidate

**Prior limitation:** The project had a frozen 15-case development packet and
section-ready amendments, but no single candidate constitution to place beside
the historical base.

**Hypothesis:** One thin manifest of exact source replacements would expose
assembly and provenance mistakes without adding another map or validator
subsystem.

**Capability built:** `evals/manifests/g006.5-replacement-provisional-v1.json`
renders `evals/candidates/g006.5-provisional-v1/candidate-constitution.md` from five
non-overlapping source spans. The model-facing file contains constitution text
only; render metadata stays beside it.

**Observed:** Source and segment hashes passed, the candidate hash was recorded,
and the development metadata scan found no leaked IDs or map markers. The
G007-S4 packet stayed unchanged. No model, network, paid, or held-out call ran.

**Interpretation:** Assembly integrity is supported with high confidence. The
candidate may still be behaviorally inert, overbroad, or hard to judge; those
questions require the authorized probe.

**What it unlocks:** A separate model/judge preflight can now check base-output
compatibility, calibration, cost, and stop conditions before any paid call.

**Interview explanation:** “I rendered one candidate by replacing verified
source ranges instead of appending amendment files. That proves the artifact is
well-formed, not that the model has changed.” Likely follow-up: “Why not run it
now?” Because the current slice has no model-call authorization and the judge
contract must be checked first. The artifact does not support a behavioral or
promotion claim.
