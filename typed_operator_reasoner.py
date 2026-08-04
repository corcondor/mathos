"""Executable semantics for reusable typed arithmetic operators.

This module parses operator applications and constraints.  It does not select
finished problem families or use benchmark identifiers.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from fractions import Fraction
from math import ceil, floor, gcd

try:
    import sympy as sp
except ImportError:  # pragma: no cover
    sp = None


@dataclass(frozen=True)
class TypedOperatorResult:
    operator: str
    input_sorts: tuple[str, ...]
    output_sort: str
    constraint: str
    answer_exact: str
    certificate: tuple[str, ...]


NUMBER_WORDS = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
    "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
    "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18,
    "nineteen": 19, "twenty": 20,
}


def format_fraction(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def _replace_simple_fractions(text: str) -> str:
    pattern = re.compile(r"\\(?:dfrac|frac)\s*\{([^{}]+)\}\s*\{([^{}]+)\}")
    previous = None
    while previous != text:
        previous = text
        text = pattern.sub(r"((\1)/(\2))", text)
    return text


def normalize_operator_text(text: str) -> str:
    text = text.lower().replace("−", "-").replace("＝", "=")
    text = _replace_simple_fractions(text)
    text = re.sub(r"\\mathop\s*\{\s*\\text\s*\{\s*(gcd|lcm)\s*\}\s*\}", r"\1", text)
    text = re.sub(r"\\(?:operatorname|mathrm|text)\s*\{\s*(gcd|lcm)\s*\}", r"\1", text)
    text = re.sub(r"\\(gcd|lcm)\b", r"\1", text)
    text = re.sub(r"\\lceil\s*([^\\]+?)\s*\\rceil", r"ceil(\1)", text)
    text = re.sub(r"\\lfloor\s*([^\\]+?)\s*\\rfloor", r"floor(\1)", text)
    text = text.replace("最大公約数", "gcd").replace("最小公倍数", "lcm")
    text = text.replace("least common multiple", "lcm").replace("greatest common divisor", "gcd")
    text = text.replace("\n", " ").replace("$", "")
    return re.sub(r"\s+", " ", text).strip()


def solve_gcd_lcm_constraints(text: str) -> TypedOperatorResult | None:
    normalized = normalize_operator_text(text)
    calls: dict[str, tuple[str, int, int]] = {}
    for operator in ("gcd", "lcm"):
        pattern = re.compile(
            rf"{operator}\s*[\(\[]\s*(?P<a>[a-z]\w*|-?\d+)\s*,\s*(?P<b>[a-z]\w*|-?\d+)\s*[\)\]]\s*=\s*(?P<v>-?\d+)"
        )
        match = pattern.search(normalized)
        if not match:
            continue
        left, right = match.group("a"), match.group("b")
        if left.lstrip("-").isdigit() == right.lstrip("-").isdigit():
            continue
        variable = right if left.lstrip("-").isdigit() else left
        constant = int(left if left.lstrip("-").isdigit() else right)
        calls[operator] = (variable, abs(constant), abs(int(match.group("v"))))
    if set(calls) != {"gcd", "lcm"}:
        return None
    gcd_variable, gcd_constant, gcd_value = calls["gcd"]
    lcm_variable, lcm_constant, lcm_value = calls["lcm"]
    if gcd_variable != lcm_variable or gcd_constant != lcm_constant or gcd_constant == 0:
        return None
    numerator = gcd_value * lcm_value
    if numerator % gcd_constant:
        return None
    value = numerator // gcd_constant
    actual_lcm = abs(value * gcd_constant) // gcd(value, gcd_constant) if value else 0
    if gcd(value, gcd_constant) != gcd_value or actual_lcm != lcm_value:
        return None
    return TypedOperatorResult(
        operator="GCDLCMProductLaw",
        input_sorts=("Integer", "Integer"),
        output_sort="Integer",
        constraint=f"gcd({gcd_variable},{gcd_constant})={gcd_value};lcm({gcd_variable},{gcd_constant})={lcm_value}",
        answer_exact=str(value),
        certificate=(
            "gcd(a,b)*lcm(a,b)=abs(a*b)",
            f"gcd({value},{gcd_constant})={gcd_value}",
            f"lcm({value},{gcd_constant})={lcm_value}",
        ),
    )


def solve_finite_lcm_fold(text: str) -> TypedOperatorResult | None:
    normalized = normalize_operator_text(text)
    match = re.search(r"lcm\s+of\s+the\s+first\s+(?P<n>[a-z]+|\d+)\s+positive\s+integers", normalized)
    if not match:
        match = re.search(r"1\s*(?:から|～|~)\s*(?P<n>\d+)\s*まで.*?lcm", normalized)
    if not match:
        return None
    token = match.group("n")
    n = int(token) if token.isdigit() else NUMBER_WORDS.get(token)
    if n is None or not 1 <= n <= 10000:
        return None
    value = 1
    for item in range(1, n + 1):
        value = abs(value * item) // gcd(value, item)
    return TypedOperatorResult(
        operator="FiniteLCMFold",
        input_sorts=("FiniteIntegerFamily",),
        output_sort="Integer",
        constraint=f"lcm(1,...,{n})",
        answer_exact=str(value),
        certificate=("lcm-fold", "prime-power-valuation maximum", f"verified range 1..{n}"),
    )


def _round_fraction(value: Fraction, operator: str) -> int:
    return ceil(value) if operator == "ceil" else floor(value)


def solve_rounding_linear_constraint(text: str) -> TypedOperatorResult | None:
    if sp is None:
        return None
    normalized = normalize_operator_text(text)
    equation = re.search(r"(?P<lhs>[^=]*?(?:ceil|floor)\s*\([^()]+\)[^=]*)=\s*(?P<rhs>.+)", normalized)
    if not equation:
        return None
    function_match = re.search(r"(?P<op>ceil|floor)\s*\(\s*(?P<var>[a-z])\s*\)", equation.group("lhs"))
    if not function_match:
        return None
    operator = function_match.group("op")
    variable_name = function_match.group("var")
    variable, rounded = sp.symbols(f"{variable_name} rounded")
    lhs = re.split(r"such that|satisf(?:y|ies|ying)|を満たす|ならば|:", equation.group("lhs"))[-1].strip()
    lhs = re.sub(rf"{operator}\s*\(\s*{re.escape(variable_name)}\s*\)", "rounded", lhs)
    lhs = re.sub(r"(?<=\d)(?=[a-z])", "*", lhs)
    rhs = equation.group("rhs").strip()
    rhs = re.split(r"(?:express|find|求めよ)", rhs, maxsplit=1)[0].strip()
    rhs = rhs.rstrip(".。、 ")
    try:
        expression = sp.expand(
            sp.sympify(lhs, locals={variable_name: variable, "rounded": rounded})
            - sp.sympify(rhs)
        )
        polynomial = sp.Poly(expression, variable, rounded)
        if polynomial.total_degree() > 1:
            return None
        b = Fraction(str(polynomial.coeff_monomial(variable)))
        a = Fraction(str(polynomial.coeff_monomial(rounded)))
        constant = Fraction(str(polynomial.coeff_monomial(1)))
    except Exception:
        return None
    if b == 0 or a + b == 0:
        return None
    target = -constant
    center = target / (a + b)
    radius = abs(b / (a + b)) + 2
    lower = floor(center - radius)
    upper = ceil(center + radius)
    solutions: list[Fraction] = []
    for integer_value in range(lower, upper + 1):
        x_value = (target - a * integer_value) / b
        if _round_fraction(x_value, operator) == integer_value:
            solutions.append(x_value)
    solutions = sorted(set(solutions))
    if len(solutions) != 1:
        return None
    value = solutions[0]
    return TypedOperatorResult(
        operator="CeilingLinearConstraint" if operator == "ceil" else "FloorLinearConstraint",
        input_sorts=("Real", "LinearConstraint"),
        output_sort="Rational",
        constraint=f"{a}*{operator}({variable_name})+{b}*{variable_name}={target}",
        answer_exact=format_fraction(value),
        certificate=(
            f"k={operator}({variable_name})",
            f"{variable_name}=({target}-{a}k)/{b}",
            f"rounding interval verified exactly for k={_round_fraction(value, operator)}",
        ),
    )


def solve_percent_relation(text: str) -> TypedOperatorResult | None:
    normalized = normalize_operator_text(text).replace(r"\%", "%")
    difference = re.search(
        r"(?:positive\s+)?difference between (?P<p>\d+(?:\.\d+)?)% of (?P<a>\d+(?:\.\d+)?) and (?P<q>\d+(?:\.\d+)?)% of (?P<b>\d+(?:\.\d+)?)",
        normalized,
    )
    if difference:
        p = Fraction(difference.group("p")) / 100
        q = Fraction(difference.group("q")) / 100
        a = Fraction(difference.group("a"))
        b = Fraction(difference.group("b"))
        value = abs(p * a - q * b)
        return TypedOperatorResult(
            operator="PercentScaleDifference",
            input_sorts=("RationalRate", "Quantity", "RationalRate", "Quantity"),
            output_sort="Quantity",
            constraint=f"abs(({p})*{a}-({q})*{b})",
            answer_exact=format_fraction(value),
            certificate=("percent=p/100", "scalar action on quantity", "ordered absolute difference"),
        )
    direct = re.search(r"(?:what is\s+)?(?P<p>\d+(?:\.\d+)?)% of (?P<a>\d+(?:\.\d+)?)", normalized)
    if direct:
        p = Fraction(direct.group("p")) / 100
        a = Fraction(direct.group("a"))
        return TypedOperatorResult(
            operator="PercentScale",
            input_sorts=("RationalRate", "Quantity"),
            output_sort="Quantity",
            constraint=f"({p})*{a}",
            answer_exact=format_fraction(p * a),
            certificate=("percent=p/100", "scalar action on quantity"),
        )
    return None


def solve_typed_operator_problem(text: str) -> TypedOperatorResult | None:
    for solver in (
        solve_gcd_lcm_constraints,
        solve_finite_lcm_fold,
        solve_rounding_linear_constraint,
        solve_percent_relation,
    ):
        result = solver(text)
        if result is not None:
            return result
    return None
