import unittest

from math_os_prototype.audit_proof_gate import summarize


class ProofGateAuditTests(unittest.TestCase):
    def test_gate_can_improve_precision_without_claiming_new_solutions(self):
        records = [
            {"answer": "1", "exact_match": True, "verification": "verified"},
            {"answer": "2", "exact_match": False, "verification": "partial"},
            {"answer": None, "exact_match": False, "verification": "partial"},
        ]
        current = summarize(records, lambda record: record.get("answer") is not None)
        gated = summarize(
            records,
            lambda record: record.get("answer") is not None
            and record.get("verification") == "verified",
        )
        self.assertEqual(current["correct"], gated["correct"])
        self.assertGreater(gated["answer_precision"], current["answer_precision"])


if __name__ == "__main__":
    unittest.main()
