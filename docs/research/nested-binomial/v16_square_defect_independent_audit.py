#!/usr/bin/env python3
"""Independent exact audit of the v16 reduced-square-denominator Pell certificate.

Does not import the producer. Fundamental units use a full quadratic-surd
period and reverse evaluation of finite continued fractions. Pell powers
use a second-order recurrence. Lucas residues use factorial tables at the
actual k and original j^2. The written height and Pell-completeness lemmas
remain necessary mathematical inputs; no Lean or CAS is invoked.
"""

import argparse
from collections import Counter
from functools import lru_cache
import hashlib
import json
from math import gcd, isqrt
from pathlib import Path


def need(condition, message):
    if not condition:
        raise AssertionError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_digest(value):
    raw = json.dumps(value, sort_keys=True, separators=(',', ':')).encode()
    return hashlib.sha256(raw).hexdigest()


def square_part_by_divisors(z):
    # Independently seek the largest integer whose square divides z.
    for s in range(isqrt(z), 0, -1):
        if z % (s * s) == 0:
            d = z // (s * s)
            need(all(d % (p * p) for p in range(2, isqrt(d) + 1)), 'square-free remainder')
            return s, d
    raise AssertionError('positive z has a square part')


def reverse_cf(coefficients):
    numerator, denominator = coefficients[-1], 1
    for a in reversed(coefficients[:-1]):
        numerator, denominator = a * numerator + denominator, numerator
    return numerator, denominator


def unit_by_full_period(D):
    root_floor = isqrt(D)
    need(root_floor ** 2 < D < (root_floor + 1) ** 2, 'nonsquare D')
    # Complete quotients (sqrt(D)+b)/c. The whole period is generated,
    # rather than stopping when a norm-one convergent is encountered.
    b, c, a = 0, 1, root_floor
    period, states = [], []
    seen = set()
    while True:
        b_new = a * c - b
        numerator = D - b_new * b_new
        need(numerator > 0 and numerator % c == 0, 'complete quotient division')
        c_new = numerator // c
        a_new = (root_floor + b_new) // c_new
        lower = a_new * c_new - b_new
        upper = (a_new + 1) * c_new - b_new
        need((lower <= 0 or lower * lower <= D) and upper > 0 and D < upper * upper,
             'independently verified complete-quotient floor')
        state = (b_new, c_new)
        need(state not in seen, 'period terminates before repeating a state')
        seen.add(state)
        states.append([b_new, c_new, a_new])
        period.append(a_new)
        if b_new == root_floor and c_new == 1:
            need(a_new == 2 * root_floor, 'end of quadratic-surd period')
            break
        b, c, a = b_new, c_new, a_new

    coefficients = ([root_floor] + period * (1 if len(period) % 2 == 0 else 2))[:-1]
    norms, denominators = [], []
    for end in range(1, len(coefficients) + 1):
        x, y = reverse_cf(coefficients[:end])
        need(y > 0 and gcd(x, y) == 1, 'reduced convergent')
        norms.append(x * x - D * y * y)
        denominators.append(y)
    need(norms[-1] == 1 and all(v != 1 for v in norms[:-1]), 'first positive norm-one convergent')
    need(all(a <= b for a, b in zip(denominators, denominators[1:])), 'ordered convergent denominators')
    x, y = reverse_cf(coefficients)
    return {
        'd': D, 'x': x, 'y': y, 'a0': root_floor,
        'period': period, 'period_states': states,
        'partial_quotients': coefficients, 'convergent_norms': norms,
    }


def classify(n_num, r_num, r_den, delta, M, K, counts):
    if n_num & 1 or r_num % r_den:
        return 'i', None
    n, r = n_num // 2, r_num // r_den
    need(M * delta * r * r == K * n * (n - 1), 'quadratic reconstruction identity')
    counts['integral_n_r'] += 1
    if n < 104:
        return 'n', None
    counts['n_ge_104'] += 1
    if gcd(n, 3) * gcd(n - 1, 6) != M:
        return 'm', None
    counts['actual_M'] += 1
    Q = n * (n - 1) // M
    if Q // gcd(Q, r * r) != delta:
        return 'd', None
    counts['actual_delta'] += 1
    if pow(r, 3, Q):
        return 'q', None
    counts['cube_divisibility'] += 1
    need(r % delta == 0 and Q % (delta ** 3) == 0, 'intrinsic defect divides r and its cube divides Q')
    if r <= 3 * n or 3 * r >= 10 * n:
        return 'c', None
    counts['strict_coarse_interval'] += 1
    J = None
    if n >= 1024:
        # floor(log_3(n-1)), computed by repeated integer quotient.
        z, J = n - 1, 0
        while z >= 3:
            z //= 3
            J += 1
        need(3 ** J < n <= 3 ** (J + 1), 'strict logarithm bracket')
        if (4 * J) * (r - 3 * n) >= 3 * n:
            return 'l', None
    counts['strict_log_interval'] += 1
    counts['original_branches'] += 2
    return 'w', {'delta': delta, 'M': M, 'K': K, 'n': n, 'r': r, 'log_lower_J': J}


def prime(p):
    return p >= 2 and all(p % v for v in range(2, isqrt(p) + 1))


@lru_cache(None)
def factorial_tables(p):
    need(prime(p), 'prime witness modulus')
    fact = [1]
    for value in range(1, p):
        fact.append(fact[-1] * value % p)
    inverse = [pow(value, p - 2, p) for value in fact]
    need(all(a * b % p == 1 for a, b in zip(fact, inverse)), 'inverse factorial table')
    return fact, inverse


def actual_lucas(N, K, p):
    need(0 <= K <= N, 'valid binomial lower index')
    fact, inv = factorial_tables(p)
    value = 1
    while N or K:
        N, a = divmod(N, p)
        K, b = divmod(K, p)
        if b > a:
            return 0
        value = value * fact[a] * inv[b] * inv[a - b] % p
    return value


def zero_digit(N, K, p, certificate):
    first = None
    position = 0
    while N or K:
        a, b = N % p, K % p
        if b > a and first is None:
            first = {'position': position, 'upper_digit': a, 'lower_digit': b}
        N //= p
        K //= p
        position += 1
    need(first == certificate, 'first zero-digit certificate including null case')


def run(input_path, generator_path, v15_path, output_path):
    input_hash, generator_hash, v15_hash = digest(input_path), digest(generator_path), digest(v15_path)
    data = json.loads(input_path.read_text())
    need(data['source_sha256'] == generator_hash, 'producer source hash')
    need(data['excluded_defects'][0] == 1, 'initial defect is 1')
    cutoff = data['excluded_defects'][1]
    need(cutoff == 12 and data['necessary_lower_bound'] == 13, 'requested fixed scope')

    triples = []
    for delta in range(1, cutoff + 1):
        for M in [1, 2, 3, 6]:
            C = M * delta
            # 10400/927 < 12 gives an independent covering enumeration.
            for K in range(1, 12 * C + 1):
                if K > 9 * C and 927 * K < 10400 * C and gcd(K, delta) == 1:
                    triples.append((delta, M, K))
    need([(f['delta'], f['M'], f['K']) for f in data['families']] == triples,
         'complete coefficient triple list')
    decompositions = [square_part_by_divisors(M * delta * K) for delta, M, K in triples]
    D_values = sorted({D for s, D in decompositions if D > 1})
    units = {D: unit_by_full_period(D) for D in D_values}
    need([v['d'] for v in data['fundamental_units']] == D_values, 'complete radicand list')
    for provided in data['fundamental_units']:
        independent = units[provided['d']]
        for key in ['a0', 'x', 'y', 'partial_quotients', 'convergent_norms']:
            need(provided[key] == independent[key], 'independent fundamental unit and trace: ' + key)

    counts_by_delta = {delta: Counter() for delta in range(1, cutoff + 1)}
    traces, candidates = [], []
    for index, ((delta, M, K), (s, D)) in enumerate(zip(triples, decompositions)):
        counts = counts_by_delta[delta]
        counts['coefficient_triples'] += 1
        supplied = data['families'][index]
        need((supplied['s'], supplied['d']) == (s, D), 'square part agrees')
        if D == 1:
            counts['square_discriminants'] += 1
            need(supplied['pell_points'] == 0 and supplied['dispositions'] == ''
                 and supplied['first_omitted_point'] is None, 'square discriminant has no positive Pell point')
            traces.append({'delta': delta, 'M': M, 'K': K, 'd': D, 's': s, 'dispositions': '',
                           'first_omitted_point': None})
            continue
        unit_x, unit_y = units[D]['x'], units[D]['y']
        last_x, last_y, x, y = 1, 0, unit_x, unit_y
        power = 1
        threshold = 2 ** (42 * delta + 1) - 1
        codes = []
        while x < threshold:
            need(x > last_x and y > last_y and x * x - D * y * y == 1, 'ordered Pell point')
            counts['pell_points_below_height'] += 1
            code, candidate = classify(x + 1, s * D * y, 2 * M * delta, delta, M, K, counts)
            codes.append(code)
            if candidate is not None:
                candidate.update({'family_index': index, 'power_index': power})
                candidates.append(candidate)
            # Independent second-order recurrence from epsilon+epsilon^-1=2*unit_x.
            last_x, x = x, 2 * unit_x * x - last_x
            last_y, y = y, 2 * unit_x * y - last_y
            power += 1
        need(last_x < threshold <= x and x * x - D * y * y == 1, 'complete first-omitted endpoint')
        endpoint = {'power': power, 'x': x, 'y': y}
        need(supplied['pell_points'] == len(codes) and supplied['dispositions'] == ''.join(codes)
             and supplied['first_omitted_point'] == endpoint, 'full recurrence trace and endpoint')
        need(len(codes) <= 28 * delta + 1, 'stated universal recurrence length bound')
        traces.append({'delta': delta, 'M': M, 'K': K, 'd': D, 's': s, 'dispositions': ''.join(codes),
                       'first_omitted_point': endpoint})

    need(len(candidates) == len(data['candidates']), 'complete final candidate count')
    modular_evidence = []
    exceptional = []
    both_zero_count = 0
    witness_primes = []
    for independent, supplied in zip(candidates, data['candidates']):
        need(all(supplied[key] == value for key, value in independent.items()), 'candidate metadata')
        n, r, delta = independent['n'], independent['r'], independent['delta']
        A = n * (n - 1) * (n - 2) // 6
        need([w['branch'] for w in supplied['witnesses']] == ['k=r', 'k=A-r'], 'both branches listed')
        for witness in supplied['witnesses']:
            k = r if witness['branch'] == 'k=r' else A - r
            p = witness['prime']
            left = actual_lucas(A, k, p)
            B = actual_lucas(n * n, (n - 3) ** 2, p)
            square = pow(k, 2, p)
            right = (B + square) % p
            need([left, B, square, right] == [witness[key] for key in
                 ['left_residue', 'B_residue', 'k_squared_residue', 'right_residue']],
                 'full original-index factorial-Lucas residues')
            need(left != right, 'original equation excluded')
            zero_digit(A, r, p, witness['left_zero_digit'])
            zero_digit(n * n, 6 * n - 9, p, witness['B_zero_digit'])
            counts_by_delta[delta]['modular_branch_exclusions'] += 1
            witness_primes.append(p)
            record = {'delta': delta, 'n': n, 'r': r, 'branch': witness['branch'], 'prime': p,
                      'actual_k_left_residue': left, 'actual_j_squared_B_residue': B,
                      'k_squared_residue': square, 'right_residue': right}
            modular_evidence.append(record)
            if left == B == 0 and square:
                both_zero_count += 1
            else:
                exceptional.append(record)

    totals = Counter()
    per_delta = []
    for delta, counts in counts_by_delta.items():
        need(counts['coefficient_triples'] < 27 * delta, 'uniform coefficient count')
        totals.update(counts)
        per_delta.append({'delta': delta, 'statistics': dict(counts)})
    need(data['statistics'] == dict(totals) and data['by_delta'] == per_delta, 'all global and per-defect counts')
    need(data['largest_witness_prime'] == max(witness_primes), 'maximum witness prime')
    need(data['both_binomials_zero_witnesses'] == both_zero_count, 'vanishing-witness classification')
    need(data['largest_candidate_decimal_digits'] == max(len(str(c['n'])) for c in candidates), 'largest candidate size')
    need(data['survivors'] == [] and data['status'] == 'PASS', 'producer final bookkeeping')
    v15 = json.loads(v15_path.read_text())
    prior_pairs = sorted({(c['n'], c['r']) for c in v15['original_equation_modular_records']})
    new_pairs = sorted((c['n'], c['r']) for c in candidates if c['delta'] == 1)
    need(prior_pairs == new_pairs, 'v15 delta-one control independently reproduced')
    need(data['v15_control']['input_sha256'] == v15_hash and
         data['v15_control']['pairs'] == [list(x) for x in new_pairs], 'v15 control report')
    need(digest(input_path) == input_hash and digest(generator_path) == generator_hash
         and digest(v15_path) == v15_hash, 'audit inputs unchanged')

    report = {
        'status': 'PASS',
        'scope': 'Independent exact finite Pell and original-equation modular audit for delta=1..12; no CAS or Lean execution.',
        'input_file': input_path.name, 'input_sha256': input_hash,
        'generator_file': generator_path.name, 'generator_sha256': generator_hash,
        'v15_input_file': v15_path.name, 'v15_input_sha256': v15_hash,
        'coefficient_enumeration': 'Enumerate K<=12*M*delta and independently impose both strict cross-multiplied inequalities and gcd(K,delta)=1.',
        'square_part_method': 'Largest square divisor by descending integer divisor checks.',
        'fundamental_unit_method': 'Complete surd period, reverse evaluation of each finite CF, all earlier norms rejected; completeness uses the stated Legendre lemma for actual Pell solutions.',
        'pell_point_method': 'Second-order recurrence with exact first-omitted point and every classification compared.',
        'modular_method': 'Factorial-table Lucas at actual k and original j^2=(n-3)^2, plus every zero-digit or null certificate.',
        'statistics': dict(totals), 'by_delta': per_delta,
        'distinct_radicands': len(D_values),
        'fundamental_units': [{'d': D, 'x': units[D]['x'], 'y': units[D]['y'],
                               'period_length': len(units[D]['period']),
                               'earlier_convergent_norms_rejected': len(units[D]['convergent_norms']) - 1}
                              for D in D_values],
        'complete_fundamental_trace_sha256': canonical_digest([units[D] for D in D_values]),
        'complete_family_trace_sha256': canonical_digest(traces),
        'candidate_metadata_sha256': canonical_digest(candidates),
        'original_equation_modular_evidence': modular_evidence,
        'largest_witness_prime': max(witness_primes),
        'both_binomials_zero_witnesses': both_zero_count,
        'nonvanishing_pattern_witnesses': exceptional,
        'delta1_final_pairs': [list(x) for x in new_pairs],
        'survivors': [],
        'completeness_boundary': 'The written height, Pell-convergent completeness and minimal-unit descent proofs are necessary; the finite check does not itself formalize them.',
        'new_lean_execution': False, 'new_complete_cas_calls': 0,
        'source_sha256': digest(Path(__file__)),
    }
    output_path.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({key: report[key] for key in ['status', 'statistics', 'distinct_radicands',
                      'largest_witness_prime', 'both_binomials_zero_witnesses', 'nonvanishing_pattern_witnesses',
                      'survivors', 'input_sha256', 'generator_sha256', 'source_sha256']}, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', required=True, type=Path)
    parser.add_argument('--generator', required=True, type=Path)
    parser.add_argument('--v15', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    run(args.input, args.generator, args.v15, args.output)
