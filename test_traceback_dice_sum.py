import unittest

from traceback_engine import closure_dice_sum


class DiceSumClosureTests(unittest.TestCase):
    def test_odd_number_of_dice_does_not_publish_scalar_mode(self):
        nodes = {node.key: node for node in closure_dice_sum(3)}
        self.assertNotIn("modal_sum", nodes)
        self.assertEqual(nodes["ways_for_modal_sum"].value, 27)

    def test_even_number_of_dice_has_unique_scalar_mode(self):
        nodes = {node.key: node for node in closure_dice_sum(4)}
        self.assertEqual(nodes["modal_sum"].value, 14)


if __name__ == "__main__":
    unittest.main()
