#!/usr/bin/env python3
"""Exact checks accompanying the written problem-posing notes.

This is not a Lean proof or a universal theorem prover.  The written arguments
in PROBLEM_SEEDS_ja.md establish completeness; samples below check transcription,
integer values, boundary cases, and polynomial coefficient identities.
Uses only the Python standard library.
"""

from hashlib import sha256
import json
from math import comb, gcd, isqrt
from pathlib import Path


HERE = Path(__file__).resolve().parent


def trimmed(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b, sign=1):
    n = max(len(a), len(b))
    return trimmed([
        (a[i] if i < len(a) else 0) + sign * (b[i] if i < len(b) else 0)
        for i in range(n)
    ])


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trimmed(out)


def factor(n):
    out = []
    p = 2
    while p * p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        if e:
            out.append((p, e))
        p += 1
    if n > 1:
        out.append((n, 1))
    return out


def primes_up_to(n):
    return [p for p in range(2, n + 1)
            if all(p % d for d in range(2, isqrt(p) + 1))]


def run():
    # P01: check the two exact linear-combination identities and attainment.
    first = (3 * 10 - 2 * 25, 3 * 2 - 2 * 3)
    second = (25 * 10 - 10 * 25, 25 * 2 - 10 * 3)
    assert first == (-20, 0) and second == (0, 20)
    a, b = 1, 5
    x, y = 10 * a + 2 * b, 25 * a + 3 * b
    assert gcd(a, b) == 1 and (x, y) == (20, 40) and gcd(x, y) == 20

    # P02: coefficient equality proves the displayed polynomial identities.
    # Coefficients are stored in increasing degree.
    polynomial = [4, 0, 1, 1, 1]
    near_root = [0, 1, 2]
    four_p = [4 * c for c in polynomial]
    left_gap = add(four_p, mul(near_root, near_root), -1)
    upper_root = add(near_root, [1])
    right_gap = add(mul(upper_root, upper_root), four_p, -1)
    assert left_gap == [16, 0, 3]
    assert right_gap == mul([-3, 1], [5, 1]) == [-15, 2, 1]
    small_cases = []
    for n in (1, 2, 3):
        value = n**4 + n**3 + n**2 + 4
        root = isqrt(value)
        small_cases.append({"n": n, "value": value, "is_square": root**2 == value})
    assert [c["n"] for c in small_cases if c["is_square"]] == [3]
    # A small transcription sample, not the proof for n >= 4.
    for n in (4, 5, 10, 31, 100):
        value, near = n**4 + n**3 + n**2 + 4, 2*n*n + n
        assert near**2 < 4*value < (near+1)**2

    # P03: the first four exponent cases and the algebra for e >= 5.
    exponent_cases = [
        {"e": e, "minimal_f": (e + 2)//3, "allowed": 2*((e + 2)//3) >= e}
        for e in range(1, 5)
    ]
    assert [c["e"] for c in exponent_cases if c["allowed"]] == [1, 2, 4]
    # 3e - 2(e+2) = e-4, positive on the written domain e >= 5.
    assert add([0, 3], [4, 2], -1) == [-4, 1]
    n_examples = []
    for n in (1, 2, 4, 8, 16, 32, 36, 72, 80, 144, 625, 1296):
        fs = factor(n)
        m = 1
        for p, e in fs:
            m *= p**((e + 2)//3)
        allowed = all(e in (1, 2, 4) for _, e in fs)
        assert m**3 % n == 0
        assert (m**2 % n == 0) == allowed
        n_examples.append({"N": n, "factors": fs, "minimal_m": m, "allowed": allowed})

    # P04: exact binomials at small primes support the written all-prime proof.
    prime_samples = []
    for p in primes_up_to(31):
        value = comb(p*p, p)
        helper = comb(p*p-1, p-1)
        assert value == p*helper
        assert value % p == 0 and value % (p*p) != 0
        assert helper % p != 0
        prime_samples.append({"p": p, "binomial_mod_p_squared": value % (p*p),
                              "helper_mod_p": helper % p})

    # Missing-hypothesis counterexamples in the cards.
    assert gcd(2, 2) == 2  # L01: a coprimality hypothesis is necessary.
    assert 2 // gcd(2, 1) == 2  # L03: without Q | r^3, delta need not divide r.
    assert comb(4, 2) % 4 != 0  # L04: N alone need not divide C(N,k).
    assert comb(3, 3) % 3 != (-comb(5, 3)) % 3  # L07: m < p is substantive.
    assert (9+3)**2-36*4 == 0  # L09: a square c can give a zero residual.
    assert (9+2)**2-36*2 == 7**2  # L09: the prime bound cannot be lowered to 7.

    # L09: small finite parameters and all possible primes within sqrt(459).
    # The general modular proof is supplied in the card itself.
    offsets = [c for c in range(2, 16) if isqrt(c)**2 != c]
    possible_primes = [p for p in primes_up_to(isqrt(459)) if p >= 11]
    residual_records = []
    for c in offsets:
        for s in range(c+1):
            d = (9+s)**2-36*c
            assert -459 <= d <= 49 and d != 0
            assert all(d % (p*p) for p in possible_primes)
            residual_records.append({"c": c, "s": s, "D": d})
    assert len(residual_records) == 118

    bound_files = [HERE.parent / "README.md", HERE / "LEMMA_CARDS_ja.md",
                   HERE / "PROBLEM_SEEDS_ja.md", Path(__file__).resolve()]
    inputs = []
    for path in bound_files:
        data = path.read_bytes()
        inputs.append({"path": str(path.relative_to(HERE.parent)),
                       "bytes": len(data), "sha256": sha256(data).hexdigest()})

    return {
        "status": "PASS",
        "scope": "Exact coefficient identities, complete small boundary cases, and labelled supporting samples. Written proofs establish the universal conclusions; no Lean run.",
        "source_commit": "4d2b7c60122c2fdcefc414b179a05d2b945545a0",
        "inputs": inputs,
        "P01": {"linear_combinations": [first, second], "attainment": [a, b, x, y], "maximum": 20},
        "P02": {"left_gap_coefficients": left_gap, "right_gap_coefficients": right_gap,
                 "small_cases": small_cases, "all_positive_solutions_by_written_proof": [3],
                 "supporting_n": [4, 5, 10, 31, 100]},
        "P03": {"small_exponents": exponent_cases, "large_exponent_identity": "3e - 2(e+2) = e-4 > 0 for e >= 5", "examples": n_examples},
        "P04": {"sample_limit": 31, "prime_samples": prime_samples,
                 "all_prime_argument": "B=pH and the product defining (p-1)! H has no factor divisible by p"},
        "L09": {"possible_primes": possible_primes, "record_count": len(residual_records),
                 "records": residual_records},
        "novelty_check": "not performed",
        "new_lean_execution": False,
        "new_deepseek_api_call": False,
    }


if __name__ == "__main__":
    result = run()
    target = HERE / "verification.json"
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], "problems": 4,
                      "P02_solutions": [3], "P04_prime_samples": len(result["P04"]["prime_samples"]),
                      "L09_records": result["L09"]["record_count"]}, ensure_ascii=False))
