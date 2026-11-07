#!/usr/bin/env python3
"""Independent algebra and written-scope audit of v18_residual_gap.md.

Does not import or execute its producer. Standard library only.
"""
import argparse
import hashlib
import json
from fractions import Fraction as R
from pathlib import Path


def plus(*items):
    result = {}
    for item in items:
        for exps, coefficient in item.items():
            result[exps] = result.get(exps, 0) + coefficient
    return {k: v for k, v in result.items() if v}


def times(left, right):
    result = {}
    for lhs, c in left.items():
        for rhs, d in right.items():
            k = tuple(a + b for a, b in zip(lhs, rhs))
            result[k] = result.get(k, 0) + c * d
    return {k: v for k, v in result.items() if v}


def scalar(poly, c):
    return {k: c * v for k, v in poly.items() if c * v}


def power(poly, n):
    result = {(0, 0, 0): 1}
    for _ in range(n):
        result = times(result, poly)
    return result


def main():
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser()
    parser.add_argument("--note", type=Path, default=here / "v18_residual_gap.md")
    args = parser.parse_args()
    a, b, rho = {(1, 0, 0): 1}, {(0, 1, 0): 1}, {(0, 0, 1): 1}
    F = {
        (6, 0, 0): 4, (4, 2, 0): 24, (4, 0, 1): -12,
        (2, 4, 0): 36, (2, 2, 1): 60, (2, 0, 2): 12,
        (0, 2, 2): -3, (0, 0, 3): -4,
    }
    q0 = {(3, 0, 0): 2, (1, 2, 0): 6, (1, 0, 1): -3}
    D0 = plus(F, scalar(power(q0, 2), -1))
    assert D0 == {
        (2, 2, 1): 96, (2, 0, 2): 3,
        (0, 2, 2): -3, (0, 0, 3): -4,
    }
    positive = plus(
        scalar(times(times(power(b, 2), rho),
                     plus(scalar(power(a, 2), 32), scalar(rho, -1))), 3),
        times(power(rho, 2), plus(scalar(power(a, 2), 3), scalar(rho, -4))))
    assert D0 == positive
    # Independently clear the denominator in q1 before squaring.
    aq1_4 = plus(scalar(times(a, q0), 4),
                 scalar(times(rho, plus(rho, scalar(power(b, 2), 32))), 3))
    remainder = plus(scalar(times(power(a, 2), F), 16),
                     scalar(power(aq1_4, 2), -1))
    claimed = plus(
        scalar(times(times(power(a, 2), rho),
                     plus(power(rho, 2), scalar(times(power(b, 2), rho), 264),
                          scalar(power(b, 4), -576))), 8),
        scalar(times(power(rho, 2),
                     power(plus(rho, scalar(power(b, 2), 32)), 2)), -9))
    assert remainder == claimed
    envelope = {
        0: R(1, 2) - R(27, 64),
        1: R(132) - R(27, 64) * 64,
        2: R(-288) - R(27, 64) * 1024,
    }
    assert envelope == {0: R(5, 64), 1: R(105), 2: R(-720)}
    K5 = R(33 * 297 ** 2, 17 ** 2) * 56 ** 5
    K7 = R(297, 17) ** 3 * 1095 * 486 * 56 ** 7
    assert K5 == R(1603123474563072, 289)
    assert K7 == R(24078860209989084260597760, 4913)
    margins = {
        "q0_positive_cubic": R(26, 17) - R(3, 2),
        "rho_below_three_quarters": R(3, 4) - R(976, 1377),
        "region_I_envelope_slope": R(105) - R(720, 7),
        "region_I_a_squared": R(26) - R(542, 21),
        "retained_n_height": R(36) - R(10164, 289),
        "five_eighths": 40 ** 8 - K5,
        "seven_elevenths": 96 ** 11 - K7,
    }
    assert all(x > 0 for x in margins.values())
    assert R(28, 243) * R(297, 17) ** 2 == R(10164, 289)
    assert R(27) ** 2 * R(28, 243) / R(17) ** 2 == R(84, 289)
    checks = [
        "a>b follows from v17 h>81M under old necessary conditions; h>=93M is not assumed",
        "Positive integer rho and exact square discriminant F are inherited from v17",
        "q0 is an integer and positive, D0>0 follows from rho<3a^2/4, so the first separation is at least one",
        "The inequality a<rho(rho+32b^2) has the correct direction when inverted to bound u^2",
        "q1 has denominator dividing 4a; in region rho>=7b^2 the displayed lower envelope is positive",
        "No positivity of R1 is assumed for rho<7b^2; that entire region uses the first separation instead",
        "The positive integer 4a(y-q1) yields R1>3a^2/4 with no omitted equality case",
        "a^2<1095b^4rho^3 covers both residual regions, including any R1 zero in region II",
        "Eliminating a gives n^5<K5 u^8 and n^7<K7 u^11; b<=486 is used only at the stated global constant step",
        "The fixed-a and fixed-rho height powers 11/3 and 11/2 follow by squaring/cubing positive inequalities",
        "No finite support sample proves the universal result; no new Lean or complete elliptic solver is claimed",
    ]
    report = {
        "status": "PASS",
        "reviewer": "Separate cofactor research collaborator",
        "producer_imported_or_executed": False,
        "exact_polynomial_checks": [
            "F-q0^2 coefficient equality",
            "D0 positive grouping",
            "16a^2(F-q1^2) denominator-cleared coefficient equality",
            "Region I lower envelope coefficients",
        ],
        "exact_positive_rational_margins": {k: str(v) for k, v in margins.items()},
        "height_coefficient_equalities": ["(28/243)*(297/17)^2=10164/289",
                                          "(28/243)*(27/17)^2=84/289"],
        "written_review": checks,
        "scope": "n>=104,Q|r^3,3n<r<10n/3 and prior v16/v17 deductions; both original k branches",
        "proof_note_sha256": hashlib.sha256(args.note.read_bytes()).hexdigest(),
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "new_lean_execution": False,
        "external_peer_review": False,
        "verification_boundary": "Independent written review plus exact coefficient/rational checks; inherited finite v17 classification is not reexecuted",
    }
    out = here / "v18_residual_independent_audit.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: v for k, v in report.items() if k not in ("written_review",)}, indent=2))


if __name__ == "__main__":
    main()

