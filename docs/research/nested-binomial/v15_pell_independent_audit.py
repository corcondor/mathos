#!/usr/bin/env python3
"""Independent exact audit of the Q|r^2 Pell certificate.

The producer finds fundamental units by enumerating y and uses first-order
unit multiplication. This audit constructs them from continued fractions,
also checks minimality, and uses second-order recurrences. Lucas arithmetic
uses factorial/inverse-factorial digit tables on the actual original k and
j^2, rather than math.comb on the producer's symmetric lower indices.
"""

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def factor(n):
    result = []
    for p in range(2, math.isqrt(n) + 1):
        if p * p > n:
            break
        if n % p:
            continue
        exponent = 0
        while n % p == 0:
            n //= p
            exponent += 1
        result.append((p, exponent))
    if n > 1:
        result.append((n, 1))
    return result


def squarefree_split(n):
    square_root = kernel = 1
    for p, exponent in factor(n):
        square_root *= p ** (exponent // 2)
        kernel *= p ** (exponent % 2)
    return square_root, kernel


def cf_unit(d):
    a0 = math.isqrt(d)
    require(a0 * a0 != d and d > 1, 'nontrivial Pell radicand')
    m, denominator, a = 0, 1, a0
    p_previous_previous, p_previous = 0, 1
    q_previous_previous, q_previous = 1, 0
    quotients = []
    while True:
        quotients.append(a)
        p = a * p_previous + p_previous_previous
        q = a * q_previous + q_previous_previous
        if p * p - d * q * q == 1:
            # Certify the minimality directly as well. These are fixed
            # radicands; the largest endpoint is only 47458.
            for smaller_y in range(1, q):
                square = 1 + d * smaller_y * smaller_y
                root = math.isqrt(square)
                require(root * root != square, f'nonminimal unit d={d}')
            return p, q, quotients
        p_previous_previous, p_previous = p_previous, p
        q_previous_previous, q_previous = q_previous, q
        m = denominator * a - m
        require((d - m * m) % denominator == 0, 'CF denominator integrality')
        denominator = (d - m * m) // denominator
        require(denominator > 0, 'CF denominator positivity')
        a = (a0 + m) // denominator


def pell_points(d, u, v, bound):
    # epsilon^2 - 2*u*epsilon + 1 = 0. The resulting second-order
    # recurrence generates powers of the positive fundamental unit.
    old_x, old_y, x, y, exponent = 1, 0, u, v, 1
    points = []
    while x < 2 * bound - 1:
        require(x * x - d * y * y == 1 and y > 0, 'Pell norm')
        points.append({'power': exponent, 'x': x, 'y': y})
        old_x, x = x, 2 * u * x - old_x
        old_y, y = y, 2 * u * y - old_y
        exponent += 1
    require(x * x - d * y * y == 1, 'terminal Pell norm')
    return points, {'power': exponent, 'x': x, 'y': y}


def rational_upper(n):
    coarse = Fraction(10 * n, 3)
    if n < 1024:
        return coarse, None
    # floor(log_3(n-1)) equals the largest integer L with 3^L<n.
    quotient, exponent = n - 1, 0
    while quotient >= 3:
        quotient //= 3
        exponent += 1
    require(3 ** exponent < n <= 3 ** (exponent + 1), 'strict log bracket')
    refined = Fraction(3 * n * (4 * exponent + 1), 4 * exponent)
    return (refined, exponent) if refined < coarse else (coarse, None)


def prime_test(p):
    return p >= 2 and all(p % d for d in range(2, math.isqrt(p) + 1))


def lucas_factorial(n, k, p):
    require(prime_test(p), 'Lucas modulus must be prime')
    if k < 0 or k > n:
        return 0
    factorial = [1] * p
    for i in range(1, p):
        factorial[i] = factorial[i - 1] * i % p
    inverse = [pow(value, p - 2, p) for value in factorial]
    result = 1
    while k:
        upper, lower = n % p, k % p
        if lower > upper:
            return 0
        result = result * factorial[upper] * inverse[lower] * inverse[upper - lower] % p
        n //= p
        k //= p
    return result


def audit_zero_digit(n, k, p, data):
    require(isinstance(data, dict), 'zero-digit certificate absent')
    position = data['position']
    require(type(position) is int and position >= 0, 'zero-digit position')
    upper = (n // p ** position) % p
    lower = (k // p ** position) % p
    require(data == {'position': position, 'upper_digit': upper, 'lower_digit': lower},
            'zero-digit values')
    require(lower > upper, 'digit does not establish Lucas zero')


def run(input_path, generator_path, output_path):
    input_hash = digest(input_path)
    source_hash = digest(generator_path)
    data = json.loads(input_path.read_text())
    require(data['source_sha256'] == source_hash, 'generator/source binding')
    bound = 2 ** 45
    require(data['proven_strict_height_bound'] == bound, 'height bound')
    require(Fraction(121, 40) ** 2 * Fraction(1024, 1023) < Fraction(55, 6),
            'logarithmic contradiction constants')
    # M comes from n modulo 6; independently reconstruct its full set.
    M_values = sorted({math.gcd(n, 3) * math.gcd(n - 1, 6) for n in range(2, 8)})
    require(M_values == [1, 2, 3, 6], 'M support')
    coefficient_pairs = [[m, L] for m in M_values for L in range(1, 12 * m)
                         if 9 * m < L and 927 * L < 10400 * m]
    require(len(coefficient_pairs) == 25 and data['coefficient_pairs'] == coefficient_pairs,
            'complete coefficient pair coverage')
    d_values = sorted({squarefree_split(m * L)[1] for m, L in coefficient_pairs})
    require(all(d > 1 for d in d_values), 'nontrivial radicands')
    require(data['radicands'] == d_values and len(d_values) == 13, 'complete radicand coverage')

    units = {}
    cf_evidence = []
    for d in d_values:
        u, v, quotients = cf_unit(d)
        units[d] = u, v
        cf_evidence.append({'d': d, 'x': u, 'y': v, 'continued_fraction_quotients': quotients,
                            'all_smaller_positive_y_rejected': v - 1})
    recorded_units = [{'d': d, 'x': units[d][0], 'y': units[d][1],
                       'minimality_y_checked_through': units[d][1]} for d in d_values]
    require(data['fundamental_units'] == recorded_units, 'fundamental units and minimality')
    require(len(data['families']) == 25, 'family count')
    families = {(r['M'], r['L']): r for r in data['families']}
    require(len(families) == 25 and set(families) == {tuple(p) for p in coefficient_pairs},
            'unique family coverage')

    stats = {'pell_points_below_height': 0, 'integral_n_r': 0, 'n_ge_104': 0,
             'correct_M': 0, 'strict_coarse_interval': 0, 'strict_log_interval': 0,
             'modular_branch_exclusions': 0}
    expected_candidates = []
    expected_modular = []
    terminal_points = []
    for m, L in coefficient_pairs:
        s, d = squarefree_split(m * L)
        family = families[m, L]
        u, v = units[d]
        require((family['s'], family['d']) == (s, d), 'squarefree factorization')
        require(family['fundamental_solution'] == [u, v], 'family unit')
        require(family['minimality_y_checked_through'] == v, 'family minimality endpoint')
        points, terminal = pell_points(d, u, v, bound)
        terminal_points.append({'M': m, 'L': L, **terminal})
        require(family['first_point_at_or_beyond_height'] == terminal, 'terminal cutoff point')
        for point in points:
            stats['pell_points_below_height'] += 1
            x, y, power = point['x'], point['y'], point['power']
            numerator = s * d * y
            if x % 2 == 0 or numerator % (2 * m):
                continue
            n, r = (x + 1) // 2, numerator // (2 * m)
            require(m * r * r == L * n * (n - 1), 'inverse Pell substitution')
            point.update({'n': n, 'r': r})
            stats['integral_n_r'] += 1
            if n < 104:
                continue
            stats['n_ge_104'] += 1
            actual_M = math.gcd(n, 3) * math.gcd(n - 1, 6)
            if actual_M != m:
                continue
            stats['correct_M'] += 1
            q = n * (n - 1) // m
            require(r * r == L * q and (r * r) % q == 0, 'actual Q and L')
            candidate = {'M': m, 'L': L, 'd': d, 'power': power, 'n': n, 'r': r, 'Q': q}
            if not (3 * n < r and 3 * r < 10 * n):
                candidate['disposition'] = 'strict_coarse_interval_exclusion'
            else:
                stats['strict_coarse_interval'] += 1
                upper, exponent = rational_upper(n)
                candidate.update({'strict_upper_bound': [upper.numerator, upper.denominator],
                                  'log_n_strict_lower_bound': exponent})
                if r >= upper:
                    candidate['disposition'] = 'strict_log_interval_exclusion'
                else:
                    stats['strict_log_interval'] += 1
                    A = n * (n - 1) * (n - 2) // 6
                    for branch, k in [('k=r', r), ('k=A-r', A - r)]:
                        require(0 < k < A, 'original binomial domain')
                        expected_modular.append({**candidate, 'branch': branch, 'k': k})
                    candidate['disposition'] = 'original_equation_modular_exclusion'
            expected_candidates.append(candidate)
        require(family['points'] == points, 'all Pell points and inverse coordinates')

    require(data['candidate_records'] == expected_candidates, 'complete candidate records')
    require(len(data['original_equation_modular_records']) == len(expected_modular),
            'all original branches represented')
    modular_evidence = []
    witness_primes = []
    for record, expected in zip(data['original_equation_modular_records'], expected_modular):
        witness = record['witness']
        require({key: value for key, value in record.items() if key != 'witness'} == expected,
                'original branch coordinates')
        require(isinstance(witness, dict), 'missing witness')
        n, r, k = record['n'], record['r'], record['k']
        A = n * (n - 1) * (n - 2) // 6
        p = witness['prime']
        require(prime_test(p), 'witness modulus prime')
        # Independently use the original lower indices in both binomials.
        left = lucas_factorial(A, k, p)
        X_value = lucas_factorial(n * n, (n - 3) ** 2, p)
        square = pow(k, 2, p)
        right = (X_value + square) % p
        require(witness['left_residue'] == left and witness['X_residue'] == X_value
                and witness['k_squared_residue'] == square and witness['right_residue'] == right,
                'independent original-equation Lucas residues')
        require(left != right, 'witness does not exclude the equation')
        # The producer's short vanishing certificates use symmetric indices.
        audit_zero_digit(A, r, p, witness['left_zero_digit'])
        audit_zero_digit(n * n, 6 * n - 9, p, witness['X_zero_digit'])
        require(left == X_value == 0 and square != 0, 'vanishing/nonzero pattern')
        stats['modular_branch_exclusions'] += 1
        witness_primes.append(p)
        modular_evidence.append({'n': n, 'r': r, 'branch': record['branch'], 'prime': p,
                                 'actual_k_left_residue': left, 'actual_j_squared_X_residue': X_value,
                                 'k_squared_residue': square, 'right_residue': right,
                                 'both_zero_digit_certificates_valid': True})

    require(data['statistics'] == stats, 'all stage counts')
    require(data['largest_witness_prime'] == max(witness_primes), 'maximum witness prime')
    require(data['survivors'] == [] and data['status'] == 'PASS', 'producer final bookkeeping')
    require(digest(input_path) == input_hash and digest(generator_path) == source_hash,
            'input changed during audit')
    result = {
        'status': 'PASS',
        'scope': 'Independent finite Pell and original-equation modular audit; no CAS or Lean execution',
        'input_file': input_path.name,
        'input_sha256': input_hash,
        'generator_file': generator_path.name,
        'generator_sha256': source_hash,
        'coefficient_pair_count': len(coefficient_pairs),
        'radicand_count': len(d_values),
        'fundamental_unit_method': 'Continued fractions, plus exact rejection of every smaller positive y',
        'point_generation_method': 'Second-order recurrence, with the first omitted point certified',
        'modular_method': 'Factorial-table Lucas digits on actual k and j^2; also verify producer zero-digit certificates',
        'statistics': stats,
        'fundamental_units': cf_evidence,
        'terminal_points': terminal_points,
        'original_equation_modular_evidence': modular_evidence,
        'largest_witness_prime': max(witness_primes),
        'survivors': [],
        'completeness_boundary': 'Written height and integer Pell-unit descent proof are necessary; no claim that finite checking alone proves them',
        'source_sha256': digest(Path(__file__)),
    }
    output_path.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({key: result[key] for key in ['status', 'coefficient_pair_count', 'radicand_count',
                      'statistics', 'largest_witness_prime', 'survivors']}, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', required=True, type=Path)
    parser.add_argument('--generator', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    arguments = parser.parse_args()
    run(arguments.input, arguments.generator, arguments.output)
