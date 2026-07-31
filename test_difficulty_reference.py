from __future__ import annotations

import unittest

try:
    from math_os_prototype.difficulty_reference import (
        DIFFICULTY_GATING_ENABLED,
        canonical_reference_statement,
        extract_problem_statement,
        load_fixed_reference,
    )
except ImportError:  # pragma: no cover
    from difficulty_reference import (
        DIFFICULTY_GATING_ENABLED,
        canonical_reference_statement,
        extract_problem_statement,
        load_fixed_reference,
    )


class DifficultyReferenceTest(unittest.TestCase):
    def test_extracts_document_body_without_preamble(self) -> None:
        source = r"""
        \documentclass{jsarticle}
        \usepackage{amsmath}
        \begin{document}
        $x^2=4$ を解け。
        \end{document}
        """
        self.assertEqual(extract_problem_statement(source), "$x^2=4$ を解け。")

    def test_rejects_unclosed_document_scaffolding(self) -> None:
        with self.assertRaises(ValueError):
            extract_problem_statement(r"\documentclass{jsarticle} $x=1$")

    def test_digest_canonicalization_ignores_preamble_and_spacing(self) -> None:
        plain = "$x^2=4$ を解け。"
        document = (
            r"\documentclass{jsarticle}"
            "\n"
            r"\begin{document}  $x^2=4$   を解け。 \end{document}"
        )
        self.assertEqual(
            canonical_reference_statement(plain),
            canonical_reference_statement(document),
        )

    def test_fixed_reference_is_self_checked_and_not_a_gate(self) -> None:
        rows, metadata = load_fixed_reference()
        self.assertEqual(metadata["count"], len(rows))
        self.assertEqual(len(metadata["sha256"]), 64)
        self.assertFalse(DIFFICULTY_GATING_ENABLED)


if __name__ == "__main__":
    unittest.main()
