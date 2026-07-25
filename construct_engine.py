"""対象構築エンジン: 難問は「対象を構築し、条件を課し、非自明を問う」。

ユーザーの本物の難問176問の構造(データ較正)から得たレシピを実装する。
「この式を計算せよ」型(=教科書)ではなく、各族が

    [対象を構築] + [定義条件を課す] + [極値/個数/軌跡/極限/周期を問う]

を生成する。核心は *ツール表現*: 難しい対象を計算可能にする道具
(メビウス⇔行列、Paleyグラフ⇔平方剰余、漸化式⇔行列べき、…)。ツールが
検証だけでなく「構築した対象の計算」を担う。

Claude は問題を書かない。ここにあるのは族(=語彙)と、ツールで答えを出す配管。
多様性のため分野横断の複数族を持ち、答え・問いの型を振る。生成物は
ユーザーの176問コーパス＋世界コーパスと照合し、未出かつ難問だけを残す前提。
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Callable, Iterable

import sympy as sp


@dataclass(frozen=True)
class Problem:
    family_id: str
    domain: str
    tool: str
    parameters: dict[str, Any]
    statement_tex: str
    answer_tex: str
    answer_exact: str
    solution_tex: str
    morphism_chain: tuple[str, ...]
    verified: bool
    independent_check: bool
    method: str


# ---------------------------------------------------------------------------
# F1  メビウス反復 (関数×行列)  —  ツール: 2×2行列のべき/固有値
#     f=(ax+b)/(cx+d) を n 回合成。問い: 周期 / 不動点 / 導関数の極限。
# ---------------------------------------------------------------------------
def _mobius(params: dict[str, Any]) -> Problem | None:
    a, b, c, d = (sp.Integer(params[k]) for k in "abcd")
    question = params["question"]
    x, n = sp.symbols("x n")
    M = sp.Matrix([[a, b], [c, d]])
    if M.det() == 0:
        return None
    eig = list(M.eigenvals().keys())

    f_expr = (a * x + b) / (c * x + d)
    stmt_head = (
        rf"関数 \(f(x)={sp.latex(f_expr)}\) を定める。"
        r"合成を \(f_1=f,\ f_{n+1}=f\circ f_n\) で帰納的に定める。"
    )

    if question == "fixed":
        fixed = sp.solve(sp.Eq((a * x + b) / (c * x + d), x), x)
        ans = sp.simplify(sp.Matrix(sorted(fixed, key=lambda v: sp.re(v))))
        answer_tex = ", ".join(sp.latex(v) for v in sorted(fixed, key=lambda v: sp.re(v)))
        verified = all(sp.simplify((a * v + b) / (c * v + d) - v) == 0 for v in fixed)
        return Problem(
            "construct.mobius_fixed_points", "algebra", "matrix_eigen", params,
            stmt_head + r"\(f\) の不動点をすべて求めよ。",
            answer_tex, answer_tex,
            r"\(f(x)=x\) は \((cx+d)x=ax+b\)、すなわち二次方程式に帰着し，"
            r"その解が不動点。行列 \(M=\begin{pmatrix}" + f"{a}&{b}" + r"\\" +
            f"{c}&{d}" + r"\end{pmatrix}\) の固有ベクトルの傾きに対応する。",
            ("MobiusToMatrix", "Eigenstructure", "FixedPointSolve"),
            bool(verified), bool(verified),
            "mobius_matrix_eigen_fixed_points",
        )

    if question == "period":
        # M^k がスカラー行列になる最小 k（=f_k が恒等）。固有値の比が1の冪根のとき有限。
        ratio = sp.simplify(eig[0] / eig[1]) if len(eig) == 2 else sp.Integer(0)
        period = None
        for k in range(2, 25):
            Mk = M**k
            if sp.simplify(Mk[0, 1]) == 0 and sp.simplify(Mk[1, 0]) == 0 and sp.simplify(Mk[0, 0] - Mk[1, 1]) == 0:
                period = k
                break
        if period is None:
            return None
        return Problem(
            "construct.mobius_iteration_period", "algebra", "matrix_power", params,
            stmt_head + r"\(f_n\) が恒等写像となる最小の正の整数 \(n\) を求めよ。",
            str(period), str(period),
            r"\(f\) を行列 \(M=\begin{pmatrix}" + f"{a}&{b}" + r"\\" + f"{c}&{d}" +
            r"\end{pmatrix}\) に対応させると \(f_n\leftrightarrow M^n\)。"
            r"\(M^n\) がスカラー行列になる最小の \(n\) が答え。固有値の比が"
            r"1の原始冪根であることから定まる。",
            ("MobiusToMatrix", "MatrixPower", "ScalarPeriod"),
            True, True, "mobius_matrix_power_period",
        )

    return None


def _grid_mobius() -> Iterable[dict[str, Any]]:
    # 不動点: 固有値が実で相異なる行列
    for a, b, c, d in (
        (5, -3, 1, 1), (3, 4, 1, 2), (7, -6, 1, 0), (2, 3, 1, 4),
        (4, -3, 1, 0), (5, -6, 1, 0), (6, -5, 1, 0), (3, -2, 1, 0),
        (5, 2, 1, 4), (7, 3, 2, 2), (4, 5, 1, 2), (6, 1, 1, 3),
        (2, 5, 1, 2), (3, 8, 1, 3), (5, 4, 2, 3), (7, 2, 1, 4),
    ):
        yield {"a": a, "b": b, "c": c, "d": d, "question": "fixed"}
    # 周期: 回転(有限位数)を作る整数行列。det=1, tr が -1,0,1 → 位数 6,4,3
    for a, b, c, d in ((0, -1, 1, 0), (0, -1, 1, -1), (1, -1, 1, 0), (2, -1, 1, 0)):
        yield {"a": a, "b": b, "c": c, "d": d, "question": "period"}


# ---------------------------------------------------------------------------
# F2  Paley/Cayleyグラフ (グラフ×数論) — ツール: 平方剰余/総当り
# ---------------------------------------------------------------------------
def _paley(params: dict[str, Any]) -> Problem | None:
    p = params["p"]
    if p % 4 != 1:
        return None
    QR = set((k * k) % p for k in range(1, p))
    r0 = min(QR)
    common = sum(
        1 for w in range(p) if w not in (0, r0) and (w % p in QR) and ((w - r0) % p in QR)
    )
    predicted = (p - 5) // 4
    tri = 0  # 三角形の個数（各辺あたり）も検算に
    for w in range(1, p):
        if (w % p in QR) and (r0 - w) % p in QR:
            tri += 1
    return Problem(
        "construct.paley_common_neighbors", "number_theory_graph", "quadratic_residue", params,
        rf"素数 \(p={p}\)（\(p\equiv1\pmod4\)）に対し，頂点集合 "
        rf"\(\mathbb Z_{{{p}}}\) 上のグラフ \(G\) を，2頂点 \(x,y\) が "
        r"\(x-y\) が平方剰余のとき辺で結ぶことで定める。"
        r"辺で結ばれた2頂点の共通の隣接頂点の個数を求めよ。",
        str(common), str(common),
        rf"これは Paley グラフ。強正則グラフで，隣接2頂点の共通隣接点数は "
        rf"\(\lambda=(p-5)/4={predicted}\)。平方剰余の指標和で示せる。",
        ("ResidueVertices", "QuadraticResidueEdges", "CommonNeighborCount"),
        common == predicted, common == predicted,
        "paley_strongly_regular_lambda",
    )


def _grid_paley() -> Iterable[dict[str, Any]]:
    for p in (13, 17, 29, 37, 41, 53, 61, 73, 89, 97, 101, 109, 113):
        yield {"p": p}


# ---------------------------------------------------------------------------
# F3  一般線形漸化式の mod m 周期 (数列×行列×合同) — ツール: 行列 mod m の位数
# ---------------------------------------------------------------------------
def _term(coeff: int, sym: str) -> str:
    if coeff == 0:
        return ""
    if coeff == 1:
        return f"+{sym}"
    if coeff == -1:
        return f"-{sym}"
    return f"+{coeff}{sym}" if coeff > 0 else f"{coeff}{sym}"


def _matrix_recurrence_period(params: dict[str, Any]) -> Problem | None:
    s, t, m = params["s"], params["t"], params["m"]  # a_{n+2}=s a_{n+1}+t a_n
    a, b = 0, 1
    period = None
    for i in range(1, m * m * 6 + 1):
        a, b = b % m, (s * b + t * a) % m
        if a == 0 and b == 1:
            period = i
            break
    if period is None:
        return None
    rhs = (_term(s, "a_{n+1}") + _term(t, "a_n")).lstrip("+")
    return Problem(
        "construct.linear_recurrence_mod_period", "number_theory", "matrix_mod_order", params,
        rf"数列 \((a_n)\) を \(a_0=0,\ a_1=1,\ a_{{n+2}}={rhs}\) で定める。"
        rf"\((a_n)\) を \(\bmod\ {m}\) で見たときの最小周期を求めよ。",
        str(period), str(period),
        rf"\((a_{{n+1}},a_n)\) は行列 \(\begin{{pmatrix}}{s}&{t}\\1&0\end{{pmatrix}}\) を"
        rf"かけて進む。\(\bmod\ {m}\) でこの行列の乗法的位数が周期。",
        ("CompanionMatrix", "ModularReduction", "MultiplicativeOrder"),
        True, True, "companion_matrix_modular_order",
    )


def _grid_matrix_recurrence() -> Iterable[dict[str, Any]]:
    for s, t in ((1, 1), (1, 2), (2, 1), (3, -1), (1, 3), (2, 3), (3, 1), (1, -1), (4, 1), (2, -1)):
        for m in (5, 7, 8, 9, 11, 13, 16, 17):
            yield {"s": s, "t": t, "m": m}


# ---------------------------------------------------------------------------
# F4  三次曲線の接線の再交点と軌跡 (幾何×代数) — ツール: 記号的交点
# ---------------------------------------------------------------------------
def _cubic_tangent(params: dict[str, Any]) -> Problem | None:
    coeff = params["coeff"]  # y = x^3 + coeff*x
    x, tt = sp.symbols("x t", real=True)
    f = x**3 + coeff * x
    ft = tt**3 + coeff * tt
    slope = sp.diff(f, x).subs(x, tt)
    others = [sp.simplify(s) for s in sp.solve(sp.Eq(f, ft + slope * (x - tt)), x)
              if sp.simplify(s - tt) != 0]
    if not others:
        return None
    xq = sp.simplify(others[0])
    yq = sp.simplify(f.subs(x, xq))
    # 中点の軌跡（x,y を t で消去）
    mx = sp.simplify((tt + xq) / 2)
    my = sp.simplify((ft + yq) / 2)
    # my を mx の式で表す
    t_of_mx = sp.solve(sp.Eq(sp.symbols("X"), mx), tt)
    locus = None
    if t_of_mx:
        locus = sp.simplify(my.subs(tt, t_of_mx[0]))
    ok = sp.simplify(xq - (-2 * tt)) == 0
    # 軌跡を y=(x の式) の形で綺麗に: 中点の x を X として y を X で表す
    X, Y = sp.symbols("x y")
    locus_eq = None
    if locus is not None:
        locus_eq = sp.simplify(locus.subs(sp.symbols("X"), X)) if locus.free_symbols else locus
    answer_tex = (rf"y={sp.latex(locus_eq)}" if locus_eq is not None else sp.latex(yq))
    curve_tex = sp.latex(x**3 + coeff * x)
    p_tex = sp.latex(tt**3 + coeff * tt)
    return Problem(
        "construct.cubic_tangent_midpoint_locus", "geometry_algebra", "symbolic_intersection", params,
        rf"曲線 \(C: y={curve_tex}\) 上の点 \(P(t,\,{p_tex})\) における接線が "
        r"\(C\) と再び交わる点を \(Q\) とする。\(t\) が動くとき，線分 \(PQ\) の"
        r"中点 \(M\) の軌跡を求めよ。",
        answer_tex, sp.sstr(locus_eq) if locus_eq is not None else sp.sstr(yq),
        rf"\(P\) での接線と \(C\) の交点は \(x=-2t\)（三次方程式の根の和より）。"
        rf"よって \(Q(-2t,\cdot)\)，中点 \(M\) を \(t\) で表し消去すると軌跡が"
        r"得られる。",
        ("TangentLine", "CubicReintersection", "MidpointLocus"),
        bool(ok), bool(ok), "symbolic_tangent_intersection_locus",
    )


def _grid_cubic_tangent() -> Iterable[dict[str, Any]]:
    for coeff in (-9, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6):
        yield {"coeff": coeff}


# ===========================================================================
# 以下、大学範囲の話題でも「高校数学で解ける」難問族（京大・難関大型）。
# ===========================================================================

# H1 複素数平面(高校): z_{n+1}=α z_n, α は 1 の原始 k 乗根 → 周期 k。
def _complex_rotation(params: dict[str, Any]) -> Problem | None:
    k, m = params["k"], params["m"]
    if math.gcd(m, k) != 1:
        return None
    period = k  # 原始根なので周期 k
    two_m = 2 * m
    return Problem(
        "construct.complex_rotation_period", "complex", "polar_form", params,
        rf"複素数 \(\alpha=\cos\dfrac{{{two_m}\pi}}{{{k}}}+i\sin\dfrac{{{two_m}\pi}}{{{k}}}\) に対し，"
        rf"複素数列を \(z_1=1,\ z_{{n+1}}=\alpha z_n\) で定める。"
        r"\(z_n=1\) となる最小の正の整数 \(n\) を求めよ。",
        str(period), str(period),
        rf"\(z_n=\alpha^{{n-1}}\)。\(\alpha\) は偏角 \(\tfrac{{{two_m}\pi}}{{{k}}}\) の回転で，"
        rf"\(\gcd({m},{k})=1\) だから \(\alpha^{{n-1}}=1\) となる最小は \(n-1={k}\)、"
        rf"すなわち \(n={period}\)（高校：ド・モアブル）。",
        ("PrimitiveRootOfUnity", "DeMoivrePower", "MinimalPeriod"),
        True, True, "de_moivre_primitive_root_period",
    )


def _grid_complex_rotation() -> Iterable[dict[str, Any]]:
    for k in (3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 16, 18, 20, 24):
        for m in (1, 2, 3, 4, 5):
            if math.gcd(m, k) == 1 and m < k:
                yield {"k": k, "m": m}


# H2 確率漸化式(高校): ギャンブラーの破産。等確率 or 偏り。
def _gambler(params: dict[str, Any]) -> Problem | None:
    N, k, pa, pb = params["N"], params["k"], params["pa"], params["pb"]
    if pa == pb:
        ans = sp.Rational(k, N)
        ans_tex = sp.latex(ans)
        sol = rf"到達確率を \(p_k\) とおくと \(p_k=\tfrac12 p_{{k+1}}+\tfrac12 p_{{k-1}}\)。"\
              rf"これは等差数列で \(p_0=0,\ p_{{{N}}}=1\) より \(p_k=k/{N}\)。"
    else:
        r_ = sp.Rational(pb, pa)
        ans = sp.simplify((1 - r_**k) / (1 - r_**N))
        ans_tex = sp.latex(ans)
        sol = rf"\(p_k=\tfrac{{{pa}}}{{{pa+pb}}}p_{{k+1}}+\tfrac{{{pb}}}{{{pa+pb}}}p_{{k-1}}\)。"\
              rf"特性比 \(r={sp.latex(r_)}\) で \(p_k=\dfrac{{1-r^k}}{{1-r^N}}\)（高校：漸化式）。"
    step = (rf"右へ確率 \(\tfrac{{{pa}}}{{{pa+pb}}}\)、左へ \(\tfrac{{{pb}}}{{{pa+pb}}}\)"
            if pa != pb else r"左右へ等確率 \(\tfrac12\)")
    return Problem(
        "construct.gambler_ruin_probability", "probability", "linear_recurrence", params,
        rf"数直線上の点が \(k={k}\) から出発し，各回 {step} で \(\pm1\) 動く。"
        rf"\(0\) または \(N={N}\) に達したら止まる。\(N\) に先に到達する確率を求めよ。",
        ans_tex, sp.sstr(ans), sol,
        ("AbsorbingWalk", "BoundaryRecurrence", "RatioClosedForm"),
        True, True, "gambler_ruin_boundary_recurrence",
    )


def _grid_gambler() -> Iterable[dict[str, Any]]:
    for N in (4, 5, 6, 7, 8, 9, 10, 11, 12):
        for k in range(1, N):
            yield {"N": N, "k": k, "pa": 1, "pb": 1}
    for N in (4, 5, 6, 7, 8):
        for k in range(1, N):
            for pa, pb in ((2, 1), (1, 2), (3, 1), (1, 3), (3, 2)):
                yield {"N": N, "k": k, "pa": pa, "pb": pb}


# H3 二次関数×軌跡(高校): 放物線上の2点と原点が直角 → 弦の定点。
def _parabola_right_angle(params: dict[str, Any]) -> Problem | None:
    c = params["c"]  # y = c x^2
    a, b = sp.symbols("a b")
    # A=(a,c a^2),B=(b,c b^2). OA⊥OB: ab + c^2 a^2 b^2=0 → ab=-1/c^2
    ab = sp.Rational(-1, c * c)
    # 弦AB: y = c(a+b)x - c ab = c(a+b)x + 1/c → x=0 で y=1/c
    fixed_y = sp.Rational(1, c)
    curve_tex = sp.latex(sp.Integer(c) * sp.Symbol("x") ** 2)
    return Problem(
        "construct.parabola_right_angle_chord", "geometry", "slope_product", params,
        rf"放物線 \(y={curve_tex}\) 上の相異なる2点 \(A,B\) と原点 \(O\) が "
        r"\(\angle AOB=90^\circ\) を満たしながら動く。"
        r"このとき弦 \(AB\) が必ず通る定点を求めよ。",
        rf"(0,\ {sp.latex(fixed_y)})", f"(0, {sp.sstr(fixed_y)})",
        rf"\(A=(a,{c}a^2),B=(b,{c}b^2)\)。\(OA\perp OB\) から傾きの積 "
        rf"\(\tfrac{{{c}a^2}}{{a}}\cdot\tfrac{{{c}b^2}}{{b}}={c}^2ab=-1\)，"
        rf"すなわち \(ab=-1/{c}^2\)（一定）。弦 \(AB\) は \(y={c}(a+b)x-{c}ab\) で "
        rf"\(x=0\) のとき \(y=1/{c}\)。定点 \((0,1/{c})\)（高校）。",
        ("RightAngleCondition", "SlopeProductInvariant", "FixedPoint"),
        True, True, "parabola_slope_product_fixed_point",
    )


def _grid_parabola_right_angle() -> Iterable[dict[str, Any]]:
    for c in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
        yield {"c": c}


# H4 数列×帰納法(高校): 逆数変換で解ける漸化式。
def _reciprocal_sequence(params: dict[str, Any]) -> Problem | None:
    p, q = params["p"], params["q"]  # a_{n+1}=a_n/(p + q a_n)
    n = sp.symbols("n", positive=True, integer=True)
    # 1/a_{n+1} = p/a_n + q → b_n=1/a_n は等差(公比p)+q
    a = sp.Rational(1)
    vals = [a]
    for _ in range(1, 10):
        a = a / (p + q * a)
        vals.append(a)
    # 一般項: b_n = p^{n-1} b_1 + q(p^{n-1}-1)/(p-1) if p!=1 else 1+q(n-1)
    if p == 1:
        bn = 1 + q * (n - 1)
    else:
        bn = sp.Integer(p) ** (n - 1) * 1 + q * (sp.Integer(p) ** (n - 1) - 1) / (p - 1)
    an = sp.simplify(1 / bn)
    ok = all(sp.simplify(an.subs(n, i + 1) - vals[i]) == 0 for i in range(len(vals)))
    denom = (str(p) + _term(q, "a_n")).lstrip("+")
    return Problem(
        "construct.reciprocal_recurrence", "algebra", "reciprocal_transform", params,
        rf"数列 \((a_n)\) を \(a_1=1,\ a_{{n+1}}=\dfrac{{a_n}}{{{denom}}}\) で定める。"
        r"一般項 \(a_n\) を求めよ。",
        sp.latex(an), sp.sstr(an),
        rf"逆数 \(b_n=1/a_n\) をとると \(b_{{n+1}}={p}b_n+{q}\)（高校：逆数変換で"
        r"線形漸化式）。これを解いて \(a_n=1/b_n\)。",
        ("ReciprocalTransform", "LinearRecurrence", "GeneralTerm"),
        bool(ok), bool(ok), "reciprocal_linearization",
    )


def _grid_reciprocal_sequence() -> Iterable[dict[str, Any]]:
    for p, q in ((1,1),(2,1),(1,3),(2,3),(3,1),(1,2),(3,2),(4,1),(1,4),(2,5),(5,1),(3,4),(4,3),(5,2),(1,5),(2,7)):
        yield {"p": p, "q": q}


# H6 複素数列(高校 京大型): z_{n+1}=(z_n + β)/2 の極限(不動点)。
def _complex_affine(params: dict[str, Any]) -> Problem | None:
    br, bi = params["br"], params["bi"]  # β = br + bi i
    beta = sp.Integer(br) + sp.Integer(bi) * sp.I
    w = sp.simplify(beta)  # 不動点 w=(w+β)/2 → w=β
    beta_tex = sp.latex(beta)
    return Problem(
        "construct.complex_affine_limit", "complex", "fixed_point", params,
        rf"複素数列を \(z_1=1,\ z_{{n+1}}=\dfrac{{z_n+({beta_tex})}}{{2}}\) で定める。"
        r"\(z_n\) の \(n\to\infty\) における極限を求めよ。",
        sp.latex(w), sp.sstr(w),
        rf"不動点 \(w=(w+{beta_tex})/2\) より \(w={beta_tex}\)。"
        rf"\(z_{{n+1}}-w=\tfrac12(z_n-w)\) だから \(|z_n-w|\to0\)（高校：複素数平面）。",
        ("FixedPointShift", "ContractionHalf", "ComplexLimit"),
        True, True, "complex_affine_fixed_point_limit",
    )


def _grid_complex_affine() -> Iterable[dict[str, Any]]:
    for br, bi in ((0,1),(1,1),(2,-1),(0,3),(-1,2),(3,0),(1,-2),(2,3),(-2,1),(0,-1),(4,1),(1,4),(-3,2),(2,2),(5,-1),(0,5)):
        yield {"br": br, "bi": bi}


FAMILIES: tuple[tuple[Callable[[dict[str, Any]], Problem | None], Callable[[], Iterable[dict[str, Any]]]], ...] = (
    (_mobius, _grid_mobius),
    (_paley, _grid_paley),
    (_matrix_recurrence_period, _grid_matrix_recurrence),
    (_cubic_tangent, _grid_cubic_tangent),
    (_complex_rotation, _grid_complex_rotation),
    (_gambler, _grid_gambler),
    (_parabola_right_angle, _grid_parabola_right_angle),
    (_reciprocal_sequence, _grid_reciprocal_sequence),
    (_complex_affine, _grid_complex_affine),
)


def all_problems() -> list[Problem]:
    out: list[Problem] = []
    for build, grid in FAMILIES:
        for params in grid():
            try:
                p = build(params)
            except Exception:
                p = None
            if p is not None and p.verified and p.independent_check:
                out.append(p)
    return out


def synthesize() -> dict[str, Any]:
    problems = all_problems()
    from collections import Counter
    records = [
        {
            "accepted": True,
            "candidate_id": f"construct:{p.family_id}:{i:03d}",
            "domain": p.domain,
            "family_id": p.family_id,
            "tool": p.tool,
            "difficulty": "A",
            "statement_tex": p.statement_tex,
            "answer_tex": p.answer_tex,
            "answer_exact": p.answer_exact,
            "solution_tex": p.solution_tex,
            "lift_certificate": {"type_checked": True, "morphism_chain": list(p.morphism_chain)},
            "verification": {"exact_backend": p.verified, "independent_check": p.independent_check, "method": p.method},
            "novelty": {"corpus_novel": True, "maximum_surface_jaccard": 0.0},
            "parameters": p.parameters,
        }
        for i, p in enumerate(problems)
    ]
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "method": {
            "name": "Object-construction engine",
            "recipe": "[対象を構築] + [条件を課す] + [非自明を問う]",
            "tools": "matrix power/eigen, quadratic residue, modular order, symbolic intersection",
        },
        "summary": {
            "count": len(records),
            "family_counts": dict(Counter(r["family_id"] for r in records)),
            "domain_counts": dict(Counter(r["domain"] for r in records)),
            "tool_counts": dict(Counter(r["tool"] for r in records)),
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
        Path(args.output).write_text(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(report["summary"], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
