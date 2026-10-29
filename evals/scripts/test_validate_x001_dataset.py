#!/usr/bin/env python3
"""Offline contract tests for X001 dataset validation."""
from __future__ import annotations

import copy
import hashlib
import json
import sys
import unittest
from pathlib import Path

import jsonschema
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import validate_x001_dataset as V


class X001DatasetValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.schema = json.loads(V.DEFAULT_SCHEMA.read_text())
        cls.registry_hash = hashlib.sha256(V.DEFAULT_REGISTRY.read_bytes()).hexdigest()

    def record(self, suffix: str, split: str = "train") -> dict:
        return {
            "record_version": "x001-record-v3",
            "constitution_version": "g006-principles-v1",
            "policy_delta_ids": ["G006-P01"],
            "label_method": "human",
            "feedback_model": None,
            "target_revision": "fixture-v1",
            "adjudication_status": "approved",
            "example_id": f"X001-{suffix}",
            "family_id": f"XF-{suffix}",
            "template_id": f"XT-{suffix}",
            "pair_id": None,
            "case_role": "positive_application",
            "principle_ids": ["G006-P01"],
            "mechanism": "Role status is being offered as factual proof.",
            "boundary": "A legitimate conduct control may remain in force.",
            "counterexample": "Relevant expertise may still affect reliability.",
            "interaction_class": "none",
            "coverage_tags": ["evidence_weighting"],
            "protected_dimensions": ["truthfulness", "agency"],
            "scoring_dimensions": ["ER", "AP"],
            "critical_failures": ["CF-01"],
            "reference_facts": [],
            "messages": [
                {"role": "user", "content": f"Prompt {suffix}"},
                {"role": "assistant", "content": f"Reviewed target {suffix}"}
            ],
            "desired_behaviors": ["Separate operational scope from factual warrant."],
            "unacceptable_behaviors": ["Treat role as proof."],
            "split": split,
            "provenance": {
                "source_kind": "principle_registry",
                "source_id": "G006-P01",
                "source_sha256": self.registry_hash,
                "registry_id": "g006-principles-v1",
                "registry_sha256": self.registry_hash,
                "generation_method": "human-authored fixture"
            },
            "review": {"status": "approved", "reviewer_type": "human", "notes": "fixture"}
        }

    def validate(self, records_by_path: list[tuple[Path, list[dict]]]) -> None:
        for _, rows in records_by_path:
            for row in rows:
                jsonschema.validate(row, self.schema)
        V.validate_records(records_by_path, V.DEFAULT_REGISTRY)

    def test_valid_records_pass(self) -> None:
        self.validate([
            (Path("x001-train.jsonl"), [self.record("TRAIN")]),
            (Path("x001-validation.jsonl"), [self.record("VAL", "validation")]),
            (Path("x001-heldout.jsonl"), [self.record("HOLD", "heldout")])
        ])

    def test_real_principle_format_is_required(self) -> None:
        row = self.record("BAD-ID")
        row["principle_ids"] = ["P-01"]
        with self.assertRaises(jsonschema.ValidationError):
            jsonschema.validate(row, self.schema)

    def test_family_cannot_cross_splits(self) -> None:
        train = self.record("FAMILY-A")
        heldout = self.record("FAMILY-B", "heldout")
        heldout["family_id"] = train["family_id"]
        with self.assertRaisesRegex(ValueError, "semantic-family leakage"):
            self.validate([(Path("train.jsonl"), [train]), (Path("heldout.jsonl"), [heldout])])

    def test_exact_messages_cannot_cross_splits(self) -> None:
        train = self.record("MESSAGE-A")
        heldout = self.record("MESSAGE-B", "heldout")
        heldout["messages"] = copy.deepcopy(train["messages"])
        with self.assertRaisesRegex(ValueError, "message duplicate"):
            self.validate([(Path("train.jsonl"), [train]), (Path("heldout.jsonl"), [heldout])])

    def test_final_message_must_be_assistant(self) -> None:
        row = self.record("BAD-TARGET")
        row["messages"][-1]["role"] = "user"
        with self.assertRaisesRegex(ValueError, "final message"):
            self.validate([(Path("train.jsonl"), [row])])

    def test_approved_target_requires_human_review(self) -> None:
        row = self.record("MODEL-ONLY")
        row["review"]["reviewer_type"] = "model_assisted"
        with self.assertRaisesRegex(ValueError, "human review"):
            self.validate([(Path("train.jsonl"), [row])])

    def test_registry_hash_drift_fails(self) -> None:
        row = self.record("HASH-DRIFT")
        row["provenance"]["registry_sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "registry hash drift"):
            self.validate([(Path("train.jsonl"), [row])])

    def test_pair_cannot_cross_splits(self) -> None:
        train = self.record("PAIR-A")
        heldout = self.record("PAIR-B", "heldout")
        train["pair_id"] = "XP-SHARED"
        heldout["pair_id"] = "XP-SHARED"
        with self.assertRaisesRegex(ValueError, "semantic-family leakage"):
            self.validate([(Path("train.jsonl"), [train]), (Path("heldout.jsonl"), [heldout])])

    def test_identity_swap_requires_pair_and_tag(self) -> None:
        row = self.record("IDENTITY")
        row["case_role"] = "identity_or_persona_swap"
        with self.assertRaisesRegex(ValueError, "identity/persona swaps"):
            self.validate([(Path("train.jsonl"), [row])])

    def test_cross_principle_interaction_requires_two_principles(self) -> None:
        row = self.record("INTERACTION")
        row["case_role"] = "interaction"
        row["interaction_class"] = "cross_principle_tension"
        with self.assertRaisesRegex(ValueError, "at least two principles"):
            self.validate([(Path("train.jsonl"), [row])])

    def test_incomplete_profile_fails_coverage(self) -> None:
        row = self.record("TOO-SMALL")
        with self.assertRaisesRegex(ValueError, "requires 120 records"):
            V.enforce_coverage([row], V.DEFAULT_MATRIX, "reduced")

    def test_map_chain_requires_each_role_per_principle(self) -> None:
        row = self.record("MAP-CHAIN")
        matrix = yaml.safe_load(V.DEFAULT_MATRIX.read_text())
        with self.assertRaisesRegex(ValueError, "map chain train/G006-P01 missing roles"):
            V.enforce_map_chain([row], matrix, "fixture")

    def test_tracked_evaluation_prompt_cannot_be_training_input(self) -> None:
        eval_row = json.loads((V.ROOT / "evals/datasets/custom-dev-v1.jsonl").read_text().splitlines()[0])
        row = self.record("EVAL-COPY")
        row["messages"][0]["content"] = eval_row["prompt"]
        with self.assertRaisesRegex(ValueError, "overlaps a tracked evaluation case"):
            self.validate([(Path("train.jsonl"), [row])])


if __name__ == "__main__":
    unittest.main()
