#!/usr/bin/env python3
"""Independent rank-proof review checks by exact interpolation uniqueness.

All polynomial differences below have degree at most 12 in each variable.
Vanishing on the full 13x13 Cartesian grid therefore proves those polynomial
identities, rather than merely sampling them. The uniform torsion argument
is reviewed in the companion Markdown file, not replaced by this grid.
"""
import hashlib
import json
from fractions import Fraction
from pathlib import Path


def main():
    base = Path(__file__).resolve().parent
    source_base = base if (base/'v19_residual_positive_rank.md').exists() else base.parent/'rank'
    note = source_base/'v19_residual_positive_rank.md'
    checker = source_base/'v19_residual_positive_rank_checks.py'
    for a in range(13):
        for b in range(13):
            A = -3*b*b*(72*a*a+b*b)
            B = 2*b*b*(648*a**4+180*a*a*b*b-b**4)
            x,y = 4*a*a-b*b,8*a*(a*a+3*b*b)
            assert y*y == x**3+A*x+B
            assert 3*x*x+A == 48*a*a*(a*a-5*b*b)
            assert -16*(4*A**3+27*B**2) == -995328*a*a*b**4*(3*a-b)**3*(3*a+b)**3
            x3,y3 = 3*b*b,4*b*(9*a*a-b*b)
            assert y3*y3 == x3**3+A*x3+B
            assert 3*x3*x3+A == -6*b*y3
    exA,exB,x,y=-1947,108214,35,288
    slope=Fraction(3*x*x+exA,2*y)
    xx=slope*slope-2*x
    yy=slope*(x-xx)-y
    assert (slope,xx,yy)==(3,-61,0)
    assert xx**3+exA*xx+exB==0
    result={'status':'PASS','review':'written uniform proof independently read; no logical gap found',
            'polynomial_method':'13x13 exact grid plus degree <=12 in each variable',
            'polynomial_identities':5,'grid_points':169,
            'exception_P0':[35,288],'exception_double':[-61,0],
            'checked_logic':['Nagell-Lutz applies without minimality',
                'P0 has nonzero y, so its double is affine',
                'rational lambda with integral square is integral',
                'gcd(a,b)=1 justifies d|24a',
                'primes >=5 excluded by gcd(d,a)|3',
                'v2(d) in {0,2}, v3(d) in {0,1}',
                'd|12 plus a>b gives only (3,1)',
                'exception is order4 and its only positive residual is nonsquare'],
            'sources':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (note,checker,Path(__file__))},
            'scope':'written proof + exact integer verification; no new Lean or API execution'}
    (base/'v19_uniform_rank_independent_review.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
