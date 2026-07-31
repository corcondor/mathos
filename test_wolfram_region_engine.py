from __future__ import annotations

import unittest

try:
    from math_os_prototype.tool_adapters import ToolExecution
    from math_os_prototype.wolfram_region_engine import build_passage_region
except ImportError:  # pragma: no cover
    from tool_adapters import ToolExecution
    from wolfram_region_engine import build_passage_region


class RecordingWolframAdapter:
    def __init__(self, counterexample: str) -> None:
        self.counterexample = counterexample
        self.calls: list[str] = []

    def execute_code(self, code: str, label: str) -> ToolExecution:
        self.calls.append(code)
        output = (
            "MATHOS_REGION=x >= 0 && y >= 0\n"
            f"MATHOS_COUNTEREXAMPLE={self.counterexample}\n"
            "MATHOS_EQUIVALENT="
            f"{'True' if self.counterexample == 'False' else 'False'}"
        )
        return ToolExecution(
            tool="wolfram",
            available=True,
            command=[code],
            status="executed",
            stdout=output,
        )


class WolframRegionEngineTest(unittest.TestCase):
    def test_accepts_only_when_xor_counterexample_set_is_empty(self) -> None:
        adapter = RecordingWolframAdapter("False")
        problem = build_passage_region(
            {"a": 2, "lo": 0, "hi": 1},
            adapter,  # type: ignore[arg-type]
        )
        self.assertIsNotNone(problem)
        self.assertEqual(problem.counterexample_set, "False")
        self.assertTrue(problem.verified)
        self.assertEqual(len(adapter.calls), 1)
        self.assertIn("Reduce[Xor[region,expected]", adapter.calls[0])

    def test_rejects_a_nonempty_counterexample_set(self) -> None:
        adapter = RecordingWolframAdapter("x == 0 && y == 1")
        problem = build_passage_region(
            {"a": 2, "lo": 0, "hi": 1},
            adapter,  # type: ignore[arg-type]
        )
        self.assertIsNone(problem)
        self.assertEqual(len(adapter.calls), 1)


if __name__ == "__main__":
    unittest.main()
