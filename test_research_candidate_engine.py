from __future__ import annotations

import unittest

from research_candidate_engine import (
    TypedMorphism,
    _preserve_stronger_corpus_evidence,
    build_payload,
    screen_known_problem,
    typecheck_chain,
)


class ResearchCandidateEngineTest(unittest.TestCase):
    def test_retains_only_unique_well_typed_structures(self) -> None:
        payload = build_payload()
        self.assertEqual(payload["summary"]["retained"], 12)
        self.assertEqual(payload["summary"]["rejected"], 0)
        self.assertEqual(payload["summary"]["unique_structural_signatures"], 12)
        self.assertEqual(payload["summary"]["unique_query_types"], 12)
        self.assertEqual(payload["summary"]["parameter_variants"], 0)

        candidates = payload["candidates"]
        self.assertTrue(all(item["typecheck"]["passed"] for item in candidates))
        self.assertTrue(all(item["morphism_count"] >= 10 for item in candidates))
        self.assertEqual(
            len({item["structural_signature"] for item in candidates}),
            len(candidates),
        )

    def test_pending_status_never_claims_human_open_problem(self) -> None:
        for candidate in build_payload()["candidates"]:
            self.assertIsNone(candidate["answer_tex"])
            self.assertEqual(
                candidate["answer_status"],
                "unresolved_by_mathos",
            )
            self.assertTrue(candidate["not_claimed_human_open"])

    def test_known_problem_marker_is_not_retained_as_novel(self) -> None:
        self.assertIn(
            "Fermat's Last Theorem",
            screen_known_problem("フェルマーの最終定理を示せ"),
        )
        self.assertIn(
            "Riemann hypothesis",
            screen_known_problem("リーマン予想を証明せよ"),
        )

    def test_typechecker_rejects_invalid_composition(self) -> None:
        chain = (
            TypedMorphism("f", "Point", "Line"),
            TypedMorphism("g", "Circle", "Area"),
        )
        passed, error = typecheck_chain(chain)
        self.assertFalse(passed)
        self.assertIsNotNone(error)

    def test_reduced_ci_corpus_does_not_replace_stronger_evidence(self) -> None:
        current = {"passed": True, "corpus_size": 176}
        previous = {"passed": True, "corpus_size": 28074}
        self.assertIs(
            _preserve_stronger_corpus_evidence(current, previous),
            previous,
        )
        failed = {"passed": False, "corpus_size": 28100}
        self.assertIs(
            _preserve_stronger_corpus_evidence(failed, previous),
            failed,
        )
        approximate = {
            "passed": True,
            "corpus_size": 28074,
            "method": "minhash64_conservative",
        }
        exact = {
            "passed": True,
            "corpus_size": 28074,
            "method": "exact_3gram_jaccard",
        }
        self.assertIs(
            _preserve_stronger_corpus_evidence(approximate, exact),
            exact,
        )


if __name__ == "__main__":
    unittest.main()
