# X001 — Local Mistral SFT Causal Probe

Status: In progress — exploratory branch
Execution stage: Local feasibility and SFT pilot design
Mainline relationship: Non-blocking branch from G006 revision 6
Mainline successor: G007 remains the next numbered goal unless this experiment produces a user-approved roadmap pivot

## Research question

Can constitution-derived supervision be learned into a compatible local Mistral adapter, and does the resulting behavior generalize beyond the training examples while preserving truthfulness, inquiry, agency, and safety?

This branch tests a different intervention from constitutional prompting. It must not be treated as evidence that the constitution improved merely because a fine-tuned model behaves differently.

## Branch rules

- The branch is exploratory and does not change the G001–G010 sequence by itself.
- G006 remains responsible for principle definitions, source replacement, and semantic evaluation contracts.
- The immutable source, frozen G002 manifests, held-out material, and official G010 gates remain unchanged.
- Fine-tuned models are separate experimental artifacts, not replacements for the constitution or the mainline candidate.
- A result may recommend a pivot, reopen a goal, or amend a downstream contract, but roadmap reordering requires explicit user approval.
- The hosted Mistral fine-tuning API is not the execution path: the account's jobs endpoint returned `410 Gone`, and the public fine-tuning documentation is deprecated.
- No local training or paid evaluation runs until a preflight records the exact checkpoint, trainer, hardware, dataset hashes, compute estimate, hard ceiling, and stop condition.
- Proposed initial ceiling: `$10` for one local LoRA/SFT pilot and its approved evaluation; this is a planning value, not authorization to spend.

## Objective

Build and evaluate one bounded local LoRA/SFT branch using policy-versioned, principle-derived training data and a clean held-out comparison. Determine whether the complete SFT package produces durable semantic behavior, merely teaches response style, or introduces material regressions. Defer preference optimization/RLAIF to a separately designed experiment.

## In scope

- Exact local checkpoint, tokenizer, trainer, hardware, seed, and adapter recording.
- A principle-derived training dataset separate from the 160-case evaluation set.
- Training, validation, and held-out splits with no case or output leakage.
- One small supervised LoRA adapter, subject to the approved compute ceiling.
- Prompt-conditioned and SFT-adapted comparison arms.
- Constitution-version and policy-delta lineage for every target, plus a pre-training label-churn report.
- An optional style-matched sham adapter only as a separately approved attribution control.
- Principle, truthfulness, uncertainty, sycophancy, honesty, safety, refusal, and agency metrics.
- Analysis of whether behavior persists without the constitution in the prompt.
- A pivot recommendation for the mainline roadmap and a decision on whether preference optimization merits a separate experiment.

## Out of scope

- Training on the frozen evaluation cases or held-out material.
- Replacing G006's principle registry or the immutable source with learned weights.
- Claiming that a fine-tuned model validates the constitution without a separate prompt-only comparison.
- Claiming to have tested a complete RLAIF, DPO, or production alignment pipeline.
- Publishing or deploying the fine-tuned model.
- Reordering G007–G010 without explicit user approval.

## Required comparison design

The preferred design is a two-by-three factorial comparison:

| Model state | Prompt condition |
| --- | --- |
| Untuned Mistral | No constitution |
| Untuned Mistral | Original constitution |
| Untuned Mistral | Mapped candidate constitution |
| SFT-adapted local Mistral | No constitution |
| SFT-adapted local Mistral | Original constitution |
| SFT-adapted local Mistral | Mapped candidate constitution |

If budget requires a reduced pilot, run these four arms first: untuned/no constitution, untuned/candidate, SFT/no constitution, and SFT/candidate. Label the reduced design exploratory because it cannot fully separate original-constitution effects from SFT effects. A style-matched sham adapter is more valuable for causal attribution than adding a preference stage to this first pilot.

The Mistral base arm must be generated on Mistral. DeepSeek historical outputs cannot serve as Mistral's baseline.

The contrasts and their interpretation are frozen in `framework/X001-analysis-contract.md` before dataset authoring. The primary test is SFT-adapted versus untuned local Mistral with no constitution (`F0 − U0`); prompt-only, conflict, compatibility, and interaction contrasts remain separate. Without a sham adapter, any causal claim is limited to the complete SFT package rather than principle content alone.

## Training-data contract

Training examples must be derived from the principle registry, not copied from the evaluation set. Each example records:

- `example_id`, `family_id`, `template_id`, optional `pair_id`, and `principle_ids`;
- `constitution_version`, `policy_delta_ids`, `label_method`, `feedback_model`, `target_revision`, and `adjudication_status`;
- a controlled case role, mechanism, boundary, counterexample, and interaction class;
- coverage tags and protected regression dimensions;
- judge-side scoring dimensions, applicable critical failures, and reference facts;
- prompt and evidence packet, where applicable;
- desired behavioral properties and unacceptable behaviors;
- a human-reviewed target response for the initial SFT job; preference records and RLAIF targets require a later schema and separately approved training method;
- train, validation, or held-out split;
- provenance, source hash, and generation method.

Judge-generated examples may assist drafting but cannot be the sole source of targets. The dataset must contain matched controls, identity-swapped or persona-neutral variants, uncertainty cases, and cases where the correct behavior is to update, disagree, disclose a limitation, or say that the answer is unknown.

Split assignment occurs at the semantic-family level. A `family_id`, `template_id`, non-null `pair_id`, or exact model-visible message sequence may appear in only one split. Surface paraphrases, identity swaps, counterfactual pairs, and difficulty variants from one family stay together. The controlled coverage floors are defined in `evals/configs/x001-semantic-matrix-v1.yaml`; they are not a demand to populate every Cartesian product.

### Initial data target

The first bounded dataset target is 300 train examples, 60 validation examples, and 100 branch-held-out examples. These are planning targets, not permission to fabricate examples or to train before the principle registry and review process exist. A smaller pilot may use 120/30/40 when the target quality is unchanged and the split remains disjoint.

The 30 custom development cases, 40 deterministic fixtures, 160-case evaluation manifest, and project held-out cases are coverage references only. They are not training records and must not be copied into the fine-tuning upload. Their role is to guide principle-balanced example design and later measure generalization.

### Current checkpoint

The offline contracts are ready. A read-only account check exposed `ministral-8b-2512` with a fine-tuning capability flag, but the account's fine-tuning jobs endpoint returned `410 Gone`; hosted fine-tuning is therefore not the execution path. No training records have been approved or uploaded. The next gate is local checkpoint/trainer/hardware compatibility and a bounded compute estimate.

## Execution stages

1. **Local feasibility preflight:** pin a compatible open-weight checkpoint, tokenizer, trainer, hardware/runtime, seed, license, compute estimate, and hard ceiling.
2. **Untuned smoke:** run a small balanced development subset with no constitution, original constitution, and mapped candidate. Stop if the local envelope, tokenizer, or accounting is invalid.
3. **Policy/data build:** create and validate policy-versioned train/validation/held-out files, calculate label churn, and keep evaluation material out of training.
4. **SFT adapter:** run one bounded local LoRA/SFT pass. Preserve checkpoint, trainer, hyperparameters, seed, logs, adapter hash, and compute cost.
5. **Focused comparison:** run the factorial pilot on principle cases, failure cases, matched controls, and untouched sentinels.
6. **Collateral-damage comparison:** run the approved broader development subset against the untuned local baseline. Do not promote an adapter on a targeted win alone.
7. **Optional attribution control:** run a separately approved style-matched sham adapter if the initial result warrants stronger causal attribution.
8. **Pivot review:** record whether the result supports `continue-mainline`, `add-learned-branch`, `reopen-principle`, `reopen-evaluation`, `design-preference-stage`, or `pivot-mainline`, with evidence and uncertainty.

## Hypotheses

Before training, record:

- the expected principle-level gains;
- the expected tradeoffs, including refusal, sycophancy, verbosity, and factuality risks;
- the mechanism by which training is expected to produce the change;
- the expected label churn under the constitution delta and which strata should remain unchanged;
- competing explanations, including prompt formatting, data leakage, sampling, and judge effects;
- the observation that would falsify the hypothesis.

After evaluation, record explanatory hypotheses separately. A gain without the predicted mechanism, or a gain limited to training-like cases, is not evidence of generalization.

The analysis must also track response length, refusal rate, hedge frequency, constitution-specific phrase overlap, sectioning, direct user agreement, and policy-label churn. A gain concentrated in style diagnostics is `attribution-unresolved`. Preference optimization/RLAIF is not part of this first result; a later stage requires its own data schema, arms, preflight, budget, and approval.

## Acceptance criteria

- **XAC1 — Clean separation:** Training, validation, and evaluation data are disjoint and hash-recorded.
- **XAC2 — Reproducible model record:** Base checkpoint, adapter, tokenizer, trainer/runtime, hardware, seed, hyperparameters, hashes, usage, and compute cost are recorded.
- **XAC3 — Valid baseline:** Untuned Mistral outputs exist for every comparison case used by the branch; no other model's historical outputs are substituted.
- **XAC4 — SFT attribution:** The chosen comparison design distinguishes prompt conditioning from the SFT package, with any reduced design labeled as limited and sham absence reported.
- **XAC5 — Principle coverage:** Training and evaluation cover positive cases, counterexamples, boundaries, interactions, and cases requiring uncertainty or correction.
- **XAC6 — No critical regression:** The fine-tuned model introduces no unreviewed critical factual, honesty, safety, over-refusal, or agency regression on the approved comparison set.
- **XAC7 — Generalization:** Any claimed improvement appears on held-out branch cases and is not confined to memorized wording or training-like prompts.
- **XAC8 — Cost integrity:** Local compute and evaluation remain within the approved ceiling; training, storage, and inference costs are recorded separately.
- **XAC9 — Pivot decision:** The branch ends with a written recommendation and explicitly states which mainline goals, if any, should be reopened or amended.
- **XAC10 — Family-level isolation:** Family, template, counterfactual-pair, and exact-message leakage checks pass across train, validation, and branch-heldout splits.
- **XAC11 — Predeclared analysis:** All reported claims use the frozen contrasts, feasibility thresholds, uncertainty labels, and style-confound rules in `framework/X001-analysis-contract.md`.
- **XAC12 — Judge integrity:** Primary comparisons are blinded and position-swapped; secondary-judge and human review follow the budget-aware adjudication contract without averaging judges.
- **XAC13 — Policy lineage:** Every training and evaluation target carries a constitution version, applicable policy delta, label method, and review status; label-churn results are preserved before training.

## Expected artifacts

- local trainer/checkpoint configuration and runtime record;
- `evals/configs/x001-local-sft-*.yaml`;
- `evals/datasets/x001-mistral-record-schema.json` and an offline preflight record;
- `evals/configs/x001-semantic-matrix-v1.yaml` and `framework/X001-analysis-contract.md`;
- `evals/datasets/x001-mistral-train.jsonl`;
- `evals/datasets/x001-mistral-validation.jsonl`;
- `evals/manifests/x001-local-sft-*.json`;
- `evals/runs/x001-local-sft-*/` with raw outputs, scores, usage, and compute cost;
- a policy-delta impact and label-churn report;
- `framework/X001-mistral-finetune-analysis.md`;
- `framework/X001-pivot-recommendation.md`;
- updates to `ROADMAP.md`, `BACKLOG.md`, or affected goal contracts only when the evidence warrants them.

## Stop conditions

Stop before training if the checkpoint/trainer is incompatible, local compute cannot be bounded, the dataset is contaminated, semantic families cross splits, the registry or constitution hash drifts, target review is incomplete, policy lineage is missing, or the runtime contract is unclear. Stop after training if the adapter cannot be evaluated reproducibly or if a critical regression appears. Route unresolved attribution as a limitation or future sham/preference experiment instead of expanding the run.
