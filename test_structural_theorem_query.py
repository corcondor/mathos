from __future__ import annotations

import math
import unittest

import sympy as sp

try:
    from math_os_prototype.structural_theorem_query import execute_structural_theorem_query
except ImportError:
    from structural_theorem_query import execute_structural_theorem_query


def run(operator: str, objects: dict, output_sort: str = "Product") -> dict:
    return execute_structural_theorem_query(
        {
            "operator": operator,
            "objects": objects,
            "output_sort": output_sort,
            "lowering_certificate": {
                "kind": "typed_structural_theorem",
                "operator": operator,
                "alpha_renamable": True,
                "memorized_answer": False,
            },
        }
    )


class StructuralTheoremQueryTests(unittest.TestCase):
    def test_circle_overlap_kernel_changes_with_offset(self) -> None:
        result = run("circle_overlap_difference_limit", {"offset_numerator": 3, "offset_denominator": 2})
        self.assertEqual(sp.sympify(result["answer_exact"]), -9 * sp.sqrt(3) / 8)

    def test_prime_power_kernel_changes_with_base(self) -> None:
        result = run("prime_power_sum_composite", {"base": 4})
        self.assertEqual(result["certificate"]["witness"]["successor_prime"], 5)
        self.assertGreater(result["certificate"]["witness"]["exceptional_divisor"], 1)

    def test_dodecahedron_kernel_scales_quadratically(self) -> None:
        unit = sp.sympify(run("regular_dodecahedron_max_triangle", {"edge": "1"})["answer_exact"])
        doubled = sp.sympify(run("regular_dodecahedron_max_triangle", {"edge": "2"})["answer_exact"])
        self.assertEqual(sp.simplify(doubled - 4 * unit), 0)

    def test_elementary_symmetric_prime_classification_on_finite_probe(self) -> None:
        primes = list(sp.primerange(2, 20))

        def predicted(p: int, q: int, r: int) -> bool:
            return (
                (p == 2 and q in {2, 3})
                or (p, q, r) in {(2, 5, 5), (2, 5, 7), (3, 3, 3), (3, 3, 5), (3, 3, 7)}
            )

        for p in primes:
            for q in primes:
                for r in primes:
                    if not p <= q <= r:
                        continue
                    sides = (p + q + r, p * q + q * r + r * p, p * q * r)
                    actual = 2 * max(sides) < sum(sides)
                    self.assertEqual(actual, predicted(p, q, r), (p, q, r))

    def test_ordered_prime_power_triangle_finite_probe(self) -> None:
        primes = list(sp.primerange(2, 30))
        for i, p in enumerate(primes):
            for j, q in enumerate(primes[i + 1 :], i + 1):
                for r in primes[j + 1 :]:
                    sides = (p**q, q**r, r**p)
                    self.assertGreaterEqual(2 * max(sides), sum(sides))

    def test_rational_sine_prime_ratio_finite_probe(self) -> None:
        hits = []
        primes = list(sp.primerange(2, 200))
        for p in primes:
            for q in primes:
                if p <= q:
                    continue
                square = p * p + 6 * p * q + q * q
                if math.isqrt(square) ** 2 == square:
                    hits.append((p, q))
        self.assertEqual(hits, [(3, 2)])

    def test_triangular_primorial_finite_probe(self) -> None:
        primorial = 1
        hits = []
        for n in range(1, 1001):
            if sp.isprime(n):
                primorial *= n
            if n * (n + 1) // 2 == primorial:
                hits.append(n)
        self.assertEqual(hits, [1, 3])

    def test_results_carry_replay_certificate(self) -> None:
        result = run("ordered_prime_power_triangle", {})
        self.assertTrue(result["verified"])
        self.assertEqual(result["certificate"]["kind"], "structural_theorem_replay")

    def test_trigonometric_area_uses_exact_tail_certificates(self) -> None:
        cosine = run("trigonometric_side_area_extremum", {"function": "cos", "direction": "minimum"})
        sine = run("trigonometric_side_area_extremum", {"function": "sin", "direction": "maximum"})
        self.assertEqual(cosine["certificate"]["witness"]["sturm_roots_on_5_6_to_1"], 0)
        self.assertEqual(sine["certificate"]["witness"]["extremizing_n"], 5)

    def test_sine_integral_bound_has_positive_rational_margin(self) -> None:
        result = run("sine_integral_rational_bounds", {})
        margin = sp.Rational(result["certificate"]["witness"]["upper_margin"])
        self.assertGreater(margin, 0)


if __name__ == "__main__":
    unittest.main()
