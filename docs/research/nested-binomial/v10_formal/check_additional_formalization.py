#!/usr/bin/env python3
"""Compile the v10 recovery extension in an already prepared, pinned mathlib.

Run with `lake env python3 /path/to/this/script.py` from the mathlib checkout.
The script preserves compiler exit codes and writes fresh, hashed evidence.
It does not download dependencies or modify the original proof logs.
"""

import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from deepseek_lean_harness import compile_lean, policy


ROOT = Path(__file__).resolve().parent
MATHLIB_COMMIT = "56a005855ea17e0b0958f73ec801ae140b0a1679"


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def local_imports(source):
    return [ROOT / (name + ".lean") for name in
            re.findall(r"^import ([A-Za-z][A-Za-z0-9_]*)\s*$", source.read_text(), re.M)
            if (ROOT / (name + ".lean")).is_file()]


def include_goal_modules(sources, *, include_registry=True):
    registry = ROOT / "goal_verified_modules.json"
    names = json.loads(registry.read_text())["modules"] if include_registry and registry.exists() else []
    ordered, seen, active = [], set(), set()
    def visit(name):
        if not isinstance(name, str) or not re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*", name):
            raise ValueError("Invalid registered Lean module")
        if name in active:
            raise ValueError("Cyclic local Lean imports")
        if name in seen:
            return
        source = ROOT / (name + ".lean")
        if not source.is_file():
            raise ValueError("Registered Lean module missing: " + name)
        active.add(name)
        for dependency in local_imports(source):
            visit(dependency.stem)
        active.remove(name); seen.add(name); ordered.append(source)
    for source in sources:
        visit(source.stem)
    for name in names:
        visit(name)
    return ordered


def reusable_records(sources, lean_version, mathlib_commit):
    repo = ROOT.parents[3]
    report_path = (ROOT / "additional_kernel_check.json").relative_to(repo).as_posix()
    try:
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo, text=True).strip()
        prior = json.loads(subprocess.check_output(
            ["git", "show", f"{commit}:{report_path}"], cwd=repo, stderr=subprocess.DEVNULL
        ))
    except (OSError, ValueError, subprocess.SubprocessError):
        return {}, None
    if (not isinstance(prior, dict) or not isinstance(prior.get("records"), list)
            or (prior.get("status"), prior.get("lean_version"), prior.get("mathlib_commit"))
            != ("PASS", lean_version, mathlib_commit)):
        return {}, None
    previous = {record["source"]: record for record in prior["records"]
                if isinstance(record, dict) and isinstance(record.get("source"), str)}
    reusable = {}
    for source in sources:
        record = previous.get(source.name)
        log = ROOT / (source.stem + ".additional_check.txt")
        if (record and record.get("exit_code") == 0 and record.get("proof_hole_or_custom_axiom_detected") is False
                and record.get("source_sha256") == sha256(source)
                and record.get("log") == log.name and log.is_file() and record.get("log_sha256") == sha256(log)
                and all(dependency.name in reusable for dependency in local_imports(source))):
            reusable[source.name] = record
    return reusable, commit


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=ROOT)
    parser.add_argument("--recheck", action="append", default=[], metavar="MODULE",
                        help="Compile this module and its dependencies, reusing matching committed checks")
    args = parser.parse_args()
    if args.recheck and args.output_dir.resolve() != ROOT:
        parser.error("--recheck uses the committed verification logs in the proof directory")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    mathlib_commit = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], text=True
    ).strip()
    if mathlib_commit != MATHLIB_COMMIT:
        raise SystemExit(f"Expected mathlib {MATHLIB_COMMIT}, got {mathlib_commit}")
    lean_version = subprocess.check_output(["lean", "--version"], text=True).strip()
    if not lean_version.startswith("Lean (version 4.35.0,"):
        raise SystemExit(f"Expected Lean 4.35.0, got {lean_version}")
    sources = [ROOT / "ValuationRecovery.lean", ROOT / "RecoveredDivisor.lean"]
    if (ROOT / "NormalizedCancellation.lean").exists():
        sources.append(ROOT / "NormalizedCancellation.lean")
    for name in ["LocalSquareRecovery", "CriticalPrimeCRT", "CFApproximationCore", "GeometricReduction", "GeometricDescent", "CFCoefficientRanges", "CFCandidateCoverage", "IntegralLiftModel", "LocalCubeCover7", "CFBoundedDivisorBridge", "CFTwistedCubeAlgebra"]:
        if (ROOT / (name + ".lean")).exists():
            sources.append(ROOT / (name + ".lean"))
    sources = include_goal_modules(sources)
    if set(args.recheck) - {source.stem for source in sources}:
        parser.error("--recheck requires registered Lean modules")
    cached, prior_commit = reusable_records(sources, lean_version, mathlib_commit) if args.recheck else ({}, None)
    fresh = include_goal_modules(
        [source for source in sources if source.name not in cached or source.stem in args.recheck],
        include_registry=False,
    )
    fresh_names = {source.name for source in fresh}
    records = {name: record for name, record in cached.items() if name not in fresh_names}
    reused = sorted(records)
    harness = policy(ROOT)
    with tempfile.TemporaryDirectory(prefix="nested-binomial-lean-") as build:
        compile_env = os.environ.copy()
        compile_env["LEAN_PATH"] = build + os.pathsep + compile_env.get("LEAN_PATH", "")
        for source in fresh:
            command = ["lean", f"--root={ROOT}", "-o", str(Path(build) / (source.stem + ".olean")), str(source)]
            result = compile_lean(command, compile_env, 180, harness)
            log = args.output_dir / (source.stem + ".additional_check.txt")
            log.write_text(result['output'])
            forbidden = bool(re.search(r"\b(sorry|admit|axiom|native_decide)\b", source.read_text()))
            trusted = "sorryAx" not in result['output'] and not forbidden
            for axiom_list in re.findall(r"depends on axioms:\s*\[([^\]]*)\]", result['output']):
                if set(re.findall(r"[A-Za-z_][\w.]*", axiom_list)) - {"propext", "Classical.choice", "Quot.sound"}:
                    trusted = False
            record = {
                "source": source.name,
                "source_sha256": sha256(source),
                "log": log.name,
                "log_sha256": sha256(log),
                "exit_code": result['exit_code'],
                "proof_hole_or_custom_axiom_detected": not trusted,
                "command": result['command'],
                "resource_attempts": result['resource_attempts'],
                "warnings": result['analysis']['warnings'],
            }
            records[source.name] = record
            print(f"{source.name}: exit={result['exit_code']}, no proof holes={trusted}", flush=True)
            if result['exit_code'] or not trusted:
                print(result['output'])
                break
    ordered_records = [records[source.name] for source in sources if source.name in records]
    passed = len(ordered_records) == len(sources) and all(
        r["exit_code"] == 0 and not r["proof_hole_or_custom_axiom_detected"] for r in ordered_records
    )
    report = {
        "status": "PASS" if passed else "FAIL",
        "checked_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "lean_version": lean_version,
        "mathlib_commit": mathlib_commit,
        "records": ordered_records,
        "scope": "Recovery, local-square, CRT and CF-core modules listed in records; not complete curve exclusion",
        "height_bound_formalized": False,
        "finite_search_completeness_formalized": False,
        "whole_equation_solved": False,
    }
    if reused:
        report["reused_verification"] = {"commit": prior_commit, "sources": reused}
    (args.output_dir / "additional_kernel_check.json").write_text(json.dumps(report, indent=2) + "\n")
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
