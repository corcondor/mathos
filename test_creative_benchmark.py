import json
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path

from math_os_prototype.creative_benchmark import (
    CreativeProblemRecord,
    HumanRating,
    build_blind_pairs,
    build_creative_benchmark,
    load_human_jsonl,
    load_mathos_report,
    structural_signature,
)


REPORT_PATH = Path(
    "C:/Users/81808/.openclaw/workspace/math_os_prototype/problem_synthesis/geometry_sweep_repair1.json"
)


def record(
    record_id: str,
    source_kind: str,
    statement: str,
    *,
    task: str = "region",
) -> CreativeProblemRecord:
    return CreativeProblemRecord(
        record_id=record_id,
        source_kind=source_kind,
        author_system="human" if source_kind == "human" else "MathOS",
        domain="geometry",
        task=task,
        statement_tex=statement,
        answer="x^2-4y>=0",
        family_id="quadratic_sweep",
        strategy="existential_elimination",
        proof_obligations=["eliminate a real parameter", "find a quadratic boundary"],
        verification={"status": "verified"},
        difficulty={"level": "medium", "raw": 4},
        rights_basis="self_authored",
    )


class CreativeBenchmarkTests(unittest.TestCase):
    def test_rights_cleared_human_records_remove_missing_corpus_limitation(self):
        human = record("human-1", "human", "面積を求めよ。")
        report = build_creative_benchmark([human])
        self.assertNotIn(
            "No human-vs-system conclusion is valid until rights-cleared human records are loaded.",
            report["limitations"],
        )
        self.assertIn(
            "No single creativity score is emitted without blind human ratings.",
            report["limitations"],
        )

    def test_loads_verified_mathos_curriculum(self) -> None:
        records = load_mathos_report(REPORT_PATH)

        self.assertEqual(len(records), 37)
        self.assertTrue(all(item.verification["status"] == "verified" for item in records))
        self.assertTrue(all(item.rights_basis == "self_authored" for item in records))

    def test_numeric_surface_changes_do_not_change_structural_signature(self) -> None:
        first = record("a", "system", "Find the region for y=tx-t^2+1.")
        second = record("b", "system", "Find the region for y=2tx-3t^2+7.")

        self.assertEqual(structural_signature(first), structural_signature(second))

    def test_human_import_requires_rights_basis(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "human.jsonl"
            path.write_text(
                json.dumps(
                    {
                        "record_id": "human-1",
                        "domain": "geometry",
                        "task": "region",
                        "statement_tex": "Find a region.",
                    }
                ),
                encoding="utf-8",
            )

            with self.assertRaises(ValueError):
                load_human_jsonl(path)

    def test_blind_pairs_hide_source_and_internal_ids(self) -> None:
        human = record("human-1", "human", "Human problem")
        system = record("system-1", "system", "System problem")

        result = build_blind_pairs([human], [system], seed=7)

        self.assertEqual(len(result["public_pairs"]), 1)
        public = result["public_pairs"][0]
        self.assertNotIn("source", public)
        self.assertNotIn("human-1", json.dumps(public))
        self.assertEqual(len(result["private_key"]), 1)

    def test_blind_pairs_reject_same_task_with_different_output_geometry(self) -> None:
        human = replace(
            record("human-1", "human", "A moving solid"),
            metadata={"match_group": "geometry:3d:solid_volume"},
        )
        system = replace(
            record("system-1", "system", "A planar region"),
            metadata={"match_group": "geometry:2d:region"},
        )

        result = build_blind_pairs([human], [system], seed=7)

        self.assertEqual(result["public_pairs"], [])
        self.assertEqual(result["private_key"], [])

    def test_creativity_composite_requires_human_ratings(self) -> None:
        human = record("human-1", "human", "Human problem")
        system = record("system-1", "system", "System problem")

        without_ratings = build_creative_benchmark([human, system])
        self.assertTrue(
            all(item["creative_composite"] is None for item in without_ratings["records"])
        )

        ratings = [
            HumanRating(
                problem_id="system-1",
                rater_id="anonymous",
                rater_group="setter",
                naturalness=4,
                elegance=4,
                surprise=3,
                pedagogical_value=5,
                source_guess="system",
                source_confidence=4,
            )
        ]
        with_ratings = build_creative_benchmark([human, system], ratings=ratings)
        system_score = next(
            item for item in with_ratings["records"] if item["problem"]["record_id"] == "system-1"
        )
        self.assertIsNotNone(system_score["creative_composite"])

    def test_unverified_human_problem_is_unknown_not_invalid(self) -> None:
        human = record("human-1", "human", "Human problem")
        human = replace(human, verification={"status": "pending"})

        result = build_creative_benchmark([human])
        source = result["summary"]["sources"]["human"]

        self.assertEqual(source["valid"], 0)
        self.assertEqual(source["invalid"], 0)
        self.assertEqual(source["unknown"], 1)
        self.assertIsNone(source["validity_rate"])
        self.assertIsNone(result["records"][0]["evidence"]["validity_gate"])

    def test_expected_human_count_is_a_hard_observability_gate(self) -> None:
        human = record("human-1", "human", "Human problem")

        incomplete = build_creative_benchmark([human], expected_human_count=60)
        complete = build_creative_benchmark([human], expected_human_count=1)

        self.assertEqual(
            incomplete["summary"]["human_dataset_completeness"],
            {
                "expected": 60,
                "observed": 1,
                "missing": 59,
                "excess": 0,
                "complete": False,
            },
        )
        self.assertTrue(complete["summary"]["human_dataset_completeness"]["complete"])

    def test_system_count_and_pairing_coverage_are_reported(self) -> None:
        human = replace(
            record("human-1", "human", "A moving solid"),
            metadata={"match_group": "geometry:3d:solid_volume"},
        )
        system = replace(
            record("system-1", "system", "A planar region"),
            metadata={"match_group": "geometry:2d:region"},
        )

        result = build_creative_benchmark(
            [human, system],
            expected_human_count=1,
            expected_system_count=2,
        )

        self.assertFalse(result["summary"]["system_dataset_completeness"]["complete"])
        self.assertEqual(result["summary"]["pairing_coverage"]["potential_pairs"], 0)
        self.assertEqual(
            result["summary"]["pairing_coverage"]["human_records_without_match"],
            1,
        )

    def test_provisional_human_fingerprints_are_not_counted_as_certified_structure(self) -> None:
        provisional = record("human-1", "human", "A problem")
        certified = replace(
            record("human-2", "human", "Another problem"),
            metadata={"lift_certificates": [{"family_id": "verified.family"}]},
        )

        result = build_creative_benchmark([provisional, certified])
        source = result["summary"]["sources"]["human"]

        self.assertEqual(source["certified_structure_count"], 1)
        self.assertEqual(source["uncertified_structure_count"], 1)
        provisional_score = next(
            item for item in result["records"] if item["problem"]["record_id"] == "human-1"
        )
        self.assertIsNone(
            provisional_score["evidence"]["structural_novelty_against_human"]
        )


if __name__ == "__main__":
    unittest.main()
