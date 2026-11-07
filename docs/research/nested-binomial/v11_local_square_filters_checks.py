#!/usr/bin/env python3
"""Exact local-unit and square-filter verification, with reusable CRT inputs.

No search of the original equation is performed. The infinite results are
proved in the companion note; the finite checks audit its identities.
"""
from pathlib import Path
from functools import lru_cache
from fractions import Fraction
from math import comb, factorial, gcd, isqrt
import hashlib
import json

ROOT = Path(__file__).resolve().parent


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))


def primes_to(limit):
    return [p for p in range(2, limit+1) if prime(p)]


def vp(n, p):
    assert n
    a = 0
    while n % p == 0:
        n //= p
        a += 1
    return a


def factorial_valuation(n, p):
    total = 0
    while n:
        n //= p
        total += n
    return total


def carry_valuation(n, k, p):
    a, b, carry, count = k, n-k, 0, 0
    while a or b or carry:
        carry = (a % p + b % p + carry) // p
        count += carry
        a //= p
        b //= p
    return count


@lru_cache(maxsize=None)
def unit_block(p, precision):
    modulus = p ** precision
    values = [1] * modulus
    for t in range(1, modulus):
        values[t] = values[t-1] * (t if t % p else 1) % modulus
    expected = (-1) % modulus if p != 2 or precision == 2 else 1
    assert values[-1] == expected
    return modulus, values, expected


def factorial_unit(n, p, precision):
    modulus, block, epsilon = unit_block(p, precision)
    value = 1
    while n:
        value = value * pow(epsilon, n // modulus, modulus) * block[n % modulus] % modulus
        n //= p
    return value


def binomial_unit(n, k, p, precision=1):
    """Return (valuation, binomial with all p factors removed modulo p^precision)."""
    assert prime(p) and precision >= 1 and 0 <= k <= n
    x = factorial_valuation(n,p)-factorial_valuation(k,p)-factorial_valuation(n-k,p)
    modulus = p ** precision
    unit = factorial_unit(n,p,precision)
    unit = unit * pow(factorial_unit(k,p,precision), -1, modulus) % modulus
    unit = unit * pow(factorial_unit(n-k,p,precision), -1, modulus) % modulus
    return x, unit


def binomial_unit_digits(n, k, p):
    """Separate precision-one calculation, by digit factorials and carries."""
    d = n-k
    x = carry_valuation(n,k,p)
    value = pow(-1,x,p)
    while n or k or d:
        value = value * factorial(n%p) % p
        value = value * pow(factorial(k%p)*factorial(d%p), -1, p) % p
        n //= p
        k //= p
        d //= p
    return x, value


def binomial_unit_direct(n, k, p, precision):
    """Independent product method; strip individual numerator/denominator factors."""
    modulus = p ** precision
    numerator = denominator = 1
    valuation = 0
    for t in range(1,k+1):
        a,b = n-k+t,t
        while a%p==0:
            a//=p
            valuation+=1
        while b%p==0:
            b//=p
            valuation-=1
        numerator=numerator*(a%modulus)%modulus
        denominator=denominator*(b%modulus)%modulus
    return valuation, numerator*pow(denominator,-1,modulus)%modulus


def factors(n):
    out={}
    p=2
    while p*p<=n:
        if n%p==0:
            a=0
            while n%p==0:
                n//=p
                a+=1
            out[p]=a
        p+=1
    if n>1:
        out[n]=1
    return out


def square_unit(unit,p,d):
    assert d>=1 and unit%p
    if p!=2:
        return pow(unit,(p-1)//2,p)==1
    return unit%(2**min(d,3))==1


def candidate_square_record(n):
    """Full local certificate for E and E_sq; factor only the three small consecutive factors."""
    A=n*(n-1)*(n-2)//6
    fac={}
    for value in (n,n-1,n-2):
        for p,a in factors(value).items():
            fac[p]=fac.get(p,0)+a
    fac[2]-=1
    fac[3]-=1
    fac={p:a for p,a in fac.items() if a}
    check=1
    for p,a in fac.items():
        assert prime(p)
        check*=p**a
    assert check==A
    E=Esq=1
    records=[]
    for p,alpha in sorted(fac.items()):
        x=factorial_valuation(n*n,p)-factorial_valuation(6*n-9,p)-factorial_valuation((n-3)**2,p)
        assert x==carry_valuation(n*n,6*n-9,p)
        d=max(alpha-3*(x//2),0) if x%2==0 else 0
        rec={'p':p,'alpha':alpha,'x':x,'critical_defect_exponent':d}
        if d:
            precision=1 if p!=2 else min(d,3)
            xx,unit=binomial_unit(n*n,6*n-9,p,precision)
            assert xx==x
            assert (x,unit%p)==binomial_unit_digits(n*n,6*n-9,p)
            modulus=p**precision
            minus_unit=(-unit)%modulus
            remains=square_unit(minus_unit,p,d)
            E*=p**d
            if remains:
                Esq*=p**d
            rec.update({'square_test_modulus':modulus,'normalized_X_unit':unit,
                        'negative_unit':minus_unit,'is_square':remains,
                        'Euler_power':pow(minus_unit,(p-1)//2,p) if p!=2 else None})
        records.append(rec)
    return {'n':n,'A':A,'factorization_A':fac,'prime_records':records,'E':E,'E_square':Esq}


def rational_constant(c):
    value=Fraction(1)
    for h in range(c):
        value*=Fraction(c-3-3*h,3*(h+1))
    return value


def main():
    odd_primes=[p for p in primes_to(127) if p!=2]
    uniform=multiple_beta=base_three=first_exponent=direct_exact=0
    samples=[]
    for w in range(1,65):
        B=comb(6*w,2*w)
        for p in odd_primes:
            if w%p==0:
                continue
            beta=vp(B,p)
            Uw=B//p**beta
            target=(-2*w*pow(Uw,-1,p))%p
            for a in range(1,7):
                q=p**a
                if q<=4*w:
                    continue
                n=w*q+2
                x,unit=binomial_unit(n*n,6*n-9,p)
                assert (x,unit)==binomial_unit_digits(n*n,6*n-9,p)
                assert x==a-beta and unit==target
                assert pow(-unit,(p-1)//2,p)==pow(2*w*Uw,(p-1)//2,p)
                uniform+=1
                multiple_beta+=beta>1
                base_three+=p==3
                first_exponent+=a==1
                if n<=256:
                    exact=comb(n*n,6*n-9)
                    assert vp(exact,p)==x and exact//p**x%p==unit
                    direct_exact+=1
                if len(samples)<15 and beta>0:
                    samples.append({'w':w,'p':p,'a':a,'n':n,'beta':beta,
                                    'valuation_X':x,'unit_X':unit,'character_negative_unit':pow(-unit,(p-1)//2,p)})

    higher_precision=exact_binomial=0
    for p in [2,3,5,7,11,13]:
        for precision in range(1,5):
            modulus=p**precision
            ns=sorted(set([0,1,p-1,p,p+1,p*p-1,p*p,p*p+1,2*p*p+1,modulus+2]))
            for n in ns:
                ks=sorted(set([0,1,n//2,max(0,n-1),n]))
                for k in ks:
                    if k>n:
                        continue
                    result=binomial_unit(n,k,p,precision)
                    assert result==binomial_unit_direct(n,k,p,precision)
                    exact=comb(n,k)
                    x=vp(exact,p)
                    assert result==(x,exact//p**x%modulus)
                    higher_precision+=1
                    exact_binomial+=1

    band_cases=band_nonsquares=0
    for w in range(1,101):
        B=comb(6*w,2*w)
        for p in primes_to(6*w-1):
            if p<=4*w:
                continue
            assert vp(B,p)==1
            t=p-4*w
            assert t%2==1
            Uw=B//p
            assert Uw%p==pow(t*comb(2*w,t),-1,p)
            J=comb(2*w-1,t-1)
            expected=(2*w)**2*J%p
            assert expected==2*w*pow(Uw,-1,p)%p
            for a in [1,4,7]:
                n=w*p**a+2
                x,unit=binomial_unit(n*n,6*n-9,p)
                assert x==a-1 and (-unit)%p==expected
                band_cases+=1
            band_nonsquares+=pow(J,(p-1)//2,p)==p-1

    constants=[]
    fixed_offset_cases=0
    expected_constants={1:(Fraction(-2,3),-6),5:(Fraction(14,729),14),
                        7:(Fraction(-88,19683),-66),11:(Fraction(3952,14348907),741)}
    for c,(expected,Dc) in expected_constants.items():
        value=rational_constant(c)
        assert value==expected
        ratio=value/Dc
        assert isqrt(ratio.numerator)**2==ratio.numerator
        assert isqrt(ratio.denominator)**2==ratio.denominator
        constants.append({'c':c,'numerator':value.numerator,'denominator':value.denominator,
                          'integer_character':Dc,'square_multiplier_numerator':ratio.numerator,
                          'square_multiplier_denominator':ratio.denominator})
        for p in primes_to(1000):
            if p<=2*c or (p+c)%6:
                continue
            w=(p+c)//6
            assert 4*w<p<6*w
            J=comb(2*w-1,c)
            assert J%p==value.numerator*pow(value.denominator,-1,p)%p
            assert pow(J,(p-1)//2,p)==pow(Dc,(p-1)//2,p)
            fixed_offset_cases+=1
    gauss_prime_checks=0
    for p in primes_to(10000):
        if p%24 not in (17,23):
            continue
        assert pow(-6,(p-1)//2,p)==p-1
        assert ((p-1)//2-p//4)%2==0
        assert ((p//3-p//6)%2)==(1 if p%24==17 else 0)
        gauss_prime_checks+=1

    # Polynomial identity in the infinite-range bound, coefficient by coefficient.
    assert 27*59-500==1093
    assert 27*59**2-1000*59==34987
    assert 9*59**3-500*59**2-8000==99911
    assert all(c>0 for c in [9,1093,34987,99911])
    boundary=[(w,p) for p in primes_to(53) for w in range(13,p//4+1) if 4*w<p<6*w]
    assert boundary==[(13,53)]
    assert comb(25,53-52-1)==1

    examples=[]
    for w,p,c,Dc in [(19,113,1,-6),(23,137,1,-6),(41,241,5,14)]:
        assert prime(p) and p==6*w-c and pow(Dc,(p-1)//2,p)==p-1
        for t in range(3):
            a=3*t+1
            n=w*p**a+2
            x,unit=binomial_unit(n*n,6*n-9,p)
            assert x==a-1 and pow(-unit,(p-1)//2,p)==p-1
            examples.append({'w':w,'p':p,'c':c,'a':a,'n':n,'valuation_X':x,
                             'negative_leading_unit':(-unit)%p,'nonresidue_Euler_power':p-1})

    local_examples=[candidate_square_record(n) for n in [289,6860,2149,3153,9883]]
    hardest=next(x for x in local_examples if x['n']==6860)
    assert hardest['E']==1143 and hardest['E_square']==9
    row127=next(x for x in hardest['prime_records'] if x['p']==127)
    assert (row127['x'],row127['normalized_X_unit'],row127['negative_unit'],row127['Euler_power'])==(0,35,92,126)
    row3=next(x for x in hardest['prime_records'] if x['p']==3)
    assert row3['critical_defect_exponent']==2 and row3['is_square']

    # A separate small-digit certificate for the former exceptional index.
    base127_digits=[]
    for value in [6860**2,6*6860-9,(6860-3)**2]:
        digits=[]
        while value:
            digits.append(value%127)
            value//=127
        base127_digits.append(digits+[0]*(4-len(digits)))
    assert base127_digits==[[4,89,123,22],[3,70,2,0],[1,19,121,22]]
    assert all(a==b+c for a,b,c in zip(*base127_digits))
    small_binomial_residues=[comb(a,b)%127 for a,b in zip(base127_digits[0],base127_digits[1])]
    assert small_binomial_residues==[4,112,10,1]
    assert 4*112*10%127==35 and pow(92,63,127)==126

    result={
        'status':'PASS',
        'scope':'Exact checks of uniform local-unit and square-filter proofs; no search of the original equation',
        'uniform_odd_unit_formula':'For n=w*p^a+2, p odd prime, p does not divide w, p^a>4w: v_p(X)=a-beta and X/p^(a-beta)=-2w/(C(6w,2w)/p^beta) modulo p',
        'uniform_formula_cases':uniform,'cases_with_beta_greater_than_one':multiple_beta,
        'prime_three_cases':base_three,'exponent_one_cases':first_exponent,
        'uniform_formula_direct_exact_binomial_checks':direct_exact,
        'uniform_formula_range':{'w':[1,64],'odd_primes_at_most':127,'a':[1,6],
                                 'restrictions':'p does not divide w, p^a>4w'},
        'sample_uniform_records':samples,
        'higher_precision_product_and_exact_binomial_checks':higher_precision,
        'higher_precision_primes':[2,3,5,7,11,13],'higher_precision_range':[1,4],
        'band_unit_formula_cases':band_cases,'band_nonsquare_prime_cofactor_pairs':band_nonsquares,
        'band_check_range':{'w':[1,100],'p':'all primes with4w<p<6w','a':[1,4,7]},
        'fixed_offset_constant_checks':fixed_offset_cases,'fixed_offset_constants':constants,
        'gauss_residue_check_primes':gauss_prime_checks,'gauss_residue_check_bound':10000,
        'large_prime_contradiction_polynomial':[9,1093,34987,99911],
        'small_boundary_pair':[13,53],'small_boundary_binomial':1,
        'proved_unbounded_exclusion':'4w<p<6w and C(2w-1,p-4w-1) a quadratic nonresidue modulo p excludes n=w*p^(3t+1)+2 for every t>=0',
        'explicit_prime_progression_family':'n=((p+1)/6)*p^(3t+1)+2, prime p=17 or23 mod24, t>=0',
        'example_infinite_subfamilies':['19*113^(3t+1)+2','23*137^(3t+1)+2','41*241^(3t+1)+2'],
        'sample_family_records':examples,'complete_local_example_records':local_examples,
        'hardest_v10_index_6860_now_excluded_by':'E_square=9 after removing127 by a nonsquare unit; existing CF threshold suffices',
        'index_6860_separate_small_certificate':{'prime':127,'base_p_digits_least_significant_first':base127_digits,
            'small_binomial_residues':small_binomial_residues,'unit_X':35,'negative_unit':92,
            'Euler_power':126,'E':1143,'E_square':9},
        'all_arithmetic_exact':True,'new_external_classification_theorem_used':False,
        'arbitrary_exponent_cutoff_used_in_proof':False,'full_unbounded_theorems_Lean_formalized':False,
        'whole_original_equation_solved':False,
        'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'proof_note_sha256':hashlib.sha256((ROOT/'v11_local_square_filters.md').read_bytes()).hexdigest(),
    }
    output=ROOT/'v11_local_square_filters_verification.json'
    output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','uniform_formula_cases',
        'cases_with_beta_greater_than_one','prime_three_cases',
        'uniform_formula_direct_exact_binomial_checks',
        'higher_precision_product_and_exact_binomial_checks','band_unit_formula_cases',
        'band_nonsquare_prime_cofactor_pairs','fixed_offset_constant_checks']}))


if __name__=='__main__':
    main()
