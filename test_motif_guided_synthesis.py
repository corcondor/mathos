from __future__ import annotations

import unittest

try:
    from math_os_prototype.entrance_scope import certify_entrance_scope
    from math_os_prototype.motif_guided_synthesis import synthesize
    from math_os_prototype.proof_graph import certify_proof_graph
except ImportError:  # pragma: no cover
    from entrance_scope import certify_entrance_scope
    from motif_guided_synthesis import synthesize
    from proof_graph import certify_proof_graph


class MotifGuidedSynthesisTest(unittest.TestCase):
    def test_candidate_is_exact_and_has_interacting_proof_graph(self) -> None:
        problem = synthesize()["problems"][0]
        self.assertTrue(problem["accepted"])
        self.assertEqual(problem["answer_exact"], ["1/12", "1/2"])
        self.assertTrue(problem["verification"]["exact_backend"])
        self.assertTrue(problem["verification"]["independent_check"])
        self.assertTrue(problem["verification"]["semantic_chain_check"]["passed"])
        self.assertEqual(problem["verification"]["semantic_chain_check"]["missing"], [])
        self.assertTrue(certify_proof_graph(problem["proof_graph"])["interaction_verified"])
        self.assertTrue(problem["morphology_certificate"]["valid"])
        self.assertTrue(problem["morphology_certificate"]["morphism_chain_aligned"])
        self.assertEqual(problem["morphology_certificate"]["edge_count"], 5)
        self.assertIn(r"\[", problem["statement_tex"])
        self.assertNotIn("\n[\n", problem["statement_tex"])

    def test_candidate_lowers_to_upper_secondary_operations(self) -> None:
        problem = synthesize()["problems"][0]
        certificate = certify_entrance_scope(problem)
        self.assertIsNotNone(certificate)
        self.assertTrue(certificate["uses_only_school_level_primitives"])


if __name__ == "__main__":
    unittest.main()
