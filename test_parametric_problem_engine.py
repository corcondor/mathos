from __future__ import annotations

import unittest

from math_os_prototype.parametric_problem_engine import (
    all_instances,
    build_families,
    deduplicate,
    generate_one,
    generate_pool,
)


class ParametricEngineTests(unittest.TestCase):
    def test_every_emitted_instance_is_double_verified(self) -> None:
        instances = all_instances()
        self.assertGreater(len(instances), 60)
        for instance in instances:
            with self.subTest(instance=instance.candidate_id):
                self.assertTrue(instance.verified)
                self.assertTrue(instance.independent_check)
                self.assertTrue(instance.answer_tex)
                self.assertEqual(len(instance.morphism_chain), 3)

    def test_structure_changing_params_give_distinct_answers(self) -> None:
        # Faulhaber j=2..12 must all have different closed forms.
        faulhaber = [
            inst
            for inst in all_instances()
            if inst.family_id == "series.faulhaber_power_sum"
        ]
        answers = {inst.answer_tex for inst in faulhaber}
        self.assertEqual(len(answers), len(faulhaber))

    def test_dedup_keeps_distinct_answers_drops_repeat_answers(self) -> None:
        pool = generate_pool()
        problems = pool["problems"]
        # No two accepted problems share the same (family, answer).
        keys = {
            (p["family_id"], p["answer_tex"]) for p in problems
        }
        self.assertEqual(len(keys), len(problems))
        self.assertGreater(pool["summary"]["accepted"], 60)
        self.assertTrue(pool["summary"]["all_backend_verified"])

    def test_generate_one_is_deterministic_and_verified(self) -> None:
        first = generate_one(seed=1234)
        again = generate_one(seed=1234)
        self.assertIsNotNone(first)
        self.assertEqual(first["candidate_id"], again["candidate_id"])
        self.assertTrue(first["verification"]["exact_backend"])
        self.assertTrue(first["verification"]["independent_check"])
        self.assertTrue(first["accepted"])

    def test_external_corpus_collision_drops_instance(self) -> None:
        instances = all_instances()
        sample = instances[0]
        from math_os_prototype.jukenmath_full_audit import surface_ngrams

        external = [surface_ngrams(sample.statement_tex)]
        kept = deduplicate(instances, external_grams=external)
        kept_ids = {inst.candidate_id for inst, _ in kept}
        self.assertNotIn(sample.candidate_id, kept_ids)


if __name__ == "__main__":
    unittest.main()
