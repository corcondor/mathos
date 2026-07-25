import unittest

from math_os_prototype.category_semantics import compile_typed_semantic_graph
from math_os_prototype.lift_backend import solve_from_lift_certificates
from math_os_prototype.prime_power_symmetry import (
    analyze_prime_power_symmetry,
    compile_prime_power_symmetric_ir,
    first_small_factor,
)


class PrimePowerSymmetryTests(unittest.TestCase):
    def test_search_does_not_discard_three_mod_four_a(self) -> None:
        report = analyze_prime_power_symmetry(search_limit=7, sieve_bound=200)

        self.assertEqual(report.candidate_a_values, 3)  # 3, 5, and 7
        self.assertEqual(report.canonical_pairs_checked, 1)
        self.assertNotIn("a≡1 (mod 4)", " ".join(report.reductions))

    def test_swap_symmetry_covers_both_orderings(self) -> None:
        report = analyze_prime_power_symmetry(search_limit=50, sieve_bound=500)

        self.assertEqual(
            report.ordered_triples_covered,
            2 * report.canonical_pairs_checked,
        )

    def test_small_factor_identifies_which_target_it_divides(self) -> None:
        moduli = [3, 5, 7]
        # x=1, y=1, z=2 modulo each modulus: x+y-z is divisible by 3.
        factor = first_small_factor(
            (1, 1, 1),
            (1, 1, 1),
            (2, 2, 2),
            moduli,
        )

        self.assertEqual(factor, ("first", 3))

    def test_corrected_bounded_search_has_no_small_example(self) -> None:
        report = analyze_prime_power_symmetry(search_limit=100, sieve_bound=1000)

        self.assertEqual(report.status, "no_example_in_bounded_search")
        self.assertEqual(report.candidate_a_values, 24)
        self.assertEqual(report.ordered_triples_covered, 4048)
        self.assertEqual(report.examples, [])

    def test_structural_lifter_accepts_latex_and_recovers_center(self) -> None:
        text = (
            "素数 a,b,c に対して, "
            "a^{a}+b^{b}-c^{c}, a^{a}-b^{b}+c^{c} がともに素数となる組は存在するか。"
        )

        ir = compile_prime_power_symmetric_ir(text)

        self.assertIsNotNone(ir)
        assert ir is not None
        self.assertEqual(ir.center_variable, "a")
        self.assertEqual(set(ir.prime_variables), {"a", "b", "c"})
        self.assertEqual(len(ir.necessary_conditions), 5)

    def test_structural_lifter_is_invariant_to_target_and_term_order(self) -> None:
        text = "For primes x,y,z, z^z-y^y+x^x and y^y+x^x-z^z are both prime. Do they exist?"

        ir = compile_prime_power_symmetric_ir(text)

        self.assertIsNotNone(ir)
        assert ir is not None
        self.assertEqual(ir.center_variable, "x")
        self.assertEqual({ir.positive_offset_variable, ir.negative_offset_variable}, {"y", "z"})

    def test_sieve_only_never_claims_unbounded_solution(self) -> None:
        report = analyze_prime_power_symmetry(
            search_limit=100,
            sieve_bound=1000,
            run_primality_checks=False,
        )

        self.assertEqual(report.status, "sieve_survivors_remaining")
        self.assertEqual(report.exact_compositeness_checks, 0)
        self.assertGreater(report.candidate_triples_after_sieve, 0)
        self.assertEqual(report.backend, "builtin modular pow")

    def test_semantic_graph_connects_ir_to_bounded_backend(self) -> None:
        text = (
            "素数 a,b,c に対して, "
            "a^a+b^b-c^c, a^a-b^b+c^c がともに素数となる組は存在するか。"
        )
        graph = compile_typed_semantic_graph(text).to_dict()
        families = {
            item["family_id"]
            for item in graph["lift_certificates"]
            if item["admissible"]
        }

        self.assertIn(
            "elementary_number_theory.prime_power_symmetric_primality",
            families,
        )
        result = solve_from_lift_certificates(graph)
        self.assertIsNotNone(result)
        assert result is not None
        self.assertEqual(result["status"], "bounded_evidence")
        self.assertIn("unbounded existence question remains unresolved", result["answer_exact"])


if __name__ == "__main__":
    unittest.main()
