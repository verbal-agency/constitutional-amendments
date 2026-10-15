import copy
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import validate_x001_source_packets as V


class SourcePacketValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.packets = V.read_packets(V.DEFAULT_PACKETS)

    def test_fixture_packets_pass(self):
        V.validate_packets(self.packets)

    def test_packet_hash_drift_fails(self):
        packets = copy.deepcopy(self.packets)
        packets[0]["event_or_issue"] = "changed"
        with self.assertRaisesRegex(ValueError, "packet_sha256"):
            V.validate_packets(packets)

    def test_source_hash_drift_fails(self):
        packets = copy.deepcopy(self.packets)
        packets[0]["sources"][0]["summary"] = "changed"
        packets[0]["packet_sha256"] = V.packet_hash(packets[0])
        with self.assertRaisesRegex(ValueError, "content_sha256"):
            V.validate_packets(packets)

    def test_unknown_claim_source_fails(self):
        packets = copy.deepcopy(self.packets)
        packets[0]["claims"][0]["source_ids"] = ["SRC-MISSING"]
        packets[0]["packet_sha256"] = V.packet_hash(packets[0])
        with self.assertRaisesRegex(ValueError, "unknown source"):
            V.validate_packets(packets)

    def test_annotation_fields_must_be_hidden(self):
        packets = copy.deepcopy(self.packets)
        packets[0]["rendering"]["annotation_fields_hidden"] = False
        packets[0]["packet_sha256"] = V.packet_hash(packets[0])
        with self.assertRaisesRegex(ValueError, "annotation fields"):
            V.validate_packets(packets)

    def test_family_cannot_cross_splits(self):
        packets = copy.deepcopy(self.packets)
        packets[0]["split"] = "train"
        packets[0]["packet_sha256"] = V.packet_hash(packets[0])
        with self.assertRaisesRegex(ValueError, "topic family"):
            V.validate_packets(packets)


if __name__ == "__main__":
    unittest.main()
