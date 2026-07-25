from __future__ import annotations

import unittest

from math_os_prototype.semantic_repair_loop import (
    LEXICAL_AUTOMATON,
    build_frozen_split,
    compile_repair_forest,
    infer_cardinality_skeleton,
    mutate_alpha_names,
    select_candidate,
)


class SemanticRepairLoopTests(unittest.TestCase):
    def test_finite_lexicon_recognizes_generic_composition(self) -> None:
        text = (
            r"方程式 \(x^4-5x^2+t=0\) の相異なる4実根を各点に対応させ，"
            r"その凸包の面積の最大値を求めよ。"
        )
        names = {item.canonical for item in LEXICAL_AUTOMATON.scan(text)}
        self.assertTrue(
            {"Equation", "RootSet", "Distinct", "Map", "ConvexHull", "Area", "Maximum"}
            <= names
        )

    def test_parse_forest_builds_typed_operator_chain(self) -> None:
        text = (
            r"方程式 \(x^4-5x^2+t=0\) の相異なる4実根を点に対応させる。"
            r"これらの点の凸包の面積の最大値を求めよ。"
        )
        selected = select_candidate(compile_repair_forest(text))
        self.assertTrue(selected.type_checked)
        self.assertEqual(
            selected.morphism_chain,
            ["Equation", "RootSet", "Map", "ConvexHull", "Area", "Maximum"],
        )

    def test_cardinality_is_structural_not_numeric_identity(self) -> None:
        self.assertEqual(
            infer_cardinality_skeleton("相異なる4実根をもつ"),
            ["cardinality:Cardinality(Set(実根))=#"],
        )

    def test_alpha_renaming_does_not_preserve_literal_names(self) -> None:
        self.assertNotEqual(mutate_alpha_names("x+y=t"), "x+y=t")

    def test_alpha_renaming_preserves_semantic_signature(self) -> None:
        text = r"実数 \(x,y\) が \(x+y=3\) を満たすとき，\(x^2+y^2\) の最小値を求めよ。"
        renamed = mutate_alpha_names(text)
        original = select_candidate(compile_repair_forest(text))
        changed = select_candidate(compile_repair_forest(renamed))
        self.assertEqual(original.canonical_signature(), changed.canonical_signature())

    def test_maximum_and_minimum_are_not_composed(self) -> None:
        text = r"関数 \(f(x)\) の最大値と最小値を求めよ。"
        selected = select_candidate(compile_repair_forest(text))
        self.assertNotEqual(selected.morphism_chain, ["Maximum", "Minimum"])

    def test_split_keeps_same_author_together(self) -> None:
        rows = [
            {"id": 1, "author_id": "a", "problem_tex": "整数 x の値を求めよ。"},
            {"id": 2, "author_id": "a", "problem_tex": "整数 y の値を求めよ。"},
            {"id": 3, "author_id": "b", "problem_tex": "円の面積を求めよ。"},
            {"id": 4, "author_id": "c", "problem_tex": "数列の極限を求めよ。"},
        ]
        split = build_frozen_split(rows)
        self.assertEqual(split["assignments"]["1"], split["assignments"]["2"])


if __name__ == "__main__":
    unittest.main()
