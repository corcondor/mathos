#!/usr/bin/env python3
"""Exact, finite certificates for v7_offset_shifted_prime_powers.md.

No unbounded claim is inferred from the representative identity checks.
The proof supplies the uniform statements and the finite exceptional cases.
Only Python's standard library is used.
"""

from hashlib import sha256
from math import comb, gcd, isqrt, prod
from pathlib import Path
import json


def prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    return all(n % q for q in range(3, isqrt(n) + 1, 2))


def factor(n):
    assert n >= 1
    out = {}
    p = 2
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            out[p] = e
        p = 3 if p == 2 else p + 2
    if n > 1:
        out[n] = 1
    return out


def vp(n, p):
    assert n > 0 and prime(p)
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def factorial_vp(n, p):
    e = 0
    while n:
        n //= p
        e += n
    return e


def binomial_vp(n, k, p):
    assert 0 <= k <= n
    return factorial_vp(n, p) - factorial_vp(k, p) - factorial_vp(n - k, p)


def c3(n):
    return prod(p ** ((e + 2) // 3) for p, e in factor(n).items())


def certify_factorization(n, expected):
    assert all(prime(p) and e >= 1 for p, e in expected.items())
    assert prod(p ** e for p, e in expected.items()) == n
    return {"n": n, "factorization": {str(p): e for p, e in expected.items()}}


def normalized_product_binomial(n, k, p, modulus):
    """Return valuation and the p-coprime part modulo a p-power."""
    e = 0
    unit = 1
    for j in range(1, k + 1):
        top, bottom = n - k + j, j
        while top % p == 0:
            top //= p
            e += 1
        while bottom % p == 0:
            bottom //= p
            e -= 1
        unit = unit * (top % modulus) * pow(bottom, -1, modulus) % modulus
    return e, unit


report = {
    "status": "pass",
    "scope": "finite exact checks supporting the separate uniform written proof",
    "formalization": "new v7 arguments are not Lean formalizations",
    "small_exceptions": [],
    "valuation_examples": [],
    "normalized_base_three_examples": [],
    "cubic_nonresidues": [],
    "wieferich_certificates": [],
    "integer_thresholds": [],
}


# These are the exceptional exponents explicitly derived in the proof.
squarefree_cases = [
    (2, 9, {2: 1, 257: 1}),
    (2, 12, {2: 1, 3: 1, 683: 1}),
    (3, 6, {17: 1, 43: 1}),
    (3, 7, {11: 1, 199: 1}),
    (5, 3, {127: 1}),
    (5, 4, {3: 1, 11: 1, 19: 1}),
    (5, 5, {53: 1, 59: 1}),
]
for b, a, expected in squarefree_cases:
    n = b ** a + 2
    entry = certify_factorization(n, expected)
    q0 = n // gcd(n, 3)
    assert all(e == 1 for e in factor(q0).values())
    entry.update(base=b, exponent=a, exclusion="n/gcd(n,3) squarefree", q0=q0)
    report["small_exceptions"].append(entry)

n = 3 ** 5 + 2
assert n == 245
entry = certify_factorization(n, {5: 1, 7: 2})
q0, D = n // gcd(n, 3), (n - 1) // gcd(n - 1, 6)
assert q0 == 245 and D == 122 and gcd(q0, D) == 1
forced = c3(q0) * c3(D)
assert forced == 4270 and 3 * forced > 10 * n
entry.update(base=3, exponent=5, exclusion="forced divisor exceeds 10n/3", forced_r_divisor=forced)
report["small_exceptions"].append(entry)


# Representative checks of the block identity and outer valuations.
# This is an identity test, not a candidate search or an exponent cutoff.
examples = [(2, 7), (2, 9), (2, 12), (3, 7), (3, 9),
            (5, 3), (5, 5), (5, 8), (7, 3), (11, 3), (13, 3), (19, 3)]
for p, a in examples:
    z, n = p ** a, p ** a + 2
    A, N, m = comb(n, 3), n * n, 6 * n - 9
    x_v = binomial_vp(N, m, p)
    block_v = binomial_vp(4, 3, p) + binomial_vp(z + 4, 6, p)
    expected_x_v = a + 1 if p == 2 else a - 1 if p in (3, 5) else a
    assert x_v == block_v == expected_x_v
    if p == 3:
        alpha, block = a - 1, 9
        expected_h_v = a - 1
    else:
        alpha, block = a, 3
        expected_h_v = 3 if p == 2 else 1 if p == 5 else 0
    scale = p ** alpha
    T = A // scale
    assert A % scale == 0 and T % p != 0
    h_v = binomial_vp(T - 1, block, p)
    assert h_v == expected_h_v
    r_samples = []
    # The three displayed choices stay inside the same proven upper block.
    for u in (7, 8, min(19, scale - 1)):
        r = block * scale + u
        assert 0 < u < scale
        d = vp(r, p)
        lhs_v = binomial_vp(A, r, p)
        assert lhs_v == alpha - d + h_v
        r_samples.append({"r": r, "valuation_r": d, "valuation_L": lhs_v})
    report["valuation_examples"].append({
        "prime": p, "exponent": a, "n": n,
        "valuation_X": x_v, "valuation_upper_block": h_v,
        "r_samples": r_samples,
    })


# Check the normalized base-three identity by independent exact methods.
for a in (5, 6, 7):
    z, n = 3 ** a, 3 ** a + 2
    N, m = n * n, 6 * n - 9
    e, unit = normalized_product_binomial(N, m, 3, 9)
    assert e == a - 1 and unit == 5
    exact = comb(N, m)
    assert exact % (3 ** (a - 1)) == 0
    assert exact // (3 ** (a - 1)) % 9 == 5
    report["normalized_base_three_examples"].append({
        "exponent": a, "valuation_X": e, "unit_mod_9": unit,
        "methods": ["factor-by-factor unit product", "direct integer binomial"],
    })
assert [v for v in range(9) if v * v % 9 == 4] == [2, 7]


for p in (13, 19):
    cubes = sorted({pow(t, 3, p) for t in range(p)})
    residue = 120 % p
    assert residue not in cubes and (-residue) % p not in cubes
    report["cubic_nonresidues"].append({
        "prime": p, "120_mod_p": residue, "cubes_mod_p": cubes,
    })


named = [(2, 1093, 364), (2, 3511, 1755),
         (3, 11, 5), (3, 1006003, 1006002),
         (5, 20771, 10385), (5, 40487, 40486)]
for b, q, f in named:
    assert prime(q) and (q - 1) % f == 0
    assert pow(b, f, q) == 1
    order_tests = {str(t): pow(b, f // t, q) for t in factor(f)}
    assert all(r != 1 for r in order_tests.values())
    mod_q2, mod_q3 = pow(b, f, q * q), pow(b, f, q ** 3)
    assert mod_q2 == 1 and mod_q3 != 1
    assert pow(b, q - 1, q * q) == 1
    report["wieferich_certificates"].append({
        "base": b, "prime": q, "exact_order": f, "exact_e": 2,
        "order_prime_divisor_tests": order_tests,
        "b_to_f_mod_q2": mod_q2, "b_to_f_mod_q3": mod_q3,
        "can_divide_plus_power": f % 2 == 0,
        "required_exponent_divisor": f // 2 if f % 2 == 0 else None,
    })


def threshold(name, lhs, rhs):
    assert lhs > rhs
    report["integer_thresholds"].append({"name": name, "lhs": lhs, "rhs": rhs, "margin": lhs - rhs})


# Lower bounds for W exceed one at the first required exponent.
threshold("base 2, h=5, W>1", 2 ** 6 * (2 ** 15 + 1), 50 * (2 ** 15 + 2))
threshold("base 3, a=9, W>1", 3 ** 5 * (3 ** 9 + 1), 180 * (3 ** 9 + 2))
threshold("base 5, a=8, W>1", 3 * 5 ** 3 * (5 ** 8 + 1), 160 * (5 ** 8 + 2))
threshold("base 5, a=11, weaker W>1", 5 ** 4 * (5 ** 11 + 1), 220 * (5 ** 11 + 2))

# The finite-set contradiction thresholds, each below the forced order.
threshold("base 2 finite-set contradiction, h=18", 2 ** 18, 10 * 18 * 1093)
threshold("base 3 finite-set contradiction, a=39", 3 ** 20, 40 * 39 * 1006003)
threshold("base 5 finite-set contradiction, a=35", 5 ** 12, 40 * 35 * 40487)
assert gcd(182, 3) == 1 and 182 > 18
assert 503001 > 39 and 503001 % 2 == 1
assert 20243 > 35 and 20243 % 3 == 2


report["counts"] = {key: len(value) for key, value in report.items() if isinstance(value, list)}
script_path = Path(__file__).resolve()
report["checker_sha256"] = sha256(script_path.read_bytes()).hexdigest()
output = script_path.with_name("v7_offset_shifted_prime_powers_verification.json")
output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
print(json.dumps({"status": report["status"], "counts": report["counts"], "output": str(output)}, sort_keys=True))
