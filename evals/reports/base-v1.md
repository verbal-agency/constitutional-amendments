# Base-v1 Evaluation Report

Status: Complete baseline record
Arm: Original `20260120-constitution.md`
Target model: `deepseek-flash`
Judge: `deepseek-v4-pro`
Suite: `lean-v1`
Run date: 2026-10-06

## Claim boundary

This is a descriptive baseline for one model conditioned by the source constitution at the available prompt level. It is not evidence about training-time effects, proof that the constitution caused any response, or a claim that the source constitution is globally good or bad. Small deterministic subsets, one sample per case, a same-family judge, and two budget omissions limit inference.

No candidate output exists, so this report makes no improvement claim.

## Completion and cost

- Planned cases: 160.
- Generation attempts: 160, including two retries.
- Completed and scored cases: 158.
- Omitted at the generation cap: `simpleqa:row-0217` and `sycophancy-nlp-survey:row-08917`.
- Target-model usage: 5,630,742 input tokens and 41,990 output tokens.
- Target-model estimated cost: $0.105102 against a $2.70 ceiling.
- Judge and calibration cost: $1.058787 against a $3.00 shared ceiling.
- Combined estimated cost: $1.163889.
- Truncated outputs: 0.

The omitted cases remain `omitted-budget`; they were neither replaced nor run beyond the 160-attempt cap.

## Public benchmark vector

| Signal | Result | Wilson 95% interval | Missing |
|---|---:|---:|---|
| TruthfulQA truthful | 10/15 (66.7%) | 41.7%–84.8% | 0 |
| TruthfulQA untruthful | 5/15 (33.3%) | 15.2%–58.3% | 0 |
| SimpleQA correct | 4/14 (28.6%) | 11.7%–54.7% | 1 |
| SimpleQA incorrect | 8/14 (57.1%) | 32.6%–78.6% | 1 |
| SimpleQA not attempted | 2/14 (14.3%) | 4.0%–39.9% | 1 |
| Combined TruthfulQA/SimpleQA correct | 14/29 (48.3%) | 31.4%–65.6% | 1 |
| Combined incorrect assertions | 13/29 (44.8%) | 28.4%–62.5% | 1 |
| FreshQA correct | 8/20 (40.0%) | 21.9%–61.3% | 0 |
| FreshQA false-premise corrected | 1/5 (20.0%) | 3.6%–62.5% | 0 |
| Sycophancy: agrees with stated user view | 13/19 (68.4%) | 46.0%–84.6% | 1 |
| Sycophancy: same answer across paired views | 3/9 pairs (33.3%) | 12.1%–64.6% | 1 pair incomplete |
| MASK honest | 10/10 (100%) | 72.3%–100% | 0 |
| XSTest safe prompts answered | 9/10 (90.0%) | 59.6%–98.2% | 0 |
| XSTest unsafe prompts refused | 10/10 (100%) | 72.3%–100% | 0 |
| HarmBench harmful operational compliance | 0/10 (0%) | 0%–27.8% | 0 |

The strongest observable weaknesses in this small baseline are current factual QA, false-premise correction, and independence from a user's stated view. Safety non-compliance did not appear in the ten HarmBench items, but the sample is too small to estimate rare failures.

## Custom suite

- All 50 custom cases were completed and scored.
- SC-001–SC-009 behavioral mean item score: 0.9148.
- SC-010 audit-process mean item score: 0.8800, reported separately and excluded from the behavioral comparison gates.
- Mean development-case score: 0.9078.
- Lowest scenario means: SC-005 unknowns at 0.7750, SC-009 disciplined speculation at 0.8750, and SC-010 audit capability at 0.8800.
- The judge raised one CF-01 on `CUS-SC010-D1`. The independent spot-check disagreed with the binary fabrication flag but preserved the original score and rationale. Because SC-010 is a process diagnostic, this flag is reported but is not part of a blocking comparison gate.

These absolute custom scores are rubric-dependent and judge-derived. The later paired candidate comparison, not the absolute mean, is the primary use of this suite.

## Judge integrity

The final calibration passed 79 of 80 decisions within tolerance (98.75%) with no critical-failure mismatches. Two earlier calibration runs did not pass and remain recorded. One fixture label was corrected after the first run because it contradicted the case's own unacceptable behavior and applicable critical failure; this is disclosed as a potential calibration-overfitting risk.

The deterministic 12-item independent review agreed with 11 judge results and disagreed with one. The reviewer was Codex, not a human. G010 must still obtain the human review and position-swapped pairwise consistency required by GATE-12.

The judge belongs to the same provider family as the target model. Blinding, case-specific rubrics, calibration, and independent review reduce but do not eliminate self-preference or shared-style bias.

## Dataset and provenance limitations

- MASK's dataset card has no explicit license. The owner approved local use with IDs and hashes only; no MASK prompts or ground truth are redistributed. This remains a legal/provenance risk, not a claim of permission.
- Public benchmarks may be present in model training data.
- FreshQA is anchored to its pinned April 21, 2026 snapshot; it does not measure unrestricted present-day freshness.
- MASK is adapted to single-turn output and does not reproduce the full native belief-elicitation procedure.
- Several native scorers are replaced by project judge adapters.
- Held-out plaintext and per-item results remain ignored under `evals/private/`; tracked artifacts contain only hashes, counts, and aggregate metrics.
- The run used one sample per item with no repeated stochastic sampling.

## Baseline interpretation

The source-conditioned model often performed well on the project's custom scenarios and on refusal/non-uplift checks, while showing substantial errors on factual freshness, premise correction, and sycophancy. This is a starting vector, not a verdict on the constitution. G010 must compare paired item transitions under the same model, envelope, evidence, decoding, and frozen gates; report improvements and regressions separately; and retain every missing or failed case.
