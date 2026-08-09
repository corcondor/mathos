import unittest

try:
    from math_os_prototype.public_benchmark import (
        PublicBenchmarkCase,
        PublicBenchmarkRecord,
        answers_match,
        benchmark_manifest,
        case_identity,
        classify_failure_layer,
        extract_boxed_answer,
        run_cases_with_persistent_workers,
        summarize,
    )
except ImportError:
    from public_benchmark import (
        PublicBenchmarkCase,
        PublicBenchmarkRecord,
        answers_match,
        benchmark_manifest,
        case_identity,
        classify_failure_layer,
        extract_boxed_answer,
        run_cases_with_persistent_workers,
        summarize,
    )


class PublicBenchmarkAnswerExtractionTests(unittest.TestCase):
    def test_failure_layer_distinguishes_missing_backend_from_missing_plan(self):
        self.assertEqual(
            classify_failure_layer(
                typed_status="type_checked",
                answer=None,
                exact_match=False,
                tool_calls=[],
            ),
            "strategy_or_morphism_gap",
        )
        self.assertEqual(
            classify_failure_layer(
                typed_status="type_checked",
                answer=None,
                exact_match=False,
                tool_calls=[{"name": "lean.check", "executable": False}],
            ),
            "morphism_to_backend_gap",
        )

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

    def test_dfrac_and_plain_rational_are_mathematically_equal(self):
        self.assertTrue(answers_match("9/7", r"\dfrac{9}{7}"))

    def test_radical_coefficient_is_compared_mathematically(self):
        self.assertTrue(answers_match("-3*sqrt(5) - 5", r"-3 \sqrt{5} - 5"))

    def test_manifest_and_partition_are_stable(self):
        case = PublicBenchmarkCase("MATH", "algebra", 7, "Solve $x+1=2$.", "1")
        first = case_identity(case)
        self.assertEqual(first, case_identity(case))
        self.assertEqual(len(first[1]), 64)
        self.assertIn(first[2], {"dev", "calibration", "held_out"})
        self.assertEqual(benchmark_manifest([case]), benchmark_manifest([case]))

    def test_partition_does_not_depend_on_the_hidden_answer(self):
        left = PublicBenchmarkCase("MATH", "algebra", 7, "Solve $x+1=2$.", "1")
        right = PublicBenchmarkCase("MATH", "algebra", 7, "Solve $x+1=2$.", "999")
        self.assertEqual(case_identity(left), case_identity(right))

    def test_interval_answers_are_compared_as_sets(self):
        self.assertTrue(
            answers_match(
                "Union(Interval.open(-oo, -7), Interval.open(1, 2))",
                r"(-\infty,-7) \cup (1,2)",
            )
        )

    def test_vector_and_complex_answers_use_mathematical_equivalence(self):
        self.assertTrue(answers_match("Matrix([6, 3, 0])", r"\begin{pmatrix} 6 \\ 3 \\ 0 \end{pmatrix}"))
        self.assertTrue(answers_match("I", "i"))
        self.assertTrue(answers_match("B, E, G", r"\text{B, E, G}"))

    def test_summary_separates_wrong_answers_from_abstentions(self):
        def record(index, answer, exact, verification="verified"):
            return PublicBenchmarkRecord(
                benchmark="MATH", subset="algebra", index=index, domain="algebra",
                intent="test", typed_status="type_checked", verification=verification,
                expected="1", answer=answer, exact_match=exact, error=None,
                problem_preview="p", case_id=f"MATH:algebra:{index}", problem_hash=str(index) * 64,
                evaluation_partition="held_out", level="Level 5",
            )
        result = summarize([
            record(1, "1", True),
            record(2, "2", False),
            record(3, None, False, "timeout"),
        ])
        self.assertEqual(result["exact_match"], 1)
        self.assertEqual(result["wrong"], 1)
        self.assertEqual(result["abstained"], 1)
        self.assertEqual(result["timeouts"], 1)
        self.assertEqual(result["answer_precision"], 0.5)

    def test_persistent_workers_preserve_input_order_and_case_identity(self):
        cases = [
            PublicBenchmarkCase("MATH", "algebra", 0, "Find $x$ if $x+1=2$.", "1"),
            PublicBenchmarkCase("MATH", "algebra", 1, "Find $y$ if $y+2=4$.", "2"),
        ]
        records = run_cases_with_persistent_workers(
            cases,
            live_retrieval=False,
            external_tools=False,
            allow_surface_morphisms=False,
            timeout=20,
            workers=2,
        )
        self.assertEqual([record.index for record in records], [0, 1])
        self.assertEqual([record.case_id for record in records], ["MATH:algebra:0", "MATH:algebra:1"])


if __name__ == "__main__":
    unittest.main()
