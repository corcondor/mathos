#!/usr/bin/env python3
"""v60: combine the two multiplicative bad-reduction factors to rule out
rational 9-/12-torsion for any fixed positive rho and b|486.

For p>=5 | rho, e=v_p(rho): N | e*(p-chi(-3,p)).
For p>=5 | 8b²+9rho, h=v_p(8b²+9rho): N | 3h*(p-1).
N=9 or 12. Rank zero and torsion restricted to 3,6 then implies no
original-branch integer solution by v50/v56. Positive-rank points remain open.
"""
import argparse
import json
import sympy as sp
from math import gcd

BS=(1,2,3,6,9,18,27,54,81,162,243,486)
assert BS==tuple(x for x in range(1,487) if 486%x==0)

def sieved(rho,b):
    assert rho>0 and b in BS
    rs=sp.factorint(rho)
    ms=sp.factorint(8*b*b+9*rho)
    excluded={9:[],12:[]}
    witnesses=[]
    for category,factors in (("rho",rs),("8b2+9rho",ms)):
        for P,exp in factors.items():
            p=int(P); e=int(exp)
            if p<5:continue
            assert sp.isprime(p)
            if category=="rho":
                chi=int(sp.legendre_symbol(-3,p))
                smooth=p-chi
                component=e
            else:
                smooth=p-1
                component=3*e
            assert gcd(p,b)==1
            entry=dict(factor=category,p=p,valuation=e,smooth_order=smooth,
                       component_bound=component)
            witnesses.append(entry)
            for n in (9,12):
                if (component*smooth)%n!=0:
                    excluded[n].append(entry)
    poss=[3,6]+[n for n in (9,12) if not excluded[n]]
    return {"rho":rho,"b":b,"first_torsion_possible":poss,
            "9_excluded_by":excluded[9],"12_excluded_by":excluded[12],
            "local_factors":witnesses,
            "rank_zero_original_solution_possible":any(n in poss for n in (9,12)),
            "IMPORTANT":"a local necessary sieve, NOT a complete rational-point classification"}

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("rho",nargs="?",type=int,default=100003)
    ap.add_argument("--b",type=int,default=None)
    opts=ap.parse_args()
    data=[sieved(opts.rho,b) for b in (BS if opts.b is None else (opts.b,))]
    if opts.rho==100003 and opts.b is None:
        assert len(data)==12
        assert all(d["first_torsion_possible"]==[3,6] for d in data)
        assert all(not d["rank_zero_original_solution_possible"] for d in data)
    if opts.rho==17 and opts.b in (None,1):
        assert data[0]["first_torsion_possible"]==[3,6]
        assert any(x["p"]==23 and x["factor"]=="8b2+9rho"
                   for x in data[0]["9_excluded_by"])
    print(json.dumps(data,indent=2,ensure_ascii=False))
    print("PASS: p-adic component and smooth-group orders checked for every factor")
    print("LIMIT: rank-positive rational points still require separate Mordell-Weil analysis")
