from __future__ import annotations

import unittest

try:
    from math_os_prototype.construct_engine import synthesize
    from math_os_prototype.geometry_deep_families import (
        _geometry_polygon_disk_sweep,
        _geometry_tetrahedron_displacement_locus,
        _geometry_cube_diagonal_section_maximum,
        _geometry_cube_ball_sweep,
        _geometry_triangle_displacement_locus,
    )
except ImportError:  # pragma: no cover
    from construct_engine import synthesize
    from geometry_deep_families import (
        _geometry_polygon_disk_sweep,
        _geometry_tetrahedron_displacement_locus,
        _geometry_cube_diagonal_section_maximum,
        _geometry_cube_ball_sweep,
        _geometry_triangle_displacement_locus,
    )


class GeometryDeepFamiliesTest(unittest.TestCase):
    def test_triangle_displacement_is_symbolic_and_verified(self) -> None:
        problem = _geometry_triangle_displacement_locus({"symbolic": True})
        self.assertIsNotNone(problem)
        self.assertEqual(problem.answer_exact, "6*S")
        self.assertIn("DifferenceBody", problem.morphism_chain)
        self.assertTrue(problem.independent_check)

    def test_polygon_disk_sweep_is_symbolic_and_verified(self) -> None:
        problem = _geometry_polygon_disk_sweep({"symbolic": True})
        self.assertIsNotNone(problem)
        self.assertEqual(problem.answer_exact, "A + r*L + pi*r**2")
        self.assertIn("MinkowskiAddition", problem.morphism_chain)
        self.assertTrue(problem.independent_check)

    def test_minkowski_shard_contains_distinct_structures(self) -> None:
        report = synthesize(only_family="geometry_minkowski_polygon")
        families = {problem["family_id"] for problem in report["problems"]}
        self.assertEqual(
            families,
            {
                "ultradeep.geometry_regular_polygon_minkowski_perimeter",
                "ultradeep.geometry_triangle_displacement_locus_area",
                "ultradeep.geometry_convex_polygon_disk_sweep_area",
            },
        )
        new_records = [
            problem for problem in report["problems"]
            if problem["family_id"] != "ultradeep.geometry_regular_polygon_minkowski_perimeter"
        ]
        self.assertTrue(all(problem["conceptual_bridge"]["necessary"] for problem in new_records))
        self.assertTrue(all(problem["conceptual_bridge"]["edge_ablation"] for problem in new_records))

    def test_tetrahedron_displacement_volume_is_verified(self) -> None:
        problem = _geometry_tetrahedron_displacement_locus({"symbolic": True})
        self.assertIsNotNone(problem)
        self.assertEqual(problem.answer_exact, "20*V")
        self.assertIn("ThreeDimensionalDifferenceBody", problem.morphism_chain)
        self.assertTrue(problem.independent_check)

    def test_cube_diagonal_section_maximum_is_verified(self) -> None:
        problem = _geometry_cube_diagonal_section_maximum({"symbolic": True})
        self.assertIsNotNone(problem)
        self.assertIn("3*sqrt(3)*a**2/4", problem.answer_exact)
        self.assertIn("SliceVolumeCorrespondence", problem.morphism_chain)
        self.assertTrue(problem.independent_check)

    def test_cube_ball_sweep_volume_is_verified(self) -> None:
        problem = _geometry_cube_ball_sweep({"symbolic": True})
        self.assertIsNotNone(problem)
        self.assertIn("4*pi*r**3/3", problem.answer_exact)
        self.assertIn("ThreeDimensionalMinkowskiAddition", problem.morphism_chain)
        self.assertTrue(problem.independent_check)

    def test_spatial_shard_contains_three_distinct_structures(self) -> None:
        report = synthesize(only_family="geometry_spatial")
        families = {problem["family_id"] for problem in report["problems"]}
        self.assertEqual(
            families,
            {
                "ultradeep.spatial_tetrahedron_displacement_locus_volume",
                "ultradeep.spatial_cube_diagonal_section_maximum",
                "ultradeep.spatial_cube_ball_sweep_volume",
            },
        )
        self.assertTrue(
            all(problem["conceptual_bridge"]["necessary"] for problem in report["problems"])
        )


if __name__ == "__main__":
    unittest.main()
