#!/usr/bin/env python3
"""Complete exact check under Q | r**2, using only ordinary Pell equations.

Prior branch inputs: n>=104; Q=(n/gcd(n,3))*((n-1)/gcd(n-1,6));
3*n<r<10*n/3; for n>=1024, r<3*n+3*n/(4*log(n)).
The assumption Q|r**2 implies n<e**30<2**45 and 25 pairs (M,L).
This program generates every positive Pell point up to that proven height,
then excludes candidates by necessary bounds or by the original equation
modulo a prime. It does not evaluate huge binomial coefficients or use CAS.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from functools import lru_cache
from math import comb, gcd, isqrt
from pathlib import Path

INDEX_LIMIT = 1 << 45


def require(test, message):
    if not test:
        raise ValueError(message)


def square_part(value):
    """Return s,d with value=s*s*d and positive square-free d."""
    original = value
    s = 1
    p = 2
    while p*p <= value:
        while value % (p*p) == 0:
            value //= p*p
            s *= p
        p += 1
    require(original == s*s*value, 'square-part product')
    return s, value


@lru_cache(None)
def fundamental_pell(d):
    """Find and certify the least positive y by a small exact exhaustive loop.

    This is not a search in n. The largest y reached for our 13 radicands
    is 47458. Since x is then forced, there is no unproved CF/CAS claim.
    """
    require(d > 1 and isqrt(d)**2 != d, 'nonsquare radicand required')
    y = 1
    while True:
        x = isqrt(1+d*y*y)
        if x*x-d*y*y == 1:
            return x, y
        y += 1


def primes_up_to(limit):
    return [p for p in range(2, limit+1)
            if all(p % divisor for divisor in range(2, isqrt(p)+1))]


def lucas(n, k, p):
    if k < 0 or k > n:
        return 0
    result = 1
    while n or k:
        a, b = n % p, k % p
        if b > a:
            return 0
        result = result*comb(a, b) % p
        n //= p
        k //= p
    return result


def lucas_zero_digit(n, k, p):
    """A single digit certifying that binom(n,k) vanishes modulo p."""
    position = 0
    while n or k:
        a, b = n % p, k % p
        if b > a:
            return {'position': position, 'upper_digit': a, 'lower_digit': b}
        n //= p
        k //= p
        position += 1
    return None


def strict_upper(n):
    upper = Fraction(10*n, 3)
    ell = None
    if n >= 1024:
        power, exponent = 1, 0
        while power*3 < n:
            power *= 3
            exponent += 1
        require(exponent > 0 and power == 3**exponent < n, 'log lower bound')
        logarithmic = Fraction(3*n)+Fraction(3*n, 4*exponent)
        if logarithmic < upper:
            upper, ell = logarithmic, exponent
    return upper, ell


def original_witness(n, r, k, primes):
    a = n*(n-1)*(n-2)//6
    for p in primes:
        lhs = lucas(a, r, p)  # binom(A,k)=binom(A,r) in either branch
        x_residue = lucas(n*n, 6*n-9, p)
        rhs = (x_residue+k*k) % p
        if lhs != rhs:
            return {'prime': p, 'left_residue': lhs, 'X_residue': x_residue,
                    'k_squared_residue': k*k % p, 'right_residue': rhs,
                    'left_zero_digit': lucas_zero_digit(a, r, p),
                    'X_zero_digit': lucas_zero_digit(n*n, 6*n-9, p)}
    return None


def main(destination, prime_limit):
    # If log(n)>=30 and n>=1024, the two exact rational bounds contradict.
    require(Fraction(121, 40)**2 < Fraction(55, 6)*Fraction(1023, 1024),
            'uniform logarithmic height contradiction')
    pairs = [(m, ell) for m in (1, 2, 3, 6)
             for ell in range(9*m+1, (10400*m-1)//927+1)]
    require(len(pairs) == 25, 'all coefficient pairs')
    primes = primes_up_to(prime_limit)
    families, candidate_records, modular_records = [], [], []
    survivors = []
    stats = {'pell_points_below_height': 0, 'integral_n_r': 0,
             'n_ge_104': 0, 'correct_M': 0, 'strict_coarse_interval': 0,
             'strict_log_interval': 0, 'modular_branch_exclusions': 0}
    for m, ell in pairs:
        s, d = square_part(m*ell)
        family = {'M': m, 'L': ell, 's': s, 'd': d}
        if d == 1:
            family.update({'trivial_square_case': True, 'points': []})
            families.append(family)
            continue
        u, v = fundamental_pell(d)
        family['fundamental_solution'] = [u, v]
        family['minimality_y_checked_through'] = v
        x, y, exponent = u, v, 1
        points = []
        while x < 2*INDEX_LIMIT-1:
            require(x*x-d*y*y == 1, 'Pell recurrence norm')
            point = {'power': exponent, 'x': x, 'y': y}
            points.append(point)
            stats['pell_points_below_height'] += 1
            if x % 2 and (s*d*y) % (2*m) == 0:
                n, r = (x+1)//2, s*d*y//(2*m)
                require(m*r*r == ell*n*(n-1), 'inverse coordinate identity')
                stats['integral_n_r'] += 1
                point.update({'n': n, 'r': r})
                if n >= 104:
                    stats['n_ge_104'] += 1
                    if gcd(n, 3)*gcd(n-1, 6) == m:
                        stats['correct_M'] += 1
                        q = (n//gcd(n, 3))*((n-1)//gcd(n-1, 6))
                        require(r*r == ell*q, 'actual Q divisibility and L')
                        candidate = {'M': m, 'L': ell, 'd': d, 'power': exponent,
                                     'n': n, 'r': r, 'Q': q}
                        candidate_records.append(candidate)
                        if r > 3*n and 3*r < 10*n:
                            stats['strict_coarse_interval'] += 1
                            upper, log_lower = strict_upper(n)
                            candidate.update({'strict_upper_bound': [upper.numerator, upper.denominator],
                                              'log_n_strict_lower_bound': log_lower})
                            if r*upper.denominator < upper.numerator:
                                stats['strict_log_interval'] += 1
                                a = n*(n-1)*(n-2)//6
                                witnesses = []
                                for branch, k in [('k=r', r), ('k=A-r', a-r)]:
                                    witness = original_witness(n, r, k, primes)
                                    record = dict(candidate, branch=branch, k=k, witness=witness)
                                    modular_records.append(record)
                                    witnesses.append(witness)
                                    if witness is None:
                                        survivors.append(record)
                                    else:
                                        stats['modular_branch_exclusions'] += 1
                                candidate['disposition'] = ('original_equation_modular_exclusion'
                                                            if all(witnesses) else 'unresolved')
                            else:
                                candidate['disposition'] = 'strict_log_interval_exclusion'
                        else:
                            candidate['disposition'] = 'strict_coarse_interval_exclusion'
            x, y = u*x+d*v*y, v*x+u*y
            exponent += 1
        family['points'] = points
        family['first_point_at_or_beyond_height'] = {'power': exponent, 'x': x, 'y': y}
        families.append(family)
    radicands = sorted({row['d'] for row in families if row['d'] > 1})
    control = [row for row in modular_records if row['n'] == 169 and row['r'] == 546]
    require(len(control) == 2 and all(row['witness'] for row in control),
            'known necessary-condition control checked in both original branches')
    require(all(row['witness']['left_zero_digit'] is not None
                and row['witness']['X_zero_digit'] is not None
                and row['witness']['k_squared_residue'] != 0
                for row in modular_records if row['witness']),
            'every modular exclusion has two single-digit zero certificates')
    report = {
        'status': 'PASS' if not survivors else 'UNRESOLVED',
        'hypothesis_under_exclusion': 'Q divides r squared',
        'scope': 'ell=1, j=i-3, n>=104, both k=r and k=A-r',
        'prior_inputs': ['Q divides r cubed (needed only for the cube-factor consequence)',
                         '3n<r<10n/3', 'n>=1024 implies r<3n+3n/(4 log n)',
                         'e<3 and e^2<8'],
        'proven_strict_height_bound': INDEX_LIMIT,
        'coefficient_pairs': pairs,
        'radicands': radicands,
        'fundamental_units': [{'d': d, 'x': fundamental_pell(d)[0],
                               'y': fundamental_pell(d)[1],
                               'minimality_y_checked_through': fundamental_pell(d)[1]}
                              for d in radicands],
        'statistics': stats,
        'families': families,
        'candidate_records': candidate_records,
        'original_equation_modular_records': modular_records,
        'survivors': survivors,
        'largest_witness_prime': max((row['witness']['prime'] for row in modular_records
                                      if row['witness']), default=None),
        'verification_boundary': 'Written elementary Pell reduction plus exact Python certificate; no Lean, no complete CAS solver',
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({k: report[k] for k in ['status', 'proven_strict_height_bound',
                     'radicands', 'statistics', 'largest_witness_prime']}))
    print(json.dumps({'survivor_count': len(survivors), 'output': str(destination)}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--prime-limit', default=97, type=int)
    args = parser.parse_args()
    main(args.output, args.prime_limit)
