#!/usr/bin/env python3
"""Independent reproduction of the v8 shifted-prime-power remainder.

Uses trial factorization and a binary-search integer cube root. The
domain is reconstructed from the proof's t ranges and n<2^192; no
certificate or code from the shifted-prime-power agent is imported.
"""

from __future__ import annotations

import json
from math import gcd, isqrt
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPORT = ROOT / "v8_composite_shifted_completion_audit_verification.json"


def distinct_prime_factors(n: int) -> list[int]:
    out = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        out.append(n)
    return out


def floor_cube_root(n: int) -> int:
    lo, hi = 0, 1 << ((n.bit_length() + 2) // 3)
    while hi - lo > 1:
        middle = (lo + hi) // 2
        if middle**3 <= n:
            lo = middle
        else:
            hi = middle
    assert lo**3 <= n < (lo + 1)**3
    return lo


def main() -> None:
    assert 162 * 513**3 * (2**18 + 1) < 163 * 512**3 * 2**18
    assert 121 < 128  # (11/4)^2 < 8, so e^128 < 2^192.
    # The initial t upper bound follows from f(z)<2025/2000.
    assert 25 * 320**2 - 5975 * 320 - 8000 > 0
    assert 50 * 320 - 5975 > 0

    pairs = sorted({
        (p, t)
        for t in range(163, 225)
        for sign in (-1, 1)
        for p in distinct_prime_factors(81 * t + sign * 40)
        if p >= 7
    })
    assert len(pairs) == 204
    assert len({p for p, _ in pairs}) == 119
    assert max(p for p, _ in pairs) == 17293
    for p, t in pairs:
        assert all(p % d for d in range(2, isqrt(p) + 1))
        assert (81 * t - 40) % p == 0 or (81 * t + 40) % p == 0

    limit = 2**192
    counts = {}
    cubes = []
    for label, rows, first_a, K in [
        ("P_at_least_7", pairs, 3, 1),
        ("P_2", [(2, t) for t in range(21, 29)], 15, 8),
        ("P_5", [(5, t) for t in range(33, 45)], 8, 5),
    ]:
        count = 0
        for p, t in rows:
            a = first_a
            while p**a + 2 < limit:
                n = p**a + 2
                Q = (n // gcd(n, 3)) * ((n - 1) // gcd(n - 1, 6))
                assert n * (n - 1) % 6 == 0
                quotient = n * (n - 1) // 6
                assert quotient == (Q // 2 if p == 2 else Q)
                assert gcd(quotient, p) == 1
                d = a // 3 if p >= 7 else a // 3 + 1 if p == 2 else (a + 1) // 3
                assert p ** (3 * d - a) == K
                assert 162 < K * t < 225
                N = t * quotient
                v = floor_cube_root(N)
                if v**3 == N:
                    cubes.append({"p": p, "a": a, "t": t, "v": v})
                count += 1
                a += 3
        counts[label] = count
    assert counts == {"P_at_least_7": 2131, "P_2": 472, "P_5": 300}
    assert not cubes

    # The separate p=3 valuation branch gives a odd>=9, then a=9.
    z = 3**9
    assert 25 * z * z - 5975 * z - 8000 > 0
    assert 50 * z - 5975 > 0
    assert 3**4 > 75
    assert z + 2 == 5 * 31 * 127
    assert all(all(p % d for d in range(2, isqrt(p) + 1)) for p in (5, 31, 127))

    report = {
        "status": "PASS",
        "independent_method": "Trial factorization and binary-search exact integer cube roots; no imported certificate.",
        "large_prime_t_pairs": len(pairs),
        "large_prime_bases": len({p for p, _ in pairs}),
        "maximum_prime_base": max(p for p, _ in pairs),
        "cube_test_counts": counts,
        "total_cube_tests": sum(counts.values()),
        "perfect_cubes": cubes,
        "base_3_final_squarefree_case": z + 2,
        "scope": "Independent reproduction of the proof-derived finite remainder for all n=P^a+2 in ell=1,j=i-3.",
    }
    REPORT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
