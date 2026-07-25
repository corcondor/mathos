import tempfile
import unittest
from pathlib import Path

from math_os_prototype.creative_tex_corpus import (
    build_tex_corpus,
    extract_itembox_problems,
    select_stratified,
)


SAMPLE_TEX = r"""
\documentclass{jsarticle}
\begin{document}
\begin{itembox}[l]{問題1}
素数 $p$ に対して $p+2$ も素数となるものを求めよ。
\end{itembox}
\begin{itembox}[l]{問題1}
三角形の面積の最大値を求めよ。
\end{itembox}
\begin{itembox}[l]{問題2}
数列 $a_{n+1}=a_n+1$ の一般項を求めよ。
\end{itembox}
\fbox{解答編}
\begin{itembox}[l]{類題}
これは取り込まない。
\end{itembox}
\section*{問題1解答}
解答本文
\end{document}
"""


class CreativeTexCorpusTests(unittest.TestCase):
    def test_extracts_only_problem_itemboxes_before_answer_section(self) -> None:
        blocks = extract_itembox_problems(SAMPLE_TEX)

        self.assertEqual(len(blocks), 3)
        self.assertEqual([block.label for block in blocks], ["問題1", "問題1", "問題2"])
        self.assertEqual(len({block.statement_hash for block in blocks}), 3)
        self.assertNotIn("解答本文", " ".join(block.statement_tex for block in blocks))

    def test_builds_stable_unique_ids_despite_duplicate_problem_labels(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "problems.tex"
            path.write_text(SAMPLE_TEX, encoding="utf-8")

            first, report = build_tex_corpus(
                path,
                source_id="sample",
                rights_basis="self_authored",
                author_system="human",
                limit=3,
                seed=7,
            )
            second, _ = build_tex_corpus(
                path,
                source_id="sample",
                rights_basis="self_authored",
                author_system="human",
                limit=3,
                seed=7,
            )

        self.assertEqual([row.record_id for row in first], [row.record_id for row in second])
        self.assertEqual(len({row.record_id for row in first}), 3)
        self.assertEqual(report["duplicate_display_labels"], {"問題1": 2})
        self.assertFalse(report["answer_section_imported"])

    def test_stratified_selection_is_deterministic_and_respects_limit(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "problems.tex"
            path.write_text(SAMPLE_TEX, encoding="utf-8")
            records, _ = build_tex_corpus(
                path,
                source_id="sample",
                rights_basis="self_authored",
                author_system="human",
                limit=None,
                seed=7,
            )

        first = select_stratified(records, limit=2, seed=99)
        second = select_stratified(records, limit=2, seed=99)

        self.assertEqual(len(first), 2)
        self.assertEqual([row.record_id for row in first], [row.record_id for row in second])

    def test_fixed_record_ids_freeze_the_evaluation_set(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "problems.tex"
            path.write_text(SAMPLE_TEX, encoding="utf-8")
            all_records, _ = build_tex_corpus(
                path,
                source_id="sample",
                rights_basis="self_authored",
                author_system="human",
                limit=None,
                seed=7,
            )
            fixed_ids = [all_records[2].record_id, all_records[0].record_id]
            selected, report = build_tex_corpus(
                path,
                source_id="sample",
                rights_basis="self_authored",
                author_system="human",
                limit=1,
                seed=999,
                fixed_record_ids=fixed_ids,
            )

        self.assertEqual([row.record_id for row in selected], fixed_ids)
        self.assertEqual(report["selection_mode"], "fixed_record_ids")


if __name__ == "__main__":
    unittest.main()
