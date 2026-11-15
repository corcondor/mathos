#!/usr/bin/env python3
"""Exact, dependency-free modular checks for F(n)=45**n+n.

Does not claim a primality proof for large candidates or Lean formalization.
Run: python3 verify_45n_plus_n.py
"""
from __future__ import annotations
import json
from math import gcd, lcm

BASE = 45


def is_prime_trial(x: int) -> bool:
    if x < 2:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1 if d == 2 else 2
    return True


def prime_divisors(n: int) -> list[int]:
    ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            ans.append(d)
            while n % d == 0:
                n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        ans.append(n)
    return ans


def order_45(p: int) -> int:
    if not is_prime_trial(p) or gcd(p, 45) != 1:
        raise ValueError("p must be prime and coprime to 45")
    order = p - 1
    for q in prime_divisors(order):
        while order % q == 0 and pow(45, order // q, p) == 1:
            order //= q
    assert pow(45, order, p) == 1
    return order


def root_for_r(p: int, r: int) -> tuple[int, int]:
    """Unique root n modulo p*d with n == r (mod d), d=ord_p(45)."""
    d = order_45(p)
    if not (0 <= r < d):
        raise ValueError("r must be in [0, d)")
    # Chinese remainder theorem; d divides p-1, hence invertible modulo p.
    t = ((-pow(45, r, p) - r) * pow(d, -1, p)) % p
    n = r + d * t
    assert 0 <= n < p * d
    assert (pow(45, n, p) + n) % p == 0
    return n, p * d


def classes_mod_p(p: int) -> tuple[int, list[int]]:
    d = order_45(p)
    return p * d, sorted(root_for_r(p, r)[0] for r in range(d))


def lift_root(p: int, r: int, e: int) -> tuple[int, int]:
    """Lift one root branch to p**e, unique mod d*p**e (odd p only)."""
    if p == 2 or e < 1:
        raise ValueError("Require odd prime p and exponent e >= 1")
    n, period = root_for_r(p, r)
    d = order_45(p)
    for level in range(1, e):
        modulus = p ** (level + 1)
        f_remainder = (pow(45, n, modulus) + n) % modulus
        assert f_remainder % (p**level) == 0
        t = -(f_remainder // (p**level)) * pow(d, -1, p) % p
        n += t * period
        period *= p
        assert (pow(45, n, modulus) + n) % modulus == 0
    return n, period


def sophie_factors(t: int) -> tuple[int, int]:
    """Factor 45**(4*t**4) + 4*t**4 by Sophie Germain's identity."""
    if t < 1:
        raise ValueError("t must be positive")
    x = pow(45, t**4)
    y = t
    return x*x - 2*x*y + 2*y*y, x*x + 2*x*y + 2*y*y


def run() -> dict:
    # Exhaustive CRT-class checks for the first few admissible primes.
    prime_checks = []
    for p in range(2, 51):
        if not is_prime_trial(p) or p in (3, 5):
            continue
        period, classes = classes_mod_p(p)
        d = order_45(p)
        assert len(classes) == d and len(set(classes)) == d
        # Exact equivalence over a complete period.
        class_set = set(classes)
        for n in range(period):
            assert ((pow(45, n, p) + n) % p == 0) == (n in class_set)
        prime_checks.append(p)

    # Verify unique p-adic lifts: for every r at p = 7,11,13,19,23,29,31.
    lift_checks = []
    for p in (7, 11, 13, 19, 23, 29, 31):
        for r in range(order_45(p)):
            before, period = root_for_r(p, r)
            for e in range(1, 4):
                lifted, new_period = lift_root(p, r, e)
                assert new_period == order_45(p) * p**e
                assert lifted % period == before
                assert (pow(45, lifted, p**e) + lifted) % p**e == 0
        lift_checks.append(p)

    for t in (1, 2, 3):
        left, right = sophie_factors(t)
        assert left > 1 and right > 1
        assert left * right == pow(45, 4 * t**4) + 4 * t**4
    assert sophie_factors(1) == (1937, 2117)

    # Direct modular examples; the huge integers themselves are never materialized.
    examples = {
        "7*11*31 divides F(362)": (7*11*31, 362),
        "11*23 divides F(758)": (11*23, 758),
        "7^5 divides F(1328)": (7**5, 1328),
        "11^3 divides F(164)": (11**3, 164),
        "7*11*13 divides F(5004)": (7*11*13, 5004),
        "1729 divides F(1728)": (1729, 1728),
        "7 divides F(48)": (7, 48),
        "7 divides F(216)": (7, 216),
    }
    for desc, (modulus, n) in examples.items():
        assert (pow(45, n, modulus) + n) % modulus == 0, desc
    assert gcd(362, 15) == 1 and gcd(758, 15) == 1
    assert pow(45, 30, 2387) == 1
    assert 362 % 30 == 2 and (45**2 + 362) == 2387
    assert pow(45, 2, 253) == 1
    assert 758 % 2 == 0 and (758 + 1) % 253 == 0
    assert 1729 == 7 * 13 * 19
    assert 1728 % lcm(6, 12, 18) == 0

    # Exponent-of-exponent family: n=2**(18*t+3) always has a factor 19.
    assert order_45(19) == 3
    for t in range(4):
        n = 2 ** (18 * t + 3)
        assert (pow(45, n, 19) + n) % 19 == 0
    assert pow(2, 18, 57) == 1

    root_7_2 = [lift_root(7, 2, e)[0] for e in range(1, 7)]
    root_11_0 = [lift_root(11, 0, e)[0] for e in range(1, 5)]
    assert root_7_2 == [26, 152, 1328, 1328, 1328, 303854]
    assert root_11_0 == [10, 43, 164, 13474]
    assert (pow(45, 1328, 7**6) + 1328) % (7**6) != 0
    assert (pow(45, 164, 11**4) + 164) % (11**4) != 0

    return {
        "status": "PASS exact modular tests (not primality certification)",
        "primes_exhaustively_checked": prime_checks,
        "prime_power_lifts_checked_for": lift_checks,
        "p7_r2_roots_for_e_1_to_6": root_7_2,
        "p11_r0_roots_for_e_1_to_4": root_11_0,
        "sophie_germain_n4_factors": [1937, 2117],
        "exponential_subsequence": "19 divides F(2**(18*t+3)) for every t >= 0",
        "divisibility_examples": {key: {"modulus": v[0], "n": v[1]} for key,v in examples.items()},
    }


if __name__ == "__main__":
    print(json.dumps(run(), ensure_ascii=False, indent=2))
