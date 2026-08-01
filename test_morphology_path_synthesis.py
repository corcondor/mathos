from __future__ import annotations

import unittest

try:
    from math_os_prototype.entrance_scope import certify_entrance_scope
    from math_os_prototype.morphology_path_synthesis import synthesize
except ImportError:  # pragma: no cover
    from entrance_scope import certify_entrance_scope
    from morphology_path_synthesis import synthesize


class MorphologyPathSynthesisTest(unittest.TestCase):
    def test_distant_domains_are_connected_by_a_verified_long_path(self) -> None:
        problem = synthesize()["problems"][0]
        self.assertTrue(problem["accepted"])
        self.assertEqual(problem["answer_exact"], "9/70")
        self.assertTrue(problem["verification"]["exact_backend"])
        self.assertTrue(problem["verification"]["independent_check"])
        self.assertTrue(problem["proof_graph_certificate"]["interaction_verified"])
        self.assertTrue(problem["morphology_certificate"]["valid"])
        self.assertTrue(problem["morphology_certificate"]["morphism_chain_aligned"])
        self.assertEqual(problem["morphology_certificate"]["edge_count"], 7)
        self.assertEqual(
            problem["verification"]["favorable_count"],
            problem["verification"]["character_filter_count"],
        )

    def test_solution_lowers_to_upper_secondary_operations(self) -> None:
        problem = synthesize()["problems"][0]
        certificate = certify_entrance_scope(problem)
        self.assertIsNotNone(certificate)
        self.assertTrue(certificate["uses_only_school_level_primitives"])


if __name__ == "__main__":
    unittest.main()
