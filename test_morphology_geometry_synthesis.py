from __future__ import annotations

import unittest

try:
    from math_os_prototype.entrance_scope import certify_entrance_scope
    from math_os_prototype.morphology_geometry_synthesis import synthesize
except ImportError:  # pragma: no cover
    from entrance_scope import certify_entrance_scope
    from morphology_geometry_synthesis import synthesize


class MorphologyGeometrySynthesisTest(unittest.TestCase):
    def test_two_nonisomorphic_families_are_verified(self) -> None:
        report = synthesize()
        self.assertEqual(report["summary"]["generated"], 2)
        self.assertEqual(report["summary"]["accepted"], 2)
        self.assertEqual(report["summary"]["families"], 2)
        paths = {tuple(problem["morphology_path"]) for problem in report["problems"]}
        self.assertEqual(len(paths), 2)
        for problem in report["problems"]:
            self.assertTrue(problem["proof_graph_certificate"]["interaction_verified"])
            self.assertTrue(problem["morphology_certificate"]["morphism_chain_aligned"])
            self.assertTrue(problem["verification"]["exact_backend"])
            self.assertTrue(problem["verification"]["independent_check"])

    def test_both_families_lower_to_school_mathematics(self) -> None:
        for problem in synthesize()["problems"]:
            certificate = certify_entrance_scope(problem)
            self.assertIsNotNone(certificate)
            self.assertTrue(certificate["uses_only_school_level_primitives"])


if __name__ == "__main__":
    unittest.main()
