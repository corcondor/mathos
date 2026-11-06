#!/usr/bin/env python3
"""Check the exact numerical comparisons in v15; not a proof assistant."""

import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


def run(output):
    comparisons = {
        "cube_height": (
            6 * (F(9, 56) + F(9, 12544))
            + F(6, 8192) * (9 + F(9, 56) + F(9, 12544)),
            F(1),
        ),
        "pell_height": (F(121, 40) ** 2, F(55, 6) * F(1023, 1024)),
        "complementary_cofactor": (6 * F(10829, 27) ** 3, F(20000) ** 2),
        "small_branch_cofactor": (36 * F(12032, 27) ** 3, F(240) ** 4),
        "prime_bound_general": (20000 * F(101, 100) ** 3 * F(100, 99), F(28) ** 3),
        "prime_bound_small_branch": (57600 * F(101, 100) ** 3 * F(100, 99) ** 2, F(40) ** 3),
    }
    for name, (left, right) in comparisons.items():
        if not left < right:
            raise AssertionError(name)
    if comparisons["cube_height"][0] != F(50111163, 51380224):
        raise AssertionError("cube height fraction")
    if comparisons["pell_height"][1] - comparisons["pell_height"][0] != F(363, 51200):
        raise AssertionError("Pell height gap")
    if not 2 ** 28 > 8192 + 1:
        raise AssertionError("exponential comparison base case")

    here = Path(__file__).resolve().parent
    notes = [
        "v15_cube_height.md",
        "v15_cubic_defect_sparsity.md",
        "v15_neighbor_prime_obstruction.md",
        "v15_pell_square_divisor.md",
    ]
    report = {
        "status": "PASS",
        "scope": "Exact rational comparisons only; the general arguments are written proofs, not machine-formalized here.",
        "comparisons": {
            name: {"left": str(left), "right": str(right), "positive_gap": str(right - left)}
            for name, (left, right) in comparisons.items()
        },
        "cube_height_exponential_base_case": {"left": 2 ** 28, "strict_lower": 8193},
        "note_sha256": {name: hashlib.sha256((here / name).read_bytes()).hexdigest() for name in notes},
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "new_lean_execution": False,
        "new_cas_calls": 0,
    }
    output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "exact_comparisons": len(comparisons), "output": str(output)}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("v15_theory_audit.json"))
    args = parser.parse_args()
    run(args.output)
