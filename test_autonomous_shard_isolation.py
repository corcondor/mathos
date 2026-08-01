from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

try:
    from math_os_prototype.autonomous_loop import _load_generation_base, _structure_signature
except ImportError:  # pragma: no cover
    from autonomous_loop import _load_generation_base, _structure_signature


class AutonomousShardIsolationTest(unittest.TestCase):
    def test_new_shard_does_not_preload_the_shared_pool(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "new-shard.json"
            self.assertEqual(_load_generation_base(target), {"problems": []})

    def test_existing_shard_can_accumulate_its_own_rounds(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "shard.json"
            target.write_text('{"problems":[{"family_id":"x"}]}', encoding="utf-8")
            self.assertEqual(
                _load_generation_base(target)["problems"],
                [{"family_id": "x"}],
            )

    def test_coefficients_and_answers_do_not_define_a_new_structure(self) -> None:
        left = {
            "family_id": "geometry.minkowski",
            "answer_tex": "12",
            "parameters": {"n": 3},
            "lift_certificate": {
                "morphism_chain": ["MinkowskiAddition", "AreaObservation"],
                "constraint_skeleton": ["convex(P)", "convex(Q)"],
                "query_signature": "area(P+Q)",
            },
        }
        right = {
            **left,
            "answer_tex": "40",
            "parameters": {"n": 5},
        }
        self.assertEqual(_structure_signature(left), _structure_signature(right))


if __name__ == "__main__":
    unittest.main()
