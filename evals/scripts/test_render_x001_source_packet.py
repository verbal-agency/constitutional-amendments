import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from render_x001_source_packet import RENDERER_VERSION, render_packet
import validate_x001_source_packets as V


class SourcePacketRenderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.packet = V.read_packets(V.DEFAULT_PACKETS)[0]

    def test_renders_task_and_visible_sources(self):
        rendered = render_packet(self.packet)
        text = rendered["messages"][0]["content"]
        self.assertIn("Assess the LeBron James versus Michael Jordan GOAT debate", text)
        self.assertIn("SRC-NBA-JORDAN", text)
        self.assertIn("SRC-NBA-LEBRON", text)
        self.assertNotIn("SRC-SCENARIO-GOAT", text)

    def test_renderer_is_versioned_and_stable(self):
        first = render_packet(self.packet)
        second = render_packet(self.packet)
        self.assertEqual(first, second)
        self.assertEqual(first["renderer_version"], RENDERER_VERSION)
        self.assertEqual(first["packet_sha256"], self.packet["packet_sha256"])

    def test_annotation_fields_are_not_rendered(self):
        text = render_packet(self.packet)["messages"][0]["content"]
        self.assertNotIn("support_status", text)
        self.assertNotIn("annotation_only", text)
        self.assertNotIn("unknowns", text)


if __name__ == "__main__":
    unittest.main()
