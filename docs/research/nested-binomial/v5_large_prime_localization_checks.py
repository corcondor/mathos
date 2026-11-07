"""Compact exact checks for v5_large_prime_localization.md.

This is not a search for all solutions. The main claims in the note are
proved uniformly; these are small, reproducible checks of the formulas.
Only Python's standard library is used. Logarithmic comparisons use
rational enclosures, never floating-point branch decisions.
"""

from fractions import Fraction as Q
from functools import lru_cache
from math import comb, isqrt
from pathlib import Path
import json


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def scale(a, c):
    c = Q(c)
    return (a[0] * c, a[1] * c) if c >= 0 else (a[1] * c, a[0] * c)


def atan_unit_reciprocal(q, terms=40):
    """Alternating-series enclosure for atan(1/q)."""
    x = Q(1, q)
    power, value = x, Q(0)
    for n in range(terms):
        value += (-1 if n % 2 else 1) * power / (2 * n + 1)
        power *= x * x
    following = (-1 if terms % 2 else 1) * power / (2 * terms + 1)
    return min(value, value + following), max(value, value + following)


def quantize_outward(interval, places=30):
    """Return rational endpoints with a short common denominator."""
    d = 10**places
    lo, hi = interval
    nlo = (lo.numerator * d) // lo.denominator
    nhi = -((-hi.numerator * d) // hi.denominator)
    return Q(nlo, d), Q(nhi, d)


@lru_cache(maxsize=None)
def pi_interval():
    # Machin's identity pi = 16 atan(1/5) - 4 atan(1/239).
    answer = add(scale(atan_unit_reciprocal(5), 16),
                 scale(atan_unit_reciprocal(239), -4))
    return quantize_outward(answer, 50)


def log_reduced(x, terms=48):
    """For 1 <= x <= 2, enclose log(x) using 2 atanh((x-1)/(x+1))."""
    x = Q(x)
    assert 1 <= x <= 2
    z = (x - 1) / (x + 1)
    z2 = z * z
    power, value = z, Q(0)
    for n in range(terms):
        value += 2 * power / (2 * n + 1)
        power *= z2
    tail = 2 * power / ((2 * terms + 1) * (1 - z2))
    return value, value + tail


@lru_cache(maxsize=None)
def log_two():
    return log_reduced(Q(2))


@lru_cache(maxsize=None)
def log_positive_rational(x):
    x = Q(x)
    assert x >= 1
    s = x.numerator.bit_length() - x.denominator.bit_length()
    while Q(2)**s > x:
        s -= 1
    while Q(2)**(s + 1) <= x:
        s += 1
    reduced = x / Q(2)**s
    return add(scale(log_two(), s), log_reduced(reduced))


@lru_cache(maxsize=None)
def log_two_pi():
    lo, hi = pi_interval()
    return log_positive_rational(2 * lo)[0], log_positive_rational(2 * hi)[1]


def g_interval(j, p):
    # An algebraically rearranged form of equation (2) in the note.
    value = Q(p*j - j*j + p)
    out = value, value
    out = add(out, scale(log_positive_rational(Q(p)),
                         Q(3*p*j - 6*j*j - p) - Q(1, 2)))
    out = add(out, scale(log_positive_rational(Q(j)), Q(1) - Q(p, 2)))
    return add(out, scale(log_two_pi(), -Q(p, 2)))


def exact_sign(interval):
    lo, hi = interval
    if lo > 0:
        return 1
    if hi < 0:
        return -1
    raise ArithmeticError("The chosen precision did not certify this sign.")


def rational_pair(interval):
    return [str(x) for x in quantize_outward(interval, 20)]


def prime_check(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def localize(p):
    assert p >= 23 and prime_check(p)
    left, right = (p + 1)//2, p - 1
    if exact_sign(g_interval(left, p)) < 0:
        return {
            "p": p,
            "first_allowed_integer": left,
            "G_at_first_integer_rational_interval": rational_pair(g_interval(left, p)),
            "conclusion": "G is already negative; every larger j is excluded.",
        }
    assert exact_sign(g_interval(right, p)) < 0
    # Maintain G(left)>0 and G(right)<0; monotonicity was proved in the note.
    while right - left > 1:
        mid = (left + right)//2
        if exact_sign(g_interval(mid, p)) > 0:
            left = mid
        else:
            right = mid
    interval = g_interval(left, p)
    excluded = interval[0] >= Q(1, 3)
    return {
        "p": p,
        "last_integer_with_G_positive": left,
        "G_at_that_integer_rational_interval": rational_pair(interval),
        "next_integer": right,
        "G_at_next_integer_rational_interval": rational_pair(g_interval(right, p)),
        "all_j_excluded_by_G": excluded,
        "reason": "G(j,p) > 1/3 at the last positive integer; all others are ruled out by monotonicity."
                  if excluded else "The unique possible integer needs the remaining tests.",
    }


def check_harmonic_identity(p, j):
    m = p**5
    H = sum(pow(h, -1, m) for h in range(1, j)) % m
    H2 = sum(pow(h, -2, m) for h in range(1, j)) % m
    K = sum(pow(h, -1, m) for h in range(1, p)) % m
    K2 = sum(pow(h, -2, m) for h in range(1, p)) % m
    assert H % p == 0 and K % (p*p) == 0
    A = comb(j*p**3, j)
    X = comb(j*j*p**6, j*j)
    L = comb(A, p)
    residual = L - X - p*p
    assert residual % (p**5) == 0
    actual = (-(residual // p**5)) % m
    predicted = (j*H + K + p + p**3 * pow(2, -1, m) * (j*j*H2 + K2)) % m
    assert actual == predicted
    return {
        "p": p, "j": j,
        "H_j_minus_1_mod_p": H % p,
        "predicted_negative_scaled_residual_mod_p5": predicted,
        "actual_negative_scaled_residual_mod_p5": actual,
        "identity_verified": True,
        "L_bit_length": L.bit_length(), "X_bit_length": X.bit_length(),
    }


def main():
    negative_error_bound = Q(1,276) + Q(1,6) + Q(1,44) + Q(1,23**4)
    positive_error_bound = Q(1,3*23**2) + Q(1,23**4)
    assert negative_error_bound < Q(1,4)
    assert positive_error_bound < Q(1,13)
    report = {
        "scope": "Small formula checks only; no claim to enumerate all primes or all solutions.",
        "exact_constant_checks": {
            "negative_error_bound": str(negative_error_bound),
            "less_than_one_quarter": True,
            "positive_error_bound": str(positive_error_bound),
            "less_than_one_thirteenth": True,
        },
        "certified_localization_examples": [localize(p) for p in (23, 101, 1009, 1000003)],
        "exact_harmonic_identity_checks": [
            check_harmonic_identity(p, j) for p, j in ((53,31), (61,51), (109,65))
        ],
    }
    destination = Path(__file__).with_name("v5_large_prime_localization_verification.json")
    destination.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
