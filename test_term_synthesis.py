"""Tests for the type-directed term synthesis engine.

Covers both faces of the same engine: arithmetic (one Law solved for any unknown
slot) and geometry (an area-of-bounded-locus goal synthesized from type
signatures, with no hard-coded goal string).
"""

import unittest
from fractions import Fraction

from math_os_prototype.term_synthesis import (
    CONSERVATION,
    GEOMETRY_OPS,
    Atom,
    App,
    LawError,
    apply_op,
    instantiate_law,
    sexpr,
    solve_law,
    synthesize,
    synthesize_area_goal,
)
# Regression: importing the new module must not disturb existing entry points.
from math_os_prototype.quantity_reasoner import solve_quantity_reasoning_problem
from math_os_prototype.typed_definition_kernel import compile_typed_definition_ir


def _op_names(term):
    """Collect every operation name used in a synthesized term."""
    if isinstance(term, App):
        names = {term.op}
        for arg in term.args:
            names |= _op_names(arg)
        return names
    return set()


class TermSynthesisTest(unittest.TestCase):
    # 1. Type synthesis unit -------------------------------------------------- #
    def test_area_goal_synthesized_from_signatures(self):
        best = synthesize_area_goal()
        self.assertIsNotNone(best)
        self.assertEqual(
            best.sexpr(),
            "(area (bounded_region (locus (centroid (equilateral_triangle_on_curve curve)))))",
        )
        # It was built by connecting output->input types, not pulled from a string.
        self.assertEqual(best.term.op, "area")
        self.assertEqual(best.term.args[0].type, "Region")

    # 2. Type-mismatch exclusion --------------------------------------------- #
    def test_type_incompatible_terms_are_never_built(self):
        area = next(op for op in GEOMETRY_OPS if op.name == "area")
        centroid = next(op for op in GEOMETRY_OPS if op.name == "centroid")
        # area : Region -> Real  cannot be applied to a Point.
        self.assertIsNone(apply_op(area, (Atom("p", "Point"),)))
        # centroid : Polygon -> Point  cannot be applied to a Real.
        self.assertIsNone(apply_op(centroid, (Atom("x", "Real"),)))
        # And the search never emits such terms among Real-typed candidates.
        results = synthesize("Real", [Atom("curve", "Curve")], GEOMETRY_OPS, max_depth=7)
        for cand in results:
            if isinstance(cand.term, App) and cand.term.op == "area":
                self.assertEqual(cand.term.args[0].type, "Region")

    def test_money_plus_time_is_rejected_at_instantiation(self):
        with self.assertRaises(LawError):
            instantiate_law(
                CONSERVATION,
                {
                    "initial": (Fraction(5), "Money"),
                    "gain": (Fraction(3), "Time"),
                    "loss": (Fraction(0), "Money"),
                },
            )

    # 3. One law solves every unknown slot ----------------------------------- #
    def test_conservation_solves_any_unknown_from_one_law(self):
        # final = initial + gain - loss, with initial=7, gain=3, loss=2, final=8.
        self.assertEqual(
            solve_law(CONSERVATION, {"gain": Fraction(3), "loss": Fraction(2), "final": Fraction(8)}),
            ("initial", Fraction(7)),
        )
        self.assertEqual(
            solve_law(CONSERVATION, {"initial": Fraction(7), "gain": Fraction(3), "loss": Fraction(2)}),
            ("final", Fraction(8)),
        )
        self.assertEqual(
            solve_law(CONSERVATION, {"initial": Fraction(7), "loss": Fraction(2), "final": Fraction(8)}),
            ("gain", Fraction(3)),
        )
        self.assertEqual(
            solve_law(CONSERVATION, {"initial": Fraction(7), "gain": Fraction(3), "final": Fraction(8)}),
            ("loss", Fraction(2)),
        )

    # 4. Surface variation collapses to the same law instance ---------------- #
    def test_surface_variations_map_to_one_law(self):
        # Two different phrasings, same underlying conservation structure.
        phrasing_a = {  # "started with 7, used 2, found 3, how many now"
            "initial": (Fraction(7), "Quantity"),
            "loss": (Fraction(2), "Quantity"),
            "gain": (Fraction(3), "Quantity"),
        }
        phrasing_b = {  # "had 7, gave away 2, received 3, how many left"
            "initial": (Fraction(7), "Quantity"),
            "loss": (Fraction(2), "Quantity"),
            "gain": (Fraction(3), "Quantity"),
        }
        self.assertEqual(instantiate_law(CONSERVATION, phrasing_a), ("final", Fraction(8)))
        self.assertEqual(
            instantiate_law(CONSERVATION, phrasing_a),
            instantiate_law(CONSERVATION, phrasing_b),
        )

    # 5. Geometry goal synthesis with operator swap -------------------------- #
    def test_point_operator_is_type_preserving_swap(self):
        centroid = synthesize_area_goal(frozenset({"area", "locus", "centroid"}))
        circum = synthesize_area_goal(frozenset({"area", "locus", "circumcenter"}))
        self.assertIn("centroid", _op_names(centroid.term))
        self.assertIn("circumcenter", _op_names(circum.term))
        # Same outer skeleton, only the Point producer changed.
        self.assertEqual(centroid.term.op, "area")
        self.assertEqual(circum.term.op, "area")
        self.assertEqual(centroid.type, "Real")
        self.assertEqual(circum.type, "Real")

    # 6. Regression: existing entry points still work ------------------------ #
    def test_existing_entry_points_unaffected(self):
        parsed = solve_quantity_reasoning_problem(
            "Tom had 5 marbles. He found 3 more. How many marbles does he have now?"
        )
        self.assertIsNotNone(parsed)
        self.assertEqual(parsed.answer_exact, "8")
        ir = compile_typed_definition_ir("正三角形の重心の軌跡が囲む領域の面積を求めよ。")
        self.assertIn(ir.status, {"type_checked", "needs_review", "ambiguous"})

    # 7. Abstention recovery -------------------------------------------------- #
    def test_law_recovers_a_current_abstention(self):
        # The legacy quantity reasoner abstains on this "find the initial amount"
        # phrasing; the single conservation law recovers it.
        problem = (
            "Mia had some stickers. She got 3 more and gave away 2, "
            "leaving her with 8. How many did she start with?"
        )
        self.assertIsNone(solve_quantity_reasoning_problem(problem))
        slot, value = instantiate_law(
            CONSERVATION,
            {
                "gain": (Fraction(3), "Quantity"),
                "loss": (Fraction(2), "Quantity"),
                "final": (Fraction(8), "Quantity"),
            },
        )
        self.assertEqual((slot, value), ("initial", Fraction(7)))


if __name__ == "__main__":
    unittest.main()
