# X001 local feasibility record

Date: 2026-10-14
Purpose: Record the bounded local runtime smoke test before any policy dataset or evaluation claim.

## Result

**Pass: local LoRA/SFT execution is feasible on the available machine.** The test trained a one-layer LoRA adapter on two tiny serialized examples, evaluated after each of two updates, saved an adapter, loaded that adapter, and generated a coherent answer to a new prompt.

This is only runtime evidence. It does not show that the constitution was learned, that the adapter generalizes, or that it improves any evaluation metric.

## Pinned runtime

- Checkpoint: `mlx-community/Ministral-3-3B-Base-2512-4bit`
- Checkpoint revision: `853f50105f14039a2acba1d9d380efdecc674dd4`
- Runtime: MLX-LM `0.31.3`, MLX `0.32.3`
- Hardware: Apple M1 Pro, 16 GB unified memory, arm64
- Fine-tune type: LoRA
- Seed: `0`
- Layers: `1`
- Iterations: `2`
- Batch size: `1`
- Maximum sequence length: `256`
- Learning rate: `1e-5` (MLX-LM default)

## Data-format finding

The checkpoint has no tokenizer chat template. Passing canonical `messages` records directly to MLX-LM failed before training with:

`ValueError: Cannot use chat template functions because tokenizer.chat_template is not set and no template argument was passed!`

The smoke test therefore used an explicit plain-text view with `User:` and `Assistant:` delimiters. The canonical X001 records remain message-based and policy-versioned. The serializer is `evals/scripts/serialize_x001_for_mlx.py` (`x001-mlx-text-v1`): it emits MLX's `{"text": ...}` rows and a separate lineage manifest mapping each output line back to the complete source record and policy metadata. The two-line smoke fixture is not a substitute for the v3 training-record contract.

## Observed metrics

- Train loss: `4.360` at iteration 1; `4.016` at iteration 2
- Validation loss: `4.039` at iteration 1; `4.018` at iteration 2
- Peak memory: `2.204 GB` during training; `2.038 GB` during adapted inference
- Adapter file: temporary `/private/tmp/x001-local-sft-adapter-text/adapters.safetensors`
- Adapter SHA-256: `b49261dc4b43399e86bf9f2157a9e9cbdb96de970568570582d942339a17610f`
- Smoke train SHA-256: `5bb514f2c4bf722fbbd8927993f811b8023c36093fa97c3c9aeb0755edaa3164`
- Smoke validation SHA-256: `dcdb4201f08c0ed68c2a32dce3771483a7538bc56371f83cffd581ce38540de6`

The tokenizer emitted a warning about an incorrect Mistral regex pattern and recommended `fix_mistral_regex=True`. This is a reproducibility risk that must be resolved or explicitly pinned before the real pilot.

## Next gate

1. Define and test the deterministic canonical-record serializer, including its version and hash.
2. Select the exact tokenizer-loading fix or pin the observed tokenizer behavior.
3. Create a reviewed, policy-versioned pilot dataset from the X001 schema; keep the frozen evaluation material out of it.
4. Run the validator, label-churn report, and split-isolation checks before requesting the bounded SFT pilot.
