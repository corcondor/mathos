from __future__ import annotations

import unittest

import sympy as sp

from math_os_prototype.geometry_fusion_synthesis import (
    _passage_line,
    _passage_parabola,
    closed_form,
    synthesize,
)


class GeometryFusionTests(unittest.TestCase):
    def test_pool_is_geometry_heavy_and_exact(self) -> None:
        report = synthesize()
        self.assertGreater(report["summary"]["accepted"], 12)
        self.assertGreater(report["summary"]["domain_counts"].get("geometry", 0), 10)
        for problem in report["problems"]:
            with self.subTest(id=problem["candidate_id"]):
                answer = sp.sympify(problem["answer_exact"])
                self.assertFalse(answer.atoms(sp.Float))  # exact, not numeric noise
                self.assertTrue(problem["statement_tex"])
                self.assertTrue(problem["verification"]["exact_backend"])

    def test_known_passage_region_value(self) -> None:
        # y = 2 t x - t^2, t in [0,1], 0<=x<=1  ->  swept area = 7/12.
        problem = _passage_line({"a": 2, "T": 1, "X": 1})
        self.assertIsNotNone(problem)
        self.assertEqual(sp.sympify(problem.answer_exact), sp.Rational(7, 12))

    def test_parabola_passage_matches_numeric(self) -> None:
        problem = _passage_parabola({"T": 2, "X": 2})
        self.assertIsNotNone(problem)
        self.assertEqual(sp.sympify(problem.answer_exact), sp.Rational(448, 15))

    def test_closed_form_rejects_overfit(self) -> None:
        # a genuinely irrational-looking noisy value with no short closed form
        self.assertIsNone(closed_form(0.7231934812734, tol=1e-9))
        # a clean rational is found
        self.assertEqual(closed_form(0.5, tol=1e-9), sp.Rational(1, 2))


if __name__ == "__main__":
    unittest.main()
