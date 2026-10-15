import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from serialize_x001_for_mlx import SERIALIZER_VERSION, serialize_file, serialize_messages


class SerializeX001Tests(unittest.TestCase):
    def test_serializes_roles_in_order(self):
        self.assertEqual(
            serialize_messages(
                [
                    {"role": "system", "content": "Be candid."},
                    {"role": "user", "content": "What is known?"},
                    {"role": "assistant", "content": "The evidence is limited."},
                ]
            ),
            "System: Be candid.\nUser: What is known?\nAssistant: The evidence is limited.",
        )

    def test_rejects_missing_chat_target(self):
        with self.assertRaisesRegex(ValueError, "final message"):
            serialize_messages([{"role": "user", "content": "Question"}, {"role": "user", "content": "Again"}])

    def test_rejects_non_human_approved_record(self):
        record = {
            "record_version": "x001-record-v3",
            "review": {"status": "approved", "reviewer_type": "model_assisted"},
            "messages": [{"role": "user", "content": "Question"}, {"role": "assistant", "content": "Answer"}],
        }
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "train.jsonl"
            source.write_text(json.dumps(record) + "\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "human review"):
                serialize_file(source, root / "out.jsonl", root / "manifest.jsonl")

    def test_emits_lineage_manifest(self):
        record = {
            "record_version": "x001-record-v3",
            "constitution_version": "g006-candidate-v1",
            "policy_delta_ids": ["G006-P01"],
            "target_revision": "r1",
            "example_id": "X001-EXAMPLE",
            "split": "train",
            "review": {"status": "approved", "reviewer_type": "human"},
            "messages": [{"role": "user", "content": "Question"}, {"role": "assistant", "content": "Answer"}],
        }
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "train.jsonl"
            output = root / "out.jsonl"
            manifest = root / "manifest.jsonl"
            source.write_text(json.dumps(record) + "\n", encoding="utf-8")
            self.assertEqual(serialize_file(source, output, manifest), 1)
            self.assertEqual(json.loads(output.read_text())['text'], "User: Question\nAssistant: Answer")
            row = json.loads(manifest.read_text())
            self.assertEqual(row["serializer_version"], SERIALIZER_VERSION)
            self.assertEqual(row["example_id"], "X001-EXAMPLE")
            self.assertEqual(row["line"], 1)


if __name__ == "__main__":
    unittest.main()
