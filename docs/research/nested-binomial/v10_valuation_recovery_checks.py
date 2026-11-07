#!/usr/bin/env python3
"""Exact structural checks for the written v10 valuation-recovery proof.

These are checks of identities and universal-lemma examples, not a bounded
search asserted to solve the original four-variable equation. Python's
standard library suffices. No floating-point arithmetic is used.
"""

from functools import lru_cache
from hashlib import sha256
from itertools import product
from math import comb, gcd, prod
from pathlib import Path
import json


ROOT = Path(__file__).resolve().parent


def vp(n, p):
    assert n > 0 and p >= 2
    out = 0
    while n % p == 0:
        out += 1
        n //= p
    return out


@lru_cache(maxsize=None)
def factor(n):
    result = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            a = 0
            while n % p == 0:
                a += 1
                n //= p
            result.append((p, a))
        p += 1
    if n > 1:
        result.append((n, 1))
    return tuple(result)


def prime_list(bound):
    return [p for p in range(2, bound + 1) if factor(p) == ((p, 1),)]


def fact_val(n, p):
    result = 0
    while n:
        n //= p
        result += n
    return result


def binomial_val(n, k, p):
    return fact_val(n, p) - fact_val(k, p) - fact_val(n - k, p)


def defect_exponent(alpha, x):
    return max(alpha - 3 * (x // 2), 0) if x % 2 == 0 else 0


def roots_by_lifting(target, p, d):
    """All roots at every precision, including the non-simple p=2 case."""
    modulus = p
    roots = [z for z in range(p) if (z * z - target) % p == 0]
    for _ in range(1, d):
        next_modulus = modulus * p
        roots = [
            z + digit * modulus
            for z in roots
            for digit in range(p)
            if ((z + digit * modulus) ** 2 - target) % next_modulus == 0
        ]
        modulus = next_modulus
    assert len(roots) == len(set(roots))
    assert all(0 <= z < p**d and (z*z-target) % (p**d) == 0 for z in roots)
    return sorted(roots)


def unit_square_test(target, p, d):
    assert target % p != 0
    if p == 2:
        return target % (2 ** min(d, 3)) == 1
    return pow(target, (p - 1) // 2, p) == 1


def check_local():
    counts = {
        'tested_exact_congruences': 0,
        'satisfying_congruences': 0,
        'low_cube_valuation_cases': 0,
        'odd_X_valuation_cases': 0,
        'critical_low_branch': 0,
        'critical_high_branch': 0,
        'unit_square_tests': 0,
        'unit_nonsquare_tests': 0,
    }
    primes = [2, 3, 5, 7, 11, 17]
    for p in primes:
        units = [z for z in range(1, min(2*p, 24) + 1) if z % p]
        r_units = [z for z in range(1, min(p+1, 10) + 1) if z % p]
        for alpha in range(1, 9):
            modulus = p**alpha
            for x in range(0, 2*alpha + 3):
                d = defect_exponent(alpha, x)
                for xu in units:
                    X = p**x * xu
                    if d:
                        roots = roots_by_lifting(-xu, p, d)
                        assert bool(roots) == unit_square_test(-xu, p, d)
                        assert len(roots) <= (4 if p == 2 else 2)
                        counts['unit_square_tests' if roots else 'unit_nonsquare_tests'] += 1
                    else:
                        roots = []
                    for e in range(0, alpha + 3):
                        for ru in r_units:
                            r = p**e * ru
                            counts['tested_exact_congruences'] += 1
                            if r * (X + r*r) % modulus:
                                continue
                            counts['satisfying_congruences'] += 1
                            assert alpha - d <= 3*e
                            if x % 2:
                                counts['odd_X_valuation_cases'] += 1
                                assert e >= max((alpha+2)//3, alpha-x)
                            if 3*e < alpha:
                                counts['low_cube_valuation_cases'] += 1
                                assert x == 2*e
                                assert (ru*ru+xu) % (p**(alpha-3*e)) == 0
                            if d:
                                t = x//2
                                if e == t:
                                    counts['critical_low_branch'] += 1
                                    assert (ru*ru+xu) % (p**d) == 0
                                else:
                                    counts['critical_high_branch'] += 1
                                    assert e >= t+d
                                if not roots:
                                    assert e >= alpha-x
                                    assert 3*e >= alpha
    return counts


def merge_crt(a, m, b, n):
    assert gcd(m, n) == 1
    return (a + m * (((b-a)*pow(m, -1, n)) % n)) % (m*n)


def verify_mixed(A, X, r):
    assert A > 0 and X > 0 and r > 0
    assert r*(X+r*r) % A == 0
    data = []
    E = 1
    E_sq = 1
    F = 1
    for p, alpha in factor(A):
        x = vp(X, p)
        d = defect_exponent(alpha, x)
        E *= p**d
        F *= p**((alpha-d+2)//3)
        if d:
            target = -X//(p**x)
            square = bool(roots_by_lifting(target, p, d))
            assert square == unit_square_test(target, p, d)
            if square:
                E_sq *= p**d
            data.append((p, alpha, x, d))
    B = A//E
    B_sq = A//E_sq
    G = gcd(A, X)
    S = A//G
    assert A % B == B % G == A % B_sq == B_sq % B == 0
    assert r**3 % B == r**3 % B_sq == 0
    assert S % E == E % E_sq == 0
    assert r % F == 0 and F**3 >= B
    u = r//F
    assert A//gcd(A, r**3) == E//gcd(E, u)
    residues, modulus = [0], 1
    bound = 1
    for p, alpha, x, d in data:
        t = x//2
        mod = p**d
        lam = (X//(p**(2*t))) * pow(F//(p**t), -2, mod) % mod
        roots = roots_by_lifting(-lam, p, d)
        local = [0] + roots
        assert u % mod in local
        assert gcd(u, mod) in (1, mod)
        residues = [merge_crt(a, modulus, b, mod) for a in residues for b in local]
        modulus *= mod
        bound *= 5 if p == 2 else 3
    assert modulus == E and len(set(residues)) == len(residues)
    assert len(residues) <= bound
    assert u % E in residues
    return {'E': E, 'E_sq': E_sq, 'S': S, 'classes': len(residues), 'critical_primes': len(data)}


def check_mixed():
    counts = {'generic_binomial_rows': 0, 'constructed_mixed_congruences': 0,
              'multiple_critical_primes': 0, 'strict_parity_recoveries': 0,
              'strict_square_recoveries': 0, 'maximum_CRT_classes': 0}
    for A in range(4, 121):
        for k in range(1, A):
            X = comb(A, k)-k*k
            if X <= 0:
                continue
            r = min(k, A-k)
            result = verify_mixed(A, X, r)
            counts['generic_binomial_rows'] += 1
            counts['multiple_critical_primes'] += result['critical_primes'] > 1
            counts['strict_parity_recoveries'] += result['E'] < result['S']
            counts['strict_square_recoveries'] += result['E_sq'] < result['E']
            counts['maximum_CRT_classes'] = max(counts['maximum_CRT_classes'], result['classes'])
    for a, b, c, d in product([0, 1, 3, 6], [0, 1, 2, 4], [0, 1, 3], [0, 1]):
        A = 2**a * 3**b * 5**c * 7**d
        if A == 1:
            continue
        values = {1, 2, 3, 4, 5, 6, 7, 8, 11, 16, 25, 27, 49, 64, 125, A-1, A, A+1}
        for r in sorted(values):
            modulus = A//gcd(A, r)
            for lift in [1, 2]:
                X = (-r*r) % modulus + lift*modulus
                result = verify_mixed(A, X, r)
                counts['constructed_mixed_congruences'] += 1
                counts['multiple_critical_primes'] += result['critical_primes'] > 1
                counts['strict_parity_recoveries'] += result['E'] < result['S']
                counts['strict_square_recoveries'] += result['E_sq'] < result['E']
                counts['maximum_CRT_classes'] = max(counts['maximum_CRT_classes'], result['classes'])
    return counts


def check_fixed_cofactors():
    counts = {'exact_binomial_valuation_examples': 0, 'nonzero_recovered_prime_defects': 0,
              'quartic_bound_examples': 0, 'normalization_examples': 0}
    candidates = []
    for w in range(1, 73):
        choose = comb(6*w, 2*w)
        D = choose//gcd(choose, 6)
        cw = w//gcd(w, 6)
        primes = sorted(set(prime_list(6*w) + [439]))
        for p in primes:
            if w % p == 0:
                continue
            b = vp(D, p)
            for a in range(1, max(5, 3*b+5)):
                q = p**a
                if q <= 4*w:
                    continue
                n = w*q+2
                alpha = binomial_val(n, 3, p)
                x = binomial_val(n*n, 6*n-9, p)
                assert alpha == a-(p == 3)
                assert max(alpha-x, 0) == b
                ep = defect_exponent(alpha, x)
                if b:
                    assert x == alpha-b
                predicted = ((3*b-alpha)//2 if b and alpha in range(b, 3*b, 2) else 0)
                assert ep == predicted
                counts['exact_binomial_valuation_examples'] += 1
                if ep:
                    counts['nonzero_recovered_prime_defects'] += 1
                    assert p**b <= (3*w if p == 2 else 2*w if p == 3 else 6*w)
                    counts['quartic_bound_examples'] += 1
                    assert 25*(n-2) <= 216*w**4
                    assert n < 16*w**4
                    if cw <= 12:
                        candidates.append([w, p, a, b, ep, n])
    for w in range(1, 201):
        for p in [2, 3, 5, 7, 11, 13, 17]:
            w0 = w//(p**vp(w, p))
            assert w0//gcd(w0, 6) <= w//gcd(w, 6)
            counts['normalization_examples'] += 1
    ws = [w for w in range(1, 73) if w//gcd(w, 6) <= 12]
    assert ws == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16,
                  18, 20, 21, 22, 24, 27, 30, 33, 36, 42, 48, 54, 60, 66, 72]
    return counts, ws, candidates


def general_height_constants():
    # Large-q critical case: 25*(16*w^4-(216*w^4/25+2))
    # = 184*(w^4-1)+134, positive for all w>=1.
    assert 25*16-216 == 184 and 184-50 == 134 > 0
    # Small-q case, putting w^2=1+t:
    # 16*w^4-4*w^2-2 = 16*t^2+28*t+10.
    assert 32-4 == 28 and 16-4-2 == 10
    assert all(z > 0 for z in [16, 28, 10])
    # e>1+1+1/2>2 gives log(2)<1; the old e<11/4
    # implies e^2<8, since 121<128.
    assert 5 > 2*2 and 11**2 < 8*4**2
    assert all(4*d <= 24 < 128 for d in [1, 2, 3, 6])
    # 128/log(n) < sqrt(768)/sqrt(log(n)) iff log(n)>64/3.
    assert 128**2 * 3 == 768 * 64
    return {
        'status': 'PASS',
        'large_q_positive_margin': '184*(w^4-1)+134',
        'small_q_positive_coefficients_in_t_equals_w_squared_minus_1': [16, 28, 10],
        'logarithmic_chain': 'log n < 4 log 2+4 log w < 4w <=24 c_w <128 c_w',
        'power_of_two_endpoint_integer_margin': 8*4**2-11**2,
        'old_vs_new_concentration_bound_crossover_log_n': '64/3',
    }


def main():
    local = check_local()
    mixed = check_mixed()
    fixed, ws, candidates = check_fixed_cofactors()
    height_constants = general_height_constants()
    report = {
        'status': 'PASS',
        'scope': 'Exact structural checks of universal written proofs; not a search proving the original equation empty',
        'local_prime_power_congruences': local,
        'mixed_prime_and_CRT_checks': mixed,
        'fixed_cofactor_checks': fixed,
        'cofactors_with_w_over_gcd_w_6_at_most_12': ws,
        'sample_domain_note': 'Fixed-cofactor rows corroborate the exponent formula; this report does not claim all bounded remainders excluded',
        'fixed_cofactor_critical_examples': candidates,
        'new_defect': 'E=product p^max(alpha_p-3*x_p/2,0) for even x_p only',
        'square_refinement': 'Retain only critical p for which -X/p^x_p is a square modulo p^d_p',
        'new_necessary_conditions': ['E>=13', 'E_sq>=13', 'log(n)<128*E_sq', 'E/gcd(E,u)>=13'],
        'CRT_short_interval': 'u^3<229*E and at most 3^omega_odd(E)*(5 if 2|E else 1) classes modulo E',
        'fixed_cofactor_quartic_bound': 'c_w<=12 implies n<=216*w^4/25+2',
        'uniform_height_for_all_w_p_a': 'log n<128*w/gcd(w,6), n<2^(192*w/gcd(w,6)); no c_w<=12 or p>6w restriction',
        'uniform_height_exact_constant_checks': height_constants,
        'every_exact_prime_power_factor_bound': 'q=p^v_p(n-2) <128*(n-2)/(gcd((n-2)/q,6)*log n) <=128*(n-2)/log n',
        'unrestricted_prime_factor_count': True,
        'CF_computation_reexecuted': False,
        'reused_CF_certificate_version': 'v9, all H=1,...,12, through the written generalized-divisor transfer',
        'separate_Lean_core_execution': 'PASS in v10_formal/ValuationRecovery.lean; see that directory for the actual execution record',
        'global_product_CRT_CF_transfer_formalized': False,
        'independent_AI_mathematical_audit': 'PASS, root and separate fixed-cofactor reviewer; includes the full note, CF transfer, CRT identities, and Lean-statement correspondence',
        'external_peer_reviewed': False,
        'whole_original_equation_solved': False,
        'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'proof_note_sha256': sha256((ROOT/'v10_valuation_recovery.md').read_bytes()).hexdigest(),
    }
    target = ROOT/'v10_valuation_recovery_verification.json'
    target.write_text(json.dumps(report, indent=2, ensure_ascii=False)+'\n')
    print(json.dumps({k: v for k, v in report.items() if k != 'fixed_cofactor_critical_examples'}, ensure_ascii=False))


if __name__ == '__main__':
    main()
