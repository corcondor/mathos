import unittest

try:
    from math_os_prototype.rate_graph_synthesis import solve_rate_graph
except ImportError:
    from rate_graph_synthesis import solve_rate_graph


class RateGraphSynthesisTests(unittest.TestCase):
    def assert_answer(self, text: str, expected: str) -> None:
        result = solve_rate_graph(text)
        self.assertIsNotNone(result)
        self.assertEqual(expected, result.answer_exact)

    def test_distance_addition_uses_target_dimension(self) -> None:
        self.assert_answer(
            "A train traveled 80 miles west and 150 miles north. What distance did it cover in the two days?",
            "230",
        )

    def test_carton_rate_chain(self) -> None:
        self.assert_answer(
            "She uses 1 serving per day. A carton contains 15 servings and costs $4 per carton. After 60 days, how much money will she spend?",
            "16",
        )

    def test_number_change_preserves_rate_contraction(self) -> None:
        first = solve_rate_graph("A machine makes 12 items per day for 5 days. How many items does it make?")
        changed = solve_rate_graph("A machine makes 18 items per day for 5 days. How many items does it make?")
        self.assertIsNotNone(first)
        self.assertIsNotNone(changed)
        self.assertEqual("60", first.answer_exact)
        self.assertEqual("90", changed.answer_exact)
        self.assertEqual(first.target_dimension, changed.target_dimension)

    def test_labeled_components_contract_before_total(self) -> None:
        self.assert_answer(
            "Mina bought 3 pairs of shorts, 3 pairs of pants, and 3 pairs of shoes. "
            "One pair of shorts costs $16.50. One pair of pants costs $22.50 and "
            "one pair of shoes costs $42. How many dollars did Mina spend on all the items?",
            "243",
        )

    def test_inverse_rate_observes_required_time(self) -> None:
        self.assert_answer(
            "Mark starts with $50 and earns $10 per day. A bike costs $300. "
            "How many days does Mark have to save his money?",
            "25",
        )

    def test_inverse_composed_rate_observes_weeks(self) -> None:
        self.assert_answer(
            "John gets paid $2 per hour and works 5 hours a day for 4 days a week. "
            "If he wants to save $80, how many weeks will it take?",
            "2",
        )

    def test_capacity_is_floor_of_inverse_rate(self) -> None:
        self.assert_answer(
            "A bridge can carry no more than 5000 pounds. Each box weighs 15 pounds. "
            "The truck weighs 3755 pounds. What is the maximum number of boxes?",
            "83",
        )

    def test_rate_graph_does_not_erase_requested_activity_label(self) -> None:
        self.assertIsNone(solve_rate_graph(
            "Every day Ryan spends 6 hours on learning English and 5 hours on "
            "learning Chinese. For 2 days, how many hours does he spend on learning English?"
        ))

    def test_rate_graph_does_not_treat_partition_difference_as_sum(self) -> None:
        self.assertIsNone(solve_rate_graph(
            "There are 56 students. The first of two groups has 24 students. "
            "How many more students will there be in the second group?"
        ))


if __name__ == "__main__":
    unittest.main()
