from __future__ import annotations

import unittest

try:
    from math_os_prototype.world_novelty_check import (
        SurfaceNgramIndex,
        surface_ngrams,
        world_novelty,
    )
except ImportError:  # pragma: no cover
    from world_novelty_check import (
        SurfaceNgramIndex,
        surface_ngrams,
        world_novelty,
    )


class SurfaceNgramIndexTest(unittest.TestCase):
    def test_index_matches_exhaustive_exact_jaccard_search(self) -> None:
        statements = [
            ("first", r"\(x^2+2x+1=0\) を解け。"),
            ("second", r"三角形ABCの面積を求めよ。"),
            ("third", r"数列 \(a_{n+1}=2a_n+1\) の一般項を求めよ。"),
        ]
        rows = [
            (source, surface_ngrams(statement))
            for source, statement in statements
        ]
        index = SurfaceNgramIndex.build(rows)
        for query in (
            r"\(x^2+3x+1=0\) を解け。",
            r"三角形PQRの面積を求めよ。",
            r"素数をすべて求めよ。",
        ):
            with self.subTest(query=query):
                exhaustive = world_novelty(query, rows, set())
                indexed = world_novelty(query, index, set())
                self.assertEqual(indexed, exhaustive)


if __name__ == "__main__":
    unittest.main()
