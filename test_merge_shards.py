from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from merge_shards import merge


def _problem(candidate: str, value: int) -> dict:
    return {
        "candidate_id": candidate,
        "family_id": "family.shared",
        "statement_tex": f"x={value}",
        "answer_tex": str(value),
        "lift_certificate": {
            "morphism_chain": ["Normalize", "Observe"],
            "constraint_skeleton": ["x is finite"],
            "query_signature": "value(x)",
        },
        "difficulty": {"score": 1.0, "band": "D_textbook"},
    }


def _with_chain(problem: dict, chain: list[str]) -> dict:
    result = dict(problem)
    result["lift_certificate"] = dict(problem["lift_certificate"])
    result["lift_certificate"]["morphism_chain"] = chain
    return result


class MergeShardsTest(unittest.TestCase):
    def test_numeric_variants_share_one_structure(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            shard = root / "shard.json"
            shard.write_text(
                json.dumps({"problems": [_problem("a", 2), _problem("b", 7)]}),
                encoding="utf-8",
            )
            report = merge([shard])
            self.assertEqual(len(report["problems"]), 1)
            self.assertEqual(report["summary"]["certified_structures"], 1)

    def test_no_semantic_change_preserves_existing_payload(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            base = root / "base.json"
            payload = {
                "generated_at": "fixed",
                "method": {
                    "name": "MathOS autonomous pool (parallel shards merged)",
                    "selection_unit": (
                        "family_id + morphism_chain + constraint_skeleton + "
                        "query_signature"
                    ),
                    "numeric_variants_count_as_new": False,
                },
                "summary": {
                    "total": 1,
                    "shards": 0,
                    "certified_structures": 1,
                    "family_counts": {"family.shared": 1},
                    "band_counts": {"D_textbook": 1},
                },
                "problems": [_problem("a", 2)],
            }
            base.write_text(json.dumps(payload), encoding="utf-8")
            report = merge([], base=base)
            self.assertEqual(report, payload)

    def test_same_answer_does_not_erase_a_different_structure(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            shard = root / "shard.json"
            left = _problem("a", 2)
            right = _with_chain(_problem("b", 3), ["Factor", "Observe"])
            right["answer_tex"] = left["answer_tex"]
            shard.write_text(
                json.dumps({"problems": [left, right]}),
                encoding="utf-8",
            )
            report = merge([shard])
            self.assertEqual(len(report["problems"]), 2)
            self.assertEqual(report["summary"]["certified_structures"], 2)


if __name__ == "__main__":
    unittest.main()
