#!/usr/bin/env python3
"""Exact checks for v17_neighbor_defect.md; standard library only."""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction
from functools import lru_cache
import gzip
import hashlib
import json
from math import gcd, isqrt
from pathlib import Path

MAX_COFACTOR = 64

@lru_cache(None)
def factor(n: int) -> tuple[tuple[int, int], ...]:
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            out.append((p, e))
        p = 3 if p == 2 else p + 2
    if n > 1:
        out.append((n, 1))
    return tuple(out)

@lru_cache(None)
def first_divisors(c0: int, epsilon: int) -> tuple[int, ...]:
    ds = [1]
    for p, e in factor(c0):
        power = 3 * e if epsilon else (3 * e) // 2
        old = ds[:]
        term = 1
        for _ in range(power):
            term *= p
            ds.extend(a * term for a in old)
    return tuple(sorted(ds))

# Bivariate polynomial arithmetic, with exact integer coefficients.
def add(*ps):
    out = Counter()
    for p in ps:
        for k, a in p.items():
            out[k] += a
    return {k: a for k, a in out.items() if a}
def scale(p, a):
    return {k: a * b for k, b in p.items() if a * b}
def mul(p, q):
    out = Counter()
    for (a, b), x in p.items():
        for (c, d), y in q.items():
            out[(a + c, b + d)] += x * y
    return {k: a for k, a in out.items() if a}
def pw(p, n):
    out = {(0, 0): 1}
    for _ in range(n):
        out = mul(out, p)
    return out

def check_identities():
    one = {(0, 0): 1}
    x = {(1, 0): 1}
    y = {(0, 1): 1}
    C = lambda a: scale(one, a)
    N = add(pw(x, 2), C(2))
    u = add(y, C(3))
    D0 = add(scale(mul(x, add(y, C(-1))), 6), pw(y, 2), C(-10))
    D1 = add(scale(mul(x, add(y, C(-2))), 6), pw(add(y, C(-1)), 2), C(-10))
    equations = {}
    for eps, D in [(0, D0), (1, D1)]:
        r_minus_eps = add(scale(x, 3), y, C(-eps))
        equations[f'neighbor_excess_epsilon_{eps}'] = add(
            pw(r_minus_eps, 2), scale(x, -6), C(8), scale(N, -9), scale(D, -1))
    R0 = add(
        mul(add(y, C(-4)), add(scale(pw(x, 2), 24), mul(x, add(scale(y, 7), C(22))))),
        scale(mul(add(x, C(-6)), u), 6))
    equations['small_branch_positive_comparison'] = add(scale(mul(x, D0), 7), scale(mul(u, N), -18), scale(R0, -1))
    R1 = add(
        mul(add(y, C(-4)), add(scale(pw(x, 2), 13), scale(mul(x, add(y, C(2))), 3), C(-10))),
        pw(x, 2), scale(x, -3), C(-70))
    equations['complementary_positive_comparison'] = add(scale(mul(x, D1), 3), scale(mul(u, N), -5), scale(R1, -1))
    equations['small_branch_coefficient_gcd'] = add(
        scale(add(scale(x, 10), scale(y, 2)), 5),
        scale(add(scale(x, 25), scale(y, 3)), -2), scale(y, -4))
    equations['complementary_coefficient_gcd'] = add(
        scale(add(scale(x, 9), scale(y, 2)), 8),
        scale(add(scale(x, 24), scale(y, 3)), -3), scale(y, -7))
    for label, residual in equations.items():
        assert not residual, (label, residual)
    return {label: 'all coefficients zero' for label in equations}

def check_constants():
    F = Fraction
    margins = {
        'small_height': F(52**2) - F(24064, 9),
        'complementary_height': F(983**2) - 6 * F(10829, 27)**2,
        'complementary_prime_bound': F(32**2) - 983 * F(10201, 9900),
        'fixed_J_height_after_cubing': F(1024**3) - F(224, 9)**3 * F(8000, 33)**2,
        'fixed_J_cofactor': F(2**20) - F(224, 9) * 2**15,
        'small_prime_bound_at_n104': F(104**2 - 53*104 - 104),
        'complementary_positive_remainder_at_n104': F(104**2 - 3*104 - 70),
    }
    assert all(v > 0 for v in margins.values())
    return {k: str(v) for k, v in margins.items()}

def check_local_transfer():
    cases = 0
    for N in range(1, 81):
        for r in range(1, 121):
            if r**3 % N:
                continue
            delta = N // gcd(N, r*r)
            assert N % delta**3 == 0
            for w in range(1, 9):
                for eps in (0, 1):
                    for shift in (0, 1):
                        c = w*r*(r-2*eps) + shift*N
                        assert c**(1+eps) % (N//delta) == 0
                        assert c % delta**(2-eps) == 0
                        assert c**3 % N**(2-eps) == 0
                        cases += 1
    return {'cases': cases, 'domain': '1<=N<=80, 1<=r<=120, N|r^3, 1<=w<=8, epsilon=0/1, shifts=0/1',
            'finite_supporting_checks_only': True}

def cofactor_certificate():
    totals = Counter()
    families = []
    second_candidates = []
    integral_p_candidates = []
    square_witnesses = []
    residual = []
    used_c0 = set()
    largest_generated_n = 0
    for w in range(1, MAX_COFACTOR + 1):
        for z in range(9*w + 1, (100*w - 1)//9 + 1):
            for eps in (0, 1):
                c0 = 2*z - (8+eps)*w
                c1 = 3*z - (2+eps)*w
                used_c0.add(c0)
                count = Counter(families=1)
                c1cube = c1**3
                for d in first_divisors(c0, eps):
                    for g in (1, 3):
                        n = g*d
                        largest_generated_n = max(largest_generated_n, n)
                        count['divisor_points'] += 1
                        if n < 104 or gcd(n, 3) != g:
                            continue
                        count['normalized_n'] += 1
                        Q1 = (n-1)//gcd(n-1, 6)
                        if c1cube % Q1**(2-eps):
                            continue
                        count['second_divisor'] += 1
                        second_candidates.append([w, z, eps, n])
                        N = n*n + 2
                        if N % w:
                            continue
                        count['integral_p'] += 1
                        p = N//w
                        integral_p_candidates.append([w, z, eps, n, p])
                        if p <= 6*n-9:
                            continue
                        count['p_large'] += 1
                        S = z*p + 6*n-8
                        a = isqrt(S)
                        if a*a == S:
                            count['square'] += 1
                            residual.append([w, z, eps, n, p, S, a])
                        else:
                            assert a*a < S < (a+1)**2
                            square_witnesses.append([w, z, eps, n, p, S, a])
                totals.update(count)
                families.append([w, z, eps] + [count[key] for key in
                    ['divisor_points', 'normalized_n', 'second_divisor', 'integral_p', 'p_large', 'square']])
    small_records = []
    small_pairs = []
    for n in range(104, 6*MAX_COFACTOR):
        M = gcd(n, 3)*gcd(n-1, 6)
        Q = n*(n-1)//M
        fac = factor(Q)
        F = 1
        for p, e in fac:
            F *= p**((e+2)//3)
        low = (3*n)//F + 1
        high = (10*n-1)//(3*F)
        pairs = []
        for j in range(low, high+1):
            r = j*F
            assert 3*n < r and 3*r < 10*n and r**3 % Q == 0
            delta = Q//gcd(Q, r*r)
            pairs.append([r, delta])
            small_pairs.append([n, r, delta])
        small_records.append([n, M, Q, list(fac), F, low, high, pairs])
    assert not residual
    assert all(delta <= 12 for n, r, delta in small_pairs)
    return {
        'status': 'PASS',
        'max_cofactor': MAX_COFACTOR,
        'scope': 'ell=1,j=i-3,n>=104,both k branches; squared-index equation',
        'large_case_reduction': '9w<z<100w/9; n=g*d, d|c0^3 or the stronger square-transfer divisor, g=gcd(n,3); second divisor; integral p; square reconstruction',
        'primality_of_reconstructed_p_required': False,
        'family_record_columns': ['w','z','epsilon','divisor_points','normalized_n','second_divisor','integral_p','p_large','square'],
        'statistics': {key: totals[key] for key in ['families','divisor_points','normalized_n','second_divisor','integral_p','p_large','square']},
        'largest_generated_n': largest_generated_n,
        'c0_factorizations': [[c0, list(factor(c0))] for c0 in sorted(used_c0)],
        'families': families,
        'second_divisor_candidate_columns': ['w','z','epsilon','n'],
        'second_divisor_candidates': second_candidates,
        'integral_p_candidate_columns': ['w','z','epsilon','n','p'],
        'integral_p_candidates': integral_p_candidates,
        'square_witness_columns': ['w','z','epsilon','n','p','S','floor_sqrt_S'],
        'square_witnesses': square_witnesses,
        'large_case_survivors': residual,
        'small_case_derived_index_interval': [104, 6*MAX_COFACTOR-1],
        'small_case_record_columns': ['n','M','Q','Q_factorization','F','first_multiple_index','last_multiple_index','r_delta_pairs'],
        'small_case_records': small_records,
        'small_case_pairs': small_pairs,
        'small_case_exclusion': 'Each exact delta is <=12, contradicting the established v16 delta>=13 theorem.',
        'conclusion': 'Every prime divisor p of n^2+2 has integer complementary cofactor (n^2+2)/p>=65; hence Pplus(n^2+2)<=(n^2+2)/65.',
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output-dir', type=Path, default=Path(__file__).resolve().parent)
    args = ap.parse_args()
    out = args.output_dir
    out.mkdir(parents=True, exist_ok=True)
    identities = check_identities()
    constants = check_constants()
    local = check_local_transfer()
    certificate = cofactor_certificate()
    source_sha = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    note = Path(__file__).with_name('v17_neighbor_defect.md')
    note_sha = hashlib.sha256(note.read_bytes()).hexdigest()
    certificate.update(source_sha256=source_sha, proof_note_sha256=note_sha)
    raw = (json.dumps(certificate, ensure_ascii=False, separators=(',', ':')) + '\n').encode()
    compressed = gzip.compress(raw, compresslevel=9, mtime=0)
    certificate_name = 'v17_neighbor_cofactor_certificate.json.gz'
    (out/certificate_name).write_bytes(compressed)
    summary = {
        'status': 'PASS',
        'scope': certificate['scope'],
        'adaptive_height_bounds': {'small': 'n<52*sqrt(delta)*w+1', 'complementary': 'n<983*sqrt(delta)*w^2+1'},
        'adaptive_prime_bounds': {'small': 'p<53*sqrt(delta)*n', 'complementary': 'p<32*delta^(1/4)*n^(3/2)'},
        'fixed_J_small_branch': ['n^4<2^150*J^15', 'w^2<2^40*J^5'],
        'fixed_J_complementary_branch_claimed': False,
        'polynomial_identities': identities,
        'positive_rational_margins': constants,
        'local_divisor_transfer_samples': local,
        'complete_cofactor_exclusion': {'max_cofactor': MAX_COFACTOR, 'statistics': certificate['statistics'],
            'largest_generated_n': certificate['largest_generated_n'],
            'last_square_witnesses': certificate['square_witnesses'],
            'small_case_index_count': len(certificate['small_case_records']),
            'small_case_pairs': certificate['small_case_pairs'],
            'survivors': []},
        'certificate': {'file': certificate_name, 'compressed_bytes': len(compressed),
            'compressed_sha256': hashlib.sha256(compressed).hexdigest(),
            'uncompressed_bytes': len(raw), 'uncompressed_sha256': hashlib.sha256(raw).hexdigest()},
        'source_sha256': source_sha,
        'proof_note_sha256': note_sha,
        'new_lean_execution': False,
        'new_deepseek_api_calls': 0,
        'new_complete_CAS_calls': 0,
        'external_peer_review': False,
        'original_solution_found': False,
        'unbounded_delta_or_J_solved': False,
        'verification_boundary': 'Generic statements use the written proofs; local finite samples support them only. The cofactor exclusion is complete because the finite divisor domains are proved to cover all cases.'
    }
    (out/'v17_neighbor_defect_checks.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'status': 'PASS', 'identities': len(identities), 'local_cases': local['cases'],
        'cofactor_statistics': certificate['statistics'], 'small_case_pairs': certificate['small_case_pairs'],
        'largest_generated_n': certificate['largest_generated_n'], 'certificate': summary['certificate']}, indent=2))

if __name__ == '__main__':
    main()
