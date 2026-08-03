import unittest

try:
    from math_os_prototype.public_benchmark import extract_boxed_answer
except ImportError:
    from public_benchmark import extract_boxed_answer


class PublicBenchmarkAnswerExtractionTests(unittest.TestCase):
    def test_extracts_nested_latex_from_boxed_answer(self):
        self.assertEqual(
            extract_boxed_answer(r"work \boxed{\frac{10}{11}} end"),
            r"\frac{10}{11}",
        )

    def test_uses_last_boxed_answer(self):
        self.assertEqual(
            extract_boxed_answer(r"candidate \boxed{1}; final \boxed{2+\sqrt{3}}"),
            r"2+\sqrt{3}",
        )


if __name__ == "__main__":
    unittest.main()
