"""Run every unittest module in isolated, bounded shards.

Each test file runs in its own process.  One slow or stateful module therefore
cannot hide the status of the rest of the suite.  The same deterministic
assignment is used locally and in GitHub Actions.
"""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time
from typing import Any


@dataclass(frozen=True)
class TestModuleResult:
    module: str
    status: str
    tests: int
    duration_seconds: float
    returncode: int | None
    output_tail: str


def discover_test_modules(root: Path) -> list[str]:
    return sorted(path.stem for path in root.glob("test_*.py") if path.is_file())


def shard_for(module: str, shard_count: int) -> int:
    digest = hashlib.sha256(module.encode("utf-8")).digest()
    return int.from_bytes(digest[:8], "big") % shard_count


def assign_shards(modules: list[str], shard_count: int) -> list[list[str]]:
    shards = [[] for _ in range(shard_count)]
    for module in modules:
        shards[shard_for(module, shard_count)].append(module)
    return shards


def unittest_context(root: Path, module: str) -> tuple[Path, str]:
    """Return the working directory and import name used by unittest."""
    if (root / "__init__.py").is_file():
        return root.parent, f"{root.name}.{module}"
    return root, module


def run_module(module: str, *, root: Path, timeout: float) -> TestModuleResult:
    started = time.perf_counter()
    cwd, target = unittest_context(root, module)
    command = [sys.executable, "-B", "-m", "unittest", target]
    env = os.environ.copy()
    import_roots = [str(root), str(root.parent)]
    if env.get("PYTHONPATH"):
        import_roots.append(env["PYTHONPATH"])
    env["PYTHONPATH"] = os.pathsep.join(import_roots)
    try:
        completed = subprocess.run(
            command,
            cwd=cwd,
            env=env,
            text=True,
            encoding="utf-8",
            errors="replace",
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=timeout,
            check=False,
        )
        output = completed.stdout or ""
        match = re.search(r"Ran\s+(\d+)\s+tests?", output)
        status = "passed" if completed.returncode == 0 else "failed"
        return TestModuleResult(
            module=module,
            status=status,
            tests=int(match.group(1)) if match else 0,
            duration_seconds=round(time.perf_counter() - started, 3),
            returncode=completed.returncode,
            output_tail=output[-6000:],
        )
    except subprocess.TimeoutExpired as exc:
        output = (exc.stdout or "") if isinstance(exc.stdout, str) else (exc.stdout or b"").decode("utf-8", "replace")
        return TestModuleResult(
            module=module,
            status="timeout",
            tests=0,
            duration_seconds=round(time.perf_counter() - started, 3),
            returncode=None,
            output_tail=output[-6000:],
        )


def run_shard(
    modules: list[str],
    *,
    shard_index: int,
    shard_count: int,
    root: Path,
    timeout: float,
) -> dict[str, Any]:
    started = time.perf_counter()
    results = [run_module(module, root=root, timeout=timeout) for module in modules]
    return build_report(results, shard_index=shard_index, shard_count=shard_count, elapsed=time.perf_counter() - started)


def build_report(
    results: list[TestModuleResult],
    *,
    shard_index: int | str,
    shard_count: int,
    elapsed: float,
) -> dict[str, Any]:
    counts: dict[str, int] = {"passed": 0, "failed": 0, "timeout": 0}
    for result in results:
        counts[result.status] = counts.get(result.status, 0) + 1
    return {
        "schema": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "shard_index": shard_index,
        "shard_count": shard_count,
        "module_count": len(results),
        "test_count": sum(result.tests for result in results),
        "status_counts": counts,
        "elapsed_seconds": round(elapsed, 3),
        "success": counts.get("failed", 0) == 0 and counts.get("timeout", 0) == 0,
        "modules": [asdict(result) for result in results],
    }


def merge_reports(paths: list[Path]) -> dict[str, Any]:
    payloads = [json.loads(path.read_text(encoding="utf-8")) for path in sorted(paths)]
    modules: dict[str, TestModuleResult] = {}
    for payload in payloads:
        for item in payload.get("modules", []):
            result = TestModuleResult(**item)
            previous = modules.get(result.module)
            if previous is not None and previous != result:
                raise ValueError(f"conflicting duplicate module result: {result.module}")
            modules[result.module] = result
    return build_report(
        [modules[name] for name in sorted(modules)],
        shard_index="all",
        shard_count=len(payloads),
        elapsed=max((float(payload.get("elapsed_seconds", 0)) for payload in payloads), default=0),
    )


def write_report(report: dict[str, Any], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({key: value for key, value in report.items() if key != "modules"}, ensure_ascii=False, indent=2))
    for item in report["modules"]:
        print(f"[{item['status'].upper():7}] {item['module']:<48} {item['duration_seconds']:>8.3f}s  tests={item['tests']}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run isolated deterministic unittest shards.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("--shards", type=int, default=8)
    parser.add_argument("--shard-index", type=int)
    parser.add_argument("--all", action="store_true", help="Run all shards concurrently in this controller.")
    parser.add_argument("--jobs", type=int, default=4, help="Maximum concurrent shards with --all.")
    parser.add_argument("--timeout", type=float, default=180.0, help="Timeout per test module in seconds.")
    parser.add_argument("--report", type=Path, default=Path("artifacts/test_shards/report.json"))
    parser.add_argument("--merge-root", type=Path, help="Merge every shard-*.json found recursively below this directory.")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.merge_root:
        paths = list(args.merge_root.rglob("shard-*.json"))
        if not paths:
            raise SystemExit(f"no shard reports found below {args.merge_root}")
        report = merge_reports(paths)
        write_report(report, args.report)
        return 0 if report["success"] else 1
    if args.shards < 1:
        raise SystemExit("--shards must be positive")
    modules = discover_test_modules(args.root)
    shards = assign_shards(modules, args.shards)
    if args.all:
        report_dir = args.report.parent
        report_dir.mkdir(parents=True, exist_ok=True)
        for stale in report_dir.glob("shard-*.json"):
            stale.unlink()
        reports: list[dict[str, Any]] = []
        with ThreadPoolExecutor(max_workers=max(1, min(args.jobs, args.shards))) as executor:
            futures = {
                executor.submit(
                    run_shard,
                    shard,
                    shard_index=index,
                    shard_count=args.shards,
                    root=args.root,
                    timeout=args.timeout,
                ): index
                for index, shard in enumerate(shards)
            }
            for future in as_completed(futures):
                report = future.result()
                reports.append(report)
                write_report(report, report_dir / f"shard-{report['shard_index']}.json")
        merged = merge_reports(sorted(report_dir.glob("shard-*.json")))
        write_report(merged, args.report)
        return 0 if merged["success"] else 1
    if args.shard_index is None or not 0 <= args.shard_index < args.shards:
        raise SystemExit("provide --shard-index in [0, --shards), or use --all")
    report = run_shard(
        shards[args.shard_index],
        shard_index=args.shard_index,
        shard_count=args.shards,
        root=args.root,
        timeout=args.timeout,
    )
    write_report(report, args.report)
    return 0 if report["success"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
