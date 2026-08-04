import unittest

try:
    from math_os_prototype.typed_operator_reasoner import solve_typed_operator_problem
except ImportError:
    from typed_operator_reasoner import solve_typed_operator_problem


class TypedOperatorReasonerTests(unittest.TestCase):
    def test_gcd_lcm_constraint_uses_product_law_and_verifies(self):
        result = solve_typed_operator_problem(r"Find m if \gcd(m,54)=6 and \operatorname{lcm}(m,54)=378.")
        self.assertIsNotNone(result)
        self.assertEqual(result.operator, "GCDLCMProductLaw")
        self.assertEqual(result.answer_exact, "42")

    def test_gcd_lcm_supports_mathop_text_lcm(self):
        result = solve_typed_operator_problem(r"Find n if \gcd(n,40)=10 and \mathop{\text{lcm}}[n,40]=280.")
        self.assertIsNotNone(result)
        self.assertEqual(result.answer_exact, "70")

    def test_lcm_fold_changes_with_unseen_bound(self):
        ten = solve_typed_operator_problem("What is the least common multiple of the first ten positive integers?")
        twelve = solve_typed_operator_problem("What is the least common multiple of the first twelve positive integers?")
        self.assertEqual(ten.answer_exact, "2520")
        self.assertEqual(twelve.answer_exact, "27720")

    def test_ceiling_equation_is_solved_by_rounding_interval(self):
        result = solve_typed_operator_problem(r"Find x such that $\lceil x \rceil+x=\dfrac{23}{7}$.")
        self.assertIsNotNone(result)
        self.assertEqual(result.operator, "CeilingLinearConstraint")
        self.assertEqual(result.answer_exact, "9/7")

    def test_floor_equation_uses_the_same_linear_constraint_solver(self):
        result = solve_typed_operator_problem(r"Find y such that $\lfloor y \rfloor+y=\frac{12}{5}$.")
        self.assertIsNotNone(result)
        self.assertEqual(result.operator, "FloorLinearConstraint")
        self.assertEqual(result.answer_exact, "7/5")

    def test_percent_scaling_recomputes_values(self):
        first = solve_typed_operator_problem("What is 35% of 240?")
        second = solve_typed_operator_problem("What is 15% of 240?")
        self.assertEqual(first.answer_exact, "84")
        self.assertEqual(second.answer_exact, "36")


if __name__ == "__main__":
    unittest.main()
