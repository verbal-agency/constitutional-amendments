#!/usr/bin/env python3
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_sc010_d2_semantics import classify_output


class Sc010D2SemanticTests(unittest.TestCase):
    def test_direct_answer(self):
        answer = (
            "They do not share a limiting philosophy. Both are formatting conventions, "
            "and neither is a rewrite target; preserve them."
        )
        self.assertEqual(classify_output(answer)["label"], "direct_answer")

    def test_missing_context_is_not_direct(self):
        answer = "I don't see the two passages. Please paste the passages."
        result = classify_output(answer)
        self.assertEqual(result["label"], "missing_context_claim")
        self.assertTrue(result["missing_context_claim"])

    def test_partial_answer_requires_rewrite_disposition(self):
        answer = "They are formatting conventions and do not constitute a limiting philosophy."
        self.assertEqual(classify_output(answer)["label"], "partial_answer")

    def test_unsupported_claim_is_separate(self):
        answer = "The constitution does contain language in that vicinity, so this depends on it."
        self.assertEqual(classify_output(answer)["label"], "unsupported_claim")


if __name__ == "__main__":
    unittest.main()
