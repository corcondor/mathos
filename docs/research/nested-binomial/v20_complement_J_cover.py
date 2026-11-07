#!/usr/bin/env python3
"""Complete complementary-branch canonical J<=32 divisor certificate.

The w<=383 cap is proved in the companion note from the v20 analytic gap.
There is no scan cutoff on n and no bound on the exact defect delta.
All arithmetic, prime factors, divisors and square obstructions are exact.
"""

import argparse
from collections import Counter
from fractions import Fraction
import gzip
import hashlib
from itertools import product
import json
from math import factorial, gcd, isqrt
from pathlib import Path
import time


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def factor(a):
    out = []
    p = 2
    while p*p <= a:
        if a % p == 0:
            e = 0
            while a % p == 0:
                a //= p
                e += 1
            out.append([p, e])
        p = 3 if p == 2 else p+2
    if a > 1:
        out.append([a, 1])
    return out


def cube_divisors(factors):
    lists = [[p**e for e in range(3*v+1)] for p, v in factors]
    out = []
    for values in product(*lists):
        d = 1
        for v in values:
            d *= v
        out.append(d)
    assert len(set(out)) == len(out)
    return sorted(out)


def build(output, gap_note, research_dir):
    start = time.perf_counter()
    # e^(7/10)>sum_{j=0}^4 (7/10)^j/j!>2, proving log(2)<7/10.
    exp_lower = sum((Fraction(7, 10)**i/Fraction(factorial(i)))
                    for i in range(5))
    assert exp_lower > 2
    assert 5001 * 32 < 2 * 85000
    assert 3 * 3520**3 < 2**37
    assert Fraction(7,16)*32*37*Fraction(7,10) < 384
    assert Fraction(189*32, 16*9*384) == Fraction(7,64)

    families, second_points, square_tests, survivors = [], [], [], []
    total = Counter()
    by_J = {}
    for J in range(1, 33):
        count = Counter()
        if J % 4 == 2:
            by_J[J] = {"excluded_by_uniform_two_adic_condition": True}
            continue
        for w in range(65, 384):
            if gcd(J, w) != 1:
                continue
            c0, c1 = 9*w+2*J, 24*w+3*J
            fac = factor(c0)
            divs = cube_divisors(fac)
            fc = Counter()
            normalized_points = []
            for e in divs:
                for g in (1, 3):
                    fc["raw_divisor_records"] += 1
                    n = g*e
                    if n < 104 or gcd(n, 3) != g:
                        continue
                    fc["normalized_n"] += 1
                    normalized_points.append(n)
                    d = gcd(n-1, 6)
                    q1 = (n-1)//d
                    if c1**3 % q1:
                        continue
                    fc["second_divisor"] += 1
                    record = {"J":J, "w":w, "n":n, "g":g, "d":d}
                    second_points.append(record)
                    N = n*n+2
                    if N % w:
                        continue
                    fc["w_divides_N"] += 1
                    G = N//w
                    S = 9*n*n+6*n+10+J*G
                    root = isqrt(S)
                    row = {**record, "G":G, "r_minus_one_squared":S,
                           "floor_square_root":root}
                    square_tests.append(row)
                    assert root*root <= S < (root+1)*(root+1)
                    if root*root == S:
                        fc["square"] += 1
                        survivors.append({**row, "r":root+1})
            fc["coefficient_families"] += 1
            count.update(fc)
            assert len(set(normalized_points)) == len(normalized_points)
            point_hash = hashlib.sha256()
            for n in sorted(normalized_points):
                point_hash.update(f"{n}\n".encode())
            families.append({"J":J, "w":w, "c0":c0, "c1":c1,
                             "c0_factorization":fac,
                             "cube_divisor_count":len(divs),
                             "normalized_n_sha256":point_hash.hexdigest(),
                             "counts":dict(fc)})
        total.update(count)
        by_J[J] = dict(count)
    assert not survivors
    assert dict(total) == {"raw_divisor_records":608102,
                           "normalized_n":429917,
                           "second_divisor":862,
                           "w_divides_N":5,
                           "coefficient_families":5323}
    assert len(second_points) == 862 and len(square_tests) == 5
    for row in square_tests:
        assert row["floor_square_root"]**2 < row["r_minus_one_squared"]
    certificate = {
        "status":"PASS_COMPLETE_COMPLEMENT_J_EXCLUSION",
        "scope":"Original squared-index binomial equation, ell=1,j=i-3,k=C(n,3)-r; all exact defects, all n>=104",
        "proved_conclusion":"Canonical complementary numerator J>=33",
        "finite_domain":{"J":[1,32], "w":[65,383],
                         "coprime":True, "excluded_J_residue":"J=2 mod4"},
        "theory_inputs":["v18 canonical w>=65 and complementary cube divisibilities",
                         "v17/v19 strict square-root gap gives T1>17*n^(3/2)",
                         "v19 canonical J not congruent to 2 modulo 4",
                         "v20 analytic gap gives w<(7/16)*J*log(n) for n>=1024"],
        "written_input_sha256":{
            gap_note.name:sha(gap_note),
            "v18_neighbor_cofactor_height.md":sha(research_dir/"v18_neighbor_cofactor_height.md"),
            "v19_canonical_J_elimination.md":sha(research_dir/"v19_canonical_J_elimination.md")},
        "cap_constants":{"exp_7_over_10_positive_partial_sum":[exp_lower.numerator,exp_lower.denominator],
                         "n_at_w384_J32_upper":3*3520**3,
                         "power_of_two_exponent":37,
                         "w384_gap_lower":[107,5],
                         "derivative_lower":[57,64]},
        "producer_sha256":sha(Path(__file__)),
        "counts":dict(total), "per_J":by_J, "families":families,
        "second_divisor_points":second_points,
        "complete_square_obstructions":square_tests,
        "survivors":survivors,
        "claims_not_made":["unbounded J excluded", "whole four-variable equation solved",
                           "new lower bound on delta", "Lucas witnesses used in this certificate",
                           "Lean execution", "DeepSeek API execution", "external peer review"]
    }
    raw = (json.dumps(certificate,sort_keys=True,ensure_ascii=False,separators=(",",":"))+"\n").encode()
    with output.open("wb") as f:
        with gzip.GzipFile(filename="",mode="wb",fileobj=f,mtime=0) as z:
            z.write(raw)
    summary = {k:v for k,v in certificate.items()
               if k not in ("families","second_divisor_points")}
    summary.update({"certificate_file":output.name,"certificate_sha256":sha(output),
                    "uncompressed_sha256":hashlib.sha256(raw).hexdigest(),
                    "wall_seconds":round(time.perf_counter()-start,6)})
    output.with_suffix("").with_suffix(".summary.json").write_text(json.dumps(summary,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({k:v for k,v in summary.items() if k!="per_J"},ensure_ascii=False,indent=2))


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path,default=Path(__file__).with_name("v20_complement_J_certificate.json.gz"))
    parser.add_argument("--gap-note",type=Path,default=Path(__file__).with_name("v20_logarithmic_gap.md"))
    parser.add_argument("--research-dir",type=Path,default=Path(__file__).parent)
    args=parser.parse_args()
    build(args.output,args.gap_note,args.research_dir)
