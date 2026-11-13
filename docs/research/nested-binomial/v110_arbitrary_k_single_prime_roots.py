#!/usr/bin/env python3
"""v110: Unconditional SINGLE-prime finite-field solution algorithm for every k.

Branch of the ORIGINAL squared-index binomial equation:
  j=1, ell=k-1 -> choose(i,k) = i**2 + choose(k*k,2*k-1).

PREVIOUS WRITTEN MATHEMATICAL INPUT (v101):
  for k>=3 every nontrivial integer solution must satisfy 2*k<i<k**3.

For EVERY supplied k:
- Bertrand guarantees prime q with k**3 < q < 2*k**3;
- compute R_k mod q from O(k) short factors, without factoring R_k;
- factor a monic polynomial of degree k over Fq to propose roots;
- independently VERIFY completeness by Euclid gcd(F(X),X**q-X), computing
  X**q modulo F by repeated squaring, NEVER making a degree-q polynomial;
- as i<k**3<q, each root gives at most ONE candidate integer i;
- exact integer comparison on no more than k candidates.

The prime q is fully certified by trial division (unconditionally finite),
the algebraic root list is checked independently with finite-field gcd,
and no numerical k cutoff is used to support a universal no-solution claim.

For the complete universal written argument, see
V110_BERTRAND_ALL_K_ONE_PRIME_ROOT_ISOLATION_ja.md.

DEPENDENCIES: sympy for root extraction; v106_nonlocal_prime_units_audit
for independently implemented modular Euclidean polynomial arithmetic.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import sympy as sp

from v106_nonlocal_prime_units_audit import poly_gcd, poly_rem, mulmod, trim


def certified_prime(q: int) -> bool:
    """Unconditional trial-division proof of primality; slower than AKS/ECPP."""
    if q < 2:
        return False
    if q % 2 == 0:
        return q == 2
    p = 3
    limit = math.isqrt(q)
    while p <= limit:
        if q % p == 0:
            return False
        p += 2
    return True


def bertrand_prime(N: int) -> int:
    """A certified prime in (N,2N). No unproved short-gap conjectures."""
    assert N >= 2
    q = N + 1
    if q > 2:
        q += (q % 2 == 0)
    while q < 2*N:
        if certified_prime(q):
            assert N < q < 2*N
            return q
        q += 2
    raise AssertionError("This contradicts the classical Bertrand theorem")


def small_R_mod(k: int, q: int) -> int:
    """R=choose(k^2,2k-1) modulo q without computing R or factoring it."""
    m = 2*k-1
    assert q > k**3 > k*k > m
    numerator = 1
    for h in range(m):
        numerator = numerator * ((k*k-h) % q) % q
    return numerator * pow(math.factorial(m), -1, q) % q


def falling_minus_square_coeffs(k: int, Rmod: int, q: int) -> list[int]:
    """Ascending modular coeffs for product(X-h)-k!X²-k!R."""
    coeff = [1]
    for h in range(k):
        new = [0]*(len(coeff)+1)
        for n, z in enumerate(coeff):
            new[n] = (new[n]-h*z) % q
            new[n+1] = (new[n+1]+z) % q
        coeff = new
    fact = math.factorial(k)
    coeff[2] = (coeff[2]-fact) % q
    coeff[0] = (coeff[0]-fact*Rmod) % q
    assert len(coeff)==k+1 and coeff[-1] == 1
    return trim(coeff)


def power_mod(base:list[int], exp:int, modulus:list[int], p:int) -> list[int]:
    res = [1]
    a = poly_rem(base, modulus, p)
    while exp:
        if exp & 1:
            res = mulmod(res, a, modulus, p)
        exp //= 2
        if exp:
            a = mulmod(a, a, modulus, p)
    return res


def finite_field_root_certificate(coeff:list[int], q:int) -> dict:
    """A heuristic root proposal followed by an INDEPENDENT exact certificate."""
    assert coeff[-1] == 1
    X = sp.symbols("X")
    F = sp.Poly.from_list(list(reversed(coeff)), X, modulus=q)
    factors = sp.factor_list(F)[1]
    roots = set()
    for factor, exponent in factors:
        if factor.degree() == 1:
            a, b = (int(v)%q for v in factor.all_coeffs())
            roots.add((-b*pow(a, -1, q)) % q)

    # Exactly all roots: gcd(F, X^q-X) in F_q[X].
    # X^q is computed modulo F, so polynomial degrees never exceed k.
    xpow = power_mod([0, 1], q, coeff, q)
    xminus = xpow + [0]*max(0, 2-len(xpow))
    xminus[1] = (xminus[1]-1) % q
    d = poly_gcd(coeff, trim(xminus), q)

    from_roots = [1]
    for root in sorted(roots):
        new = [0]*(len(from_roots)+1)
        for n, c in enumerate(from_roots):
            new[n] = (new[n]-c*root) % q
            new[n+1] = (new[n+1]+c) % q
        from_roots = new
    assert from_roots == d, (
        "Incomplete or false linear root proposal", q, from_roots, d)
    assert len(roots) <= len(coeff)-1
    return {
        "all_roots_Fq": sorted(roots),
        "gcd_degree":len(d)-1,
        "verified_frobenius_gcd_equals_all_linear_root_factors":True,
        "no_field_roots":d == [1],
        "modular_polynomial_degree":len(coeff)-1,
    }


def certify(k:int, crosscheck:bool=False) -> dict:
    assert k >= 3
    q = bertrand_prime(k**3)
    c = small_R_mod(k, q)
    f = falling_minus_square_coeffs(k, c, q)
    roots = finite_field_root_certificate(f, q)
    candidates = [a for a in roots["all_roots_Fq"] if 2*k<a<k**3]
    assert len(candidates) <= k
    # Exact bigint evaluation only on the <=k algebraic root representatives.
    R_exact = None
    if candidates or crosscheck:
        R_exact = math.comb(k*k, 2*k-1)
        assert R_exact%q == c
    exact_checks = []
    for i in candidates:
        defect = math.comb(i, k) - i*i - R_exact
        exact_checks.append({
            "i":i,
            "integer_defect_zero":defect==0,
            "defect_sign":(defect>0)-(defect<0),
            "defect_mod_q":defect%q,
        })
        assert defect % q == 0
    found=[x["i"] for x in exact_checks if x["integer_defect_zero"]]
    return {
        "k":k, "bertrand_prime_q":q,"q_gt_k_cubed":q>k**3,
        "q_less_than_2k_cubed":q<2*k**3,
        "q_prime_proven_by_trial_division":True,
        "R_mod_q_small_factor_formula":c,
        "root_certificate":roots,
        "all_height_admissible_integer_candidates":candidates,
        "exact_bigint_candidate_evaluations":len(exact_checks),
        "exact_checks":exact_checks,
        "original_equation_solutions_with_v101_height":found,
        "certified_result":
            "EXACT_SOLUTION_FOUND" if found else "NO_SOLUTION_FOR_THIS_FIXED_K",
        "height_bound_status":
            "2k<i<k^3 is previous v101 written theorem; NOT Lean formalized here",
        "exhaustive_search_over_i":False,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--k", type=int, nargs="+",
        default=[3, 6, 8, 10, 14, 17])
    parser.add_argument("--output", type=Path)
    parser.add_argument("--crosscheck", action="store_true")
    args = parser.parse_args()
    records = []
    for k in args.k:
        row = certify(k, crosscheck=args.crosscheck)
        print("V110_CASE", json.dumps(row, ensure_ascii=False), flush=True)
        records.append(row)
    report = {
        "status":"PASS_UNCONDITIONAL_ARBITRARY_K_DECISION_ALGORITHM",
        "meaning":"the procedure works for EVERY input k>=3; listed cases are merely audits",
        "all_k_math_theorem_proven":"at most k exact candidates per k using Bertrand q>k^3",
        "all_k_nonexistence_proven":False,
        "original_four_variable_problem_solved":False,
        "cases":records,
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2, ensure_ascii=False)+"\n")
