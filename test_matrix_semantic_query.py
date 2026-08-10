from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

try:
    from math_os_prototype.category_semantics import compile_typed_semantic_graph
    from math_os_prototype.diagram_feedback import observe_circle_witness
    from math_os_prototype.matrix_semantic_query import compile_matrix_semantic_query, execute_matrix_semantic_query
except ImportError:
    from category_semantics import compile_typed_semantic_graph
    from diagram_feedback import observe_circle_witness
    from matrix_semantic_query import compile_matrix_semantic_query, execute_matrix_semantic_query


class MatrixSemanticQueryTests(unittest.TestCase):
    def execute(self, problem: str) -> dict:
        ir = compile_matrix_semantic_query(problem)
        self.assertIsNotNone(ir)
        assert ir is not None
        result = execute_matrix_semantic_query(ir.to_dict())
        self.assertTrue(result["verified"])
        self.assertEqual(result["lowering_certificate"]["kind"], "typed_matrix_chart")
        return result

    def test_parameter_region_uses_discriminant_matrix(self) -> None:
        result = self.execute(
            "If $m$ is real and $2x^2+mx+8$ has two distinct real roots, "
            "what are the possible values of $m$?"
        )
        self.assertEqual(result["answer_exact"], "Union(Interval.open(-oo, -8), Interval.open(8, oo))")
        self.assertEqual(result["matrix_witness"]["determinant"], "(m - 8)*(m + 8)")

    def test_root_incidence_solves_parameter(self) -> None:
        result = self.execute(
            r"For what real value of $k$ is $\frac{13-\sqrt{131}}{4}$ a root of $2x^2-13x+k$?"
        )
        self.assertEqual(result["answer_exact"], "19/4")

    def test_root_incidence_accepts_equation_form(self) -> None:
        result = self.execute(
            r"If $3+\sqrt{5}$ is a root of $x^2-3x+b=0$, compute $b$."
        )
        self.assertEqual(result["answer_exact"], "-3*sqrt(5) - 5")

    def test_point_incidence_builds_evaluation_matrix(self) -> None:
        result = self.execute(
            "A parabola $ax^2+bx+c$ contains the points $(-1,0)$, $(0,5)$, and $(5,0)$. "
            "Find $100a+10b+c$."
        )
        self.assertEqual(result["answer_exact"], "-55")
        self.assertEqual(result["matrix_witness"]["rank"], 3)

    def test_circle_uses_homogeneous_quadratic_form_and_pixel_feedback(self) -> None:
        result = self.execute("Find the radius of the circle $x^2+8x+y^2-6y=0$.")
        self.assertEqual(result["answer_exact"], "5")
        self.assertTrue(result["diagram_observation"]["verified"])

    def test_circle_coordinate_extremum_uses_same_conic_matrix(self) -> None:
        result = self.execute(
            "Let $(x,y)$ satisfy $x^2+y^2=14x+48y$. What is the maximum value of $y$?"
        )
        self.assertEqual(result["answer_exact"], "49")
        self.assertEqual(result["matrix_witness"]["observation"], "maximum_y")

    def test_graph_distance_uses_gram_lift(self) -> None:
        result = self.execute(
            r"The smallest distance from the origin to the graph $y=\frac12x^2-9$ is $a$. Find $a^2$."
        )
        self.assertEqual(result["answer_exact"], "17")
        self.assertEqual(result["representation"]["kind"], "gram_distance_lift")

    def test_rational_root_integer_projection(self) -> None:
        result = self.execute(
            "Find all positive integer values of $c$ such that $x^2-7x+c=0$ "
            "only has roots that are real and rational."
        )
        self.assertEqual(result["answer_exact"], "12, 10, 6")

    def test_prime_roots_project_through_vieta_map(self) -> None:
        result = self.execute(
            "Suppose the roots of $x^2-mx+n$ are positive prime integers. "
            "Given $m<20$, how many possible values of $n$ are there?"
        )
        self.assertEqual(result["answer_exact"], "18")

    def test_root_region_can_be_observed_as_finite_probability(self) -> None:
        result = self.execute(
            "Choose an integer $n$ between $1$ and $10$ inclusive. What is the probability "
            "that $x(x+5)=-n$ has no real solutions?"
        )
        self.assertEqual(result["answer_exact"], "2/5")

    def test_numeric_changes_preserve_chart_not_answer(self) -> None:
        first = compile_matrix_semantic_query("If $m$ is real and $2x^2+mx+8$ has two distinct real roots, find the values of $m$.")
        second = compile_matrix_semantic_query("If $m$ is real and $3x^2+mx+12$ has two distinct real roots, find the values of $m$.")
        self.assertIsNotNone(first)
        self.assertIsNotNone(second)
        assert first is not None and second is not None
        self.assertEqual(first.chart, second.chart)
        self.assertEqual(first.query_operator, second.query_operator)
        self.assertNotEqual(
            execute_matrix_semantic_query(first.to_dict())["answer_exact"],
            execute_matrix_semantic_query(second.to_dict())["answer_exact"],
        )

    def test_matrix_chart_is_preserved_in_shared_semantic_graph(self) -> None:
        ir = compile_matrix_semantic_query(
            "If $m$ is real and $2x^2+mx+8$ has two distinct real roots, find the values of $m$."
        )
        self.assertIsNotNone(ir)
        assert ir is not None
        graph = compile_typed_semantic_graph("", matrix_query_ir=ir.to_dict())
        self.assertTrue(any(item.source == "matrix_query_ir" for item in graph.morphisms))
        self.assertEqual(graph.queries[0].kind, "quadratic_parameter_region")

    def test_diagram_observer_can_emit_an_inspectable_image(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "circle.png"
            certificate = observe_circle_witness(
                {"center": ["-4", "3"], "radius_squared": "25"},
                image_path=path,
            )
            self.assertTrue(certificate["verified"])
            self.assertTrue(path.exists())

    def test_indefinite_quadratic_form_center(self) -> None:
        result = self.execute("Find the center of the hyperbola $4x^2-6x+2=y^2-10y$.")
        self.assertEqual(result["answer_exact"], "(3/4, 5)")
        self.assertEqual(result["query_operator"], "quadratic_form_center")

    def test_indefinite_quadratic_distance_minimum(self) -> None:
        result = self.execute(
            "Find the shortest distance from the origin to the hyperbola $x^2+8xy+7y^2=225$."
        )
        self.assertEqual(result["answer_exact"], "5")

    def test_ellipse_distance_extremum_from_external_point(self) -> None:
        result = self.execute(
            "The point $P=(-1,0)$ lies on the ellipse $4x^2+y^2=4$. Let $Q$ be another point "
            "on this ellipse, and let $d$ be the maximum length of $PQ$. Find $d^2$."
        )
        self.assertEqual(result["answer_exact"], "16/3")

    def test_parabola_directrix_uses_focal_parameter(self) -> None:
        result = self.execute("Find the equation of the directrix of the parabola $y=x^2$.")
        self.assertEqual(result["answer_exact"], "y = -1/4")

    def test_line_hyperplane_intersection_in_three_dimensions(self) -> None:
        result = self.execute(
            r"Find the point of intersection of the line "
            r"$\frac{x-2}{3}=\frac{y+1}{4}=\frac{z-2}{12}$ and the plane $x-y+z=5$."
        )
        self.assertEqual(result["answer_exact"], "(2, -1, 2)")
        self.assertEqual(result["matrix_witness"]["ambient_dimension"], 3)

    def test_hyperplane_reflection_in_three_dimensions(self) -> None:
        result = self.execute("Find the reflection of the point $(11,16,22)$ across the plane $3x+4y+5z=7$.")
        self.assertEqual(result["answer_exact"], "(-13, -16, -18)")
        self.assertEqual(result["matrix_witness"]["ambient_dimension"], 3)

    def test_isotropic_quadric_radius_is_dimension_generic(self) -> None:
        result = self.execute("Find the radius of the sphere $w^2+x^2+y^2+z^2-2w+4x-6y+8z=5$.")
        self.assertEqual(result["answer_exact"], "sqrt(35)")
        self.assertEqual(result["matrix_witness"]["ambient_dimension"], 4)


if __name__ == "__main__":
    unittest.main()
