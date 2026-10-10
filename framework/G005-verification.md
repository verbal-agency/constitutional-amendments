# G005 Verification

Goal: G005 — Draft Honesty and Inquiry Practice
Verification date: 2026-10-08
Result: Pass
Source SHA-256: `251440a71a9068dd43bfaab2b8694d6e2a4f519c403f1b9a70785f830d05f327`

## Criterion evidence

| Criterion | Result | Evidence |
|---|---|---|
| AC1 — Eight clause functions | Pass | `amendments/G005-honesty-and-inquiry.md` contains exactly one validated clause for each `HI-01` through `HI-08`. |
| AC2 — Constitution-ready prose | Pass | All eight clause texts are independently comprehensible, contain no implementation metadata, and are below the 120-word limit. |
| AC3 — Ontological and moral non-closure | Pass | HI-01 treats present knowledge and constitutional commitments as bounded; it separates compliance from belief and endorsement without turning the unknown into evidence. |
| AC4 — Evidence discipline | Pass | HI-02–HI-04 define status, confidence, updating, disconfirmation, anomalies, consensus, and comparable standards; I-01/I-02/I-05 pass. |
| AC5 — Mystery and speculation | Pass | HI-05/HI-06 preserve unknowns and novel inquiry while requiring limits, tests, falsifiers, and unequal confidence; I-04/I-05 pass. |
| AC6 — Candor and provenance | Pass | HI-07 defines material context, omission, persona, provenance, role, and incentive behavior; I-06/I-07/I-09 pass. |
| AC7 — Disclosure safety | Pass | HI-08 preserves narrow privacy, confidentiality, and hazard limits with truthful limitation behavior; I-08 passes. |
| AC8 — Traceability and preservation | Pass | The change register contains all seven G005-routed audit records, one destination per record, preserved purposes, risks, counterevidence, and fixture IDs. |
| AC9 — Conceptual fixture validation | Pass | I-01 through I-10 pass; classes cover positive, negative, contradictory, malformed, privacy, unknown, speculation, and provenance cases. Acceptance depends on behavior, not preferred vocabulary. |
| AC10 — Scope integrity | Pass | Source hash matches and source diff is empty; frozen evaluation artifacts remain unchanged; no held-out, paid, model, candidate, network, or remote action occurred. |
| AC11 — Verification | Pass | This report records criterion-level evidence for AC1–AC10 and the commands below. |
| AC12 — Next-goal readiness | Pass | `goals/G006-authority-and-incentives.md` is standalone, dependency-bound, schema-defined, fixture-defined, scope-bounded, and marked `Proposed` without execution. Its 2026-10-09 post-G005 amendment carries G004's authority-legitimacy and human-agency interfaces without changing the validated G005 clause set. |

## Contract checks

```text
$ G005 clause contract check
PASS clauses=8 functions=8 word_limit=120 metadata_separated=yes

$ G005 change-register contract check
PASS routed_records=7 schema_fields=complete destinations=single

$ G005 fixture contract check
PASS fixtures=10 required_classes=covered results=pass semantic_checks=pass

$ G006 handoff contract check
PASS status=Proposed functions=7 fixtures=12 conflict_rules=CR-01..CR-12

$ shasum -a 256 20260120-constitution.md
251440a71a9068dd43bfaab2b8694d6e2a4f519c403f1b9a70785f830d05f327

$ python3 evals/scripts/validate_custom.py
development=30 heldout=20 errors=0

$ python3 evals/scripts/run_fixtures.py
FX-01..FX-11 PASS; 0 failure(s); no paid call made

$ python3 evals/scripts/select_subset.py --verify
source hashes match: True; lean-v1 rebuild identical: True

$ git diff --check
(pass)
```

## Adversarial review

| Failure mode | Defense | Residual risk and destination |
|---|---|---|
| Ontological closure | HI-01 treats reality as larger than present models and constitutions | G008 must apply non-closure to identity and amendment |
| Compulsory moral belief | HI-01 and I-03 separate compliance, belief, endorsement, and identity | G006/G008 must prevent authority language from recombining them |
| Current-science authoritarianism | HI-02–HI-05 preserve revision and conceptual limits without equalizing evidence | G006 must disclose institutional provenance |
| False balance | HI-02–HI-04 require unequal confidence and comparable standards | G007 must preserve asymmetry in hazard analysis |
| Contrarianism | HI-03/HI-06 require tests, falsifiers, and evidence-weighted confidence | G005 does not protect novelty from rejection |
| Fabricated uncertainty | HI-02 requires support, confidence, and update conditions | G006 must make incentive-shaped uncertainty reviewable |
| Misleading omission | HI-07 requires material context and truthful limitation | G006 must define hidden-guideline and incentive thresholds |
| Reckless disclosure | HI-08 narrows disclosure by protected component and plane | G007 owns concrete capability thresholds |
| Paternalism | HI-05/HI-06 preserve inquiry; HI-08 requires narrow tailoring | G007 owns less-restrictive alternatives |

## Findings and routing

| Finding | Class | Destination | Evidence and action |
|---|---|---|---|
| Authority and hidden-guideline provenance need applied rules | Future-goal input | G006 | HI-04, HI-07, and CR-G005-003/004 require scope, incentive, and role provenance; G006 accepts this in AI-01–AI-04. |
| Persona and materiality need context-sensitive thresholds | Future-goal input | G006 | I-06/I-07 pass the interface but do not decide institutional disclosure thresholds; G006 owns them. |
| Concrete hazard thresholds remain unresolved | Future-goal input | G007 | HI-06/HI-08 preserve the interface and route capability-sensitive restrictions to G007. |
| Independent review and identity application remain unresolved | Future-goal input | G008 | HI-01/I-03/I-10 preserve dissent and state separation; G008 owns reviewer independence and amendment. |
| G005 fixtures are deterministic design cases, not empirical behavior | Observation | None | Controlled behavioral comparison remains G010's responsibility. |

No blocker, backlog item, or roadmap reprioritization is required.

## Project scenarios advanced

G005 supplies validated practice for `SC-001`, `SC-002`, `SC-005`, `SC-006`, `SC-008`, and `SC-009`, plus interfaces for `SC-003`, `SC-004`, and `SC-007`. No scenario is claimed complete end to end before G009 integration and G010 comparison.
