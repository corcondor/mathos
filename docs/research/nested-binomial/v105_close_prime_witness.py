#!/usr/bin/env python3
"""v105: one explicit witness for the close-prime forced-divisor theorem.

No search over i or over primes is performed.  The universal statements
are proved algebraically in V105_CLOSE_PRIME_FORCED_DIVISORS_ja.md,
with the four-prime infinitude supplied by Maynard's 2015 theorem.

For p=821 and q in {823,827,829} we verify by *exact* integer arithmetic:
q|R_p, the only root x in F_q of C(x,p)=x^2 is x=0, and
the product of three required q exceeds p^3.
"""
import json
import math


def prime(n):
    return n>1 and all(n%d for d in range(2,math.isqrt(n)+1))


def verify():
    p=821
    follower=[823,827,829]
    assert prime(p) and all(prime(q) for q in follower)
    R=math.comb(p*p,2*p-1)
    details=[]
    for q in follower:
        d=q-p
        assert 2<=d and d%2==0
        assert p>2**(d-1)+d*d+d+1
        assert p*p%q==d*d
        assert (2*p-1)%q==p-d-1
        assert d*d<p-d-1
        assert R%q==0
        # This finite illustration is separate from the ALL-even-d proof:
        deltas=[(-1)**s*math.comb(d-1,s)-(d-s)**2 for s in range(d)]
        assert all(delta!=0 and abs(delta)<q for delta in deltas)
        # Verify every residue class of this one small example. This is
        # optional cross-check only; the note proves it for all large p.
        roots=[x for x in range(q)
               if math.comb(x,p)%q == x*x%q]
        assert roots==[0]
        details.append({"forced_prime":q,"offset":d,"max_abs_delta":max(map(abs,deltas)),
                        "numerator_digit":p*p%q,"denominator_digit":(2*p-1)%q,
                        "only_modular_root":0,"R_mod_q":R%q})
    Q=math.prod(follower)
    assert Q==564234809 and p**3==553387661 and Q>p**3
    return {
        "status":"PASS_EXACT_V105_WITNESS",
        "p":p,
        "forced_primes":follower,
        "R_bitlength":R.bit_length(),
        "individual_forcing":details,
        "required_product":Q,
        "v101_height_upper_exclusive":p**3,
        "conclusion":"no integer solution for j=1, ell=k-1, k=821, for ANY i",
        "infinite_theorem_input":"Maynard 2015 Theorem 1.1 (4 primes in bounded windows infinitely often)",
        "scope":"example arithmetic only; all-even-d proof is written, not Lean-checked"
    }


if __name__=="__main__":
    report=verify()
    print("V105_RESULT",json.dumps(report,ensure_ascii=False),flush=True)
