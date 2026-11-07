#!/usr/bin/env python3
"""Meaningful positive and extraneous-sign tests of the generic isolator.

Constructed conic/canonical-coordinate fixtures are not original solutions.
Checks include exact domain-boundary roots and a 61-digit integer root.
"""
import hashlib
import json
from math import gcd
from pathlib import Path
from v20_fixed_parameter_solver import isolate,quartic_sign


def run():
    records=[]
    for n,r in [(104,340),(121,400),(1000,3200),(10**60+1,31*(10**59)+3)]:
        common=gcd(r*r,n*(n-1));c=n*(n-1)//common;h=r*r//common
        assert 9*c<h and 927*h<10400*c
        N=n*n+2
        for branch,eps in [('small',0),('complement',1)]:
            T=(r-eps)**2-9*n*n-6*n-10
            assert T>0
            G=gcd(N,T);J=T//G
            found=isolate(c,h,J,G,branch)
            assert found['root']==n
            records.append({'case':'positive_root','n':n,'r':r,'c':c,'h':h,'J':J,'G':G,
                            'branch':branch,'isolation':found})
        # Squaring would introduce this n, but its L(n) is negative.
        T=(r+1)**2-9*n*n-6*n-10;G=gcd(N,T);J=T//G
        L=(h-9*c)*n*n-(h+6*c)*n-c*(J*G+9)
        assert L==-2*c*r and L*L==4*c*h*n*(n-1)
        found=isolate(c,h,J,G,'complement')
        assert found['root']!=n and quartic_sign(n,c,h,J,G)==-1
        records.append({'case':'negative_sign_extraneous_root','n':n,'r':r,'c':c,'h':h,
                        'J':J,'G':G,'L':L,'isolation':found})
    result={'status':'PASS','positive_integer_roots_recovered':8,
            'negative_sign_quartic_roots_correctly_rejected':4,
            'includes_n104_domain_boundary':True,'largest_positive_n_digits':61,
            'records':records,'scope':'Isolator validation fixtures, not original binomial solutions',
            'solver_sha256':hashlib.sha256(Path(__file__).with_name('v20_fixed_parameter_solver.py').read_bytes()).hexdigest(),
            'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='records'},indent=2))


if __name__=='__main__':run()
