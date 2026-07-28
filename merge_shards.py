"""並列シャードの成果を1つのプールにまとめる（重複排除＋族上限）。"""
from __future__ import annotations
import argparse, json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

try:
    from math_os_prototype.autonomous_loop import PER_FAMILY_CAP, POOL
    from math_os_prototype.difficulty_field import (
        difficulty_band as _difficulty_band,
        difficulty_score as _difficulty_score,
    )
    from math_os_prototype.jukenmath_full_audit import canonical_surface
except ImportError:
    from autonomous_loop import PER_FAMILY_CAP, POOL
    from difficulty_field import (
        difficulty_band as _difficulty_band,
        difficulty_score as _difficulty_score,
    )
    from jukenmath_full_audit import canonical_surface


def merge(paths: list[Path]) -> dict:
    seen_answer: set[tuple[str, str]] = set()
    seen_stmt: set[str] = set()
    merged: list[dict] = []
    for path in paths:
        if not path.exists():
            continue
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        for p in payload.get("problems", []):
            akey = (p.get("family_id"), canonical_surface(str(p.get("answer_tex", ""))))
            skey = canonical_surface(str(p.get("statement_tex", "")))
            if akey in seen_answer or skey in seen_stmt:
                continue
            seen_answer.add(akey)
            seen_stmt.add(skey)
            merged.append(p)

    by_family: dict[str, list[dict]] = defaultdict(list)
    for r in sorted(merged, key=lambda r: -_difficulty_score(r)):
        if len(by_family[r["family_id"]]) >= PER_FAMILY_CAP:
            continue
        by_family[r["family_id"]].append(r)
    out: list[dict] = []
    queues = list(by_family.values())
    while any(queues):
        for q in queues:
            if q:
                out.append(q.pop(0))
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "method": {"name": "MathOS autonomous pool (parallel shards merged)"},
        "summary": {
            "total": len(out),
            "shards": len(paths),
            "family_counts": dict(Counter(r["family_id"] for r in out)),
            "band_counts": dict(Counter(_difficulty_band(r) for r in out)),
        },
        "problems": out,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--inputs", nargs="+", type=Path, required=True)
    ap.add_argument("--output", type=Path, default=POOL)
    args = ap.parse_args()
    report = merge(list(args.inputs))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(report["summary"], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
