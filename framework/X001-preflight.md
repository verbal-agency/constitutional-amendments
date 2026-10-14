# X001 offline preflight

Status: blocked before paid execution
Date: 2026-10-13
Branch: Mistral fine-tuning experiment, non-blocking from G006 revision 6

## What is ready

- The branch contract is active in `goals/X001-mistral-finetune-experiment.md`.
- The proposed provider adapter is `evals/providers/mistral.py`.
- The offline configuration is `evals/configs/x001-mistral-v1.yaml`.
- The v2 training-record contract is `evals/datasets/x001-mistral-record-schema.json`.
- The semantic coverage contract is `evals/configs/x001-semantic-matrix-v1.yaml`.
- The predeclared contrasts and judging rules are in `framework/X001-analysis-contract.md`.
- The planned factorial comparison is untuned/fine-tuned crossed with no constitution/original/mapped candidate.
- The initial data target is 300 train, 60 validation, and 100 branch-held-out records. A reduced 120/30/40 pilot is allowed only if it preserves the same review and split rules.

## Evidence checked

| Check | Result | Evidence |
| --- | --- | --- |
| Principle registry exists | **Pass** | `framework/principles-v1.yaml`, registry `g006-principles-v1`, SHA-256 `4209f05fb5fc46528de664e283f0a9541246a5fbbd3eeab2cd707dfe4211fe7f` |
| Training data is separate from evaluation data | Ready by contract | X001 schema and matrix forbid evaluation reuse; the validator rejects tracked development/public text overlap and semantic-family leakage without reading private held-out material |
| Dataset validation contract | **Pass** | Schema v2, registry/config hash consistency, message targets, review authority, semantic roles, split isolation, and coverage failures pass 12 offline tests |
| Analysis contract | **Pass** | Six arms, primary and secondary contrasts, feasibility thresholds, uncertainty labels, style confounds, and judge adjudication are predeclared |
| Development evaluation coverage | Available | 30 custom development cases; 40 deterministic fixtures; 160-case lean manifest |
| Held-out evaluation material | Protected | `evals/private/` remains excluded and is not used for dataset construction |
| Mistral adapter | Ready offline | Importable adapter with explicit model, key, endpoint, and usage normalization |
| Exact model eligibility | **Pending** | Requires account-scoped `/v1/models` and fine-tuning eligibility check |
| Mistral API credential available | **Blocked** | The ignored `.env` currently contains `DEEPSEEK_KEY` and `OPEN_AI_KEY`, but no `MISTRAL_API_KEY`; the adapter made no request |
| Exact fine-tuning price | **Pending** | Must be recorded from the account/provider before a job is approved |
| Paid authorization | Not granted by this artifact | The proposed `$10` ceiling is a planning value, not approval |

## Why training is stopped now

The principle registry and offline data contracts are now ready. Training remains stopped because the account-scoped model eligibility and price are unconfirmed, no reviewed dataset exists yet, and no paid job has been approved.

The account-scoped check was attempted on 2026-10-13 and stopped locally because the required credential was absent. No request was sent and no provider state was changed.

## Next safe step

1. Provide `MISTRAL_API_KEY` in the ignored environment, then run the adapter's account-scoped model and fine-tuning preflight, recording only model metadata, eligibility, price basis, and hashes.
2. Draft a small reviewed batch against schema v2, validate message structure and registry provenance, and inspect semantic-family leakage.
3. Expand only after the sample passes the selected semantic-matrix profile; then lock and hash the branch-heldout split.
4. Request separate approval for one bounded training job and any evaluation calls.

No paid request was made while producing this record.
