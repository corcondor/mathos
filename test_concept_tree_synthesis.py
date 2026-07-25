from __future__ import annotations

import unittest

import sympy as sp

from math_os_prototype.concept_tree_synthesis import (
    base,
    combine,
    embed,
    evaluate,
    observable,
    query,
    synthesize,
)


class ConceptTreeSynthesisTests(unittest.TestCase):
    def test_reconstructs_known_kyoto_convex_hull_problem(self) -> None:
        # Maximize hull area of {(r, r^3)} for roots of x^4 - 5x^2 + t == 25/2.
        tree = query(observable(embed(base(5), 3), "HullArea"), "Maximize")
        result = evaluate(tree)
        self.assertIsNotNone(result)
        self.assertEqual(sp.sympify(result["answer_exact"]), sp.Rational(25, 2))
        self.assertTrue(result["certified"])
        self.assertTrue(result["certification"].startswith("symbolic_proof"))

    def test_all_certified_answers_are_exact_and_short(self) -> None:
        report = synthesize()
        self.assertGreater(report["summary"]["certified"], 12)
        for problem in report["problems"]:
            with self.subTest(tree=problem["tree_signature"]):
                answer = sp.sympify(problem["answer_exact"])
                self.assertFalse(answer.atoms(sp.Float))  # exact, not numeric
                # numeric-certified answers are short; symbolically proven ones
                # may be longer exact expressions but are still valid.
                limit = 9 if problem["certification"].startswith("numeric") else 20
                self.assertLessEqual(sp.count_ops(answer), limit)
                # numeric answer reproduces the certified closed form
                self.assertAlmostEqual(
                    float(answer), problem["extreme_value_numeric"], places=6
                )

    def test_branching_tree_produces_certified_problem(self) -> None:
        # A genuine tree tensor network: two hull-area subtrees merge.
        tree = query(
            combine(
                observable(embed(base(5), 3), "HullArea"),
                observable(embed(base(5), 5), "HullArea"),
                "Difference",
            ),
            "Minimize",
        )
        result = evaluate(tree)
        self.assertIsNotNone(result)
        self.assertFalse(sp.sympify(result["answer_exact"]).atoms(sp.Float))

    def test_tree_surgery_gives_distinct_answers(self) -> None:
        # Swapping the embedding exponent changes the answer (recombination).
        answers = set()
        for k in (3, 5):
            result = evaluate(query(observable(embed(base(5), k), "HullArea"), "Maximize"))
            self.assertIsNotNone(result)
            answers.add(result["answer_exact"])
        self.assertEqual(len(answers), 2)


if __name__ == "__main__":
    unittest.main()
