#!/usr/bin/env python3
"""v108: exact audit of the HUGE→SMALL many-prime structural theorem.

No scan over original i. We check only:
- one exact 17^3-local root within the proven global height (counterexample
  to an invalid universal 'all lifts outside' claim);
- 19 and 59 prime polynomial gcd certificates modulo their finite fields,
  via fast polynomial exponentiation and Euclid (not scanning residues);
- four Chinese-remainder representatives, all excluded by i<8^3;
- two large rational inequalities that anchor the elementary
  prime-factor growth argument for EVERY k>=1000.

The all-k count |{q>2k-1 : q|R_k}|>k/(10 log k)
is proved in V108_MANY_PRIME_CRT_AND_ROOT_DENSITY_GATE_ja.md,
not by checking a finite list of k.
"""
import json
import math

from v106_nonlocal_prime_units_audit import (
    isprime, forced_polynomial, poly_gcd, x_to_qminus1_minus1
)


def quotient_by_x_plus_one(g, q):
    """Exact synthetic division of ascending coefficients modulo q."""
    assert len(g)>=2
    h=[0]*(len(g)-1)
    h[-1]=g[-1]%q
    for j in range(len(g)-2,0,-1):
        h[j-1]=(g[j]-h[j])%q
    assert g[0]%q == h[0]%q
    assert all(
        g[j]%q == (h[j]+(h[j-1] if j else 0))%q
        for j in range(len(h))
    )
    assert g[-1]%q == h[-1]%q
    return h


def rootfree_except_zero_or_minus_one(k, q):
    assert k%2==0 and isprime(q) and q>2*k-1
    g=forced_polynomial(k,q)
    h=quotient_by_x_plus_one(g,q)
    gcd=poly_gcd(h,x_to_qminus1_minus1(h,q),q)
    assert gcd==[1],(k,q,gcd)
    # H(0) is nonzero, so gcd=1 with X^(q-1)-1 (all nonzero elements)
    # also means no root in F_q at all.
    assert h[0]!=0
    return {"q":q, "cofactor_degree":len(h)-1,
            "gcd_cofactor_fermat":[1],
            "permissible_i_mod_q":[0,q-1]}


def v108_check():
    k=8
    R=math.comb(k*k,2*k-1)
    q17=17
    fake_i=68
    defect=math.comb(fake_i,k)-fake_i*fake_i-R
    assert R==159518999862720
    assert 0<fake_i<k**3 and R%q17==0
    assert defect==-159511607857576 and defect!=0
    assert defect%(q17**3)==0

    q1,q2=19,59
    assert R%q1==R%q2==0
    roots=[rootfree_except_zero_or_minus_one(k,q1),
           rootfree_except_zero_or_minus_one(k,q2)]
    modulus=q1*q2
    reps=[]
    for a in (0,q1-1):
        for b in (0,q2-1):
            x=a+q1*((b-a)*pow(q1,-1,q2)%q2)
            assert 0<=x<modulus and x%q1==a and x%q2==b
            reps.append(x)
    reps.sort()
    assert modulus==1121 and reps==[0,531,589,1120]
    assert not any(0<i<k**3 for i in reps)
    assert k**3<modulus

    # An exact rational base/monotonic proof component used in the note:
    # (13/10)^(2k-1) > 6*k^22 for all k>=1000.
    # At k=1000 the inequality is checked exactly as integers. The
    # adjacent quotient is increasing in k and >1 for k>=1000,
    # because (169/100)*(k/(k+1))^22 > 1.
    K=1000
    base=13**(2*K-1)>6*K**22*10**(2*K-1)
    step=169*K**22>100*(K+1)**22
    assert base and step
    return {
        "status":"PASS_V108_LOCAL_GLOBAL_COLLISION",
        "original_special_branch":"j=1, ell=k-1, k=8, original i<512 from v101",
        "local_counterexample":{
            "q":q17,"i":fake_i,"height":k**3,
            "defect":defect,
            "defect_mod_q_cubed":0,
            "genuine_integer_solution":False},
        "cofactor_root_free_fields":roots,
        "two_prime_crt":{
            "primes":[q1,q2],
            "modulus":modulus,
            "representatives":reps,
            "compatible_positive_i_below_512":0,
            "conclusion":"NO ORIGINAL SOLUTION FOR ANY i (using v101 height)"},
        "all_k_prime_count_analytic_certificate":{
            "scope":"every integer k>=1000; general proof uses Legendre and Stirling",
            "rational_base_at_k1000":base,
            "rational_monotonicity_step_at_k1000":step,
            "consequence":"large-prime product > k^20 hence at least 11 distinct eligible q for k>=1000",
            "stronger_written_bound":"number of eligible q>k/(10 log k) for k>=1000"},
        "whole_four_variable_equation_solved":False
    }


if __name__=="__main__":
    r=v108_check()
    print("V108_RESULT",json.dumps(r,ensure_ascii=False),flush=True)
