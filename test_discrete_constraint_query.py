from __future__ import annotations

import unittest

try:
    from math_os_prototype.category_semantics import compile_typed_semantic_graph
    from math_os_prototype.discrete_constraint_query import (
        compile_discrete_constraint_query,
        execute_discrete_constraint_query,
    )
except ImportError:
    from category_semantics import compile_typed_semantic_graph
    from discrete_constraint_query import compile_discrete_constraint_query, execute_discrete_constraint_query


class DiscreteConstraintQueryTests(unittest.TestCase):
    def execute(self, problem: str) -> dict:
        query = compile_discrete_constraint_query(problem)
        self.assertIsNotNone(query)
        assert query is not None
        result = execute_discrete_constraint_query(query.to_dict())
        self.assertTrue(result["verified"])
        self.assertEqual(result["lowering_certificate"]["kind"], "typed_discrete_constraint")
        return result

    def test_crt_extremum(self) -> None:
        result = self.execute(
            "What is the largest integer less than $2010$ that has a remainder of $5$ when divided by $7$, "
            "a remainder of $10$ when divided by $11$, and a remainder of $10$ when divided by $13$?"
        )
        self.assertEqual(result["answer_exact"], "1440")

    def test_modular_observation_accepts_expression(self) -> None:
        self.assertEqual(self.execute(r"Find the modulo 4 residue of $17\cdot18$.")["answer_exact"], "2")
        self.assertEqual(self.execute("Find the remainder of $2^8$ when it is divided by 5.")["answer_exact"], "1")

    def test_finite_integer_filter_is_shared_by_counting_and_number_theory(self) -> None:
        multiples = self.execute("How many numbers between 1 and 2005 are integer multiples of 3 or 4 but not 12?")
        primes = self.execute("How many prime numbers less than 100 have a units digit of 3?")
        self.assertEqual(multiples["query_operator"], "finite_set_filter_count")
        self.assertEqual(primes["query_operator"], "finite_set_filter_count")
        self.assertEqual(multiples["answer_exact"], "835")
        self.assertEqual(primes["answer_exact"], "7")

    def test_injective_roles_and_word_complement(self) -> None:
        roles = self.execute(
            "Our club has 20 members. In how many ways can we choose a president and a vice-president "
            "if the same person can't hold both offices?"
        )
        words = self.execute(
            "We use an alphabet (26 letters). Each word is 3 letters and must contain the letter A at least once. "
            "How many words are possible?"
        )
        self.assertEqual(roles["answer_exact"], "380")
        self.assertEqual(words["answer_exact"], "1951")

    def test_multiset_and_nonadjacent_permutations(self) -> None:
        assortment = self.execute(
            "Select six cookies from a tray containing only chocolate chip, oatmeal, and peanut butter cookies. "
            "How many different assortments can be selected? Cookies of the same type are not distinguishable."
        )
        books = self.execute(
            "I have 6 different books, 2 of which are math books. In how many ways can I stack my 6 books "
            "if I do not want the math books to be next to each other?"
        )
        self.assertEqual(assortment["answer_exact"], "28")
        self.assertEqual(books["answer_exact"], "480")

    def test_probability_is_favorable_over_enumerated_sample_space(self) -> None:
        result = self.execute(
            "The digits 2, 3, 4, 7 and 8 will be put in random order. What is the probability that the resulting "
            "integer will be divisible by 11?"
        )
        self.assertEqual(result["answer_exact"], "1/10")
        self.assertEqual(result["finite_witness"], {"outcomes": 120, "favorable": 12})

    def test_numeric_changes_preserve_operator_but_change_answer(self) -> None:
        first = compile_discrete_constraint_query("How many prime numbers less than 100 have a units digit of 3?")
        second = compile_discrete_constraint_query("How many prime numbers less than 200 have a units digit of 7?")
        self.assertIsNotNone(first)
        self.assertIsNotNone(second)
        assert first is not None and second is not None
        self.assertEqual(first.operator, second.operator)
        self.assertNotEqual(
            execute_discrete_constraint_query(first.to_dict())["answer_exact"],
            execute_discrete_constraint_query(second.to_dict())["answer_exact"],
        )

    def test_discrete_query_is_lifted_into_shared_semantic_graph(self) -> None:
        query = compile_discrete_constraint_query("How many prime numbers less than 100 have a units digit of 3?")
        self.assertIsNotNone(query)
        assert query is not None
        graph = compile_typed_semantic_graph("", discrete_query_ir=query.to_dict())
        self.assertTrue(any(item.source == "discrete_constraint_query_ir" for item in graph.morphisms))
        self.assertEqual(graph.queries[0].kind, "finite_set_filter_count")

    def test_binomial_expression_uses_tex_structure(self) -> None:
        self.assertEqual(self.execute(r"Compute $\binom{13}{4}+\binom{13}{9}$.")["answer_exact"], "1430")
        self.assertEqual(self.execute(r"Compute $\binom{10}{2}\binom{8}{3}$.")["answer_exact"], "2520")

    def test_multiset_word_permutations(self) -> None:
        self.assertEqual(
            self.execute("Determine the number of ways to arrange the letters of the word ELLIPSE.")["answer_exact"],
            "1260",
        )
        self.assertEqual(
            self.execute("Determine the number of ways to arrange the letters of the word NINE.")["answer_exact"],
            "12",
        )

    def test_subset_selection_and_group_quotas(self) -> None:
        plain = self.execute("Our math team has 8 members. In how many ways can we select 4 of them?")
        grouped = self.execute(
            "There are 30 men and 40 women in the club. They form a 7-person committee with 3 men and 4 women. "
            "In how many ways can they form the committee?"
        )
        self.assertEqual(plain["answer_exact"], "70")
        self.assertEqual(grouped["answer_exact"], "371043400")

    def test_block_contraction_works_for_linear_and_cyclic_orders(self) -> None:
        cyclic = self.execute(
            "In how many ways can 8 people sit around a round table if 3 of the people all want to sit together?"
        )
        linear = self.execute(
            "The family has 4 sons and 3 daughters. In how many ways can they sit in a row of 7 chairs "
            "such that all 3 girls sit next to each other?"
        )
        self.assertEqual(cyclic["answer_exact"], "720")
        self.assertEqual(linear["answer_exact"], "720")


if __name__ == "__main__":
    unittest.main()
