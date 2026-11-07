#!/usr/bin/env python3
"""Exact reduction certificate for v7_large_prime_prime_power_extensions.md.

This verifies polynomial identities and finite residue calculations. It does
not reprove the cited Thomas--Mignotte completeness theorem. It does not scan
the original Diophantine equation or assume a bound on its unknowns.

Only Python's standard library is required.
"""

import json
from math import comb, isqrt
from pathlib import Path


# Sparse polynomials in three independent indeterminates T, R, S over Z.
ZERO = {}
ONE = {(0, 0, 0): 1}
T = {(1, 0, 0): 1}
R = {(0, 1, 0): 1}
S = {(0, 0, 1): 1}


def add(*polys):
    out = {}
    for poly in polys:
        for monomial, coefficient in poly.items():
            out[monomial] = out.get(monomial, 0) + coefficient
    return {m: c for m, c in out.items() if c}


def scale(poly, scalar):
    return {m: scalar * c for m, c in poly.items() if scalar * c}


def sub(left, right):
    return add(left, scale(right, -1))


def mul(left, right):
    out = {}
    for lm, lc in left.items():
        for rm, rc in right.items():
            monomial = tuple(a + b for a, b in zip(lm, rm))
            out[monomial] = out.get(monomial, 0) + lc * rc
    return {m: c for m, c in out.items() if c}


def power(poly, exponent):
    result = ONE
    for _ in range(exponent):
        result = mul(result, poly)
    return result


def evaluate(poly, t, r, s):
    return sum(c * t**a * r**b * s**d for (a, b, d), c in poly.items())


PHI = add(power(T, 2), T, ONE)


def divide_by_phi(poly):
    """Exact division by the monic T^2+T+1 in Z[R,S][T]."""
    quotient = {}
    remainder = dict(poly)
    while True:
        candidates = [m for m in remainder if m[0] >= 2]
        if not candidates:
            break
        monomial = max(candidates)
        coefficient = remainder[monomial]
        term = {(monomial[0] - 2, monomial[1], monomial[2]): coefficient}
        quotient = add(quotient, term)
        remainder = sub(remainder, mul(term, PHI))
    assert add(mul(quotient, PHI), remainder) == poly
    return quotient, remainder


def eisenstein_mul(left, right):
    # (a+b*w)(c+d*w)=(ac-bd)+(ad+bc-bd)*w, w^2=-w-1.
    a, b = left
    c, d = right
    return sub(mul(a, c), mul(b, d)), sub(add(mul(a, d), mul(b, c)), mul(b, d))


def eisenstein_power(value, exponent):
    result = (ONE, ZERO)
    for _ in range(exponent):
        result = eisenstein_mul(result, value)
    return result


def norm(value):
    a, b = value
    return add(power(a, 2), scale(mul(a, b), -1), power(b, 2))


def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def lucas(top, bottom, prime):
    result = 1
    while top or bottom:
        top_digit, bottom_digit = top % prime, bottom % prime
        if bottom_digit > top_digit:
            return 0
        result = result * comb(top_digit, bottom_digit) % prime
        top //= prime
        bottom //= prime
    return result


def main():
    checks = []

    alpha = (T, scale(ONE, -1))
    beta = (R, S)
    omega = (ZERO, ONE)
    omega2 = eisenstein_power(omega, 2)
    assert eisenstein_power(omega, 3) == (ONE, ZERO)
    assert norm(alpha) == PHI
    assert norm(beta) == add(power(R, 2), scale(mul(R, S), -1), power(S, 2))
    checks.append("Eisenstein multiplication, units, and norms")

    p_form = add(power(R, 3), scale(mul(R, power(S, 2)), -3), power(S, 3))
    q_form = add(scale(mul(power(R, 2), S), 3), scale(mul(R, power(S, 2)), -3))
    assert eisenstein_power(beta, 3) == (p_form, q_form)
    c_form, d_form = eisenstein_mul(alpha, (p_form, q_form))
    assert c_form == add(mul(T, p_form), q_form)
    assert d_form == sub(mul(add(T, ONE), q_form), p_form)
    checks.append("Equations (14) and (15): exact cube and alpha-times-cube")

    assert eisenstein_mul(omega, (c_form, d_form))[1] == sub(c_form, d_form)
    assert eisenstein_mul(omega2, (c_form, d_form))[1] == scale(c_form, -1)
    checks.append("Equation (16): all three unit choices")

    w_form = add(R, mul(power(T, 2), S))
    quotient_c, remainder_c = divide_by_phi(sub(c_form, mul(T, power(w_form, 3))))
    quotient_cd, remainder_cd = divide_by_phi(
        sub(sub(c_form, d_form), mul(add(T, ONE), power(w_form, 3)))
    )
    assert remainder_c == remainder_cd == ZERO
    checks.append("Equation (17): both coefficient congruences modulo T^2+T+1")

    # F_(3t)(s,-r), with F_m(U,V)=U^3-mU^2V-(m+3)UV^2-V^3.
    u_form, v_form = S, scale(R, -1)
    thue_form = add(
        power(u_form, 3),
        scale(mul(mul(T, power(u_form, 2)), v_form), -3),
        scale(mul(mul(add(T, ONE), u_form), power(v_form, 2)), -3),
        scale(power(v_form, 3), -1),
    )
    assert thue_form == scale(d_form, -1)
    checks.append("Equation (19): reduction to Thomas--Mignotte parameter n=3t+1")

    # The published theorem supplies completeness of this six-pair list.
    trivial_pairs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1)]
    transformed = []
    for u, v in trivial_pairs:
        r, s = -v, u
        beta_norm = r * r - r * s + s * s
        assert beta_norm == 1
        for t in (2, 3, 5, 6):
            value = evaluate(thue_form, t, r, s)
            assert value in (-1, 1)
        transformed.append({"U": u, "V": v, "r": r, "s": s, "norm_beta": beta_norm})
    checks.append("Equation (20): all six transformed trivial solutions have norm one")

    # In these variables R stands for x; this is an identity, not a bounded check.
    assert sub(add(power(R, 2), R, ONE), PHI) == mul(sub(R, T), add(R, T, ONE))
    checks.append("Final identity Phi_3(x)-Phi_3(t)=(x-t)(x+t+1)")

    examples = []
    for t in (2, 3, 5, 6):
        c = t * t + t + 1
        assert is_prime(c) and c % 9 in (4, 7)
        assert pow(t, 3, c) == 1 and t % c != 1
        assert pow(t, (c - 1) // 3, c) != 1
        cubes = {pow(w, 3, c) for w in range(c)}
        image_c = {(t * z) % c for z in cubes}
        image_cd = {((t + 1) * z) % c for z in cubes}
        assert not ({1, c - 1} & image_c)
        assert not ({1, c - 1} & image_cd)
        examples.append({
            "t": t,
            "c": c,
            "c_mod_9": c % 9,
            "cubes_mod_c": sorted(cubes),
            "C_image_mod_c": sorted(image_c),
            "C_minus_D_image_mod_c": sorted(image_cd),
        })
    checks.append("Complete residue tables for c=7,13,31,43 reject both nontrivial unit cases")

    # Section 1's top-binomial identity. Here T=p, R=D; the defining equation
    # p^3-1=7D(p-1) makes the first factor on the right zero.
    correction = scale(mul(R, sub(T, ONE)), 7)
    lhs = sub(power(T, 6), power(add(ONE, correction), 2))
    rhs = mul(sub(sub(power(T, 3), ONE), correction), add(power(T, 3), ONE, correction))
    assert lhs == rhs
    assert power(add(ONE, correction), 2) == add(
        ONE,
        scale(mul(R, sub(T, ONE)), 14),
        scale(mul(power(R, 2), power(sub(T, ONE), 2)), 49),
    )
    checks.append("Equation (8): exact top-binomial expansion under N=7D")

    # Exact, structured checks of the generic Lucas digit formula. The top
    # below is generated from the proven expansion; these are not candidate
    # solutions to the original equation and no completeness is inferred.
    digit_cases = 0
    for prime in (13, 19):
        for exponent in (1, 2, 3, 4):
            d = prime**exponent
            for n in (d + 1, d + d // 2, 2 * d - 1):
                for p in (3, prime + 2):
                    top = n * (1 + 7 * d * (p - 1))**2
                    expected = (1 + 14 * n * (p - 1)) % prime
                    assert lucas(top, n, prime) == expected
                    digit_cases += 1
    checks.append("Equation (9): 48 structured exact checks of the generic Lucas digit formula")

    # The final congruence transformation, modulo Phi_3(p).
    # Here T=p and R=j^2.
    expression = add(scale(mul(R, sub(T, ONE)), 14), power(T, 2), ONE)
    transformed_congruence = add(scale(R, 42), T, scale(ONE, -1))
    _, remainder = divide_by_phi(add(mul(expression, add(T, scale(ONE, 2))), transformed_congruence))
    assert remainder == ZERO
    checks.append("Equation (10): exact congruence elimination to 42j^2+p-1")

    report = {
        "status": "PASS",
        "original_equation": "choose(choose(i,j),choose(k,ell)) = choose(i^2,j^2) + choose(k^2,ell^2)",
        "certificate_scope": "Exact algebraic reduction and finite residue checks, not a new proof of the cited completeness theorem",
        "external_theorem": {
            "author": "M. Mignotte",
            "title": "Verification of a Conjecture of E. Thomas",
            "doi": "10.1006/jnth.1993.1043",
            "statement_used": "For n>3, U^3-(n-1)U^2V-(n+2)UV^2-V^3=+/-1 has only the six trivial integral solutions",
            "parameter_substitution": "n=3t+1>=7",
            "completeness_reproved_by_this_script": False,
        },
        "check_count": len(checks),
        "checks": checks,
        "transformed_thue_trivial_solutions": transformed,
        "prime_cofactor_examples": examples,
        "generic_digit_cases": digit_cases,
        "unbounded_original_equation_scan": False,
        "unproved_scope_expansions": [
            "No replacement of modulus q by q^a in the prime-power digit condition",
            "No claim for composite c in the cubic-exponent theorem",
            "No exclusion of 7q^a for a>=2 and 3 not dividing a",
            "No Lean formalization claim",
        ],
    }
    output = Path(__file__).with_name("v7_large_prime_prime_power_extensions_verification.json")
    output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "PASS", "check_count": len(checks), "generic_digit_cases": digit_cases, "report": str(output)}))


if __name__ == "__main__":
    main()
