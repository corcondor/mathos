#!/usr/bin/env python3
"""v98: all 5214 small-defect curves via the v11 bound + Legendre's theorem.

Proof of the exhaustive split (in V98_CONVERGENT_ONLY_CERTIFICATE_ja.md):

For every potential original solution, primitive p/q, q>0, p>3*q,
D=T*q^3-6*S*p^3>0 and D | 6*S*T (v11 / Lean CFBoundedDivisorBridge).
Writing alpha=(T/(6*S))^(1/3) gives

  0 < alpha-p/q = D/[6*S*q^3*(alpha^2+alpha*p/q+(p/q)^2)]
                 < T/(27*q^3).

If 1 <= S <= 12, T < 229*S, q >= 204, then 2*T < 27*q, so
0<alpha-p/q<1/(2*q^2). By the ordinary Legendre theorem for
IRRATIONAL alpha, p/q is an ordinary CF convergent. For q<204
we enumerate *every* possible primitive p with the rigorously
bounded positive D, without assuming it is a convergent.

The certificate reconstructs exact CF prefixes with v96's independently
authenticated integer-arithmetic prefix routine but NEVER uses v96's
65-pair candidate enumeration or twisted-cube recovery.
It instead tests D | T*q and g^2=T*q/D directly.

This is a rigorous finite integer computation conditional on the
written Legendre/CF coverage proof, NOT a complete Lean certificate.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
import time
from pathlib import Path

from v96_twisted_cube_cf_complete import icbrt_floor, exact_cf_prefix, verify_prefix

MAX_S = 24

def cutoff(S):
    # Since T<229*S, q>=17*S implies 2*T<458*S<459*S<=27*q.
    return 17*S
FIELDS = ("small_q_checked","small_primitive_candidates","small_D_dvd_Tq",
          "small_square_g","small_S_divisible_points",
          "large_convergents","large_relevant_convergents",
          "large_D_bounded","large_D_dvd_Tq","large_square_g",
          "large_S_divisible_points","recovered_points","strict_survivors")

def new_stats():
    return {k: ([] if k=="recovered_points" else 0) for k in FIELDS}

def recovered(S, T, p, q, D, H, stats, branch):
    # D is the positive *exact* integer difference.
    if (T*q) % D:
        return
    stats[branch+"_D_dvd_Tq"] += 1
    g_sq = (T*q)//D
    g=math.isqrt(g_sq)
    if g*g != g_sq or g == 0:
        return
    stats[branch+"_square_g"] += 1
    n=g*q+1
    r=g*p
    # Algebraically confirm the *original curve*, no approximate check.
    assert 6*S*r**3 == T*n*(n-1)*(n-2)
    if (n-2)%S: return
    stats[branch+"_S_divisible_points"] += 1
    item={"S":S,"T":T,"n":str(n),"r":str(r),
          "p":str(p),"q":str(q),"g":str(g),"D":str(D),"branch":branch}
    if n>=104 and n<H and 3*n<r and 3*r<10*n:
        stats["strict_survivors"]+=1
        item["result"]="SURVIVES"
    else:
        item["result"]="excluded by original height or strict gap"
    stats["recovered_points"].append(item)

def check_small_denominators(S,T,H,stats):
    C=6*S
    bound=C*T
    for q in range(1,cutoff(S)):
        stats["small_q_checked"]+=1
        # strict D>0 => C*p^3 < T*q^3.
        p=icbrt_floor((T*q**3-1)//C)
        while p>3*q:
            D=T*q**3-C*p**3
            assert D>0
            # D grows strictly as p decreases, so every omitted p
            # necessarily violates the proven D<=6*S*T bound.
            if D>bound: break
            if math.gcd(p,q)==1 and math.gcd(q,S)==1:
                stats["small_primitive_candidates"]+=1
                recovered(S,T,p,q,D,H,stats,"small")
            p-=1

def check_large_convergents(S,T,H,conv,stats):
    C=6*S
    bound=C*T
    assert 2*T < 27*cutoff(S)
    for p,q in conv:
        if q<cutoff(S) or q>=H: continue
        stats["large_convergents"]+=1
        # Consecutive convergents are automatically reduced; check
        # the actual p/q and all original necessary divisibility.
        if p<=3*q or math.gcd(q,S)!=1:continue
        stats["large_relevant_convergents"]+=1
        D=T*q**3-C*p**3
        if not (0<D<=bound):continue
        stats["large_D_bounded"]+=1
        assert math.gcd(p,q)==1
        recovered(S,T,p,q,D,H,stats,"large")

def run(min_s=1,max_s=12):
    assert 1<=min_s<=max_s<=MAX_S
    start=time.monotonic()
    totals=new_stats()
    overview={"status":"RUNNING","range":[min_s,max_s],
             "small_q_threshold_rule":"q < 17*S","curves":0,
             "irrational_curves":0,"rational_curves":0,"cf_terms":0,
             "by_S":[],"note":"Python exact finite check + written v11 bound and Legendre theorem, NOT full Lean"}
    for S in range(min_s,max_s+1):
        stats=new_stats()
        curves=rational=irrational=terms=0
        H=1<<(192*S)
        for T in range(162*S+1,229*S):
            assert 2*T<27*LOW_BOUND
            curves+=1
            check_small_denominators(S,T,H,stats)
            word=exact_cf_prefix(S,T)
            conv=verify_prefix(S,T,word)
            if conv is None:
                rational+=1
                # The rational root case is excluded by the existing
                # Lean theorem CFRationalCubeExclusionB, not by Legendre.
                # For S<=24, v^3|6S gives v<=5 and the rational-root gap
                # n-1<3*v/2 contradicts n>=104. The rational case is
                # not tested with Legendre or counted as an irrational curve.
                continue
            irrational+=1
            terms+=len(word)
            check_large_convergents(S,T,H,conv,stats)
        assert curves==67*S-1
        # Retain any survivors as explicit evidence rather than aborting the audit.
        for k in FIELDS:
            if k=="recovered_points":totals[k].extend(stats[k])
            else:totals[k]+=stats[k]
        overview["curves"]+=curves
        overview["rational_curves"]+=rational
        overview["irrational_curves"]+=irrational
        overview["cf_terms"]+=terms
        overview["by_S"].append({"S":S,"curves":curves,"rational":rational,
                      "irrational":irrational,"cf_terms":terms,
                      **{k:len(stats[k]) if k=="recovered_points" else stats[k]
                         for k in FIELDS}})
        print("V98_S",json.dumps(overview["by_S"][-1],ensure_ascii=False),flush=True)
    if (min_s,max_s)==(1,12):
        assert (overview["curves"],overview["rational_curves"],overview["irrational_curves"],
                overview["cf_terms"])==(5214,1,5213,4877566)
        assert totals["small_q_checked"]==733810
        assert totals["strict_survivors"]==0
        expected={(1,225,10,30),(2,450,10,30),(4,900,10,30),
                  (8,1800,10,30),(10,1681,82,246)}
        actual={(x["S"],x["T"],int(x["n"]),int(x["r"]))
                for x in totals["recovered_points"]}
        assert len(totals["recovered_points"])==5 and actual==expected,actual
        assert totals["large_S_divisible_points"]==0
    overview.update({k:totals[k] for k in FIELDS})
    overview["status"]="COMPLETE_EXACT_V98_ARITHMETIC"
    overview["complete_5214_curves"]=(min_s,max_s)==(1,12)
    overview["elapsed_seconds"]=round(time.monotonic()-start,3)
    overview["source_sha256"]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    print("V98_RESULT",json.dumps({k:v for k,v in overview.items()
        if k not in ("by_S","recovered_points")},ensure_ascii=False),flush=True)
    return overview

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--min-s",type=int,default=1)
    parser.add_argument("--max-s",type=int,default=12)
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    out=run(args.min_s,args.max_s)
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(out,indent=2,ensure_ascii=False)+"\n")
