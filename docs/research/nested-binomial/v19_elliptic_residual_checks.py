#!/usr/bin/env python3
"""Exact checks and finite Runge certificate for v19 residual geometry.

No floating point, Lean invocation, or rank assumption is used.  The complete
domain for 1 <= rho <= 10 comes from v18's PROVED a < rho(rho+32b^2).
"""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path


class P:
    """Sparse integer polynomial in (a,b,rho), independent coefficient check."""
    def __init__(self, terms=0):
        if isinstance(terms, P):
            terms = terms.d
        if isinstance(terms, int):
            terms = {(0, 0, 0): terms}
        self.d = {e: c for e, c in terms.items() if c}

    def __add__(self, other):
        out = self.d.copy()
        for e, c in P(other).d.items():
            out[e] = out.get(e, 0) + c
        return P(out)

    __radd__ = __add__

    def __neg__(self):
        return P({e: -c for e, c in self.d.items()})

    def __sub__(self, other):
        return self + -P(other)

    def __rsub__(self, other):
        return P(other) + -self

    def __mul__(self, other):
        out = {}
        for e, c in self.d.items():
            for f, d in P(other).d.items():
                z = tuple(x + y for x, y in zip(e, f))
                out[z] = out.get(z, 0) + c * d
        return P(out)

    __rmul__ = __mul__

    def __pow__(self, n):
        out = P(1)
        for _ in range(n):
            out = out * self
        return out


def f(a, b, r):
    return (4*a**6 + (24*b*b-12*r)*a**4
            + (36*b**4+60*b*b*r+12*r*r)*a*a - 3*b*b*r*r-4*r**3)


def coefficient_checks():
    a, b, r = [P({tuple(int(i == j) for i in range(3)): 1}) for j in range(3)]
    checks = []

    def same(label, lhs, rhs):
        assert not (lhs-rhs).d, label
        checks.append(label)

    F = f(a, b, r)
    A = 48*b*b*(9*r-b*b)
    B = 1296*r*r*b*b-2880*r*b**4-128*b**6
    X = 4*a*a+8*b*b-4*r
    same('fixed_b_rho_map', X**3+A*X+B, 16*F)
    same('fixed_b_rho_discriminant', -16*(4*A**3+27*B**2),
         -995328*r*b**4*(9*r+8*b*b)**3)
    tx, ty = 12*b*b, 4*b*(9*r+8*b*b)
    same('T_on_curve', tx**3+A*tx+B, ty*ty)
    same('T_tangent_slope', 3*tx*tx+A, 12*b*ty)
    same('T_flex', (a+tx)**3+A*(a+tx)+B-(ty+6*b*a)**2, a**3)
    same('T_boundary', f(a,b,a*a-b*b), b*b*(9*a*a-b*b)**2)
    c2, c1, c0 = 24*b*b-12*r, 36*b**4+60*b*b*r+12*r*r, -3*b*b*r*r-4*r**3
    cubic_disc = c2*c2*c1*c1-16*c1**3-4*c2**3*c0-432*c0*c0+72*c2*c1*c0
    same('quotient_cubic_discriminant', cubic_disc,
         -3888*r*b**4*(9*r+8*b*b)**3)
    Aa = -3*b*b*(72*a*a+b*b)
    Ba = 2*b*b*(648*a**4+180*a*a*b*b-b**4)
    Xa = 4*a*a-b*b-4*r
    same('fixed_a_b_map', Xa**3+Aa*Xa+Ba, 16*F)
    same('fixed_a_b_c4', -48*Aa, 144*b*b*(72*a*a+b*b))
    same('fixed_a_b_discriminant', -16*(4*Aa**3+27*Ba**2),
         -995328*a*a*b**4*(3*a-b)**3*(3*a+b)**3)
    sx, sy = 3*b*b, 4*b*(9*a*a-b*b)
    same('S_on_curve', sx**3+Aa*sx+Ba, sy*sy)
    same('S_tangent_slope', 3*sx*sx+Aa, -6*b*sy)
    same('S_flex', (r+sx)**3+Aa*(r+sx)+Ba-(sy-3*b*r)**2, r**3)
    same('v18_Runge_remainder', F-(2*a**3+(6*b*b-3*r)*a)**2,
         3*r*(r+32*b*b)*a*a-r*r*(3*b*b+4*r))
    return checks


def mod5_check():
    residues = []
    for z in (0, 1, 4):
        value = (4*z**3+2*z*z+3*z+3) % 5
        assert value not in (0, 1, 4)
        residues.append({'a2_over_b2': z, 'F_over_b6': value})
    # Also verify the normalized assertion against all nonzero b mod 5.
    for a in range(5):
        for b in range(1, 5):
            assert f(a,b,b*b % 5) % 5 not in (0,1,4)
    return residues


def reconstruct(a, b, r, y):
    result = []
    for sign in (-1, 1):
        t = Fraction(2*a*(a*a+3*b*b)-r*(3*b+2*a)+sign*y, 2*b*r)
        n = (b*b*(t*t+3*t+3)+a*b*(t+6)-a*a+r)/(9*a*b)
        if t.denominator != 1:
            disposition = 't_not_integer'
        elif t < 4:
            disposition = 't_below_4'
        elif n.denominator != 1:
            disposition = 'n_not_integer'
        elif n < 104:
            disposition = 'n_below_104'
        elif n <= 3*t:
            disposition = 'coarse_interval_fails'
        else:
            ni = int(n)
            M = gcd(ni,3)*gcd(ni-1,6)
            disposition = 'denominator_fails' if (81*M) % b else 'survivor'
        assert disposition != 'survivor', (a,b,r,y,t,n)
        result.append({'sign':sign,'t':str(t),'n':str(n),'disposition':disposition})
    return result


def finite_certificate():
    bs = (1,2,3,6,9,18,27,54,81,162,243,486)
    rows, points = [], []
    for r in range(1,11):
        for b in bs:
            classes = [a for a in range(b) if gcd(a,b)==1 and (a*a-r) % b == 0]
            if not classes:
                continue
            # Original-equation range: v17 h >= 93M, hence 27a >= 31b.
            lo = max(b+1, (31*b+26)//27)
            hi = r*(r+32*b*b)-1  # v18 strict, proof-derived upper bound
            row = {'b':b,'rho':r,'lower_a':lo,'upper_a':hi,'classes_mod_b':classes,
                   'candidates':0,'square_tests':0,'squares':0,
                   'uniform_mod5_obstruction':(r-b*b)%5==0}
            for ar in classes:
                first = lo+(ar-lo) % b
                for a in range(first,hi+1,b):
                    if 1377*r >= 216*a*a+760*b*b:
                        continue
                    row['candidates'] += 1
                    if row['uniform_mod5_obstruction']:
                        continue
                    F = f(a,b,r)
                    assert F > 0
                    row['square_tests'] += 1
                    y = isqrt(F)
                    if y*y != F:
                        continue
                    row['squares'] += 1
                    assert (4*y)**2 == ((4*a*a+8*b*b-4*r)**3
                        +48*b*b*(9*r-b*b)*(4*a*a+8*b*b-4*r)
                        +1296*r*r*b*b-2880*r*b**4-128*b**6)
                    points.append({'a':a,'b':b,'rho':r,'y':y,
                                   'roots':reconstruct(a,b,r,y)})
            rows.append(row)
    expected = {(13,2,1,4674),(7,1,4,660),(7,2,7,798),(4,3,7,405),(10,3,10,2430)}
    assert {(p['a'],p['b'],p['rho'],p['y']) for p in points} == expected
    return {'rho_domain':[1,10],'denominators':list(bs),'curves':len(rows),
            'mod5_blocked_curves':sum(r['uniform_mod5_obstruction'] for r in rows),
            'candidates':sum(r['candidates'] for r in rows),
            'square_tests':sum(r['square_tests'] for r in rows),
            'square_discriminants':len(points),'survivors':0,
            'rows':rows,'points':points}


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    here = Path(__file__).resolve().parent
    bindings = {'checker_sha256':sha(Path(__file__))}
    for name in ('v17_square_root_gap.md','v18_residual_gap.md','v19_elliptic_residual.md'):
        p = here/name
        if not p.exists():
            p = here.parents[1]/'mathos/docs/research/nested-binomial'/name
        if p.exists():
            bindings[name] = sha(p)
    result = {'status':'PASS','evidence':'written identities and exact finite certificate; no Lean',
              'coefficient_identities':coefficient_checks(),'mod5_table':mod5_check(),
              'certificate':finite_certificate(),'sha256':bindings}
    dest = here/'v19_elliptic_residual_checks.json'
    dest.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'identities':len(result['coefficient_identities']),
        **{k:v for k,v in result['certificate'].items() if k not in ('rows','points','denominators')},
        'report':str(dest)},ensure_ascii=False,indent=2))


if __name__ == '__main__':
    main()
