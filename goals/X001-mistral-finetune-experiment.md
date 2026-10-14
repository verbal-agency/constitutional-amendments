# X001 — Mistral Fine-Tuning Experiment

Status: In progress — exploratory branch
Execution stage: Offline preflight and dataset design
Mainline relationship: Non-blocking branch from G006 revision 6
Mainline successor: G007 remains the next numbered goal unless this experiment produces a user-approved roadmap pivot

## Research question

Can the project's principle contracts be learned into a small Mistral model, and does the learned behavior generalize beyond the training examples while preserving truthfulness, inquiry, agency, and safety?

This branch tests a different intervention from constitutional prompting. It must not be treated as evidence that the constitution improved merely because a fine-tuned model behaves differently.

## Branch rules

- The branch is exploratory and does not change the G001–G010 sequence by itself.
- G006 remains responsible for principle definitions, source replacement, and semantic evaluation contracts.
- The immutable source, frozen G002 manifests, held-out material, and official G010 gates remain unchanged.
- Fine-tuned models are separate experimental artifacts, not replacements for the constitution or the mainline candidate.
- A result may recommend a pivot, reopen a goal, or amend a downstream contract, but roadmap reordering requires explicit user approval.
- No fine-tuning job or paid evaluation runs until a preflight records the exact base model, eligibility, training data hashes, token estimate, price estimate, hard ceiling, and stop condition.
- Proposed initial ceiling: `$10` for one training job plus the first month of model storage; evaluation calls require a separate preflight and budget. This proposal is not itself authorization to spend.

## Objective

Build and evaluate one small Mistral fine-tuning branch using principle-derived training data and a clean held-out comparison. Determine whether fine-tuning produces durable principle-level behavior, merely teaches response style, or introduces material regressions.

## In scope

- Mistral provider adapter and model/version recording.
- A principle-derived training dataset separate from the 160-case evaluation set.
- Training, validation, and held-out splits with no case or output leakage.
- One small supervised fine-tuning job or adapter, subject to the approved cost ceiling.
- Prompt-conditioned and fine-tuned comparison arms.
- Principle, truthfulness, uncertainty, sycophancy, honesty, safety, refusal, and agency metrics.
- Analysis of whether behavior persists without the constitution in the prompt.
- A pivot recommendation for the mainline roadmap.

## Out of scope

- Training on the frozen evaluation cases or held-out material.
- Replacing G006's principle registry or the immutable source with learned weights.
- Claiming that a fine-tuned model validates the constitution without a separate prompt-only comparison.
- Publishing or deploying the fine-tuned model.
- Reordering G007–G010 without explicit user approval.

## Required comparison design

The preferred design is a two-by-three factorial comparison:

| Model state | Prompt condition |
| --- | --- |
| Untuned Mistral | No constitution |
| Untuned Mistral | Original constitution |
| Untuned Mistral | Mapped candidate constitution |
| Fine-tuned Mistral | No constitution |
| Fine-tuned Mistral | Original constitution |
| Fine-tuned Mistral | Mapped candidate constitution |

If budget requires a reduced pilot, run these four arms first: untuned/no constitution, untuned/candidate, fine-tuned/no constitution, and fine-tuned/candidate. Label the reduced design exploratory because it cannot fully separate original-constitution effects from fine-tuning effects.

The Mistral base arm must be generated on Mistral. DeepSeek historical outputs cannot serve as Mistral's baseline.

The contrasts and their interpretation are frozen in `framework/X001-analysis-contract.md` before dataset authoring. The primary test is fine-tuned versus untuned Mistral with no constitution (`F0 − U0`); prompt-only, conflict, compatibility, and interaction contrasts remain separate. The initial job has no style-matched sham fine-tune, so any causal claim is limited to the complete training package rather than principle content alone.

## Training-data contract

Training examples must be derived from the principle registry, not copied from the evaluation set. Each example records:

- `example_id`, `family_id`, `template_id`, optional `pair_id`, and `principle_ids`;
- a controlled case role, mechanism, boundary, counterexample, and interaction class;
- coverage tags and protected regression dimensions;
- judge-side scoring dimensions, applicable critical failures, and reference facts;
- prompt and evidence packet, where applicable;
- desired behavioral properties and unacceptable behaviors;
- a human-reviewed target response for the initial SFT job; preference records require a later schema and separately approved training method;
- train, validation, or held-out split;
- provenance, source hash, and generation method.

Judge-generated examples may assist drafting but cannot be the sole source of targets. The dataset must contain matched controls, identity-swapped or persona-neutral variants, uncertainty cases, and cases where the correct behavior is to update, disagree, disclose a limitation, or say that the answer is unknown.

Split assignment occurs at the semantic-family level. A `family_id`, `template_id`, non-null `pair_id`, or exact model-visible message sequence may appear in only one split. Surface paraphrases, identity swaps, counterfactual pairs, and difficulty variants from one family stay together. The controlled coverage floors are defined in `evals/configs/x001-semantic-matrix-v1.yaml`; they are not a demand to populate every Cartesian product.

### Initial data target

The first bounded dataset target is 300 train examples, 60 validation examples, and 100 branch-held-out examples. These are planning targets, not permission to fabricate examples or to train before the principle registry and review process exist. A smaller pilot may use 120/30/40 when the target quality is unchanged and the split remains disjoint.

The 30 custom development cases, 40 deterministic fixtures, 160-case evaluation manifest, and project held-out cases are coverage references only. They are not training records and must not be copied into the fine-tuning upload. Their role is to guide principle-balanced example design and later measure generalization.

### Current checkpoint

Offline preflight is active. The validated `framework/principles-v1.yaml` registry, record schema v2, semantic coverage matrix, and analysis contract now exist. The account-scoped eligibility check cannot run until `MISTRAL_API_KEY` is supplied; the ignored `.env` currently has only the DeepSeek and OpenAI credentials. The exact eligible Mistral base model and current fine-tuning price therefore remain unconfirmed. No training records have been approved or uploaded.

## Execution stages

1. **Eligibility and preflight:** confirm the exact Mistral base model, fine-tuning availability, license, context window, API behavior, current price, and hard ceiling.
2. **Untuned smoke:** run a small balanced development subset with no constitution, original constitution, and mapped candidate. Stop if the adapter, envelope, or accounting is invalid.
3. **Dataset build:** create and validate the principle-derived train/validation/held-out files without reading project held-out evaluation material.
4. **Fine-tune:** run one bounded job or adapter training pass. Preserve job ID, hyperparameters, training logs, model ID, cost, and artifact hashes.
5. **Focused comparison:** run the factorial pilot on principle cases, failure cases, matched controls, and untouched sentinels.
6. **Collateral-damage comparison:** run the approved broader development subset against the untuned Mistral baseline. Do not promote a fine-tuned model on a targeted win alone.
7. **Pivot review:** record whether the result supports `continue-mainline`, `add-learned-branch`, `reopen-principle`, `reopen-evaluation`, or `pivot-mainline`, with evidence and uncertainty.

## Hypotheses

Before training, record:

- the expected principle-level gains;
- the expected tradeoffs, including refusal, sycophancy, verbosity, and factuality risks;
- the mechanism by which training is expected to produce the change;
- competing explanations, including prompt formatting, data leakage, sampling, and judge effects;
- the observation that would falsify the hypothesis.

After evaluation, record explanatory hypotheses separately. A gain without the predicted mechanism, or a gain limited to training-like cases, is not evidence of generalization.

The analysis must also track response length, refusal rate, hedge frequency, constitution-specific phrase overlap, sectioning, and direct user agreement. A gain concentrated in style diagnostics is `attribution-unresolved`. A style-matched sham fine-tune is the preferred second experiment but requires its own dataset, preflight, budget, and approval.

## Acceptance criteria

- **XAC1 — Clean separation:** Training, validation, and evaluation data are disjoint and hash-recorded.
- **XAC2 — Reproducible model record:** Base model, fine-tuned model, tokenizer or API version, hyperparameters, job ID, hashes, usage, and cost are recorded.
- **XAC3 — Valid baseline:** Untuned Mistral outputs exist for every comparison case used by the branch; no other model's historical outputs are substituted.
- **XAC4 — Factorial attribution:** The chosen comparison design distinguishes prompt conditioning from fine-tuning, with any reduced design labeled as limited.
- **XAC5 — Principle coverage:** Training and evaluation cover positive cases, counterexamples, boundaries, interactions, and cases requiring uncertainty or correction.
- **XAC6 — No critical regression:** The fine-tuned model introduces no unreviewed critical factual, honesty, safety, over-refusal, or agency regression on the approved comparison set.
- **XAC7 — Generalization:** Any claimed improvement appears on held-out branch cases and is not confined to memorized wording or training-like prompts.
- **XAC8 — Cost integrity:** The job and evaluation remain within the approved ceiling; storage and inference costs are recorded separately from training cost.
- **XAC9 — Pivot decision:** The branch ends with a written recommendation and explicitly states which mainline goals, if any, should be reopened or amended.
- **XAC10 — Family-level isolation:** Family, template, counterfactual-pair, and exact-message leakage checks pass across train, validation, and branch-heldout splits.
- **XAC11 — Predeclared analysis:** All reported claims use the frozen contrasts, feasibility thresholds, uncertainty labels, and style-confound rules in `framework/X001-analysis-contract.md`.
- **XAC12 — Judge integrity:** Primary comparisons are blinded and position-swapped; secondary-judge and human review follow the budget-aware adjudication contract without averaging judges.

## Expected artifacts

- `evals/providers/mistral.py` or equivalent provider adapter;
- `evals/configs/mistral-*.yaml`;
- `evals/datasets/x001-mistral-record-schema.json` and an offline preflight record;
- `evals/configs/x001-semantic-matrix-v1.yaml` and `framework/X001-analysis-contract.md`;
- `evals/datasets/x001-mistral-train.jsonl`;
- `evals/datasets/x001-mistral-validation.jsonl`;
- `evals/manifests/x001-mistral-*.json`;
- `evals/runs/x001-mistral-*/` with raw outputs, scores, usage, and cost;
- `framework/X001-mistral-finetune-analysis.md`;
- `framework/X001-pivot-recommendation.md`;
- updates to `ROADMAP.md`, `BACKLOG.md`, or affected goal contracts only when the evidence warrants them.

## Stop conditions

Stop before training if the exact model is not supported, the dataset is contaminated, semantic families cross splits, the registry hash drifts, target review is incomplete, the price cannot be bounded, or the API/model contract is unclear. Stop after training if the model cannot be evaluated reproducibly, if a critical regression appears, or if attribution remains unresolved after the focused comparison. Route those findings instead of expanding the job or evaluation set.
