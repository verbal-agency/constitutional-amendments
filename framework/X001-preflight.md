# X001 local SFT preflight

Status: local execution path pending feasibility gate
Date: 2026-10-14
Branch: Local Mistral SFT causal probe, non-blocking from G006 revision 6

## What is ready

- The branch contract is active in `goals/X001-mistral-finetune-experiment.md`.
- The hosted provider check is retained as evidence only; it is not the execution path.
- The local configuration is to be added after checkpoint/trainer selection.
- The v3 training-record contract is `evals/datasets/x001-mistral-record-schema.json`.
- The semantic coverage contract is `evals/configs/x001-semantic-matrix-v1.yaml`.
- The predeclared contrasts and judging rules are in `framework/X001-analysis-contract.md`.
- The planned factorial comparison is untuned/SFT-adapted crossed with no constitution/original/mapped candidate.
- The initial data target is 300 train, 60 validation, and 100 branch-held-out records. A reduced 120/30/40 pilot is allowed only if it preserves the same review and split rules.

## Evidence checked

| Check | Result | Evidence |
| --- | --- | --- |
| Principle registry exists | **Pass** | `framework/principles-v1.yaml`, registry `g006-principles-v1`, SHA-256 `4209f05fb5fc46528de664e283f0a9541246a5fbbd3eeab2cd707dfe4211fe7f` |
| Training data is separate from evaluation data | Ready by contract | X001 schema and matrix forbid evaluation reuse; the validator rejects tracked development/public text overlap and semantic-family leakage without reading private held-out material |
| Dataset validation contract | **Pass** | Schema v3, registry/config hash consistency, policy lineage, message targets, review authority, semantic roles, split isolation, and coverage failures pass 12 offline tests |
| Analysis contract | **Pass** | Six arms, primary and secondary contrasts, feasibility thresholds, uncertainty labels, style confounds, and judge adjudication are predeclared |
| Development evaluation coverage | Available | 30 custom development cases; 40 deterministic fixtures; 160-case lean manifest |
| Held-out evaluation material | Protected | `evals/private/` remains excluded and is not used for dataset construction |
| Account-visible Mistral model | **Observed** | Read-only `/v1/models` exposed `ministral-8b-2512` with a `fine_tuning` capability flag and 262,144-token context |
| Hosted fine-tuning jobs API | **Blocked** | Read-only `GET /v1/fine_tuning/jobs` returned HTTP `410 Gone`; hosted fine-tuning is not the execution path |
| Local checkpoint/trainer | **Pending** | Must select a compatible open-weight checkpoint and reproducible LoRA/SFT runtime |
| Local compute estimate | **Pending** | Must record hardware, runtime, token estimate, ceiling, and stop condition |
| Paid authorization | Not granted by this artifact | The proposed `$10` ceiling is a planning value, not approval |

## Why training is stopped now

The principle registry and offline data contracts are ready. Training remains stopped because no local checkpoint/trainer/hardware combination has been selected, no reviewed dataset exists yet, and no local compute budget has been approved.

The account-scoped model check was completed read-only on 2026-10-14. The model capability flag is not treated as sufficient because the fine-tuning jobs endpoint returned `410 Gone`. No file was uploaded and no training or inference call was made.

## Next safe step

1. Select a compatible open-weight Mistral checkpoint, tokenizer, local trainer, hardware/runtime, seed, and license.
2. Record a local compute estimate and hard ceiling; stop if the pilot cannot fit the approved budget.
3. Draft a small reviewed, policy-versioned batch against schema v3, calculate label churn, validate registry provenance, and inspect semantic-family leakage.
4. Expand only after the sample passes the selected semantic-matrix profile; then lock and hash the branch-heldout split.
5. Request separate approval for one bounded local SFT run and its evaluation calls.

No paid request was made while producing this record.
