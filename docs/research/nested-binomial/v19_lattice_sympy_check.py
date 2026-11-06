#!/usr/bin/env python3
"""Run SymPy's actual LLL implementation on three certified research boxes.

This is a separate implementation check, not the all-family covering algorithm.
All returned transformations and 3/4-LLL inequalities are checked with integers.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import time

import sympy


def run(source, output):
    start = time.perf_counter()
    document = json.loads(gzip.decompress(source.read_bytes()))
    f = next(row for row in document["families"]
             if (row["delta"], row["M"], row["K"]) == (13, 6, 703))
    checked = []
    for sample in f["basis_samples"]:
        initial = sympy.Matrix(sample["input_basis"])
        reduced, U = initial.lll_transform(delta=sympy.Rational(3, 4))
        assert U * initial == reduced and abs(U.det()) == 1
        assert abs(reduced.det()) == sample["L"]
        u, v = [tuple(map(int, reduced.row(i))) for i in (0, 1)]
        norm1, norm2 = sum(z*z for z in u), sum(z*z for z in v)
        inner = sum(a*b for a,b in zip(u,v))
        assert 2 * abs(inner) <= norm1
        assert 4 * norm2 >= 3 * norm1
        assert norm1 * norm2 - inner * inner == sample["L"] ** 2
        checked.append({"C": 78, "K": 703, "box_exponent": sample["exponent"],
                        "determinant_bits": sample["L"].bit_length(),
                        "input_basis": sample["input_basis"],
                        "reduced_basis": [list(u),list(v)],
                        "unimodular_transform": [[int(z) for z in U.row(i)] for i in (0,1)],
                        "exact_checks": ["U*B=R", "abs(det(U))=1", "abs(det(R))=B^2",
                                         "size reduction", "Lovasz 3/4", "GSO determinant identity"]})
    result = {"status":"PASS", "implementation":"sympy.Matrix.lll_transform",
              "sympy_version":sympy.__version__, "LLL_delta":"3/4", "samples":checked,
              "certificate_sha256":hashlib.sha256(source.read_bytes()).hexdigest(),
              "checker_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "wall_seconds":round(time.perf_counter()-start,6),
              "scope":"Three actual C=78,K=703 dyadic boxes; full coverage separately uses the verified Gauss reducer"}
    output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k!="samples"},indent=2))


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--certificate",type=Path,default=Path(__file__).with_name("v19_lattice_certificate.json.gz"))
    parser.add_argument("--output",type=Path,default=Path(__file__).with_name("v19_lattice_sympy_check.json"))
    args=parser.parse_args()
    run(args.certificate,args.output)
