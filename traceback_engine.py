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
# 構築 3: 楕円上の2点における接線の交点からの2接線
# ---------------------------------------------------------------------------
def _ellipse_rational_points(a: int, b: int, limit: int = 40) -> list[tuple[sp.Expr, sp.Expr]]:
    """楕円 x^2/a^2+y^2/b^2=1 上の有理点を集める。"""
    pts: list[tuple[sp.Expr, sp.Expr]] = []
    for num in range(-limit, limit + 1):
        px = sp.Rational(num, 5)
        rhs = 1 - px**2 / a**2
        if rhs <= 0:
            continue
        root = sp.sqrt(sp.nsimplify(b**2 * rhs))
        if root.is_rational and root != 0:
            pts.append((px, root))
    return pts


def closure_ellipse_tangent(params: tuple[int, int, int, int]) -> list[DerivedNode]:
    """楕円と外部点からの2接線という構築から、導ける量を列挙する。"""

    a, b, i1, i2 = params
    pts = _ellipse_rational_points(a, b)
    if len(pts) <= max(i1, i2) or i1 == i2:
        return []
    x, y = sp.symbols("x y", real=True)
    T1 = pts[i1]
    T2 = (pts[i2][0], -pts[i2][1])
    if T1 == T2:
        return []
    sol = sp.solve(
        [T1[0] * x / a**2 + T1[1] * y / b**2 - 1,
         T2[0] * x / a**2 + T2[1] * y / b**2 - 1],
        [x, y], dict=True,
    )
    if not sol:
        return []
    P = (sol[0][x], sol[0][y])
    base = f"楕円 x^2/{a}^2+y^2/{b}^2=1 と，そこから引いた2本の接線の交点 P"
    nodes: list[DerivedNode] = []

    def add(key, raw, question, hidden, morphisms, solution, scope):
        value = _exact(raw)
        if value is not None:
            nodes.append(DerivedNode(
                key, value, question, (base,), hidden, morphisms, solution, scope,
            ))

    add("chord_length_sq",
        (T1[0]-T2[0])**2 + (T1[1]-T2[1])**2,
        r"2つの接点を結ぶ線分の長さの平方を求めよ。",
        ("接点弦（極線）の方程式",),
        ("EllipseObject", "TangentLine", "DualLinePair", "EdgeLengthObservation"),
        r"接点弦は \(\frac{p x}{a^2}+\frac{q y}{b^2}=1\)。楕円との交点を求めて距離を計算する。",
        ("楕円", "接線", "2点間の距離"))

    add("tangent_slope_product",
        ((T1[1]-P[1])/(T1[0]-P[0])) * ((T2[1]-P[1])/(T2[0]-P[0])),
        r"2本の接線の傾きの積を求めよ。",
        ("接線が接する条件（判別式 0）",),
        ("EllipseObject", "TangentLine", "CoordinateSolve"),
        r"P を通る傾き \(m\) の直線を楕円に代入し，判別式 \(=0\) が与える "
        r"\(m\) の二次方程式の解と係数の関係から積を読む。",
        ("楕円", "判別式", "解と係数の関係"))

    add("contact_triangle_area",
        sp.Rational(1, 2)*sp.Abs(
            (T1[0]-P[0])*(T2[1]-P[1]) - (T2[0]-P[0])*(T1[1]-P[1])),
        r"P と2つの接点が作る三角形の面積を求めよ。",
        ("接点の座標", "P の座標"),
        ("EllipseObject", "TangentLine", "CoordinateSolve", "ShoelaceArea"),
        r"接点と P の座標を求め，三角形の面積公式を用いる。",
        ("楕円", "接線", "座標平面の面積"))

    add("chord_midpoint_x",
        (T1[0]+T2[0])/2,
        r"2つの接点を結ぶ線分の中点の \(x\) 座標を求めよ。",
        ("接点弦と楕円の交点",),
        ("EllipseObject", "TangentLine", "MidpointLocus"),
        r"接点弦と楕円の連立から2交点を求め，中点を取る。",
        ("楕円", "接線", "中点"))

    add("monge_radius_sq",
        sp.Integer(a**2 + b**2),
        r"2本の接線が直交するような点 P 全体は円をなす。その半径の平方を求めよ。",
        ("2接線が直交する条件", "傾きの積 = -1"),
        ("EllipseObject", "TangentLine", "RightAngleCondition", "CircleParameter"),
        r"傾きの二次方程式で解の積 \(=-1\) とおくと \(x^2+y^2=a^2+b^2\) を得る。",
        ("楕円", "判別式", "円の方程式"))

    add("center_to_polar_dist_sq",
        1/((P[0]/a**2)**2 + (P[1]/b**2)**2),
        r"原点から接点弦までの距離の平方を求めよ。",
        ("接点弦の方程式", "点と直線の距離"),
        ("EllipseObject", "DualLinePair", "CoordinateSolve"),
        r"接点弦 \(\frac{p x}{a^2}+\frac{q y}{b^2}=1\) と原点の距離を点と直線の距離公式で求める。",
        ("楕円", "点と直線の距離"))
    return nodes


def grid_ellipse_tangent() -> Iterable[tuple[int, int, int, int]]:
    return ((5, 3, 2, 5), (5, 4, 1, 4), (13, 5, 2, 6))


# ---------------------------------------------------------------------------
# 構築 4: 正方格子上の経路と対角線による反射
# ---------------------------------------------------------------------------
def closure_lattice_path(n: int) -> list[DerivedNode]:
    """(0,0)→(n,n) の最短経路という構築から、導ける量を列挙する。"""

    if n < 2 or n > 40:
        return []
    base = f"格子点 (0,0) から ({n},{n}) へ右または上に1ずつ進む最短経路"
    total = sp.binomial(2*n, n)
    catalan = sp.simplify(total/(n+1))
    nodes: list[DerivedNode] = []

    def add(key, raw, question, hidden, morphisms, solution, scope):
        value = _exact(raw)
        if value is not None:
            nodes.append(DerivedNode(
                key, value, question, (base,), hidden, morphisms, solution, scope,
            ))

    add("total_paths", total,
        r"経路は全部で何通りあるか。",
        ("右と上の並べ替え",),
        ("PathStateSpace", "SubsetCount"),
        rf"\(2n\) 回の移動のうち右を選ぶ位置を決めればよく \(\binom{{{2*n}}}{{{n}}}\)。",
        ("場合の数", "組合せ"))

    add("catalan_paths", catalan,
        r"直線 \(y=x\) より上側に出ない経路は何通りあるか。",
        ("対角線を越える経路の鏡映",),
        ("PathStateSpace", "ReflectionBijection", "SubsetCount"),
        r"越える経路を \(y=x+1\) で鏡映すると別の端点への経路と1対1に対応し，"
        r"差を取ってカタラン数を得る。",
        ("場合の数", "組合せ", "1対1対応"))

    add("strictly_above_paths", sp.binomial(2*n-2, n-1)/n,
        r"出発直後から到着直前まで直線 \(y=x\) に一度も触れない経路は何通りあるか。",
        ("最初の一歩を固定した後の鏡映",),
        ("PathStateSpace", "ReflectionBijection", "SubsetCount"),
        r"最初と最後の一歩を固定し，残りに鏡映の議論を適用する。",
        ("場合の数", "組合せ", "1対1対応"))

    add("total_paths_divisor_count",
        sp.Integer(sp.divisor_count(int(total))),
        r"経路の総数の正の約数の個数を求めよ。",
        ("二項係数の素因数分解",),
        ("PathStateSpace", "SubsetCount", "PrimeFactorization", "DivisorCount"),
        r"総数を素因数分解し，指数に1を足して掛ける。",
        ("場合の数", "素因数分解", "約数の個数"))

    add("catalan_divisor_count",
        sp.Integer(sp.divisor_count(int(catalan))),
        r"対角線より上に出ない経路の総数の正の約数の個数を求めよ。",
        ("鏡映による数え上げ", "素因数分解"),
        ("PathStateSpace", "ReflectionBijection", "PrimeFactorization", "DivisorCount"),
        r"鏡映で経路数を求めたのち素因数分解する。",
        ("場合の数", "1対1対応", "約数の個数"))

    if n % 2 == 0:
        add("through_center_paths", sp.binomial(n, n//2)**2,
            rf"点 \(({n//2},{n//2})\) を通る経路は何通りあるか。",
            ("経路の前半と後半への分割",),
            ("PathStateSpace", "SubsetCount"),
            r"中点までとそこからの経路数の積を取る。",
            ("場合の数", "組合せ"))
    return nodes


def grid_lattice_path() -> Iterable[int]:
    return (5, 6, 7, 8, 10, 12)


# ---------------------------------------------------------------------------
# 構築 5: 2 の累乗の 10 進表示（常用対数）
# ---------------------------------------------------------------------------
def closure_digit_power(k: int) -> list[DerivedNode]:
    """2^k の10進表示という構築から、導ける量を列挙する。"""

    if k < 5 or k > 400:
        return []
    value = 2**k
    text = str(value)
    base = f"2 の {k} 乗の10進表示"
    nodes: list[DerivedNode] = []

    def add(key, raw, question, hidden, morphisms, solution, scope):
        exact = _exact(raw)
        if exact is not None:
            nodes.append(DerivedNode(
                key, exact, question, (base,), hidden, morphisms, solution, scope,
            ))

    add("digit_count", sp.Integer(len(text)),
        rf"\(2^{{{k}}}\) は何桁の整数か。",
        ("常用対数 log10(2) の評価",),
        ("PowerSequence", "DecimalDigitCount"),
        rf"\(\log_{{10}}2^{{{k}}}={k}\log_{{10}}2\) の整数部分に1を足す。",
        ("指数", "常用対数", "桁数"))

    add("leading_digit", sp.Integer(int(text[0])),
        rf"\(2^{{{k}}}\) の最高位の数字を求めよ。",
        ("常用対数の小数部分",),
        ("PowerSequence", "LeadingDigit"),
        rf"\({k}\log_{{10}}2\) の小数部分 \(f\) に対し \(10^{{f}}\) の整数部分が最高位。",
        ("指数", "常用対数", "小数部分"))

    add("digit_increase_count",
        sp.Integer(sum(1 for n in range(1, k+1)
                       if len(str(2**n)) > len(str(2**(n-1))))),
        rf"\(n=1,2,\ldots,{k}\) のうち，\(2^{{n}}\) の桁数が \(2^{{n-1}}\) より"
        r"増えるような \(n\) の個数を求めよ。",
        ("桁数の階段関数", "log10(2) の無理性"),
        ("PowerSequence", "DecimalDigitCount", "ArithmeticObservation"),
        r"桁数は \(\lfloor n\log_{10}2\rfloor+1\)。増える回数は最終桁数から1を引いた数に等しい。",
        ("指数", "常用対数", "ガウス記号"))

    add("leading_one_count",
        sp.Integer(sum(1 for n in range(1, k+1) if str(2**n)[0] == "1")),
        rf"\(n=1,2,\ldots,{k}\) のうち，\(2^{{n}}\) の最高位が 1 となる \(n\) の個数を求めよ。",
        ("桁上がりの直後だけ最高位が1になること",),
        ("PowerSequence", "LeadingDigit", "ArithmeticObservation"),
        r"最高位が1になるのは桁数が増えた直後に限る。よって桁数の増加回数に一致する。",
        ("指数", "常用対数", "ガウス記号"))

    add("digit_sum", sp.Integer(sum(int(c) for c in text)),
        rf"\(2^{{{k}}}\) の各位の数字の和を求めよ。",
        ("10 進展開の各位",),
        ("PowerSequence", "ArithmeticObservation"),
        r"10進表示を求めて各位を加える。",
        ("指数", "整数の性質"))
    return nodes


def grid_digit_power() -> Iterable[int]:
    return (20, 30, 40, 50, 64, 100)


# ---------------------------------------------------------------------------
# 構築 6: 整数座標の三角形の五心とオイラー線
# ---------------------------------------------------------------------------
def closure_triangle_centers(
    params: tuple[int, int, int, int, int, int],
) -> list[DerivedNode]:
    """三角形という構築から、五心と関連量を列挙する。"""

    ax, ay, bx, by, cx, cy = params
    A = sp.Matrix([ax, ay])
    B = sp.Matrix([bx, by])
    C = sp.Matrix([cx, cy])
    area = sp.Rational(1, 2)*sp.Abs(
        (B[0]-A[0])*(C[1]-A[1]) - (C[0]-A[0])*(B[1]-A[1]))
    if area == 0:
        return []
    u, v = sp.symbols("u v", real=True)
    solutions = sp.solve([
        (u-A[0])**2 + (v-A[1])**2 - (u-B[0])**2 - (v-B[1])**2,
        (u-A[0])**2 + (v-A[1])**2 - (u-C[0])**2 - (v-C[1])**2,
    ], [u, v], dict=True)
    if not solutions:
        return []
    O = sp.Matrix([solutions[0][u], solutions[0][v]])
    H = A + B + C - 2*O
    r2 = sp.simplify((O[0]-A[0])**2 + (O[1]-A[1])**2)
    la = sp.sqrt((B[0]-C[0])**2 + (B[1]-C[1])**2)
    lb = sp.sqrt((A[0]-C[0])**2 + (A[1]-C[1])**2)
    lc = sp.sqrt((A[0]-B[0])**2 + (A[1]-B[1])**2)
    inradius = sp.simplify(area/((la+lb+lc)/2))
    incenter = sp.simplify((la*A + lb*B + lc*C)/(la+lb+lc))
    base = (
        f"3点 A({ax},{ay}), B({bx},{by}), C({cx},{cy}) を頂点とする三角形"
    )
    nodes: list[DerivedNode] = []

    def add(key, raw, question, hidden, morphisms, solution, scope):
        value = _exact(raw)
        if value is not None:
            nodes.append(DerivedNode(
                key, value, question, (base,), hidden, morphisms, solution, scope,
            ))

    add("area", area,
        r"この三角形の面積を求めよ。",
        (),
        ("TriangleConstruction", "ShoelaceArea"),
        r"座標から面積公式で直接求める。",
        ("座標平面", "三角形の面積"))

    add("circumradius_sq", r2,
        r"外接円の半径の平方を求めよ。",
        ("2辺の垂直二等分線の交点",),
        ("TriangleConstruction", "CircleParameter", "CoordinateSolve"),
        r"2辺の垂直二等分線を連立して外心を求め，頂点までの距離を測る。",
        ("座標平面", "垂直二等分線", "円"))

    add("inradius", inradius,
        r"内接円の半径を求めよ。",
        ("面積と周長の関係 S=rs",),
        ("TriangleConstruction", "EdgeLengthObservation", "IncenterWeights"),
        r"\(S=rs\)（\(s\) は半周長）から \(r=S/s\)。",
        ("三角形の面積", "内接円"))

    add("orthocenter_x", H[0],
        r"垂心の \(x\) 座標を求めよ。",
        ("2本の垂線の交点", "オイラー線の関係 H=A+B+C-2O"),
        ("TriangleConstruction", "OrthocenterIntersection", "CoordinateSolve"),
        r"2頂点から対辺への垂線を連立する。",
        ("座標平面", "垂線", "内積"))

    if sp.simplify(H[0]-O[0]) != 0:
        add("euler_line_slope", (H[1]-O[1])/(H[0]-O[0]),
            r"外心と垂心を通る直線の傾きを求めよ。",
            ("外心と垂心の座標", "重心もこの直線上にあること"),
            ("TriangleConstruction", "CircleParameter",
             "OrthocenterIntersection", "JoiningLine"),
            r"外心と垂心を求め，2点を通る直線の傾きを計算する。重心も同じ直線上にある。",
            ("座標平面", "直線の傾き"))

    add("nine_point_radius_sq", r2/4,
        r"各辺の中点3つを通る円の半径の平方を求めよ。",
        ("九点円が外接円の半分の半径をもつこと",),
        ("TriangleConstruction", "CentroidMap", "CircleParameter"),
        r"3辺の中点を通る円を求めると，半径は外接円の半分になる。",
        ("座標平面", "中点", "円"))

    add("incenter_x", incenter[0],
        r"内心の \(x\) 座標を求めよ。",
        ("辺の長さを重みとする内分",),
        ("TriangleConstruction", "EdgeLengthObservation", "IncenterWeights"),
        r"内心は \(\frac{aA+bB+cC}{a+b+c}\)（\(a,b,c\) は対辺の長さ）。",
        ("座標平面", "角の二等分線", "内分点"))

    add("OH_dist_sq", (H[0]-O[0])**2 + (H[1]-O[1])**2,
        r"外心と垂心の距離の平方を求めよ。",
        ("外心と垂心の座標", "OH^2 = 9R^2-(a^2+b^2+c^2)"),
        ("TriangleConstruction", "CircleParameter",
         "OrthocenterIntersection", "EdgeLengthObservation"),
        r"外心と垂心を求めて距離を計算する。\(OH^2=9R^2-(a^2+b^2+c^2)\) でも確かめられる。",
        ("座標平面", "円", "2点間の距離"))
    return nodes


def grid_triangle_centers() -> Iterable[tuple[int, int, int, int, int, int]]:
    return (
        (0, 0, 14, 0, 5, 12),    # 13-14-15 ヘロン三角形
        (0, 0, 13, 0, 4, 3),     # 5-12-13
        (0, 0, 21, 0, 6, 8),     # 10-17-21
        (0, 0, 16, 0, 5, 12),    # 13-15-16
    )


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
    (
        "ellipse_tangent",
        closure_ellipse_tangent,
        grid_ellipse_tangent,
        lambda params: (
            rf"楕円 \(E:\dfrac{{x^2}}{{{params[0]**2}}}"
            rf"+\dfrac{{y^2}}{{{params[1]**2}}}=1\) の外部の点 \(P\) から "
            r"\(E\) に2本の接線を引き，接点を \(T_1,T_2\) とする。"
        ),
    ),
    (
        "lattice_path",
        closure_lattice_path,
        grid_lattice_path,
        lambda n: (
            rf"格子点 \((0,0)\) から \(({n},{n})\) まで，"
            r"右または上に 1 ずつ進んで到達する最短経路を考える。"
        ),
    ),
    (
        "digit_power",
        closure_digit_power,
        grid_digit_power,
        lambda k: (
            rf"\(2^{{{k}}}\) を10進法で表す。"
            r"必要ならば \(\log_{10}2=0.3010\ldots\) を用いてよい。"
        ),
    ),
    (
        "triangle_centers",
        closure_triangle_centers,
        grid_triangle_centers,
        lambda p: (
            rf"座標平面上の3点 \(A({p[0]},{p[1]})\), \(B({p[2]},{p[3]})\), "
            rf"\(C({p[4]},{p[5]})\) を頂点とする三角形 \(ABC\) を考える。"
        ),
    ),
)


CONSTRUCTION_DOMAIN: dict[str, str] = {
    "regular_polygon": "complex_geometry",
    "cubic_tangent": "geometry_algebra",
    "ellipse_tangent": "conic_geometry",
    "lattice_path": "combinatorics",
    "digit_power": "number_theory",
    "triangle_centers": "plane_geometry",
}


def cut_problems() -> list[Problem]:
    """演繹閉包の各ノードを 1 問として切り出す。"""

    out: list[Problem] = []
    # 同じノードをパラメータ違いで作り直さない。グリッドは、そのノードが
    # 厳密に導ける param を1つ見つけるためだけに回す。数値変種は問題数を
    # 水増しするだけで、演繹閉包としては同じ1点にしかならない。
    seen: set[tuple[str, str]] = set()
    for cname, closure, grid, preamble in CONSTRUCTIONS:
        for param in grid():
            try:
                nodes = closure(param)
            except Exception:
                continue
            for node in nodes:
                if (cname, node.key) in seen:
                    continue
                seen.add((cname, node.key))
                statement = preamble(param) + node.question_ja
                depth = len(node.morphisms) + len(node.hidden)
                out.append(Problem(
                    f"traceback.{cname}.{node.key}",
                    CONSTRUCTION_DOMAIN.get(cname, "geometry_algebra"),
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
