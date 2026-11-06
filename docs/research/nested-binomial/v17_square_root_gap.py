#!/usr/bin/env python3
"""Complete exact certificate for the region (r-3n)^2 <= 9n.

The proof first restricts the reduced fraction h/(81M)=a/b to b|486,
27a<31b, then bounds a positive integral residual j. No arbitrary n
cutoff, floating arithmetic, CAS integral-point solver, or Lean execution
is used. All finite arithmetic below uses the Python standard library.
"""

import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import json
from math import comb, gcd, isqrt
from pathlib import Path


class Poly:
    """Small exact polynomial ring Z[a,b,j,t] for coefficient identities."""
    def __init__(self, terms):
        if isinstance(terms, int):
            terms = {(0, 0, 0, 0): terms}
        self.terms = {e: c for e, c in terms.items() if c}

    @staticmethod
    def coerce(x):
        return x if isinstance(x, Poly) else Poly(x)

    def __add__(self, other):
        out = self.terms.copy()
        for e, c in self.coerce(other).terms.items():
            out[e] = out.get(e, 0) + c
        return Poly(out)

    __radd__ = __add__

    def __neg__(self):
        return Poly({e: -c for e, c in self.terms.items()})

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) + (-self)

    def __mul__(self, other):
        out = {}
        for e, c in self.terms.items():
            for f, d in self.coerce(other).terms.items():
                g = tuple(x + y for x, y in zip(e, f))
                out[g] = out.get(g, 0) + c * d
        return Poly(out)

    __rmul__ = __mul__

    def __pow__(self, power):
        assert power >= 0
        out = Poly(1)
        for _ in range(power):
            out = out * self
        return out


def coefficients(a, b, j):
    A = j * b * b
    B = j * (3 * b * b + 2 * a * b) - 2 * a * b * (a * a + 3 * b * b)
    C = (j * (3 * b * b + 3 * a * b - 2 * a * a + j)
         - a * (9 * b ** 3 + 21 * a * b * b + 3 * a * a * b - a ** 3))
    return A, B, C


def reduced_discriminant(a, b, j):
    return (4 * a ** 6 + 24 * a ** 4 * b ** 2 - 12 * a ** 4 * j
            + 36 * a ** 2 * b ** 4 + 60 * a ** 2 * b ** 2 * j
            + 12 * a ** 2 * j ** 2 - 3 * b ** 2 * j ** 2 - 4 * j ** 3)


def reconstruction_numerator(a, b, j, t):
    return b * b * (t * t + 3 * t + 3) + a * b * (t + 6) - a * a + j


def exact_algebra():
    a, b, j, t = (Poly({tuple(int(k == i) for k in range(4)): 1}) for i in range(4))
    A, B, C = coefficients(a, b, j)
    P = A * t * t + B * t + C
    F = reduced_discriminant(a, b, j)
    N = reconstruction_numerator(a, b, j, t)
    X = 4 * a * a - b * b - 4 * j
    EA = -3 * b * b * (72 * a * a + b * b)
    EB = 2 * b * b * (648 * a ** 4 + 180 * a * a * b * b - b ** 4)
    identities = {
        'reconstruction_equation': N * N - (9 * a * b + b * b * (t * t + 3 * t + 3)) * N - a * b ** 3 * t ** 3 - P,
        'quadratic_discriminant': B * B - 4 * A * C - b * b * F,
        'elliptic_coordinate_identity': 16 * F - (X ** 3 + EA * X + EB),
        'elliptic_discriminant': -16 * (4 * EA ** 3 + 27 * EB ** 2)
            + 995328 * a * a * b ** 4 * (3 * a - b) ** 3 * (3 * a + b) ** 3,
        # For this identity only, a denotes u=t+3 and b denotes n.
        'stronger_shifted_gap_expansion':
            (9*(a-3)**2+27*(a-3)+27)*b+(a-3)**3-93*b*(b-1)
            - ((9*a*a*b-93*b*b)+a**3+(120-27*a)*b-9*a*a+27*a-27),
    }
    for name, p in identities.items():
        assert not p.terms, name
    assert Fraction(2187, 68) * Fraction(32, 6561) == Fraction(8, 51)
    assert Fraction(2187, 68) * (96 + Fraction(448, 27)) == Fraction(61560, 17)
    assert Fraction(61560, 17 * 81 ** 2) == Fraction(760, 1377)
    assert 51 * 27 == 1377
    return {name: 'all integer coefficients zero' for name in identities}


def lucas(n, k, p):
    """Binomial residue via small exact math.comb values."""
    answer = 1
    while n or k:
        ni, ki = n % p, k % p
        if ki > ni:
            return 0
        answer = answer * comb(ni, ki) % p
        n //= p
        k //= p
    return answer


def branch_witnesses(n, r):
    A = comb(n, 3)
    out = []
    for branch, k in [('r', r), ('A-r', A-r)]:
        for p in [2, 3, 5, 7, 11, 13]:
            left = lucas(A, k, p)
            inner = lucas(n*n, (n-3)**2, p)
            square = pow(k, 2, p)
            right = (inner + square) % p
            if left != right:
                out.append({'branch': branch, 'k': k, 'prime': p, 'left': left,
                            'inner': inner, 'square': square, 'right': right})
                break
        else:
            raise AssertionError(('No modular witness', n, r, branch))
    return out


def run(output):
    identities = exact_algebra()
    bs = [b for b in range(1, 487) if 486 % b == 0]
    assert bs == [1, 2, 3, 6, 9, 18, 27, 54, 81, 162, 243, 486]
    stats = Counter()
    families = []
    all_integer_t = []
    restored = []
    for b in bs:
        for a in range(1, (31*b-1)//27 + 1):
            if gcd(a, b) != 1:
                continue
            stats['coefficient_pairs'] += 1
            maximum_j = (216*a*a + 760*b*b - 1)//1377
            first_j = a*a % b or b
            codes = []
            squares = []
            count = 0
            for j in range(first_j, maximum_j+1, b):
                stats['residual_values'] += 1
                count += 1
                F = reduced_discriminant(a, b, j)
                if F < 0:
                    codes.append('-')
                    continue
                y = isqrt(F)
                if y*y != F:
                    codes.append('.')
                    continue
                codes.append('s')
                stats['square_discriminants'] += 1
                A, B, C = coefficients(a, b, j)
                assert B*B - 4*A*C == b*b*F
                record = {'j': j, 'F': F, 'sqrt_F': y, 'roots': []}
                T = 2*a*(a*a+3*b*b) - j*(3*b+2*a)
                for numerator in sorted({T-y, T+y}):
                    denominator = 2*b*j
                    frac_t = Fraction(numerator, denominator)
                    root = {'t_numerator': frac_t.numerator, 't_denominator': frac_t.denominator}
                    if frac_t.denominator != 1:
                        root['disposition'] = 'nonintegral_t'
                    elif frac_t < 4:
                        root['disposition'] = 't_below_4'
                    else:
                        t = int(frac_t)
                        stats['integer_t_ge_4'] += 1
                        assert A*t*t+B*t+C == 0
                        frac_n = Fraction(reconstruction_numerator(a,b,j,t), 9*a*b)
                        root.update(n_numerator=frac_n.numerator, n_denominator=frac_n.denominator)
                        row = {'a': a, 'b': b, 'j': j, 't': t,
                               'n_numerator': frac_n.numerator, 'n_denominator': frac_n.denominator}
                        all_integer_t.append(row)
                        if frac_n.denominator != 1:
                            root['disposition'] = 'nonintegral_n'
                        elif frac_n < 104:
                            root['disposition'] = 'n_below_104'
                        else:
                            stats['integer_n_ge_104'] += 1
                            n = int(frac_n)
                            M = gcd(n,3)*gcd(n-1,6)
                            if 3*t >= n:
                                root['disposition'] = 'outside_coarse_interval'
                            elif 81*M % b:
                                root['disposition'] = 'wrong_actual_denominator'
                            else:
                                stats['restored_necessary_pairs'] += 1
                                r = 3*n+t
                                h = 81*M*a//b
                                Q = n*(n-1)//M
                                assert r**3 % Q == 0
                                assert h*n*(n-1) == M*((9*t*t+27*t+27)*n+t**3)
                                g = gcd(h,81*M)
                                assert (h//g,81*M//g) == (a,b)
                                J = 729*M*(h*n-h-M*(9*t*t+27*t+27))-81*M*h*(t-3)+h*h
                                assert J == g*g*j
                                assert 17*b*(t+3) < 27*a*(2*a*a+3*a*b+6*b*b)
                                assert 289*b*n < 84*a*(2*a*a+3*a*b+6*b*b)**2
                                delta = Q//gcd(Q,r*r)
                                # This is an observed output of the complete enumeration,
                                # checked exactly, not imposed as a candidate filter.
                                assert t*t == 9*n
                                stats['equality_pairs'] += 1
                                assert 6 % delta == 0
                                root['disposition'] = 'equality_candidate'
                                witnesses = branch_witnesses(n,r)
                                stats['original_branch_exclusions'] += len(witnesses)
                                restored.append({'a':a,'b':b,'j':j,'t':t,'n':n,'r':r,'M':M,
                                                 'h':h,'delta':delta,'witnesses':witnesses})
                    record['roots'].append(root)
                squares.append(record)
            families.append({'a':a,'b':b,'first_j':first_j,'maximum_j':maximum_j,
                             'step':b,'count':count,'classifications':''.join(codes),
                             'square_records':squares})
    restored.sort(key=lambda z:z['n'])
    ss = [isqrt(z['n']) for z in restored]
    expected_s = [s for s in range(11,650) if 324*gcd(s-1,2) % (s-1) == 0]
    assert ss == expected_s == [13,19,25,28,37,55,73,82,109,163,217,325,649]
    assert all(z['r'] == 3*s*(s+1) for z,s in zip(restored,ss))
    # h<=81M is a subset of the same complete coefficient domain.
    low_h_candidates = [z for z in restored if z['a'] <= z['b']]
    assert not low_h_candidates
    low_h = {'coefficient_pairs': sum(f['a']<=f['b'] for f in families),
             'residual_values': sum(f['count'] for f in families if f['a']<=f['b']),
             'square_discriminants': sum(len(f['square_records']) for f in families if f['a']<=f['b']),
             'integer_t_ge_4': sum(z['a']<=z['b'] for z in all_integer_t),
             'integer_n_ge_104': sum(z['a']<=z['b'] and z['n_denominator']==1 and z['n_numerator']>=104 for z in all_integer_t)}
    assert low_h == {'coefficient_pairs':486,'residual_values':80274,'square_discriminants':199,
                     'integer_t_ge_4':17,'integer_n_ge_104':0}
    assert dict(stats) == {'coefficient_pairs':557,'residual_values':94710,'square_discriminants':272,
                          'integer_t_ge_4':30,'integer_n_ge_104':13,'restored_necessary_pairs':13,
                          'equality_pairs':13,'original_branch_exclusions':26}
    here = Path(__file__).resolve().parent
    report = {
        'status':'PASS',
        'scope':'ell=1, j=i-3 in the original squared-index equation; both k branches',
        'old_necessary_inputs':'n>=104, M=gcd(n,3)*gcd(n-1,6), Q=n(n-1)/M divides r^3, 3n<r<10n/3',
        'theorems':[
            'The old necessary inputs imply (r-3n)^2>=9n.',
            'Equality in the old inputs holds for exactly the 13 listed s with n=s^2, r=3s(s+1).',
            'For the original binomial equation, r>3n+3*sqrt(n).',
            'The old necessary inputs imply h>81M; h=81M+1 is attained by n=421201,r=1265550,M=6.',
            'For the original binomial equation, h>=93M and r-3n+3>sqrt(31*n/3).' 
        ],
        'boundary_reduction':'t<=3*sqrt(n) implies h/M<=81+108/(sqrt(n)-1)<93, hence 27a<31b',
        'definitions':{'h':'M*((9t^2+27t+27)*n+t^3)/(n*(n-1))','a/b':'h/(81*M) in lowest terms',
                       'g':'gcd(h,81*M)','j':'J/g^2; J is the positive v16 residual'},
        'complete_denominators':bs,
        'coefficient_domain':'a>=1, b|486, gcd(a,b)=1, 27*a<31*b',
        'residual_domain':'j>=1, j=a^2 mod b, 1377*j<216*a^2+760*b^2',
        'polynomial_height':{'t_plus_3':'<27*a*(2*a^2+3*a*b+6*b^2)/(17*b)',
                             'n':'<84*a*(2*a^2+3*a*b+6*b^2)^2/(289*b)'},
        'exact_algebra':identities,
        'statistics':dict(stats),
        'classification_codes':{'-':'negative reduced discriminant','.':'nonsquare reduced discriminant',
                                's':'square reduced discriminant; full roots recorded'},
        'families':families,
        'integer_t_records':all_integer_t,
        'necessary_pairs':restored,
        'elementary_equality_s':ss,
        'low_h_subdomain':low_h,
        'original_equation_survivors':[],
        'max_witness_prime':max(w['prime'] for z in restored for w in z['witnesses']),
        'both_binomials_zero_witnesses':sum(w['left']==0 and w['inner']==0 for z in restored for w in z['witnesses']),
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'proof_note_sha256':hashlib.sha256((here/'v17_square_root_gap.md').read_bytes()).hexdigest(),
        'verification_boundary':{'written_reduction_plus_complete_finite_integer_certificate':True,
                                 'finite_extrapolation':False,'new_lean_execution':False,
                                 'new_deepseek_api_calls':0,'complete_CAS_solver':False,
                                 'original_solutions_found':False}
    }
    assert report['both_binomials_zero_witnesses']==24
    output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ['status','statistics','low_h_subdomain','max_witness_prime',
                                          'source_sha256','proof_note_sha256']},indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('v17_square_root_gap_results.json'))
    args = parser.parse_args()
    run(args.output)
