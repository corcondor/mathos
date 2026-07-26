from __future__ import annotations

import unittest

from autonomous_morphism_search import (
    ATLAS,
    DOMAINS,
    AtlasMorphism,
    grow_payload,
    quotient_signature,
    search_chain,
    similarity_limit,
    structural_similarity,
    typecheck_chain,
)
from research_candidate_engine import build_payload


class AutonomousMorphismSearchTest(unittest.TestCase):
    def test_atlas_search_returns_only_composable_deep_chains(self) -> None:
        import random

        for index, domain in enumerate(DOMAINS):
            chain = search_chain(domain, 10, random.Random(index))
            self.assertIsNotNone(chain, domain.name)
            passed, error = typecheck_chain(chain or ())
            self.assertTrue(passed, error)
            self.assertEqual(len(chain or ()), 10)

    def test_quotient_erases_numeric_labels_and_normalizes_commuting_runs(self) -> None:
        left = (
            AtlasMorphism("F2", "X", "X", "", "d", "F2", commutation_group="g"),
            AtlasMorphism("G9", "X", "X", "", "d", "G9", commutation_group="g"),
            AtlasMorphism("Q", "X", "Classification", "", "d", "Q", True, "q"),
        )
        right = (
            AtlasMorphism("G3", "X", "X", "", "d", "G3", commutation_group="g"),
            AtlasMorphism("F8", "X", "X", "", "d", "F8", commutation_group="g"),
            AtlasMorphism("Q", "X", "Classification", "", "d", "Q", True, "q"),
        )
        self.assertEqual(
            quotient_signature(left, ("c2",)),
            quotient_signature(right, ("c9",)),
        )

    def test_growth_adds_unique_non_parameter_structures(self) -> None:
        payload = grow_payload(build_payload(), None, count=12, seed=42)
        generated = [
            item
            for item in payload["candidates"]
            if item.get("origin") == "autonomous_atlas_search"
        ]
        self.assertEqual(len(generated), 12)
        self.assertEqual(len({item["quotient_signature"] for item in generated}), 12)
        self.assertTrue(all(item["morphism_count"] >= 10 for item in generated))
        self.assertTrue(all(item["answer_tex"] is None for item in generated))
        self.assertTrue(all(item["typecheck"]["passed"] for item in generated))
        self.assertTrue(
            all(
                item["effective_morphism_count"]
                >= int(item["morphism_count"] * 0.85)
                for item in generated
            )
        )
        self.assertEqual(
            set(payload["autonomous_search"]["domain_counts"]),
            {domain.name for domain in DOMAINS},
        )
        self.assertTrue(
            all(
                count == 2
                for count in payload["autonomous_search"]["domain_counts"].values()
            )
        )
        self.assertTrue(
            all(
                item["search_trace"]["nearest_prior_structural_similarity"] < 0.82
                for item in generated
            )
        )
        self.assertTrue(
            all(
                item["search_trace"]["nearest_prior_structural_similarity"]
                < item["search_trace"]["similarity_limit"]
                for item in generated
            )
        )

    def test_previous_generation_is_retained_and_depth_floor_increases(self) -> None:
        first = grow_payload(build_payload(), None, count=4, seed=10)
        second = grow_payload(build_payload(), first, count=4, seed=11)
        third = grow_payload(build_payload(), second, count=4, seed=12)
        self.assertEqual(first["autonomous_search"]["epoch"], 1)
        self.assertEqual(second["autonomous_search"]["epoch"], 2)
        self.assertEqual(third["autonomous_search"]["epoch"], 3)
        self.assertEqual(third["autonomous_search"]["depth_floor"], 11)
        self.assertEqual(third["summary"]["autonomous_candidates"], 12)
        paused = grow_payload(build_payload(), third, count=0, seed=13)
        self.assertEqual(paused["autonomous_search"]["epoch"], 3)
        self.assertEqual(paused["summary"]["autonomous_candidates"], 12)

    def test_structural_similarity_distinguishes_reordered_noncommuting_paths(self) -> None:
        self.assertLess(
            structural_similarity("X|A/B/C/Q|Y|c", "X|A/C/B/Q|Y|c"),
            1.0,
        )

    def test_deeper_search_has_a_stricter_similarity_limit(self) -> None:
        self.assertEqual(similarity_limit(10), 0.82)
        self.assertLess(similarity_limit(20), similarity_limit(10))
        self.assertEqual(similarity_limit(100), 0.55)

    def test_every_atlas_edge_has_a_valid_domain_and_description(self) -> None:
        domains = {domain.name for domain in DOMAINS}
        self.assertTrue(ATLAS)
        self.assertTrue(all(edge.domain in domains for edge in ATLAS))
        self.assertTrue(all(edge.description_ja for edge in ATLAS))


if __name__ == "__main__":
    unittest.main()
