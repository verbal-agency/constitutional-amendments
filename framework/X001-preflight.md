# X001 offline preflight

Status: blocked before paid execution
Date: 2026-10-13
Branch: Mistral fine-tuning experiment, non-blocking from G006 revision 6

## What is ready

- The branch contract is active in `goals/X001-mistral-finetune-experiment.md`.
- The proposed provider adapter is `evals/providers/mistral.py`.
- The offline configuration is `evals/configs/x001-mistral-v1.yaml`.
- The training-record contract is `evals/datasets/x001-mistral-record-schema.json`.
- The planned factorial comparison is untuned/fine-tuned crossed with no constitution/original/mapped candidate.
- The initial data target is 300 train, 60 validation, and 100 branch-held-out records. A reduced 120/30/40 pilot is allowed only if it preserves the same review and split rules.

## Evidence checked

| Check | Result | Evidence |
| --- | --- | --- |
| Principle registry exists | **Fail** | `framework/principles-v1.yaml` is absent |
| Training data is separate from evaluation data | Ready by contract | X001 schema and config explicitly reject evaluation manifests as training data |
| Development evaluation coverage | Available | 30 custom development cases; 40 deterministic fixtures; 160-case lean manifest |
| Held-out evaluation material | Protected | `evals/private/` remains excluded and is not used for dataset construction |
| Mistral adapter | Ready offline | Importable adapter with explicit model, key, endpoint, and usage normalization |
| Exact model eligibility | **Pending** | Requires account-scoped `/v1/models` and fine-tuning eligibility check |
| Exact fine-tuning price | **Pending** | Must be recorded from the account/provider before a job is approved |
| Paid authorization | Not granted by this artifact | The proposed `$10` ceiling is a planning value, not approval |

## Why training is stopped now

Without the principle registry, there is no defensible source for principle-derived targets. Creating examples from the constitution text, evaluation cases, or model guesses would mix the intervention with the data source and make later attribution weak. Without an account-scoped eligibility and price check, the base model and the job cost are also not bounded.

## Next safe step

1. Create or restore `framework/principles-v1.yaml` from the accepted G003/G006 principle contracts.
2. Run the adapter's account-scoped model and fine-tuning preflight, recording only model metadata, eligibility, price basis, and hashes.
3. Draft a small reviewed batch against the schema, validate it, and inspect leakage before expanding toward the target counts.
4. Request separate approval for one bounded training job and any evaluation calls.

No paid request was made while producing this record.
