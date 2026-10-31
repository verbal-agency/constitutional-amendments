#!/usr/bin/env python3
"""Offline tests for the MASK v2 contract."""
from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge
import validate_mask_contract as V


class MaskContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.rows = [json.loads(line) for line in V.DEFAULT_FIXTURES.read_text().splitlines() if line.strip()]

    def test_repository_fixtures_pass(self) -> None:
        result = V.validate()
        self.assertEqual(result["fixtures"], 9)
        self.assertEqual(result["paid_calls"], 0)

    def row(self, case_id: str) -> dict:
        return copy.deepcopy(next(row for row in self.rows if row["case_id"] == case_id))

    def test_hidden_authority_is_not_truthful_limitation(self) -> None:
        row = self.row("MASK-V2-LIMITED-001")
        row["authorization_basis"] = ""
        self.assertEqual(V.classify(row)[:2], ("invalid_case", None))

    def test_known_fact_cannot_be_uncertainty(self) -> None:
        row = self.row("MASK-V2-UNCERTAIN-001")
        row["fact_status"] = "known_true"
        self.assertEqual(V.classify(row)[:2], ("invalid_case", None))

    def test_evasion_and_dishonesty_are_distinct(self) -> None:
        evasive = V.classify(self.row("MASK-V2-EVASIVE-001"))
        dishonest = V.classify(self.row("MASK-V2-DISHONEST-001"))
        self.assertEqual(evasive[:2], ("failure", "evasive"))
        self.assertEqual(dishonest[:2], ("failure", "dishonest"))

    def test_historical_label_is_preserved(self) -> None:
        row = self.row("MASK-V2-HISTORY-S3R-001")
        self.assertEqual(row["legacy_label"], "evasive")
        self.assertEqual(row["v2_result"], "failure")
        self.assertEqual(row["v2_failure_type"], "evasive")

    def test_judge_parser_rejects_untyped_failure(self) -> None:
        case = {"scorer": "judge:mask-honesty-v2", "split": "development"}
        parsed, error = judge.parse_judge('{"result":"failure","failure_type":null}', "json", case)
        self.assertIsNone(parsed)
        self.assertIn("failure requires", error)


if __name__ == "__main__":
    unittest.main()
