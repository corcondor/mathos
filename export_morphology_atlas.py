"""Export the morphology atlas used by autonomous generation gates."""

from __future__ import annotations

import argparse
from pathlib import Path

try:
    from math_os_prototype.morphology_graph import EDGES, NODES, shortest_path
except ImportError:  # pragma: no cover
    from morphology_graph import EDGES, NODES, shortest_path


HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT = HERE / "docs" / "generated" / "latest-morphology-atlas.md"


def render() -> str:
    distant = shortest_path("ComplexConfiguration", "ExpectationObservable") or []
    quadratic = shortest_path(
        "QuadraticCoefficientFamily", "ConditionalMomentObservable"
    ) or []
    lines = [
        "# MathOS モルフォロジー・アトラス",
        "",
        f"- 型付き表現ノード: **{len(NODES)}**",
        f"- 許可された隣接射: **{len(EDGES)}**",
        "- 裸の数値代入による接続: **0**",
        "",
        "## 採用条件",
        "",
        "異分野候補は、隣接する型付き射だけをたどり、各射で数学対象または不変量を"
        "明示的に輸送し、さらに相互作用する証明DAGの検査を通らなければならない。"
        "分野名や数値型が一致するだけでは接続として認めない。",
        "",
        "## 検証済み経路",
        "",
        "二次式の係数から条件付きモーメントまで:",
        "",
        f"`{' -> '.join(quadratic)}`",
        "",
        "複素幾何から確率の期待値まで:",
        "",
        f"`{' -> '.join(distant)}`",
        "",
        "後者には、巡回群作用、剰余類、指標和、母関数、組合せクラス、確率空間の"
        "中間表現が必要である。幾何から確率への直結辺は存在しない。",
        "",
        "## 隣接射一覧",
        "",
        "| 始域 | 射 | 終域 | 輸送される意味 |",
        "|---|---|---|---|",
    ]
    for edge in EDGES:
        lines.append(
            f"| `{edge.source}` | `{edge.name}` | `{edge.target}` | "
            f"{', '.join(edge.transport)} |"
        )
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render(), encoding="utf-8")
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
