from __future__ import annotations

import unittest

import sympy as sp

try:
    from math_os_prototype.iterated_relation_closure import (
        certify_affine_recurrence,
        certify_affine_root_image,
        certify_error_squaring,
        certify_reciprocal_root_image,
        synthesize,
        x,
    )
except ImportError:  # pragma: no cover
    from iterated_relation_closure import (
        certify_affine_recurrence,
        certify_affine_root_image,
        certify_error_squaring,
        certify_reciprocal_root_image,
        synthesize,
        x,
    )


class IteratedRelationClosureTest(unittest.TestCase):
    def assert_certified(self, certificate: dict[str, object]) -> None:
        self.assertTrue(certificate["identity_verified"])
        self.assertTrue(certificate["global_relation_verified"])
        self.assertTrue(certificate["independent_check"])
        self.assertTrue(
            all(
                residual == "0"
                for residual in certificate["identity_residuals"].values()
            )
        )

    def test_affine_recurrence_generalizes_to_other_coefficients(self) -> None:
        self.assert_certified(
            certify_affine_recurrence(
                sp.Rational(2, 3),
                sp.Rational(2),
                sp.Rational(9),
            )
        )

    def test_error_squaring_generalizes_to_other_initial_values(self) -> None:
        self.assert_certified(certify_error_squaring(sp.Rational(1, 3)))

    def test_affine_root_image_generalizes_beyond_cubic_example(self) -> None:
        certificate = certify_affine_root_image(
            x**2 - 2,
            sp.Rational(3),
            sp.Rational(-2),
        )
        self.assert_certified(certificate)
        self.assertEqual(
            sp.sympify(certificate["image_polynomial"]),
            sp.Symbol("y") ** 2 + 4 * sp.Symbol("y") - 14,
        )

    def test_reciprocal_root_image_generalizes(self) -> None:
        self.assert_certified(
            certify_reciprocal_root_image(x**4 + 2 * x + 1)
        )

    def test_synthesized_observations_are_all_certified(self) -> None:
        report = synthesize()
        self.assertEqual(report["summary"]["accepted"], 4)
        self.assertEqual(
            len(
                {
                    problem["lift_certificate"]["query_signature"]
                    for problem in report["problems"]
                }
            ),
            4,
        )


if __name__ == "__main__":
    unittest.main()
