"""Exact finite remainder for i prime and ell = 1, in both branches.

The proof reduces all remaining cases to 21<=j<=99, prime i<330,
r=m*i with 3<=m<=9, r<10*j, and A/i mod i < m.
"""

from math import comb, isqrt
from pathlib import Path
import json


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))


def verify():
    families = 0
    counts = {"lower": [0,0], "upper": [0,0]}
    equalities = []
    for p in range(23, 330):
        if not prime(p):
            continue
        for j in range(21, min(99,p-2)+1):
            A = comb(p,j)
            a = (A//p) % p
            assert A % p == 0
            assert a == ((-1)**(j-1)*pow(j,-1,p)) % p
            X = comb(p*p,j*j)
            for m in range(3,10):
                r=m*p
                if not (j+2 <= r < 10*j and 2*r <= A and a<m):
                    continue
                families += 1
                lhs=comb(A,r)
                for name,B in (("lower",r),("upper",A-r)):
                    rhs=X+B*B
                    if lhs==rhs:
                        equalities.append([p,j,B,1])
                    else:
                        counts[name][int(lhs>rhs)] += 1
    assert not equalities, equalities
    return {
        "verified": True,
        "scope": "Prime i, ell=1, 21<=j<=99, i<330; both B=r and B=A-r",
        "families_after_proved_modular_filter": families,
        "equations_checked": 2*families,
        "lower_left_smaller_larger": counts["lower"],
        "upper_left_smaller_larger": counts["upper"],
        "equalities": equalities,
        "arithmetic": "Exact integers only, math.comb, exhaustive primality trial division",
    }


if __name__ == "__main__":
    result=verify()
    Path(__file__).with_name("verification_prime_first_ell_one.json").write_text(
        json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result,indent=2))
