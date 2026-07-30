"""MathOS の問題が、参照コーパスと比べてどの位置にあるかを測る。

比べる相手は 2 つ:

  * 手作りの難問コーパス（corpus/ の .tex と curation.db）
      = ユーザ自身が作った問題。difficulty の較正に使ったのもこれ。
  * 過去問コーパス（東大・京大ほか、約28,000問）

読み方の注意を先に書く。ここで使う difficulty は、ユーザの手作り問題に
合わせて較正した指標である。つまり測っているのは
  「その人の難問と同じ形をしているか」
であって、「客観的に難しいか」ではない。数オリの本選問題を解けるかどうかを
測るものでもない。指標が何を見ているかを外して読むと誤る。

それでも意味はある。同じ物差しで 3 つの分布を並べれば、
MathOS の出力が手作り問題の分布のどこに落ちるかは分かる。
"""

from __future__ import annotations

import json
import statistics
import sys
from pathlib import Path
from typing import Any

try:
    from math_os_prototype.world_novelty_check import (
        difficulty, load_local_hard_corpus, load_world_corpus,
    )
except ImportError:  # pragma: no cover
    from world_novelty_check import (
        difficulty, load_local_hard_corpus, load_world_corpus,
    )

HERE = Path(__file__).resolve().parent
POOL = HERE / "problem_synthesis" / "entrance_exam_pool.json"


def score_of(statement: str, solution: str = "") -> float:
    return float(difficulty({
        "statement_tex": statement,
        "solution_tex": solution,
    }).get("score", 0.0))


def percentile(values: list[float], q: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    index = min(len(ordered) - 1, max(0, int(round(q * (len(ordered) - 1)))))
    return ordered[index]


def describe(name: str, values: list[float]) -> dict[str, Any]:
    if not values:
        return {"name": name, "count": 0}
    return {
        "name": name,
        "count": len(values),
        "median": statistics.median(values),
        "p75": percentile(values, 0.75),
        "p90": percentile(values, 0.90),
        "p99": percentile(values, 0.99),
        "max": max(values),
    }


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")

    pool = json.loads(POOL.read_text(encoding="utf-8"))
    mathos = [
        score_of(p.get("statement_tex") or "", p.get("solution_tex") or "")
        for p in pool["problems"]
    ]

    handmade = [
        score_of(item.get("statement", ""), item.get("solution", ""))
        for item in load_local_hard_corpus()
    ]

    world = load_world_corpus()
    past = [score_of(item.get("statement", "")) for item in world]

    rows = [
        describe("MathOS 生成", mathos),
        describe("手作りの難問", handmade),
        describe("過去問", past),
    ]

    print("難易度スコアの分布（同じ物差しで比較）")
    print(f"{'集合':<14}{'問題数':>8}{'中央値':>9}{'75%':>8}{'90%':>8}{'99%':>8}{'最大':>8}")
    for row in rows:
        if not row["count"]:
            print(f"{row['name']:<14}{'—':>8}")
            continue
        print(
            f"{row['name']:<14}{row['count']:>8}"
            f"{row['median']:>9.2f}{row['p75']:>8.2f}{row['p90']:>8.2f}"
            f"{row['p99']:>8.2f}{row['max']:>8.2f}"
        )

    print()
    for reference, label in ((handmade, "手作りの難問"), (past, "過去問")):
        if not reference or not mathos:
            continue
        for q, tag in ((0.5, "中央値"), (0.75, "75%点"), (0.9, "90%点")):
            threshold = percentile(reference, q)
            above = sum(1 for value in mathos if value >= threshold)
            print(
                f"  {label}の{tag}({threshold:.2f}) を超える MathOS の問題: "
                f"{above}/{len(mathos)} ({above / len(mathos):.0%})"
            )
        print()

    # 射の連鎖の深さも並べておく（生成側にしかない指標）
    depths = [
        len((p.get("lift_certificate") or {}).get("morphism_chain") or [])
        for p in pool["problems"]
    ]
    if depths:
        print(f"射の連鎖の深さ: 中央値 {statistics.median(depths):.0f} / "
              f"最大 {max(depths)} / 平均 {statistics.mean(depths):.1f}")

    print()
    print("読み方: この指標はユーザの手作り問題に較正してある。")
    print("        『その人の難問と同じ形か』を測っており、")
    print("        『客観的に難しいか』『数オリで通用するか』は測っていない。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
