from __future__ import annotations

import unittest

from math_os_prototype.build_entrance_pool import build_pool
from math_os_prototype.entrance_scope import CURRICULUM


class EntranceScopeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = build_pool()

    def test_every_problem_has_a_school_scope_lowering(self) -> None:
        problems = self.report["problems"]
        self.assertGreaterEqual(len(problems), 20)
        for problem in problems:
            certificate = problem["curriculum_certificate"]
            self.assertEqual(certificate["scope"], CURRICULUM)
            self.assertTrue(certificate["type_checked"])
            self.assertTrue(certificate["lowering_chain"])

    def test_graph_and_gambler_families_are_not_exam_delivery(self) -> None:
        families = {
            problem["family_id"] for problem in self.report["problems"]
        }
        self.assertFalse(any("paley" in family for family in families))
        self.assertFalse(any("gambler" in family for family in families))
        self.assertFalse(any("graph" in family for family in families))

    def test_numeric_variants_collapse_to_one_structure(self) -> None:
        keys = [
            problem["structure_key"] for problem in self.report["problems"]
        ]
        self.assertEqual(len(keys), len(set(keys)))
        self.assertGreater(
            self.report["summary"]["rejected"].get(
                "same_structure_variant",
                0,
            ),
            500,
        )

    def test_geometry_and_algebra_are_the_majority(self) -> None:
        summary = self.report["summary"]
        self.assertGreaterEqual(
            summary["geometry_algebra_structures"] * 2,
            summary["certified_structures"],
        )


if __name__ == "__main__":
    unittest.main()
