import unittest

from parent_conditioned_discovery import discover


class ParentConditionedDiscoveryTest(unittest.TestCase):
    def test_unknown_parents_still_produce_typed_hypotheses(self) -> None:
        result = discover([
            {
                "id": "integral-parent",
                "statement": r"数列 a_n を積分 a_n=\int_0^1(1-x^2)^n dx で定め、極限を求めよ。",
                "solution": "部分積分から漸化式を得る。",
            },
            {
                "id": "integer-parent",
                "statement": r"素数 p と整数 n に対し n^2\equiv-1\pmod p となる条件を示せ。",
                "solution": "合同式と平方剰余を用いる。",
            },
        ])
        self.assertEqual(result["engine"], "MathOS parent-conditioned structural discovery (no LLM)")
        self.assertGreaterEqual(len(result["hypotheses"]), 1)
        self.assertEqual(result["selected_plan"]["kind"], "conjectured_universal_construction")
        target = result["selected_plan"]["target_sort"]
        self.assertTrue("IntegralFunctional" in target or "Sequence" in target)
        self.assertTrue(
            "IntegerStructure" in target
            or "ResidueClassStructure" in target
            or "PrimeSpectrum" in target
        )
        self.assertNotIn("OpaqueMathematicalObject", target)
        self.assertEqual(result["cards"][0]["parent_ids"], ["integral-parent", "integer-parent"])
        derivation = result["cards"][0]["fusion_derivation"]
        self.assertTrue(derivation["passed"])
        self.assertTrue(derivation["ablationPassed"])
        self.assertEqual(len(derivation["assignments"]), 2)

    def test_structure_signature_depends_on_selected_parents(self) -> None:
        base = {
            "statement": r"曲線 y=x^2 の接線の包絡線を求めよ。",
            "solution": "媒介変数を消去する。",
        }
        first = discover([{**base, "id": "a"}, {**base, "id": "b"}])
        second = discover([{**base, "id": "a"}, {**base, "id": "c"}])
        self.assertNotEqual(
            first["structures"][0]["blueprint"]["id"],
            second["structures"][0]["blueprint"]["id"],
        )

    def test_surface_and_number_changes_preserve_the_lift(self) -> None:
        first = discover([
            {"id": "i1", "statement": r"数列 a_n=\int_0^1 x^n dx の極限を求めよ。"},
            {"id": "n1", "statement": r"素数 p に対して x^2\equiv-1\pmod p を考える。"},
        ])
        second = discover([
            {"id": "i2", "statement": r"積分 b_k=\int_0^2 t^k dt で定まる数列の極限を求めよ。"},
            {"id": "n2", "statement": r"整数 y と素数 q が y^2\equiv-1\pmod q を満たす条件を示せ。"},
        ])
        first_roots = [graph["semantic_roots"] for graph in first["parent_graphs"]]
        second_roots = [graph["semantic_roots"] for graph in second["parent_graphs"]]
        self.assertEqual(first_roots, second_roots)
        self.assertEqual(first["selected_plan"]["constructor"], second["selected_plan"]["constructor"])

    def test_scalar_coercion_is_not_accepted_as_fusion(self) -> None:
        result = discover([
            {"id": "seq", "statement": r"数列 a_n=\int_0^1 x^n dx の極限を求めよ。"},
            {"id": "mod", "statement": r"素数 p に対し x^2\equiv 2\pmod p の可解性を示せ。"},
        ])
        self.assertNotEqual(result["selected_plan"]["kind"], "known_typed_join")
        for path in result["selected_plan"]["paths"]:
            self.assertGreaterEqual(len(path["morphisms"]), 1)


if __name__ == "__main__":
    unittest.main()
