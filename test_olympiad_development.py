import unittest
from unittest.mock import patch

from pathlib import Path

try:
    from math_os_prototype.olympiad_development import (
        OlympiadCase,
        evaluate_case,
        evaluate_worker_cases,
        partition_for_cluster,
        row_to_case,
        structural_signature,
    )
    from math_os_prototype.corpus_lift_protocol import is_frozen_selfauthored_source, load_tex_cases
except ImportError:
    from olympiad_development import (
        OlympiadCase,
        evaluate_case,
        evaluate_worker_cases,
        partition_for_cluster,
        row_to_case,
        structural_signature,
    )
    from corpus_lift_protocol import is_frozen_selfauthored_source, load_tex_cases


class OlympiadDevelopmentTests(unittest.TestCase):
    def test_numeric_variants_share_structure_cluster(self):
        left = structural_signature(
            "Find all primes p such that p^2 + 3 is divisible by 7.",
            topics=["Number Theory > Congruences"],
            problem_type="answer",
        )
        right = structural_signature(
            "Find all primes p such that p^5 + 19 is divisible by 31.",
            topics=["Number Theory > Congruences"],
            problem_type="answer",
        )
        self.assertEqual(left, right)
        self.assertEqual(partition_for_cluster(left), partition_for_cluster(right))

    def test_row_does_not_store_worked_solution(self):
        case = row_to_case(
            {
                "id": "secret-id",
                "problem_markdown": "Find $x$ if $x+2=5$.",
                "solutions_markdown": ["This must never enter the solver."],
                "final_answer": "3",
                "country": "Test",
                "competition": "Test Olympiad",
                "topics_flat": ["Algebra > Equations"],
                "problem_type": "answer",
            }
        )
        self.assertFalse(hasattr(case, "solutions_markdown"))
        self.assertNotIn("solution", case.problem.lower())

    def test_evaluator_passes_only_statement_to_compilers(self):
        case = OlympiadCase(
            corpus_id="not-a-solver-input",
            problem="Find $x$ if $x+2=5$.",
            expected="3",
            country="Test",
            competition="Test",
            topics=("Algebra > Equations",),
            language="en",
            problem_type="answer",
            structure_cluster_id="0" * 20,
            partition="development",
        )
        module = evaluate_case.__module__
        with patch(f"{module}.compile_typed_semantic_graph") as graph_compile, patch(
            f"{module}.compile_typed_definition_ir"
        ) as typed_compile:
            graph_compile.return_value.to_dict.return_value = {
                "status": "partial",
                "sorts": [],
                "morphisms": [],
                "constraints": [],
                "queries": [],
                "lift_certificates": [],
            }
            typed_compile.return_value.to_dict.return_value = {
                "status": "needs_review",
                "backend_obligations": [],
            }
            evaluate_case(case)
        graph_compile.assert_called_once_with(case.problem)
        typed_compile.assert_called_once_with(case.problem)

    def test_selfauthored_corpus_is_frozen_by_default(self):
        path = Path("全問題.tex")
        self.assertTrue(is_frozen_selfauthored_source(path))
        with self.assertRaisesRegex(ValueError, "frozen for final validation"):
            load_tex_cases([path])

    def test_worker_evaluator_receives_statement_without_answers_or_labels(self):
        case = OlympiadCase(
            corpus_id="secret-corpus-id",
            problem="For every integer n, prove that n(n+1) is even.",
            expected="proof hidden from worker",
            country="Hidden Country",
            competition="Hidden Competition",
            topics=("Number Theory > Divisibility",),
            language="en",
            problem_type="proof",
            structure_cluster_id="1" * 20,
            partition="development",
        )
        module = evaluate_worker_cases.__module__
        output = {
            "status": "goal_reached",
            "atlas_size": 100,
            "root_sorts": ["Integer"],
            "query_sorts": ["Proof"],
            "morphisms": ["PropositionCertification"],
            "language_analysis": {"parse_count": 1, "constraints": [{"operator": "="}]},
            "states_explored": 3,
            "goal_count": 1,
            "first_goal": {"steps": [{"morphism": "PropositionCertification"}]},
        }
        with patch(f"{module}.evaluate_with_worker", return_value=[output]) as bridge:
            records = evaluate_worker_cases([case])
        request = bridge.call_args.args[0][0]
        self.assertEqual(request["statement"], case.problem)
        self.assertNotIn(case.expected, request.values())
        self.assertNotIn(case.corpus_id, request.values())
        self.assertNotIn(case.competition, request.values())
        self.assertEqual(records[0].status, "goal_reached")


if __name__ == "__main__":
    unittest.main()
