#!/usr/bin/env python3
"""Independent verifier for v4_upper_j1_pell certificates.

Unlike the generator, use (2k-1)^2-4k(k-1)=1, a different Pell family,
a coarser separately derived height, gcd-based smoothness, trial-division
prime generation, and factorial-table Lucas residues.
"""

import argparse
import hashlib
import json
import math
import pathlib
import time


def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, math.isqrt(n) + 1))


def supported(n, primorial):
    assert n >= 1
    while n > 1:
        divisor = math.gcd(n, primorial)
        if divisor == 1:
            return False
        n //= divisor
    return True


def products_recursive(primes, index=0, product=1):
    if index == len(primes):
        if product != 1:
            yield product
        return
    yield from products_recursive(primes, index + 1, product)
    yield from products_recursive(primes, index + 1, product * primes[index])


def pell_base(d, x_limit):
    # Complete quotients [a0; a1, ...], using a 2-by-2 convergent matrix.
    a0 = math.isqrt(d)
    assert a0 * a0 < d
    shift, scale = 0, 1
    h_left, h_right = 1, 0
    k_left, k_right = 0, 1
    while True:
        quotient = (a0 + shift) // scale
        h_left, h_right = quotient * h_left + h_right, h_left
        k_left, k_right = quotient * k_left + k_right, k_left
        if h_left > x_limit:
            return None
        if h_left * h_left == d * k_left * k_left + 1:
            return h_left, k_left
        shift = quotient * scale - shift
        assert (d - shift * shift) % scale == 0
        scale = (d - shift * shift) // scale


def alternate_ks(primes, k_limit):
    primorial = math.prod(primes)
    found = set()
    x_limit = 2 * k_limit - 1
    d_count = 0
    for d in products_recursive(primes):
        d_count += 1
        base = pell_base(d, x_limit)
        if base is None:
            continue
        a, b = base
        x, y = a, b
        while x <= x_limit:
            if x % 2:
                k = (x + 1) // 2
                if all(supported(z, primorial) for z in (k - 1, k, k + 1)):
                    assert k not in found
                    found.add(k)
            x, y = a * x + d * b * y, a * y + b * x
    assert d_count == 2 ** len(primes) - 1
    return found, d_count


def factorial_tables(p):
    factorial = [1] * p
    for n in range(1, p):
        factorial[n] = factorial[n - 1] * n % p
    inverse = [1] * p
    for n in range(p):
        inverse[n] = pow(factorial[n], p - 2, p)
    return factorial, inverse


def residue(n, r, p, tables):
    if r > n or r < 0:
        return 0
    factorial, inverse = tables
    product = 1
    while r:
        top, bottom = n % p, r % p
        if bottom > top:
            return 0
        product *= factorial[top] * inverse[bottom] * inverse[top - bottom]
        product %= p
        n, r = n // p, r // p
    return product


def verify(path, output):
    started = time.monotonic()
    raw = pathlib.Path(path).read_bytes()
    data = json.loads(raw)
    assert data["scope"]["j"] == 1
    lo, hi = data["scope"]["ell_min"], data["scope"]["ell_max"]
    assert 21 <= lo <= hi
    assert not data["survivors"]
    certificates = {}
    for item in data["witnesses"]:
        key = item["ell"], int(item["k"]), item["t"]
        assert key not in certificates
        assert lo <= key[0] <= hi
        assert is_prime(item["p"])
        certificates[key] = item
    assert len(certificates) == data["total_equation_candidates"]
    assert len(certificates) == data["witness_count"]
    tables = {p: factorial_tables(p) for p in {x["p"] for x in certificates.values()}}
    groups = {}
    for ell in range(lo, hi + 1):
        primes = tuple(p for p in range(2, 2 * ell + 1) if is_prime(p))
        groups.setdefault(primes, []).append(ell)
    counts = {ell: 0 for ell in range(lo, hi + 1)}
    group_reports = []
    for primes, ells in groups.items():
        # Prior height theorem: k < ell*e^ell < ell*3^ell.
        k_limit = max(ell * 3 ** ell - 1 for ell in ells)
        ks, d_count = alternate_ks(primes, k_limit)
        group_reports.append({"ells": ells, "d_count": d_count,
                              "coarse_k_limit": str(k_limit), "ks": len(ks)})
        print(json.dumps(group_reports[-1]), flush=True)
        for ell in ells:
            numerator = math.factorial(ell * ell)
            denominator = math.factorial(ell) ** (2 * ell)
            a_limit = (numerator + denominator - 1) // denominator - 1
            t_first = max(ell + 2, (ell + math.isqrt(5 * ell * ell)) // 2 + 1)
            for k in sorted(ks):
                if k < ell + 2:
                    continue
                B = math.comb(k, ell)
                if B >= a_limit:
                    continue
                t_last = min(B, (2 if k >= 2 * ell else 10) * ell - 1,
                             a_limit - B)
                for t in range(t_first, t_last + 1):
                    counts[ell] += 1
                    witness = certificates.pop((ell, k, t))
                    p = witness["p"]
                    A = B + t
                    left = residue(A, t, p, tables[p])
                    right = (pow(A, 2, p) + residue(k * k, ell * ell, p, tables[p])) % p
                    assert left == witness["left"]
                    assert right == witness["right"]
                    assert left != right
    assert not certificates
    assert sum(counts.values()) == data["total_equation_candidates"]
    assert {str(k): v for k, v in counts.items()} == data["candidate_counts"]
    report = {"status": "pass", "ell_min": lo, "ell_max": hi,
              "j": 1, "branch": "upper", "verified_candidates": sum(counts.values()),
              "candidate_counts": counts, "groups": group_reports,
              "coverage": "independent adjacent-pair Pell enumeration with coarser proved height",
              "residues": "factorial-table Lucas implementation",
              "certificate_sha256": hashlib.sha256(raw).hexdigest(),
              "formal_proof_assistant_executed": False,
              "seconds": time.monotonic() - started}
    pathlib.Path(output).write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", default="v4_upper_j1_pell_certificates.json")
    parser.add_argument("--output", default="v4_upper_j1_pell_verification.json")
    args = parser.parse_args()
    verify(args.path, args.output)
