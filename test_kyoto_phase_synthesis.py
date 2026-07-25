from __future__ import annotations

import unittest

import sympy as sp

from math_os_prototype.kyoto_phase_synthesis import (
    build_phase_candidate,
    choose_candidate,
    quotient_x3_coefficient,
)


class KyotoPhaseSynthesisTests(unittest.TestCase):
    def test_quotient_coefficient_for_third_power(self) -> None:
        self.assertEqual(quotient_x3_coefficient(3), 1)

    def test_quotient_coefficient_for_fifth_power(self) -> None:
        t = sp.symbols("t", real=True)
        self.assertEqual(quotient_x3_coefficient(5), 5)

    def test_third_power_candidate_is_verified(self) -> None:
        candidate = build_phase_candidate(3)
        self.assertTrue(candidate.backend_verified)
        self.assertEqual(candidate.maximum_area, "25/2")
        self.assertEqual(candidate.maximizer_t, ["25/8"])

    def test_phase_selector_prefers_short_equivalence_representative(self) -> None:
        candidates = [build_phase_candidate(exponent) for exponent in (3, 5, 7)]
        self.assertEqual(choose_candidate(candidates).exponent, 3)


if __name__ == "__main__":
    unittest.main()
