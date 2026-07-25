from __future__ import annotations

import unittest

from math_os_prototype.jukenmath_full_audit import (
    canonical_surface,
    describe_lengths,
    find_near_duplicates,
    jaccard,
    surface_ngrams,
)


class JukenmathFullAuditTests(unittest.TestCase):
    def test_canonical_surface_ignores_spacing_and_display_style(self) -> None:
        self.assertEqual(
            canonical_surface(r"\displaystyle x ^ 2 + 1"),
            canonical_surface(r"x^2+1"),
        )

    def test_jaccard_is_one_for_same_surface(self) -> None:
        grams = surface_ngrams(r"$x^2+1=0$")
        self.assertEqual(jaccard(grams, grams), 1.0)

    def test_near_duplicate_detection(self) -> None:
        samples = {
            1: surface_ngrams("正の整数 n について n^2+n を求めよ"),
            2: surface_ngrams("正の整数nについてn^2+nを求めよ"),
            3: surface_ngrams("円に内接する三角形の面積を求めよ"),
        }
        pairs = find_near_duplicates(samples, threshold=0.9)
        self.assertEqual([(item["left_id"], item["right_id"]) for item in pairs], [(1, 2)])

    def test_length_summary(self) -> None:
        self.assertEqual(
            describe_lengths([1, 3, 5, 7]),
            {"min": 1, "median": 4.0, "mean": 4.0, "max": 7},
        )


if __name__ == "__main__":
    unittest.main()
