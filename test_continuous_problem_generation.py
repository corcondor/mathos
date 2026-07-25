from __future__ import annotations

import unittest

import sympy as sp

from math_os_prototype.continuous_problem_generation import (
    bridge_expected_zero_count,
    build_all_candidates,
    build_batch_report,
    build_bridge_zero_problem,
    build_cycle_laplacian_problem,
    build_gcd_determinant_problem,
    build_interpolation_problem,
    chain_signature,
    collect_structural_signatures,
    compare_novelty,
    finite_field_triple_count,
    load_external_corpus,
    predicted_finite_field_count,
    prime_inverse_square_product,
    type_check_chain,
)
from math_os_prototype.semantic_repair_loop import (
    compile_repair_forest,
    select_candidate,
)


class ContinuousProblemGenerationTests(unittest.TestCase):
    def test_all_charts_have_distinct_families_and_verify(self) -> None:
        candidates = build_all_candidates()
        self.assertEqual(len(candidates), 21)
        self.assertEqual(len({item.family_id for item in candidates}), 21)
        for candidate in candidates:
            with self.subTest(candidate=candidate.candidate_id):
                chain_ok, errors = type_check_chain(
                    candidate.morphisms,
                    candidate.query_sort,
                )
                self.assertTrue(chain_ok, errors)
                self.assertTrue(candidate.verification.exact_backend)
                self.assertTrue(candidate.verification.independent_check)

    def test_finite_field_count_matches_piecewise_law(self) -> None:
        for prime in list(sp.primerange(2, 50)):
            with self.subTest(prime=prime):
                self.assertEqual(
                    finite_field_triple_count(prime),
                    predicted_finite_field_count(prime),
                )

    def test_random_bridge_observable(self) -> None:
        for n in range(1, 7):
            with self.subTest(n=n):
                expected = sp.Rational(4**n, sp.binomial(2 * n, n)) - 1
                self.assertEqual(bridge_expected_zero_count(n), expected)

    def test_prime_product_phase(self) -> None:
        for prime in list(sp.primerange(3, 100)):
            with self.subTest(prime=prime):
                expected = 0 if prime % 4 == 1 else 4 % prime
                self.assertEqual(prime_inverse_square_product(prime), expected)

    def test_empty_corpus_accepts_verified_distinct_structures(self) -> None:
        report = build_batch_report([], [], [])
        self.assertEqual(report["summary"]["generated"], 21)
        self.assertEqual(report["summary"]["accepted"], 21)
        self.assertTrue(report["summary"]["all_backend_verified"])
        self.assertTrue(report["summary"]["all_certificates_type_checked"])
        self.assertTrue(report["summary"]["all_structurally_novel"])

    def test_structural_signature_collision_rejects_reused_recipe(self) -> None:
        candidates = build_all_candidates()
        target = candidates[0]
        # A prior batch that already used this family blocks re-acceptance even
        # though the surface corpus is empty.
        novelty = compare_novelty(
            target,
            [],
            [],
            [],
            [],
            prior_families={target.family_id},
            prior_chains=set(),
        )
        self.assertTrue(novelty["surface_novel"])
        self.assertFalse(novelty["structural"]["structural_novel"])
        self.assertFalse(novelty["corpus_novel"])

        chain = chain_signature(item.name for item in target.morphisms)
        by_chain = compare_novelty(
            target, [], [], [], [], prior_families=set(), prior_chains={chain}
        )
        self.assertTrue(by_chain["structural"]["chain_collision"])
        self.assertFalse(by_chain["corpus_novel"])

    def test_prior_signatures_block_matching_candidates_in_batch(self) -> None:
        candidates = build_all_candidates()
        blocked = candidates[3].family_id
        report = build_batch_report(
            [], [], [], [], prior_families={blocked}, prior_chains=set()
        )
        by_family = {
            record["family_id"]: record for record in report["problems"]
        }
        self.assertFalse(by_family[blocked]["accepted"])
        self.assertEqual(report["summary"]["accepted"], 20)

    def test_collect_structural_signatures_walks_mixed_schemas(self) -> None:
        families: set[str] = set()
        chains: set[str] = set()
        payload = {
            "method": {
                "family_id": "kyoto.demo",
                "morphism_chain": ["A", "B", "C"],
            },
            "problems": [
                {
                    "family_id": "batch.demo",
                    "morphisms": [{"name": "X"}, {"name": "Y"}],
                }
            ],
        }
        collect_structural_signatures(payload, families, chains)
        self.assertIn("kyoto.demo", families)
        self.assertIn("batch.demo", families)
        self.assertIn("A>B>C", chains)
        self.assertIn("X>Y", chains)

    def test_external_corpus_loading_is_optional(self) -> None:
        from pathlib import Path

        rows = load_external_corpus(
            parquet_paths=[Path("does_not_exist.parquet")],
            jsonl_paths=[Path("also_missing.jsonl")],
        )
        self.assertEqual(rows, [])

    def test_generic_semantic_operators_are_not_problem_id_rules(self) -> None:
        cases = [
            (build_interpolation_problem(), ["Evaluation"]),
            (
                build_cycle_laplacian_problem(),
                ["Laplacian", "Eigenvalues", "FiniteProduct"],
            ),
            (build_bridge_zero_problem(), ["Expectation"]),
            (build_gcd_determinant_problem(), ["Determinant"]),
        ]
        for problem, expected_chain in cases:
            with self.subTest(problem=problem.candidate_id):
                selected = select_candidate(
                    compile_repair_forest(problem.statement_tex)
                )
                self.assertEqual(selected.morphism_chain, expected_chain)
                self.assertTrue(selected.type_checked)


if __name__ == "__main__":
    unittest.main()
