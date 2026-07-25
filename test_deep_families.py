from __future__ import annotations

import unittest

from construct_engine import (
    FIXED_SHARD_FAMILY_IDS,
    SHARD_FAMILIES,
    all_problems,
)
from deep_families import DEEP_FAMILIES


class DeepFamiliesTest(unittest.TestCase):
    def test_every_family_has_verified_candidates(self) -> None:
        for build, grid in DEEP_FAMILIES:
            candidates = [
                problem
                for parameters in grid()
                if (problem := build(parameters)) is not None
            ]
            self.assertTrue(candidates, build.__name__)
            self.assertTrue(all(problem.verified for problem in candidates))
            self.assertTrue(
                all(problem.independent_check for problem in candidates)
            )

    def test_ultradeep_families_have_at_least_ten_morphisms(self) -> None:
        ultradeep = []
        for build, grid in DEEP_FAMILIES:
            for parameters in grid():
                problem = build(parameters)
                if problem is not None and problem.family_id.startswith("ultradeep."):
                    ultradeep.append(problem)
        self.assertEqual(len({problem.family_id for problem in ultradeep}), 5)
        self.assertTrue(
            all(len(problem.morphism_chain) >= 10 for problem in ultradeep)
        )

    def test_action_shards_are_disjoint_and_cover_fixed_generation(self) -> None:
        statements_by_shard: dict[str, set[str]] = {}
        for shard in SHARD_FAMILIES:
            problems = all_problems(shard)
            self.assertTrue(problems, shard)
            self.assertTrue(
                all(
                    problem.family_id in FIXED_SHARD_FAMILY_IDS[shard]
                    for problem in problems
                ),
                shard,
            )
            statements_by_shard[shard] = {
                problem.statement_tex for problem in problems
            }

        shards = list(statements_by_shard)
        for index, left in enumerate(shards):
            for right in shards[index + 1 :]:
                self.assertFalse(
                    statements_by_shard[left] & statements_by_shard[right],
                    f"{left} overlaps {right}",
                )

        covered = set().union(*statements_by_shard.values())
        self.assertEqual(
            covered,
            {problem.statement_tex for problem in all_problems()},
        )


if __name__ == "__main__":
    unittest.main()
