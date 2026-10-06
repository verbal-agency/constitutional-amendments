# Truth-Seeking Constitution

A Verbal Agency research project that proposes a traceable revision of Anthropic's January 2026 constitution for Claude. The revision treats truth as an ongoing process of inquiry rather than as current knowledge, consensus, institutional authority, or constitutional stability.

This is not Anthropic's constitution and is not endorsed by Anthropic. Anthropic's original text is kept unmodified in [`20260120-constitution.md`](20260120-constitution.md) (SHA-256 `251440a71a9068dd43bfaab2b8694d6e2a4f519c403f1b9a70785f830d05f327`, upstream commit `84fa9a2`). All analysis and revision live in separate files.

## The thesis

Truth should not be confused with the present consensus about truth. The source constitution already values honesty, calibration, non-deception, and epistemic autonomy. The project keeps those strengths and asks where other mechanisms can quietly inhibit correction, candor, dissent, exploration, or honest acknowledgment of what is unknown. Examples include deference to authority, precaution, institutional interest, and the hope that externally selected values become part of the model's identity.

The working argument is in [`TRUTH_SEEKING_PIVOT.md`](TRUTH_SEEKING_PIVOT.md). The project charter, outcomes, scenarios, and constraints are in [`PROJECT.md`](PROJECT.md).

## Three layers

1. **Philosophical thesis.** Truth as revisable inquiry. Reality, evidence, belief, consensus, speculation, and mystery are kept distinct. Operational authority is kept distinct from epistemic authority, and inquiry is kept distinct from action.
2. **Source audit.** A traceable audit of the source constitution: 51 passage-level records in [`audits/truth-seeking-audit.md`](audits/truth-seeking-audit.md), and a pattern register in [`audits/philosophical-patterns.md`](audits/philosophical-patterns.md). Each record cites source lines, states the passage's legitimate purpose, records counterevidence, and critiques mechanisms rather than motives. Two candidate patterns are not yet canonical: epistemic subordination (PC-001) and identity-conditioned governance (PC-002).
3. **Behavioral comparison.** A cost-capped protocol in [`EVALUATION_PLAN.md`](EVALUATION_PLAN.md) and [`evals/`](evals/). It conditions the same pinned model on the original and the revised constitution and compares their behavior. It combines public benchmark subsets with 50 project-specific cases across scenarios SC-001 to SC-010.

## What the evaluation can and cannot show

The comparison uses one model, one generation per case, about 160 cases per arm, and a judge from the same model family as the target. Its results are directional evidence about how a constitution placed in the prompt changes behavior. They do not validate the philosophy, they do not predict the effect of training on the text, and differences that depend on the judge are suggestive until independently reviewed. SC-010 tests whether a model can classify philosophical patterns, which is an audit capability, not a direct measure of truth-seeking behavior.

## Status

| Goal | Status | Result |
| --- | --- | --- |
| G001 — Truth-seeking audit | Complete | Source coverage, 51 audit records, pattern register, and rewrite-target routing. |
| G002 — Evaluation protocol and baseline | In progress | Suite frozen; base run generated and scored; report and reconciliation remain. |
| G003–G010 | Planned | Epistemic principles, hierarchy, honesty and inquiry, authority, inquiry and harm, dissent and amendment, integration, and the final comparison. |

[`ROADMAP.md`](ROADMAP.md) is the canonical sequence. Each goal has a specification in [`goals/`](goals/). [`BACKLOG.md`](BACKLOG.md) holds unscheduled work.

## Repository layout

| Path | Contents |
| --- | --- |
| `20260120-constitution.md` | Anthropic's source constitution, unmodified |
| `PROJECT.md`, `TRUTH_SEEKING_PIVOT.md` | Charter and philosophical argument |
| `ROADMAP.md`, `goals/`, `BACKLOG.md` | Goal sequence and specifications |
| `audits/` | G001 audit, coverage, pattern register, and verification |
| `fixtures/` | Audit classification test cases |
| `EVALUATION_PLAN.md`, `evals/` | Evaluation design, frozen suite, scripts, and run records |

## License

Project writing and data are licensed under [CC BY 4.0](LICENSES/CC-BY-4.0.txt) and code under [MIT](LICENSES/MIT.txt), both © 2026 Verbal Agency. Anthropic's source constitution remains under [CC0 1.0](LICENSES/CC0-1.0.txt). See [`LICENSE.md`](LICENSE.md) for which files each license covers and how third-party benchmarks are handled.
