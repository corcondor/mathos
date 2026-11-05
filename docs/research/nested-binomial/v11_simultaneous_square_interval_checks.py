"""CRT on squared values: <=4 integer tests per unitary support, <=1 for E>=512.

The mathematical proof is uniform. Finite cases here check the implementation
against direct enumeration of the already reduced u conditions, not the original
four-variable equation. Original-binomial examples are labelled separately.
"""
from pathlib import Path
from math import comb, gcd, isqrt, prod
import hashlib
import json

ROOT = Path(__file__).resolve().parent


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


def root3(n):
    low,high = 0,1 << ((n.bit_length()+2)//3)
    while low < high:
        mid = (low+high+1)//2
        if mid**3 <= n:
            low = mid
        else:
            high = mid-1
    return low


def crt(residues):
    value,modulus = 0,1
    for residue,other in residues:
        correction = ((residue-value)*pow(modulus,-1,other)) % other
        value += modulus*correction
        modulus *= other
    return value,modulus


def ceil_div(a,b):
    return -((-a)//b)


def squared_interval_candidates(E,K,units):
    """units[p] is lambda_p mod p^v_p(E). Return all reduced candidates.

    This implements every critical-prime condition and 162E<K*u^3<229E,
    with the established effective defect H>=14. Other conditions of the
    original binomial equation still have to be checked.
    """
    assert E >= 1 and K >= 1 and gcd(E,K) == 1
    fac = factor(E)
    blocks = [(p,p**a) for p,a in fac.items()]
    assert set(units) == set(fac)
    assert all(gcd(units[p],q) == 1 for p,q in blocks)
    output,records = set(),[]
    for mask in range(1 << len(blocks)):
        Z = prod(q for bit,(_,q) in enumerate(blocks) if mask >> bit & 1)
        H = E//Z
        if H < 14:
            continue
        assert gcd(Z,H) == 1
        J = K*Z*Z
        if J >= 229*H:
            continue
        residues = [((-units[p]*pow(Z,-1,q)**2) % q,q)
                    for bit,(p,q) in enumerate(blocks) if not (mask >> bit & 1)]
        R,modulus = crt(residues)
        assert modulus == H and 0 < R < H and gcd(R,H) == 1
        # W=v^2. Strict cubic inequalities for W, no real powers or rounding.
        lower = root3((162*H)**2//(J*J))+1
        upper = root3(((229*H)**2-1)//(J*J))
        mlow = max(0,ceil_div(lower-R,H))
        mhigh = (upper-R)//H
        count = max(0,mhigh-mlow+1)
        assert count <= 4
        scale = E*K*K*Z**3
        if scale >= 512:
            assert count <= 1
        if Z >= 3:
            assert count <= 1
        if Z == 2:
            assert count <= 2
        if scale >= 229**2 and count:
            assert mlow == mhigh == 0
        found = []
        for m in range(mlow,mhigh+1):
            square = R+m*H
            v = isqrt(square)
            if v*v != square:
                continue
            assert 162*H < J*v**3 < 229*H
            u = Z*v
            assert E//gcd(E,u) == H
            assert all(u*(u*u+units[p]) % q == 0 for p,q in blocks)
            output.add(u)
            found.append(u)
        records.append({'Z':Z,'H':H,'J':J,'R':R,'W_low':lower,'W_high':upper,
                        'm_low':mlow,'m_high':mhigh,'integer_tests':count,
                        'candidates_u':found})
    assert sum(r['integer_tests'] for r in records) <= len(records)+4
    return sorted(output),records


def direct_reduced_candidates(E,K,units):
    """Reference checks each u in the proof-bounded cubic interval."""
    blocks = [(p,p**a) for p,a in factor(E).items()]
    ans = []
    first = root3(162*E//K)+1
    last = root3((229*E-1)//K)
    for u in range(first,last+1):
        if E//gcd(E,u) < 14:
            continue
        if all(u*(u*u+units[p]) % q == 0 for p,q in blocks):
            ans.append(u)
    return ans


def unit_seed(seed,p,q):
    value = (seed*seed+3*seed+p+1) % q
    while gcd(value,q) != 1:
        value = (value+1) % q
    return value


def binomial_data(n):
    A = n*(n-1)*(n-2)//6
    X = comb(n*n,6*n-9)
    afac = factor(A)
    xvals = {}
    for p in afac:
        value = X
        exponent = 0
        while value % p == 0:
            exponent += 1
            value //= p
        xvals[p] = exponent
    efac = {p:max(a-3*(xvals[p]//2),0) if xvals[p] % 2 == 0 else 0
            for p,a in afac.items()}
    E = prod(p**d for p,d in efac.items())
    B = A//E
    F = prod(p**((a-efac[p]+2)//3) for p,a in afac.items())
    K = F**3//B
    assert F**3 == B*K and gcd(K,E) == 1
    assert all(a <= 2 for a in factor(K).values())
    units = {}
    for p,d in efac.items():
        if not d:
            continue
        t = xvals[p]//2
        modulus = p**d
        units[p] = ((X//p**(2*t))*pow(F//p**t,-1,modulus)**2) % modulus
    return A,X,E,K,F,units


def verify():
    assert 8*229**2 < 75**3
    assert 8*162**2 > 59**3
    assert 8**3 < 4**3*14
    assert 14*3**4 > 512 and 14*2**4 > 64
    Es = [14,15,16,18,19,24,25,27,30,32,35,49,51,64,81,105,121,125,
          128,169,256,343,511,512,513,707,1001,2310,4096,52440,52441,65536,99991,100003]
    Ks = [1,2,3,4,5,6,7,9,10,11,13,25,49,121]
    stats = {'synthetic_cases':0,'support_branches':0,'integer_square_tests':0,
             'positive_reduced_candidates':0,'max_integer_tests_per_support':0,
             'cases_E_at_least_512':0,'zero_support_cases':0}
    for E in Es:
        fac = factor(E)
        for K in Ks:
            if gcd(E,K) != 1:
                continue
            for seed in range(8):
                units = {p:unit_seed(seed,p,p**a) for p,a in fac.items()}
                got,rows = squared_interval_candidates(E,K,units)
                assert got == direct_reduced_candidates(E,K,units)
                stats['synthetic_cases'] += 1
                stats['support_branches'] += len(rows)
                stats['integer_square_tests'] += sum(x['integer_tests'] for x in rows)
                stats['positive_reduced_candidates'] += len(got)
                stats['max_integer_tests_per_support'] = max(
                    stats['max_integer_tests_per_support'],
                    max((x['integer_tests'] for x in rows),default=0))
                stats['cases_E_at_least_512'] += E >= 512
                stats['zero_support_cases'] += any(x['Z'] > 1 and x['candidates_u'] for x in rows)
    # Explicit positive reduced examples; these are NOT solutions of the
    # original nested-binomial equation. One has v and Z sharing a prime.
    positive_examples = []
    for E,units,target in [(15,{3:2,5:4},14),
                           (1001,{7:1,11:10,13:10},56),
                           (707,{7:1,101:23},49)]:
        got,rows = squared_interval_candidates(E,1,units)
        assert got == direct_reduced_candidates(E,1,units) and target in got
        positive_examples.append({'E':E,'K':1,'units':units,'candidates_u':got,'supports':rows,
                                  'original_equation_solution':False})
    originals = []
    for n in [104,105,106,111,127,128,129,169,195,233,289,327,343,387,489,
              512,686,729,771,975,1024,1330,2048,4096,6860]:
        A,X,E,K,F,units = binomial_data(n)
        got,rows = squared_interval_candidates(E,K,units)
        assert got == direct_reduced_candidates(E,K,units)
        survivors = [F*u for u in got if 9*n < 3*F*u < 10*n
                     and (F*u*(X+(F*u)**2)) % A == 0]
        originals.append({'n':n,'E':E,'K':K,'F':F,'candidates_u':got,
                          'supports':len(rows),'remaining_polynomial_congruence_candidates_r':survivors})
    report = {'status':'PASS',**stats,'original_binomial_examples':originals,
              'positive_reduced_examples':positive_examples,
              'all_arithmetic_exact':True,
              'uniform_claim_basis':'written mathematical proof, not extrapolation from samples',
              'whole_original_equation_solved':False,
              'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    out = ROOT / 'v11_simultaneous_square_interval_verification.json'
    out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ['status',*stats]},sort_keys=True),flush=True)
    print(json.dumps({'original_binomial_examples':originals}),flush=True)


if __name__ == '__main__':
    verify()
