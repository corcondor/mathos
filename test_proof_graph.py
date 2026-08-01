from __future__ import annotations

import unittest

try:
    from math_os_prototype.proof_graph import certify_proof_graph
except ImportError:  # pragma: no cover
    from proof_graph import certify_proof_graph


class ProofGraphTest(unittest.TestCase):
    def test_rejects_flat_chain_as_interaction(self) -> None:
        graph = {
            "nodes": [
                {"id": "a", "kind": "object"},
                {"id": "b", "kind": "transform"},
                {"id": "q", "kind": "query"},
            ],
            "edges": [
                {"source": "a", "target": "b"},
                {"source": "b", "target": "q"},
            ],
        }
        certificate = certify_proof_graph(graph)
        self.assertTrue(certificate["valid_dag"])
        self.assertFalse(certificate["interaction_verified"])

    def test_accepts_two_constraints_that_converge(self) -> None:
        graph = {
            "nodes": [
                {"id": "object", "kind": "object"},
                {"id": "constraint", "kind": "constraint"},
                {"id": "lemma", "kind": "lemma"},
                {"id": "query", "kind": "query"},
            ],
            "edges": [
                {"source": "object", "target": "lemma"},
                {"source": "constraint", "target": "lemma"},
                {"source": "lemma", "target": "query"},
            ],
        }
        certificate = certify_proof_graph(graph)
        self.assertTrue(certificate["interaction_verified"])
        self.assertEqual(certificate["merge_count"], 1)

    def test_rejects_cycle(self) -> None:
        graph = {
            "nodes": [
                {"id": "a", "kind": "object"},
                {"id": "b", "kind": "query"},
            ],
            "edges": [
                {"source": "a", "target": "b"},
                {"source": "b", "target": "a"},
            ],
        }
        self.assertEqual(certify_proof_graph(graph)["reason"], "cycle_detected")


if __name__ == "__main__":
    unittest.main()

