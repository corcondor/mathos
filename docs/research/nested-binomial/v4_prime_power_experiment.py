"""Exploratory p-adic constraints for ell=1 and i a prime power.

This is NOT a certificate of global nonexistence.  It measures which
analytically permitted triples survive one prime-power congruence.
"""
import argparse
import json
from math import comb, isqrt


def vp(n, p):
    assert n > 0
    value = 0
    while n % p == 0:
        n //= p
        value += 1
    return value


def binomial_row_mod(n, limit, p, modulus):
    unit = 1
    valuation = 0
    yield 0, 1, 0
    for r in range(1, min(limit, n) + 1):
        numerator, denominator = n - r + 1, r
        while numerator % p == 0:
            numerator //= p
            valuation += 1
        while denominator % p == 0:
            denominator //= p
            valuation -= 1
        unit = unit * (numerator % modulus) % modulus
        unit = unit * pow(denominator, -1, modulus) % modulus
        assert valuation >= 0
        yield r, unit * pow(p, valuation, modulus) % modulus, valuation


def factorial_units(n, p, modulus):
    values = [1] * (n + 1)
    for s in range(1, n + 1):
        unit = s
        while unit % p == 0:
            unit //= p
        values[s] = values[s - 1] * unit % modulus
    return values


def verify_primitives():
    for p in [2, 3, 5, 7]:
        modulus = p ** 7
        for n in range(1, 70):
            for r, residue, valuation in binomial_row_mod(n, n, p, modulus):
                exact = comb(n, r)
                assert residue == exact % modulus
                assert valuation == vp(exact, p)


def prime_powers(limit):
    for p in range(2, isqrt(limit) + 1):
        if any(p % d == 0 for d in range(2, isqrt(p) + 1)):
            continue
        n, exponent = p * p, 2
        while n <= limit:
            if n >= 23:
                yield p, exponent, n
            n *= p
            exponent += 1


def run(limit):
    verify_primitives()
    summaries = []
    survivors = []
    for p, a, n in sorted(prime_powers(limit), key=lambda x: x[2]):
        modulus = p ** (2 * a + 4)
        units = factorial_units(n * n, p, modulus)
        count = [0, 0]
        for j in range(21, n - 1):
            A = comb(n, j)
            b = vp(j, p)
            Xv = 2 * (a - b)
            X = units[n*n] * pow(units[j*j], -1, modulus)
            X = X * pow(units[n*n-j*j], -1, modulus) % modulus
            X = X * pow(p, Xv, modulus) % modulus
            if n >= 2*j:
                upper = 2*j - 1
            elif n-j >= 5:
                upper = 3*j - 1
            elif n-j >= 4:
                upper = 4*j - 1
            elif n-j >= 3 or j >= 800:
                upper = 5*j - 1
            else:
                upper = 10*j - 1
            upper = min(upper, A//2)
            for r, L, Lv in binomial_row_mod(A, upper, p, modulus):
                if r < j+2 or r*r-r*j-j*j <= 0:
                    continue
                count[0] += 1
                for side, B in [('lower', r), ('upper', A-r)]:
                    if (L-X-B*B) % modulus == 0:
                        count[1] += 1
                        survivors.append({'p':p,'a':a,'i':n,'j':j,'r':r,
                                          'side':side,'v_j':b,'v_r':vp(r,p),
                                          'v_L':Lv,'v_X':Xv})
        summaries.append({'p':p,'a':a,'i':n,'triples':count[0],
                          'surviving_branches':count[1], 'modulus_exponent':2*a+4})
        print(json.dumps(summaries[-1]), flush=True)
    output = {'status':'exploratory_not_a_global_proof','upper_i':limit,
              'summaries':summaries,'survivors':survivors}
    with open('v4_prime_power_experiment.json','w') as f:
        json.dump(output,f,indent=2)
    print('survivors',len(survivors))
    print(json.dumps(survivors[:30]))


if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--limit',type=int,default=512)
    run(parser.parse_args().limit)
