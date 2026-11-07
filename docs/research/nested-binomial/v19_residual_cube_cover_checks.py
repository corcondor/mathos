#!/usr/bin/env python3
"""Exact residual 3-cover identities and complete finite-field audit.

The sign Z>0 is inherited from the v17 square-root gap.  The bounded
negative-Z audit is an independent check under weaker residual hypotheses,
NOT an improvement of that original necessary condition.  No Lean, API,
ECDLP, full Mordell-Weil basis, or Selmer computation is claimed.
"""
from __future__ import annotations

import hashlib
import itertools
import json
from collections import Counter
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
BS = [d for d in range(1, 487) if 486 % d == 0]
PRIMES = [p for p in range(5, 62) if all(p % d for d in range(2, isqrt(p) + 1))]


def sha_bytes(data):
    return hashlib.sha256(data).hexdigest()


def encoded(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode()


def f(a, b, rho):
    return (4*a**6 + (24*b*b-12*rho)*a**4
            + (36*b**4+60*b*b*rho+12*rho*rho)*a*a
            - 3*b*b*rho*rho - 4*rho**3)


def identities():
    a, b, rho, Z = sp.symbols("a b rho Z")
    z = a*a-b*b-rho
    L = 6*a*a+2*b*b+3*rho
    checks = {}
    checks["unscaled_factorization"] = sp.expand(f(a,b,rho)-b*b*L*L-4*z**3) == 0
    rn = a*a-b*b-b*Z
    Ln = 9*a*a-b*b-3*b*Z
    checks["normalized_factorization"] = sp.expand(f(a,b,rn)-b*b*(Ln*Ln+4*b*Z**3)) == 0
    n, t = sp.symbols("n t")
    K = (9*t*t+27*t+27)*n+t**3
    checks["sign_elimination_identity"] = sp.expand(
        81*n*(n-1)*(t+1)*(t+2)+K*(t+6-9*n)
        -(t*t-9*n)*(9*n+t*t+6*t)) == 0
    al, be, ga, u, v = sp.symbols("alpha beta gamma u v")
    D = 9*a*a-b*b
    U, V = al*u**3, be*v**3
    rc = a*a-b*b-ga*u*v
    Lc = D-3*ga*u*v
    H = V-U+3*ga*u*v-D
    R = ga**3-al*be*b*b
    checks["cover_ideal_membership"] = sp.expand(
        f(a,b,rc)-b*b*(U+V)**2+b*b*(Lc+V-U)*H-4*u**3*v**3*R) == 0
    # The normalized genus-two fiber discriminant is used only for the
    # written all-primes limitation theorem, not the finite exclusion.
    x, s = sp.symbols("x s")
    ff = f(x, 1, s)
    checks["sextic_discriminant"] = sp.factor(sp.discriminant(ff,x)) == (
        3869835264*s**4*(4*s+3)*(9*s+8)**6)
    checks["singular_s_zero"] = sp.expand(ff.subs(s,0)-4*x*x*(x*x+3)**2) == 0
    checks["singular_s_minus_8_9"] = sp.expand(
        ff.subs(s,-sp.Rational(8,9))-4*(3*x-1)**2*(3*x+1)**2*(9*x*x+80)/729) == 0
    checks["singular_s_minus_3_4"] = sp.expand(
        ff.subs(s,-sp.Rational(3,4))-x*x*(16*x**4+132*x*x-9)/4) == 0
    assert all(checks.values())
    return checks


def add(P, Q, A, p):
    if P is None:
        return Q
    if Q is None:
        return P
    x, y = P
    xx, yy = Q
    if x == xx and (y+yy) % p == 0:
        return None
    if P == Q:
        lam = (3*x*x+A)*pow(2*y,-1,p) % p
    else:
        lam = (yy-y)*pow(xx-x,-1,p) % p
    xxx = (lam*lam-x-xx) % p
    return xxx, (lam*(x-xxx)-y) % p


def local_tables():
    rows = []
    for p in PRIMES:
        squares = {j*j % p for j in range(p)}
        fibers = []
        for s in range(p):
            A, B = 48*(9*s-1) % p, (1296*s*s-2880*s-128) % p
            good = (4*A**3+27*B*B) % p != 0
            assert good == (s*(9*s+8) % p != 0)
            allowed = [q for q in sorted(squares)
                       if (4*q**3+(24-12*s)*q*q+(36+60*s+12*s*s)*q-3*s*s-4*s**3) % p in squares]
            point_count = 1
            for x in range(p):
                vv = (x**3+A*x+B) % p
                point_count += 1 if vv == 0 else 2 if vv in squares else 0
            T = (12 % p, 4*(9*s+8) % p)
            if good:
                assert (T[1]*T[1]-T[0]**3-A*T[0]-B) % p == 0
                assert add(add(T,T,A,p),T,A,p) is None
                assert add(T,T,A,p) != T and T is not None
                assert point_count % 3 == 0
            fibers.append({"s":s, "allowed_a2_over_b2":allowed,
                           "elliptic_good_reduction":good,
                           "elliptic_point_count_with_infinity":point_count,
                           "known_T_order":3 if good else None})
        empty = [row["s"] for row in fibers if not row["allowed_a2_over_b2"]]
        assert empty == ([1] if p == 5 else [])
        rows.append({"prime":p,"fibers":fibers,"empty_affine_genus_two_fibers":empty})
    return {"scope":"Complete residue tables for normalized a/b and rho/b^2; b invertible.",
            "table_primes":PRIMES,"rows":rows,
            "global_limitation":"The note proves that no prime p>=7 excludes a whole rho/b^2 fiber by this mod-p test alone. This does not assert p-adic or global solubility."}


def reconstruct(a, b, rho, y):
    out = []
    for sign in (-1, 1):
        t = Fraction(2*a*(a*a+3*b*b)-rho*(3*b+2*a)+sign*y, 2*b*rho)
        n = (b*b*(t*t+3*t+3)+a*b*(t+6)-a*a+rho)/(9*a*b)
        out.append({"sign":sign,"t":str(t),"n":str(n)})
    return out


def bounded_sign_audit():
    families = []
    witness_histogram = Counter()
    prior_mod5_excluded = 0
    for b in BS:
        lo = max(b+1, (31*b+26)//27)
        hi = isqrt((2137*b*b-1)//1161)
        for a in range(lo,hi+1):
            if gcd(a,b) != 1:
                continue
            zmin = (1161*a*a-2137*b*b)//(1377*b)+1
            entries = []
            for Z in range(zmin,0):
                rho = a*a-b*b-b*Z
                assert rho > 0 and 1377*rho < 216*a*a+760*b*b
                L = 9*a*a-b*b-3*b*Z
                v = L*L+4*b*Z**3
                assert b*b*v == f(a,b,rho)
                prior_mod5_excluded += (rho-b*b) % 5 == 0
                witnesses = [p for p in PRIMES if rho*(9*rho+8*b*b) % p != 0
                             and pow(v%p,(p-1)//2,p) == p-1]
                assert witnesses, (a,b,Z)
                p = witnesses[0]
                witness_histogram[p] += 1
                entries.append([Z,p,v%p])
            rho = a*a-b*b
            y = b*(9*a*a-b*b)
            roots = reconstruct(a,b,rho,y)
            assert Fraction(roots[0]["t"]) < 0
            assert Fraction(roots[1]["n"]) <= 100
            assert Fraction(roots[1]["t"])**2 == 9*Fraction(roots[1]["n"])
            families.append({"a":a,"b":b,"Z_min":zmin,"negative_Z_witnesses":entries,
                             "Z_zero_roots":roots})
    negative_count = sum(len(x["negative_Z_witnesses"]) for x in families)
    assert len(families) == 102 and negative_count == 6221
    assert prior_mod5_excluded == 1252
    return {"role":"Independent finite-field reconstruction audit under weaker residual inputs; sign already follows directly from v17.",
            "coefficient_families":len(families),"negative_Z_cases":negative_count,
            "Z_zero_cases":len(families),"total_cases":negative_count+len(families),
            "prior_whole_fiber_mod5_exclusions":prior_mod5_excluded,
            "joint_local_sieve_exclusions":negative_count,"remaining_negative_Z":0,
            "all_witnesses_good_reduction":True,"largest_witness_prime":max(witness_histogram),
            "witness_prime_histogram":dict(sorted(witness_histogram.items())),"families":families}


def factor(n):
    out = {}
    p = 2
    while p*p <= n:
        while n % p == 0:
            out[p] = out.get(p,0)+1
            n //= p
        p += 1 if p == 2 else 2
    if n > 1:
        out[n] = out.get(n,0)+1
    return out


def icbrt(n):
    lo, hi = 0, 1
    while hi**3 <= n:
        hi *= 2
    while hi-lo > 1:
        mi = (lo+hi)//2
        if mi**3 <= n:
            lo = mi
        else:
            hi = mi
    return lo


def core(n):
    fac = factor(n)
    a = 1
    for p, e in fac.items():
        a *= p**(e % 3)
    u = icbrt(n//a)
    assert a*u**3 == n
    return a,u


def cover_coefficients(a,b):
    S = sorted(factor(b*(9*a*a-b*b)))
    bf = factor(b)
    rows = []
    for aa in itertools.product(range(3), repeat=len(S)):
        al = be = ga = 1
        for p,i in zip(S,aa):
            e = bf.get(p,0)
            j = (-i-2*e) % 3
            al *= p**i
            be *= p**j
            ga *= p**((i+j+2*e)//3)
        assert ga**3 == al*be*b*b
        rows.append([al,be,ga])
    assert len(rows) == len(set(map(tuple,rows))) == 3**len(S)
    return S,rows


def examples():
    out=[]
    for a,b,rho in [(13,2,1),(6469,486,501997),(2551,243,52792)]:
        y=isqrt(f(a,b,rho))
        assert y*y == f(a,b,rho) and y%b == 0
        Z=(a*a-b*b-rho)//b
        assert a*a-b*b-rho == b*Z and Z>0
        L=9*a*a-b*b-3*b*Z
        assert (y//b-L)%2 == 0
        U,V=(y//b-L)//2,(y//b+L)//2
        assert U>0 and V>0 and U*V == b*Z**3
        al,u=core(U);be,v=core(V);ga=icbrt(al*be*b*b)
        assert ga**3==al*be*b*b
        assert ga*u*v==b*Z
        assert be*v**3-al*u**3+3*ga*u*v==9*a*a-b*b
        assert b*(Z**3+3*Z)>=9*a*a-b*b+1
        S,classes=cover_coefficients(a,b)
        assert [al,be,ga] in classes
        out.append({"a":a,"b":b,"rho":rho,"y":y,"Z":Z,"L":L,"U":U,"V":V,
                    "support":S,"cover_count":len(classes),
                    "cover_coefficients_sha256":sha_bytes(encoded(classes)),
                    "alpha":al,"beta":be,"gamma":ga,"u":u,"v":v,
                    "reconstruction":reconstruct(a,b,rho,y),
                    "warning":"Auxiliary residual point only; not a solution of the original binomial equation."})
    return out


def main():
    tables=local_tables()
    table_path=HERE/"v19_residual_cube_cover_local_tables.json"
    table_path.write_bytes(encoded(tables))
    cert={"status":"PASS","date_jst":"2026-11-07",
          "scope":"ell=1,j=i-3; original right-hand indices squared; both k branches",
          "identity_checks":identities(),"sign_audit":bounded_sign_audit(),
          "examples":examples(),"denominators":BS,
          "local_tables_sha256":sha_bytes(table_path.read_bytes()),
          "producer_sha256":sha_bytes(Path(__file__).read_bytes()),
          "claims_not_made":["New original bound from Z>0", "Full four-variable classification",
              "Lean verification", "DeepSeek API execution", "Complete Selmer group",
              "Complete Mordell-Weil basis", "Cryptographic discrete-log attack"]}
    dest=HERE/"v19_residual_cube_cover_certificate.json"
    dest.write_bytes(encoded(cert))
    print(json.dumps({"status":"PASS","identities":len(cert["identity_checks"]),
        "coefficient_families":cert["sign_audit"]["coefficient_families"],
        "negative_Z_cases":cert["sign_audit"]["negative_Z_cases"],
        "max_prime":cert["sign_audit"]["largest_witness_prime"],
        "local_table_fibers":sum(len(r["fibers"]) for r in tables["rows"]),
        "cover_examples":len(cert["examples"]),"certificate_sha256":sha_bytes(dest.read_bytes())},indent=2))


if __name__=="__main__":
    main()
