import unittest

try:
    from math_os_prototype.affine_relation_synthesis import solve_affine_relation_problem
except ImportError:
    from affine_relation_synthesis import solve_affine_relation_problem


class AffineRelationSynthesisTests(unittest.TestCase):
    def assert_answer(self, problem: str, expected: str, kind: str | None = None) -> None:
        result = solve_affine_relation_problem(problem)
        self.assertIsNotNone(result)
        self.assertEqual(expected, result.answer_exact)
        if kind:
            self.assertEqual(kind, result.relation_kind)

    def test_unknown_initial_state(self) -> None:
        self.assert_answer(
            "Some children were riding on a bus. Then 2 children got on. After that there were 41 children. How many were riding before?",
            "39",
            "unknown_state",
        )

    def test_unknown_state_with_gain_and_loss(self) -> None:
        self.assert_answer(
            "Lena had some dollars. She lost 4 dollars and received 9 dollars. After that she had 66 dollars. How many dollars did she have at first?",
            "61",
            "unknown_state",
        )

    def test_unknown_state_with_omitted_loss_object(self) -> None:
        self.assert_answer(
            "Roger had some lychee. Gordon took 38 from him. Now Roger has 84 lychee. How many lychee Roger had primitively?",
            "122",
            "unknown_state_clause_elaboration",
        )

    def test_unknown_state_with_omitted_gain_object(self) -> None:
        self.assert_answer(
            "Wanda had some papaya. Linda gave him 8 more. Now Wanda has 44 papaya. How many papaya did Wanda have in the first?",
            "36",
            "unknown_state_clause_elaboration",
        )

    def test_unknown_state_production_then_sale(self) -> None:
        self.assert_answer(
            "Baker made some cakes. He sold 145 of them. If he still has 72 cakes left. How many cakes did Baker make?",
            "217",
            "unknown_state_clause_elaboration",
        )

    def test_partition_and_difference_system(self) -> None:
        self.assert_answer(
            "A team played 22 games. They won 8 more than they lost. How many did they win?",
            "15",
            "partition_comparison",
        )

    def test_category_neutral_total_difference_partition(self) -> None:
        self.assert_answer(
            "Gretchen has 110 coins. There are 30 more gold coins than silver coins. How many gold coins does Gretchen have?",
            "70",
            "total_difference_partition",
        )

    def test_ratio_total_projects_requested_part(self) -> None:
        self.assert_answer(
            "The ratio of dogs to cats at the pound is 4:3. How many dogs were at the pound if a total of 280 dogs and cats were at the pound?",
            "160",
            "ratio_part",
        )

    def test_ratio_known_part_projects_other_part(self) -> None:
        self.assert_answer(
            "The ratio of red sweets to green sweets is 3:4. If the bag contains 120 green sweets, how many red sweets are there?",
            "90",
            "ratio_part",
        )

    def test_ratio_surface_and_number_perturbation(self) -> None:
        self.assert_answer(
            "The ratio of red tokens to blue tokens is 5:2. A box contains 98 tokens in total. How many red tokens are there?",
            "70",
            "ratio_part",
        )

    def test_scalar_ratio_reduction(self) -> None:
        self.assert_answer(
            "The length of a ribbon was originally 30 cm. It was reduced in the ratio 5:3. What is its length now?",
            "18",
            "ratio_scale",
        )

    def test_ratio_share_then_owner_event(self) -> None:
        self.assert_answer(
            "Gerald and Julia divided $100 in the ratio 3:2. If Gerald spent $10 on a book, how much money did he have left?",
            "50",
            "ratio_part_after_event",
        )

    def test_inverse_discount(self) -> None:
        self.assert_answer(
            "A book costs $19.50 after a 25% discount from the original price. What was the original price?",
            "26",
            "percentage_inverse_discount",
        )

    def test_surface_and_number_perturbation(self) -> None:
        self.assert_answer(
            "A club played 30 matches. They won 6 more than they lost. How many did they lose?",
            "12",
            "partition_comparison",
        )

    def test_collective_pronoun_observes_all_named_members(self) -> None:
        self.assert_answer(
            "Aya has 10 books. Ben has 3 more books than Aya. How many books do they own?",
            "23",
            "comparison_chain_total",
        )

    def test_percentage_does_not_drop_a_second_relation(self) -> None:
        self.assertIsNone(solve_affine_relation_problem(
            "There are 15 red cards and 60% more green cards. Yellow cards equal the sum of red and green cards. How many cards are there?"
        ))

    def test_comparison_chain_uses_one_affine_backend(self) -> None:
        self.assert_answer(
            "A magazine costs half as much as a book. The book costs $4. A pen costs $1 less than the magazine. How much is the pen?",
            "1",
            "comparison_chain",
        )

    def test_comparison_chain_total(self) -> None:
        self.assert_answer(
            "There were 175 diamonds and 35 fewer rubies than diamonds. There were twice as many emeralds as rubies. How many gems were there in all?",
            "595",
            "comparison_chain_total",
        )

    def test_comparison_chain_does_not_drop_rate_constraints(self) -> None:
        self.assertIsNone(solve_affine_relation_problem(
            "Claire earns 1 badge every month. Wendy earns three times as many as Claire. How many more badges after 20 months?"
        ))

    def test_collective_query_sums_all_typed_members(self) -> None:
        self.assert_answer(
            "There are 9 red sticks and 5 more blue sticks than red. The number of yellow sticks is 3 less than the blue sticks. How many sticks do they have?",
            "34",
            "comparison_chain_total",
        )

    def test_weighted_observation_is_part_of_affine_system(self) -> None:
        self.assert_answer(
            "A gallon jar costs $2 more than a half-gallon jar. A gallon jar costs $5. Find the total spent on 10-gallon jars and 16 half-gallon jars.",
            "98",
            "weighted_comparison_total",
        )

    def test_weighted_observation_surface_perturbation(self) -> None:
        self.assert_answer(
            "A large ticket costs $3 more than a small ticket. A large ticket costs $8. What is paid for 7 large tickets and 4 small tickets?",
            "76",
            "weighted_comparison_total",
        )

    def test_relative_clause_resolves_to_antecedent(self) -> None:
        self.assert_answer(
            "Rani has 10 more shells than Monic, who has 4 fewer shells than Bo. Bo has 40 shells. How many shells do the three have in total?",
            "122",
            "comparison_chain_total",
        )

    def test_percentage_rejects_query_type_change(self) -> None:
        self.assertIsNone(solve_affine_relation_problem(
            "There are 45% more pears than bananas. There are 200 bananas. How many fruits are there?"
        ))

    def test_unresolved_pronoun_is_not_a_variable(self) -> None:
        self.assertIsNone(solve_affine_relation_problem(
            "A child has 5 cards. His brother has 3 fewer cards than he has. How many cards do they have together?"
        ))

    def test_known_value_does_not_cross_sentence_boundary(self) -> None:
        self.assert_answer(
            "Adam has 3 more apples than Jackie. Adam has 9 apples. How many apples does Jackie have?",
            "6",
            "comparison_chain",
        )

    def test_comparative_query_builds_observation_morphism(self) -> None:
        self.assert_answer(
            "James has 6 more candies than Robert. John has twice as many candies as Robert. John has 54 candies. How many more candies does John have than James?",
            "21",
            "comparison_chain_difference",
        )

    def test_multiplier_plus_offset_is_one_affine_equation(self) -> None:
        self.assert_answer(
            "Janey has 3 more than twice the number of books that Sally has. Janey has 21 books. How many books does Sally have?",
            "9",
            "multiplier_offset",
        )

    def test_product_sort_keeps_two_attributes_separate(self) -> None:
        self.assert_answer(
            "Jake has 13 fewer peaches and 3 more apples than Steven. Steven has 9 peaches and 8 apples. How many apples does Jake have?",
            "11",
            "multisort_comparison",
        )

    def test_fractional_state_actions_share_one_affine_backend(self) -> None:
        self.assert_answer(
            "A seller had some cards. She sold a third of them, sold 2 more, and sold half of what was left. She has 5 cards left. How many did she start with?",
            "18",
            "affine_state_transition_inverse",
        )

    def test_partition_actions_can_observe_percentage(self) -> None:
        self.assert_answer(
            "A class of 40 students has 20% enrolled in art. Then 25% of the remaining students enrolled in music, and the rest chose science. What percentage chose science?",
            "60",
            "affine_state_transition_percentage",
        )

    def test_numeric_perturbation_preserves_state_operator(self) -> None:
        first = solve_affine_relation_problem(
            "A 1000-piece puzzle had a quarter placed, then a third of the remaining pieces were placed. How many pieces are left?"
        )
        changed = solve_affine_relation_problem(
            "A 1200-piece puzzle had a quarter placed, then a third of the remaining pieces were placed. How many pieces are left?"
        )
        self.assertIsNotNone(first)
        self.assertIsNotNone(changed)
        self.assertEqual(first.relation_kind, changed.relation_kind)
        self.assertEqual("500", first.answer_exact)
        self.assertEqual("600", changed.answer_exact)

    def test_percentage_offset_and_scale_share_one_fact_graph(self) -> None:
        self.assert_answer(
            "Shondra has 7 fewer plants than Toni. Toni has 60% more plants than "
            "Frederick. Frederick has 10 plants. How many plants does Shondra have?",
            "9",
            "mixed_affine_fact_graph",
        )

    def test_percentage_and_multiplier_chain(self) -> None:
        self.assert_answer(
            "Mitchel went down the slide 30 times. Anne went down the slide 30% less "
            "than Mitchel and Robert went down 4 times as much as Anne. "
            "How many times did Robert go down the slide?",
            "84",
            "mixed_affine_fact_graph",
        )

    def test_mixed_fact_graph_number_perturbation(self) -> None:
        changed = solve_affine_relation_problem(
            "Shondra has 9 fewer plants than Toni. Toni has 50% more plants than "
            "Frederick. Frederick has 20 plants. How many plants does Shondra have?"
        )
        self.assertIsNotNone(changed)
        self.assertEqual("21", changed.answer_exact)

    def test_state_transition_does_not_drop_a_sibling_initial_category(self) -> None:
        self.assertIsNone(solve_affine_relation_problem(
            "A pet store had 13 siamese cats and 5 house cats. During a sale they "
            "sold 10 cats. How many cats do they have left?"
        ))


if __name__ == "__main__":
    unittest.main()
