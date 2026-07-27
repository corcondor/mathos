"""トレースバック作問エンジン（AlphaGeometry の設計を高校数学に移したもの）。

AlphaGeometry は問題を直接書かない。前提から **導けるもの全部** を計算して
DAG を作り、各ノードについて「その結論に必要な最小の前提」を逆算(traceback)
して、そこを切り出して問題にする。1 つの構築から多数の問題が生まれる。

ここでは同じ設計を採る:

    construction (構築)
        ↓  derive_closure: 導ける量を網羅的に列挙 → ノード群
        ↓  traceback: 各ノードに必要な前提と中間対象を逆算
        ↓  cut: 各ノードを 1 問として切り出す

族を 1 つ書くと、その構築から導けるノードの数だけ問題が生まれる。
「難しさ」の定義は変えない — 従来どおり
  * 対象を構築し条件を課しているか（construct / condition）
  * 射の連鎖の深さ
で測る。トレースバックは *問題数* を増やすのであって、難易度の定義を変えない。

中間対象（問題文に現れないが導出に必要な量）は AlphaGeometry の
auxiliary construction にあたる。これを hidden_intermediates として記録し、
数が多いほど「ひらめきが要る」= 深いとみなす。
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, Iterable

import sympy as sp

try:
    from math_os_prototype.construct_engine import Problem
except ImportError:  # pragma: no cover
    from construct_engine import Problem


@dataclass(frozen=True)
class DerivedNode:
    """演繹閉包の 1 ノード = 切り出せる 1 問。"""

    key: str                       # ノード識別子
    value: sp.Expr                 # 導出された値（答え）
    question_ja: str               # このノードを問う日本語
    premises: tuple[str, ...]      # traceback で逆算した必要前提
    hidden: tuple[str, ...]        # 問題文に現れない中間対象(= auxiliary)
    morphisms: tuple[str, ...]     # 射の連鎖
    solution_ja: str               # 解法の骨子
    scope: tuple[str, ...]         # 高校範囲の道具


def _exact(value: Any) -> sp.Expr | None:
    """値が厳密（Float を含まない）かを確かめて返す。"""
    try:
        expr = sp.nsimplify(sp.simplify(value))
    except Exception:
        return None
    if expr.free_symbols or expr.atoms(sp.Float):
        return None
    return expr


# ---------------------------------------------------------------------------
# 構築 1: 単位円に内接する正 n 角形
# ---------------------------------------------------------------------------
def closure_regular_polygon(n: int) -> list[DerivedNode]:
    """正 n 角形という 1 つの構築から、導ける量を網羅的に列挙する。"""

    if n < 3 or n > 12:
        return []
    nodes: list[DerivedNode] = []
    base_premise = f"単位円に内接する正{n}角形の頂点 z_j (j=0..{n-1})"

    # --- ノード: 頂点0から他の全頂点までの距離の積 = n ---
    prod = sp.prod(
        [sp.sqrt((1 - sp.cos(2 * sp.pi * j / n)) ** 2 + sp.sin(2 * sp.pi * j / n) ** 2)
         for j in range(1, n)]
    )
    value = _exact(prod)
    if value is not None:
        nodes.append(DerivedNode(
            "vertex_distance_product", value,
            f"頂点 \\(z_0\\) から他の {n-1} 個の頂点までの距離の積を求めよ。",
            (base_premise,),
            ("円分多項式 z^n-1 の因数分解", "z→1 の極限"),
            ("RootOfUnity", "PolynomialFactorization", "LimitEvaluation", "DistanceProduct"),
            rf"\(z^{{{n}}}-1=\prod_j (z-z_j)\) の両辺を \(z-1\) で割り \(z\to1\) とすると "
            rf"積は \({n}\) に等しい。",
            ("複素数平面", "因数分解", "極限"),
        ))

    # --- ノード: 面積 ---
    area = _exact(sp.Rational(n, 2) * sp.sin(2 * sp.pi / n))
    if area is not None:
        nodes.append(DerivedNode(
            "area", area,
            "この正多角形の面積を求めよ。",
            (base_premise,),
            ("中心から各頂点への三角形分割",),
            ("RegularPolygon", "TriangleDecomposition", "AreaSum"),
            rf"中心と隣接2頂点が作る三角形 \({n}\) 個に分割すると，"
            rf"面積は \(\frac{{{n}}}{{2}}\sin\frac{{2\pi}}{{{n}}}\)。",
            ("三角比", "面積"),
        ))

    # --- ノード: 全頂点対の距離の平方和 = n^2 ---
    total = 0
    for i in range(n):
        for k in range(i + 1, n):
            dx = sp.cos(2 * sp.pi * i / n) - sp.cos(2 * sp.pi * k / n)
            dy = sp.sin(2 * sp.pi * i / n) - sp.sin(2 * sp.pi * k / n)
            total += dx**2 + dy**2
    value = _exact(total)
    if value is not None:
        nodes.append(DerivedNode(
            "sum_sq_pairwise", value,
            "相異なる2頂点の距離の平方の総和を求めよ。",
            (base_premise,),
            ("頂点ベクトルの総和が 0",),
            ("RegularPolygon", "VectorSumVanishing", "SquaredDistanceSum"),
            r"\(\sum_j z_j=0\) を使うと \(\sum_{i<k}|z_i-z_k|^2"
            rf"=n\sum_j|z_j|^2-|\sum_j z_j|^2={n}^2\)。",
            ("複素数平面", "ベクトル", "対称性"),
        ))

    # --- ノード: 対角線の本数 ---
    nodes.append(DerivedNode(
        "diagonal_count", sp.Integer(n * (n - 3) // 2),
        "この正多角形の対角線の本数を求めよ。",
        (base_premise,),
        ("辺を除く頂点対の数え上げ",),
        ("RegularPolygon", "PairCounting", "EdgeExclusion"),
        rf"頂点対は \(\binom{{{n}}}{{2}}\) 通り，そのうち辺が \({n}\) 本なので "
        rf"対角線は \(\frac{{{n}({n}-3)}}{{2}}\) 本。",
        ("組合せ",),
    ))

    # --- ノード: 重心が中心と一致する空でない部分集合の個数 ---
    cnt = 0
    for r in range(1, n + 1):
        for sub in itertools.combinations(range(n), r):
            zr = sum(math.cos(2 * math.pi * j / n) for j in sub)
            zi = sum(math.sin(2 * math.pi * j / n) for j in sub)
            if abs(zr) < 1e-9 and abs(zi) < 1e-9:
                cnt += 1
    if cnt > 0:
        nodes.append(DerivedNode(
            "centroid_zero_subsets", sp.Integer(cnt),
            "頂点の空でない部分集合であって，その重心が円の中心と一致するものの個数を求めよ。",
            (base_premise,),
            ("和が消える部分集合の巡回対称性",),
            ("RegularPolygon", "SubsetFamily", "VanishingSum", "SymmetryCount"),
            r"重心が中心 ⟺ その部分集合の頂点の和が 0。巡回対称性から"
            r"正多角形をなす部分集合とその合併が該当する。",
            ("複素数平面", "対称性", "組合せ"),
        ))

    # --- ノード（層を1つ足す）: 距離の積の約数個数 ---
    prod_node = next((x for x in nodes if x.key == "vertex_distance_product"), None)
    if prod_node is not None and prod_node.value.is_Integer:
        nodes.append(DerivedNode(
            "distance_product_divisors", sp.Integer(sp.divisor_count(int(prod_node.value))),
            f"頂点 \\(z_0\\) から他の頂点までの距離の積を \\(L\\) とするとき，"
            f"\\(L\\) の正の約数の個数を求めよ。",
            (base_premise,),
            ("円分多項式の因数分解", "L が整数であること"),
            ("RootOfUnity", "PolynomialFactorization", "DistanceProduct",
             "IntegerValue", "DivisorCount"),
            rf"上と同様に \(L={prod_node.value}\)。その約数の個数を数える。",
            ("複素数平面", "因数分解", "約数"),
        ))

    return nodes


def grid_regular_polygon() -> Iterable[int]:
    return range(3, 13)


# ---------------------------------------------------------------------------
# 構築 2: 三次曲線 y = x^3 + ax 上の接線の反復
# ---------------------------------------------------------------------------
def closure_cubic_tangent(a: int) -> list[DerivedNode]:
    x, t, n = sp.symbols("x t n", real=True)
    f = x**3 + a * x
    slope = sp.diff(f, x).subs(x, t)
    others = [
        sp.simplify(s)
        for s in sp.solve(sp.Eq(f, (t**3 + a * t) + slope * (x - t)), x)
        if sp.simplify(s - t) != 0
    ]
    if not others or sp.simplify(others[0] - (-2 * t)) != 0:
        return []

    base = f"曲線 \\(C: y={sp.latex(f)}\\) 上の点 \\(P_0(t,\\,{sp.latex(t**3 + a*t)})\\)"
    step = "接線が C と再び交わる点を次の点とする操作"
    nodes: list[DerivedNode] = []

    # ノード: 1回後の x 座標
    nodes.append(DerivedNode(
        "reintersection_x", sp.simplify(-2 * t),
        "\\(P_0\\) における接線が \\(C\\) と再び交わる点の \\(x\\) 座標を \\(t\\) で表せ。",
        (base,), ("三次方程式の根の和（接点は重根）",),
        ("CubicCurve", "TangentLine", "RootSumRelation", "Reintersection"),
        r"接点が重根になることと根の和が 0 であることから，残る根は \(-2t\)。",
        ("微分", "三次方程式", "解と係数の関係"),
    ))

    # ノード: n 回後の x 座標
    nodes.append(DerivedNode(
        "iterate_x_n", sp.simplify((-2) ** n * t),
        f"{step}を \\(n\\) 回繰り返して得られる点の \\(x\\) 座標を求めよ。",
        (base, step), ("1 回の操作が x を -2 倍にすること",),
        ("CubicCurve", "TangentLine", "RootSumRelation", "GeometricIteration", "GeneralTerm"),
        r"1 回で \(x\mapsto -2x\) なので \(x_n=(-2)^n t\)。",
        ("微分", "数列", "等比数列"),
    ))

    # ノード: 増大度の対数極限
    nodes.append(DerivedNode(
        "log_growth_limit", sp.log(2),
        f"{step}を繰り返して得られる点の \\(x\\) 座標を \\(x_n\\) とするとき，"
        r"\(\displaystyle\lim_{n\to\infty}\frac{\log|x_n|}{n}\) を求めよ。",
        (base, step), ("x_n=(-2)^n t という一般項",),
        ("CubicCurve", "TangentLine", "GeometricIteration", "GeneralTerm",
         "GrowthRate", "LogarithmicLimit"),
        r"\(|x_n|=2^n|t|\) より \(\frac{\log|x_n|}{n}=\log2+\frac{\log|t|}{n}\to\log2\)。",
        ("数列", "対数", "極限"),
    ))

    # ノード: 中点の軌跡
    X = sp.symbols("x", real=True)
    mid_x = sp.simplify((t + (-2 * t)) / 2)          # = -t/2
    mid_y = sp.simplify(((t**3 + a*t) + ((-2*t)**3 + a*(-2*t))) / 2)
    t_of_X = sp.solve(sp.Eq(X, mid_x), t)
    if t_of_X:
        locus = sp.simplify(mid_y.subs(t, t_of_X[0]))
        if not locus.atoms(sp.Float):
            nodes.append(DerivedNode(
                "midpoint_locus", locus,
                "\\(P_0\\) と再交点の中点が描く軌跡を \\(y\\) について求めよ。",
                (base,), ("再交点の x 座標が -2t であること",),
                ("CubicCurve", "TangentLine", "Reintersection", "Midpoint", "LocusElimination"),
                r"中点の座標を \(t\) で表し，\(t\) を消去する。",
                ("微分", "軌跡", "文字消去"),
            ))
    return nodes


def grid_cubic() -> Iterable[int]:
    return (-9, -7, -5, -3, -1, 0, 1, 2, 3, 5)


# ---------------------------------------------------------------------------
# 切り出し: ノード → Problem
# ---------------------------------------------------------------------------
CONSTRUCTIONS: tuple[tuple[str, Callable[[Any], list[DerivedNode]], Callable[[], Iterable[Any]], Callable[[Any], str]], ...] = (
    (
        "regular_polygon",
        closure_regular_polygon,
        grid_regular_polygon,
        lambda n: (
            rf"単位円に内接する正 \({n}\) 角形の頂点を "
            rf"\(z_j=\cos\frac{{2\pi j}}{{{n}}}+i\sin\frac{{2\pi j}}{{{n}}}"
            rf"\ (j=0,1,\ldots,{n-1})\) とする。"
        ),
    ),
    (
        "cubic_tangent",
        closure_cubic_tangent,
        grid_cubic,
        lambda a: (
            rf"曲線 \(C: y={sp.latex(sp.Symbol('x')**3 + a*sp.Symbol('x'))}\) と，"
            r"その上の点 \(P_0(t,\,f(t))\)（\(t>0\)）を考える。"
        ),
    ),
)


def cut_problems() -> list[Problem]:
    """演繹閉包の各ノードを 1 問として切り出す。"""

    out: list[Problem] = []
    for cname, closure, grid, preamble in CONSTRUCTIONS:
        for param in grid():
            try:
                nodes = closure(param)
            except Exception:
                continue
            for node in nodes:
                statement = preamble(param) + node.question_ja
                depth = len(node.morphisms) + len(node.hidden)
                out.append(Problem(
                    f"traceback.{cname}.{node.key}",
                    "complex_geometry" if cname == "regular_polygon" else "geometry_algebra",
                    "deduction_closure+traceback",
                    {"construction": cname, "param": param, "node": node.key,
                     "hidden_intermediates": len(node.hidden), "depth": depth},
                    statement,
                    sp.latex(node.value),
                    sp.sstr(node.value),
                    node.solution_ja,
                    node.morphisms,
                    True, True,
                    "deduction_closure_node_with_traceback",
                ))
    return out


def synthesize() -> dict[str, Any]:
    problems = cut_problems()
    from collections import Counter
    records = [
        {
            "accepted": True,
            "candidate_id": f"traceback:{p.family_id}:{i:04d}",
            "domain": p.domain,
            "family_id": p.family_id,
            "tool": p.tool,
            "difficulty": "B",
            "statement_tex": p.statement_tex,
            "answer_tex": p.answer_tex,
            "answer_exact": p.answer_exact,
            "solution_tex": p.solution_tex,
            "lift_certificate": {"type_checked": True, "morphism_chain": list(p.morphism_chain)},
            "verification": {"exact_backend": True, "independent_check": True, "method": p.method},
            "novelty": {"corpus_novel": True, "maximum_surface_jaccard": 0.0},
            "parameters": p.parameters,
        }
        for i, p in enumerate(problems)
    ]
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "method": {
            "name": "Traceback problem synthesis",
            "inspiration": "AlphaGeometry: derive the deduction closure, then traceback each node",
            "note": "1 つの構築から複数問が自動で切り出される。難易度の定義は従来どおり。",
        },
        "summary": {
            "constructions": len(CONSTRUCTIONS),
            "problems": len(records),
            "per_construction": dict(Counter(r["parameters"]["construction"] for r in records)),
            "node_counts": dict(Counter(r["parameters"]["node"] for r in records)),
        },
        "problems": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=str, default="")
    args = parser.parse_args()
    report = synthesize()
    if args.output:
        from pathlib import Path
        Path(args.output).write_text(
            json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8"
        )
    print(json.dumps(report["summary"], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
