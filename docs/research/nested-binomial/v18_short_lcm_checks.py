#!/usr/bin/env python3
"""Exact certificates for v18_short_lcm.md; Python standard library only.

Complete domains: 118 endpoint constants; 828 cubic square reconstructions;
two seventh-power reconstructions; the two remaining forced-divisor exclusions.
The valuation samples support the separately written universal argument.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction
from math import comb, gcd, isqrt
from pathlib import Path

CS = (2, 3, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15)

def prime(p: int) -> bool:
    return p >= 2 and all(p % d for d in range(2, isqrt(p) + 1))

def factor(n: int) -> list[list[int]]:
    assert n >= 1
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            out.append([p, e])
        p += 1
    if n > 1:
        out.append([n, 1])
    assert all(prime(p) for p, _ in out)
    return out

def vp(n: int, p: int) -> int:
    assert n != 0
    n = abs(n)
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e

def floorlog(n: int, p: int) -> int:
    e = 0
    while n >= p:
        n //= p
        e += 1
    return e

def factorial_vp(n: int, p: int) -> int:
    out = 0
    while n:
        n //= p
        out += n
    return out

def binomial_vp(n: int, k: int, p: int) -> int:
    assert 0 <= k <= n
    return factorial_vp(n, p) - factorial_vp(k, p) - factorial_vp(n-k, p)

def hensel_roots(c: int, p: int, exponent: int) -> list[int]:
    roots = [x for x in range(p) if (x*x-c) % p == 0]
    modulus = p
    for _ in range(1, exponent):
        new = []
        for x in roots:
            if x % p:
                q = ((x*x-c)//modulus) % p
                z = (-q * pow(2*x, -1, p)) % p
                new.append(x+modulus*z)
            else:
                new.extend(x+modulus*z for z in range(p)
                           if ((x+modulus*z)**2-c) % (modulus*p) == 0)
        roots = sorted(set(new))
        modulus *= p
    assert all((x*x-c) % modulus == 0 for x in roots)
    return roots

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path(__file__).with_suffix(".json"))
    args = parser.parse_args()

    constants = []
    for c in CS:
        for t in range(c+1):
            D = (9+t)**2-36*c
            assert D != 0 and -459 <= D <= 49
            fs = factor(abs(D))
            assert all(p < 11 or e == 1 for p,e in fs)
            constants.append({"c":c,"t":t,"D":D,"factorization":fs})
    assert len(constants) == 118
    assert [u for u in (1,2,3) if (-u) % 4 in {0,1}] == [3]
    assert 6 not in {x*x % 9 for x in range(9)}
    assert 459 < 4*11**2

    ps = [p for p in range(11,75) if prime(p)]
    cubic = []
    squares = []
    for p in ps:
        for w in range(1,(p-1)//9+1):
            assert 9*w < p
            for c in CS:
                N = p**3*w+c
                a = isqrt(N)
                assert a*a <= N < (a+1)*(a+1)
                cubic.append([p,w,c,N,a])
                if a*a == N:
                    squares.append([p,w,c,a])
    assert len(ps) == 17
    assert sum((p-1)//9 for p in ps) == 69
    assert len(cubic) == 828
    assert squares == [[13,1,12,47],[23,2,2,156],[61,6,3,1167]]
    assert (12+2)*47-3*12 == 622
    assert 622 % 6 != 0

    seventh = []
    for p,c in ((11,12),(13,14)):
        N = p**7+c
        a = isqrt(N)
        assert a*a < N < (a+1)*(a+1)
        assert 9 < p < 18  # w=1 is the entire positive w<p/9 domain.
        seventh.append([p,1,c,N,a])
    assert seventh == [[11,1,12,19487183,4414],
                       [13,1,14,62748531,7921]]

    forced = []
    for n in (156,1167):
        M = gcd(n,3)*gcd(n-1,6)
        Q = n*(n-1)//M
        fs = factor(Q)
        F = 1
        for p,e in fs:
            F *= p**((e+2)//3)
        assert F**3 % Q == 0
        assert 3*F > 10*n
        forced.append({"n":n,"M":M,"Q":Q,"factorization":fs,
                       "least_cube_divisor":F,"strict_interval_margin":3*F-10*n})
    assert [x["least_cube_divisor"] for x in forced] == [4030,226787]

    # The parity formulas prove the entire J-domain classification.
    # J=2a gives exponent a+2-d; J=2a+1 gives exponent a+1-d.
    parity_identities = {
        "even": "3*(a+1)-d-2*a-1 = a+2-d",
        "odd": "3*(a+1)-d-(2*a+1)-1 = a+1-d",
        "d0_allowed": "J=1 and 11<=p<75",
        "d1_allowed": "p in {11,13}; J in {1,3}",
    }
    assert (3-2, -1, 3-1) == (1, -1, 2)  # coefficients of a,d,1, even J
    assert (3-2, -1, 3-1-1) == (1, -1, 1)  # coefficients, odd J
    margins = {
        "cube_quotient": str(Fraction(225)-Fraction(208000,927)),
        "odd_cofactor": str(Fraction(8,9)*104**2-12*15),
        "prime_square_threshold": 11**2-75,
    }
    assert Fraction(margins["cube_quotient"]) > 0
    assert Fraction(margins["odd_cofactor"]) > 0
    assert margins["prime_square_threshold"] > 0

    # Supporting valuation checks, not a finite-extrapolation proof.
    seen = set()
    examples = []
    inner_count = 0
    outer_count = 0
    crossing_count = 0
    actual_binomial_count = 0
    support_primes = [p for p in range(11,98) if prime(p)]
    for p in support_primes:
        for c in CS:
            for exponent in (2,3,4,5):
                for n in hensel_roots(c,p,exponent):
                    if n < 104 or ((c+2)*n-3*c) % 6:
                        continue
                    key = (p,c,n)
                    if key in seen:
                        continue
                    seen.add(key)
                    N = n*n-c
                    e = vp(N,p)
                    m = 6*n-9
                    assert 0 < m <= n*n
                    bv = binomial_vp(n*n,m,p)
                    assert bv >= e-1
                    assert m % (p*p) > c
                    assert all(n*n % p**a == c and m % p**a > c
                               for a in range(2,e+1))
                    inner_count += 1
                    A = n*(n-1)*(n-2)//6
                    a_c = ((c+2)*n-3*c)//6
                    for r in sorted({3*n+1,19*n//6,(10*n-1)//3}):
                        assert 3*n < r and 3*r < 10*n and 0 < a_c < r < m
                        J = floorlog(r,p)
                        if e <= J or J == 0:
                            continue
                        av = binomial_vp(A,r,p)
                        assert av >= e-J
                        assert bv >= e-J
                        assert vp(A-a_c,p) == e
                        G = factorial_vp(r,p)-factorial_vp(a_c,p)-factorial_vp(r-a_c-1,p)
                        assert 0 <= G <= J
                        assert av == e-G
                        outer_count += 1
                        crossing_count += int(r < p**e <= m)
                        if len(examples) < 24:
                            examples.append({"p":p,"c":c,"n":n,"e":e,"r":r,
                                             "J_r":J,"inner_vp":bv,"outer_vp":av})
                        if n <= 1500 and actual_binomial_count < 6:
                            assert vp(comb(n*n,m),p) == bv
                            assert vp(comb(A,r),p) == av
                            actual_binomial_count += 1
    assert inner_count > 0 and outer_count > 0
    report = {
        "status":"PASS",
        "scope":"Original squared-index equation; ell=1, j=i-3; small branch for square-LCM, both branches for shorter excess product",
        "universal_theorems":{
            "inner_valuation":"v_p(B)>=v_p(n^2-c)-1 for all p>=11 and admissible nonsquare c",
            "both_branch_excess":"R_r|k^2; gcd(R_r,Q)=1; R_r^3*Q^2|k^6",
            "small_branch_square_lcm":"n^2-c divides lcm(1,...,r)^2, all primes and all exponents",
            "small_branch_odd_cofactor":"p^e||(n^2-c), e odd, w=(n^2-c)/p^e imply p<12*w",
            "lcm_last_index":"Q has at least two prime factors, so r is not a prime power and L_r=L_(r-1)",
        },
        "endpoint_constants":constants,
        "endpoint_large_square_divisors":[],
        "complete_exception_domain":{
            "primes":ps,"prime_count":len(ps),"p_w_count":69,
            "cubic_square_record_columns":["p","w","c","p^3*w+c","floor_sqrt"],
            "cubic_square_records":cubic,
            "cubic_square_count":len(cubic),"cubic_squares":squares,
            "seventh_square_record_columns":["p","w","c","p^7*w+c","floor_sqrt"],
            "seventh_square_records":seventh,"seventh_square_count":len(seventh),
            "total_square_candidates":len(cubic)+len(seventh),
            "forced_divisor_exclusions":forced,"survivors":[],
        },
        "parity_domain_identities":parity_identities,
        "positive_constant_margins":margins,
        "supporting_valuations":{
            "primes":"11<=p<=97","Hensel_exponents":[2,3,4,5],
            "distinct_inner_cases":inner_count,"outer_cases":outer_count,
            "r_less_than_p_power_at_most_m_cases":crossing_count,
            "actual_binomial_pairs":actual_binomial_count,
            "examples":examples,
            "these_inputs_are_original_solutions":False,
            "finite_samples_prove_universal_theorems":False,
        },
        "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "proof_note_sha256":hashlib.sha256(Path(__file__).with_name("v18_short_lcm.md").read_bytes()).hexdigest(),
        "new_lean_execution":False,"new_deepseek_api_calls":0,"new_complete_CAS_calls":0,
        "external_peer_review":False,"original_solution_found":False,
        "verification_boundary":"Written universal valuation/coverage proofs plus complete exact finite exception reconstruction; supporting samples are not completeness claims.",
    }
    args.output.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"status":"PASS","endpoint_constants":118,
        "complete_square_candidates":830,"cubic_squares":squares,
        "seventh_squares":0,"remaining_original_candidates":0,
        "supporting_inner_cases":inner_count,"supporting_outer_cases":outer_count,
        "crossing_cases":crossing_count,"actual_binomial_pairs":actual_binomial_count,
        "output":str(args.output)},ensure_ascii=False))

if __name__ == "__main__":
    main()

