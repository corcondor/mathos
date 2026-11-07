"""Independent H=13 reproduction: algebraic CF, no saved prefixes or cube root.

The unique real root of an integral cubic is followed under x=a+1/y.
Exact polynomial signs determine every partial quotient. Candidate fractions
use the union of the two complete coefficient lists, not the verifier's halves.
"""
from pathlib import Path
from math import gcd, isqrt
import hashlib
import json

ROOT = Path(__file__).resolve().parent
H = 13


def evaluate(coeff, k):
    a,b,c,d = coeff
    return ((a*k+b)*k+c)*k+d


def algebraic_prefix(t):
    coeff = (6*H,0,0,-t)
    p0,p1,q0,q1 = 0,1,1,0
    bound = 1 << (192*H)
    out = []
    while True:
        # The cubic has positive leading coefficient and exactly one real root.
        # That root is positive. A zero at an integer would contradict the
        # irrationality of (t/78)^(1/3), proved in the accompanying note.
        assert coeff[0] > 0 and evaluate(coeff,0) < 0
        low,high = 0,1
        while evaluate(coeff,high) < 0:
            low,high = high,2*high
        while high-low > 1:
            mid = (low+high)//2
            if evaluate(coeff,mid) < 0:
                low = mid
            else:
                high = mid
        assert evaluate(coeff,low) < 0 < evaluate(coeff,low+1)
        digit = low
        p,q = digit*p1+p0,digit*q1+q0
        out.append((digit,p,q))
        if q >= bound:
            assert q1 < bound
            return out
        p0,p1,q0,q1 = p1,p,q1,q
        a,b,c,d = coeff
        new = (evaluate(coeff,digit),(3*a*digit+2*b)*digit+c,3*a*digit+b,a)
        coeff = tuple(-v for v in new) if new[0] < 0 else new


def divisors_by_products(n):
    values = [1]
    rest = n
    for prime in range(2,isqrt(n)+1):
        if rest % prime:
            continue
        powers = [1]
        while rest % prime == 0:
            rest //= prime
            powers.append(powers[-1]*prime)
        values = [v*z for v in values for z in powers]
        if rest == 1:
            break
    if rest > 1:
        values += [v*rest for v in values]
    return set(values)


def reproduce():
    bound = 1 << (192*H)
    counts = {'H':H,'curves':0,'continued_fraction_terms':0,
              'reduced_fractions_sieved':0,'divisor_residue_passes':0,
              'exact_cubic_checks':0,'surviving_points':0}
    all_recoveries = set()
    survivors = set()
    for t in range(162*H+1,229*H):
        if t % H == 0:
            continue
        expansion = algebraic_prefix(t)
        counts['curves'] += 1
        counts['continued_fraction_terms'] += len(expansion)
        modulus = 12*H*t+1  # Deliberately differs from the primary verifier.
        possible = divisors_by_products(6*H*t)
        mods = [(p % modulus,q % modulus) for _,p,q in expansion]
        for stage in range(len(expansion)-1):
            _,pn,qn = expansion[stage]
            if stage:
                _,pp,qp = expansion[stage-1]
                rp,sp = mods[stage-1]
            else:
                pp,qp,rp,sp = 1,0,1,0
            anext,_,qnext = expansion[stage+1]
            rn,sn = mods[stage]
            upper = min(qnext-1,bound-1)
            for b in range(-2,3):
                choices = set(range(-1,5)) | {b*anext+c for c in range(-3,4)}
                for a in choices:
                    if gcd(a,b) != 1:
                        continue
                    q = a*qn+b*qp
                    if not qn <= q <= upper:
                        continue
                    p = a*pn+b*pp
                    if p <= 3*q:
                        continue
                    counts['reduced_fractions_sieved'] += 1
                    pm,qm = (a*rn+b*rp) % modulus,(a*sn+b*sp) % modulus
                    rem = (t*pow(qm,3,modulus)-6*H*pow(pm,3,modulus)) % modulus
                    if rem not in possible:
                        continue
                    counts['divisor_residue_passes'] += 1
                    assert gcd(p,q) == 1
                    counts['exact_cubic_checks'] += 1
                    difference = t*q*q*q-6*H*p*p*p
                    if difference != rem or (t*q) % difference:
                        continue
                    g2 = t*q//difference
                    g = isqrt(g2)
                    if g*g != g2:
                        continue
                    n,r = g*q+1,g*p
                    assert 6*H*r**3 == t*n*(n-1)*(n-2)
                    all_recoveries.add((t,n,r))
                    if n >= 104 and n < bound and (n-2) % H == 0 and 9*n < 3*r < 10*n:
                        survivors.add((t,n,r))
        if counts['curves'] % 100 == 0:
            print(json.dumps({'phase':'independent algebraic CF',**counts}),flush=True)
    counts['surviving_points'] = len(survivors)
    report = {
        'status':'PASS' if not survivors else 'CANDIDATES_REMAIN',**counts,
        'recovered_integer_points':[{'T':t,'n':str(n),'r':str(r)} for t,n,r in sorted(all_recoveries)],
        'survivors':sorted(survivors),
        'saved_certificates_read':False,'primary_verifier_imported':False,
        'cube_root_algorithm_used':False,
        'CF_generation':'exact integer cubic transformations and polynomial signs',
        'candidate_enumeration':'union of coefficient lists; gcd(a,b)=1',
        'residue_modulus':'12HT+1',
        'original_n_interval_scanned':False,'all_arithmetic_exact':True,
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'whole_original_equation_solved':False
    }
    assert counts['curves'] == 804
    out = ROOT / 'v11_effective_defect_cf_reproduction_verification.json'
    out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report),flush=True)


if __name__ == '__main__':
    reproduce()
