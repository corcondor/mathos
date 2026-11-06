#!/usr/bin/env python3
"""Independent arithmetic review of v18_neighbor_cofactor_height.md.

Does not import or execute the cofactor producer. Written proof review
and finite supporting calculations are explicitly separated.
"""
from fractions import Fraction as F
from hashlib import sha256
from math import gcd, isqrt
from pathlib import Path
import argparse
import json

def exact_identities():
    # These evaluation grids are coefficient certificates: each identity
    # has the declared degree at most 3 separately in w,J, or 2,3 in n,v.
    # A polynomial of those degrees vanishing on the full grid is zero.
    tests={}
    for e in (0,1):
        count=0
        for w in range(4):
            for J in range(4):
                c0=(10-e)*w+2*J
                c1=(25-e)*w+3*J
                if e==0:
                    left=125*c0**3-8*c1**3
                    right=J*(30000*w*w+9600*w*J+784*J*J)
                else:
                    left=512*c0**3-27*c1**3
                    right=7*J*(15552*w*w+5400*w*J+481*J*J)
                assert left==right
                count+=1
        tests["leading_cube_cancellation_epsilon_"+str(e)]={"grid_points":count,"degree_each_variable":3}
    count=0
    for n in range(3):
        for v in range(4):
            left=n*n*v*(30000+9600*v+784*v*v)-125*(10+2*v)**3*(2*n-1)
            right=((784*n*n-2000*n+1000)*v**3
                   +(9600*n*n-30000*n+15000)*v*v
                   +(30000*n*n-150000*n+75000)*v
                   -250000*n+125000)
            assert left==right
            count+=1
    tests["small_branch_positive_numerator"]={"grid_points":count,"degree_n":2,"degree_v":3}
    # Avoid denominator n: compare the lower-bound identity after multiplying by n.
    for n in range(3):
        left=17*(30000*n*n-150000*n+75000)-250000*n*n+125000*n
        right=260000*n*n-2425000*n+1275000
        assert left==right
    tests["small_branch_linear_positive_bound"]={"grid_points":3,"degree_n":2}
    for s in range(4):
        assert 6*s*s*(3*s-1)+(3*s)**2-10==18*s**3+3*s*s-10
    tests["square_root_height_boundary"]={"grid_points":4,"degree_s":3}
    return tests

def constants():
    v=F(19,9)
    C0=36*(30000+9600*v+784*v*v)
    C1=42*(15552+5400*v+481*v*v)
    assert C0==F(17418496,9)
    assert C1==F(32994542,27)
    small=C0*F(104,103)**2*F(112,3)**2
    comp=C1*F(104,103)*F(288,5)**2
    oldsmall=C0*F(104,103)**2*F(224,9)**2
    oldcomp=C1*F(104,103)*F(192,5)**2
    assert small==F(2363270191120384,859329)
    assert comp==F(10541360234496,2575)
    assert oldsmall==F(9453080764481536,7733961)
    assert oldcomp==F(14055146979328,7725)
    margins={
        "complementary_positive_numerator":108864*11-512*F(119,9)**3,
        "new_small_height":2**32-small,
        "new_complementary_height":2**32-comp,
        "old_gap_small_height":2**31-oldsmall,
        "old_gap_complementary_height":2**31-oldcomp,
        "small_w_power":2**37-F(112,3)**7,
        "complementary_w_power":2**18-F(288,5)**3,
        "old_gap_small_w":2**14-F(224,9)**3,
        "short_height_c0_constant":F(19,25)-F(1667,3000)-F(1,5),
        "short_height_cubic_constant":F(4)-9*F(19,25)**3,
    }
    assert margins["complementary_positive_numerator"]==F(10179008,729)
    assert all(x>0 for x in margins.values())
    return {k:str(v) for k,v in margins.items()}

def divisors_by_pairs(n):
    out=[]
    for d in range(1,isqrt(n)+1):
        if n%d==0:
            out.append(d)
            if d*d!=n:out.append(n//d)
    return sorted(out)

def support(rows):
    output=[]
    canonical=[]
    for row in rows:
        n,r=row["n"],row["r"]
        g,d=gcd(n,3),gcd(n-1,6)
        M=g*d;Q0=n//g;Q1=(n-1)//d
        N=n*n+2
        for eps in (0,1):
            S=(r-eps)**2-6*n+8
            G=gcd(N,S)
            for q in divisors_by_pairs(G):
                w=N//q;z=S//q;J=z-9*w
                assert J>0 and 9*J<19*w
                c0=(10-eps)*w+2*J
                c1=(25-eps)*w+3*J
                assert (c0-w*r*(r-2*eps))%Q0==0
                assert (c1-w*r*(r-2*eps))%Q1==0
                assert c0**3%Q0==0 and c1**3%Q1==0
                if eps==0:
                    assert c0**3%(Q0*Q0)==0 and c1**3%(Q1*Q1)==0
                    b0=g*g*c0**3//(n*n)
                    b1=d*d*c1**3//((n-1)**2)
                    E=125*d*d*b0-8*g*g*b1
                    FF=J*(30000*w*w+9600*w*J+784*J*J)
                    assert E*n*n*(n-1)**2==M*M*(n*n*FF-125*c0**3*(2*n-1))
                    assert E>=1
                    assert (n-1)**2<36*FF
                    assert n**14<2**352*J**33
                    assert w**7<2**101*J**13
                    assert n**6<2**155*J**15
                    assert w<2**15*J*J
                    T=S-9*N
                    assert T>0 and T*T>18**2*n**3
                    assert 25**2*c0*c0<19**2*J*J*n
                    assert n<16*J**6 and J>=2
                else:
                    a0=g*c0**3//n
                    a1=d*c1**3//(n-1)
                    E=512*d*a0-27*g*a1
                    FF=7*J*(15552*w*w+5400*w*J+481*J*J)
                    assert E*n*(n-1)==M*(n*FF-512*c0**3)
                    assert E>=1
                    assert n-1<6*FF
                    assert n**3<2**352*J**33
                    assert w<2**49*J**5
                    assert n<2**155*J**15
                    assert w<2**68*J**7
                output.append({"n":n,"r":r,"epsilon":eps,"q":q,"w":w,"J":J,
                               "integer_difference":E})
                if q==G:
                    assert gcd(w,J)==1
                    assert (20 if eps==0 else 21)%gcd(c0,c1)==0
                    Q=Q0*Q1
                    delta=Q//gcd(Q,r*r)
                    common=gcd(delta,J)
                    assert (25 if eps==0 else 72)%common==0
                    canonical.append({"n":n,"r":r,"epsilon":eps,"G":G,"w":w,"J":J,
                                      "coefficient_gcd":gcd(c0,c1),"delta":delta,
                                      "defect_numerator_gcd":common})
    return output,canonical

def valuation(n,p):
    n=abs(n)
    assert n>0
    v=0
    while n%p==0:
        n//=p;v+=1
    return v

def logfloor(m,p):
    a=0
    while m>=p:
        m//=p;a+=1
    return a

def choose_mod_prime_power(n,k,p,s):
    """Independent exact numerator/denominator unit products."""
    if s==0:return 0
    if k<0 or k>n:return 0
    k=min(k,n-k)
    modulus=p**s;num=den=1;exponent=0
    for j in range(1,k+1):
        x=n-k+j;y=j
        while x%p==0:x//=p;exponent+=1
        while y%p==0:y//=p;exponent-=1
        num=num*x%modulus;den=den*y%modulus
    assert exponent>=0 and gcd(den,modulus)==1
    if exponent>=s:return 0
    return num*pow(den,-1,modulus)*pow(p,exponent,modulus)%modulus

def prime_power_support():
    # Nontrivial high-multiplicity small-prime cases, including p=3.
    cases=[(2695,3),(1917,11),(3492,17),(3433,41),(450,73)]
    rows=[]
    for n,p in cases:
        N=n*n+2;m=6*n-9;A=n*(n-1)*(n-2)//6
        e=valuation(N,p);a=logfloor(m,p)
        loss=1 if p in (2,3) else 0
        inner_s=e-a;outer_s=e-a-loss
        assert outer_s>0
        B=choose_mod_prime_power(n*n,m,p,inner_s)
        assert (B-(8-6*n))%(p**inner_s)==0
        for r in [3*n+4,(10*n-1)//3]:
            out=choose_mod_prime_power(A,r,p,outer_s)
            assert out==0
            assert (A-1)%(p**outer_s)==0
            rows.append({"n":n,"p":p,"e":e,"floor_log_p_m":a,
                         "inner_modulus":p**inner_s,"inner_residue":B,
                         "r":r,"outer_modulus":p**outer_s,"outer_residue":out})
    return rows

def local_defect_support():
    """Test the local valuation lemma separately from original-solution status.

    At the chosen prime, alpha=D+2E<=3E is enforced exactly. Other
    primes and the interval for r are deliberately not imposed here.
    """
    summaries=[]
    witnesses=[]
    total=0
    for p in [2,3,5,7,11]:
        counts=[0,0]
        maxima=[-1,-1]
        max_rows=[None,None]
        units=[x for x in range(1,2*p) if x%p]
        for D in range(1,6):
            for E in range(D,D+4):
                alpha=D+2*E
                for endpoint in [0,1]:
                    loss=1 if p==3 or (p==2 and endpoint==1) else 0
                    for s in units:
                        n=endpoint+p**(alpha+loss)*s
                        Q=n*(n-1)//(gcd(n,3)*gcd(n-1,6))
                        assert valuation(Q,p)==alpha
                        for v in units:
                            r=p**E*v
                            delta=Q//gcd(Q,r*r)
                            assert valuation(delta,p)==D
                            N=n*n+2
                            for eps in [0,1]:
                                T=(r-eps)**2-9*n*n-6*n-10
                                assert T!=0
                                G=gcd(N,T)
                                J=T//G
                                value=min(D,valuation(J,p))
                                bound=({5:2}.get(p,0) if eps==0 else {2:3,3:2}.get(p,0))
                                assert value<=bound
                                counts[eps]+=1
                                total+=1
                                if value>maxima[eps]:
                                    maxima[eps]=value
                                    max_rows[eps]={"p":p,"epsilon":eps,"n":n,"r":r,
                                                   "D":D,"E":E,"v_p_J":valuation(J,p),
                                                   "common_exponent":value,
                                                   "local_valuation_example_only":True}
        summaries.append({"p":p,"counts_by_branch":counts,
                          "largest_common_exponent_by_branch":maxima})
        witnesses.extend(max_rows)
    return {"total_local_cases":total,"summaries":summaries,"maximal_examples":witnesses,
            "scope":"Local chosen-prime conditions only, not full old-necessary pairs or original solutions"}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    here=Path(__file__).resolve().parent
    default_proof=here/"v18_neighbor_cofactor_height.md"
    if not default_proof.exists():
        default_proof=here.parent/"cofactor"/"v18_neighbor_cofactor_height.md"
    parser.add_argument("--proof",type=Path,default=default_proof)
    parser.add_argument("--gap-report",type=Path,default=here/"v18_residual_gap_checks.json")
    parser.add_argument("--output",type=Path,default=here/"v18_neighbor_cofactor_independent_review.json")
    args=parser.parse_args()
    sample=json.loads(args.gap_report.read_text())["supporting_sample"]
    identities=exact_identities()
    margins=constants()
    rows,canonical=support(sample["records"])
    binomial=prime_power_support()
    local_defect=local_defect_support()
    report={
        "status":"PASS",
        "date":"2026-11-07 JST",
        "reviewed_file":args.proof.name,
        "reviewed_sha256":sha256(args.proof.read_bytes()).hexdigest(),
        "source_sha256":sha256(Path(__file__).read_bytes()).hexdigest(),
        "gap_sample_input_sha256":sha256(args.gap_report.read_bytes()).hexdigest(),
        "producer_imported_or_executed":False,
        "written_review":[
            "The common-divisor domain uses q|gcd(N,S_epsilon); w,z,J are integral and positive without a prime or q>m restriction.",
            "Coefficient transfers follow directly from w(r-epsilon)^2=zN+6wn-8w modulo Q0 and Q1; no cancellation at 2 or 3.",
            "The small-branch square-cube transfer is valid prime by prime, including primes dividing w.",
            "E0 and E1 are integers from the divisibility inputs; their strictly positive numerators are proved uniformly for n>=104,t>=4.",
            "Both J-height bounds use the separately proved v18 gap, with branch-specific exponents and no bound on J itself.",
            "The all-prime-power congruence follows from the elementary choose divisibility and alternating Pascal, with the exact loss floor(log_p(m))+v_p(6).",
            "R=N/gcd(N,3L_m) is coprime to Q and has at most one prime base because N<m^2.",
            "The v17 no-primality cofactor certificate transfers logically to every common divisor q; its small-q case still uses delta>=13.",
            "Canonical gcd(w,J)=1 is required for gcd(c0,c1)|20 or21, and is not silently assumed for general q.",
            "The v17 necessary square-root bound gives T0>18*n^(3/2); c0/J<(19/25)*sqrt(n) and Q0^2|c0^3 imply n<16*J^6 and J>=2 without a finite J=1 enumeration.",
            "For canonical J, the defect exponents alpha=D+2E and E>=D force gcd(delta,J)|25 in the small branch and |72 in the complementary branch; primes 2,3,5 are checked separately with the cancellation by G retained.",
        ],
        "coefficient_certificates":identities,
        "rational_margins":margins,
        "supporting_cases":{
            "old_necessary_pairs":len(sample["records"]),
            "all_common_divisor_records":len(rows),"canonical_records":len(canonical),
            "records":rows,"canonical":canonical,
            "original_solutions":False,"finite_samples_prove_universal_theorem":False},
        "independent_prime_power_binomial_cases":binomial,
        "independent_local_defect_numerator_cases":local_defect,
        "new_lean_execution":False,"external_peer_review":False,
        "canonical_J1_enumeration_reexecuted":False,
        "verification_boundary":"Independent written review of the cofactor, prime-power, short J-height and canonical-defect sections plus exact coefficient/constant checks. The exploratory J=1 enumeration was not reexecuted and is not needed for the audited analytic proof.",
    }
    args.output.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"status":"PASS","coefficient_certificates":len(identities),
                      "positive_margins":len(margins),"common_divisor_records":len(rows),
                      "canonical_records":len(canonical),"prime_power_cases":len(binomial),
                      "local_defect_cases":local_defect["total_local_cases"],
                      "report":str(args.output)},ensure_ascii=False))
if __name__=="__main__":main()

