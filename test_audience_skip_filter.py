from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

try:
    from math_os_prototype.build_entrance_pool import (
        _audience_rejected_structure_keys,
        _structure_key,
    )
    from math_os_prototype.refresh_selection_feedback import summarize_ratings
except ImportError:  # pragma: no cover
    from build_entrance_pool import _audience_rejected_structure_keys, _structure_key
    from refresh_selection_feedback import summarize_ratings


class AudienceSkipFilterTest(unittest.TestCase):
    def test_rejected_structure_key_is_loaded_for_active_removal(self) -> None:
        problem = {
            "family_id": "example.family",
            "lift_certificate": {
                "morphism_chain": ["A", "B"],
                "constraint_skeleton": ["x>0"],
                "query_signature": "Area",
            },
        }
        structure_key = _structure_key(problem)
        payload = {
            "structures": [
                {"structure_key": structure_key, "label": "rejected"},
                {"structure_key": "selected-key", "label": "selected"},
            ]
        }
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "feedback.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            self.assertEqual(
                _audience_rejected_structure_keys(path),
                {structure_key},
            )

    def test_conflicting_votes_do_not_delete_structure(self) -> None:
        result = summarize_ratings(
            {"p1": "same", "p2": "same", "p3": "rejected-only"},
            [
                {"problem_id": "p1", "status": "selected"},
                {"problem_id": "p2", "status": "rejected"},
                {"problem_id": "p3", "status": "rejected"},
            ],
        )
        labels = {item["structure_key"]: item["label"] for item in result["structures"]}
        self.assertEqual(labels["same"], "conflict")
        self.assertEqual(labels["rejected-only"], "rejected")


if __name__ == "__main__":
    unittest.main()
