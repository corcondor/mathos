#!/usr/bin/env python3
"""Compile the v10 recovery extension in an already prepared, pinned mathlib.

Run with `lake env python3 /path/to/this/script.py` from the mathlib checkout.
The script preserves compiler exit codes and writes fresh, hashed evidence.
It does not download dependencies or modify the original proof logs.
"""

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


def include_goal_modules(sources):
    registry = ROOT / "goal_verified_modules.json"
    if not registry.exists():
        return sources
    names = json.loads(registry.read_text())["modules"]
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
        for dependency in re.findall(r"^import ([A-Za-z][A-Za-z0-9_]*)\s*$", source.read_text(), re.M):
            if (ROOT / (dependency + ".lean")).is_file():
                visit(dependency)
        active.remove(name); seen.add(name); ordered.append(source)
    for source in sources:
        visit(source.stem)
    for name in names:
        visit(name)
    return ordered


def main():
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
    for name in ["LocalSquareRecovery", "CriticalPrimeCRT", "CFApproximationCore", "GeometricReduction", "GeometricDescent", "CFCoefficientRanges", "CFCandidateCoverage"]:
        if (ROOT / (name + ".lean")).exists():
            sources.append(ROOT / (name + ".lean"))
    sources = include_goal_modules(sources)
    records = []
    harness = policy(ROOT)
    with tempfile.TemporaryDirectory(prefix="nested-binomial-lean-") as build:
        compile_env = os.environ.copy()
        compile_env["LEAN_PATH"] = build + os.pathsep + compile_env.get("LEAN_PATH", "")
        for source in sources:
            command = ["lean", f"--root={ROOT}", "-o", str(Path(build) / (source.stem + ".olean")), str(source)]
            result = compile_lean(command, compile_env, 180, harness)
            log = ROOT / (source.stem + ".additional_check.txt")
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
            records.append(record)
            print(f"{source.name}: exit={result['exit_code']}, no proof holes={trusted}", flush=True)
            if result['exit_code'] or not trusted:
                print(result['output'])
                break
    passed = len(records) == len(sources) and all(
        r["exit_code"] == 0 and not r["proof_hole_or_custom_axiom_detected"] for r in records
    )
    report = {
        "status": "PASS" if passed else "FAIL",
        "checked_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "lean_version": lean_version,
        "mathlib_commit": mathlib_commit,
        "records": records,
        "scope": "Recovery, local-square, CRT and CF-core modules listed in records; not complete curve exclusion",
        "height_bound_formalized": False,
        "finite_search_completeness_formalized": False,
        "whole_equation_solved": False,
    }
    (ROOT / "additional_kernel_check.json").write_text(json.dumps(report, indent=2) + "\n")
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
