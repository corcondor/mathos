from __future__ import annotations

import unittest

try:
    from math_os_prototype.build_entrance_pool import _delivery_topic
except ImportError:  # pragma: no cover
    from build_entrance_pool import _delivery_topic


class DeliveryCurationTest(unittest.TestCase):
    def test_repetitive_dice_construction_is_not_deployed(self) -> None:
        self.assertEqual(
            _delivery_topic({"parameters": {"construction": "dice_sum"}}),
            "dice_sum",
        )
        self.assertEqual(
            _delivery_topic({"family_id": "traceback.dice_sum.modal_sum"}),
            "dice_sum",
        )

    def test_gambler_method_is_not_deployed(self) -> None:
        problem = {"verification": {"method": "gambler_ruin_boundary_recurrence"}}
        self.assertEqual(_delivery_topic(problem), "gambler_ruin")

    def test_ellipse_tangent_calculation_is_held_for_repair(self) -> None:
        self.assertEqual(
            _delivery_topic({"parameters": {"construction": "ellipse_tangent"}}),
            "ellipse_tangent",
        )
        self.assertEqual(
            _delivery_topic({"family_id": "traceback.ellipse_tangent.chord_length"}),
            "ellipse_tangent",
        )
        self.assertEqual(
            _delivery_topic({"family_id": "ultradeep.geometry_ellipse_tangent_pair_locus"}),
            "ellipse_tangent",
        )
        self.assertEqual(
            _delivery_topic({"statement_tex": "楕円上の点を動かす。"}),
            "ellipse_tangent",
        )

    def test_general_probability_is_not_excluded(self) -> None:
        problem = {"verification": {"method": "exact_subset_enumeration"}}
        self.assertIsNone(_delivery_topic(problem))


if __name__ == "__main__":
    unittest.main()
