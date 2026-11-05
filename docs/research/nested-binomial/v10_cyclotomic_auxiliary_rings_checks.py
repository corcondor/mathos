#!/usr/bin/env python3
"""Exact finite checks for the written v10 auxiliary-ring proofs.

No search of the original four-variable equation is performed.
Ring powers are checked independently by pair multiplication and
two-by-two matrix multiplication. Frozen v9 full periods are reproduced.
"""
from pathlib import Path
from math import gcd, isqrt, lcm
import hashlib
import json

ROOT = Path(__file__).resolve().parent


def mul(z, w, modulus=None):
    x, y = z
    u, v = w
    value = (x * u - y * v, x * v + y * u - y * v)
    return value if modulus is None else tuple(t % modulus for t in value)


def power(z, exponent, modulus):
    result = (1, 0)
    z = tuple(t % modulus for t in z)
    while exponent:
        if exponent & 1:
            result = mul(result, z, modulus)
        z = mul(z, z, modulus)
        exponent //= 2
    return result


def mmul(a, b, modulus):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2)) % modulus
                       for j in range(2)) for i in range(2))


def independent_power(z, exponent, modulus):
    x, y = z
    matrix = ((x % modulus, -y % modulus),
              (y % modulus, (x - y) % modulus))
    result = ((1, 0), (0, 1))
    for _ in range(exponent):
        result = mmul(matrix, result, modulus)
    return result[0][0], result[1][0]


def norm(z):
    x, y = z
    return x*x - x*y + y*y


def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def primes_sieve(limit):
    flags = bytearray(b'\x01') * (limit + 1)
    flags[:2] = b'\x00\x00'
    for p in range(2, isqrt(limit) + 1):
        if flags[p]:
            for k in range(p*p, limit+1, p):
                flags[k] = 0
    return [p for p in range(2, limit+1) if flags[p]]


def primary(q):
    pairs = []
    for m in range(1, isqrt(4*q//27) + 1):
        b = isqrt(4*q - 27*m*m)
        if b*b + 27*m*m == 4*q:
            B = b if b % 3 == 2 else -b
            assert B % 3 == 2
            for y in (3*m, -3*m):
                x = (B+y)//2
                assert (B+y) % 2 == 0 and x % 3 == 1 and y % 3 == 0
                assert norm((x,y)) == q
                pairs.append((x,y))
            return B, m, pairs
    raise AssertionError(('no primary representation', q))


def minimal_order(value, q):
    order = q-1
    factors = [p for p in primes_sieve(isqrt(q-1)) if (q-1) % p == 0]
    remainder = q-1
    for p in factors:
        while remainder % p == 0:
            remainder //= p
    if remainder > 1:
        factors.append(remainder)
    for p in factors:
        while order % p == 0 and pow(value, order//p, q) == 1:
            order //= p
    assert pow(value, order, q) == 1
    return order


def main():
    gamma = {2: (2,-1), 4: (-1,2)}
    comparison_count = 0
    mod2 = []
    for x in range(2):
        for y in range(2):
            z = (x,y)
            if norm(z) % 2 == 0:
                assert z == (0,0)
                continue
            assert power(z, 3, 2) == (1,0)
            for h,g in gamma.items():
                allowed = []
                for a in range(3):
                    pw = power(z,a,2)
                    assert pw == independent_power(z,a,2)
                    comparison_count += 1
                    if mul(g,pw,2) == (1,1):
                        allowed.append(a)
                assert 0 not in allowed
                if z == (1,0):
                    assert not allowed
                mod2.append({'pi':z,'p_mod7':h,'allowed_a_mod3':allowed})

    mod5 = []
    trace_zero_cases = scalar_cases = 0
    for x in range(5):
        for y in range(5):
            z=(x,y)
            if norm(z) % 5 == 0:
                assert z == (0,0)
                continue
            assert power(z,24,5)==(1,0)
            for h,g in gamma.items():
                allowed=[]
                for a in range(24):
                    pw=power(z,a,5)
                    assert pw==independent_power(z,a,5)
                    comparison_count += 1
                    c,d=mul(g,pw,5)
                    # 3|a excluded by F4, 4|a by the prior square theorem;
                    # the h=4 branch cannot have even a.
                    if a%3 and a%4 and (h==2 or a%2) and d==4 and c:
                        allowed.append(a)
                if (2*x-y)%5==0:
                    assert norm(z)%5 in (2,3)
                    assert power(z,2,5)==((-norm(z))%5,0)
                    assert mul(gamma[2],z,5)==(4*x%5,0)
                    assert mul(gamma[4],z,5)==(0,x)
                    assert not allowed
                    trace_zero_cases += 1
                if y==0:
                    if allowed:
                        assert norm(z)%5 == (1 if h==2 else 4)
                    scalar_cases += 1
                mod5.append({'pi':z,'p_mod7':h,'trace_mod5':(2*x-y)%5,
                             'norm_mod5':norm(z)%5,'allowed_a_mod24':allowed})

    mod7=[]
    for x in range(7):
        for y in range(7):
            z=(x,y)
            Q=norm(z)%7
            if Q==0:
                continue
            assert power(z,6,7)==(1,0)
            u2,u4=(x+2*y)%7,(x+4*y)%7
            B=(2*x-y)%7
            assert u2*u4%7==Q and (u2+u4)%7==B
            for h,g in gamma.items():
                allowed=[]
                for a in range(6):
                    pw=power(z,a,7)
                    assert pw==independent_power(z,a,7)
                    comparison_count += 1
                    if a%3 and mul(g,pw,7)==(h,6):
                        allowed.append(a)
                        if h==2:
                            assert u4 in (1,6)
                            assert u4!=6 or a%2==0
                            assert B*B%7==(Q+1)**2%7
                        else:
                            assert a in (1,5)
                            assert u2==(3 if a==1 else 5)
                            assert B==((3+5*Q)%7 if a==1 else (5+3*Q)%7)
                mod7.append({'pi':z,'p_mod7':h,'norm_mod7':Q,
                             'trace_mod7':B,'allowed_a_mod6':allowed})

    concrete=[]
    for q,r,h,expected in [(19,11,4,(-5,-3)),(31,5,4,(1,6)),
                            (67,37,2,(-2,-9)),(367,83,2,(13,-9))]:
        B,m,pairs=primary(q)
        oriented=[z for z in pairs if (z[0]+z[1]*r)%q==0]
        assert oriented==[expected]
        assert (r*r+r+1)%q==0
        concrete.append({'q':q,'B':B,'m':m,'r':r,'p_mod7':h,
                         'oriented_pi':expected})
    assert primary(31)[:2]==(-4,2)
    assert primary(67)[:2]==(5,3)
    assert primary(367)[:2]==(35,3)
    assert primary(223)[:2]==(-28,2)
    assert primary(229)[:2]==(-22,4)
    assert primary(379)[:2]==(29,5)
    assert primary(439)[:2]==(-28,6)
    assert 14**2+27==223 and 11**2+27*2**2==229
    assert 4*379==29**2+27*5**2 and 379%5==4
    assert 4*439==(-28)**2+27*6**2
    even_interval_composites={391:[17,23],403:[13,31],415:[5,83],
                             427:[7,61],451:[11,41]}
    for composite,factors in even_interval_composites.items():
        assert composite==factors[0]*factors[1]
        assert all(is_prime(p) for p in factors)

    q=19
    assert [r for r in range(q) if (r*r+r+1)%q==0]==[7,11]
    quadratic=[]
    for r in (7,11):
        square=(1-r)*pow(42,-1,q)%q
        character=pow(square,9,q)
        quadratic.append({'r':r,'j_squared':square,'character':character})
    assert quadratic==[{'r':7,'j_squared':8,'character':18},
                       {'r':11,'j_squared':7,'character':1}]
    trace_powers=[pow(-7,a,19) for a in range(6)]
    assert trace_powers==[1,12,11,18,7,8]
    r=11
    assert (2*r+1)*pow(r+3,-1,19)%19==3
    assert (r+2)*pow(r-2,-1,19)%19==12
    z=(-5,-3)
    assert mul(gamma[4],z)==(11,-1)
    assert mul(mul(z,z),mul(z,z))==(-185,231)
    assert power(z,4,11)==(2,0)
    assert mul(gamma[4],z,11)==(0,10)
    assert power(z,12,5)==(1,0) and power(z,40,11)==(1,0)
    q19_records=[]
    for a in range(120):
        v5=mul(gamma[4],power(z,a,5),5)
        v11=mul(gamma[4],power(z,a,11),11)
        assert power(z,a,5)==independent_power(z,a,5)
        assert power(z,a,11)==independent_power(z,a,11)
        comparison_count += 2
        if a%6==1 and v5[1]==4:
            assert a%4==1 and v11[0]==0
            q19_records.append({'a_mod120':a,'pair_mod5':v5,'pair_mod11':v11})
    assert len(q19_records)==10

    # Reproduce every one of the frozen v9 period records. Their a%3
    # filter now has the elementary F4 proof above in the prime-p scope.
    prior_path=ROOT/'v9_cyclotomic_primary_trace_verification.json'
    prior=json.loads(prior_path.read_text())
    periods=prior['all_exponent_tables']+prior['even_exponent_tables']+[
        prior['first_unexcluded_even_base_table']]
    prime_list=primes_sieve(367)
    assert [t['q'] for t in prior['all_exponent_tables']]==[
        q for q in prime_list if 13<=q<=211 and q%3==1]
    assert [t['q'] for t in prior['even_exponent_tables']]==[
        q for q in prime_list if 13<=q<367 and q%12==7]
    reproduced=[]
    for table in periods:
        q=table['q']
        assert is_prime(q)
        B,m,pairs=primary(q)
        d=minimal_order(B,q)
        period=lcm(d,12)
        assert (B,m,d,period)==(table['primary_trace'],table['norm_m'],
                               table['multiplicative_order'],table['full_exponent_period'])
        roots=[r for r in range(q) if (r*r+r+1)%q==0]
        assert roots==[r['p_mod_q'] for r in table['roots']]
        survivor_count=even_count=0
        for root in table['roots']:
            r=root['p_mod_q']
            residue=(1-r)*pow(42,-1,q)%q
            character=pow(residue,(q-1)//2,q)
            assert residue==root['j_squared_residue']
            assert character==root['quadratic_character']
            for branch in root['branches']:
                h=branch['p_mod_7']
                target=((2*r+1)*pow(r+3,-1,q) if h==2 else
                        (r+2)*pow(r-2,-1,q))%q
                assert target==branch['target']
                kept=[a for a in range(period)
                      if character==1 and a%3 and a%4 and
                      (a%2 or(q%12==7 and h==2)) and pow(B,a,q)==target]
                assert kept==branch['surviving_exponent_residues_mod_period']
                survivor_count+=len(kept)
                even_count+=sum(a%2==0 for a in kept)
        assert table['all_exponents_excluded']==(survivor_count==0)
        reproduced.append({'q':q,'period':period,'surviving_residues':survivor_count,
                           'surviving_even_residues':even_count})
    assert len(reproduced)==39
    assert all(t['surviving_even_residues']==0 for t in reproduced[21:38])
    assert sorted(t['q'] for t in reproduced[:21] if t['surviving_residues'])==[19,31,67]
    assert [q for q in primes_sieve(240) if q>211 and q%3==1]==[223,229]
    assert [q for q in primes_sieve(462) if q>367 and q%12==7]==[379,439]
    assert 463%12==7 and is_prime(463)

    result={
        'status':'PASS',
        'scope':'Uniform written auxiliary-ring obstructions; complete small finite-ring checks; no original-equation box search',
        'new_uniform_necessary_conditions':['3 does not divide a','B and m are odd','5 does not divide B',
            'p=2 mod7 implies B^2=(q+1)^2 mod7',
            'p=4 mod7 implies a odd and B=3+5q or 5+3q mod7',
            '5|m implies q=1 mod5 if p=2 mod7, q=4 mod5 if p=4 mod7'],
        'new_all_exponent_exclusions':[19,31,67,223,229,367,439],
        'additional_even_exponent_exclusions':[379],
        'intervening_even_residue_composites':even_interval_composites,
        'prime_shape_exclusion':'q=b^2+27*u^2, u nonzero; q prime',
        'trace_shape_exclusion':'primary trace B divisible by 5',
        'prime_p_cyclotomic_external_Thue_dependency_removed':True,
        'v7_all_integer_x_Thue_theorem_dependency_removed':False,
        'all_exponent_q_lower_bound':241,
        'even_exponent_q_lower_bound':463,
        'mod2_records':mod2,'mod5_records':mod5,'mod7_records':mod7,
        'mod5_trace_zero_branch_cases':trace_zero_cases,
        'mod5_scalar_branch_cases':scalar_cases,
        'pair_matrix_power_comparisons':comparison_count,
        'concrete_primary_orientations':concrete,
        'q19_quadratic_records':quadratic,
        'q19_trace_powers':trace_powers,
        'q19_complete_combined_period':120,
        'q19_forced_p_divisible_by_11_records':q19_records,
        'prior_complete_periods_reproduced':reproduced,
        'prior_complete_period_record_count':39,
        'prior_period_file_sha256':hashlib.sha256(prior_path.read_bytes()).hexdigest(),
        'independent_power_method':'Two-by-two matrices with separate repeated multiplication',
        'all_arithmetic_exact':True,
        'arbitrary_exponent_cutoff':False,
        'new_external_theorem_used':False,
        'whole_cyclotomic_branch_solved':False,
        'whole_original_equation_solved':False,
        'full_unbounded_theorems_Lean_formalized':False,
        'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'proof_note_sha256':hashlib.sha256((ROOT/'v10_cyclotomic_auxiliary_rings.md').read_bytes()).hexdigest(),
    }
    output=ROOT/'v10_cyclotomic_auxiliary_rings_verification.json'
    output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','pair_matrix_power_comparisons',
        'mod5_trace_zero_branch_cases','mod5_scalar_branch_cases',
        'prior_complete_period_record_count','all_exponent_q_lower_bound','even_exponent_q_lower_bound']}))


if __name__=='__main__':
    main()
