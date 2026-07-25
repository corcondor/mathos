import json
import tempfile
import unittest
from pathlib import Path

from math_os_prototype.atlas_problem_synthesis import (
    build_charts,
    evaluate_candidate,
    generate_candidates,
    run_atlas_synthesis,
)
from math_os_prototype.creative_benchmark import load_mathos_report


class AtlasProblemSynthesisTests(unittest.TestCase):
    def test_default_atlas_generates_exactly_54_verified_problems(self):
        report = run_atlas_synthesis(limit=54)
        self.assertEqual(report["summary"]["evaluated"], 54)
        self.assertEqual(report["summary"]["verified"], 54)
        self.assertEqual(report["summary"]["rejected"], 0)
        self.assertEqual(len(report["curriculum_items"]), 54)

    def test_every_export_passes_backend_and_lift_gates(self):
        report = run_atlas_synthesis(limit=54)
        for result in report["results"]:
            self.assertTrue(result["verification"]["backend_verified"])
            self.assertTrue(result["verification"]["lift_verified"])
            self.assertIn(
                result["verification"]["expected_family_id"],
                result["verification"]["observed_family_ids"],
            )

    def test_requested_atlas_families_are_covered(self):
        report = run_atlas_synthesis(limit=54)
        counts = report["summary"]["family_counts"]
        expected = {
            "measure_geometry.planar_area",
            "optimization.planar_area_extremum",
            "optimization.positive_definite_quadratic",
            "real_analysis.limit_observable",
            "real_analysis.planar_measure_limit",
            "real_analysis.correlation_limit",
            "measure_geometry.solid_volume",
            "elementary_number_theory.prime_constraint_query",
        }
        self.assertEqual(set(counts), expected)

    def test_candidate_ids_are_unique_and_chart_derived(self):
        candidates = generate_candidates(build_charts())
        ids = [candidate.candidate_id for candidate in candidates]
        self.assertEqual(len(ids), 72)
        self.assertEqual(len(ids), len(set(ids)))
        self.assertTrue(all(value.startswith("atlas:") for value in ids))

    def test_creative_benchmark_loader_preserves_item_family_and_match_group(self):
        report = run_atlas_synthesis(limit=1)
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "atlas.json"
            path.write_text(json.dumps(report, ensure_ascii=False), encoding="utf-8")
            records = load_mathos_report(path)
        self.assertEqual(len(records), 1)
        item = report["curriculum_items"][0]
        self.assertEqual(records[0].family_id, item["family_id"])
        self.assertEqual(records[0].metadata["match_group"], item["match_group"])
        self.assertEqual(records[0].verification["status"], "verified")

    def test_single_candidate_exposes_executable_evidence(self):
        candidate = generate_candidates(build_charts())[0]
        result = evaluate_candidate(candidate, build_charts())
        self.assertEqual(result["phase"], "verified")
        self.assertTrue(result["backend"]["trace"])
        self.assertTrue(result["lift"]["certificates"])

    def test_extended_atlas_adds_inner_product_structures(self):
        report = run_atlas_synthesis(limit=72)
        self.assertEqual(report["summary"]["evaluated"], 72)
        self.assertEqual(report["summary"]["verified"], 72)
        expected = {
            "linear_algebra.frobenius_pairing",
            "linear_algebra.orthogonal_projection",
            "optimization.inner_product_extremum",
            "real_analysis.normalized_inner_product_limit",
            "probability.autocorrelation_function",
        }
        self.assertTrue(expected <= set(report["summary"]["family_counts"]))


if __name__ == "__main__":
    unittest.main()
