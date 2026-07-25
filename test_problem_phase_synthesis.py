import unittest
from fractions import Fraction

from math_os_prototype.problem_phase_synthesis import (
    CandidateProblem,
    GeometrySweepCandidate,
    evaluate_candidate,
    evaluate_geometry_candidate,
    repair_geometry_candidate,
    repair_candidate,
    run_geometry_phase_synthesis,
    run_geometry_repair_experiment,
    run_repair_experiment,
    run_phase_synthesis,
)
from math_os_prototype.synthetic_curriculum_benchmark import run_curriculum_benchmark


class ProblemPhaseSynthesisTest(unittest.TestCase):
    def test_floor_log_finite_boundary_has_closed_form(self):
        candidate = CandidateProblem(
            candidate_id="test",
            alpha=Fraction(1, 2),
            beta=Fraction(-2, 1),
            gamma=3,
            p=Fraction(1, 1),
        )
        result = evaluate_candidate(candidate)
        self.assertEqual(result.phase, "finite_closed")
        self.assertEqual(result.answer, "1/(2e)")
        self.assertIn("good_candidate", result.labels)
        self.assertEqual(result.solver_trace["status"], "supports_limit")

    def test_floor_log_phase_changes_with_power(self):
        base = dict(candidate_id="test", alpha=Fraction(2, 1), beta=Fraction(-3, 1), gamma=2)
        divergent = evaluate_candidate(CandidateProblem(**base, p=Fraction(0, 1)))
        vanishing = evaluate_candidate(CandidateProblem(**base, p=Fraction(2, 1)))
        self.assertEqual(divergent.phase, "divergent")
        self.assertEqual(vanishing.phase, "vanishing")
        self.assertTrue(divergent.degenerate)
        self.assertTrue(vanishing.degenerate)

    def test_phase_synthesis_returns_top_candidates(self):
        diagram = run_phase_synthesis(limit=120, top_k=5)
        self.assertEqual(diagram.total_candidates, 120)
        self.assertGreater(diagram.phase_counts.get("finite_closed", 0), 0)
        self.assertGreater(len(diagram.top_candidates), 0)

    def test_repair_loop_moves_invalid_candidate_to_good_finite_candidate(self):
        candidate = CandidateProblem(
            candidate_id="repair-unit",
            alpha=Fraction(1, 2),
            beta=Fraction(-3, 1),
            gamma=0,
            p=Fraction(0, 1),
        )
        trace = repair_candidate(candidate, max_steps=4)
        self.assertTrue(trace.successful)
        self.assertEqual(trace.original["phase"], "invalid_domain")
        self.assertEqual(trace.final["phase"], "finite_closed")
        self.assertEqual(trace.final["answer"], "1/(2e)")
        self.assertGreaterEqual(len(trace.steps), 2)

    def test_repair_experiment_reports_transition_summary(self):
        report = run_repair_experiment(limit=120, repair_limit=30, max_steps=4, top_k=5)
        self.assertEqual(report["summary"]["attempted"], 30)
        self.assertGreater(report["summary"]["successful"], 0)
        self.assertIn("invalid_domain -> finite_closed", report["summary"]["transitions"])
        self.assertGreater(len(report["top_repaired_candidates"]), 0)

    def test_geometry_sweep_region_uses_existing_dsl_backend(self):
        candidate = GeometrySweepCandidate(
            candidate_id="geo-region",
            task="region",
            a=1,
            b=-1,
            c=0,
            d=0,
        )
        result = evaluate_geometry_candidate(candidate)
        self.assertEqual(result["phase"], "closed_region")
        self.assertEqual(result["answer"], "y <= x**2/4")
        self.assertEqual(result["normal_form"]["normal_form"], "x**2 - 4*y >= 0")
        self.assertEqual(result["execution"]["problem"]["task"], "region")

    def test_geometry_sweep_envelope_uses_existing_dsl_backend(self):
        candidate = GeometrySweepCandidate(
            candidate_id="geo-envelope",
            task="envelope",
            a=1,
            b=-1,
            c=0,
            d=0,
        )
        result = evaluate_geometry_candidate(candidate)
        self.assertEqual(result["phase"], "closed_envelope")
        self.assertEqual(result["answer"], "-x**2 + 4*y = 0")
        self.assertEqual(result["normal_form"]["normal_form"], "x**2 - 4*y = 0")
        self.assertEqual(result["execution"]["problem"]["task"], "envelope")

    def test_geometry_phase_synthesis_returns_region_and_envelope_candidates(self):
        report = run_geometry_phase_synthesis(limit=96, top_k=6)
        self.assertEqual(report["total_candidates"], 96)
        self.assertGreater(report["phase_counts"].get("closed_region", 0), 0)
        self.assertGreater(report["phase_counts"].get("closed_envelope", 0), 0)
        tasks = {item["candidate"]["task"] for item in report["top_candidates"]}
        self.assertIn("region", tasks)
        self.assertIn("envelope", tasks)
        normal_forms = [item["normal_form"]["normal_form"] for item in report["top_candidates"]]
        self.assertEqual(len(normal_forms), len(set(normal_forms)))

    def test_geometry_repair_loop_repairs_partial_region(self):
        candidate = GeometrySweepCandidate(
            candidate_id="geo-repair",
            task="region",
            a=1,
            b=0,
            c=0,
            d=0,
        )
        trace = repair_geometry_candidate(candidate, max_steps=4)
        self.assertTrue(trace["successful"])
        self.assertEqual(trace["original"]["phase"], "partial_region")
        self.assertEqual(trace["final"]["phase"], "closed_region")
        self.assertIn("normal_form", trace["final"])

    def test_geometry_repair_experiment_exports_curriculum_items(self):
        report = run_geometry_repair_experiment(limit=96, repair_limit=20, max_steps=4, top_k=6)
        self.assertEqual(report["summary"]["attempted"], 20)
        self.assertGreater(report["summary"]["successful"], 0)
        self.assertGreater(len(report["curriculum_items"]), 0)

    def test_synthetic_curriculum_benchmark_grades_by_normal_form(self):
        item = {
            "source": "unit",
            "input_tex": "実数$t$に対して，曲線\\[y=tx-t^2+1\\]が定まる。この曲線族の通過領域を求めよ。",
            "dsl": "task region; family y = t*x - t**2 + 1; param t in R",
            "task": "region",
            "expected_answer": "y <= (x**2 + 4)/4",
            "normal_form": {
                "kind": "region",
                "normal_form": "x**2 - 4*y + 4 >= 0",
                "boundary_polynomial": "x**2 - 4*y + 4",
                "operator": ">=",
                "parse_status": "ok",
            },
        }
        report = run_curriculum_benchmark([item], modes=["tex", "dsl", "tex_mutation", "full_tex"], limit=None)
        self.assertEqual(report["summary"]["overall"]["correct"], 4)
        self.assertEqual(report["summary"]["overall"]["exact_rate"], 1.0)


if __name__ == "__main__":
    unittest.main()
