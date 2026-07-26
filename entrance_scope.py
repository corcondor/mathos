"""Japanese entrance-mathematics lowering certificates.

The research atlas may use arbitrary mathematical objects internally.  A
problem enters the examination-facing pool only when its statement and a full
solution can be lowered to the finite vocabulary of Japanese upper-secondary
mathematics.  This is an admission contract, not a difficulty classifier.
"""

from __future__ import annotations

from typing import Any


CURRICULUM = "jp_upper_secondary_math_IA_IIB_IIIC"

# Each retained family has an explicit lowering route.  The route records the
# school-level primitives needed to reconstruct the solution; merely attaching
# a high-school label is not sufficient.
FAMILY_LOWERINGS: dict[str, tuple[str, ...]] = {
    # --- 追加登録: 高校範囲の道具に分解できる族 ---
    "construct.mobius_fixed_points": (
        "rational_function",
        "quadratic_equation",
        "fixed_point_equation",
    ),
    "construct.mobius_iteration_period": (
        "rational_function",
        "function_composition",
        "periodicity",
    ),
    "ultradeep.geometry_regular_polygon_minkowski_perimeter": (
        "regular_polygon",
        "vector_addition",
        "perimeter_computation",
    ),
    "algebraic_geometry.even_quartic_parabola_hull_area": (
        "polynomial_roots",
        "vieta_relations",
        "coordinate_area",
        "one_variable_extremum",
    ),
    "algebraic_geometry.cubic_discriminant_triangle_area": (
        "polynomial_roots",
        "vieta_relations",
        "coordinate_area",
        "one_variable_extremum",
    ),
    "complex_geometry.reciprocal_root_polygon_area": (
        "complex_plane",
        "roots_of_unity",
        "polygon_area",
        "trigonometry",
    ),
    "polynomial.interpolation_harmonic_observable": (
        "polynomial_factorization",
        "finite_difference",
        "differentiation",
    ),
    "conic_duality.tangent_intercept_centroid_minimum": (
        "differentiation",
        "tangent_line",
        "centroid",
        "quadratic_minimum",
    ),
    "asymptotic.recurrence_square_increment": (
        "recurrence",
        "inequality",
        "sequence_limit",
    ),
    "analysis.boundary_layer_integral_limit": (
        "definite_integral",
        "substitution",
        "inequality",
        "sequence_limit",
    ),
    "binomial.roots_of_unity_filter_mod3": (
        "binomial_theorem",
        "complex_plane",
        "roots_of_unity",
    ),
    "analysis.reflection_symmetric_integral": (
        "definite_integral",
        "substitution",
        "trigonometric_identity",
    ),
    "probability.left_to_right_maxima_expectation": (
        "permutation",
        "indicator_counting",
        "expectation",
    ),
    "recurrence.cassini_fibonacci_determinant_invariant": (
        "recurrence",
        "mathematical_induction",
        "algebraic_identity",
    ),
    "lattice_paths.dyck_reflection_catalan_count": (
        "lattice_path",
        "combination",
        "reflection_bijection",
    ),
    "passage_region.line_family_sweep": (
        "quadratic_range",
        "parameter_elimination",
        "definite_integral",
        "area",
    ),
    "passage_region.parabola_family_sweep": (
        "quadratic_range",
        "parameter_elimination",
        "definite_integral",
        "area",
    ),
    "fusion.trig_absolute_value_integral": (
        "trigonometric_equation",
        "sign_partition",
        "definite_integral",
    ),
    "fusion.trig_floor_integral": (
        "trigonometric_inequality",
        "piecewise_function",
        "definite_integral",
    ),
    "construct.cubic_tangent_midpoint_locus": (
        "differentiation",
        "tangent_line",
        "vieta_relations",
        "parameter_elimination",
        "locus",
    ),
    "construct.parabola_right_angle_chord": (
        "coordinate_geometry",
        "inner_product",
        "quadratic_equation",
    ),
    "construct.complex_affine_limit": (
        "complex_number",
        "geometric_sequence",
        "sequence_limit",
    ),
    "construct.complex_rotation_period": (
        "complex_plane",
        "de_moivre",
        "integer_period",
    ),
    "construct.reciprocal_recurrence": (
        "recurrence",
        "algebraic_transform",
        "sequence_limit",
    ),
    "construct.linear_recurrence_mod_period": (
        "recurrence",
        "congruence",
        "finite_state_iteration",
    ),
    "layered.recurrence_period_observable": (
        "recurrence",
        "congruence",
        "finite_counting",
        "integer_factorization",
    ),
    "layered.cubic_tangent_iteration": (
        "differentiation",
        "tangent_line",
        "recurrence",
        "mathematical_induction",
    ),
    "layered.rotation_orbit_hull_area": (
        "complex_plane",
        "de_moivre",
        "regular_polygon",
        "area",
    ),
    "deep.tangent_iteration_growth": (
        "differentiation",
        "tangent_line",
        "recurrence",
        "logarithm",
        "sequence_limit",
    ),
    "deep.polygon_subset_centroid": (
        "complex_plane",
        "roots_of_unity",
        "centroid",
        "combination",
    ),
    "deep.rotation_diagonal_product_divisors": (
        "complex_plane",
        "roots_of_unity",
        "distance",
        "polynomial_factorization",
        "integer_factorization",
    ),
    "ultradeep.cyclotomic_distance_norm_divisor_count": (
        "complex_plane",
        "roots_of_unity",
        "polynomial_factorization",
        "integer_factorization",
    ),
    "ultradeep.cubic_root_triangle_discriminant_divisor_count": (
        "polynomial_roots",
        "vieta_relations",
        "coordinate_area",
        "integer_factorization",
    ),
    "ultradeep.geometry_astroid_envelope_area": (
        "trigonometric_parameter",
        "tangent_line",
        "parameter_elimination",
        "definite_integral",
        "area",
    ),
    "ultradeep.geometry_ellipse_tangent_pair_locus": (
        "ellipse",
        "differentiation",
        "tangent_line",
        "simultaneous_equations",
        "parameter_elimination",
        "locus",
    ),
    "ultradeep.geometry_orthocenter_locus_area": (
        "ellipse",
        "inner_product",
        "orthocenter",
        "parameter_elimination",
        "area",
    ),
    "ultradeep.geometry_parabola_normal_envelope": (
        "parabola",
        "differentiation",
        "normal_line",
        "parameter_elimination",
        "locus",
    ),
}

FORBIDDEN_SURFACE_TERMS = (
    "Paley",
    "ラプラシアン",
    "隣接行列",
    "全域木",
    "Minkowski",
    "ミンコフスキー",
    "ルジャンドル記号",
    r"\mathbb F_",
)


def certify_entrance_scope(
    problem: dict[str, Any],
) -> dict[str, Any] | None:
    family_id = str(problem.get("family_id") or "")
    lowering = FAMILY_LOWERINGS.get(family_id)
    if lowering is None:
        return None
    surface = " ".join(
        (
            str(problem.get("statement_tex") or ""),
            str(problem.get("solution_tex") or ""),
        )
    )
    if any(term in surface for term in FORBIDDEN_SURFACE_TERMS):
        return None
    lift = problem.get("lift_certificate") or {}
    morphisms = list(lift.get("morphism_chain") or [])
    if not morphisms or not lift.get("type_checked"):
        return None
    return {
        "scope": CURRICULUM,
        "type_checked": True,
        "abstract_morphism_chain": morphisms,
        "lowering_chain": list(lowering),
        "uses_only_school_level_primitives": True,
    }

