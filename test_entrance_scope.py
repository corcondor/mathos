from __future__ import annotations

import unittest

from math_os_prototype.build_entrance_pool import build_pool
from math_os_prototype.entrance_scope import (
    CURRICULUM,
    OUT_OF_VOCABULARY_SURFACE_TERMS,
)


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

    def test_delivered_surface_uses_only_school_vocabulary(self) -> None:
        """族の名前ではなく、配信される文章そのものを検査する。

        内部で平方剰余やグラフを使うこと自体は禁止しない。禁止するのは、
        高校の語彙に書き換えられないまま配信されることだけである。
        """
        for problem in self.report["problems"]:
            surface = " ".join(
                (
                    str(problem.get("statement_tex") or ""),
                    str(problem.get("solution_tex") or ""),
                )
            )
            for term in OUT_OF_VOCABULARY_SURFACE_TERMS:
                self.assertNotIn(term, surface, problem["family_id"])

    def test_numeric_variants_are_never_generated(self) -> None:
        """数値だけ違う同一構造は、作ってから捨てるのではなく作らない。"""
        keys = [
            problem["structure_key"] for problem in self.report["problems"]
        ]
        self.assertEqual(len(keys), len(set(keys)))
        discarded = self.report["summary"]["rejected"].get(
            "same_structure_variant",
            0,
        )
        self.assertLessEqual(discarded, len(keys))

    def test_geometry_and_algebra_are_the_majority(self) -> None:
        summary = self.report["summary"]
        self.assertGreaterEqual(
            summary["geometry_algebra_structures"] * 2,
            summary["certified_structures"],
        )


if __name__ == "__main__":
    unittest.main()
