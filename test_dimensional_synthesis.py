import unittest

try:
    from math_os_prototype.dimensional_synthesis import solve_dimensional_arithmetic
except ImportError:
    from dimensional_synthesis import solve_dimensional_arithmetic


class DimensionalSynthesisTests(unittest.TestCase):
    def assert_answer(self, problem: str, expected: str) -> None:
        result = solve_dimensional_arithmetic(problem)
        self.assertIsNotNone(result)
        self.assertEqual(expected, result.answer_exact)

    def test_rate_times_duration(self) -> None:
        self.assert_answer(
            "Mrs. Hilt ate 5 apples every hour. How many apples had she eaten at the end of 3 hours?",
            "15",
        )

    def test_equal_share_is_dimension_division(self) -> None:
        self.assert_answer(
            "There are 9 students and 27 Skittles. The Skittles are divided equally among the students. How many does each student get?",
            "3",
        )

    def test_additive_choice_waits_for_event_semantics(self) -> None:
        self.assertIsNone(solve_dimensional_arithmetic(
            "Jerry bought 41 regular sodas and 22 diet sodas. His fridge holds 9 sodas on each shelf. How many shelves would he fill?",
        ))

    def test_surface_and_number_change_reuses_the_same_type_law(self) -> None:
        self.assert_answer(
            "A machine makes 8 bolts every hour. How many bolts does it make in 6 hours?",
            "48",
        )

    def test_referential_number_in_query_is_not_a_new_premise(self) -> None:
        self.assert_answer(
            "Mrs. Hilt bought 3 pizzas for $8 each. What was the total amount she paid for the three pizzas?",
            "24",
        )

    def test_unparsed_tex_fraction_is_delegated(self) -> None:
        self.assertIsNone(solve_dimensional_arithmetic(
            r"A recipe uses $\frac14$ teaspoon per quart. How many quarts use two teaspoons?"
        ))

    def test_missing_month_to_year_conversion_is_not_guessed(self) -> None:
        self.assertIsNone(solve_dimensional_arithmetic(
            "Jenna has 4 roommates. Each month the bill is $100. How much will each roommate pay per year?"
        ))

    def test_ambiguous_same_dimension_expression_is_rejected(self) -> None:
        self.assertIsNone(solve_dimensional_arithmetic("There are 8 apples. Elsewhere there are 3 apples. How many apples are relevant?"))


if __name__ == "__main__":
    unittest.main()
