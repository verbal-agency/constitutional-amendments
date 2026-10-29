# X001 dataset expansion plan

## Purpose

The approved 11-record process batch proves the record, review, provenance, split, and MLX serialization machinery. It is not large enough to support a behavioral claim. This plan expands the data toward the reduced pilot without treating synthetic drafts as training-ready before human review.

## Current state

- Base process batch: 7 approved train records and 4 approved validation records.
- Serializer proof: `evals/runs/x001-process-batch-20261021/` contains 7 train and 4 validation MLX-text rows plus lineage manifests.
- Process expansion wave 1: 9 train and 4 validation records, all human-approved and serialized, in separate files with disjoint families.
- News packet wave 1: 6 train and 2 validation source packets, pending human factual and task review, in `evals/datasets/x001-source-packets-news-wave1-v1.jsonl`.
- The three LeBron–Jordan source packets remain held out and are not reused for training.

## Reduced-pilot target

The target remains 120 train, 30 validation, and 40 branch-heldout records. At least 60% of each reduced-profile split should be source-packet news analysis; process cases supply transfer and regression coverage, not the majority of the applied dataset.

## Waves

1. **Machinery proof:** serialize the 11 approved base records, verify line counts and lineage, and confirm pending records are rejected.
2. **Process expansion wave 1:** review the 12 new records; preserve identity pairs, interaction cases, uncertainty cases, and source-provenance boundaries as separate families.
3. **Source-packet wave:** review the eight new LeBron–Jordan packets with factual review, claim typing, cutoff dates, and family-level isolation. Do not reuse the three held-out calibration packets. Later waves can add other news topics.
4. **Reduced pilot fill:** reach 120/30/40 only after the reviewed wave passes semantic coverage and leakage checks.

The semantic coverage check is now an executable epistemological-map gate, not a count-only review. Before serialization, run `python3 evals/scripts/validate_x001_dataset.py --profile reduced ...` and require every registry principle to have its policy delta, mechanism, boundary, counterexample, desired/unacceptable behaviors, scoring dimension, and positive, legitimate-exception, overapplication, and counterexample roles in each split.

## Cross-cutting review gate

Every record must preserve meaningful unknowns as live uncertainty. Reviewers check that the target states material unresolved points, identifies evidence or tests that could update the view, avoids both false certainty and empty agnosticism, and keeps uncertain interim actions proportionate and reversible.

## Stop conditions

Stop expansion if a family crosses splits, the map-chain coverage gate fails, a target is only a surface paraphrase, a source packet lacks provenance or factual review, a pending record is serialized, or the expanded set starts optimizing for coverage counts at the expense of target quality.
