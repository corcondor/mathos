#!/usr/bin/env python3
"""Complete check after the written bound 1 < a < 24."""
import hashlib
import json
from math import gcd
from pathlib import Path

root = Path(__file__).resolve().parent
pairs = [(a, b) for a in range(2, 24) for b in range(1, a)]
primitive = [(a, b) for a, b in pairs if gcd(a, b) == 1]
solutions = [(a, b) for a, b in primitive if 24 * a % (a*a + 3*b*b) == 0]
assert solutions == [(3, 1)]
report = {
    "status": "PASS",
    "domain_justification": "a^2+3b^2 divides 24a => a^2 < 24a => a < 24",
    "complete_pairs": len(pairs),
    "coprime_pairs": len(primitive),
    "all_solutions": solutions,
    "note_sha256": hashlib.sha256((root/"v19_problem_seed_ja.md").read_bytes()).hexdigest(),
    "scope": "Written elementary proof plus complete verification of its bounded domain; no Lean execution."
}
(root/"v19_problem_seed_verification.json").write_text(json.dumps(report, indent=2)+"\n")
print(json.dumps(report, indent=2))

