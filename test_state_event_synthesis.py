import unittest

try:
    from math_os_prototype.state_event_synthesis import solve_state_event_arithmetic
except ImportError:
    from state_event_synthesis import solve_state_event_arithmetic


class StateEventSynthesisTests(unittest.TestCase):
    def assert_answer(self, problem: str, expected: str) -> None:
        result = solve_state_event_arithmetic(problem)
        self.assertIsNotNone(result)
        self.assertEqual(expected, result.answer_exact)

    def test_additive_state_with_loss(self) -> None:
        self.assert_answer(
            "Nancy took 49 pictures at the zoo and 8 pictures at the museum. She later deleted 38 pictures. How many pictures did she have left?",
            "19",
        )

    def test_problem_and_variable_renaming_preserves_law(self) -> None:
        self.assert_answer(
            "A player scored 17 points, scored 6 points, and lost 16 points. How many points did the player have at the end?",
            "7",
        )

    def test_comparison_is_not_misread_as_event(self) -> None:
        self.assertIsNone(solve_state_event_arithmetic(
            "A has 5 cards. B has 3 fewer than A. How many cards do they have altogether?"
        ))

    def test_selected_subtotal_is_not_guessed(self) -> None:
        self.assertIsNone(solve_state_event_arithmetic(
            "Jack received 4 emails in the morning, 5 in the afternoon and 8 in the evening. How many in the afternoon and evening?"
        ))


if __name__ == "__main__":
    unittest.main()
