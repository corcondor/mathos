import unittest

try:
    from math_os_prototype.audit_backend_gaps import contract_for
except ImportError:
    from audit_backend_gaps import contract_for


class BackendGapAuditTests(unittest.TestCase):
    def test_how_many_is_an_observation_not_a_finite_domain_contract(self) -> None:
        record = {
            "problem_preview": "A machine makes 3 pieces per hour. How many pieces after 4 hours?",
            "intent": "cas_symbolic_algebra",
        }
        self.assertEqual("typed_rate_graph_contract_observe", contract_for(record))

    def test_combinatorial_domain_remains_finite(self) -> None:
        record = {
            "problem_preview": "In how many ways can 3 students be selected from 8 students?",
            "intent": "cas_symbolic_algebra",
        }
        self.assertEqual("finite_domain_filter_observe", contract_for(record))


if __name__ == "__main__":
    unittest.main()
