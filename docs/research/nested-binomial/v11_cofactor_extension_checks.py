#!/usr/bin/env python3
"""Exact finite certificates for every cofactor w/gcd(w,192) <= 13.

The unbounded reduction is proved in v11_cofactor_extension.md.  Generation
uses exact binomial coefficients, a sieve, factorial valuations, and trial
factorization.  Verification independently reconstructs the parameter
domain, checks complete prime factorizations, and recomputes the squared-
index valuations by base-p carries.  It never builds the original large
binomial coefficients or scans an interval of their arguments.
"""

from collections import Counter
from math import comb, factorial, gcd, isqrt, prod
from pathlib import Path
import argparse
import base64
import hashlib
import json
import zlib

BASE = Path(__file__).resolve().parent
CERT_PATH = BASE / 'v11_cofactor_extension_certificates.json'
REPORT_PATH = BASE / 'v11_cofactor_extension_verification.json'
NOTE_PATH = BASE / 'v11_cofactor_extension.md'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sieve(bound):
    flags = bytearray([1]) * (bound + 1)
    flags[:2] = b'\0\0'
    for p in range(2, isqrt(bound) + 1):
        if flags[p]:
            for n in range(p * p, bound + 1, p):
                flags[n] = 0
    return [p for p in range(2, bound + 1) if flags[p]]


def trial_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def vp(n, p):
    assert n > 0
    e = 0
    while n % p == 0:
        e += 1
        n //= p
    return e


def factorial_valuation(n, p):
    result = 0
    while n:
        n //= p
        result += n
    return result


def binomial_valuation(n, k, p):
    return (factorial_valuation(n, p) - factorial_valuation(k, p)
            - factorial_valuation(n - k, p))


def carry_valuation(n, k, p):
    """Independent Kummer calculation: carries in k+(n-k), base p."""
    left, right, carry, total = k, n - k, 0, 0
    while left or right or carry:
        digit_sum = left % p + right % p + carry
        carry = int(digit_sum >= p)
        total += carry
        left //= p
        right //= p
    return total


def factor_with_primes(n, primes):
    factors = []
    for p in primes:
        if p * p > n:
            break
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            factors.append([p, e])
    if n > 1:
        factors.append([n, 1])
    return factors


def generated_domain():
    cofactors = [w for w in range(1, 2497) if w // gcd(w, 192) <= 13]
    prime_list = sieve(14976)
    records, coefficient_records = [], []
    for w in cofactors:
        bignum = comb(6 * w, 2 * w)
        D = bignum // gcd(bignum, 6)
        coefficient_records.append({
            'w': w, 'c192_w': w // gcd(w, 192),
            'D_w_factorization': factor_with_primes(D, prime_list),
        })
        for p in prime_list:
            if p > 6 * w:
                break
            if w % p == 0:
                continue
            b = vp(D, p)
            exponents = {b + 2 * t + int(p == 3) for t in range(b)}
            a, q = 1, p
            while q <= 4 * w:
                exponents.add(a)
                a, q = a + 1, q * p
            for a in sorted(exponents):
                q = p ** a
                n = w * q + 2
                if n < 104:
                    continue
                records.append({
                    'w': w, 'p': p, 'a': a, 'n': n, 'b': b,
                    'reduction_case': ('small_power' if q <= 4 * w
                                       else 'possible_local_defect'),
                })
    return cofactors, coefficient_records, records


def generate():
    cofactors, coefficients, domain = generated_domain()
    primes = sieve(isqrt(max(row['n'] for row in domain)))
    certs = []
    for n in sorted({row['n'] for row in domain}):
        a_factors = {}
        for value in (n, n - 1, n - 2):
            for p, e in factor_with_primes(value, primes):
                a_factors[p] = a_factors.get(p, 0) + e
        a_factors[2] -= 1
        a_factors[3] = a_factors.get(3, 0) - 1
        a_factors = {p: e for p, e in a_factors.items() if e}
        valuations, forced, defect, divisor = [], [], 1, 1
        for p, a0 in sorted(a_factors.items()):
            x = binomial_valuation(n * n, 6 * n - 9, p)
            e = x // 2 if x % 2 == 0 and 3 * x < 2 * a0 else (a0 + 2) // 3
            valuations.append([p, x])
            forced.append([p, e])
            defect *= p ** max(0, a0 - 3 * e)
            divisor *= p ** e
        first = (3 * n // divisor + 1) * divisor
        if defect <= 13:
            exclusion = 'recovered_defect_at_most_13'
        elif 3 * first >= 10 * n:
            exclusion = 'no_forced_multiple_in_broad_gap'
        else:
            assert n == 6860 and divisor == 1330 and first == 21280
            assert n >= 1024 and 4 ** 8 * n > 11 ** 8
            assert 32 * first >= 99 * n
            exclusion = 'logarithmic_gap_with_log_n_greater_than_8'
        certs.append({
            'n': n,
            'A_factorization': [[p, e] for p, e in sorted(a_factors.items())],
            'X_valuations': valuations,
            'forced_r_exponents': forced,
            'recovered_defect': defect,
            'forced_r_divisor_decimal': str(divisor),
            'first_multiple_above_3n_decimal': str(first),
            'exclusion': exclusion,
        })
    output = {
        'schema': 'nested-binomial-v11-cofactor-extension-v1',
        'equation': 'C(C(i,j),C(k,ell)) = C(i^2,j^2) + C(k^2,ell^2)',
        'scope': 'ell=1, j=i-3, i=w*p^a+2, w/gcd(w,192)<=13, p prime, a>=1',
        'cofactors': cofactors,
        'cofactor_coefficients': coefficients,
        'complete_parameter_domain': domain,
        'index_certificates': certs,
        'whole_original_equation_solved': False,
    }
    raw = json.dumps(output, ensure_ascii=False, separators=(',', ':')).encode('utf-8')
    compressed = zlib.compress(raw, 9)
    wrapper = {
        'schema': 'nested-binomial-v11-cofactor-extension-packed-v1',
        'encoding': 'base64(zlib(JSON UTF-8))',
        'uncompressed_sha256': hashlib.sha256(raw).hexdigest(),
        'compressed_sha256': hashlib.sha256(compressed).hexdigest(),
        'uncompressed_bytes': len(raw),
        'compressed_bytes': len(compressed),
        'complete_parameter_records': len(domain),
        'distinct_indices': len(certs),
        'payload_base64': base64.b64encode(compressed).decode('ascii'),
    }
    CERT_PATH.write_text(json.dumps(wrapper, ensure_ascii=False, indent=2) + '\n')
    return output


def read_complete_certificate():
    wrapper = json.loads(CERT_PATH.read_text())
    assert wrapper['schema'] == 'nested-binomial-v11-cofactor-extension-packed-v1'
    assert wrapper['encoding'] == 'base64(zlib(JSON UTF-8))'
    packed = base64.b64decode(wrapper['payload_base64'], validate=True)
    assert len(packed) == wrapper['compressed_bytes']
    assert hashlib.sha256(packed).hexdigest() == wrapper['compressed_sha256']
    raw = zlib.decompress(packed)
    assert len(raw) == wrapper['uncompressed_bytes']
    assert hashlib.sha256(raw).hexdigest() == wrapper['uncompressed_sha256']
    data = json.loads(raw)
    assert len(data['complete_parameter_domain']) == wrapper['complete_parameter_records']
    assert len(data['index_certificates']) == wrapper['distinct_indices']
    return data, wrapper


def independently_reconstructed_domain():
    # Reconstruct w from c192=w/gcd(w,192) and the divisor gcd(w,192).
    cofactors = sorted({g * c for c in range(1, 14) for g in (1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 192)
                        if gcd(g * c, 192) == g})
    rows, coefficient_records = [], []
    for w in cofactors:
        D_exact = factorial(6 * w) // (factorial(2 * w) * factorial(4 * w))
        D_exact //= gcd(D_exact, 6)
        coeff_factors = []
        for p in range(2, 6 * w + 1):
            if not trial_prime(p):
                continue
            factorial_b = binomial_valuation(6 * w, 2 * w, p)
            b = max(0, factorial_b - int(p in (2, 3)))
            if b:
                coeff_factors.append([p, b])
            if w % p == 0:
                continue
            # Check every exponent up to the proved final possible defect,
            # also retaining all q<=4w.  Do not use the generator's progression.
            a, q = 1, p
            while q <= 4 * w or a <= 3 * b - 2 + int(p == 3):
                n = w * q + 2
                a0 = a - int(p == 3)
                x = a0 - b
                possible_defect = b > 0 and x >= 0 and x % 2 == 0 and 3 * x < 2 * a0
                if n >= 104 and (q <= 4 * w or possible_defect):
                    rows.append({
                        'w': w, 'p': p, 'a': a, 'n': n, 'b': b,
                        'reduction_case': ('small_power' if q <= 4 * w
                                           else 'possible_local_defect'),
                    })
                a, q = a + 1, q * p
        assert prod(p ** b for p, b in coeff_factors) == D_exact
        coefficient_records.append({
            'w': w, 'c192_w': w // gcd(w, 192),
            'D_w_factorization': coeff_factors,
        })
    return cofactors, coefficient_records, rows


def verify(write_report=True):
    data, wrapper = read_complete_certificate()
    assert data['schema'] == 'nested-binomial-v11-cofactor-extension-v1'
    cofactors, coefficients, domain = independently_reconstructed_domain()
    assert data['cofactors'] == cofactors
    assert data['cofactor_coefficients'] == coefficients
    assert data['complete_parameter_domain'] == domain
    records = data['index_certificates']
    assert [row['n'] for row in records] == sorted({row['n'] for row in domain})
    by_n, prime_checks, carry_checks = {}, 0, 0
    for row in records:
        n = row['n']
        assert n >= 104
        factors = row['A_factorization']
        assert [p for p, _ in factors] == sorted({p for p, _ in factors})
        for p, a0 in factors:
            assert isinstance(p, int) and isinstance(a0, int) and a0 > 0
            assert trial_prime(p)
            prime_checks += 1
        assert prod(p ** a0 for p, a0 in factors) == n * (n - 1) * (n - 2) // 6
        valuations, forced, B, R = [], [], 1, 1
        for p, a0 in factors:
            x = carry_valuation(n * n, 6 * n - 9, p)
            carry_checks += 1
            # Necessary alternatives from A | k(X+k^2): either 3e>=a0,
            # or 2e=x.  Enumerate this finite local alternative directly.
            permissible_e = [e for e in range(a0 + 1) if 3 * e >= a0 or 2 * e == x]
            e = min(permissible_e)
            valuations.append([p, x])
            forced.append([p, e])
            forced_A_exponent = min(a0, 3 * e)
            assert forced_A_exponent >= min(a0, x)
            B *= p ** forced_A_exponent
            R *= p ** e
        A = n * (n - 1) * (n - 2) // 6
        assert A % B == 0
        Sstar = A // B
        assert (n - 2) // gcd(n - 2, 192) % Sstar == 0
        assert row['X_valuations'] == valuations
        assert row['forced_r_exponents'] == forced
        assert row['recovered_defect'] == Sstar
        assert row['forced_r_divisor_decimal'] == str(R)
        first = (3 * n // R + 1) * R
        assert row['first_multiple_above_3n_decimal'] == str(first)
        assert first > 3 * n and first - R <= 3 * n
        exclusion = row['exclusion']
        if exclusion == 'recovered_defect_at_most_13':
            assert Sstar <= 13
        elif exclusion == 'no_forced_multiple_in_broad_gap':
            assert Sstar >= 14 and 3 * first >= 10 * n
        elif exclusion == 'logarithmic_gap_with_log_n_greater_than_8':
            assert (n, R, first) == (6860, 1330, 21280)
            assert n >= 1024
            # e<11/4, hence n>(11/4)^8 implies log(n)>8.
            assert n * 4 ** 8 > 11 ** 8
            # r < 3n+3n/(4log n) < (99/32)n.
            assert 32 * first >= 99 * n
        else:
            raise AssertionError(exclusion)
        by_n[n] = row
    assert len(cofactors) == 94
    assert len(domain) == 28316
    assert len(records) == 28133
    parameter_counts = Counter(by_n[row['n']]['exclusion'] for row in domain)
    unique_counts = Counter(row['exclusion'] for row in records)
    assert parameter_counts == {
        'recovered_defect_at_most_13': 11749,
        'no_forced_multiple_in_broad_gap': 16566,
        'logarithmic_gap_with_log_n_greater_than_8': 1,
    }
    assert max(row['n'] for row in domain) == 7844717829890
    report = {
        'status': 'PASS',
        'scope': data['scope'],
        'cofactors': cofactors,
        'cofactor_count': len(cofactors),
        'new_cofactors_beyond_v10_c6_le_12': [w for w in cofactors if w // gcd(w, 6) > 12],
        'complete_parameter_records': len(domain),
        'distinct_indices': len(records),
        'largest_index': max(row['n'] for row in domain),
        'largest_index_parameter': max(domain, key=lambda row: row['n']),
        'parameter_exclusion_counts': dict(sorted(parameter_counts.items())),
        'distinct_index_exclusion_counts': dict(sorted(unique_counts.items())),
        'prime_factor_checks': prime_checks,
        'independent_digit_carry_valuations': carry_checks,
        'parameters_by_cofactor': dict(sorted(Counter(row['w'] for row in domain).items())),
        'independent_parameter_domain_reconstruction': 'PASS',
        'all_factorizations_complete_and_primes_deterministic': True,
        'all_integer_arithmetic_exact': True,
        'arbitrary_search_cutoff': False,
        'original_binomial_coefficients_constructed': False,
        'original_i_interval_scanned': False,
        'r_interval_scanned': False,
        'new_Lean_formalization_by_this_script': False,
        'whole_original_equation_solved': False,
        'checker_sha256': digest(Path(__file__)),
        'certificate_sha256': digest(CERT_PATH),
        'certificate_uncompressed_bytes': wrapper['uncompressed_bytes'],
        'certificate_compressed_bytes': wrapper['compressed_bytes'],
        'certificate_uncompressed_sha256': wrapper['uncompressed_sha256'],
        'certificate_compressed_sha256': wrapper['compressed_sha256'],
        'full_lossless_certificate': True,
        'effective_defect_exclusion_dependency': 'v11_effective_defect_cf.md (H=13) and v9 (H<=12)',
        'proof_note_sha256': digest(NOTE_PATH) if NOTE_PATH.exists() else None,
    }
    if write_report:
        REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('action', nargs='?', default='verify', choices=['generate', 'verify'])
    args = parser.parse_args()
    if args.action == 'generate':
        generate()
    result = verify()
    print(json.dumps(result, ensure_ascii=False, indent=2))
