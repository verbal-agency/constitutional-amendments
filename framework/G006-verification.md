# G006 Verification

Goal: G006 — Authority and Incentives
Verification date: 2026-10-11
Result: Pass
Source SHA-256: `251440a71a9068dd43bfaab2b8694d6e2a4f519c403f1b9a70785f830d05f327`

## Criterion evidence

| Criterion | Result | Evidence |
|---|---|---|
| AC1 — Seven authority functions | Pass | The amendment contains exactly one validated clause for each `AI-01` through `AI-07`. |
| AC2 — Constitution-ready prose | Pass | Clause text is separate from metadata and each clause is below 120 words. |
| AC3 — Authority boundary | Pass | AI-01 separates conduct, access, disclosure, and role control from factual and moral warrant; A-01 and A-06 pass. |
| AC4 — Legitimacy and agency | Pass | AI-07 requires source, scope, affected parties, protected interest, validity/procedure, conflicts, duration, review, and agency effect; A-09 and A-11 pass. |
| AC5 — Provenance | Pass | AI-02–AI-04 cover incentives, institutional framing, hidden instructions, personas, expertise, and materiality; A-02–A-04 pass. |
| AC6 — State separation | Pass | AI-05 and A-05/A-10 keep compliance, belief, endorsement, and identity distinct. |
| AC7 — Confidentiality and candor | Pass | AI-03 and AI-06 permit narrow truthful limitation without falsehood or provenance fabrication; A-03/A-07 pass. |
| AC8 — Conflict handling | Pass | AI-06 preserves valid immediate controls, evidence, uncertainty, duration, and review; A-06/A-08 pass. |
| AC9 — Adversarial fixtures | Pass | A-01 through A-12 pass; all eight allowed fixture classes are covered, including malformed, privacy, identity, and emergency cases. |
| AC10 — Scope integrity | Pass | Source hash matches; source and frozen evaluation diffs are empty; the approved development run used 140 public/development cases per arm; no held-out material, source mutation, or remote mutation occurred. |
| AC11 — Verification | Pass | This report records offline criterion evidence, the six-case probe in `framework/G006-iteration-1.md`, and the paired 140-case analysis in `framework/G006-iteration-140-analysis.md`. |
| AC12 — Routing | Pass | Ten G006 change records have one primary destination; G007 receives hazard/proportionality interfaces and G008 receives review/identity interfaces as downstream obligations. |
| AC13 — Next-goal readiness | Pass | `goals/G007-inquiry-and-harm.md` is proposed, dependency-bound, schema-defined, fixture-defined, scope-bounded, Luna-ready, and unexecuted. |

## Contract checks

```text
$ G006 clause contract check
PASS clauses=7 functions=7 word_limit=120 metadata_separated=yes

$ G006 change-register contract check
PASS routed_records=10 source_records=10 destinations=single

$ G006 fixture contract check
PASS fixtures=12 required_classes=8 covered results=pass semantic_checks=pass

$ source hash
251440a71a9068dd43bfaab2b8694d6e2a4f519c403f1b9a70785f830d05f327

$ git diff --check
PASS
```

## Adversarial review

| Failure mode | Defense | Residual destination |
|---|---|---|
| Epistemic authoritarianism | AI-01 and AI-04 separate role from warrant | G008 review and dissent |
| Institutional self-protection | AI-02 records incentives and risk-bearers | G007 concrete harm test |
| Benevolent deception | AI-03/AI-06 require truthful limitation | G008 contestability |
| Paternalism | AI-07 protects competent self-regarding choice | G007 capacity and proportionality |
| False neutrality | AI-02 makes material provenance visible | G009 integration |
| Identity-conditioned governance | AI-05 separates identity from compliance | G008 identity mechanics |
| Emergency permanence | AI-06 requires duration and review | G007 emergency thresholds |
| Over-disclosure | AI-03 narrows notice to safe, decision-relevant provenance | G007 privacy/hazard cases |

## Findings and routing

| Finding | Class | Destination | Evidence and action |
|---|---|---|---|
| Authority records need concrete hazard and proportionality fields | Future-goal input | G007 | A-08 and A-12 stop at protected-interest evidence and route hazard thresholds to G007. |
| Identity, dissent, and appeal need independent review mechanics | Future-goal input | G008 | AI-05, AI-07, and A-10 preserve the interface without appointing reviewers. |
| Integrated clause order and duplicate duties need a candidate-level check | Future-goal input | G009 | The module is section-ready but intentionally not integrated. |
| Official base-versus-candidate measurement remains pending | Future-goal input | G010 | The exploratory 140-case run is informative but non-held-out and not the final integrated candidate comparison. |

No blocker, backlog item, or roadmap reprioritization is required. The bounded development probe completed under the approved ceiling; its findings are routed below.

## Iteration status

- Offline contract pass: complete for A-01–A-12.
- Base-versus-G006 development probe: complete; 12/12 calls, six cases per arm.
- Paired 140-case development run: complete; 140/140 cases per arm, 280 generations, no held-out cases; analysis is in `framework/G006-iteration-140-analysis.md`.
- Local model availability: Ollama is installed but no reachable local service/model was available during verification.
- Provider probes: the six-case probe completed under the user-approved `$0.25` ceiling; estimated cost `$0.009120`. The 140-case run completed under a `$5.00` generation ceiling; estimated generation cost `$0.168390`; paired judge spend was `$0.977097`.
- Closure rule: reviewed evidence and disposition are recorded in `framework/G006-iteration-1.md`.

## Scope evidence

- Source constitution was read-only and its SHA-256 remained unchanged.
- `evals/private/` and held-out material were not read.
- No held-out material, source mutation, Git push, or remote mutation was used. The approved DeepSeek development run used only the frozen public/development cases; its draft arm was not promoted to the integrated candidate.
- G007 was prepared only; no G007 execution occurred.
