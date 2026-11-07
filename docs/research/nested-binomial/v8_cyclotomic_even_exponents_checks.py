#!/usr/bin/env python3
"""Exact structural checks for v8_cyclotomic_even_exponents.md.

No bounded search of the original equation is performed. The unbounded
statements follow from the written factorization and valuation proofs.
Only Python's standard library is required.
"""

import json
from math import comb, gcd, isqrt
from pathlib import Path


# Sparse polynomials in two independent variables R,T over Z.
ONE = {(0, 0): 1}
R = {(1, 0): 1}
T = {(0, 1): 1}


def add(*polys):
    out = {}
    for poly in polys:
        for m, c in poly.items():
            out[m] = out.get(m, 0) + c
    return {m: c for m, c in out.items() if c}


def scale(poly, scalar):
    return {m: scalar * c for m, c in poly.items() if scalar * c}


def sub(a, b):
    return add(a, scale(b, -1))


def mul(a, b):
    out = {}
    for (i, j), c in a.items():
        for (k, l), d in b.items():
            m = i + k, j + l
            out[m] = out.get(m, 0) + c * d
    return {m: c for m, c in out.items() if c}


def power(a, exponent):
    out = ONE
    for _ in range(exponent):
        out = mul(out, a)
    return out


def emul(a, b):
    # (x+y*w)(z+t*w)=(xz-yt)+(xt+yz-yt)*w.
    x, y = a
    z, t = b
    return sub(mul(x, z), mul(y, t)), sub(add(mul(x, t), mul(y, z)), mul(y, t))


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def vp(n, q):
    assert n > 0
    value = 0
    while n % q == 0:
        n //= q
        value += 1
    return value


def choose_mod_prime_power(n, k, q, exponent):
    """Factor-by-factor exact q-adic unit computation, no float arithmetic."""
    assert 0 <= k <= n and exponent >= 1
    modulus = q**exponent
    valuation, unit = 0, 1
    for i in range(1, k + 1):
        numerator, denominator = n - k + i, i
        while numerator % q == 0:
            numerator //= q
            valuation += 1
        while denominator % q == 0:
            denominator //= q
            valuation -= 1
        unit = unit * (numerator % modulus) * pow(denominator, -1, modulus) % modulus
    assert valuation >= 0
    return 0 if valuation >= exponent else unit * q**valuation % modulus


def main():
    checks = []
    beta = (R, T)
    alpha = (scale(ONE, 2), scale(ONE, -1))
    c_form = add(scale(power(R, 2), 2), scale(mul(R, T), 2), scale(power(T, 2), -3))
    f_form = add(power(R, 2), scale(mul(R, T), -6), scale(power(T, 2), 2))
    norm_beta = add(power(R, 2), scale(mul(R, T), -1), power(T, 2))
    assert emul(alpha, emul(beta, beta)) == (c_form, scale(f_form, -1))
    assert f_form == sub(power(sub(R, scale(T, 3)), 2), scale(power(T, 2), 7))
    assert add(power(c_form, 2), mul(c_form, f_form), power(f_form, 2)) == scale(power(norm_beta, 2), 7)
    assert sub(sub(c_form, scale(ONE, 2)), scale(mul(T, sub(scale(R, 2), T)), 7)) == scale(sub(f_form, ONE), 2)
    checks.append("Exact square factorization, norm identity, and C=7t(2r-t)+2 when F=1")

    squares_mod_7 = sorted({x*x % 7 for x in range(7)})
    assert 6 not in squares_mod_7
    mod3_pairs = [(r, t) for r in range(3) for t in range(3) if (r*r - 6*r*t + 2*t*t) % 3 == 1]
    assert all(t == 0 and r*r % 3 == 1 and (2*r*r + 2*r*t - 3*t*t) % 3 == 2 for r, t in mod3_pairs)
    parity_pairs = [(r, t) for r in range(1, 8, 2) for t in range(1, 8, 2)
                    if (r*r - 6*r*t + 2*t*t) % 8 == 1]
    assert parity_pairs and all(r*t % 4 == 3 and (r*r-r*t+t*t) % 4 == 3 for r, t in parity_pairs)
    assert [p for p in range(1, 8, 2) if (p*p+p+1) % 8 == 7] == [5]
    assert [p for p in range(168) if p % 3 == 2 and p % 7 == 2 and p % 8 == 5] == [149]
    checks.append("Complete residue tables for all sign, conjugation, parity, and CRT steps")

    # A nontrivial arithmetic example; it is not a candidate solution of the
    # original nested-binomial equation, and its y is not a prime power.
    r, t, p, y = 17, 3, 653, 247
    assert prime(p) and r*r - 6*r*t + 2*t*t == 1
    assert p == 2*r*r + 2*r*t - 3*t*t and y == r*r-r*t+t*t
    assert p*p+p+1 == 7*y*y and y % 4 == 3 and p % 168 == 149
    checks.append("Nontrivial arithmetic example p=653,y=247 satisfies the theorem")

    # Equation (18), with R=j,T=p and b=7j(p-1), as a polynomial identity.
    phi = add(power(T, 2), T, ONE)
    condition = add(scale(power(R, 2), 42), T, scale(ONE, -1))
    b_form = scale(mul(R, sub(T, ONE)), 7)
    lhs = scale(add(scale(power(b_form, 2), 2), scale(T, 14), scale(ONE, 7)), 3)
    rhs = sub(scale(mul(power(sub(T, ONE), 2), condition), 7), scale(mul(sub(T, scale(ONE, 4)), phi), 7))
    assert lhs == rhs
    # Elimination with R=b,T=p.
    z_form = add(scale(power(R, 2), 2), scale(ONE, 7))
    eliminated = sub(scale(phi, 196), mul(add(scale(T, 14), z_form), sub(add(scale(T, 14), scale(ONE, 14)), z_form)))
    assert eliminated == add(scale(power(R, 4), 4), scale(ONE, 147))
    assert 4*1**4+147 == 151 and prime(151)
    assert 4*2**4+147 == 211 and prime(211)
    checks.append("Exact congruence elimination and the two exceptional primes 151,211")

    outer_cases = []
    for q in (13, 19):
        for s in (1, 2):
            u = q**s
            for h in (3, 5, q+1, q+2, q+3):
                A = 1 + u*h
                for residue in (2, 3, 7):
                    p = 2*u + residue
                    assert 2*u+1 < p < 3*u and gcd(p*(p-1), q) == 1
                    value = comb(A, p)
                    expected_v = s + vp(h-1, q) + vp(h-2, q)
                    assert vp(value, q) == expected_v
                    normalized = (value // u) % q
                    # The low block contributes (-1)^p. In the original
                    # application p is an odd prime, hence this sign is -1.
                    expected_unit = (-1)**p*h*(h-1)*(h-2)*pow(2*p*(p-1), -1, q) % q
                    assert normalized == expected_unit
                    outer_cases.append({"q": q, "s": s, "H": h, "p_mod_u": residue, "valuation": expected_v})
    assert len(outer_cases) == 60
    checks.append("60 exact generic cases of the outer valuation and normalized-residue block lemmas")

    # Generic instance of the retained-index product identity. Here the top
    # is n*(1+7u^2*c)^2, so its displacement from n has valuation exactly2s.
    # No original p or binomial equation is searched.
    reduced_cases = []
    for q, s in ((13, 1), (19, 1), (13, 2), (19, 2)):
        u = q**s
        for offset in (1, 3):
            j = u + offset
            n = j*j
            assert u*u < n < 2*u*u and j % q
            for c in (1, 2):
                top = n * (1 + 7*u*u*c)**2
                M = (top-n) // u
                K = n // u
                assert top-n == u*M and vp(top-n, q) == 2*s and K < 2*u
                left = choose_mod_prime_power(top, n, q, s+1)
                right = choose_mod_prime_power(M+K, K, q, s+1)
                assert left == right
                if s == 1:
                    assert left == comb(top, n) % q**(s+1)
                reduced_cases.append({"q": q, "s": s, "j_offset": offset, "c": c, "original_bottom": n, "reduced_bottom": K})
    assert len(reduced_cases) == 16
    checks.append("16 exact generic product reductions, with direct-binomial cross-checks at s=1")

    residue_examples = []
    for q in (13, 37):
        assert prime(q) and q % 12 == 1
        left, right = pow(-3, (q-1)//4, q), pow(42, (q-1)//2, q)
        assert left != right
        primitive_cube_roots = [p for p in range(q) if (p*p+p+1) % q == 0]
        assert len(primitive_cube_roots) == 2
        # Independent complete finite check of the original quadratic condition.
        assert all((42*j*j+p-1) % q for p in primitive_cube_roots for j in range(q))
        residue_examples.append({"q": q, "left": left, "right": right, "primitive_cube_roots": primitive_cube_roots})
    checks.append("Prime-only obstruction and complete independent finite checks for q=13,37")

    report = {
        "status": "PASS",
        "scope": "Exact structural checks supporting separate uniform proofs; no search of the original nested-binomial equation",
        "check_groups": len(checks),
        "checks": checks,
        "squares_mod_7": squares_mod_7,
        "F_equal_1_mod_3_pairs": mod3_pairs,
        "odd_F_equal_1_mod_8_pairs": parity_pairs,
        "outer_digit_case_count": len(outer_cases),
        "outer_digit_cases": outer_cases,
        "product_reduction_case_count": len(reduced_cases),
        "product_reduction_cases": reduced_cases,
        "prime_only_obstruction_examples": residue_examples,
        "new_external_completeness_theorem_used": False,
        "full_large_prime_branch_solved": False,
        "not_lean_formalized": True,
    }
    output = Path(__file__).with_name("v8_cyclotomic_even_exponents_verification.json")
    output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "check_groups": len(checks), "outer_cases": len(outer_cases), "product_cases": len(reduced_cases), "report": str(output)}))


if __name__ == "__main__":
    main()
