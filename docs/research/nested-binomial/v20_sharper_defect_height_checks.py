#!/usr/bin/env python3
"""Exact finite constants supporting the written v20 upper-gap proof.

No finite n scan, floating-point logarithm, or general proof checker is used.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    checks = {}

    def record(name: str, value: bool) -> None:
        checks[name] = bool(value)
        if not value:
            raise AssertionError(name)

    alpha = F(47, 100)
    lower_log2 = 2 * (F(1, 3) + F(1, 3)**3 / 3)
    lower_log_n = 256 * lower_log2
    upper_x = alpha / lower_log_n
    record('integral_lower_log2', lower_log2 == F(56, 81))
    record('log_n_lower_constant', lower_log_n == F(14336, 81))
    record('log_n_lower_above_100', lower_log_n > 100)
    record('x_upper_constant', upper_x == F(3807, 1433600))
    record('x_below_one_hundredth', upper_x < F(1, 100))
    record('exponential_log2_upper', sum(F(7, 10)**j / __import__('math').factorial(j) for j in range(4)) > 2)
    record('derivative_log_below_three', F(8, 3)**3 > 6 * F(301, 100))
    record('log48_below_four', F(8, 3)**4 > 48)
    record('main_linear_constant', 3 * lower_log2 - F(103, 50) == F(19, 1350))
    record('positive_gap_margin', F(19, 1350) - 3 * upper_x > F(1, 200))
    record('A_lower_at_21', F(20*19, 6*21**2) > F(1, 7))
    record('A_above_16n_squared', 2**256 > 112)
    record('b_below_four_n', F(301, 100) + F(1, 2**256) < 4)
    record('four_a_over_n_below_13', 4 * F(301, 100) < 13)
    record('threshold_log_below_180', 256 * F(7, 10) < 180)
    record('threshold_binomial_margin', F(2**256, 200) > 197)
    record('threshold_log_over_n', F(180, 2**256) < F(1, 9000))
    record('threshold_n_ratio', F(2**256, 2**256-1) < F(1001, 1000))
    record('square_alpha_over_log_bound', alpha**2 / 100 < F(1, 400))
    constant = 6 * (6 * alpha + F(1, 400) + F(1, 1000)) * F(1001, 1000)
    record('defect_exact_coefficient', constant == F(16957941, 1000000))
    record('defect_coefficient_below_17', constant < 17)
    record('lower_range_defect_margin', 256 * F(7, 10) < 17*25)
    record('base_two_height_conversion', 25 * lower_log2 > 17)
    record('bit_height_reduction', 1-F(25,42) == F(17,42))

    # Independent exact expansions of the polynomial terms used in (11).
    import sympy as sp
    n, L, z = sp.symbols('n L z', positive=True)
    record('quadratic_height_identity', sp.expand(
        L*((3*n+z*n/L)**2-9*n*(n-1)) - ((6*z+z*z/L)*n+9*L)*n
    ) == 0)
    record('analytic_constant_identity', F(47,50) - 3 == -F(103,50))
    record('A_exp_lower_margin', sp.expand(4*(n-3)-3*n) == n-12)

    note = Path(__file__).with_name('v20_sharper_defect_height.md')
    result = {
        'status': 'PASS',
        'scope': 'Exact finite constants and symbolic identities supporting a written universal proof; not Lean verification.',
        'note_sha256': hashlib.sha256(note.read_bytes()).hexdigest(),
        'checks_count': len(checks),
        'checks': checks,
        'new_bounds': {
            'upper_gap_threshold': 'n >= 2^256',
            'upper_gap': 'r - 3*n < 47*n/(100*log(n))',
            'defect_height': 'log(n) < 17*delta; n < 2^(25*delta)',
            'low_range_input': 'Previously established delta >= 25',
        },
        'unresolved': 'delta is unbounded; the original equation is unsolved',
    }
    text = json.dumps(result, ensure_ascii=False, indent=2) + '\n'
    if args.output:
        args.output.write_text(text)
    print(text)


if __name__ == '__main__':
    main()
