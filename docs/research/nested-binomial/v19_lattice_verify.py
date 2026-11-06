#!/usr/bin/env python3
"""Independent integer-lattice audit; imports neither producer nor Pell code.

This implementation reduces the two basis rows with a different tie convention,
orients the determinant positively, enumerates the OTHER lattice coefficient,
and uses a slightly larger closed rectangle. It independently checks the complete
conic-point digest for every family and all final binomial residue witnesses.
"""

import argparse
from collections import Counter
import gzip
import hashlib
import json
from math import gcd, isqrt
from pathlib import Path
import time


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def square_norm(v):
    return sum(t * t for t in v)


def product(u, v):
    return sum(x * y for x, y in zip(u, v))


def nearest_with_zero_ties(a, b):
    q, rem = divmod(abs(a), b)
    if 2 * rem > b:
        q += 1
    return q if a >= 0 else -q


def reduce_and_verify(vectors, matrix, a, q):
    u, v = vectors
    e, f = matrix
    while True:
        if square_norm(u) > square_norm(v):
            u, v, e, f = v, u, f, e
        mu = nearest_with_zero_ties(product(u, v), square_norm(u))
        if mu == 0:
            break
        v = tuple(y - mu * x for x, y in zip(u, v))
        f = tuple(y - mu * x for x, y in zip(e, f))
    determinant = u[0] * v[1] - u[1] * v[0]
    if determinant < 0:
        u, e = tuple(-z for z in u), tuple(-z for z in e)
        determinant = -determinant
    assert determinant == q
    assert e[0] * f[1] - e[1] * f[0] == 1
    assert u == (e[0], q * e[1] - a * e[0])
    assert v == (f[0], q * f[1] - a * f[0])
    norm1, norm2, cross = square_norm(u), square_norm(v), product(u, v)
    assert 2 * abs(cross) <= norm1
    assert 3 * norm1 <= 4 * norm2
    assert norm1 * norm2 - cross * cross == q * q
    return (u, v), (e, f)


def linear_range(slope, intercept, lo, hi):
    if slope == 0:
        return (None, None) if lo <= intercept <= hi else None
    if slope > 0:
        return -((intercept - lo) // slope), (hi - intercept) // slope
    return -((intercept - hi) // slope), (lo - intercept) // slope


def enumerate_other_coefficient(u, v, determinant, left, right, bottom, top):
    corners = [x * v[1] - y * v[0]
               for x in (left, right) for y in (bottom, top)]
    first, last = -((-min(corners)) // determinant), max(corners) // determinant
    for i in range(first, last + 1):
        tx = linear_range(v[0], i * u[0], left, right)
        ty = linear_range(v[1], i * u[1], bottom, top)
        if tx is None or ty is None:
            continue
        lower = max(z for z in (tx[0], ty[0]) if z is not None)
        upper = min(z for z in (tx[1], ty[1]) if z is not None)
        for j in range(lower, upper + 1):
            x, y = i * u[0] + j * v[0], i * u[1] + j * v[1]
            assert left <= x <= right and bottom <= y <= top
            yield x, y


def recover_all(delta, M, K):
    C = M * delta
    if isqrt(C * K) ** 2 == C * K:
        return [], 0, 0
    basis = transform = None
    a_old = None
    points = set()
    vector_count = box_count = 0
    for bit in range(7, 42 * delta + 1):
        B = 2 ** bit
        modulus = 2 ** (2 * bit)
        a = isqrt((K * modulus * modulus) // C)
        assert C * a * a <= K * modulus * modulus
        assert K * modulus * modulus < C * (a + 1) * (a + 1)
        if basis is None:
            # Deliberately opposite initial row order from the producer.
            basis, transform = ((0, modulus), (1, -a)), ((0, 1), (1, 0))
        else:
            basis = tuple((x, 4 * y + (4 * a_old - a) * x) for x, y in basis)
        basis, transform = reduce_and_verify(basis, transform, a, modulus)
        box_count += 1
        # Enlarge the producer's strict e rectangle by including both boundaries.
        left = max(207, B)
        right = min(2 * B - 1, (2 ** (42 * delta + 1)) - 3)
        for x, err in enumerate_other_coefficient(*basis, modulus,
                                                  left, right, -4 * B, 2 * B):
            vector_count += 1
            quotient, remainder = divmod(err + a * x, modulus)
            assert remainder == 0
            if quotient <= 0 or x % 2 == 0 or quotient % 2:
                continue
            n, r = (x + 1) // 2, quotient // 2
            if C * r * r == K * n * (n - 1):
                assert 104 <= n < 2 ** (42 * delta)
                assert (n, r) not in points
                points.add((n, r))
        a_old = a
    return sorted(points), box_count, vector_count


def points_hash(points):
    h = hashlib.sha256()
    for point in sorted(points):
        h.update((str(point[0]) + "," + str(point[1]) + "\n").encode("ascii"))
    return h.hexdigest()


def classify(n, r, M, delta):
    if gcd(n, 3) * gcd(n - 1, 6) != M:
        return "wrong_M", None
    Q = n * (n - 1) // M
    if Q // gcd(Q, r ** 2) != delta:
        return "wrong_delta", None
    if r ** 3 % Q:
        return "cube_divisibility", None
    if r <= 3 * n or 3 * r >= 10 * n:
        return "coarse_interval", None
    j = None
    if n >= 1024:
        j, z = 0, 1
        while 3 * z < n:
            z *= 3
            j += 1
        assert z < n <= 3 * z
        if 4 * j * (r - 3 * n) >= 3 * n:
            return "log_interval", j
    return "candidate", j


def digit_binomial(a, b, p):
    if b > a:
        return 0
    factorials = [1]
    for k in range(1, p):
        factorials.append(factorials[-1] * k % p)
    return (factorials[a] * pow(factorials[b] * factorials[a-b] % p, -1, p)) % p


def binomial_mod(n, k, p):
    out = 1
    while n or k:
        out = out * digit_binomial(n % p, k % p, p) % p
        n, k = n // p, k // p
    return out


def check_witnesses(row):
    n, r = row["n"], row["r"]
    A = n * (n - 1) * (n - 2) // 6
    assert {w["branch"] for w in row["witnesses"]} == {"small", "complement"}
    for w in row["witnesses"]:
        p = w["prime"]
        assert p >= 2 and all(p % d for d in range(2, isqrt(p) + 1))
        k = r if w["branch"] == "small" else A - r
        left = binomial_mod(A, r, p)
        inner = binomial_mod(n * n, 6 * n - 9, p)
        right = (inner + k * k) % p
        assert left == w["left"] and inner == w["inner"]
        assert k * k % p == w["k_squared"] and right == w["right"]
        assert left != right


def verify(path, output):
    start = time.perf_counter()
    doc = json.loads(gzip.decompress(path.read_bytes()))
    assert doc["scope"] == "All 3571 fixed-defect coefficient families for 13<=delta<=24"
    supplied = {(f["delta"], f["M"], f["K"]): f for f in doc["families"]}
    assert len(supplied) == len(doc["families"]) == 3571
    candidates = {(c["delta"], c["M"], c["K"], c["n"], c["r"]): c
                  for c in doc["candidates"]}
    assert len(candidates) == len(doc["candidates"]) == 93
    consumed, families_seen = set(), set()
    totals = Counter()
    for delta in range(13, 25):
        for M in (1, 2, 3, 6):
            C = M * delta
            # Wider loop and separate exact rational inequality, rather than
            # the producer's precomputed floor upper endpoint.
            for K in range(9 * C + 1, 12 * C):
                if gcd(K, delta) != 1 or 927 * K >= 10400 * C:
                    continue
                key = delta, M, K
                families_seen.add(key)
                stored = supplied[key]
                pts, boxes, vectors = recover_all(*key)
                assert len(pts) == stored["conic_count"]
                assert points_hash(pts) == stored["conic_points_sha256"]
                assert boxes == stored["boxes"] == stored["basis_checks"]
                disposition = Counter()
                for n, r in pts:
                    kind, j = classify(n, r, M, delta)
                    disposition[kind] += 1
                    if kind == "candidate":
                        ck = delta, M, K, n, r
                        row = candidates[ck]
                        assert row["log_lower_j"] == j
                        check_witnesses(row)
                        consumed.add(ck)
                assert dict(disposition) == stored["dispositions"]
                totals["coefficient_families"] += 1
                totals["conic_points_n_ge_104"] += len(pts)
                totals["boxes_and_exact_LLL_checks"] += boxes
                totals["vectors_in_enlarged_rectangles"] += vectors
    assert families_seen == set(supplied)
    assert consumed == set(candidates)
    assert totals["conic_points_n_ge_104"] == doc["counts"]["conic_points_n_ge_104"]
    assert totals["boxes_and_exact_LLL_checks"] == doc["counts"]["boxes"]
    result = {
        "status": "PASS",
        "certificate": {"file": path.name, "sha256": sha(path)},
        "verifier_sha256": sha(Path(__file__)),
        "scope": "All 3571 families, every dyadic box, complete positive integral conic point sets and 93 final candidates",
        "counts": dict(totals),
        "final_candidates": len(consumed),
        "original_binomial_branches_excluded": sum(len(v["witnesses"]) for v in candidates.values()),
        "no_producer_or_Pell_import": True,
        "no_Pell_units_or_convergents_read": True,
        "independence": "Opposite basis order, ties toward zero, positive determinant, other coefficient enumeration, enlarged closed error rectangle, factorial-inverse Lucas digits",
        "completeness_input": "Written v16 height and coefficient interval; new lattice-rectangle proof in companion note",
        "wall_seconds": round(time.perf_counter() - start, 6),
        "limits": "Exact arithmetic certificate, not Lean; confirms existing finite delta exclusion, not unbounded delta or the full equation"
    }
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path,
                        default=Path(__file__).with_name("v19_lattice_certificate.json.gz"))
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_name("v19_lattice_independent_audit.json"))
    options = parser.parse_args()
    verify(options.certificate, options.output)
