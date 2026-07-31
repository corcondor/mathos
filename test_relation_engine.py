from __future__ import annotations

import unittest

import sympy as sp

try:
    from math_os_prototype.entrance_scope import certify_entrance_scope
    from math_os_prototype.relation_engine import synthesize
except ImportError:  # pragma: no cover - direct repository execution
    from entrance_scope import certify_entrance_scope
    from relation_engine import synthesize


class RelationEngineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = synthesize()
        cls.problems = cls.report["problems"]

    def test_generates_distinct_relation_structures(self) -> None:
        self.assertGreaterEqual(len(self.problems), 19)
        families = [problem["family_id"] for problem in self.problems]
        self.assertEqual(len(families), len(set(families)))
        self.assertIn("min", self.report["summary"]["kinds"])
        self.assertIn("max", self.report["summary"]["kinds"])
        self.assertIn("sos", self.report["summary"]["kinds"])

    def test_every_relation_has_an_exact_certificate(self) -> None:
        for problem in self.problems:
            certificate = problem["parameters"]["relation_certificate"]
            self.assertTrue(certificate["identity_verified"])
            self.assertTrue(certificate["global_relation_verified"])
            self.assertTrue(certificate["independent_numeric_check"])
            self.assertEqual(certificate["counterexample_set"], "EmptySet")
            self.assertNotIn(
                sp.Float,
                {type(atom) for atom in sp.sympify(certificate["bound_exact"]).atoms()},
            )

    def test_proof_questions_show_the_verified_factorization(self) -> None:
        proofs = [
            problem
            for problem in self.problems
            if problem["parameters"]["kind"] == "sos"
            and problem["family_id"].startswith(
                "relation.constrained_symmetric"
            )
        ]
        self.assertGreaterEqual(len(proofs), 6)
        for problem in proofs:
            factor_tex = problem["parameters"]["relation_certificate"][
                "factorization_tex"
            ]
            self.assertIn(factor_tex, problem["solution_tex"])
            self.assertNotIn("平方因子をもつ", problem["solution_tex"])

    def test_product_reciprocal_keeps_both_equality_cases(self) -> None:
        problem = next(
            problem
            for problem in self.problems
            if problem["family_id"].endswith("product_reciprocal_minimum")
        )
        points = problem["parameters"]["relation_certificate"]["equality_points"]
        self.assertEqual(len(points), 2)
        self.assertTrue(any("sqrt(3)" in point for point in points))

    def test_every_relation_lowers_to_school_primitives(self) -> None:
        for problem in self.problems:
            certificate = certify_entrance_scope(problem)
            self.assertIsNotNone(certificate, problem["family_id"])

    def test_structural_relations_have_long_derivations(self) -> None:
        structural = [
            problem
            for problem in self.problems
            if not problem["family_id"].startswith(
                ("relation.constrained_symmetric", "relation.triangle_angles")
            )
        ]
        self.assertEqual(len(structural), 4)
        for problem in structural:
            chain = problem["lift_certificate"]["morphism_chain"]
            self.assertGreaterEqual(len(chain), 6)
            self.assertTrue(problem["verification"]["exact_backend"])
            self.assertTrue(problem["verification"]["independent_check"])
            self.assertIn(r"\geq0", problem["solution_tex"])


if __name__ == "__main__":
    unittest.main()
