from __future__ import annotations

import unittest

from construct_engine import (
    FIXED_SHARD_FAMILY_IDS,
    SHARD_FAMILIES,
    _verified_problem_entries,
    all_problems,
    explore_random,
)
from deep_families import DEEP_FAMILIES
from geometry_deep_families import GEOMETRY_DEEP_FAMILIES


ALL_DEEP_FAMILIES = DEEP_FAMILIES + GEOMETRY_DEEP_FAMILIES


class DeepFamiliesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.entries = _verified_problem_entries()
        cls.problems = [entry[2] for entry in cls.entries]

    def test_every_family_has_verified_candidates(self) -> None:
        for build, _grid in ALL_DEEP_FAMILIES:
            candidates = [
                problem
                for source, _is_traceback, problem in self.entries
                if source == build.__name__
            ]
            self.assertTrue(candidates, build.__name__)
            self.assertTrue(all(problem.verified for problem in candidates))
            self.assertTrue(
                all(problem.independent_check for problem in candidates)
            )

    def test_ultradeep_families_have_at_least_ten_morphisms(self) -> None:
        ultradeep = [
            problem
            for problem in self.problems
            if problem.family_id.startswith("ultradeep.")
        ]
        self.assertGreaterEqual(len({problem.family_id for problem in ultradeep}), 10)
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

    def test_random_exploration_deduplicates_parameter_tuples(self) -> None:
        problems = explore_random(
            samples=6000,
            seed=7,
            only_family="cubic_tangent",
        )
        self.assertLessEqual(len(problems), 25)
        self.assertEqual(
            len(problems),
            len(
                {
                    tuple(sorted(problem.parameters.items()))
                    for problem in problems
                }
            ),
        )

    def test_geometry_families_do_not_collapse_to_divisor_count(self) -> None:
        representatives = []
        for build, _grid in GEOMETRY_DEEP_FAMILIES:
            problem = next(
                (
                    candidate
                    for source, _is_traceback, candidate in self.entries
                    if source == build.__name__
                ),
                None,
            )
            self.assertIsNotNone(problem, build.__name__)
            representatives.append(problem)

        self.assertEqual(len(representatives), len(GEOMETRY_DEEP_FAMILIES))
        self.assertTrue(
            all("約数" not in problem.statement_tex for problem in representatives)
        )
        self.assertGreaterEqual(
            len({problem.morphism_chain[-1] for problem in representatives}),
            4,
        )


if __name__ == "__main__":
    unittest.main()
