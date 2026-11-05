#!/usr/bin/env python3
"""Exact checks for v6_large_prime_cyclotomic.md.

The17-case region is derived in the proof. This is not a chosen search
box for the original equation. Only Python's standard library is used.
"""
from fractions import Fraction as F
from math import comb, isqrt
from pathlib import Path
import json

LOWER_P = 103
EXCLUSIVE_UPPER_P = 3**9
WITNESSES = [
    (107,54), (1355,689), (2459,1250), (3707,1884),
    (4811,2446), (6059,3080), (7163,3642), (8411,4276),
    (9515,4837), (10763,5472), (11867,6033), (13115,6668),
    (14219,7229), (15467,7864), (16571,8425), (17819,9059),
    (18923,9621),
]


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))


def lucas(n, k, q):
    answer = 1
    while n or k:
        a, b = n % q, k % q
        if b > a:
            return 0
        answer = answer * comb(a,b) % q
        n //= q
        k //= q
    return answer


def constant_checks():
    assert F(100,361) < F(1,3)
    assert 3*23**2 - 4*23 - 4 > 0
    assert 23**2 - 18*23 - 22 > 0
    assert 82*361 - 29400 == 202 > 0
    assert 700 < 722
    log_margin = 4**13 * 3**12 - 11**13
    ratio_margin = 38*238**2 - 147*121**2
    assert log_margin == 1141689649093 > 0
    assert ratio_margin == 245 > 0
    return {
        "log3_lower_bound_integer_margin": log_margin,
        "slope_comparison_integer_margin": ratio_margin,
        "proved_p_upper_bound_exclusive": EXCLUSIVE_UPPER_P,
    }


def finite_completion():
    # Generate the complete region by the two CRT arithmetic progressions.
    generated = sorted(
        p
        for residue in (107,1355)
        for p in range(residue,EXCLUSIVE_UPPER_P,2352)
        if p >= LOWER_P
    )
    # Independently verify coverage from the original modular conditions.
    independently_covered = [
        p for p in range(LOWER_P,EXCLUSIVE_UPPER_P)
        if p % 16 == 11 and p % 3 == 2
        and (76*p*p+69*p+83) % 49 == 0
    ]
    assert generated == independently_covered == [p for p,b in WITNESSES]
    assert len(generated) == 17
    rows = []
    for p,b in WITNESSES:
        numerator = 76*p*p+69*p+83
        assert numerator % 294 == 0
        s = numerator // 294
        lower_gap = s-b*b
        upper_gap = (b+1)*(b+1)-s
        # Witness verification is just multiplication and comparison; it
        # does not trust an approximate square root or a factoring routine.
        assert lower_gap > 0 and upper_gap > 0
        assert b == isqrt(s)
        rows.append({
            "p":p, "S":s, "square_lower_witness":b,
            "S_minus_b_squared":lower_gap,
            "next_square_minus_S":upper_gap,
        })
    return {
        "candidate_count":len(rows),
        "coverage_methods":[
            "two CRT arithmetic progressions",
            "independent congruence conditions in the proved p interval",
        ],
        "primality_assumed_in_completion":False,
        "unresolved":0,
        "rows":rows,
    }


def prime_power_identity(p,j,q,a,c,direct):
    assert prime(p) and prime(q) and j % 2 == 1
    assert j+2 <= p < 2*j
    assert F(j,p) < F(10,19)
    n = p*p+p+1
    d = q**a
    assert n == c*d and c in (1,3) and d > j*j
    h = a//2+1
    assert p < q**h
    i = j*p**3
    A = comb(i,j)
    assert A % (q**h) == 1
    l = lucas(A,p,q)
    x = lucas(i*i,j*j,q)
    assert (l,x) == (0,1)
    assert (p*p+1) % q != 0
    if direct:
        assert comb(A,p) % q == l
        assert comb(i*i,j*j) % q == x
    return {
        "p":p, "j":j, "q":q, "a":a, "cofactor":c,
        "normalization_exponent_h":h,
        "A_mod_q_to_h":A % (q**h),
        "L_mod_q":l, "X_mod_q":x,
        "right_side_mod_q":(x+p*p)%q,
        "direct_binomial_cross_check":direct,
    }


def seven_q_identity(p,j):
    assert prime(p) and j % 2 == 1
    assert j+2 <= p < 2*j and F(j,p) < F(10,19)
    n = p*p+p+1
    assert n % 7 == 0
    q = n//7
    assert prime(q) and q > p and q < j*j < 2*q
    i = j*p**3
    A = comb(i,j)
    L = comb(A,p)
    X = comb(i*i,j*j)
    predicted_x = (1+14*j*j*(p-1)) % q
    assert A % q == 1
    assert L % q == 0
    assert X % q == lucas(i*i,j*j,q) == predicted_x
    # Before setting the original equation residual to zero, the
    # transformation in the proof is an exact modular identity.
    residual = (X+p*p) % q
    transformed = (42*j*j+p-1) % q
    assert (residual*(p+2)+transformed) % q == 0
    return {
        "p":p, "j":j, "q":q,
        "A_mod_q":A%q, "L_mod_q":L%q,
        "X_mod_q_direct":X%q,
        "X_mod_q_formula":predicted_x,
        "equation_right_side_mod_q":residual,
        "quadratic_expression_mod_q":transformed,
        "direct_binomial_cross_check":True,
    }


def main():
    report = {
        "status":"pass",
        "scope":"Uniform proof in the companion note; exact17-case completion and formula checks here.",
        "original_equation_globally_solved":False,
        "new_claims_formalized_in_Lean":False,
        "exact_constants":constant_checks(),
        "finite_completion":finite_completion(),
        "prime_power_obstruction_checks":[
            prime_power_identity(59,31,3541,1,1,True),
            prime_power_identity(313,159,181,2,3,False),
        ],
        "seven_q_digit_identity_checks":[
            seven_q_identity(53,27),
            seven_q_identity(179,91),
        ],
    }
    destination = Path(__file__).with_name("v6_large_prime_cyclotomic_verification.json")
    destination.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))


if __name__ == "__main__":
    main()

