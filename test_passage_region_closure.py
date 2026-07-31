from __future__ import annotations

import unittest

import sympy as sp

try:
    from math_os_prototype.passage_region_closure import (
        ConcaveQuadraticSweep,
        synthesize,
        x,
    )
    from math_os_prototype.wolfram_region_engine import _piecewise_to_wolfram
except ImportError:  # pragma: no cover
    from passage_region_closure import ConcaveQuadraticSweep, synthesize, x
    from wolfram_region_engine import _piecewise_to_wolfram


class PassageRegionClosureTest(unittest.TestCase):
    def test_known_sweep_area_is_seven_twelfths(self) -> None:
        sweep = ConcaveQuadraticSweep(
            q=sp.Rational(1),
            b_slope=sp.Rational(2),
            b_intercept=sp.Rational(0),
            vertical_shift=sp.Integer(0),
            t_low=sp.Rational(0),
            t_high=sp.Rational(1),
            x_low=sp.Rational(0),
            x_high=sp.Rational(1),
        )
        self.assertEqual(sweep.certified_area(), sp.Rational(7, 12))

    def test_certificate_proves_bounds_by_exact_independent_slices(self) -> None:
        sweep = ConcaveQuadraticSweep(
            q=sp.Rational(2),
            b_slope=sp.Rational(3),
            b_intercept=sp.Rational(-1),
            vertical_shift=x**2,
            t_low=sp.Rational(-1),
            t_high=sp.Rational(2),
            x_low=sp.Rational(-2),
            x_high=sp.Rational(3),
        )
        certificate = sweep.certificate()
        self.assertTrue(certificate["exact_identity_check"])
        self.assertTrue(certificate["independent_exact_slice_check"])
        self.assertTrue(
            all(value == "0" for value in certificate["identity_residuals"].values())
        )

    def test_one_certified_object_supports_three_observations(self) -> None:
        report = synthesize()
        self.assertEqual(report["summary"]["accepted"], 3)
        self.assertEqual(len(report["summary"]["query_types"]), 3)
        for problem in report["problems"]:
            with self.subTest(problem=problem["candidate_id"]):
                self.assertTrue(problem["verification"]["exact_backend"])
                self.assertTrue(problem["verification"]["independent_check"])
                self.assertTrue(problem["lift_certificate"]["type_checked"])

    def test_wolfram_crosscheck_receives_real_piecewise_bounds(self) -> None:
        sweep = ConcaveQuadraticSweep(
            q=sp.Rational(1),
            b_slope=sp.Rational(2),
            b_intercept=sp.Rational(0),
            vertical_shift=sp.Integer(0),
            t_low=sp.Rational(0),
            t_high=sp.Rational(1),
            x_low=sp.Rational(0),
            x_high=sp.Rational(1),
        )
        rendered = _piecewise_to_wolfram(sweep.upper_bound)
        self.assertIn("Piecewise", rendered)
        self.assertIn("x <= 1", rendered)


if __name__ == "__main__":
    unittest.main()
