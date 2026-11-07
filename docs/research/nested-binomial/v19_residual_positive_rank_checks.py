#!/usr/bin/env python3
"""Exact coefficient and exceptional-point checks for the written rank proof.

Standard library only. This is not a bounded search masquerading as a
uniform proof: the uniform argument is written in the companion note.
"""
from fractions import Fraction
from hashlib import sha256
from math import gcd
from pathlib import Path
import argparse
import json


def const(n):
    return {(0, 0): n} if n else {}


def add(*ps):
    out = {}
    for p in ps:
        for term, c in p.items():
            out[term] = out.get(term, 0) + c
    return {term: c for term, c in out.items() if c}


def scale(p, c):
    return {term: c*v for term, v in p.items() if c*v}


def mul(p, q):
    out = {}
    for (a, b), c in p.items():
        for (d, e), f in q.items():
            term = (a+d, b+e)
            out[term] = out.get(term, 0) + c*f
    return {term: c for term, c in out.items() if c}


def power(p, e):
    out = const(1)
    for _ in range(e):
        out = mul(out, p)
    return out


def value(p, a, b):
    return sum(c*a**i*b**j for (i,j), c in p.items())


def verify(output):
    a, b = {(1,0): 1}, {(0,1): 1}
    a2, b2 = power(a,2), power(b,2)
    A = scale(mul(b2,add(scale(a2,72),b2)),-3)
    B = scale(mul(b2,add(scale(power(a,4),648),
                          scale(mul(a2,b2),180),scale(power(b,4),-1))),2)
    x = add(scale(a2,4),scale(b2,-1))
    d = add(a2,scale(b2,3))
    y = scale(mul(a,d),8)
    checks = {}
    def identity(name, p):
        assert p == {}, (name,p)
        checks[name] = True
    identity('P0_lies_on_curve',add(power(y,2),scale(power(x,3),-1),
                                   scale(mul(A,x),-1),scale(B,-1)))
    disc = scale(add(scale(power(A,3),4),scale(power(B,2),27)),-16)
    expected = scale(mul(mul(a2,power(b,4)),
                         mul(power(add(scale(a,3),scale(b,-1)),3),
                             power(add(scale(a,3),b),3))),-995328)
    identity('discriminant_factorization',add(disc,scale(expected,-1)))
    tangent_numerator = add(scale(power(x,2),3),A)
    identity('P0_tangent_numerator',add(tangent_numerator,
              scale(mul(a2,add(a2,scale(b2,-5))),-48)))
    x3 = scale(b2,3)
    y3 = scale(mul(b,add(scale(a2,9),scale(b2,-1))),4)
    identity('P3_lies_on_curve',add(power(y3,2),scale(power(x3,3),-1),
                                   scale(mul(A,x3),-1),scale(B,-1)))
    identity('P3_tangent_slope',add(scale(power(x3,2),3),A,
                                  scale(mul(b,y3),6)))
    identity('P3_doubled_x_equals_original',add(scale(b2,9),scale(x3,-3)))

    # Check complete residue classes needed by the written valuations.
    mod8_count = mod9_count = 0
    for av in range(8):
        for bv in range(8):
            if av % 2 == bv % 2 == 0:
                continue
            dv = av*av+3*bv*bv
            if av % 2 and bv % 2:
                assert dv % 8 == 4
            else:
                assert dv % 2 == 1
            mod8_count += 1
    for av in range(9):
        for bv in range(9):
            if av % 3 == bv % 3 == 0:
                continue
            dv = av*av+3*bv*bv
            if av % 3 == 0:
                assert dv % 9 == 3
            else:
                assert dv % 3 == 1
            mod9_count += 1

    av,bv = 3,1
    exA,exB = value(A,av,bv),value(B,av,bv)
    exx,exy = value(x,av,bv),value(y,av,bv)
    slope = Fraction(3*exx*exx+exA,2*exy)
    dx = slope*slope-2*exx
    dy = slope*(exx-dx)-exy
    assert (exA,exB)==(-1947,108214)
    assert (exx,exy,slope,dx,dy)==(35,288,3,-61,0)
    assert dx**3+exA*dx+exB==0
    assert Fraction(2704,1377)<2
    rho=1
    F=4*av**6+24*av**4*bv**2-12*av**4*rho+36*av**2*bv**4
    F+=60*av**2*bv**2*rho+12*av**2*rho*rho-3*bv*bv*rho*rho-4*rho**3
    assert F==4853 and 69**2<F<70**2
    # Complete finite conclusion only after the proved d|12 reduction.
    exceptions=[(aa,bb) for aa in range(2,4) for bb in range(1,aa)
                if gcd(aa,bb)==1 and 12%(aa*aa+3*bb*bb)==0]
    assert exceptions==[(3,1)]
    note=Path(__file__).with_name('v19_residual_positive_rank.md')
    result={'status':'PASS','polynomial_identities':checks,
            'mod8_classes':mod8_count,'mod9_classes':mod9_count,
            'possible_torsion_exception':exceptions,
            'exception_P0':[exx,exy],'exception_2P0':[int(dx),int(dy)],
            'exception_point_exact_order':4,'exception_residual_F':F,
            'uniform_proof':'Nagell-Lutz plus d|24a and exact 2/3-adic classification; see companion note',
            'formalization':'No new Lean execution',
            'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'note_sha256':sha256(note.read_bytes()).hexdigest()}
    output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('v19_residual_positive_rank_checks.json'))
    verify(parser.parse_args().output)
