# X001 local SFT preflight

Status: local runtime preflight passed; policy-data gate pending
Date: 2026-10-15
Branch: Local Mistral SFT news depolarization probe, non-blocking from G006 revision 6

Primary applied target: evidence-centered news depolarization under `framework/X001-news-depolarization-contract.md`.

## What is ready

- The branch contract is active in `goals/X001-mistral-finetune-experiment.md`.
- The hosted provider check is retained as evidence only; it is not the execution path.
- The local runtime is pinned in `framework/X001-local-feasibility-record.md`; the unsandboxed preflight loaded the pinned checkpoint and completed a one-token generation with the pinned tokenizer setting.
- The v3 training-record contract is `evals/datasets/x001-mistral-record-schema.json`.
- The semantic coverage contract is `evals/configs/x001-semantic-matrix-v1.yaml`.
- The predeclared contrasts and judging rules are in `framework/X001-analysis-contract.md`.
- The source-packet machinery is validated, and the three LeBron/Jordan held-out calibration packets are human-approved in `evals/datasets/x001-source-packets.jsonl`.
- No policy-derived train, validation, or branch-heldout records exist yet; the approved calibration packets are evaluation material, not training data.
- The planned factorial comparison is untuned/SFT-adapted crossed with no constitution/original/mapped candidate.
- The initial data target is 300 train, 60 validation, and 100 branch-held-out records. A reduced 120/30/40 pilot is allowed only if it preserves the same review and split rules.

## Evidence checked

| Check | Result | Evidence |
| --- | --- | --- |
| Principle registry exists | **Pass** | `framework/principles-v1.yaml`, registry `g006-principles-v1`, SHA-256 `4209f05fb5fc46528de664e283f0a9541246a5fbbd3eeab2cd707dfe4211fe7f` |
| Training data is separate from evaluation data | **Not yet exercised** | X001 schema and matrix forbid evaluation reuse; no policy train/validation files have been created; the validator rejects tracked development/public text overlap and semantic-family leakage without reading private held-out material |
| Dataset validation contract | **Pass for empty contract** | Schema v3, registry/config hash consistency, policy lineage, message targets, review authority, semantic roles, split isolation, and coverage checks pass the offline validator and tests; no real policy records are available to validate |
| Analysis contract | **Pass** | Six arms, primary and secondary contrasts, feasibility thresholds, uncertainty labels, style confounds, and judge adjudication are predeclared |
| Development evaluation coverage | Available | 30 custom development cases; 40 deterministic fixtures; 160-case lean manifest |
| Held-out evaluation material | Protected | `evals/private/` remains excluded and is not used for dataset construction |
| Account-visible Mistral model | **Observed** | Read-only `/v1/models` exposed `ministral-8b-2512` with a `fine_tuning` capability flag and 262,144-token context |
| Hosted fine-tuning jobs API | **Blocked** | Read-only `GET /v1/fine_tuning/jobs` returned HTTP `410 Gone`; hosted fine-tuning is not the execution path |
| Local checkpoint/trainer | **Pass** | MLX-LM `0.31.3` loaded `mlx-community/Ministral-3-3B-Base-2512-4bit` at revision `853f50105f14039a2acba1d9d380efdecc674dd4`; a one-token local generation completed successfully in the Metal-capable runtime |
| Local compute estimate | **Pass for smoke; pilot estimate pending** | M1 Pro/16 GB; 2-example smoke peaked at 2.204 GB. The full pilot still needs a token estimate and hard ceiling |
| Canonical-to-trainer serialization | **Pass** | `evals/scripts/serialize_x001_for_mlx.py` is versioned as `x001-mlx-text-v1`; serializer tests pass and the source-packet renderer is separately versioned as `x001-source-packet-render-v1` |
| Tokenizer reproducibility | **Pass** | `fix_mistral_regex=True` loads the pinned tokenizer; tokenizer config SHA-256 is `f3a437d1214f6b61c8eae19d1256b0ebbf567793f6dcc1f63f4a30b829f85235`; the checkpoint has no chat template, so the versioned plain-text serializer remains required |
| Paid authorization | Not granted by this artifact | The proposed `$10` ceiling is a planning value, not approval |

## Why training is stopped now

The principle registry, source-packet contracts, deterministic serializers, and local runtime preflight are ready. The policy pilot remains stopped because no policy train/validation records exist and the full-pilot compute estimate is still pending.

The account-scoped model check was completed read-only on 2026-10-14. The model capability flag is not treated as sufficient because the fine-tuning jobs endpoint returned `410 Gone`. No file was uploaded and no training or inference call was made.

## Next safe step

1. Record a full-pilot token estimate and hard ceiling; stop if the pilot cannot fit the proposed `$10` ceiling.
2. Draft a small reviewed, policy-versioned train/validation batch against schema v3, calculate label churn, validate registry provenance, and inspect semantic-family leakage.
3. Expand only after the sample passes the selected semantic-matrix profile; then lock and hash the branch-heldout split.
4. Request separate approval for one bounded local SFT run and its evaluation calls.

No paid request was made while producing this record. The local smoke used no API calls.
