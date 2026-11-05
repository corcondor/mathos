#!/usr/bin/env python3
"""Exact consistency checks for the offset-three proof notes.

This checks algebraic constants and the six remaining a=7 cases.
It is deliberately not a bounded search offered as an infinite proof.
The complete infinite argument is in the companion Markdown notes.
"""
import json
from math import comb
from pathlib import Path


def strip_three(value):
    valuation = 0
    while value % 3 == 0:
        valuation += 1
        value //= 3
    return valuation, value


def normalized_product(top, bottom):
    """Independent valuation and unit of C(top,bottom), modulo 9.

    Multiply the rational product one factor at a time, stripping every
    factor of 3 before taking residues. This does not call math.comb.
    """
    valuation = 0
    unit = 1
    for m in range(1, bottom + 1):
        numerator_val, numerator_unit = strip_three(top + 1 - m)
        denominator_val, denominator_unit = strip_three(m)
        valuation += numerator_val - denominator_val
        unit = (unit * numerator_unit * pow(denominator_unit, -1, 9)) % 9
    return valuation, unit


def main():
    # Independently expand the shifted polynomial by coefficient arithmetic.
    coefficients = [42, -512, 1536, -400, 6]
    shifted = [sum(coefficients[k] * comb(k, j) * 64 ** (k-j)
                   for k in range(j, len(coefficients)))
               for j in range(len(coefficients))]
    assert shifted == [2064426, 1572352, 72192, 1136, 6]

    upper_constant = 125 * 2**38 * 104**2 - 216 * 33**10
    sharper_constant = 2**103 - 3**37 * 5**19
    assert upper_constant == 40813869371167016 > 0
    assert sharper_constant == 1552720879039172862272697908633 > 0
    assert 7**8 < 3 * 8**7
    assert 3**24 == 282429536481 < 2**18 * 5**9 == 512000000000
    assert 6**5 > 2 * 5**5
    assert 3**10 > 2**15

    cube_sets = {p: sorted({pow(v, 3, p) for v in range(1, p)})
                 for p in (13, 19)}
    assert all(120 % p not in cube_sets[p] for p in cube_sets)
    unit_cubes_mod_9 = sorted({pow(v, 3, 9) for v in range(1, 9)
                               if v % 3 != 0})
    assert unit_cubes_mod_9 == [1, 8]

    a, h, alpha, d = 7, 2, 6, 4
    n = 3**a
    q = 3**alpha
    A = comb(n, 3)
    T = A // q
    X = comb(n*n, 6*n-9)
    x_valuation, _ = strip_three(X)
    assert x_valuation == 2*a-2 == 12
    assert X % (3**(2*d)) == 0
    x_normalized = (X // 3**(2*d)) % 9
    assert x_normalized == 0
    h_valuation, h_unit = normalized_product(T-1, 9)
    assert (h_valuation, h_unit) == (alpha, 4)

    expected = [(82, 6642, 1, 4, 1), (83, 6723, 1, 7, 4),
                (85, 6885, 7, 2, 7), (86, 6966, 7, 2, 7),
                (88, 7128, 1, 7, 4), (89, 7209, 1, 4, 1)]
    rows = []
    for v, r, expected_u, expected_l, expected_rhs in expected:
        assert r == 3**d * v
        assert 3*n < r and 3*r < 10*n
        assert v % 3 != 0

        # The first route computes the whole integer binomial exactly.
        direct_l = comb(A, r)
        direct_val, direct_unit = strip_three(direct_l)
        direct_unit %= 9
        assert direct_val == 2*d
        assert direct_unit == expected_l

        # The second route strips each individual factor in C(A-1,r-1).
        product_val, product_unit = normalized_product(A-1, r-1)
        assert product_val == alpha
        product_l_unit = (T * product_unit * pow(v, -1, 9)) % 9
        assert alpha - d + product_val == 2*d
        assert product_l_unit == direct_unit

        # The third route uses the explicit q-block and the small unit list.
        special_s = [s for s in range(1, (r-1)//(q//3)+1) if s % 3]
        unit_product = 1
        for s in special_s:
            unit_product = unit_product * (1 - 3*T*pow(s, -1, 9)) % 9
        assert unit_product == expected_u
        theorem_unit = (4 * (-1)**r * unit_product * pow(v, -1, 9)) % 9
        assert theorem_unit == direct_unit

        branch_residues = []
        for B in (r, A-r):
            Y = B*B
            y_valuation, _ = strip_three(Y)
            assert y_valuation == 2*d
            rhs_unit = ((X+Y)//3**(2*d)) % 9
            assert rhs_unit == expected_rhs == v*v % 9
            assert direct_unit != rhs_unit
            branch_residues.append(rhs_unit)
        rows.append({"v": v, "r": r,
                     "special_unit_factor_count": len(special_s),
                     "unit_product_mod_9": unit_product,
                     "left_valuation": direct_val,
                     "left_unit_direct_math_comb": direct_unit,
                     "left_unit_stripped_product": product_l_unit,
                     "left_unit_q_block_formula": theorem_unit,
                     "right_units_lower_upper": branch_residues})

    result = {
        "status": "pass",
        "scope": "Exact constants and all six a=7 residual cases; infinite proof is in the companion Markdown notes",
        "formalized_in_Lean": False,
        "shifted_polynomial_coefficients_ascending": shifted,
        "upper_gap_positive_integer": upper_constant,
        "sharper_gap_positive_integer": sharper_constant,
        "nonzero_cube_residue_sets": cube_sets,
        "unit_cubes_modulo_9": unit_cubes_mod_9,
        "a_7_parameters": {"a": a, "h": h, "n": n, "A": A,
                           "alpha": alpha, "d": d,
                           "X_valuation": x_valuation,
                           "X_normalized_mod_9": x_normalized,
                           "q_block_valuation": h_valuation,
                           "q_block_unit_mod_9": h_unit},
        "a_7_rows": rows,
        "independent_proof_review": {
            "v5_offset_three_structure.md": ["root: passed", "v5_l1_gap: passed"],
            "v5_offset_three_three_power.md": ["root: passed", "v5_l1_gap: passed"]}
    }
    output = Path(__file__).with_name("v5_offset_three_verification.json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
