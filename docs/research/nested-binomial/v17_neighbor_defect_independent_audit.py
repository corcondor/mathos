#!/usr/bin/env python3
"""Independent reconstruction of the complete v17 cofactor certificate.

Does not import or execute the producer. Divisors are found by trial divisor
pairs of c0^3, not by its prime-exponent Cartesian product. Small n cases are
checked by every r in the proved interval, not by a forced-divisor list.
"""
from pathlib import Path
from functools import lru_cache
from math import gcd
from fractions import Fraction
import argparse
import gzip
import hashlib
import json


def floor_root(n):
    lo, hi = 0, 1 << ((n.bit_length() + 1) // 2)
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid * mid <= n:
            lo = mid
        else:
            hi = mid
    return hi if hi * hi <= n else lo


@lru_cache(None)
def divisors_by_pairs(n):
    found = []
    for d in range(1, floor_root(n) + 1):
        q, remainder = divmod(n, d)
        if remainder == 0:
            found.append(d)
            if q != d:
                found.append(q)
    return tuple(sorted(found))


def validate_factorization(n, factored):
    product = 1
    seen = set()
    for p, e in factored:
        assert p not in seen and e >= 1 and p >= 2
        seen.add(p)
        assert all(p % d for d in range(2, floor_root(p) + 1))
        product *= p ** e
    assert product == n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--input-dir', type=Path, default=Path(__file__).resolve().parent)
    ap.add_argument('--output', type=Path, default=Path(__file__).with_suffix('.json'))
    args = ap.parse_args()
    d = args.input_dir
    compressed = (d / 'v17_neighbor_cofactor_certificate.json.gz').read_bytes()
    raw = gzip.decompress(compressed)
    cert = json.loads(raw)
    summary = json.loads((d / 'v17_neighbor_defect_checks.json').read_text())
    assert cert['status'] == summary['status'] == 'PASS'
    assert cert['max_cofactor'] == 64
    source = d / 'v17_neighbor_defect_checks.py'
    note = d / 'v17_neighbor_defect.md'
    for key, path in [('source_sha256', source), ('proof_note_sha256', note)]:
        assert cert[key] == summary[key] == hashlib.sha256(path.read_bytes()).hexdigest()
    assert summary['certificate']['compressed_sha256'] == hashlib.sha256(compressed).hexdigest()
    assert summary['certificate']['uncompressed_sha256'] == hashlib.sha256(raw).hexdigest()

    names = ('families', 'divisor_points', 'normalized_n', 'second_divisor', 'integral_p', 'p_large', 'square')
    statistics = dict.fromkeys(names, 0)
    families = []
    second, integral, nonsquares, squares = [], [], [], []
    largest = 0
    used_c0 = set()
    for epsilon in (1, 0):
        for w in range(64, 0, -1):
            for z in range((100 * w) // 9, 9 * w, -1):
                if 9 * z >= 100 * w:
                    continue
                c0 = 2 * z - (8 + epsilon) * w
                c1 = 3 * z - (2 + epsilon) * w
                used_c0.add(c0)
                cube = c0 ** 3
                ds = divisors_by_pairs(cube)
                if epsilon == 0:
                    ds = tuple(x for x in ds if cube % (x * x) == 0)
                row = dict.fromkeys(names, 0)
                row['families'] = 1
                for g in (3, 1):
                    for div in reversed(ds):
                        n = g * div
                        largest = max(largest, n)
                        row['divisor_points'] += 1
                        if n < 104 or (3 if n % 3 == 0 else 1) != g:
                            continue
                        row['normalized_n'] += 1
                        q1 = (n - 1) // gcd(n - 1, 6)
                        required = q1 if epsilon else q1 * q1
                        if gcd(required, c1 ** 3) != required:
                            continue
                        row['second_divisor'] += 1
                        second.append([w, z, epsilon, n])
                        p, rem = divmod(n * n + 2, w)
                        if rem:
                            continue
                        row['integral_p'] += 1
                        integral.append([w, z, epsilon, n, p])
                        if p < 6 * n - 8:
                            continue
                        row['p_large'] += 1
                        S = z * p + 6 * n - 8
                        a = floor_root(S)
                        if a * a == S:
                            squares.append([w, z, epsilon, n, p, S, a])
                            row['square'] += 1
                        else:
                            assert a * a < S < (a + 1) * (a + 1)
                            nonsquares.append([w, z, epsilon, n, p, S, a])
                for key in names:
                    statistics[key] += row[key]
                families.append([w, z, epsilon] + [row[key] for key in names[1:]])

    assert statistics == cert['statistics'] == summary['complete_cofactor_exclusion']['statistics']
    assert sorted(families) == sorted(cert['families'])
    assert sorted(second) == sorted(cert['second_divisor_candidates'])
    assert sorted(integral) == sorted(cert['integral_p_candidates'])
    assert sorted(nonsquares) == sorted(cert['square_witnesses'])
    assert squares == cert['large_case_survivors'] == []
    assert largest == cert['largest_generated_n']
    assert sorted(used_c0) == [record[0] for record in cert['c0_factorizations']]
    for c0, factored in cert['c0_factorizations']:
        validate_factorization(c0, factored)

    small_pairs = []
    records = {row[0]: row for row in cert['small_case_records']}
    checked_r = 0
    assert sorted(records) == list(range(104, 384))
    for n in range(104, 384):
        M = gcd(n, 3) * gcd(n - 1, 6)
        Q = n * (n - 1) // M
        local = []
        for r in range(3 * n + 1, (10 * n + 2) // 3):
            assert 3 * n < r and 3 * r < 10 * n
            checked_r += 1
            if pow(r, 3, Q):
                continue
            delta = Q // gcd(Q, r * r)
            assert delta <= 12
            local.append([r, delta])
            small_pairs.append([n, r, delta])
        saved = records[n]
        assert saved[1:3] == [M, Q] and saved[7] == local
        validate_factorization(Q, saved[3])
        forced = 1
        for p, e in saved[3]:
            forced *= p ** ((e + 2) // 3)
        assert forced == saved[4]
        assert saved[5] == 3 * n // forced + 1
        assert saved[6] == (10 * n - 1) // (3 * forced)
    assert small_pairs == cert['small_case_pairs'] == [[169, 546, 1], [243, 792, 1], [250, 830, 5], [361, 1140, 1]]

    # Recompute all displayed constant margins without the producer functions.
    F = Fraction
    margins = [F(52**2) - F(24064, 9),
               F(983**2) - 6 * F(10829, 27)**2,
               F(32**2) - 983 * F(10201, 9900),
               F(1024**3) - F(224, 9)**3 * F(8000, 33)**2,
               F(2**20) - F(224, 9) * 2**15,
               F(104**2 - 53*104 - 104), F(104**2 - 3*104 - 70)]
    assert all(x > 0 for x in margins)

    result = {
        'status': 'PASS',
        'producer_imported_or_executed': False,
        'divisor_method': 'Complete pairs d, N/d for 1<=d<=floor(sqrt(N)), N=c0^3; square-transfer filter d^2|N',
        'small_index_method': 'Every integer r in the proved interval for each 104<=n<=383',
        'square_method': 'Integer binary search',
        'statistics': statistics,
        'all_family_records_match': True,
        'all_second_divisor_candidates_match': True,
        'all_integral_p_candidates_match': True,
        'all_square_witnesses_match': True,
        'largest_generated_n': largest,
        'factorizations_checked': len(used_c0),
        'small_indices': 280,
        'small_r_values_checked': checked_r,
        'small_pairs': small_pairs,
        'last_square_witnesses': sorted(nonsquares),
        'constant_margins': [str(x) for x in margins],
        'survivors': [],
        'certificate_sha256': hashlib.sha256(compressed).hexdigest(),
        'uncompressed_certificate_sha256': hashlib.sha256(raw).hexdigest(),
        'producer_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
        'proof_note_sha256': hashlib.sha256(note.read_bytes()).hexdigest(),
        'auditor_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'new_lean_execution': False,
        'external_peer_review': False,
        'verification_boundary': 'Exact independent reproduction of the complete finite cofactor certificate; depends on the separately reviewed written reductions and inherited branch theorems.',
    }
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({key: result[key] for key in ('status', 'statistics', 'small_pairs', 'small_r_values_checked', 'largest_generated_n')}))


if __name__ == '__main__':
    main()
