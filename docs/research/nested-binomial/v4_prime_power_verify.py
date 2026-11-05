"""Direct exact-integer consistency checks for v4_prime_power_reduction.md.

The universal results are proved in the note.  These finite checks are
not a claim of global nonexistence, nor a Lean formal proof.
No dependency on the p-adic exploratory implementation is used.
"""
import json
from math import comb, gcd, isqrt


def valuation(n, p):
    assert n > 0
    exponent = 0
    while n % p == 0:
        exponent += 1
        n //= p
    return exponent


def main():
    denominator_pairs = 0
    residual_congruences = 0
    for i in range(2, 81):
        for j in range(1, i):
            q = i // gcd(i,j)
            A, X = comb(i,j), comb(i*i,j*j)
            assert A % q == 0
            assert X % (q*q) == 0
            denominator_pairs += 1
            L = 1
            for r in range(1, min(2*j, A//2) + 1):
                L = L * (A-r+1) // r
                for B in {r, A-r}:
                    assert (r*(L-X-B*B)+r**3) % q == 0
                    residual_congruences += 1

    power_pairs = 0
    valuation_checks = 0
    normalized_unit_checks = 0
    higher_precision_checks = 0
    for p in range(2, 12):
        if any(p % divisor == 0 for divisor in range(2, isqrt(p)+1)):
            continue
        a = 1
        i = p
        while i <= 128:
            for j in range(1,i):
                A, X = comb(i,j), comb(i*i,j*j)
                b = valuation(j,p)
                c = a-b
                u = j//(p**b)
                assert valuation(A,p) == c
                assert valuation(X,p) == 2*c
                assert A//(p**c) % p == (-1)**(j-1)*pow(u,-1,p) % p
                power_pairs += 1
                L = 1
                for r in range(1,min(p**c-1,A//2)+1):
                    L = L*(A-r+1)//r
                    d = valuation(r,p)
                    v = r//(p**d)
                    assert valuation(L,p) == c-d
                    for B in {r,A-r}:
                        assert valuation(X+B*B,p) == 2*d
                        valuation_checks += 1
                        if c == 3*d:
                            modulus = p**(2*d)
                            assert (L-X-B*B) % modulus == 0
                            exact_residue = ((L-X-B*B)//modulus) % p
                            unit_residue = ((-1)**(j+r)*pow(u*v,-1,p)-v*v) % p
                            assert exact_residue == unit_residue
                            normalized_unit_checks += 1
                            if i >= 2*j and j+2 <= r < 2*j:
                                s=0
                                while p**(s+1) <= r-1:
                                    s+=1
                                exponent=min(2*d,3*d-s)
                                assert exponent>=1
                                precision=p**exponent
                                scaled=(u*v)*((L-X-B*B)//modulus)
                                predicted=(-1)**(j+r)-u*v**3
                                assert scaled%precision==predicted%precision
                                higher_precision_checks+=1
            i *= p
            a += 1

    output = {
        'status':'all_exact_consistency_checks_passed',
        'global_proof_source':'v4_prime_power_reduction.md',
        'formal_proof_assistant_executed_by_this_script':False,
        'arbitrary_i_range':[2,80],
        'primitive_denominator_pairs':denominator_pairs,
        'outer_residual_congruences':residual_congruences,
        'prime_power_i_max':128,
        'prime_power_pairs':power_pairs,
        'valuation_checks':valuation_checks,
        'normalized_unit_checks':normalized_unit_checks,
        'higher_precision_product_checks':higher_precision_checks,
    }
    with open('v4_prime_power_verification.json','w') as out:
        json.dump(output,out,indent=2)
    print(json.dumps(output,indent=2))


if __name__ == '__main__':
    main()
