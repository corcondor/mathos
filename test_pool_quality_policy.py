from __future__ import annotations

import unittest

try:
    from math_os_prototype.build_entrance_pool import (
        _domain_components,
        _morphology_contract,
        _quality_annotations,
    )
except ImportError:  # pragma: no cover
    from build_entrance_pool import (
        _domain_components,
        _morphology_contract,
        _quality_annotations,
    )


class PoolQualityPolicyTest(unittest.TestCase):
    def test_valid_path_without_interacting_proof_is_rejected(self) -> None:
        problem = {
            "morphology_path": [
                "EuclideanConfiguration",
                "CoordinateConfiguration",
            ],
            "lift_certificate": {
                "morphism_chain": ["CoordinateRealization"],
            },
            "proof_graph": {
                "nodes": [
                    {"id": "only", "kind": "object"},
                    {"id": "answer", "kind": "query"},
                ],
                "edges": [{"source": "only", "target": "answer"}],
            },
        }
        reason, morphology, proof = _morphology_contract(problem)
        self.assertTrue(morphology["valid"])
        self.assertFalse(proof["interaction_verified"])
        self.assertEqual(reason, "morphology_without_interacting_proof")

    def test_composite_domains_are_detected_without_family_names(self) -> None:
        self.assertEqual(_domain_components("complex_geometry"), ["complex_geometry"])
        self.assertEqual(
            _domain_components("complex_geometry_combinatorics_probability"),
            ["complex_geometry", "combinatorics", "probability"],
        )
        self.assertEqual(
            _domain_components("probability_linear_algebra_number_theory"),
            ["probability", "linear_algebra", "number_theory"],
        )

    def test_legacy_thresholds_are_annotations_only(self) -> None:
        problem = {"lift_certificate": {"morphism_chain": ["Solve"]}}
        annotations = _quality_annotations(problem, legacy_score=2.0)
        self.assertEqual(annotations["policy"], "annotation_only")
        self.assertFalse(annotations["human_calibrated"])
        self.assertTrue(annotations["below_legacy_difficulty_threshold"])
        self.assertTrue(annotations["below_legacy_morphism_threshold"])
        self.assertLess(
            annotations["observed_human_auc"],
            annotations["minimum_auc_for_gating"],
        )


if __name__ == "__main__":
    unittest.main()
