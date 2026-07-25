"""深層族 (8層): 族を減らして深くする。東大・数オリ級を狙う。

各族は 8 個の射を連鎖し、途中で構造が何度も変わる。すべて高校数学の道具で
解けるが、到達するまでに何段も踏む必要がある。
"""

from __future__ import annotations

import itertools
import math
from typing import Any, Callable, Iterable

import sympy as sp

try:
    from math_os_prototype.construct_engine import Problem, _term
except ImportError:  # pragma: no cover
    from construct_engine import Problem, _term


def _deep_paley_spectrum(params: dict[str, Any]) -> Problem | None:
    """素数→平方剰余→Paleyグラフ→隣接行列→A^3→閉歩道→三角形→トレース(8層)。"""
    p = params["p"]
    if p % 4 != 1:
        return None
    QR = set((k * k) % p for k in range(1, p))
    triangles = p * (p - 1) * (p - 5) // 48
    brute = 0
    for x in range(p):
        for y in range(x + 1, p):
            if (y - x) % p not in QR:
                continue
            for z in range(y + 1, p):
                if (z - y) % p in QR and (z - x) % p in QR:
                    brute += 1
    if brute != triangles:
        return None
    answer = 6 * triangles
    return Problem(
        "deep.paley_spectrum_triangles",
        "number_theory_graph",
        "quadratic_residue+spectral+counting",
        params,
        rf"素数 \(p={p}\)（\(p\equiv1\pmod4\)）に対し，頂点集合 \(\mathbb Z_{{{p}}}\) 上の"
        r"グラフ \(G\) を，2頂点 \(x,y\) が \(x-y\) が平方剰余のとき辺で結ぶことで定める。"
        r"\(G\) の隣接行列を \(A\) とするとき，\(\operatorname{tr}(A^3)\) を求めよ。",
        str(answer),
        str(answer),
        rf"\(\operatorname{{tr}}(A^3)\) は長さ3の閉じた歩道の総数で，三角形1個が6回"
        rf"数えられる。この \(G\) では各辺の共通隣接点が \((p-5)/4\) 個なので三角形は "
        rf"\(\frac{{p(p-1)(p-5)}}{{48}}={triangles}\) 個。よって "
        rf"\(\operatorname{{tr}}(A^3)=6\times{triangles}={answer}\)。",
        (
            "PrimeField", "QuadraticResidueSet", "PaleyGraph", "AdjacencyMatrix",
            "MatrixCube", "ClosedWalkCount", "TriangleCount", "TraceInvariant",
        ),
        True,
        True,
        "adjacency_trace_vs_exhaustive_triangle_count",
    )


def _grid_deep_paley() -> Iterable[dict[str, Any]]:
    for p in (13, 17, 29, 37, 41, 53, 61, 73, 89, 97):
        yield {"p": p}


def _deep_tangent_growth(params: dict[str, Any]) -> Problem | None:
    """三次曲線→接線→再交点→反復→一般項→増大度→対数→極限(8層)。"""
    coeff = params["coeff"]
    x, t, n = sp.symbols("x t n", real=True)
    f = x**3 + coeff * x
    slope = sp.diff(f, x).subs(x, t)
    others = [
        sp.simplify(s)
        for s in sp.solve(sp.Eq(f, (t**3 + coeff * t) + slope * (x - t)), x)
        if sp.simplify(s - t) != 0
    ]
    if not others or sp.simplify(others[0] - (-2 * t)) != 0:
        return None
    limit = sp.log(2)
    return Problem(
        "deep.tangent_iteration_growth",
        "geometry_analysis",
        "symbolic_intersection+iteration+limit",
        params,
        rf"曲線 \(C: y={sp.latex(f)}\) 上に点 "
        rf"\(P_0(t,\,{sp.latex(t**3 + coeff * t)})\)（\(t>0\)）をとる。"
        r"\(P_i\) における \(C\) の接線が \(C\) と再び交わる点を \(P_{i+1}\) と定め，"
        r"\(P_n\) の \(x\) 座標を \(x_n\) とする。"
        r"極限 \(\displaystyle\lim_{n\to\infty}\frac{\log|x_n|}{n}\) を求めよ。",
        sp.latex(limit),
        sp.sstr(limit),
        r"接点で重根をもつことと三次方程式の根の和の関係から \(x_{i+1}=-2x_i\)。"
        r"したがって \(x_n=(-2)^n t\)，\(|x_n|=2^n|t|\)。"
        r"\(\frac{\log|x_n|}{n}=\log 2+\frac{\log|t|}{n}\to\log 2\)。",
        (
            "CubicCurve", "TangentLine", "Reintersection", "RootSumRelation",
            "GeometricIteration", "GeneralTerm", "GrowthRate", "LogarithmicLimit",
        ),
        True,
        True,
        "tangent_iteration_ratio_then_log_limit",
    )


def _grid_deep_tangent() -> Iterable[dict[str, Any]]:
    for coeff in (-9, -7, -5, -3, -1, 0, 1, 2, 3, 5):
        yield {"coeff": coeff}


def _deep_rotation_divisors(params: dict[str, Any]) -> Problem | None:
    """1の冪根→正n角形→頂点間距離→全積(=n)→約数個数(8層)。"""
    n_val = params["n"]
    if n_val < 3:
        return None
    prod = 1.0
    for j in range(1, n_val):
        d = abs(
            complex(1, 0)
            - complex(math.cos(2 * math.pi * j / n_val), math.sin(2 * math.pi * j / n_val))
        )
        prod *= d
    if abs(prod - n_val) > 1e-6:
        return None
    answer = sp.divisor_count(n_val)
    return Problem(
        "deep.rotation_diagonal_product_divisors",
        "complex_geometry",
        "roots_of_unity+product+divisor_function",
        params,
        rf"単位円に内接する正 \({n_val}\) 角形の頂点を "
        rf"\(z_j=\cos\frac{{2\pi j}}{{{n_val}}}+i\sin\frac{{2\pi j}}{{{n_val}}}"
        rf"\ (j=0,1,\ldots,{n_val - 1})\) とする。頂点 \(z_0\) から他の "
        rf"\({n_val - 1}\) 個の頂点までの距離の積を \(L\) とするとき，"
        r"\(L\) の正の約数の個数を求めよ。",
        str(answer),
        str(answer),
        rf"\(z^{{{n_val}}}-1=\prod_{{j=0}}^{{{n_val - 1}}}(z-z_j)\) の両辺を \(z-1\) で"
        rf"割り \(z\to1\) とすると \(\prod_{{j=1}}^{{{n_val - 1}}}(1-z_j)={n_val}\)。"
        rf"絶対値をとって \(L={n_val}\)。よって約数の個数は \({answer}\)。",
        (
            "RootOfUnity", "RegularPolygon", "VertexDistances", "PolynomialFactorization",
            "LimitEvaluation", "DistanceProduct", "IntegerValue", "DivisorCount",
        ),
        True,
        True,
        "cyclotomic_product_identity_plus_numeric_check",
    )


def _grid_deep_rotation() -> Iterable[dict[str, Any]]:
    for n in range(3, 40):
        yield {"n": n}


def _deep_recurrence_qr(params: dict[str, Any]) -> Problem | None:
    """漸化式→随伴行列→mod p の位数→周期→素因数→オイラーの規準→ルジャンドル記号(8層)。"""
    s, t, p = params["s"], params["t"], params["p"]
    if not sp.isprime(p):
        return None
    a, b, period = 0, 1, None
    for i in range(1, p * p * 6 + 1):
        a, b = b % p, (s * b + t * a) % p
        if a == 0 and b == 1:
            period = i
            break
    if not period or period < 2:
        return None
    q = max(sp.primefactors(period))
    if q % p == 0:
        return None
    answer = 1 if pow(q % p, (p - 1) // 2, p) == 1 else -1
    rhs = (_term(s, "a_{n+1}") + _term(t, "a_n")).lstrip("+")
    return Problem(
        "deep.recurrence_period_quadratic_character",
        "number_theory",
        "matrix_mod_order+legendre_symbol",
        params,
        rf"数列 \((a_n)\) を \(a_0=0,\ a_1=1,\ a_{{n+2}}={rhs}\) で定める。"
        rf"\((a_n)\) を \(\bmod\ {p}\) で見たときの最小周期を \(T\) とし，"
        rf"\(T\) の最大の素因数を \(q\) とする。ルジャンドル記号 "
        rf"\(\left(\dfrac{{q}}{{{p}}}\right)\) の値を求めよ。",
        str(answer),
        str(answer),
        rf"\((a_{{n+1}},a_n)\) は随伴行列 "
        rf"\(\begin{{pmatrix}}{s}&{t}\\1&0\end{{pmatrix}}\) を掛けて進むので，"
        rf"\(\bmod\ {p}\) でのこの行列の位数が周期 \(T={period}\)。"
        rf"その最大素因数は \(q={q}\)。オイラーの規準 "
        rf"\(q^{{({p}-1)/2}}\equiv{answer}\pmod{{{p}}}\) より "
        rf"\(\left(\frac{{{q}}}{{{p}}}\right)={answer}\)。",
        (
            "LinearRecurrence", "CompanionMatrix", "ModularReduction",
            "MultiplicativeOrder", "MinimalPeriod", "PrimeFactorization",
            "EulerCriterion", "LegendreSymbol",
        ),
        True,
        True,
        "modular_period_then_euler_criterion",
    )


def _grid_deep_recurrence() -> Iterable[dict[str, Any]]:
    for s, t in ((1, 1), (1, 2), (2, 1), (3, -1), (1, 3)):
        for p in (7, 11, 13, 17, 19, 23, 29, 31):
            yield {"s": s, "t": t, "p": p}


def _deep_centroid_subsets(params: dict[str, Any]) -> Problem | None:
    """正n角形→部分集合→重心→中心一致→巡回対称→個数(8層)。"""
    n_val = params["n"]
    if n_val < 3 or n_val > 12:
        return None
    count = 0
    for r in range(1, n_val + 1):
        for subset in itertools.combinations(range(n_val), r):
            zr = sum(math.cos(2 * math.pi * j / n_val) for j in subset)
            zi = sum(math.sin(2 * math.pi * j / n_val) for j in subset)
            if abs(zr) < 1e-9 and abs(zi) < 1e-9:
                count += 1
    if count == 0:
        return None
    return Problem(
        "deep.polygon_subset_centroid",
        "complex_geometry",
        "roots_of_unity+subset_enumeration",
        params,
        rf"単位円に内接する正 \({n_val}\) 角形の頂点を "
        rf"\(z_j=\cos\frac{{2\pi j}}{{{n_val}}}+i\sin\frac{{2\pi j}}{{{n_val}}}"
        rf"\ (j=0,1,\ldots,{n_val - 1})\) とする。空でない部分集合 \(S\) であって，"
        r"\(S\) に属する頂点の重心が円の中心と一致するものの個数を求めよ。",
        str(count),
        str(count),
        rf"重心が中心であることは \(\sum_{{j\in S}}z_j=0\) と同値。\(z_j\) は1の "
        rf"\({n_val}\) 乗根なので，和が消える部分集合を数えればよい。"
        r"巡回対称性から，正多角形をなす頂点集合とその合併が条件を満たす。",
        (
            "RootOfUnity", "RegularPolygon", "SubsetFamily", "CentroidMap",
            "VanishingSum", "CyclotomicRelation", "SymmetryReduction", "SubsetCount",
        ),
        True,
        True,
        "exhaustive_subset_vanishing_sum_count",
    )


def _grid_deep_centroid() -> Iterable[dict[str, Any]]:
    for n in range(3, 13):
        yield {"n": n}


DEEP_FAMILIES: tuple[
    tuple[Callable[[dict[str, Any]], "Problem | None"], Callable[[], Iterable[dict[str, Any]]]], ...
] = (
    (_deep_paley_spectrum, _grid_deep_paley),
    (_deep_tangent_growth, _grid_deep_tangent),
    (_deep_rotation_divisors, _grid_deep_rotation),
    (_deep_recurrence_qr, _grid_deep_recurrence),
    (_deep_centroid_subsets, _grid_deep_centroid),
)
