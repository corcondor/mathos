"""10段の射を持つ幾何作問族。

包絡線、双対円錐曲線、発展曲線、直交中心、Minkowski和を、それぞれ
異なる観測量へ送る。閉形式と独立な数値・記号計算が一致した問題だけ返す。
"""

from __future__ import annotations

import math
from typing import Any, Callable, Iterable

import sympy as sp

try:
    from math_os_prototype.construct_engine import Problem
except ImportError:  # pragma: no cover
    from construct_engine import Problem


def _shoelace_area(points: list[tuple[float, float]]) -> float:
    return abs(
        sum(
            x1 * y2 - y1 * x2
            for (x1, y1), (x2, y2) in zip(points, points[1:] + points[:1])
        )
    ) / 2


def _convex_hull(
    points: list[tuple[float, float]],
) -> list[tuple[float, float]]:
    unique = sorted(set(points))
    if len(unique) <= 1:
        return unique

    def cross(
        origin: tuple[float, float],
        left: tuple[float, float],
        right: tuple[float, float],
    ) -> float:
        return (
            (left[0] - origin[0]) * (right[1] - origin[1])
            - (left[1] - origin[1]) * (right[0] - origin[0])
        )

    lower: list[tuple[float, float]] = []
    for point in unique:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], point) <= 1e-10:
            lower.pop()
        lower.append(point)
    upper: list[tuple[float, float]] = []
    for point in reversed(unique):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], point) <= 1e-10:
            upper.pop()
        upper.append(point)
    return lower[:-1] + upper[:-1]


def _geometry_astroid_envelope(params: dict[str, Any]) -> Problem | None:
    a, b = int(params["a"]), int(params["b"])
    if a <= 0 or b <= 0:
        return None

    exact_area = sp.Rational(3, 8) * sp.pi * a * b
    sample_count = 4096
    boundary = [
        (
            a * math.cos(2 * math.pi * index / sample_count) ** 3,
            b * math.sin(2 * math.pi * index / sample_count) ** 3,
        )
        for index in range(sample_count)
    ]
    numeric_area = _shoelace_area(boundary)
    if abs(numeric_area - float(exact_area)) > 2e-5 * float(exact_area):
        return None

    return Problem(
        "ultradeep.geometry_astroid_envelope_area",
        "analytic_geometry",
        "line_envelope+stationarity+numeric_shoelace",
        params,
        rf"\(0<\theta<\frac{{\pi}}{{2}}\) に対し，点 "
        rf"\(A_\theta=({a}\cos\theta,0)\), "
        rf"\(B_\theta=(0,{b}\sin\theta)\) をとる。直線 "
        rf"\(A_\theta B_\theta\) を対称性により全象限へ拡張して得られる"
        r"直線族の包絡線が囲む面積を求めよ。",
        sp.latex(exact_area),
        sp.sstr(exact_area),
        rf"直線族を \(F=\frac{{x}}{{{a}\cos\theta}}+"
        rf"\frac{{y}}{{{b}\sin\theta}}-1=0\) とする。"
        r"\(F=F_\theta=0\) から "
        rf"\(x={a}\cos^3\theta,\ y={b}\sin^3\theta\)。"
        r"したがって包絡線はアステロイドであり，Greenの公式より "
        rf"\(\frac12\oint(x\,dy-y\,dx)={sp.latex(exact_area)}\)。",
        (
            "CircleParameter",
            "AxisEndpointPair",
            "JoiningLine",
            "LineFamily",
            "EnvelopeStationarity",
            "ParameterElimination",
            "AstroidIdentification",
            "ClosedCurveOrientation",
            "GreenAreaMorphism",
            "AreaObservation",
        ),
        True,
        True,
        "symbolic_envelope_conditions_vs_numeric_shoelace",
    )


def _grid_geometry_astroid() -> Iterable[dict[str, Any]]:
    for a in range(2, 9):
        for b in range(2, 9):
            yield {"a": a, "b": b}


def _geometry_ellipse_tangent_pair(params: dict[str, Any]) -> Problem | None:
    a, b, k = int(params["a"]), int(params["b"]), int(params["k"])
    if not (a > b > 0 and k >= 3):
        return None

    delta = math.pi / k
    scale = 1 / math.cos(delta)
    for index in range(24):
        t = 2 * math.pi * index / 24 + 0.013
        matrix = sp.Matrix(
            [
                [math.cos(t + delta) / a, math.sin(t + delta) / b],
                [math.cos(t - delta) / a, math.sin(t - delta) / b],
            ]
        )
        point = matrix.inv() * sp.ones(2, 1)
        expected = (a * scale * math.cos(t), b * scale * math.sin(t))
        if max(abs(float(point[i]) - expected[i]) for i in range(2)) > 1e-8:
            return None

    rhs = sp.sec(sp.pi / k) ** 2
    return Problem(
        "ultradeep.geometry_ellipse_tangent_pair_locus",
        "projective_geometry",
        "dual_conic+tangent_intersection+linear_system",
        params,
        rf"楕円 \(E:\frac{{x^2}}{{{a * a}}}+\frac{{y^2}}{{{b * b}}}=1\) "
        rf"上の点を \(P(t)=({a}\cos t,{b}\sin t)\) とする。"
        rf"\(P(t+\frac{{\pi}}{{{k}}})\) と "
        rf"\(P(t-\frac{{\pi}}{{{k}}})\) における2本の接線の交点を \(Q(t)\)"
        r"とするとき，\(Q(t)\) の軌跡の方程式を求めよ。",
        rf"\frac{{x^2}}{{{a * a}}}+\frac{{y^2}}{{{b * b}}}"
        rf"={sp.latex(rhs)}",
        sp.sstr(rhs),
        rf"2本の接線の方程式を加減して解くと "
        rf"\(Q(t)=({a}\sec\frac{{\pi}}{{{k}}}\cos t,"
        rf"{b}\sec\frac{{\pi}}{{{k}}}\sin t)\)。よって軌跡は "
        rf"\(\frac{{x^2}}{{{a * a}}}+\frac{{y^2}}{{{b * b}}}"
        rf"={sp.latex(rhs)}\)。",
        (
            "EllipseObject",
            "TrigonometricChart",
            "PairedParameterShift",
            "TangentDualization",
            "DualLinePair",
            "LinearIntersection",
            "TrigonometricDiagonalization",
            "HomothetyRecognition",
            "ConicElimination",
            "LocusEquationObservation",
        ),
        True,
        True,
        "closed_intersection_formula_vs_numeric_two_line_solve",
    )


def _grid_geometry_ellipse_tangent_pair() -> Iterable[dict[str, Any]]:
    for a in range(2, 7):
        for b in range(1, a):
            for k in range(3, 9):
                yield {"a": a, "b": b, "k": k}


def _geometry_parabola_normal_envelope(params: dict[str, Any]) -> Problem | None:
    a = int(params["a"])
    if a <= 0:
        return None

    t, x, y = sp.symbols("t x y")
    family = x + t * y - 2 * a * t - a * t**3
    stationary = sp.diff(family, t)
    resultant = sp.factor(sp.resultant(family, stationary, t))
    implicit = sp.expand(4 * (y - 2 * a) ** 3 - 27 * a * x**2)
    if sp.simplify(resultant - a**2 * implicit) != 0:
        return None
    for value in (-3, -2, -1, 0, 1, 2, 3):
        px = -2 * a * value**3
        py = 2 * a + 3 * a * value**2
        if implicit.subs({x: px, y: py}) != 0:
            return None

    return Problem(
        "ultradeep.geometry_parabola_normal_envelope",
        "differential_geometry",
        "normal_family+resultant+evolute",
        params,
        rf"放物線 \(C:y=\frac{{x^2}}{{{4 * a}}}\) 上の各点で法線を引く。"
        r"この法線族の包絡線の方程式を求めよ。",
        rf"4(y-{2 * a})^3={27 * a}x^2",
        sp.sstr(implicit),
        rf"\(C\) を \(P(t)=({2 * a}t,{a}t^2)\) と表示する。法線族は "
        rf"\(F=x+ty-{2 * a}t-{a}t^3=0\)。"
        r"\(F=F_t=0\) から "
        rf"\(x=-{2 * a}t^3,\ y={2 * a}+{3 * a}t^2\)。"
        rf"消去すると \(4(y-{2 * a})^3={27 * a}x^2\)。",
        (
            "ParabolaObject",
            "TangentVector",
            "NormalDirection",
            "NormalLine",
            "NormalLineFamily",
            "EnvelopeStationarity",
            "StationaryParameterSolve",
            "EvoluteParametrization",
            "ResultantElimination",
            "ImplicitCurveObservation",
        ),
        True,
        True,
        "symbolic_resultant_identity_vs_parametric_substitution",
    )


def _grid_geometry_parabola_normal() -> Iterable[dict[str, Any]]:
    for a in range(1, 31):
        yield {"a": a}


def _geometry_orthocenter_locus(params: dict[str, Any]) -> Problem | None:
    a, b = int(params["a"]), int(params["b"])
    if not (a > b > 0):
        return None

    exact_area = sp.pi * sp.Rational(a**3, b)
    sample_count = 4096
    locus: list[tuple[float, float]] = []
    for index in range(sample_count):
        t = 2 * math.pi * (index + 0.25) / sample_count
        px, py = a * math.cos(t), b * math.sin(t)
        hx = px
        hy = (a * a - px * px) / py
        locus.append((hx, hy))
    numeric_area = _shoelace_area(locus)
    if abs(numeric_area - float(exact_area)) > 2e-5 * float(exact_area):
        return None

    return Problem(
        "ultradeep.geometry_orthocenter_locus_area",
        "euclidean_geometry",
        "orthocenter+linear_image+numeric_shoelace",
        params,
        rf"楕円 \(E:\frac{{x^2}}{{{a * a}}}+\frac{{y^2}}{{{b * b}}}=1\) "
        rf"の長軸の端点を \(A=(-{a},0),B=({a},0)\) とする。"
        r"\(E\) 上を動く点 \(P\ne A,B\) に対し，三角形 \(ABP\) の"
        r"垂心を \(H\) とする。\(H\) の軌跡が囲む面積を求めよ。",
        sp.latex(exact_area),
        sp.sstr(exact_area),
        rf"\(P=({a}\cos t,{b}\sin t)\) とおく。\(AB\) が水平なので"
        rf"垂心の \(x\) 座標は \({a}\cos t\)。もう1本の高さから "
        rf"\(H=({a}\cos t,\frac{{{a * a}}}{{{b}}}\sin t)\)。"
        rf"したがって軌跡は半軸 \({a},\frac{{{a * a}}}{{{b}}}\) の楕円で，"
        rf"面積は \({sp.latex(exact_area)}\)。",
        (
            "EllipseObject",
            "MajorAxisVertexPair",
            "MovingTriangle",
            "AltitudeConstraint",
            "OrthocenterIntersection",
            "CoordinateSolve",
            "LinearImageRecognition",
            "ImageEllipse",
            "DeterminantAreaScaling",
            "AreaObservation",
        ),
        True,
        True,
        "altitude_coordinate_formula_vs_numeric_locus_shoelace",
    )


def _grid_geometry_orthocenter() -> Iterable[dict[str, Any]]:
    for a in range(2, 10):
        for b in range(1, a):
            yield {"a": a, "b": b}


def _geometry_minkowski_polygon(params: dict[str, Any]) -> Problem | None:
    n, radius = int(params["n"]), int(params["R"])
    if n < 3 or radius <= 0:
        return None

    polygon = [
        (
            radius * math.cos(2 * math.pi * index / n),
            radius * math.sin(2 * math.pi * index / n),
        )
        for index in range(n)
    ]
    rotated = [
        (
            radius * math.cos(2 * math.pi * index / n + math.pi / n),
            radius * math.sin(2 * math.pi * index / n + math.pi / n),
        )
        for index in range(n)
    ]
    hull = _convex_hull(
        [(x1 + x2, y1 + y2) for x1, y1 in polygon for x2, y2 in rotated]
    )
    numeric_perimeter = sum(
        math.hypot(x2 - x1, y2 - y1)
        for (x1, y1), (x2, y2) in zip(hull, hull[1:] + hull[:1])
    )
    exact_perimeter = 4 * n * radius * sp.sin(sp.pi / n)
    if len(hull) != 2 * n:
        return None
    if abs(numeric_perimeter - float(exact_perimeter)) > 1e-8:
        return None

    return Problem(
        "ultradeep.geometry_regular_polygon_minkowski_perimeter",
        "convex_geometry",
        "minkowski_sum+support_faces+convex_hull",
        params,
        rf"同じ中心・外接円半径 \({radius}\) の正 \({n}\) 角形 \(P,Q\) があり，"
        rf"\(Q\) は \(P\) を中心のまわりに \(\frac{{\pi}}{{{n}}}\) 回転したもの"
        r"とする。Minkowski和 \(P+Q=\{p+q\mid p\in P,q\in Q\}\) の周長を求めよ。",
        sp.latex(exact_perimeter),
        sp.sstr(exact_perimeter),
        rf"両多角形の辺の法線方向は交互に現れるため，\(P+Q\) は正 \({2 * n}\)"
        rf"角形になる。隣接頂点間の距離は \(2\cdot {radius}"
        rf"\sin\frac{{\pi}}{{{n}}}\)。したがって周長は "
        rf"\({2 * n}\cdot2\cdot {radius}\sin\frac{{\pi}}{{{n}}}"
        rf"={sp.latex(exact_perimeter)}\)。",
        (
            "RootOfUnityChart",
            "RegularPolygon",
            "HalfStepRotation",
            "SecondRegularPolygon",
            "MinkowskiAddition",
            "SupportDirectionMerge",
            "VertexSumHull",
            "RegularDoublePolygon",
            "EdgeLengthObservation",
            "PerimeterObservation",
        ),
        True,
        True,
        "regular_polygon_formula_vs_all_vertex_sums_convex_hull",
    )


def _grid_geometry_minkowski() -> Iterable[dict[str, Any]]:
    for n in range(3, 13):
        for radius in range(1, 7):
            yield {"n": n, "R": radius}


GEOMETRY_DEEP_FAMILIES: tuple[
    tuple[
        Callable[[dict[str, Any]], Problem | None],
        Callable[[], Iterable[dict[str, Any]]],
    ],
    ...,
] = (
    (_geometry_astroid_envelope, _grid_geometry_astroid),
    (_geometry_ellipse_tangent_pair, _grid_geometry_ellipse_tangent_pair),
    (_geometry_parabola_normal_envelope, _grid_geometry_parabola_normal),
    (_geometry_orthocenter_locus, _grid_geometry_orthocenter),
    (_geometry_minkowski_polygon, _grid_geometry_minkowski),
)
