from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from novelty_sketch import build_snapshot, screen_snapshot


class NoveltySketchTest(unittest.TestCase):
    def test_snapshot_rejects_exact_content_and_keeps_unrelated_content(self) -> None:
        records = [
            {
                "source": "test",
                "statement": "三角形ABCの重心をGとし、AGの長さを求めよ。",
            },
            {
                "source": "test",
                "statement": "素数pについて平方剰余の個数を求めよ。",
            },
        ]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sketch.npz"
            metadata = build_snapshot(records, path)
            self.assertEqual(metadata["corpus_size"], 2)
            exact = screen_snapshot(records[0]["statement"], path)
            unrelated = screen_snapshot(
                "凸体の極双対と射影体の合成関手の固定点を分類せよ。",
                path,
            )
            self.assertIsNotNone(exact)
            self.assertFalse(exact["passed"])
            self.assertTrue(exact["exact_surface_collision"])
            self.assertIsNotNone(unrelated)
            self.assertTrue(unrelated["passed"])


if __name__ == "__main__":
    unittest.main()
