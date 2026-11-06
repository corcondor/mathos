#!/usr/bin/env python3
"""Exact certificates and supporting checks for the v17 written deductions.

The 69 exception root tables exhaust a proved finite domain. Other samples
are consistency checks, not a replacement for the uniform written proof.
"""
from pathlib import Path
from math import comb, gcd, isqrt
import hashlib
import json

HERE = Path(__file__).resolve().parent
CS = (2, 3, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15)


def factors(n):
    out = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        out[n] = 1
    return out


def primes(bound):
    return [p for p in range(2, bound + 1) if factors(p) == {p: 1}]


def vp(n, p):
    assert n != 0
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def choose_vp(n, r, p):
    result = 0
    nr = n - r
    while n:
        n, r, nr = n // p, r // p, nr // p
        result += n - r - nr
    return result


def choose_vp_direct(n, r, p):
    # Independent digit-sum formula, used only as a supporting comparison.
    def digitsum(x):
        out = 0
        while x:
            out += x % p
            x //= p
        return out
    return (digitsum(r) + digitsum(n - r) - digitsum(n)) // (p - 1)


def logarithmic_exponent(m, p):
    result, q = 0, 1
    while q * p <= m:
        q *= p
        result += 1
    return result


def hensel_roots(c, p):
    roots = []
    for x in range(p):
        if (x * x - c) % p == 0:
            assert x % p
            z = -((x * x - c) // p) * pow(2 * x, -1, p) % p
            roots.append(x + p * z)
    return sorted(roots)


def r_choices(n, p=None):
    low, high = 3 * n + 1, (10 * n - 1) // 3
    if p:
        return range(((low + p - 1) // p) * p, high + 1, p)
    return sorted({low, (low + high) // 2, high})


def main():
    constants = []
    exceptions = []
    residual = []
    all_primes = set()
    full_residue_checks = 0
    for c in CS:
        selected = {29, 31, 37}
        for t in range(c + 1):
            d = (9 + t) ** 2 - 36 * c
            assert d
            f = factors(abs(d))
            selected.update(p for p in f if p >= 29)
            constants.append({'c': c, 't': t, 'D': d, 'factorization': f})
        all_primes.update(selected)
        for p in sorted(selected):
            roots = hensel_roots(c, p)
            direct = [x for x in range(p * p) if (x * x - c) % (p * p) == 0]
            assert roots == direct
            full_residue_checks += p * p
            upper = (p * p + 8) // 6
            candidates = [n for n in roots if 104 <= n <= upper and ((c + 2) * n - 3 * c) % 6 == 0]
            exceptions.append({'c': c, 'p': p, 'roots': roots, 'n_upper': upper, 'indices': candidates})
            for n in candidates:
                M = gcd(n, 3) * gcd(n - 1, 6)
                Q = n * (n - 1) // M
                ff = factors(Q)
                forced = 1
                for q, e in ff.items():
                    forced *= q ** ((e + 2) // 3)
                assert 3 * forced > 10 * n
                residual.append({'c': c, 'p': p, 'n': n, 'M': M, 'Q': Q, 'factorization': ff, 'forced_divisor': forced})
    assert len(constants) == 118 and len(exceptions) == 69 and len(all_primes) == 25
    assert [(x['c'], x['p'], x['n']) for x in residual] == [(7, 37, 157), (10, 71, 275), (10, 191, 5382), (13, 43, 149)]

    # Exact algebra and factorial checks for actual quadratic roots.
    negative_rows = []
    negative_cases = 0
    for c in CS:
        for p in primes(211):
            if p < 29:
                continue
            for n in hensel_roots(c, p):
                if n < 104 or p * p <= 6 * n - 9 or ((c + 2) * n - 3 * c) % 6:
                    continue
                A, m = n * (n - 1) * (n - 2) // 6, 6 * n - 9
                a, N = ((c + 2) * n - 3 * c) // 6, n * n - c
                assert 6 * (A - a) == (n - 3) * N
                e = vp(N, p)
                assert vp(A - a, p) == e
                F = m // p - (m - c - 1) // p
                for r in r_choices(n):
                    G = r // p - a // p - (r - a - 1) // p
                    bl, ol = choose_vp(n * n, m, p), choose_vp(A, r, p)
                    assert F in (0, 1) and G in (0, 1)
                    assert bl == e - F and ol == e - G
                    assert bl == choose_vp_direct(n * n, m, p)
                    assert ol == choose_vp_direct(A, r, p)
                    negative_cases += 1
                    negative_rows.append({'c': c, 'p': p, 'n': n, 'r': r, 'e': e, 'F': F, 'G': G})
    actual_binomials = []
    for row in sorted(negative_rows, key=lambda x: (x['n'], x['r'], x['p']))[:16]:
        n, p, r = row['n'], row['p'], row['r']
        A, m = n * (n - 1) * (n - 2) // 6, 6 * n - 9
        observed = [vp(comb(A, r), p), vp(comb(n * n, m), p)]
        assert observed == [row['e'] - row['G'], row['e'] - row['F']]
        actual_binomials.append({**row, 'actual_binomial_valuations': observed})

    # Main-index prime factors: every allowed r multiple in a bounded sample.
    first_index_cases = [0, 0]
    first_index_exceptions = []
    for p in primes(211):
        if p < 29:
            continue
        for w in range(1, (p - 1) // 6 + 1):
            for shift in (0, 1):
                n = p * w + shift
                if n < 104:
                    continue
                A, m = n * (n - 1) * (n - 2) // 6, 6 * n - 9
                assert p * p > m
                assert choose_vp(n * n, m, p) == 2
                for r in r_choices(n, p):
                    outer = choose_vp(A, r, p)
                    assert outer == choose_vp_direct(A, r, p)
                    first_index_cases[shift] += 1
                    if shift == 1:
                        j = p * w % 6 or 6
                        b = (j * p - w) // 6
                        assert (j * p - w) % 6 == 0 and 0 < b < p
                        assert vp(A // p - b, p) == 1
                        assert outer in (0, 1)
                    elif outer >= 2:
                        assert n % 3 == 2 and 6 * w < p < 9 * w
                        assert (3 * w * w + 2) % p == 0
                        first_index_exceptions.append({'p': p, 'w': w, 'n': n, 'r': r, 'outer_valuation': outer})

    # General congruence lemmas and the positive-neighbor alternating identity.
    congruence_cases = 0
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 29):
        for e in range(1, 7):
            for m in sorted({1, 3, p - 2, p + 2, 2 * p - 1, p * p - 2}):
                if not (1 <= m <= 299) or m % 2 == 0:
                    continue
                J = logarithmic_exponent(m, p)
                if e <= J:
                    continue
                q = p ** e
                for w in (1, 2):
                    U, modulus = w * q, p ** (e - J)
                    assert U > m
                    for j in sorted({1, (m + 1) // 2, m}):
                        assert comb(U, j) % modulus == 0
                    assert comb(U - 1, m) % modulus == modulus - 1
                    b = m // 3
                    assert comb(U + b, m) % modulus == 0
                    congruence_cases += 1

    # Constants behind the product bounds are checked exactly at their endpoint.
    assert 208000 < 225 * 927
    assert 35 * 104 < 36 * 103
    assert 6 * 104 - 9 > 5 * 104
    assert 41 * (6 * 104 - 9) > 225 * 104
    m_values = [3, 6, 1, 6, 3, 2]
    for n in range(104, 110):
        M = gcd(n, 3) * gcd(n - 1, 6)
        assert M == m_values[n % 6]
        assert M * (n - 2) % 6 == 0

    report = {
        'status': 'PASS',
        'scope': 'ell=1, j=i-3, both k branches, original squared-index equation',
        'new_lean_execution': False,
        'new_deepseek_api_calls': 0,
        'original_solutions_found': [],
        'written_proof_is_universal_basis': True,
        'complete_exception_domain': {
            'constants_count': len(constants), 'constants': constants,
            'root_table_count': len(exceptions), 'distinct_primes': sorted(all_primes),
            'full_residue_checks': full_residue_checks, 'tables': exceptions,
            'residual_indices': residual, 'survivors': [],
            'root_methods': ['unique Hensel lift', 'all residues modulo p^2'],
        },
        'supporting_checks': {
            'negative_neighbor_valuation_cases': negative_cases,
            'negative_neighbor_inputs': len(negative_rows) // 3,
            'actual_binomial_pairs': len(actual_binomials),
            'actual_binomial_records': actual_binomials,
            'main_index_n_cases': first_index_cases[0],
            'main_index_n_minus_one_cases': first_index_cases[1],
            'main_index_possible_valuation_exceptions': first_index_exceptions,
            'binomial_congruence_lemma_cases': congruence_cases,
            'samples_are_original_solutions': False,
            'supporting_samples_are_not_a_completeness_claim': True,
        },
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'proof_note_sha256': hashlib.sha256((HERE / 'v17_quadratic_prime_powers.md').read_bytes()).hexdigest(),
    }
    target = HERE / 'v17_quadratic_prime_powers_checks.json'
    target.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({
        'status': report['status'],
        'root_tables': len(exceptions), 'complete_residual_indices': len(residual),
        'negative_valuation_cases': negative_cases,
        'main_index_cases': first_index_cases,
        'congruence_cases': congruence_cases,
        'report': str(target),
    }))


if __name__ == '__main__':
    main()
