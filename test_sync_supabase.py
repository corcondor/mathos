from __future__ import annotations

import unittest

try:
    from math_os_prototype.sync_supabase import stale_active_ids
except ImportError:  # pragma: no cover
    from sync_supabase import stale_active_ids


class SyncSupabaseTest(unittest.TestCase):
    def test_only_superseded_active_rows_are_archived(self) -> None:
        existing = {"keep-a", "keep-b", "old-version"}
        rows = [{"id": "keep-a"}, {"id": "keep-b"}, {"id": "new-version"}]
        self.assertEqual(stale_active_ids(existing, rows), ["old-version"])

    def test_order_and_duplicates_do_not_change_exact_set(self) -> None:
        existing = {"a", "b"}
        rows = [{"id": "b"}, {"id": "a"}, {"id": "a"}]
        self.assertEqual(stale_active_ids(existing, rows), [])


if __name__ == "__main__":
    unittest.main()
