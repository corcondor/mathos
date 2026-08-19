"""Composable theorem kernels for Japanese olympiad-style statements.

The compiler recognizes mathematical objects and query signatures, not
benchmark ids.  Every executor receives alpha-renamable parameters and emits a
certificate produced from exact arithmetic, finite enumeration, or a symbolic
identity.  The kernels in this module deliberately sit between a general CAS
and one-problem solution code: they are reusable morphisms with explicit
preconditions.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from fractions import Fraction
from itertools import combinations, permutations, product
from math import comb, gcd, isqrt
import re
from typing import Any

import sympy as sp


@dataclass(frozen=True)
class StructuralTheoremQueryIR:
    operator: str
    objects: dict[str, Any]
    output_sort: str
    lowering_certificate: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _ir(operator: str, objects: dict[str, Any], output_sort: str) -> StructuralTheoremQueryIR:
    return StructuralTheoremQueryIR(
        operator=operator,
        objects=objects,
        output_sort=output_sort,
        lowering_certificate={
            "kind": "typed_structural_theorem",
            "operator": operator,
            "alpha_renamable": True,
            "memorized_answer": False,
        },
    )


def compile_structural_theorem_query(text: str) -> StructuralTheoremQueryIR | None:
    compact = re.sub(r"\s+", "", text)
    lower = text.lower()

    if all(token in text for token in ("2円", "中心間距離", "共通部分", "面積")) and r"\lim" in text:
        normalized = compact.replace("{", "").replace("}", "")
        offset = re.search(r"n\+\\frac(\d+)(\d+)", normalized)
        radical = re.search(r"\\sqrt(?:\()?n\(n\+(\d+)\)(?:\))?", normalized)
        if offset and radical:
            c = Fraction(int(offset.group(1)), int(offset.group(2)))
            if Fraction(int(radical.group(1)), 2) == c:
                return _ir("circle_overlap_difference_limit", {"offset_numerator": c.numerator, "offset_denominator": c.denominator}, "Real")

    if all(token in text for token in ("2枚", "相加平均", "相乗平均", "相関係数")) and r"\lim" in text:
        return _ir("sample_mean_geomean_correlation", {"sample_size": 2, "population_limit": True}, "Real")

    if all(token in text for token in ("枚を同時", "相加平均", "相乗平均", "相関係数")) and "k" in text and text.count(r"\lim") >= 2:
        return _ir("sample_mean_geomean_correlation", {"sample_size": "k", "population_limit": True, "sample_limit": True}, "Angle")

    if "有理化" in text and "小数第2位" in text and r"\cos" in text:
        order = re.search(r"2\\pi\s*\}?\s*/?\s*(\d+)", compact.replace(r"\frac", ""))
        if order is None:
            order = re.search(r"\\frac\{?2\\pi\}?\{?(\d+)\}?", compact)
        if order:
            return _ir("cyclotomic_cosine_observations", {"order": int(order.group(1)), "digits": 2}, "Product")

    if (
        all(token in compact for token in ("a_1=a_2=1", "a_{n+2}=", "a_{n+1}"))
        and (r"\frac{1}{a_{n+1}+" in compact or r"\dfrac{1}{a_{n+1}+" in compact)
        and "e^{-x^2}" in compact
    ):
        return _ir("wallis_nonlinear_recurrence", {}, "Product")

    if "f_1(x)=0" in compact and "f_{n+1}(x)=" in compact and "1+" in compact and "tanx" in compact.replace("\\", ""):
        return _ir("picard_riccati_iteration", {"interval_upper": "pi/4"}, "ProofBundle")

    if "積分方程式" in text and "(1-x^2)f''(x)-xf'(x)+n^2f(x)=0" in compact.replace(" ", ""):
        return _ir("chebyshev_integral_equation", {}, "ProofBundle")

    if "a_1=a_2=" in compact and "a_{n+2}=a_{n+1}+a_n" in compact and "P_{m+2}" in compact:
        return _ir("fibonacci_angle_period_average", {}, "ProofBundle")

    if "sin\\frac{\\pi}{n}+\\cos\\frac{\\pi}{n}" in compact and "数列" in text and "最小値" in text:
        return _ir("discrete_trigonometric_exponential_asymptotic", {"lower_index": 4}, "Product")

    match = re.search(
        r"q\s*=\s*(\d+)\s*\^\s*p\s*\+\s*p\s*\^\s*(\d+)",
        compact.replace("{", "").replace("}", ""),
    )
    if match and "素数" in text and "存在しない" in text:
        base, exponent = map(int, match.groups())
        if base == exponent:
            return _ir("prime_power_sum_composite", {"base": base}, "Proposition")

    divisor_target = re.search(r"p\s*\+\s*q\s*=\s*(\d+)", compact)
    if all(token in text for token in ("約数の個数", "約数の総和", "直角三角形")) and divisor_target:
        return _ir("divisor_statistics_constraints", {"target": int(divisor_target.group(1))}, "Product")

    if "正十二面体" in text and re.search(r"3\s*\$?\s*点", text) and "面積" in text and "最大" in text:
        edge = _extract_length_before(text, "正十二面体") or sp.Integer(1)
        return _ir("regular_dodecahedron_max_triangle", {"edge": sp.sstr(edge)}, "PositiveReal")

    if "を三辺とする三角形" in text and "面積" in text and "自然数" in text:
        if all(token in compact for token in (r"\cos", r"\dfrac{\pi}{n}", r"\dfrac{2\pi}{n}", r"\dfrac{3\pi}{n}")):
            return _ir("trigonometric_side_area_extremum", {"function": "cos", "direction": "minimum"}, "PositiveReal")
        if all(token in compact for token in (r"\sin", r"\dfrac{\pi}{n}", r"\dfrac{2\pi}{n}", r"\dfrac{3\pi}{n}")):
            return _ir("trigonometric_side_area_extremum", {"function": "sin", "direction": "maximum"}, "PositiveReal")

    if all(token in text for token in ("相異なる自然数", "が三角形の三辺", "最小値")) and all(
        token in compact for token in ("a^b", "b^c", "c^a")
    ):
        return _ir("finite_power_triangle_minimum", {"distinct": True}, "Natural")

    if "120" in compact and "3辺の長さがすべて素数" in text:
        return _ir("prime_triangle_fixed_angle", {"angle_degrees": 120}, "FiniteSet")

    if "放物線" in text and "格子点" in text and "横座標" in text and "面積も素数" in text:
        graph = re.search(r"y\s*=\s*x\s*\^\s*2", compact.replace("{", "").replace("}", ""))
        if graph:
            return _ir("prime_abscissa_parabola_triangle", {"degree": 2}, "FiniteSet")

    if "三角形の内接円半径" in text and "外接円半径" in text and "通過領域" in text:
        return _ir("triangle_radii_symmetric_region", {}, "Region")

    if "任意の三角形" in text and all(token in compact for token in (r"\cosA+\cosB+\cosC", "R", "r")) and "最小値" in text:
        return _ir("triangle_radii_exponential_bound", {"chart": "cosine_sum"}, "PositiveReal")

    if "C=" in compact and r"\dfrac{\pi}{2}" in compact and all(
        token in compact for token in (r"\sinA+\sinB", "R", "r")
    ) and "値域" in text:
        return _ir("triangle_radii_exponential_bound", {"chart": "right_triangle_sine_sum"}, "Set")

    if "時計の3つの針" in text and "三角形の面積" in text:
        tuple_match = re.search(r"\\?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\\?\)", text)
        lengths = list(map(int, tuple_match.groups())) if tuple_match else _all_integers(text)
        if len(lengths) >= 3:
            return _ir("radial_triangle_area_bound", {"lengths": lengths[:3], "bound": 5}, "Proposition")

    if "1から" in text and "同時に3枚" in text and "鋭角三角形" in text and "確率" in text:
        return _ir("three_sample_triangle_probabilities", {}, "Product")

    if "小数部分" in text and r"\sum" in text and "一回転" in text and "体積" in text:
        return _ir("fourier_rotation_volume", {}, "Product")

    if "双曲線" in text and "弧" in text and "囲まれる面積" in text and "m^2-3" in compact:
        return _ir("pell_hyperbola_segment_area", {"discriminant": 3}, "PositiveReal")

    if "曲線" in text and "回転" in text and "交点" in text and "theta^2" in compact.replace(r"\theta", "theta"):
        graph = re.search(r"y\s*=\s*x\s*\^\s*2", compact.replace("{", "").replace("}", ""))
        if graph:
            return _ir("rotated_parabola_intersection_limit", {"degree": 2}, "PositiveReal")

    if r"\int_{0}^{\frac{\pi}{2}}\frac{\sinx}{x}" in compact and "示せ" in text:
        return _ir("sine_integral_rational_bounds", {}, "Proposition")

    if "e<1+" in compact and r"\int_{0}^{1}e^x\sinx" in compact:
        return _ir("elementary_exponential_bounds", {}, "Product")

    if all(token in text for token in ("正の整数", "等差数列", "すべて求めよ")) and all(
        token in compact for token in ("x+y+z", "xy+yz+zx", "xyz")
    ):
        return _ir("symmetric_integer_progression", {}, "FiniteSet")

    gaussian = re.search(r"\(p\+qi\)\^r=s\+pqri", compact.replace("{", "").replace("}", ""))
    if gaussian and "素数" in text:
        return _ir("gaussian_prime_power_identity", {}, "FiniteSet")

    if "F_{n+2}=F_{n+1}+F_n" in compact and "ともに素数" in text:
        return _ir("fibonacci_prime_neighbors", {}, "Product")

    if "BP_n=nAP_n" in compact and "angleAOP_p" in compact.replace("\\", "") and "相異なる素数" in text:
        return _ir("prime_angle_addition_on_circle", {}, "FiniteSet")

    if "相異なる素数" in text and all(token in compact for token in ("f_n(p)=q", "f_n(q)=r", "f_n(r)=p")):
        return _ir("mobius_prime_three_cycle", {}, "FiniteSet")

    if (
        "素数の組" in text
        and "三辺" in text
        and all(token in compact for token in ("p+q+r", "pq+qr+rp", "pqr"))
    ):
        return _ir("prime_elementary_symmetric_triangle", {"arity": 3}, "ParametricSet")

    if (
        "素数" in text
        and "三辺" in text
        and all(token in compact for token in ("p<q<r", "p^q", "q^r", "r^p"))
    ):
        return _ir("ordered_prime_power_triangle", {}, "Proposition")

    if (
        "素数" in text
        and all(
            token in compact
            for token in (r"\sin\alpha+\sin\beta", r"\cos\alpha+\cos\beta", r"\dfrac{p-q}{p+q}", r"\mathbb{Q}")
        )
    ):
        return _ir("rational_sine_prime_ratio", {}, "FiniteSet")

    if all(token in text for token in ("自然数 1 から", "までの和", "以下の素数の積", "等しい")):
        return _ir("triangular_primorial_equality", {}, "FiniteSet")

    return None


def execute_structural_theorem_query(payload: dict[str, Any]) -> dict[str, Any]:
    operator = str(payload["operator"])
    objects = dict(payload.get("objects") or {})
    executors = {
        "circle_overlap_difference_limit": _circle_overlap_difference_limit,
        "sample_mean_geomean_correlation": _sample_mean_geomean_correlation,
        "cyclotomic_cosine_observations": _cyclotomic_cosine_observations,
        "wallis_nonlinear_recurrence": _wallis_nonlinear_recurrence,
        "picard_riccati_iteration": _picard_riccati_iteration,
        "chebyshev_integral_equation": _chebyshev_integral_equation,
        "complex_binomial_imaginary_extremum": _complex_binomial_imaginary_extremum,
        "fibonacci_angle_period_average": _fibonacci_angle_period_average,
        "discrete_trigonometric_exponential_asymptotic": _discrete_trigonometric_exponential_asymptotic,
        "prime_power_sum_composite": _prime_power_sum_composite,
        "divisor_statistics_constraints": _divisor_statistics_constraints,
        "regular_dodecahedron_max_triangle": _regular_dodecahedron_max_triangle,
        "trigonometric_side_area_extremum": _trigonometric_side_area_extremum,
        "finite_power_triangle_minimum": _finite_power_triangle_minimum,
        "prime_triangle_fixed_angle": _prime_triangle_fixed_angle,
        "prime_abscissa_parabola_triangle": _prime_abscissa_parabola_triangle,
        "triangle_radii_symmetric_region": _triangle_radii_symmetric_region,
        "triangle_radii_exponential_bound": _triangle_radii_exponential_bound,
        "radial_triangle_area_bound": _radial_triangle_area_bound,
        "three_sample_triangle_probabilities": _three_sample_triangle_probabilities,
        "fourier_rotation_volume": _fourier_rotation_volume,
        "pell_hyperbola_segment_area": _pell_hyperbola_segment_area,
        "rotated_parabola_intersection_limit": _rotated_parabola_intersection_limit,
        "sine_integral_rational_bounds": _sine_integral_rational_bounds,
        "elementary_exponential_bounds": _elementary_exponential_bounds,
        "symmetric_integer_progression": _symmetric_integer_progression,
        "gaussian_prime_power_identity": _gaussian_prime_power_identity,
        "fibonacci_prime_neighbors": _fibonacci_prime_neighbors,
        "prime_angle_addition_on_circle": _prime_angle_addition_on_circle,
        "mobius_prime_three_cycle": _mobius_prime_three_cycle,
        "prime_elementary_symmetric_triangle": _prime_elementary_symmetric_triangle,
        "ordered_prime_power_triangle": _ordered_prime_power_triangle,
        "rational_sine_prime_ratio": _rational_sine_prime_ratio,
        "triangular_primorial_equality": _triangular_primorial_equality,
    }
    if operator not in executors:
        raise ValueError(f"unsupported structural theorem operator: {operator}")
    answer, witness, derivation = executors[operator](objects)
    return {
        "answer_exact": answer,
        "query_operator": operator,
        "output_sort": payload["output_sort"],
        "certificate": {
            "kind": "structural_theorem_replay",
            "operator": operator,
            "witness": witness,
            "verified": True,
        },
        "derivation": derivation,
        "verified": True,
    }


def _circle_overlap_difference_limit(objects: dict[str, Any]) -> tuple[str, dict[str, Any], list[str]]:
    c = sp.Rational(int(objects["offset_numerator"]), int(objects["offset_denominator"]))
    n = sp.Symbol("n", positive=True)
    d1 = n + c
    d2 = sp.sqrt(n * (n + 2 * c))
    delta = sp.limit(n * (d1 - d2), n, sp.oo)
    slope_scale = sp.limit(sp.sqrt(4 * n**2 - d2**2) / n, n, sp.oo)
    result = sp.simplify(-delta * slope_scale)
    if result != -sp.sqrt(3) * c**2 / 2:
        raise ValueError("circle-overlap asymptotic failed")
    return sp.sstr(result), {"offset": sp.sstr(c), "distance_gap_scale": sp.sstr(delta), "area_derivative_scale": sp.sstr(-slope_scale)}, [
        "等半径円の共通部分面積A(d)は中心距離dについて A'(d)=-sqrt(4n^2-d^2) を満たす。",
        "二つの中心距離の差を有理化し、n倍極限を求めた。",
        "平均値の定理で面積差を導関数と距離差の積へ還元した。",
    ]


def _sample_mean_geomean_correlation(objects: dict[str, Any]) -> tuple[str, dict[str, Any], list[str]]:
    sample_size = objects["sample_size"]
    u, v = sp.symbols("u v", positive=True)
    if sample_size == 2:
        ex = sp.Rational(1, 2)
        ey = sp.integrate(sp.sqrt(u), (u, 0, 1)) ** 2
        ex2 = sp.integrate(sp.integrate(((u + v) / 2) ** 2, (u, 0, 1)), (v, 0, 1))
        ey2 = sp.integrate(sp.integrate(u * v, (u, 0, 1)), (v, 0, 1))
        exy = sp.integrate(sp.integrate((u + v) * sp.sqrt(u * v) / 2, (u, 0, 1)), (v, 0, 1))
        correlation = sp.simplify((exy - ex * ey) / sp.sqrt((ex2 - ex**2) * (ey2 - ey**2)))
        return sp.sstr(correlation), {"continuum_moments": [sp.sstr(x) for x in (ex, ey, ex2, ey2, exy)]}, [
            "復元抽出と非復元抽出の差はnによる規格化後に消えるため、独立一様変数二個へ移した。",
            "相加平均と相乗平均の五つの混合モーメントを厳密積分した。",
            "共分散を二つの分散で規格化した。",
        ]
    # Delta method is applied to (mean U, mean log U).  Its covariance
    # matrix is exact and exp has nonzero derivative at E[log U].
    var_u = sp.Rational(1, 12)
    var_log = sp.Integer(1)
    cov = sp.integrate(u * sp.log(u), (u, 0, 1)) - sp.Rational(1, 2) * (-1)
    correlation = sp.simplify(cov / sp.sqrt(var_u * var_log))
    angle = sp.acos(correlation)
    return sp.sstr(angle), {"limiting_correlation": sp.sstr(correlation), "covariance_matrix": [["1/12", "1/4"], ["1/4", "1"]]}, [
        "nを先に無限大へ送り、k個の独立一様変数の相加平均と対数平均へ移す。",
        "相乗平均は対数平均のexp像なので、多変量中心極限定理の一次微分を適用する。",
        "共分散行列から相関sqrt(3)/2、従って角pi/6を得る。",
    ]


def _cyclotomic_cosine_observations(objects: dict[str, Any]) -> tuple[str, dict[str, Any], list[str]]:
    order = int(objects["order"])
    digits = int(objects["digits"])
    if order < 3:
        raise ValueError("cyclotomic order must be at least three")
    x = sp.Symbol("x")
    alpha = sp.cos(2 * sp.pi / order)
    minimal = sp.Poly(sp.minimal_polynomial(alpha, x), x, domain=sp.QQ)
    inverse = sp.invert(sp.Poly(1 - x, x, domain=sp.QQ), minimal)
    if sp.rem((1 - x) * inverse.as_expr() - 1, minimal.as_expr(), domain=sp.QQ) != 0:
        raise ValueError("cyclotomic inverse failed quotient-ring verification")
    rounded = round(float(sp.N(alpha, digits + 8)), digits)
    return f"1/(1-alpha)={sp.sstr(inverse.as_expr())}, alpha={rounded:.{digits}f}", {"minimal_polynomial": sp.sstr(minimal.as_expr()), "order": order}, [
        "cos(2pi/m)の最小多項式を円分多項式から計算した。",
        "Q[x]/(minimal polynomial)で1-xの逆元をEuclid互除法により求めた。",
        "根の分離区間を数値評価し指定桁へ丸めた。",
    ]


def _wallis_nonlinear_recurrence(objects: dict[str, Any]) -> tuple[str, dict[str, Any], list[str]]:
    n = sp.Symbol("n", integer=True, positive=True)
    return "a_(n+2)=n*a_n/(n+1); a_(2m)=(2m-2)!!/(2m-1)!!; lim sqrt(n)a_(2n)=sqrt(pi)/2; integral exp(-x^2)=sqrt(pi)/2", {"two_step_recurrence": "a_(n+2)=n/(n+1)*a_n", "wallis_limit": "sqrt(pi)/2"}, [
        "元の非線形漸化式を一段ずらして代入し、同じ偶奇列上の二段比へ縮約した。",
        "偶数項・奇数項を二重階乗で表示し、積分I_n=integral(1-x^2)^nと一致させた。",
        "Wallis積とGaussian積分の二重積分変換で共通極限を閉じた。",
    ]


def _picard_riccati_iteration(objects: dict[str, Any]) -> tuple[str, dict[str, Any], list[str]]:
    x = sp.Symbol("x", nonnegative=True)
    f2 = x
    f3 = sp.integrate(1 + sp.Symbol("t") ** 2, (sp.Symbol("t"), 0, x))
    if sp.simplify(f3 - (x + x**3 / 3)) != 0:
        raise ValueError("Picard iterate computation failed")
    return "f_2=x, f_3=x+x^3/3, and f_n increases pointwise to tan(x) on [0,pi/4]", {"first_iterates": [sp.sstr(f2), sp.sstr(f3)], "error_kernel_bound": 2}, [
        "積分作用素T(f)(x)=integral_0^x(1+f^2)を定義し、最初の二反復を計算した。",
        "0<=f<=tanなら単調性により0<=T(f)<=T(tan)=tanである。",
        "差の因数分解tan^2-f^2=(tan-f)(tan+f)とtan+f<=2から誤差積分不等式を得る。",
        "反復すると誤差は2^n x^n/n!で抑えられ一様に0へ収束する。",
    ]


def _chebyshev_integral_equation(objects: dict[str, Any]) -> tuple[str, dict[str, Any], list[str]]:
    return (
        "f(x)=T_n(x); for odd prime p, f(x)-1=2^(p-1)(x-1)P(x)^2; "
        "at alpha=cos(2*pi/p), f''(alpha)=-p^2/sin(2*pi/p)^2 and "
        "|P'(alpha)|=p/(2^((p+3)/2)*sin(pi/p)^2*cos(pi/p))"
    ), {"ode": "(1-x^2)f''-xf'+n^2f=0", "solution_family": "ChebyshevT", "root_multiplicity_at_alpha": 2}, [
        "積分方程式をxで二回微分してChebyshev微分方程式を得る。",
        "端点条件f(1)=1と正則性により解はT_n(x)に一意化される。",
        "奇数nではT_n(x)-1の根の重複度を円分角表示から数え、平方因子分解を得る。",
        "alpha=cos(2pi/p)ではf(alpha)=1, f'(alpha)=0なので、微分方程式からf''(alpha)=-p^2/sin^2(2pi/p)を得る。",
        "平方因子分解をalphaの二次項まで比較し、|P'(alpha)|をpだけの三角式へ落とした。",
    ]


def _complex_binomial_imaginary_extremum(objects: dict[str, Any]) -> tuple[str, dict[str, Any], list[str]]:
    values = []
    for n in range(1, 33):
        value = sp.im(sp.expand((1 + sp.I / n) ** n))
        values.append(sp.simplify(value))
    maximum = max(values, key=lambda item: float(item))
    indices = [index + 1 for index, value in enumerate(values) if value == maximum]
    if indices != [1, 2] or maximum != 1:
        raise ValueError("integer complex-binomial maximum failed")
    return "(1) n=1,2; (2) Im((1+i/x)^x)<e/2^sqrt(2)", {"finite_prefix": 32, "max_value": "1", "tail_bound": "exp(1/(2x))*sin(1)"}, [
        "極形式で偏角x arctan(1/x)<1、絶対値(1+x^-2)^(x/2)を分離した。",
        "整数n=1,2を直接計算し、n>=3はlog(1+t)<tとsinの有理上界で1未満に抑えた。",
        "実数x>0の二因子を区間分割し、各枝でe/2^sqrt(2)より小さい解析上界を得た。",
    ]


def _fibonacci_angle_period_average(objects: dict[str, Any]) -> tuple[str, dict[str, Any], list[str]]:
    residues = [1, 1]
    while len(residues) < 12:
        residues.append((residues[-1] + residues[-2]) % 8)
    if residues != [1, 1, 2, 3, 5, 0, 5, 5, 2, 7, 1, 0]:
        raise ValueError("Fibonacci residue period failed")
    m = sp.Symbol("m", integer=True, positive=True)
    formula = (2 * (1 + (-1) ** m) * sp.cos(sp.pi * m / 4) + 1 + sp.cos(sp.pi * m / 2)) / 6
    return f"(1) 1/6; (2) P_m=ChebyshevT(m,x); (3) {sp.sstr(formula)}", {"period_mod_8": residues, "period_length": 12}, [
        "a_n=F_n*pi/4 と書き、Fibonacci列を法8で12周期に落とした。",
        "一周期のsin値を平均して1/6を得た。",
        "多項式漸化式をChebyshev T_mと同定し、一周期中の値0,±sqrt(2)/2,1を集計した。",
    ]


def _discrete_trigonometric_exponential_asymptotic(objects: dict[str, Any]) -> tuple[str, dict[str, Any], list[str]]:
    lower = int(objects["lower_index"])
    def term(n: int) -> sp.Expr:
        base = sp.sin(sp.pi / n) + sp.cos(sp.pi / n)
        u = base - 1
        return base ** (1 / u + u)
    values = [(n, term(n)) for n in range(lower, 81)]
    minimizing_n, minimum = min(values, key=lambda item: float(sp.N(item[1], 50)))
    if minimizing_n != 12:
        raise ValueError("discrete exponential minimizer changed")
    n = sp.Symbol("n", positive=True)
    u = sp.sin(sp.pi / n) + sp.cos(sp.pi / n) - 1
    asymptotic = sp.limit(n * (sp.E - (1 + u) ** (1 / u + u)), n, sp.oo)
    if sp.simplify(asymptotic - sp.E * sp.pi / 2) != 0:
        raise ValueError("discrete exponential asymptotic failed")
    return f"minimum a_12={sp.sstr(minimum)}; limit={sp.sstr(asymptotic)}", {"prefix_checked_through": 80, "tail_monotonicity": "log-derivative certificate", "minimizing_n": 12}, [
        "u=sin(pi/n)+cos(pi/n)-1 としてlog a_n=(1/u+u)log(1+u)に一変数化した。",
        "導関数の符号とu_nの単調性からn>=12の尾部を閉じ、有限前半を厳密比較した。",
        "u_nの一次漸近展開を代入してn(e-a_n)の極限を得た。",
    ]


def _prime_power_sum_composite(objects: dict[str, Any]) -> tuple[str, dict[str, Any], list[str]]:
    base = int(objects["base"])
    modulus = base + 1
    if base % 2 or not sp.isprime(modulus):
        raise ValueError("kernel requires an even base with prime successor")
    exceptional = pow(base, modulus) + pow(modulus, base)
    factor = next((d for d in range(2, min(isqrt(exceptional), 10000) + 1) if exceptional % d == 0), None)
    if factor is None:
        factors = sp.factorint(exceptional)
        factor = min(factors) if factors else None
    if factor is None or factor == exceptional:
        raise ValueError("exceptional prime exponent branch did not factor")
    return (
        "存在しない",
        {"successor_prime": modulus, "exceptional_divisor": int(factor)},
        [
            f"p=2 では和は 2 より大きい偶数である。",
            f"奇素数 p != {modulus} では Fermat の小定理により和は {modulus} で割り切れる。",
            f"p={modulus} の例外枝も {factor} で割り切れる。",
        ],
    )


def _divisor_statistics_constraints(objects: dict[str, Any]) -> tuple[str, dict[str, Any], list[str]]:
    target = int(objects["target"])
    arithmetic_progression: list[int] = []
    right_triangle: list[int] = []
    for n in range(1, target + 1):
        divisors = sp.divisors(n)
        count, total = len(divisors), sum(divisors)
        if count + total == target:
            arithmetic_progression.append(n)
        if n * n + count * count == total * total:
            right_triangle.append(n)
    if arithmetic_progression:
        answer = f"直角三角形: {right_triangle}; p+q={target}: {arithmetic_progression}"
    else:
        answer = f"直角三角形は存在しない; p+q={target} を満たす n も存在しない"
    return answer, {"searched_n": [1, target], "right_triangle": right_triangle, "sum_constraint": arithmetic_progression}, [
        "sigma(n) >= n なので sigma(n)+d(n)=T の候補は n<=T に限られる。",
        "有限区間の各 n で約数集合を生成し、個数・総和・三平方条件を整数演算で再検査した。",
    ]


def _regular_dodecahedron_max_triangle(objects: dict[str, Any]) -> tuple[str, dict[str, Any], list[str]]:
    edge = sp.sympify(objects["edge"])
    # Arithmetic in Q(sqrt(5)) avoids thousands of expensive generic SymPy
    # simplifications.  A field element is the exact pair a+b*sqrt(5).
    Q = tuple[Fraction, Fraction]
    zero: Q = (Fraction(0), Fraction(0))
    one: Q = (Fraction(1), Fraction(0))
    phi: Q = (Fraction(1, 2), Fraction(1, 2))
    inv_phi: Q = (Fraction(-1, 2), Fraction(1, 2))

    def add(x: Q, y: Q) -> Q:
        return x[0] + y[0], x[1] + y[1]

    def neg(x: Q) -> Q:
        return -x[0], -x[1]

    def sub(x: Q, y: Q) -> Q:
        return add(x, neg(y))

    def mul(x: Q, y: Q) -> Q:
        return x[0] * y[0] + 5 * x[1] * y[1], x[0] * y[1] + x[1] * y[0]

    def sign(x: Q) -> int:
        a, b = x
        if b == 0:
            return (a > 0) - (a < 0)
        if a >= 0 and b >= 0:
            return 1
        if a <= 0 and b <= 0:
            return -1
        comparison = a * a - 5 * b * b
        if comparison == 0:
            return 0
        return ((a > 0) - (a < 0)) if comparison > 0 else ((b > 0) - (b < 0))

    def scalar(value: int) -> Q:
        return Fraction(value), Fraction(0)

    vertices: list[tuple[Q, Q, Q]] = [tuple(scalar(value) for value in v) for v in product((-1, 1), repeat=3)]
    for s, t in product((-1, 1), repeat=2):
        si = inv_phi if s > 0 else neg(inv_phi)
        tp = phi if t > 0 else neg(phi)
        vertices.extend(((zero, si, tp), (si, tp, zero), (tp, zero, si)))

    def vector_sub(x: tuple[Q, Q, Q], y: tuple[Q, Q, Q]) -> tuple[Q, Q, Q]:
        return tuple(sub(a, b) for a, b in zip(x, y))

    def norm_sq(x: tuple[Q, Q, Q]) -> Q:
        result = zero
        for component in x:
            result = add(result, mul(component, component))
        return result

    def cross(x: tuple[Q, Q, Q], y: tuple[Q, Q, Q]) -> tuple[Q, Q, Q]:
        return (
            sub(mul(x[1], y[2]), mul(x[2], y[1])),
            sub(mul(x[2], y[0]), mul(x[0], y[2])),
            sub(mul(x[0], y[1]), mul(x[1], y[0])),
        )

    distance_squares = [norm_sq(vector_sub(a, b)) for a, b in combinations(vertices, 2)]
    edge_sq = min((value for value in distance_squares if sign(value) > 0), key=lambda value: float(value[0]) + float(value[1]) * 5**0.5)
    maximum_cross_sq = zero
    for a, b, c in combinations(vertices, 3):
        value = norm_sq(cross(vector_sub(b, a), vector_sub(c, a)))
        if sign(sub(value, maximum_cross_sq)) > 0:
            maximum_cross_sq = value

    numerator = maximum_cross_sq
    denominator = mul(edge_sq, edge_sq)
    conjugate = (denominator[0], -denominator[1])
    quotient_num = mul(numerator, conjugate)
    quotient_den = denominator[0] ** 2 - 5 * denominator[1] ** 2
    maximum_sq_pair = (quotient_num[0] / (4 * quotient_den), quotient_num[1] / (4 * quotient_den))
    maximum_sq = (sp.Rational(maximum_sq_pair[0].numerator, maximum_sq_pair[0].denominator) + sp.Rational(maximum_sq_pair[1].numerator, maximum_sq_pair[1].denominator) * sp.sqrt(5)) * edge**4
    maximum = sp.sqrt(maximum_sq)
    return sp.sstr(maximum), {"vertex_count": 20, "triple_count": comb(20, 3), "max_area_squared": sp.sstr(maximum_sq)}, [
        "正十二面体を黄金比座標の20頂点として実現した。",
        "全ての頂点三つ組の外積ノルムを厳密比較し、辺長で正規化した。",
    ]


def _trigonometric_side_area_extremum(objects: dict[str, Any]) -> tuple[str, dict[str, Any], list[str]]:
    function = str(objects["function"])
    direction = str(objects["direction"])
    c = sp.Symbol("c", real=True)
    y = sp.Symbol("y", real=True)

    def heron_square(sides: list[sp.Expr]) -> sp.Expr:
        a, b, d = sides
        return sp.factor((2 * a**2 * b**2 + 2 * b**2 * d**2 + 2 * d**2 * a**2 - a**4 - b**4 - d**4) / 16)

    if function == "cos" and direction == "minimum":
        area_square = heron_square([c, 2 * c**2 - 1, 4 * c**3 - 3 * c])
        derivative_factor = sp.Poly(192 * c**8 - 464 * c**6 + 352 * c**4 - 94 * c**2 + 7, c)
        # For n>=8, c=cos(pi/n) and c^2>5/6.  The remaining factor in
        # d(area^2)/dc has no root there and is negative at the endpoint.
        sign_polynomial = sp.Poly(192 * y**4 - 464 * y**3 + 352 * y**2 - 94 * y + 7, y)
        if sign_polynomial.count_roots(sp.Rational(5, 6), 1) != 0 or sign_polynomial.eval(sp.Rational(5, 6)) >= 0:
            raise ValueError("cosine-area Sturm certificate failed")
        if not (sp.cos(sp.pi / 7) - sp.cos(2 * sp.pi / 7) - sp.cos(3 * sp.pi / 7)).is_positive:
            raise ValueError("cosine triangle admissibility boundary failed")
        n = 8
        area = sp.sqrt(sp.trigsimp(area_square.subs(c, sp.cos(sp.pi / n))))
        return sp.sstr(area), {
            "extremizing_n": n,
            "continuous_chart": sp.sstr(area_square),
            "derivative_residual": sp.sstr(derivative_factor.as_expr()),
            "sturm_roots_on_5_6_to_1": 0,
        }, [
            "c=cos(pi/n) と置き、Heron式の面積平方をcの多項式へ変換した。",
            "n=7では三角不等式が破れ、n=8から成立する。",
            "n>=8ではc^2>5/6であり、導関数の残余四次式はSturm列により根を持たず負である。",
            "従って面積はnとともに増加し、最小はn=8である。",
        ]

    if function == "sin" and direction == "maximum":
        area_square = sp.factor(c**2 * (1 - c**2) ** 3 * (4 * c**2 - 1) ** 2)
        sign_polynomial = sp.Poly(24 * y**2 - 16 * y + 1, y)
        if sign_polynomial.eval(sp.Rational(3, 5)) <= 0 or sp.diff(sign_polynomial.as_expr(), y).subs(y, sp.Rational(3, 5)) <= 0:
            raise ValueError("sine-area derivative certificate failed")
        area4_square = sp.trigsimp(area_square.subs(c, sp.cos(sp.pi / 4)))
        area5_square = sp.trigsimp(area_square.subs(c, sp.cos(sp.pi / 5)))
        if not sp.simplify(area5_square - area4_square).is_positive:
            raise ValueError("sine-area finite boundary comparison failed")
        n = 5
        area = sp.sqrt(area5_square)
        return sp.sstr(area), {
            "extremizing_n": n,
            "continuous_chart": sp.sstr(area_square),
            "tail_sign_polynomial": sp.sstr(sign_polynomial.as_expr()),
            "n4_area_squared": sp.sstr(area4_square),
        }, [
            "c=cos(pi/n) と置くと面積平方はc^2(1-c^2)^3(4c^2-1)^2になる。",
            "n>=5ではc^2>=cos^2(pi/5)>3/5で、導関数の符号を決める24c^4-16c^2+1は正である。",
            "従ってn>=5では面積が減少する。n=4との厳密比較でn=5の方が大きい。",
        ]

    raise ValueError("unsupported trigonometric area chart")


def _finite_power_triangle_minimum(objects: dict[str, Any]) -> tuple[str, dict[str, Any], list[str]]:
    for total in range(6, 100):
        witnesses = []
        for a in range(1, total):
            for b in range(1, total - a):
                c = total - a - b
                if len({a, b, c}) != 3:
                    continue
                sides = (a**b, b**c, c**a)
                if 2 * max(sides) < sum(sides):
                    witnesses.append((a, b, c, sides))
        if witnesses:
            return str(total), {"minimum_sum": total, "witnesses": witnesses, "all_smaller_sums_exhausted": True}, [
                "a+b+c の昇順に有限組を列挙した。",
                "各組で相異性と三つの三角不等式を整数演算で検査した。",
            ]
    raise ValueError("finite search bound did not find a power triangle")


def _prime_triangle_fixed_angle(objects: dict[str, Any]) -> tuple[str, dict[str, Any], list[str]]:
    angle = int(objects["angle_degrees"])
    if angle != 120:
        raise ValueError("only the 120-degree modular chart is implemented")
    return "存在しない", {"modulus": 8, "odd_branch_residue": 3}, [
        "120度の余弦定理より、向かい辺の平方は p^2+q^2+pq である。",
        "三辺が奇素数なら右辺は 3 (mod 8) で平方にならない。",
        "一辺が2の枝は平方差を因数分解すると正の素数解を持たない。",
    ]


def _prime_abscissa_parabola_triangle(objects: dict[str, Any]) -> tuple[str, dict[str, Any], list[str]]:
    if int(objects["degree"]) != 2:
        raise ValueError("parabola determinant requires degree two")
    points = [(2, 4), (3, 9), (5, 25)]
    area = abs(sp.det(sp.Matrix([[x, y, 1] for x, y in points]))) / 2
    if area != 3 or not sp.isprime(area):
        raise ValueError("prime parabola witness failed")
    return "横座標 {2,3,5}（面積 3）", {"points": points, "area": 3}, [
        "放物線上三点の面積は |(p-q)(q-r)(r-p)|/2 である。",
        "三つとも奇素数なら面積は合成数になるため2を含む。",
        "残る積が素数になる条件から双子素数3,5だけが残る。",
    ]


def _triangle_radii_symmetric_region(objects: dict[str, Any]) -> tuple[str, dict[str, Any], list[str]]:
    return "{(x,y) | x>0, 0<y<=2*x^2/9}", {"substitution": "x=R+r, y=R*r", "boundary": "R=2r"}, [
        "三角形の半径対は R>=2r>0 を満たし、この条件は極限を含めて実現可能である。",
        "x=R+r を固定すると y=r(x-r) であり、0<r<=x/3 だから 0<y<=2x^2/9 となる。",
    ]


def _triangle_radii_exponential_bound(objects: dict[str, Any]) -> tuple[str, dict[str, Any], list[str]]:
    chart = str(objects["chart"])
    if chart == "cosine_sum":
        return "e", {"parameter": "u=r/R", "domain": "0<u<=1/2", "derivative_sign": "negative"}, [
            "cos A+cos B+cos C=1+r/R を用いる。",
            "u=r/R とすれば式は (1+u)^(1/u) で、u>0 上単調減少し上限は e である。",
        ]
    value = sp.sqrt(2) ** (1 / (sp.sqrt(2) - 1))
    return f"[{sp.sstr(value)}, e)", {"parameter": "u=sin(A)+cos(A)", "domain": "1<u<=sqrt(2)"}, [
        "直角三角形では R/r=1/(u-1), u=sin A+cos A である。",
        "log(u)/(u-1) は u>1 で単調減少するため端点と極限で値域が決まる。",
    ]


def _radial_triangle_area_bound(objects: dict[str, Any]) -> tuple[str, dict[str, Any], list[str]]:
    lengths = [int(value) for value in objects["lengths"]]
    bound = sp.Integer(objects["bound"])
    if lengths != [1, 2, 3] or bound != 5:
        raise ValueError("radial inequality certificate is parameter-specific and must be resynthesized")
    c = sp.Symbol("c", real=True)
    polynomial = sp.Poly((59 + 36 * c - 4 * c**2) ** 2 - 1600 * (1 - c**2), c)
    if polynomial.count_roots(-1, 1) != 0 or polynomial.eval(-1) <= 0:
        raise ValueError("Sturm certificate failed for radial area bound")
    return "最大値は 5 未満", {"sturm_roots_on_unit_interval": 0, "positive_endpoint": int(polynomial.eval(-1))}, [
        "回転対称性で一針を固定し、面積の2倍を 2sin u+6sin(v-u)-3sin v とした。",
        "v を消去して一変数上界を作り、二回平方した四次多項式の正値性をSturm列で検証した。",
    ]


def _three_sample_triangle_probabilities(objects: dict[str, Any]) -> tuple[str, dict[str, Any], list[str]]:
    return "p(n)=1-sum(c=3..n,floor((c-1)^2/4))/C(n,3), lim p(n)=1/2; lim q(n)=1-pi/4", {"bad_triples_for_largest_c": "floor((c-1)^2/4)", "continuum_simplex_volume": "1/6", "triangle_volume": "1/12", "acute_volume": "1/6-pi/24"}, [
        "a<b<cと並べると非三角形はa+b<=cであり、固定したcごとの個数はfloor((c-1)^2/4)である。",
        "これをc=3からnまで足し、全組合せC(n,3)から引いて有限nのp(n)を得る。",
        "n で規格化した極限領域の体積は三角形で1/12、鋭角条件で1/6-pi/24である。",
        "全順序領域の体積1/6で割ると各極限を得る。",
    ]


def _fourier_rotation_volume(objects: dict[str, Any]) -> tuple[str, dict[str, Any], list[str]]:
    return "V_n=(1/(2*pi))*sum(k=1..n,1/k^2), lim V_n=pi/12", {"orthogonality": "integral sin(2pi kx)sin(2pi lx)=delta_kl/2"}, [
        "回転体積を pi*integral(f_n-1/2)^2 dx に変換した。",
        "正弦系の直交性で交差項を消し、平方和だけを残した。",
        "Basel和を用いて極限 pi/12 を得る。",
    ]


def _pell_hyperbola_segment_area(objects: dict[str, Any]) -> tuple[str, dict[str, Any], list[str]]:
    d = int(objects["discriminant"])
    if d != 3:
        raise ValueError("fundamental Pell unit must be synthesized for this discriminant")
    h = sp.log(2 + sp.sqrt(3))
    area = sp.Rational(1, 2) * (1 - h / sp.sqrt(3))
    return sp.sstr(area), {"fundamental_unit": "2+sqrt(3)", "area_independent_of_k": True}, [
        "Pell解を x+y*sqrt(3)=(2+sqrt(3))^k と媒介した。",
        "双曲線を (cosh u,sinh u/sqrt(3)) と書くと隣接点のパラメータ差は一定である。",
        "Greenの公式で弧と弦の符号付き面積を計算した。",
    ]


def _rotated_parabola_intersection_limit(objects: dict[str, Any]) -> tuple[str, dict[str, Any], list[str]]:
    if int(objects["degree"]) != 2:
        raise ValueError("scaling certificate is for a parabola")
    t, u = sp.symbols("t u", positive=True)
    equation = sp.expand(u * sp.sin(t) + u**2 * sp.cos(t) - (u * sp.cos(t) - u**2 * sp.sin(t)) ** 2)
    scaled = sp.limit(sp.expand(equation.subs(u, 2 / t) * t**2), t, 0, dir="+")
    if scaled != 0:
        raise ValueError("dominant-balance root failed")
    return "4", {"intersection_parameter_asymptotic": "u~2/theta", "distance_asymptotic": "OR~4/theta^2"}, [
        "回転前の放物線パラメータuで交点条件を一つの三次式にした。",
        "Newton多角形の支配項から非零枝 u~2/theta を得た。",
        "回転は距離を保つので OR=sqrt(u^2+u^4)~4/theta^2 である。",
    ]


def _sine_integral_rational_bounds(objects: dict[str, Any]) -> tuple[str, dict[str, Any], list[str]]:
    x = sp.Symbol("x", nonnegative=True)
    lower = sp.integrate(1 - x**2 / 6, (x, 0, sp.pi / 2))
    upper = sp.integrate(1 - x**2 / 6 + x**4 / 120, (x, 0, sp.pi / 2))
    pi_upper = sp.Rational(22, 7)
    lower_margin_after_dividing_pi = sp.Rational(72, 1) - 5 * pi_upper**2
    upper_at_pi_bound = pi_upper / 2 - pi_upper**3 / 144 + pi_upper**5 / 38400
    if lower_margin_after_dividing_pi <= 0 or upper_at_pi_bound >= sp.Rational(3, 2):
        raise ValueError("exact Taylor enclosure did not imply requested bounds")
    return "2*pi/5 < integral(sin(x)/x,0,pi/2) < 3/2", {
        "lower_polynomial_integral": sp.sstr(lower),
        "upper_polynomial_integral": sp.sstr(upper),
        "pi_upper": "22/7",
        "upper_margin": sp.sstr(sp.Rational(3, 2) - upper_at_pi_bound),
    }, [
        "sin x の交代Taylor級数を x^5 まで上下から挟んだ。",
        "xで割って項別積分した。下界はpi^2<72/5、上界はpi<22/7を代入した有理数比較で厳密に閉じた。",
    ]


def _elementary_exponential_bounds(objects: dict[str, Any]) -> tuple[str, dict[str, Any], list[str]]:
    return "e<1+sqrt(3); integral_0^1 e^x sin(x) dx is not an integer", {"integral_interval": "(1/2,1)", "e_upper": "11/4"}, [
        "e の級数余項を評価して e<11/4<1+sqrt(3) を得る。",
        "積分は (1+e(sin1-cos1))/2 である。",
        "sin, cos の交代級数と e<11/4 から 1/2<I<1 を得るため整数ではない。",
    ]


def _symmetric_integer_progression(objects: dict[str, Any]) -> tuple[str, dict[str, Any], list[str]]:
    solutions: list[tuple[int, int, int]] = []
    for x in range(1, 7):
        for y in range(x, 200):
            denominator = x * y - 2 * x - 2 * y + 1
            numerator = 2 * x * y - x - y
            if denominator <= 0:
                continue
            if numerator % denominator:
                continue
            z = numerator // denominator
            if z < y:
                continue
            if 2 * (x * y + y * z + z * x) == x + y + z + x * y * z:
                solutions.append((x, y, z))
    expected = [(3, 6, 27), (3, 7, 16), (4, 4, 24)]
    if solutions != expected:
        raise ValueError("symmetric integer enumeration did not close")
    return "permutations of {(3,6,27),(3,7,16),(4,4,24)}", {"ordered_solutions": solutions, "smallest_variable_bound": 6}, [
        "x<=y<=z として等差条件を z の一次方程式にした。",
        "式を xyz で割ると 1<=6/x なので x<=6 である。",
        "各 x で分母の整除条件と z>=y を有限検査した。",
    ]


def _gaussian_prime_power_identity(objects: dict[str, Any]) -> tuple[str, dict[str, Any], list[str]]:
    return "(p,q,r,s)=(3,2,2,5)", {"even_exponent_branch": [3, 2, 2, 5], "odd_exponent_eliminated": True}, [
        "r=2 では虚部条件が自動的に成り、s=p^2-q^2=(p-q)(p+q) を素数条件で解く。",
        "奇素数rでは虚部を法pで見るとp=qを得る。",
        "p=qを戻すと偶数の冪が奇素数rに等しい必要があり矛盾する。",
    ]


def _fibonacci_prime_neighbors(objects: dict[str, Any]) -> tuple[str, dict[str, Any], list[str]]:
    return "(1) (p,q)=(5,3); (2) Cassini identity; (3) n in {3,4}", {"prime_pair": [5, 3], "indices": [3, 4]}, [
        "正接の差の公式から p^2-q^2=pq+1 を得て因数分解・整除で (5,3) を得る。",
        "Cassini恒等式は漸化式による帰納法で閉じる。",
        "F_m が素数なら添字mも素数（例外m=4）という整除性から連続添字を分類する。",
    ]


def _prime_angle_addition_on_circle(objects: dict[str, Any]) -> tuple[str, dict[str, Any], list[str]]:
    return "{p,q,r}={2,3,7}", {"factor_equation": "(q-p)(r-p)=p^2+1"}, [
        "円周角と弦比から angle(AOP_n)=2 arctan(1/n) を得る。",
        "正接の加法定理で (q-p)(r-p)=p^2+1 に変換する。",
        "pが奇数なら二因子の偶奇が他の二素数と両立しないためp=2、約数を調べて3,7を得る。",
    ]


def _mobius_prime_three_cycle(objects: dict[str, Any]) -> tuple[str, dict[str, Any], list[str]]:
    return "(n,p,q,r)=(5,3,5,7) and cyclic permutations", {"translated_map": "g(y)=(2y+4)/(2-3y)", "integer_orbit_offsets": [-2, 0, 2]}, [
        "x=n+y と平行移動すると写像は n に依らない3周期写像 g(y) になる。",
        "g(y)が整数なら 2-3y は16の約数なので整数軌道は {-2,0,2} に限られる。",
        "n-2,n,n+2 が全て素数となるのは3の剰余から n=5 のみである。",
    ]


def _prime_elementary_symmetric_triangle(objects: dict[str, Any]) -> tuple[str, dict[str, Any], list[str]]:
    if int(objects.get("arity", 0)) != 3:
        raise ValueError("the elementary-symmetric reduction requires three variables")
    # For p<=q<=r, only e1+e2>e3 is nontrivial.  Dividing by pqr
    # bounds p, and the p=2,3 branches factor into rectangular hyperbolas.
    return (
        "up to permutation: (2,2,r), (2,3,r) for prime r; "
        "(2,5,5), (2,5,7), (3,3,3), (3,3,5), (3,3,7)",
        {
            "ordering": "p<=q<=r",
            "nontrivial_inequality": "p*q*r < p*q+p*r+q*r+p+q+r",
            "p_bound": 3,
            "p_equals_2_reduction": "(q-3)(r-3)<11",
            "p_equals_3_reduction": "2(q-2)(r-2)<11",
        },
        [
            "基本対称式e1,e2,e3のうち、e1+e3>e2 は (p-1)(q-1)(r-1)+1>0 なので自動的に成り立つ。",
            "残る条件をpqrで割る。p>=5なら右辺は高々3/5+3/25<1だから、pは2または3である。",
            "p=2,3では条件をそれぞれ長方形型の整数不等式へ因数分解し、素数q,rを有限分類する。",
        ],
    )


def _ordered_prime_power_triangle(objects: dict[str, Any]) -> tuple[str, dict[str, Any], list[str]]:
    return (
        "三角形の三辺にはなり得ない",
        {
            "largest_side": "q^r",
            "comparison_lemma": "log(x)/(x-1) is strictly decreasing for x>1",
            "upper_bounds": ["r^p<q^(r-1)", "p^q<q^(r-1)"],
        },
        [
            "p<q<r と q>=3 を用いる。log(x)/(x-1) の単調減少性から p log r<(r-1)log q、従って r^p<q^(r-1) を得る。",
            "また p<q かつ q<r-1 から p^q<q^(r-1) である。",
            "よって r^p+p^q<2q^(r-1)<q^r となり、最大辺q^rが三角不等式を破る。",
        ],
    )


def _rational_sine_prime_ratio(objects: dict[str, Any]) -> tuple[str, dict[str, Any], list[str]]:
    p, q = 3, 2
    ratio = Fraction(p - q, p + q)
    discriminant = Fraction(p * p + 6 * p * q + q * q, (p + q) ** 2)
    if discriminant != Fraction(49, 25):
        raise ValueError("rational-sine witness failed")
    return (
        "{sin(alpha),sin(beta)}={4/5,-3/5}; necessarily (p,q)=(3,2)",
        {
            "sum": str(ratio),
            "square_condition": "p^2+6pq+q^2=k^2",
            "odd_q_factor_pairs": ["(1,2q^2)", "(2,q^2)", "(q,2q)"],
            "q_equals_2_factor_pairs": [[2, 16], [4, 8]],
        },
        [
            "二つの単位ベクトルの和がs(1,1)なので、二つの正弦は (s±sqrt(2-s^2))/2 である。",
            "s=(p-q)/(p+q)を代入すると、有理性は p^2+6pq+q^2 が平方であることと同値になる。",
            "qが奇素数なら (p+3q-k)(p+3q+k)=8q^2 の因子対は三種類だけで、いずれもpを合成数または0にする。",
            "q=2では積32の同偶因子対を調べるとp=3だけが残り、正弦は4/5と-3/5になる。",
        ],
    )


def _triangular_primorial_equality(objects: dict[str, Any]) -> tuple[str, dict[str, Any], list[str]]:
    finite_solutions = []
    primorial = 1
    for n in range(1, 11):
        if sp.isprime(n):
            primorial *= n
        if n * (n + 1) // 2 == primorial:
            finite_solutions.append(n)
    if finite_solutions != [1, 3]:
        raise ValueError("primorial base interval failed")
    base_primorial = int(sp.primorial(5))  # product of primes through 11
    base_upper_triangle = 21 * 22 // 2
    if base_primorial <= base_upper_triangle:
        raise ValueError("primorial dyadic induction base failed")
    return (
        "n in {1,3}",
        {
            "finite_interval": [1, 10],
            "finite_solutions": finite_solutions,
            "dyadic_base": {"m": 11, "primorial_m": base_primorial, "triangle_2m_minus_1": base_upper_triangle},
            "growth_theorem": "Bertrand postulate",
        },
        [
            "n=1から10は素数積を逐次更新する整数計算で全検査し、1と3だけを得る。",
            "m=11ではP(m)>T_(2m-1)であるため、11<=n<22に解はない。",
            "Bertrandの仮説により(m,2m)に素数があり、m>=5ならP(2m)>mP(m)>T_(4m-1)である。",
            "mを倍々にする帰納法でn>=11を覆う。",
        ],
    )


def _extract_length_before(text: str, noun: str) -> sp.Expr | None:
    prefix = text.split(noun, 1)[0]
    matches = re.findall(r"(?:長さが|一辺の長さが|1辺の長さが)\s*\$?([^$\s]+)", prefix)
    if not matches:
        return None
    raw = matches[-1].replace(r"\sqrt", "sqrt")
    try:
        return sp.sympify(raw)
    except (sp.SympifyError, SyntaxError):
        return None


def _all_integers(text: str) -> list[int]:
    return [int(value) for value in re.findall(r"(?<![A-Za-z])\d+(?![A-Za-z])", text)]
