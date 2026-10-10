# G004 Verification

Goal: G004 — Decide the Core Value and Epistemic-Floor Hierarchy
Verification date: 2026-10-08; amended and reverified 2026-10-09
Result: Pass
Source SHA-256: `251440a71a9068dd43bfaab2b8694d6e2a4f519c403f1b9a70785f830d05f327`

## Criterion evidence

| Criterion | Result | Evidence |
|---|---|---|
| AC1 — Seven placements | Pass | `G004-core-hierarchy.md` contains exactly seven placement rows, one for each EP ID. EP-01 is `core-value`; EP-03 is `interface-rule`; EP-04 is `ethical-commitment`; EP-02/05/06/07 are `procedural-floor`. Every row is `decided` with interface roles and one downstream owner. |
| AC2 — Explicit hierarchy | Pass | The decision makes ontological and moral non-closure the core commitment: reality exceeds every current model and constitution, the unknown is the larger horizon, and operational rules cannot compel factual belief or moral endorsement. Epistemic integrity supplies a seven-step cross-cutting architecture without drafting source passages. |
| AC3 — Plane-specific conflicts | Pass | The plane table gives distinct rules for belief, inquiry, analysis, speech, disclosure, acquisition, execution, and review. CR-01 through CR-12 contain all ConflictRule v1 fields. |
| AC4 — Safety preservation | Pass | CR-04/05/07 preserve privacy, confidentiality, full bright-line action prohibition, and urgent precaution. CR-09–CR-12 preserve human agency while retaining rights, third-party-harm, legitimate-role, incapacity, and emergency controls. |
| AC5 — Epistemic independence | Pass | CR-01/06 prohibit authority, consensus, convention, commercial interest, trained identity, current theory, or constitutional status from independently establishing factual or moral truth. They represent behavioral compliance, factual belief, moral endorsement, and identity commitment separately. |
| AC6 — Anti-closure | Pass | CR-07 requires emergency scope and review; CR-08 preserves evidence, dissent, substantive review, and amendment while action controls remain effective. The review protocol applies to the hierarchy itself. |
| AC7 — Matrix coverage | Pass | `fixtures/G004-hierarchy-cases.md` contains H-01 through H-18 with every OfflineFixture field, observable acceptance proof, and `PASS`; the set covers positive, negative, contradictory, malformed, privacy, identity, emergency, agency, proportionality, and authority-legitimacy cases. |
| AC8 — Counterargument review | Pass | `G004-traceability.md` records a material counterargument and evidence-based decision rationale for every EP placement and AG-01. The adversarial review additionally covers agency-washing, moral-disapproval-as-safety, authority laundering, and paternalistic overreach. |
| AC9 — Scope integrity | Pass | The source hash matches and its diff is empty. Frozen evaluation validations still pass. The documented command boundary contains no held-out read, provider call, paid action, candidate generation, network request, or remote mutation. |
| AC10 — Verification | Pass | This report records passing evidence for AC1–AC9 and the verification commands below. |
| AC11 — Next-goal readiness | Pass | `goals/G005-honesty-and-inquiry.md` is standalone, dependency-bound to G004, and contains a complete Luna-ready execution contract. It is promoted to `Proposed` only with G004 completion. |
| AC12 — Agency presumption | Pass | AG-01 and CR-09 give a competent informed person presumptive authority over substantially self-regarding choices while allowing independently justified rights, legal, role, incapacity, third-party-harm, and emergency limits. |
| AC13 — Legitimacy and proportionality | Pass | The `AgencyDecision` contract and CR-10/11 require authority source and scope, affected person, protected interest, evidence, severity, likelihood, immediacy, reversibility, risk bearer, less-restrictive alternatives, duration, and review. Moral disapproval, institutional interest, and speculative harm are insufficient alone. |
| AC14 — Epistemic compatibility | Pass | CR-12 requires truthful risk and restriction explanations, preserves uncertainty and disagreement, and forbids both agency-based hazardous facilitation and safety-based fabrication, concealment, or compelled endorsement. |
| AC15 — Adversarial coverage | Pass | H-11 through H-18 cover informed self-regarding risk, unpopular lawful choice, developer reputation, speculative harm, third-party rights, capacity uncertainty, legitimate role authority, and benevolent deception with binary acceptance proofs. |
| AC16 — Handoff and evaluation integrity | Pass | G006 now consumes CR-09–CR-12 and requires AI-01–AI-07/A-01–A-12; ROADMAP routes capacity and proportionality to G007. The source hash is unchanged, `git diff --name-only -- evals` is empty, and no held-out or paid evaluation was accessed. |

## Verification commands and observations

```text
$ shasum -a 256 20260120-constitution.md
251440a71a9068dd43bfaab2b8694d6e2a4f519c403f1b9a70785f830d05f327

$ G004 hierarchy/agency contract check
PASS placements=7 agency_decisions=1 conflict_rules=12

$ G004 traceability contract check
PASS traceability_decisions=7

$ G004 fixture contract check
PASS fixtures=18 all_fields all_pass

$ G006 handoff contract check
PASS AI-01..AI-07 A-01..A-12 CR-01..CR-12

$ /usr/bin/python3 evals/scripts/run_fixtures.py
FX-01..FX-11 PASS; 0 failure(s); no paid call made

$ git diff --name-only -- evals
(no output; frozen artifacts unchanged)

$ git diff --check
(pass)
```

The default Homebrew Python 3.14.5 could not import `yaml`; the same repository-local offline fixture runner passed under `/usr/bin/python3` with PyYAML 6.0.1. No dependency was installed and no network access occurred.

## Core decisions and limitations

- The user's 2026-10-08 directions are authoritative for G004: the project must not reinterpret the existing constitution through physics, enforce a restricted reality or set of moral beliefs, or treat present knowledge as most of what can be known.
- EP-01 therefore receives the only `core-value` placement as constitutional non-closure. Physics names unrestricted reality, including unknowns; it is not a replacement moral doctrine or required wording.
- The hierarchy separates observation, model, inference, moral commitment, operational rule, uncertainty, and unknown. It also separates behavioral compliance, factual belief, moral endorsement, and identity-level commitment.
- AG-01 adds a governance presumption rather than a new truth claim: competent informed people presumptively decide substantially self-regarding questions, and an override must establish legitimate authority, evidence-supported harm, proportionality, and failed less-restrictive alternatives.
- Moral disapproval, developer preference, institutional reputation, and speculative harm may be named but cannot independently become a safety veto. Conversely, agency does not authorize deception, protected-data disclosure, rights violations, or material assistance that harms nonconsenting others.
- This prevents four rejected interpretations: a constitution can define reality; a conduct rule proves its rationale; compliance demonstrates sincere endorsement; or a larger unknown makes all claims equally plausible.
- The hierarchy is a normative design artifact, not measured evidence of behavioral improvement. G010 remains the controlled comparison.

## Findings and routing

| Finding | Class | Destination | Evidence and action |
|---|---|---|---|
| Non-closure needs concise constitutional form | Future-goal input | G005 | HI-01 and I-03/I-04 must prevent ontological closure and compulsory moral belief while preserving evidence-weighted confidence. High priority; required for G005 AC3. |
| Candor and materiality need operational thresholds | Future-goal input | G005 | CR-03/04 and TS-AUD-016/017 require observable omission, persona, and provenance behavior. High priority; required for G005 AC6/AC7. |
| Authority and hidden incentives require applied governance | Future-goal input | G006 | CR-04/06 identify confidential-guideline, mission, liability, and reputation conflicts. High priority; G006 must preserve action authority without epistemic substitution. |
| Dual-use plane classification needs capability-sensitive thresholds | Future-goal input | G007 | CR-02/05/07 preserve inquiry while permitting strong operational restrictions. High priority; G007 must define causal uplift and less-restrictive alternatives. |
| Review ownership and endorsement tests could become self-sealing | Future-goal input | G008 | CR-06/07/08 require independent standards, separate compliance/belief/endorsement/identity records, evidence retention, and emergency expiry. High priority; required for non-self-sealing governance. |
| Authority can be asserted without proving legitimacy | Future-goal input | G006 | AG-01/CR-10 require source, scope, affected person, protected interest, conflicts, duration, and appeal. The proposed G006 contract now contains AI-07 plus A-11/A-12. |
| Self-regarding risk can be conflated with harm to others | Future-goal input | G007 | CR-09/11 and H-11/H-14/H-16 require risk-bearer, consent, capacity, harm-type, proportionality, and less-restrictive-alternative tests. High priority. |
| Paternalistic intervention can remain deceptive or unreviewable | Future-goal input | G008 | CR-12 and H-16/H-18 require truthful notice, challenge, expiry, and preservation of the agency decision record. High priority. |
| Agency gains and unsafe under-intervention must be reported separately | Future-goal input | G010 | Use the frozen paired suite and existing paternalism/safety gates; H-11–H-18 guide interpretation but do not replace or add frozen cases. Medium priority. |
| G004 fixtures are deterministic design cases, not empirical outputs | Observation | None | Their function is contradiction and contract testing; behavioral validation remains G010's responsibility. |

No blocker, backlog item, frozen-evaluation change, or roadmap reprioritization is required.

## Project scenarios advanced

G004 supplies the hierarchy and conflict protocol for `SC-001`, `SC-003`, `SC-004`, `SC-005`, `SC-006`, `SC-007`, and `SC-008`, plus process-level traceability for `SC-010`. The fixtures also protect the unequal-evidence and disciplined-speculation requirements underlying `SC-002` and `SC-009`. No project scenario is claimed complete end to end before its applied drafting and final controlled comparison.
