from __future__ import annotations

import unittest

try:
    from math_os_prototype.morphology_graph import (
        certify_morphology_path,
        enumerate_paths,
        shortest_path,
    )
except ImportError:  # pragma: no cover
    from morphology_graph import certify_morphology_path, enumerate_paths, shortest_path


class MorphologyGraphTest(unittest.TestCase):
    def test_rejects_unrelated_scalar_jump(self) -> None:
        certificate = certify_morphology_path(
            ["EuclideanConfiguration", "CombinatorialClass"]
        )
        self.assertFalse(certificate["valid"])
        self.assertEqual(certificate["reason"], "non_adjacent_jump")

    def test_accepts_smooth_quadratic_to_measure_path(self) -> None:
        path = [
            "QuadraticCoefficientFamily",
            "CoefficientLattice",
            "DiscriminantFeasibleLattice",
            "SemialgebraicRegion",
            "MeasureObservable",
            "ConditionalMomentObservable",
        ]
        certificate = certify_morphology_path(path)
        self.assertTrue(certificate["valid"])
        self.assertEqual(certificate["edge_count"], 5)
        self.assertGreaterEqual(certificate["theory_transitions"], 4)
        self.assertIn("real_root_existence", certificate["transported_invariants"])

    def test_distant_domains_require_intermediate_charts(self) -> None:
        path = shortest_path("ComplexConfiguration", "ExpectationObservable")
        self.assertIsNotNone(path)
        self.assertGreaterEqual(len(path or []) - 1, 7)
        self.assertTrue(certify_morphology_path(path)["valid"])

    def test_enumerator_never_skips_an_edge(self) -> None:
        paths = list(
            enumerate_paths(
                "QuadraticCoefficientFamily",
                min_edges=3,
                max_edges=5,
            )
        )
        self.assertTrue(paths)
        self.assertTrue(all(certify_morphology_path(path)["valid"] for path in paths))

    def test_rejects_a_valid_path_attached_to_an_unrelated_solution(self) -> None:
        path = [
            "ComplexConfiguration",
            "CyclicGroupAction",
            "ResidueClassStructure",
            "CharacterSum",
        ]
        certificate = certify_morphology_path(
            path,
            morphism_chain=["RegularPolygon", "AreaObservation"],
        )
        self.assertFalse(certificate["valid"])
        self.assertEqual(certificate["reason"], "morphism_chain_misaligned")

    def test_conditional_shortcut_requires_proved_conditions(self) -> None:
        path = [
            "SymmetricInvariant",
            "AntipodalOrbitStructure",
            "CombinatorialClass",
        ]
        rejected = certify_morphology_path(
            path,
            morphism_chain=["AntipodalFactorization", "CompatibilityClass"],
        )
        self.assertFalse(rejected["valid"])
        self.assertEqual(rejected["reason"], "edge_precondition_unproved")
        accepted = certify_morphology_path(
            path,
            morphism_chain=["AntipodalFactorization", "CompatibilityClass"],
            established_conditions=[
                "unit_roots",
                "four_distinct_roots",
                "vanishing_odd_coefficients",
            ],
        )
        self.assertTrue(accepted["valid"])


if __name__ == "__main__":
    unittest.main()
