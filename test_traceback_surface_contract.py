from __future__ import annotations

import unittest

try:
    from math_os_prototype.build_entrance_pool import _surface_contract
    from math_os_prototype.traceback_engine import cut_problems
except ImportError:  # pragma: no cover
    from build_entrance_pool import _surface_contract
    from traceback_engine import cut_problems


class TracebackSurfaceContractTest(unittest.TestCase):
    def test_fixed_ellipse_observations_publish_the_external_point(self) -> None:
        ellipse = {
            problem.parameters["node"]: problem
            for problem in cut_problems()
            if problem.parameters.get("construction") == "ellipse_tangent"
        }
        for node in (
            "chord_length_sq",
            "tangent_slope_product",
            "contact_triangle_area",
            "chord_midpoint_x",
            "center_to_polar_dist_sq",
        ):
            with self.subTest(node=node):
                problem = ellipse[node]
                self.assertIn("external_point_coordinate", problem.parameters["surface_bindings"])
                self.assertIn(r"P\left(-25,- \frac{15}{2}\right)", problem.statement_tex)

    def test_locus_observation_keeps_the_external_point_free(self) -> None:
        problem = next(
            problem
            for problem in cut_problems()
            if problem.parameters.get("construction") == "ellipse_tangent"
            and problem.parameters.get("node") == "monge_radius_sq"
        )
        self.assertEqual(problem.parameters["required_surface_bindings"], [])
        self.assertNotIn(r"P\left(", problem.statement_tex)

    def test_missing_required_binding_is_rejected(self) -> None:
        certificate = _surface_contract({
            "parameters": {
                "required_surface_bindings": ["external_point_coordinate"],
                "surface_bindings": [],
            },
        })
        self.assertFalse(certificate["valid"])
        self.assertEqual(certificate["missing"], ["external_point_coordinate"])


if __name__ == "__main__":
    unittest.main()
