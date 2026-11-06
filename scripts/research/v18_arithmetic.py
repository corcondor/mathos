"""Exact, standard-library arithmetic for the v18 Actions experiments.

Implements the published necessary conditions, not a new reduction proof.
The residual j/rho and canonical cofactor J are DIFFERENT parameters.
"""
from array import array
from math import comb, gcd, isqrt

DENOMINATORS = (1, 2, 3, 6, 9, 18, 27, 54, 81, 162, 243, 486)
PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43)


def pairs(a_max):
    """Remaining ratio domain after v17 excluded 27*a < 31*b."""
    return [(a, b) for a in range(1, a_max + 1) for b in DENOMINATORS
            if gcd(a, b) == 1 and 27*a >= 31*b]


def curve_coefficients(a, b):
    return (-3*b*b*(72*a*a+b*b),
            2*b*b*(648*a**4+180*a*a*b*b-b**4))


def residual_points(a, b):
    """Exhaust every allowed rho, including both signs, on ORIGINAL model."""
    c4, c6 = curve_coefficients(a, b)
    upper = (216*a*a+760*b*b-1)//1377
    result = []
    count = 0
    for rho in range(a*a % b or b, upper+1, b):
        count += 1
        x = 4*a*a-b*b-4*rho
        rhs = x**3+c4*x+c6
        if rhs < 0:
            continue
        y = isqrt(rhs)
        if y*y != rhs:
            continue
        assert y % 4 == 0
        for signed in sorted({y, -y}):
            result.append({"rho": rho, "X": x, "Y": signed})
    return {"complete": True, "rho_upper": upper, "rho_tested": count,
            "method": "exact integer square root over every admissible rho",
            "domain": "rho>0; rho=a^2 mod b; 1377*rho<216*a^2+760*b^2",
            "model": "original integral model; no minimal-model integrality inference",
            "points": result}


def lucas(n, k, p):
    value = 1
    while n or k:
        ni, ki = n % p, k % p
        if ki > ni:
            return 0
        value = value*comb(ni, ki) % p
        n //= p
        k //= p
    return value


def modular_witness(n, r, epsilon):
    """binom(binom(n,3),k) = binom(n^2,(n-3)^2) + k^2."""
    outer = comb(n, 3)
    k = outer-r if epsilon else r
    for p in PRIMES:
        left = lucas(outer, k, p)
        right = (lucas(n*n, (n-3)**2, p)+k*k) % p
        if left != right:
            return {"prime": p, "left": left, "right": right}
    return None  # Necessary-condition survivor, NEVER a solution claim.


def spf_sieve(limit):
    """Smallest prime factors, 4 bytes per index; no CAS factoring per n."""
    spf = array('I', range(limit+1))
    for p in range(2, isqrt(limit)+1):
        if spf[p] == p:
            for n in range(p*p, limit+1, p):
                if spf[n] == n:
                    spf[n] = p
    return spf


def factors(n, spf):
    result = {}
    while n > 1:
        p, e = spf[n], 0
        while n % p == 0:
            n //= p
            e += 1
        result[p] = e
    return result


def forced_r_divisor(n, spf):
    """Least F such that Q|r^3 iff F|r, Q=n(n-1)/M (v18 (1))."""
    fs = factors(n, spf)
    for p, e in factors(n-1, spf).items():
        fs[p] = fs.get(p, 0)+e
    m = gcd(n, 3)*gcd(n-1, 6)
    for p, e in factors(m, spf).items():
        fs[p] -= e
    f = 1
    for p, e in fs.items():
        f *= p**((e+2)//3)
    return f


def n_height_exclusive(j, epsilon):
    """Integer H such that n<H. Uses strict integer-root rounding."""
    if epsilon == 0:
        radicand, degree = (1 << 352)*j**33, 14
        lo, hi = 0, 1
        while hi**degree < radicand:
            hi *= 2
        while hi-lo > 1:
            mid = (lo+hi)//2
            if mid**degree < radicand:
                lo = mid
            else:
                hi = mid
        return min(16*j**6, hi)
    radicand = (1 << 352)*j**33
    lo, hi = 0, 1
    while hi**3 < radicand:
        hi *= 2
    while hi-lo > 1:
        mid = (lo+hi)//2
        if mid**3 < radicand:
            lo = mid
        else:
            hi = mid
    return hi
