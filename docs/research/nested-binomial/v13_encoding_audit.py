#!/usr/bin/env python3
"""Audit saved prime-support Thue results without invoking a CAS.

Coverage is generated independently as a 3^s by 3^s table, then filtered
by gcd(A, B) = 1.  This checks recorded solutions and their encodings;
it does not independently establish completeness of PARI's Thue solver.

Default: audit the saved S={2,3,5,7} report beside this script.
Use --all for every thue_support_*_audit.json in --data-dir, or supply
explicit paths with --inputs.  All dependencies are in the standard library.
"""
from __future__ import annotations

import argparse
import ast
from datetime import datetime, timezone
import hashlib
import itertools
import json
import math
from pathlib import Path
import sys


class AuditFailure(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AuditFailure(message)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def is_prime(n: int) -> bool:
    if type(n) is not int or n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    return all(n % divisor for divisor in range(3, math.isqrt(n) + 1, 2))


def independent_core_pairs(primes: list[int]) -> tuple[list[int], list[tuple[int, int]]]:
    require(isinstance(primes, list), "support_primes must be a list")
    require(all(is_prime(p) for p in primes), "support must consist of primes")
    require(len(set(primes)) == len(primes), "support primes must be distinct")
    require({2, 3}.issubset(primes), "the stated reduction requires 2 and 3 in S")
    cores = sorted(
        math.prod(p**exponent for p, exponent in zip(primes, exponents))
        for exponents in itertools.product(range(3), repeat=len(primes))
    )
    require(len(cores) == len(set(cores)) == 3 ** len(primes), "cube-free core count")
    pairs = sorted((a, b) for a in cores for b in cores if math.gcd(a, b) == 1)
    require(len(pairs) == 5 ** len(primes), "coprime ordered-pair count")
    require([(a, b) for a, b in pairs if a == b] == [(1, 1)], "swap fixed point")
    unordered = {tuple(sorted((a, b))) for a, b in pairs if a != b}
    require(len(unordered) == (5 ** len(primes) - 1) // 2, "unordered-pair count")
    return cores, pairs


def integer_pairs(value: object, label: str) -> list[tuple[int, int]]:
    require(isinstance(value, list), f"{label}: expected a list")
    result = []
    for row in value:
        require(isinstance(row, (list, tuple)) and len(row) == 2,
                f"{label}: expected an integer pair")
        require(all(type(entry) is int for entry in row), f"{label}: noninteger entry")
        result.append((row[0], row[1]))
    require(len(result) == len(set(result)), f"{label}: duplicate solution")
    return sorted(result)


def audit_report(report_path: Path, generator_source: Path) -> dict:
    report_bytes = report_path.read_bytes()
    report = json.loads(report_bytes)
    require(report.get("status") == "PASS", f"{report_path.name}: input status")
    primes = report["support_primes"]
    cores, expected_pairs = independent_core_pairs(primes)
    records = report["records"]
    require([(row["A"], row["B"]) for row in records] == expected_pairs,
            "saved coefficient pairs do not equal independently generated coverage")
    require(report["pair_count"] == len(expected_pairs), "reported pair count")
    require(report["pari_calls"] == 2 * len(expected_pairs), "reported PARI call count")
    require(report["thueinit_flag"] == 1, "reported unconditional thueinit flag")

    source_hash = sha256(generator_source.read_bytes())
    require(report["source_sha256"] == source_hash, "generator-source SHA-256")
    input_path = report_path.with_suffix(".gp")
    stdout_path = report_path.with_suffix(".stdout")
    input_bytes = input_path.read_bytes()
    stdout_bytes = stdout_path.read_bytes()
    require(report["gp_input_sha256"] == sha256(input_bytes), "GP-input SHA-256")
    require(report["gp_stdout_sha256"] == sha256(stdout_bytes), "GP-stdout SHA-256")

    # Check actual GP commands, including flag=1, against independent coverage.
    expected_program = ["print(version());"]
    for a, b in expected_pairs:
        expected_program.append(
            f"print([{a},{b},thue(thueinit({a}*x^3-{b},1),1),"
            f"thue(thueinit(x^3-{a*a*b},1),{a*a})]);"
        )
    expected_program.append("quit;")
    require(input_bytes.decode("utf-8").splitlines() == expected_program,
            "GP commands, coefficients, or unconditional flags differ")

    output_lines = stdout_bytes.decode("utf-8").splitlines()
    require(len(output_lines) == len(expected_pairs) + 1, "GP stdout record count")
    raw_output = [ast.literal_eval(line) for line in output_lines]
    require(raw_output[0] == report["pari_version"], "recorded GP version")

    positive_ns: set[int] = set()
    unordered_ns: dict[tuple[int, int], set[int]] = {}
    direct_count = transformed_count = rejected_transformed_count = 0
    for row, raw in zip(records, raw_output[1:]):
        a, b = row["A"], row["B"]
        require(isinstance(raw, list) and len(raw) == 4, "GP output row structure")
        require(raw[:2] == [a, b], "GP output coefficient order")
        direct = integer_pairs(raw[2], f"direct ({a},{b})")
        transformed = integer_pairs(raw[3], f"transformed ({a},{b})")
        require(direct == integer_pairs(row["all_integer_solutions"], "saved direct"),
                "JSON direct solutions differ from stdout")
        require(transformed == integer_pairs(row["transformed_all_integer_solutions"],
                                             "saved transformed"),
                "JSON transformed solutions differ from stdout")
        require(all(a*x**3 - b*y**3 == 1 for x, y in direct),
                "a listed direct signed pair fails its exact equation")
        require(all(u**3 - a*a*b*y**3 == a*a for u, y in transformed),
                "a listed transformed signed pair fails its exact equation")
        recovered = sorted((u // a, y) for u, y in transformed if u % a == 0)
        require(direct == recovered, "nonmonic/monic encoding correspondence")
        positive = [(x, y) for x, y in direct if x > 0 and y > 0]
        require(positive == integer_pairs(row["positive_solutions"], "saved positive"),
                "positive-solution filtering")
        ns = sorted(a*x**3 for x, y in positive)
        require(ns == row["positive_n"], "positive first-index reconstruction")
        if a == b == 1:
            require(not positive, "(1,1) must have no positive cubic solution")
        positive_ns.update(ns)
        unordered_ns.setdefault(tuple(sorted((a, b))), set()).update(ns)
        direct_count += len(direct)
        transformed_count += len(transformed)
        rejected_transformed_count += sum(u % a != 0 for u, y in transformed)

    require(sorted(positive_ns) == report["positive_n"], "combined first-index list")
    require(all(len(ns) <= 1 for ns in unordered_ns.values()),
            "recorded results contradict Bennett's at-most-one bound")
    cardinal_bound = (5 ** len(primes) - 1) // 2
    require(len(positive_ns) <= cardinal_bound, "observed first-index cardinal bound")
    return {
        "status": "PASS",
        "input_file": report_path.name,
        "support_primes": primes,
        "coverage_method": "all 3^s cube-free cores squared, then gcd(A,B)=1",
        "core_count": len(cores),
        "unfiltered_ordered_pair_count": len(cores)**2,
        "verified_ordered_pair_count": len(expected_pairs),
        "unordered_nontrivial_pair_count": cardinal_bound,
        "listed_direct_signed_solution_count": direct_count,
        "listed_transformed_signed_solution_count": transformed_count,
        "transformed_solutions_rejected_by_A_divisibility": rejected_transformed_count,
        "positive_n": sorted(positive_ns),
        "positive_n_count": len(positive_ns),
        "pari_version_recorded_in_source_output": raw_output[0],
        "input_report_sha256": sha256(report_bytes),
        "generator_source_sha256": source_hash,
        "gp_input_sha256": sha256(input_bytes),
        "gp_stdout_sha256": sha256(stdout_bytes),
    }


BENNETT_REVIEW = {
    "status": "mathematical statement audit; not a machine-checked proof",
    "primary_reference": "https://personal.math.ubc.ca/~bennett/B-Crelle2.pdf",
    "reference": "M. A. Bennett, J. reine angew. Math. 535 (2001), 1-49, Theorem 1.1",
    "assumptions": [
        "S is a finite set of primes containing 2 and 3",
        "n>=3 and H,T,r are positive integers",
        "H divides n-2 and 6 H r^3 = T n(n-1)(n-2)",
        "v_p(T) is divisible by 3 for every prime p outside S",
    ],
    "reduction": (
        "If p outside S divides n or n-1, it divides neither 6H nor the other "
        "two consecutive factors. Valuations imply 3 divides v_p(n) or "
        "v_p(n-1), respectively. Thus their unique positive cube-free cores "
        "A,B are supported on S and coprime."
    ),
    "cardinality_reason": (
        "Each prime has five placements: absent, exponent 1 or 2 in A, "
        "or exponent 1 or 2 in B. Swapping A,B has only the fixed pair (1,1), "
        "which has no solution in positive cubic bases. Bennett's theorem "
        "applied to |A x^3-B y^3|=1 gives at most one positive base pair "
        "per remaining unordered core pair; n is the larger of the two terms."
    ),
    "distinct_first_index_bound": "(5^|S|-1)/2, uniformly in H and all allowed exponents of T",
    "full_auxiliary_tuple_finiteness": (
        "Also impose 3n<r<10n/3. For each n there are floor((n-1)/3) "
        "integer choices of r, finitely many positive H dividing n-2, and "
        "at most one T for each n,H,r. If gcd(H,T)=1, n,r uniquely determine "
        "H=A0/g and T=r^3/g, where A0=binomial(n,3), g=gcd(A0,r^3). "
        "Without a bound on r, the first-index bound alone does not give "
        "finiteness of all auxiliary tuples."
    ),
    "scope_limit": "This does not classify the original four-variable equation.",
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", type=Path, default=Path(__file__).resolve().parent)
    select = parser.add_mutually_exclusive_group()
    select.add_argument("--inputs", type=Path, nargs="+")
    select.add_argument("--all", action="store_true")
    parser.add_argument("--source", type=Path, help="executed Thue audit generator source")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    source = args.source or args.data_dir / "thue_support_audit.py"
    output = args.output or args.data_dir / "v13_encoding_audit.json"
    paths = (args.inputs if args.inputs else
             sorted(args.data_dir.glob("thue_support_*_audit.json")) if args.all else
             [args.data_dir / "thue_support_2_3_5_7_audit.json"])
    result = {
        "status": "FAIL",
        "audit_source_sha256": sha256(Path(__file__).read_bytes()),
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "scope": (
            "Independent finite coverage generation, exact listed-solution "
            "checks, encoding correspondence, and saved-file hashes. "
            "No CAS rerun; this is not an independent proof of PARI solver "
            "completeness, an independent CAS implementation, or Lean verification."
        ),
        "bennett_cardinality_statement_review": BENNETT_REVIEW,
        "reports": [],
    }
    try:
        require(bool(paths), "no input reports selected")
        for path in paths:
            result["reports"].append(audit_report(path, source))
        result["status"] = "PASS"
    except Exception as error:
        result["error"] = f"{type(error).__name__}: {error}"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": result["status"], "output": str(output),
        "verified_reports": len(result["reports"]),
        "verified_ordered_pairs": sum(r["verified_ordered_pair_count"] for r in result["reports"]),
        "error": result.get("error"),
    }))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
