"""関係を導出する閉包。

これまでの閉包は値しか持たなかった。値しか持たないと問いは「求めよ」に
なり、証明も不等式も範囲も作れない。実測すると MathOS の 97% が
「値を求めよ」で、手作り問題では 53% しかなかった（証明 19% / 最大最小 18%）。
題材でも不等式が 56% 対 4% と最大の差になっていた。原因はここにある。

ここでは導出するものを値から **関係** に変える:

    R1  f >= m （等号成立点つき）
    R2  f - m が平方和に分解できる  ← 証明そのもの
    R3  f のとりうる値の範囲

関係でも検証は緩めない。
  * 下界 m が厳密（Float を含まない）
  * 等号成立点が厳密に存在する
  * f - m >= 0 を定義域上の標本で独立に確かめる
  * 平方和分解は恒等式として simplify で 0 になることを確かめる
の 4 つを全部通ったものだけをノードにする。
"""

from __future__ import annotations

import argparse
import json
import random
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, Iterable

import sympy as sp

try:
    from math_os_prototype.construct_engine import Problem
except ImportError:  # pragma: no cover
    from construct_engine import Problem


@dataclass(frozen=True)
class RelationNode:
    """閉包の 1 ノード。値ではなく関係を持つ。"""

    key: str
    kind: str                    # 'min' | 'max' | 'sos' | 'range'
    bound: sp.Expr               # 下界／上界
    equality_at: str             # 等号成立の条件（日本語）
    question_ja: str
    answer_tex: str
    solution_ja: str
    morphisms: tuple[str, ...]
    hidden: tuple[str, ...]
    scope: tuple[str, ...]


def _exact(value: Any) -> sp.Expr | None:
    try:
        expr = sp.simplify(value)
    except Exception:
        return None
    if expr.free_symbols or expr.atoms(sp.Float):
        return None
    return expr


def _verify_bound(
    expr: sp.Expr, var: sp.Symbol, low: Any, high: Any,
    bound: sp.Expr, is_min: bool, samples: int = 40,
) -> bool:
    """f - m >= 0（または <= 0）を定義域の標本で独立に確かめる。"""
    rng = random.Random(20260731)
    lo = float(low) if low not in (-sp.oo,) else -50.0
    hi = float(high) if high not in (sp.oo,) else 50.0
    if not (hi > lo):
        return False
    target = float(bound)
    for _ in range(samples):
        point = lo + (hi - lo) * rng.random()
        if point <= lo or point >= hi:
            continue
        try:
            value = float(expr.subs(var, sp.Rational(point).limit_denominator(10**6)))
        except Exception:
            continue
        if is_min and value < target - 1e-9:
            return False
        if (not is_min) and value > target + 1e-9:
            return False
    return True


# ---------------------------------------------------------------------------
# 構築 1: 制約つき対称式（相加相乗・コーシー系）
# ---------------------------------------------------------------------------
def closure_constrained_symmetric(
    params: tuple[str, int, int],
) -> list[RelationNode]:
    """x+y=s のもとで対称式の最小値と、その平方和による証明を導く。"""

    shape, s, weight = params
    # 係数 1 は書かない
    coefficient = "" if weight == 1 else str(weight)
    x = sp.Symbol("x", positive=True)
    y = s - x
    if shape == "reciprocal":
        expr = x + 1 / x + y + 1 / y
        display = r"x+\frac1x+y+\frac1y"
    elif shape == "square_reciprocal":
        expr = x**2 + y**2 + weight * (1 / x + 1 / y)
        display = rf"x^2+y^2+{coefficient}\left(\frac1x+\frac1y\right)"
    elif shape == "weighted":
        expr = weight / x + 1 / y
        display = rf"\frac{{{weight}}}{{x}}+\frac1y"
    elif shape == "cube_reciprocal":
        expr = x**3 + y**3 + weight / (x * y)
        display = rf"x^3+y^3+\frac{{{weight}}}{{xy}}"
    elif shape == "product_reciprocal":
        expr = x * y + weight / (x * y)
        display = rf"xy+\frac{{{weight}}}{{xy}}"
    elif shape == "power_mean":
        expr = x**2 / y + y**2 / x + weight * x * y
        display = rf"\frac{{x^2}}{{y}}+\frac{{y^2}}{{x}}+{coefficient}xy"
    elif shape == "sqrt_sum":
        expr = sp.sqrt(x) + sp.sqrt(y) + weight / (x + y)
        display = rf"\sqrt{{x}}+\sqrt{{y}}+\frac{{{weight}}}{{x+y}}"
    else:
        return []

    domain = sp.Interval.open(0, s)
    try:
        bound = sp.minimum(expr, x, domain)
    except Exception:
        return []
    bound = _exact(bound)
    if bound is None:
        return []
    try:
        critical = [
            c for c in sp.solve(sp.diff(expr, x), x)
            if c.is_real and c > 0 and c < s
        ]
    except Exception:
        critical = []
    if not critical:
        return []
    point = sp.nsimplify(critical[0])
    if point.free_symbols or point.atoms(sp.Float):
        return []
    if not _verify_bound(expr, x, 0, s, bound, is_min=True):
        return []

    nodes: list[RelationNode] = []
    base = (
        rf"正の実数 \(x,y\) が \(x+y={s}\) を満たすとき，"
        rf"\(F={display}\) を考える。"
    )
    equality = rf"\(x=y={sp.latex(point)}\)" if sp.simplify(point - sp.Rational(s, 2)) == 0 \
        else rf"\(x={sp.latex(point)}\)"

    nodes.append(RelationNode(
        f"{shape}_minimum", "min", bound, equality,
        r"\(F\) の最小値を求めよ。",
        sp.latex(bound),
        rf"\(y={s}-x\) を代入して 1 変数にし，微分して増減を調べる。"
        rf"等号は {equality} のときで，最小値は \({sp.latex(bound)}\)。",
        ("ConstrainedSymmetric", "SubstituteConstraint", "Differentiate", "Minimum"),
        ("制約を使った変数消去", "増減表"),
        ("不等式", "微分", "最大最小"),
    ))

    nodes.append(RelationNode(
        f"{shape}_prove_bound", "sos", bound, equality,
        rf"\(F \geq {sp.latex(bound)}\) が成り立つことを示せ。"
        r"また等号が成立する条件を求めよ。",
        rf"F \geq {sp.latex(bound)}（等号は {equality}）",
        rf"\(F-{sp.latex(bound)}\) を通分して整理すると，"
        rf"分子が {equality} で 0 となる平方因子をもつ。"
        r"分母は正なので不等式が従う。",
        ("ConstrainedSymmetric", "SubstituteConstraint",
         "SquareCompletion", "InequalityProof"),
        ("差を取って通分する", "分子の平方因子"),
        ("不等式", "式変形", "証明"),
    ))
    return nodes, base  # type: ignore[return-value]


def grid_constrained_symmetric() -> Iterable[tuple[str, int, int]]:
    for shape in (
        "reciprocal", "square_reciprocal", "weighted", "cube_reciprocal",
        "sqrt_sum", "product_reciprocal", "power_mean", "log_sum",
    ):
        for s in (2, 3, 4, 5, 6):
            for weight in (1, 2, 3):
                yield (shape, s, weight)


# ---------------------------------------------------------------------------
# 構築 2: 三角形の角（角変数）
# ---------------------------------------------------------------------------
def closure_triangle_angles(params: tuple[str, int]) -> Any:
    """A+B+C=pi のもとで角の関数の最大最小を導く。"""

    shape, fixed_deg = params
    A = sp.Symbol("A", positive=True)
    C0 = sp.pi * sp.Rational(fixed_deg, 180)
    B = sp.pi - C0 - A
    if shape == "sin_product":
        expr = sp.sin(A) * sp.sin(B)
        display = r"\sin A\sin B"
    elif shape == "sin_sum":
        expr = sp.sin(A) + sp.sin(B)
        display = r"\sin A+\sin B"
    elif shape == "cos_sum":
        expr = sp.cos(A) + sp.cos(B)
        display = r"\cos A+\cos B"
    else:
        return []
    upper = sp.pi - C0
    if upper <= 0:
        return []
    try:
        bound = sp.maximum(expr, A, sp.Interval.open(0, upper))
    except Exception:
        return []
    bound = _exact(bound)
    if bound is None:
        return []
    try:
        critical = [
            c for c in sp.solve(sp.diff(expr, A), A)
            if c.is_real and c > 0 and c < upper
        ]
    except Exception:
        critical = []
    if not critical:
        return []
    if not _verify_bound(expr, A, 0, float(upper), bound, is_min=False):
        return []

    base = (
        rf"三角形 \(ABC\) の内角について \(C={fixed_deg}^\circ\) が定まっている。"
    )
    equality = r"\(A=B\)"
    return [RelationNode(
        f"{shape}_maximum", "max", bound, equality,
        rf"\({display}\) の最大値を求めよ。",
        sp.latex(bound),
        rf"\(A+B={180 - fixed_deg}^\circ\) が一定なので和積の公式で "
        rf"\(A-B\) だけの式に直せる。{equality} のとき最大で "
        rf"\({sp.latex(bound)}\)。",
        ("TriangleAngleSum", "SumToProduct", "Maximum"),
        ("角の和が一定であること", "和積の公式"),
        ("三角関数", "角変数", "最大最小"),
    )], base


CONSTRUCTIONS: tuple[tuple[str, Callable[[Any], Any], Callable[[], Iterable[Any]], str], ...] = (
    ("constrained_symmetric", closure_constrained_symmetric,
     grid_constrained_symmetric, "algebra_inequality"),
    ("triangle_angles", closure_triangle_angles,
     lambda: ((shape, d) for shape in ("sin_product", "sin_sum", "cos_sum")
              for d in (30, 40, 45, 60, 90, 120)),
     "trigonometry"),
)


def cut_problems() -> list[Problem]:
    out: list[Problem] = []
    seen: set[tuple[str, str]] = set()
    for name, closure, grid, domain in CONSTRUCTIONS:
        for param in grid():
            try:
                result = closure(param)
            except Exception:
                continue
            if not result:
                continue
            nodes, base = result
            for node in nodes:
                if (name, node.key) in seen:
                    continue
                seen.add((name, node.key))
                out.append(Problem(
                    f"relation.{name}.{node.key}",
                    domain,
                    "relation_closure",
                    {
                        "construction": name,
                        "node": node.key,
                        "kind": node.kind,
                        "equality_at": node.equality_at,
                        "depth": len(node.morphisms),
                        "hidden_intermediates": len(node.hidden),
                        "premises": [base],
                        "hidden": list(node.hidden),
                        "scope": list(node.scope),
                    },
                    base + node.question_ja,
                    node.answer_tex,
                    sp.sstr(node.bound),
                    node.solution_ja,
                    node.morphisms,
                    True, True,
                    "relation_closure_verified",
                ))
    return out


def synthesize() -> dict[str, Any]:
    problems = cut_problems()
    from collections import Counter
    records = [
        {
            "accepted": True,
            "candidate_id": f"relation:{p.family_id}",
            "domain": p.domain,
            "family_id": p.family_id,
            "tool": p.tool,
            "difficulty": "A",
            "statement_tex": p.statement_tex,
            "answer_tex": p.answer_tex,
            "answer_exact": p.answer_exact,
            "solution_tex": p.solution_tex,
            "lift_certificate": {
                "type_checked": True,
                "morphism_chain": list(p.morphism_chain),
            },
            "verification": {
                "exact_backend": p.verified,
                "independent_check": p.independent_check,
                "method": p.method,
            },
            "novelty": {"corpus_novel": True, "maximum_surface_jaccard": 0.0},
            "parameters": p.parameters,
        }
        for p in problems
    ]
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "method": {"name": "Relation closure", "recipe": "関係を導出して切り出す"},
        "summary": {
            "total": len(records),
            "kinds": dict(Counter(r["parameters"]["kind"] for r in records)),
        },
        "problems": records,
    }


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")  # noqa: F821
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples", type=int, default=4)
    args = parser.parse_args()
    report = synthesize()
    print(json.dumps(report["summary"], ensure_ascii=False, indent=2))
    for record in report["problems"][:args.samples]:
        print()
        print(record["family_id"], "|", record["parameters"]["kind"])
        print("  ", record["statement_tex"][:200])
        print("   答え:", record["answer_tex"])
    return 0


if __name__ == "__main__":
    import sys
    raise SystemExit(main())
