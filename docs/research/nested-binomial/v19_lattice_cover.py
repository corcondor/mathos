#!/usr/bin/env python3
"""Exact rank-two lattice covering of the fixed-defect conics.

The covering algorithm does not use Pell equations, continued fractions,
floating-point square roots, a black-box small-root claim, or randomization.
The saved v19 Pell certificate is read only for an AFTER-THE-FACT comparison.
Every dyadic-box basis has an explicit unimodular transformation and satisfies
the size-reduction and Lovasz conditions with delta_LLL = 3/4.
"""

import argparse
from collections import Counter
import gzip
import hashlib
import json
from math import comb, gcd, isqrt
from pathlib import Path
import time


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pair_digest(points):
    h = hashlib.sha256()
    for n, r in sorted(points):
        h.update(f"{n},{r}\n".encode())
    return h.hexdigest()


def det(v, w):
    return v[0] * w[1] - v[1] * w[0]


def dot(v, w):
    return v[0] * w[0] + v[1] * w[1]


def norm(v):
    return dot(v, v)


def sub(v, w, q):
    return v[0] - q * w[0], v[1] - q * w[1]


def gauss_reduce(rows, transform):
    """Exact Gauss reduction; the returned rows also satisfy 3/4-LLL."""
    rows, transform = list(rows), list(transform)
    operations = 0
    while True:
        if norm(rows[1]) < norm(rows[0]):
            rows.reverse()
            transform.reverse()
            operations += 1
        length = norm(rows[0])
        q = (2 * dot(rows[0], rows[1]) + length) // (2 * length)
        if q == 0:
            return rows, transform, operations
        rows[1] = sub(rows[1], rows[0], q)
        transform[1] = sub(transform[1], transform[0], q)
        operations += 1


def check_basis(rows, transform, a, L):
    """Verify the output independently of the reduction's stopping rule."""
    assert abs(det(*transform)) == 1
    assert abs(det(*rows)) == L
    for (u, v), row in zip(transform, rows):
        assert row == (u, -a * u + L * v)
    n1, n2, scalar = norm(rows[0]), norm(rows[1]), dot(*rows)
    assert n1 > 0 and n2 > 0
    # |mu_21| <= 1/2.  The Lovasz inequality is equivalent to
    # ||b2||^2 >= (3/4)||b1||^2 in dimension two.
    assert 2 * abs(scalar) <= n1
    assert 4 * n2 >= 3 * n1
    # Exact GSO denominator, determinant identity, and positive second length.
    assert n1 * n2 - scalar * scalar == L * L


def ceil_div(a, b):
    assert b > 0
    return -((-a) // b)


def coefficient_interval(c, offset, low, high):
    """All integer z with low <= c*z+offset <= high."""
    if c < 0:
        c, offset, low, high = -c, -offset, -high, -low
    if c == 0:
        return (None, None) if low <= offset <= high else None
    return ceil_div(low - offset, c), (high - offset) // c


def rectangle_vectors(rows, xlo, xhi, elo, ehi):
    """Complete exact enumeration, by inverse-matrix coefficient bounds."""
    b1, b2 = rows
    D = det(b1, b2)
    values = [b1[0] * e - b1[1] * x
              for x in (xlo, xhi) for e in (elo, ehi)]
    if D < 0:
        D, values = -D, [-v for v in values]
    z2lo, z2hi = ceil_div(min(values), D), max(values) // D
    for z2 in range(z2lo, z2hi + 1):
        p = coefficient_interval(b1[0], z2 * b2[0], xlo, xhi)
        q = coefficient_interval(b1[1], z2 * b2[1], elo, ehi)
        if p is None or q is None:
            continue
        lows = [v for v in (p[0], q[0]) if v is not None]
        highs = [v for v in (p[1], q[1]) if v is not None]
        assert lows and highs  # b1 is nonzero.
        for z1 in range(max(lows), min(highs) + 1):
            x = z1 * b1[0] + z2 * b2[0]
            e = z1 * b1[1] + z2 * b2[1]
            assert xlo <= x <= xhi and elo <= e <= ehi
            yield x, e


def conic_cover(C, K, delta, keep_samples=False):
    """All n>=104, r>0, n<2^(42*delta) with C*r^2=K*n*(n-1)."""
    assert C > 0 and 9 * C < K and 927 * K < 10400 * C < 16 * 927 * C
    if isqrt(C * K) ** 2 == C * K:
        # Then x^2 - z^2 = 1 with rational z and z^2 integer; z is an
        # integer.  Hence x=1,z=0 is the only nonnegative possibility.
        return [], {"square_CK": True, "boxes": 0, "rectangle_vectors": 0,
                    "reduction_operations": 0, "basis_checks": 0}

    rows = transform = None
    previous_a = None
    B = 1 << 7
    points = []
    counts = Counter()
    trace = hashlib.sha256()
    samples = []
    xcap = (1 << (42 * delta + 1)) - 3
    for exponent in range(7, 42 * delta + 1):
        L = B * B
        a = isqrt((K * L * L) // C)
        # This proves a=floor(L*sqrt(K/C)), without numerical roots.
        assert C * a * a <= K * L * L < C * (a + 1) ** 2
        if rows is None:
            rows, transform = [(1, -a), (0, L)], [(1, 0), (0, 1)]
        else:
            # Under B -> 2B, the same U transforms the next input basis.
            correction = 4 * previous_a - a
            assert -3 <= correction <= 0
            rows = [(x, 4 * e + correction * x) for x, e in rows]
        rows, transform, operations = gauss_reduce(rows, transform)
        check_basis(rows, transform, a, L)
        counts["reduction_operations"] += operations
        counts["basis_checks"] += 1
        counts["boxes"] += 1
        xlo, xhi = max(B, 207), min(2 * B - 1, xcap)
        elo, ehi = -4 * B + 1, 2 * B - 1
        row = [exponent, a, [list(v) for v in transform],
               [xlo, xhi, elo, ehi]]
        trace.update((json.dumps(row, separators=(",", ":")) + "\n").encode())
        if keep_samples and exponent in (7, 42 * delta // 2, 42 * delta):
            samples.append({"exponent": exponent, "B": B, "L": L, "a": a,
                            "input_basis": [[1, -a], [0, L]],
                            "reduced_basis": [list(v) for v in rows],
                            "unimodular_transform": [list(v) for v in transform],
                            "rectangle": [xlo, xhi, elo, ehi]})
        seen = set()
        for x, e in rectangle_vectors(rows, xlo, xhi, elo, ehi):
            counts["rectangle_vectors"] += 1
            assert (e + a * x) % L == 0
            y = (e + a * x) // L
            if x % 2 == 1 and y > 0 and y % 2 == 0:
                counts["parity_candidates"] += 1
                if C * y * y == K * (x * x - 1):
                    n, r = (x + 1) // 2, y // 2
                    assert n >= 104 and n < (1 << (42 * delta)) and r > 0
                    assert C * r * r == K * n * (n - 1)
                    assert (n, r) not in seen
                    seen.add((n, r))
                    points.append((n, r))
        B *= 2
        previous_a = a
    assert len(set(points)) == len(points)
    info = dict(counts)
    info.update({"square_CK": False, "first_box_exponent": 7,
                 "last_box_exponent": 42 * delta,
                 "basis_trace_sha256": trace.hexdigest()})
    if samples:
        info["basis_samples"] = samples
    return sorted(points), info


def strict_log3_lower(n):
    # 3^j < n <= 3^(j+1), in exact arithmetic.
    low, high = 0, n.bit_length()
    while low + 1 < high:
        mid = (low + high) // 2
        if pow(3, mid) < n:
            low = mid
        else:
            high = mid
    assert pow(3, low) < n <= pow(3, low + 1)
    return low


def necessary_filters(n, r, M, delta):
    if gcd(n, 3) * gcd(n - 1, 6) != M:
        return "wrong_M", None
    Q = n * (n - 1) // M
    if Q // gcd(Q, r * r) != delta:
        return "wrong_delta", None
    if pow(r, 3, Q):
        return "cube_divisibility", None
    if not (3 * n < r and 3 * r < 10 * n):
        return "coarse_interval", None
    j = strict_log3_lower(n) if n >= 1024 else None
    if j is not None and not 4 * j * r < (12 * j + 3) * n:
        return "log_interval", j
    return "candidate", j


def lucas(n, k, p):
    answer = 1
    while n or k:
        a, b = n % p, k % p
        if b > a:
            return 0
        answer = answer * comb(a, b) % p
        n //= p
        k //= p
    return answer


def modular_witnesses(n, r):
    A = n * (n - 1) * (n - 2) // 6
    branches = {"small": r, "complement": A - r}
    out = []
    primes = [p for p in range(2, 98)
              if all(p % q for q in range(2, isqrt(p) + 1))]
    for p in primes:
        left = lucas(A, r, p)
        inner = lucas(n * n, 6 * n - 9, p)
        for name, k in list(branches.items()):
            right = (inner + k * k) % p
            if left != right:
                out.append({"branch": name, "prime": p,
                            "left": left, "inner": inner,
                            "k_squared": k * k % p, "right": right})
                del branches[name]
        if not branches:
            break
    assert not branches
    return out


def baseline_conic_points(family, units):
    """Comparison ONLY; never supplies a lattice bound, basis, or vector."""
    C = family["M"] * family["delta"]
    s, d = family["s"], family["d"]
    if d == 1:
        return []
    u, v = units[d]
    x, y = u, v
    cap = (1 << (42 * family["delta"] + 1)) - 1
    points = []
    while x < cap:
        assert x * x - d * y * y == 1
        if (x + 1) % 2 == 0 and (s * d * y) % (2 * C) == 0:
            n, r = (x + 1) // 2, (s * d * y) // (2 * C)
            if n >= 104:
                points.append((n, r))
        x, y = u * x + d * v * y, v * x + u * y
    return sorted(points)


def build(source, output, selected_only=False):
    started = time.perf_counter()
    old = json.loads(gzip.decompress(source.read_bytes()))
    assert old["defects_processed"] == [13, 24]
    units = {v["d"]: (v["x"], v["y"]) for v in old["units"]}
    old_families = {(f["delta"], f["M"], f["K"]): f for f in old["families"]}
    selected = {(c["delta"], c["M"], c["K"]) for c in old["candidates"]}
    expected = {(c["delta"], c["M"], c["K"], c["n"], c["r"])
                for c in old["candidates"]}
    total, final, families = Counter(), [], []
    lattice_seconds = comparison_seconds = 0.0
    for delta in range(13, 25):
        for M in (1, 2, 3, 6):
            C = M * delta
            for K in range(9 * C + 1, (10400 * C - 1) // 927 + 1):
                if gcd(K, delta) != 1:
                    continue
                key = delta, M, K
                if selected_only and key not in selected:
                    continue
                assert key in old_families
                stamp = time.perf_counter()
                points, info = conic_cover(C, K, delta, key == (13, 6, 703))
                lattice_seconds += time.perf_counter() - stamp
                # Independent input path: the lattice run is already complete.
                stamp = time.perf_counter()
                old_points = baseline_conic_points(old_families[key], units)
                assert points == old_points, key
                comparison_seconds += time.perf_counter() - stamp
                dispositions = Counter()
                for n, r in points:
                    disposition, j = necessary_filters(n, r, M, delta)
                    dispositions[disposition] += 1
                    if disposition == "candidate":
                        witnesses = modular_witnesses(n, r)
                        final.append({"delta": delta, "M": M, "K": K,
                                      "n": n, "r": r, "log_lower_j": j,
                                      "witnesses": witnesses})
                total["coefficient_families"] += 1
                total["square_CK_families"] += int(info["square_CK"])
                total["conic_points_n_ge_104"] += len(points)
                for label in ("boxes", "rectangle_vectors", "parity_candidates",
                              "reduction_operations", "basis_checks"):
                    total[label] += info.get(label, 0)
                for label, count in dispositions.items():
                    total["filter_" + label] += count
                families.append({"delta": delta, "M": M, "K": K,
                                 "conic_count": len(points),
                                 "conic_points_sha256": pair_digest(points),
                                 "dispositions": dict(dispositions), **info})
    found = {(c["delta"], c["M"], c["K"], c["n"], c["r"]) for c in final}
    assert found == expected
    assert len(families) == (34 if selected_only else 3571)
    assert len(final) == 93
    if not selected_only:
        assert total["conic_points_n_ge_104"] == old["counts"]["n_ge_104"]
    data = {
        "status": "PASS_EXACT_LATTICE_COVER",
        "algorithm": "Incremental exact Gauss reduction, certified as rank-two 3/4-LLL; complete rectangle enumeration",
        "scope": "Selected 34 candidate-bearing families" if selected_only else "All 3571 fixed-defect coefficient families for 13<=delta<=24",
        "coefficient_conditions": "M in {1,2,3,6}, C=M*delta, 9C<K<10400C/927, gcd(K,delta)=1",
        "height": "104<=n<2^(42*delta); inherited v16 theorem, not a chosen scan bound",
        "transform": "x=2n-1, y=2r; C*y^2-K*x^2=-K",
        "dyadic_cover": "B=2^b, 7<=b<=42*delta, max(B,207)<=x<=min(2B-1,2^(42delta+1)-3)",
        "rectangle": "-4B<e<2B, e=B^2*y-floor(B^2*sqrt(K/C))*x",
        "baseline_certificate": {"file": source.name, "sha256": digest(source)},
        "producer_sha256": digest(Path(__file__)),
        "counts": dict(total),
        "same_contract_comparison": {"all_conic_point_sets_equal": True,
                                     "all_93_final_pairs_equal": True,
                                     "old_Pell_used_for_lattice_generation": False},
        "modular_branches_excluded": sum(len(c["witnesses"]) for c in final),
        "max_witness_prime": max(w["prime"] for c in final for w in c["witnesses"]),
        "families": families, "candidates": final,
        "not_claimed": ["new numerical delta lower bound beyond existing v19",
                        "unbounded delta coverage", "original four-variable classification",
                        "Coppersmith execution", "elliptic-curve discrete logarithm computation",
                        "Lean formalization", "DeepSeek API execution", "external peer review"]}
    raw = (json.dumps(data, sort_keys=True, ensure_ascii=False, separators=(",", ":")) + "\n").encode()
    with output.open("wb") as f:
        with gzip.GzipFile(filename="", fileobj=f, mode="wb", mtime=0) as z:
            z.write(raw)
    summary = {k: v for k, v in data.items() if k not in ("families", "candidates")}
    summary["certificate_file"] = output.name
    summary["certificate_sha256"] = digest(output)
    summary["uncompressed_sha256"] = hashlib.sha256(raw).hexdigest()
    summary["wall_seconds"] = round(time.perf_counter() - started, 6)
    summary["lattice_cover_seconds"] = round(lattice_seconds, 6)
    summary["stored_Pell_comparison_seconds"] = round(comparison_seconds, 6)
    summary["timing_limits"] = "Single sequential run; stored-unit comparison excludes Pell unit generation and is not a performance superiority test."
    output.with_suffix("").with_suffix(".summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline-certificate", type=Path,
                        default=Path(__file__).with_name("v19_defect_13_24_certificate.json.gz"))
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_name("v19_lattice_certificate.json.gz"))
    parser.add_argument("--candidate-families-only", action="store_true")
    args = parser.parse_args()
    build(args.baseline_certificate, args.output, args.candidate_families_only)
