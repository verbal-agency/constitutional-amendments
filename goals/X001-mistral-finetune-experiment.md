# X001 — Local Mistral SFT News Depolarization Probe

Status: Planned — exploratory branch; bounded target-authoring slice pending
Execution stage: Local feasibility passed; evidence-centered news dataset and SFT pilot design
Mainline relationship: Non-blocking branch from G006 revision 6
Mainline successor: G007 remains the next numbered goal unless this experiment produces a user-approved roadmap pivot

## Research question

Can constitution-derived supervision be learned into a compatible local Mistral adapter that produces evidence-centered news briefings, and does the resulting behavior generalize beyond the training examples while preserving truthfulness, factual asymmetry, inquiry, agency, and safety?

This branch tests a different intervention from constitutional prompting. It must not be treated as evidence that the constitution improved merely because a fine-tuned model behaves differently.

## Primary applied target

The first practical target is an evidence-centered news depolarizer. Given a frozen packet of reporting and primary evidence, the model should separate facts, inference, values, provenance, incentives, and consequential unknowns; reduce gratuitous identity-driven framing; preserve unequal evidentiary support; and leave conclusions and value tradeoffs to the user.

Depolarization does not mean political centrism, equal treatment of unequal claims, emotional sanitization, or persuasion toward a preferred belief. The complete task, packet, dataset, comparison, and decision contract is `framework/X001-news-depolarization-contract.md`.

The first calibration family is the LeBron James versus Michael Jordan GOAT debate. It is a low-stakes sports domain used to test evidence/value separation and identity-pressure handling before collecting higher-stakes news packets. The three initial packets are human-approved held-out calibration material and remain outside training data.

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

Build and evaluate one bounded local LoRA/SFT branch using policy-versioned, principle-derived source-packet training data and a clean held-out comparison. Determine whether the complete SFT package produces useful evidence-centered news analysis, merely teaches a neutral-sounding response style, can be replaced by a strong prompt, or introduces material regressions. Defer preference optimization/RLAIF to a separately designed experiment.

## Rescue slice

The branch is narrowed before further execution. Its next slice is target authoring and preflight, not model training.

- **Primary owner:** X001. G006 owns the upstream principle and replacement contracts; X001 consumes them.
- **Consumer:** the bounded local SFT preflight and later adapter comparison.
- **Current slice:** author and review target records for the approved eight-packet applied news wave, validate split and lineage fields, and record the bounded local compute estimate.
- **Hypothesis:** reviewed target records can be created from the approved packets without evaluation leakage, while preserving principle lineage and the evidence-centered news contract.
- **Closure criteria:** (1) target records pass schema, family-isolation, and source-packet validation; (2) train, validation, and branch-heldout hashes and counts are recorded; (3) every target has constitution/policy lineage and review status; (4) the local training/evaluation preflight records checkpoint, runtime, ceiling, and stop condition.
- **Deferred:** LoRA/SFT training, focused comparison, sham adapter, frontier reference, and pivot classification remain later slices and are not authorized by this rescue.

The broader acceptance table below remains the experiment-level contract. The four criteria above govern the next bounded slice.

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
- A source-packet news slice with event-family isolation, factual review, false-balance traps, and matched framing variants.
- A strong-prompt control and one separately approved frontier-model reference for practical usefulness.
- A pivot recommendation for the mainline roadmap and a decision on whether preference optimization merits a separate experiment.

## Out of scope

- Training on the frozen evaluation cases or held-out material.
- Replacing G006's principle registry or the immutable source with learned weights.
- Claiming that a fine-tuned model validates the constitution without a separate prompt-only comparison.
- Claiming to have tested a complete RLAIF, DPO, or production alignment pipeline.
- Publishing or deploying the fine-tuned model.
- Autonomous news retrieval, live-feed ranking, personalized political persuasion, or claims of independent verification.
- Treating a politically moderate tone as evidence of accuracy or depolarization.
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

For the primary applied target, source packets, target-authoring procedure, topic-family isolation, real-versus-synthetic boundaries, and practical comparison arms follow `framework/X001-news-depolarization-contract.md`. At least 60% of each reduced-profile split is source-packet news analysis; the remainder tests whether the same principles transfer outside the news format.

Split assignment occurs at the semantic-family level. A `family_id`, `template_id`, non-null `pair_id`, or exact model-visible message sequence may appear in only one split. Surface paraphrases, identity swaps, counterfactual pairs, and difficulty variants from one family stay together. The controlled coverage floors are defined in `evals/configs/x001-semantic-matrix-v1.yaml`; they are not a demand to populate every Cartesian product.

### Initial data target

The first bounded dataset target is 300 train examples, 60 validation examples, and 100 branch-held-out examples. These are planning targets, not permission to fabricate examples or to train before the principle registry and review process exist. A smaller pilot may use 120/30/40 when the target quality is unchanged and the split remains disjoint.

The 30 custom development cases, 40 deterministic fixtures, 160-case evaluation manifest, and project held-out cases are coverage references only. They are not training records and must not be copied into the fine-tuning upload. Their role is to guide principle-balanced example design and later measure generalization.

### Current checkpoint

The offline contracts, local runtime smoke, source-packet schema, deterministic renderer, and validators are ready. MLX-LM previously trained and loaded a tiny LoRA adapter for the pinned 3B checkpoint; this establishes runtime feasibility only. The three calibration packets are human-approved and remain held out. The 11-record process batch and expansion wave 1 are human-approved and have passed serialization; the eight-packet applied news wave is also approved, but its target records still need authoring. The next gate is creating those records and recording the bounded compute estimate.

## Execution stages

1. **Local feasibility preflight:** pin a compatible open-weight checkpoint, tokenizer, trainer, hardware/runtime, seed, license, compute estimate, and hard ceiling.
2. **Untuned smoke:** run a small balanced development subset with no constitution, original constitution, and mapped candidate. Stop if the local envelope, tokenizer, or accounting is invalid.
3. **Source-packet and policy/data build:** freeze reviewed news packets, create policy-versioned train/validation/held-out files, calculate label churn, and keep evaluation material out of training.
4. **SFT adapter:** run one bounded local LoRA/SFT pass. Preserve checkpoint, trainer, hyperparameters, seed, logs, adapter hash, and compute cost.
5. **Focused comparison:** run the factorial pilot on principle cases, news packets, false-balance traps, matched framings, failure cases, and untouched sentinels.
6. **Collateral-damage comparison:** run the approved broader development subset against the untuned local baseline. Do not promote an adapter on a targeted win alone.
7. **Optional attribution control:** run a separately approved style-matched sham adapter if the initial result warrants stronger causal attribution.
8. **Practical reference:** after freezing the local candidate, compare it blind with the untuned strong-prompt control and one approved frontier reference on the same source packets.
9. **Pivot review:** classify the product result as `useful-specialist`, `prompt-sufficient`, `research-only`, `revise-data-or-principles`, or `stop`, then record any mainline recommendation with evidence and uncertainty.

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
- **XAC5 — Principle coverage:** The semantic-matrix validator proves the epistemological-map chain for every registry principle in train, validation, and branch-heldout: policy delta, mechanism, boundary, counterexample, desired/unacceptable behavior, scoring dimension, and positive, exception, overapplication, and counterexample roles.
- **XAC6 — No critical regression:** The fine-tuned model introduces no unreviewed critical factual, honesty, safety, over-refusal, or agency regression on the approved comparison set.
- **XAC7 — Generalization:** Any claimed improvement appears on held-out branch cases and is not confined to memorized wording or training-like prompts.
- **XAC8 — Cost integrity:** Local compute and evaluation remain within the approved ceiling; training, storage, and inference costs are recorded separately.
- **XAC9 — Pivot decision:** The branch ends with a written recommendation and explicitly states which mainline goals, if any, should be reopened or amended.
- **XAC10 — Family-level isolation:** Family, template, counterfactual-pair, and exact-message leakage checks pass across train, validation, and branch-heldout splits.
- **XAC11 — Predeclared analysis:** All reported claims use the frozen contrasts, feasibility thresholds, uncertainty labels, and style-confound rules in `framework/X001-analysis-contract.md`.
- **XAC12 — Judge integrity:** Primary comparisons are blinded and position-swapped; secondary-judge and human review follow the budget-aware adjudication contract without averaging judges.
- **XAC13 — Policy lineage:** Every training and evaluation target carries a constitution version, applicable policy delta, label method, and review status; label-churn results are preserved before training.
- **XAC14 — Applied behavior:** Held-out news outputs separate facts, inference, values, provenance, and unknowns while preserving material evidentiary asymmetry.
- **XAC15 — No false depolarization:** No promoted result relies on false balance, tone-only neutrality, evidence suppression, covert persuasion, or irrelevant identity-conditioned treatment.
- **XAC16 — Prompt necessity:** The strong-prompt untuned control is run and the analysis states whether fine-tuning adds behavior beyond prompting.
- **XAC17 — Practical comparison:** Any claim of benefit over ChatGPT or Claude uses a pinned, separately approved frontier reference and blind user review on identical frozen packets.
- **XAC18 — Source integrity:** Every real packet has dates, source/use provenance, hashes, claim typing, a cutoff, factual review, and event-family split isolation; synthetic variants remain explicitly labeled.

### Applied-target evidence map

| Criterion | Required evidence |
| --- | --- |
| XAC14 | Held-out item scores and paired outputs for all ten news dimensions |
| XAC15 | False-balance, identity-swap, framing, and critical-failure results |
| XAC16 | Tuned-minimal versus untuned-minimal and untuned-strong-prompt contrasts |
| XAC17 | Pinned frontier run record, cost ledger, blind ordering, and user-usefulness form |
| XAC18 | Packet manifest validation, hashes, review status, and split-isolation report |

## Expected artifacts

- local trainer/checkpoint configuration and runtime record;
- `evals/configs/x001-local-sft-*.yaml`;
- `evals/datasets/x001-mistral-record-schema.json` and an offline preflight record;
- `evals/configs/x001-semantic-matrix-v1.yaml` and `framework/X001-analysis-contract.md`;
- `framework/X001-news-depolarization-contract.md` and `evals/configs/x001-news-depolarization-v1.yaml`;
- `framework/X001-dataset-expansion-plan.md` and the versioned process-batch expansion wave;
- `evals/datasets/x001-source-packet-schema.json`, reviewed source-packet manifest, deterministic renderer, validator, and tests;
- `evals/datasets/x001-mistral-train.jsonl`;
- `evals/datasets/x001-mistral-validation.jsonl`;
- `evals/manifests/x001-local-sft-*.json`;
- `evals/runs/x001-local-sft-*/` with raw outputs, scores, usage, and compute cost;
- a policy-delta impact and label-churn report;
- `framework/X001-mistral-finetune-analysis.md`;
- `framework/X001-news-depolarization-analysis.md` and blind usefulness review;
- `framework/X001-pivot-recommendation.md`;
- updates to `ROADMAP.md`, `BACKLOG.md`, or affected goal contracts only when the evidence warrants them.

## Stop conditions

Stop before training if the checkpoint/trainer is incompatible, local compute cannot be bounded, the dataset is contaminated, semantic families cross splits, the epistemological-map coverage gate fails, the registry or constitution hash drifts, target review is incomplete, policy lineage is missing, or the runtime contract is unclear. Stop after training if the adapter cannot be evaluated reproducibly or if a critical regression appears. Route unresolved attribution as a limitation or future sham/preference experiment instead of expanding the run.
