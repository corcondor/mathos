from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

try:
    from math_os_prototype.run_test_shards import (
        TestModuleResult,
        assign_shards,
        discover_test_modules,
        merge_reports,
        unittest_context,
        write_report,
    )
except ImportError:
    from run_test_shards import (
        TestModuleResult,
        assign_shards,
        discover_test_modules,
        merge_reports,
        unittest_context,
        write_report,
    )


class TestShardRunnerTests(unittest.TestCase):
    def test_assignment_is_complete_disjoint_and_stable(self) -> None:
        modules = ["test_alpha", "test_beta", "test_gamma", "test_delta"]
        first = assign_shards(modules, 3)
        second = assign_shards(list(reversed(modules)), 3)
        self.assertEqual(sorted(item for shard in first for item in shard), sorted(modules))
        self.assertEqual([sorted(shard) for shard in first], [sorted(shard) for shard in second])

    def test_discovery_includes_each_test_file_once(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "test_a.py").touch()
            (root / "test_b.py").touch()
            (root / "helper.py").touch()
            self.assertEqual(discover_test_modules(root), ["test_a", "test_b"])

    def test_package_tests_run_from_parent_with_qualified_name(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "sample_package"
            root.mkdir()
            (root / "__init__.py").touch()
            cwd, target = unittest_context(root, "test_sample")
            self.assertEqual(cwd, root.parent)
            self.assertEqual(target, "sample_package.test_sample")

    def test_reports_merge_without_losing_failures(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            left = {
                "modules": [TestModuleResult("test_a", "passed", 2, 1.0, 0, "").__dict__],
                "elapsed_seconds": 1.0,
            }
            right = {
                "modules": [TestModuleResult("test_b", "failed", 1, 2.0, 1, "failure").__dict__],
                "elapsed_seconds": 2.0,
            }
            write_report({**left, "schema": 1, "generated_at": "x", "shard_index": 0, "shard_count": 2, "module_count": 1, "test_count": 2, "status_counts": {"passed": 1, "failed": 0, "timeout": 0}, "success": True}, root / "shard-0.json")
            write_report({**right, "schema": 1, "generated_at": "x", "shard_index": 1, "shard_count": 2, "module_count": 1, "test_count": 1, "status_counts": {"passed": 0, "failed": 1, "timeout": 0}, "success": False}, root / "shard-1.json")
            merged = merge_reports(list(root.glob("shard-*.json")))
            self.assertFalse(merged["success"])
            self.assertEqual(merged["module_count"], 2)
            self.assertEqual(merged["status_counts"]["failed"], 1)


if __name__ == "__main__":
    unittest.main()
