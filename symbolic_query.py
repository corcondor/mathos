"""Typed symbolic-query IR and exact SymPy execution.

The legacy algebra route treated every relation as ``solve(..., x)``.  This
module keeps the mathematical constraints separate from the requested
observation, so one relation can be mapped to a solution set, a root
aggregate, an extremizer, or an inequality set without problem templates.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field, replace
import re
from typing import Any

import sympy as sp
from sympy.parsing.sympy_parser import (
    convert_xor,
    implicit_multiplication_application,
    parse_expr,
    standard_transformations,
)

try:
    from math_os_prototype.latex_frontend import parse_latex_problem
except ImportError:
    from latex_frontend import parse_latex_problem


@dataclass(frozen=True)
class SymbolicQueryIR:
    constraints: list[str]
    expressions: list[str]
    query_operator: str
    target: str
    variables: list[str]
    output_sort: str
    definitions: dict[str, dict[str, str]] = field(default_factory=dict)
    substitutions: dict[str, str] = field(default_factory=dict)
    parameters: dict[str, Any] = field(default_factory=dict)
    lowering_certificate: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def compile_symbolic_query(text: str) -> SymbolicQueryIR | None:
    parsed = parse_latex_problem(text)
    segments = [clean_math_segment(part) for item in parsed.math_segments for part in split_math_statements(item)]
    segments = [item for item in segments if item]
    lower = parsed.normalized_text.lower()
    definitions = extract_function_definitions(segments)
    constraints = [
        relation
        for item in segments
        if relation_operator(item)
        for relation in expand_chained_relation(item)
    ]
    expressions = [item for item in segments if not relation_operator(item)]
    variables = sorted(extract_symbols(segments) - set(definitions))

    if contains_word(lower, "expand") or "展開" in lower:
        target = last_expression(expressions)
        return build_ir(constraints, expressions, "expand", target, variables, "Expression", definitions)
    factor_request = bool(re.search(r"(?:^|[.!?]\s*)factor(?:\s+the)?\s+(?:following\s+)?(?:expression|polynomial)?", lower))
    japanese_factor_request = bool(
        re.search(r"因数分解\s*(?:せよ|しなさい|してください|すること)", lower)
    ) and not bool(re.search(r"因数分解\s*できることを\s*(?:示せ|証明)", lower))
    if factor_request or japanese_factor_request:
        target = last_expression(expressions)
        return build_ir(constraints, expressions, "factor", target, variables, "Expression", definitions)
    if contains_word(lower, "simplify") or "簡単" in lower:
        target = last_expression(expressions)
        return build_ir(constraints, expressions, "simplify", target, variables, "Expression", definitions)

    function_target = next(
        (item for item in reversed(expressions) if any(function_call_present(item, name) for name in definitions)),
        "",
    )
    unsupported_function_query = any(
        marker in lower
        for marker in ("remainder", "divided by", "inverse", "^{-1}", "polynomial of degree", "roots of", "余り", "割")
    )
    if definitions and function_target and query_requests_value(lower) and not unsupported_function_query:
        return build_ir(
            constraints,
            expressions,
            "evaluate_defined_expression",
            function_target,
            variables,
            "Expression",
            definitions,
        )

    equation = next((item for item in constraints if equation_operator(item)), "")
    inequalities = [item for item in constraints if inequality_operator(item)]
    inequality = inequalities[0] if inequalities else ""
    equations = [item for item in constraints if equation_operator(item)]
    if len(equations) > 1:
        target = expression_requested_by_query(lower, expressions)
        if target and query_requests_value(lower):
            compiled = build_ir(
                constraints,
                expressions,
                "solve_system_evaluate",
                target,
                sorted(extract_symbols(equations)),
                "Scalar",
                definitions,
            )
            if compiled is not None:
                return replace(
                    compiled,
                    lowering_certificate={
                        "kind": "constraint_system_observation",
                        "constraint_count": len(equations),
                        "observation": "evaluate target under the unique satisfying assignment",
                    },
                )
        return None

    rounding_operator = None
    if "greatest integer less than or equal" in lower or "floor" in lower or "床関数" in lower:
        rounding_operator = "floor_value"
    elif "least integer greater than or equal" in lower or "ceiling" in lower or "天井関数" in lower:
        rounding_operator = "ceiling_value"
    if not constraints and rounding_operator and expressions:
        target = expressions[-1]
        if is_closed_scalar_term(target):
            compiled = build_ir(constraints, expressions, rounding_operator, target, [], "Integer", definitions)
            if compiled is not None:
                return replace(
                    compiled,
                    lowering_certificate={
                        "kind": "ordered_integer_projection",
                        "constraint_count": 0,
                        "observation": rounding_operator,
                    },
                )

    closed_projection: tuple[str, str] | None = None
    if "nearest integer" in lower or "最も近い整数" in lower:
        closed_projection = ("nearest_integer_value", "Integer")
    elif "positive square root" in lower or "正の平方根" in lower:
        closed_projection = ("positive_square_root", "Real")
    elif "units digit" in lower or "ones digit" in lower or "一の位" in lower:
        closed_projection = ("units_digit", "Integer")
    if not constraints and closed_projection and expressions:
        target = expressions[-1]
        if is_closed_scalar_term(target):
            operator, output_sort = closed_projection
            compiled = build_ir(constraints, expressions, operator, target, [], output_sort, definitions)
            if compiled is not None:
                return replace(
                    compiled,
                    lowering_certificate={
                        "kind": "closed_term_projection",
                        "constraint_count": 0,
                        "observation": operator,
                    },
                )
    query_variable = infer_query_variable(lower, variables, equation or inequality)

    named_roots = extract_named_roots(lower)
    symmetric_target = next(
        (
            item
            for item in reversed(expressions)
            if named_roots and all(re.search(rf"\b{re.escape(name)}\b", item) for name in named_roots)
        ),
        "",
    )
    if equation and named_roots and symmetric_target:
        compiled = build_ir(
            constraints,
            expressions,
            "symmetric_root_expression",
            symmetric_target,
            [infer_symbol(equation) or "x"],
            "Scalar",
            definitions,
        )
        if compiled is not None:
            return replace(compiled, parameters={"equation": equation, "root_symbols": named_roots})

    qualified_root_subset = any(
        marker in lower for marker in ("positive real", "negative real", "real part", "imaginary part", "inside", "outside")
    )
    if equation and root_aggregate_query(lower) and not qualified_root_subset:
        operator, output_sort = root_aggregate_query(lower)
        return build_ir(constraints, expressions, operator, equation, [query_variable], output_sort, definitions)

    extremum_expression = expression_for_extremum(lower, expressions)
    if extremum_expression:
        operator = "argmin" if asks_for_extremizer(lower) else "minimum_value"
        if any(word in lower for word in ("maximum", "maximal")) or "最大" in lower:
            operator = "argmax" if asks_for_extremizer(lower) else "maximum_value"
        return build_ir(
            constraints,
            expressions,
            operator,
            extremum_expression,
            [query_variable],
            "Scalar",
            definitions,
        )

    if inequality and query_requests_solution_set(lower):
        return build_ir(
            constraints,
            expressions,
            "solve_inequality",
            " and ".join(inequalities),
            [query_variable],
            "Set",
            definitions,
        )

    excluded_solve_observation = any(
        marker in lower for marker in ("asymptote", "radius", "area", "volume", "distance", "remainder", "|z|", "modulus")
    )
    if equation and query_requests_solution(lower) and not excluded_solve_observation:
        compiled = build_ir(constraints, expressions, "solve", equation, [query_variable], "Set", definitions)
        if compiled is None:
            return None
        return replace(
            compiled,
            substitutions=extract_known_solution_substitution(lower, expressions, equation, query_variable),
        )
    non_scalar_observations = (
        "area", "volume", "radius", "locus", "envelope", "limit", "integral",
        "remainder", "probability", "correlation", "prove", "show that",
        "面積", "体積", "半径", "軌跡", "包絡線", "極限", "積分", "余り", "確率", "相関", "証明", "示せ",
    )
    if (
        not constraints
        and expressions
        and directly_requests_closed_term(lower, expression_requested_by_query(lower, expressions))
        and not any(marker in lower for marker in non_scalar_observations)
    ):
        target = expression_requested_by_query(lower, expressions)
        if target and is_closed_scalar_term(target):
            return replace(
                build_ir(constraints, expressions, "evaluate_expression", target, [], "Scalar", definitions),
                lowering_certificate={
                    "kind": "closed_term_evaluation",
                    "constraint_count": 0,
                    "observation": "normalize and evaluate a closed mathematical term",
                },
            )
    return None


def directly_requests_closed_term(text: str, target: str) -> bool:
    """Require a syntactic dependency from the query operator to its term.

    A closed number appearing in a word problem is data, not automatically the
    requested observation. This elaboration gate prevents a generic CAS
    evaluator from answering an unrelated number found in the statement.
    """
    if not target:
        return False
    escaped = re.escape(target)
    boundary = r"(?=\s|[.!?]|$)"
    english = rf"(?:evaluate|compute|calculate)(?:\s+the)?(?:\s+value\s+of)?\s+{escaped}{boundary}"
    value_question = rf"what\s+is\s+the\s+value\s+of\s+{escaped}{boundary}"
    japanese = rf"{escaped}\s*(?:を)?\s*計算"
    return bool(re.search(english, text) or re.search(value_question, text) or re.search(japanese, text))


def execute_symbolic_query(payload: dict[str, Any]) -> dict[str, Any]:
    ir = SymbolicQueryIR(**payload)
    locals_map = sympy_locals(ir)
    variable_name = ir.variables[0] if ir.variables else "x"
    variable = locals_map.setdefault(variable_name, sp.Symbol(variable_name, real=True))
    operator = ir.query_operator

    if operator in {"expand", "factor", "simplify"}:
        expression = parse_expression(ir.target, locals_map)
        result = {
            "expand": sp.expand,
            "factor": sp.factor,
            "simplify": sp.simplify,
        }[operator](expression)
    elif operator == "evaluate_expression":
        expression = parse_expression(ir.target, locals_map)
        if expression.free_symbols:
            raise ValueError("closed-term evaluation contains unbound symbols")
        result = sp.simplify(expression)
    elif operator in {"floor_value", "ceiling_value", "nearest_integer_value", "positive_square_root", "units_digit"}:
        expression = parse_expression(ir.target, locals_map)
        if expression.free_symbols:
            raise ValueError("integer projection contains unbound symbols")
        if operator == "floor_value":
            result = sp.floor(expression)
        elif operator == "ceiling_value":
            result = sp.ceiling(expression)
        elif operator == "nearest_integer_value":
            result = sp.floor(expression + sp.Rational(1, 2))
        elif operator == "positive_square_root":
            result = sp.sqrt(expression)
        else:
            if expression.is_integer is not True:
                raise ValueError("units-digit projection requires an integer term")
            result = sp.Mod(expression, 10)
    elif operator == "solve_system_evaluate":
        equations = [parse_relation(item, locals_map) for item in ir.constraints if equation_operator(item)]
        variables = sorted(
            set().union(*(equation.free_symbols for equation in equations)),
            key=lambda item: item.name,
        )
        target = parse_expression(ir.target, locals_map)
        if not target.free_symbols <= set(variables):
            raise ValueError("target contains symbols not declared by the constraint system")
        solutions = sp.solve(equations, variables, dict=True)
        if not solutions:
            raise ValueError("constraint system has no finite symbolic solutions")
        observed: list[sp.Expr] = []
        for assignment in solutions:
            if any(variable not in assignment for variable in target.free_symbols):
                raise ValueError("constraint system leaves the requested observation underdetermined")
            if not all(sp.simplify(equation.lhs.subs(assignment) - equation.rhs.subs(assignment)) == 0 for equation in equations):
                raise ValueError("backend assignment failed constraint re-verification")
            value = sp.simplify(target.subs(assignment))
            if value.free_symbols:
                raise ValueError("observed value still contains unbound symbols")
            observed.append(value)
        result = observed[0]
        if any(sp.simplify(value - result) != 0 for value in observed[1:]):
            raise ValueError("constraint system does not determine a unique observation")
    elif operator == "evaluate_defined_expression":
        result = evaluate_defined_expression(ir.target, ir.definitions, locals_map)
        result = sp.expand(result)
        if result.free_symbols:
            raise ValueError("defined-expression observation contains unbound symbols")
    elif operator in {"root_sum", "root_product", "root_square_product"}:
        polynomial = polynomial_from_equation(ir.target, variable, locals_map)
        degree = polynomial.degree()
        if operator == "root_sum":
            result = -polynomial.all_coeffs()[1] / polynomial.all_coeffs()[0]
        else:
            root_product = (-1) ** degree * polynomial.all_coeffs()[-1] / polynomial.all_coeffs()[0]
            result = root_product if operator == "root_product" else sp.expand(root_product**2)
    elif operator == "symmetric_root_expression":
        equation = str(ir.parameters.get("equation") or "")
        root_names = [str(item) for item in ir.parameters.get("root_symbols", [])]
        polynomial = polynomial_from_equation(equation, variable, locals_map)
        if polynomial.degree() != len(root_names) or not root_names:
            raise ValueError("named roots do not match the polynomial degree")
        roots = [sp.Symbol(name) for name in root_names]
        target_locals = {**locals_map, **dict(zip(root_names, roots))}
        target = parse_expression(ir.target, target_locals)
        symmetric, remainder, mapping = sp.symmetrize(target, roots, formal=True)
        if remainder != 0:
            raise ValueError("requested root expression is not symmetric")
        coefficients = polynomial.all_coeffs()
        substitutions = {
            generator: (-1) ** index * coefficients[index] / coefficients[0]
            for index, (generator, _) in enumerate(mapping, start=1)
        }
        result = sp.simplify(symmetric.subs(substitutions))
    elif operator == "solve":
        relation = parse_relation(ir.target, locals_map)
        for name, value in ir.substitutions.items():
            symbol = locals_map.setdefault(name, sp.Symbol(name, real=True))
            relation = relation.subs(symbol, parse_expression(value, locals_map))
        solutions = sp.solve(relation, variable)
        if any(getattr(solution, "free_symbols", set()) for solution in solutions):
            raise ValueError("solution still contains an unbound symbol")
        if len(solutions) == 1:
            return result_payload(ir, solutions[0], expression=ir.target)
        return result_payload(ir, solutions, expression=ir.target)
    elif operator == "solve_inequality":
        relation_sources = [item for item in ir.constraints if inequality_operator(item)]
        if not relation_sources:
            raise ValueError("inequality query has no order constraints")
        solution_sets = [
            sp.solve_univariate_inequality(parse_relation(item, locals_map), variable, relational=False)
            for item in relation_sources
        ]
        result = sp.Intersection(*solution_sets)
    elif operator in {"argmin", "minimum_value", "argmax", "maximum_value"}:
        expression = parse_expression(ir.target, locals_map)
        result = solve_polynomial_extremum(expression, variable, operator)
    else:
        raise ValueError(f"unsupported symbolic query operator: {operator}")
    return result_payload(ir, result, expression=ir.target)


def build_ir(
    constraints: list[str],
    expressions: list[str],
    operator: str,
    target: str,
    variables: list[str],
    output_sort: str,
    definitions: dict[str, dict[str, str]],
) -> SymbolicQueryIR | None:
    if not target:
        return None
    return SymbolicQueryIR(
        constraints=constraints,
        expressions=expressions,
        query_operator=operator,
        target=target,
        variables=variables or [infer_symbol(target) or "x"],
        output_sort=output_sort,
        definitions=definitions,
    )


def result_payload(ir: SymbolicQueryIR, result: Any, *, expression: str) -> dict[str, Any]:
    if isinstance(result, (list, tuple, set)):
        answer = [sp.sstr(item) for item in result]
    else:
        answer = sp.sstr(result)
    return {
        "answer_exact": answer,
        "query_operator": ir.query_operator,
        "output_sort": ir.output_sort,
        "expression": expression,
        "constraint_count": len(ir.constraints),
        "verified": True,
    }


def solve_polynomial_extremum(expression: sp.Expr, variable: sp.Symbol, operator: str) -> sp.Expr:
    polynomial = sp.Poly(expression, variable)
    if polynomial.degree() != 2:
        raise ValueError("the exact extremum backend currently requires a univariate quadratic")
    a, b, _ = polynomial.all_coeffs()
    extremizer = sp.cancel(-b / (2 * a))
    is_minimum = sp.ask(sp.Q.positive(a)) is True
    if operator in {"argmin", "minimum_value"} and not is_minimum:
        raise ValueError("quadratic has no global minimum")
    if operator in {"argmax", "maximum_value"} and is_minimum:
        raise ValueError("quadratic has no global maximum")
    return extremizer if operator.startswith("arg") else sp.simplify(expression.subs(variable, extremizer))


def polynomial_from_equation(source: str, variable: sp.Symbol, locals_map: dict[str, Any]) -> sp.Poly:
    relation = parse_relation(source, locals_map)
    expression = sp.together(relation.lhs - relation.rhs)
    numerator, _ = expression.as_numer_denom()
    return sp.Poly(sp.expand(numerator), variable)


def parse_relation(source: str, locals_map: dict[str, Any]) -> Any:
    for token, constructor in (("<=", sp.Le), (">=", sp.Ge), ("!=", sp.Ne), ("=", sp.Eq), ("<", sp.Lt), (">", sp.Gt)):
        if token in source:
            left, right = source.split(token, 1)
            return constructor(parse_expression(left, locals_map), parse_expression(right, locals_map))
    raise ValueError("no relation operator")


def parse_expression(source: str, locals_map: dict[str, Any]) -> sp.Expr:
    cleaned = re.sub(r"\b(?:If|Let|Find|Solve|What|For)\b.*?(?=[A-Za-z0-9_(])", "", source).strip(" .,?:")
    return parse_expr(
        cleaned,
        local_dict=locals_map,
        transformations=standard_transformations + (convert_xor, implicit_multiplication_application),
        evaluate=True,
    )


def evaluate_defined_expression(
    source: str,
    definitions: dict[str, dict[str, str]],
    locals_map: dict[str, Any],
) -> sp.Expr:
    expanded = source
    for name, definition in definitions.items():
        pattern = rf"\b{re.escape(name)}\*?\(([^()]*)\)"
        while re.search(pattern, expanded):
            match = re.search(pattern, expanded)
            assert match is not None
            argument = parse_expression(match.group(1), locals_map)
            formal = locals_map.setdefault(definition["variable"], sp.Symbol(definition["variable"]))
            body = parse_expression(definition["expression"], locals_map).subs(formal, argument)
            expanded = expanded[: match.start()] + f"({sp.sstr(body)})" + expanded[match.end() :]
    return parse_expression(expanded, locals_map)


def extract_function_definitions(segments: list[str]) -> dict[str, dict[str, str]]:
    definitions: dict[str, dict[str, str]] = {}
    for segment in segments:
        match = re.fullmatch(r"\s*([A-Za-z])\*?\(([A-Za-z])\)\s*=\s*(.+)", segment)
        if match:
            definitions[match.group(1)] = {"variable": match.group(2), "expression": match.group(3)}
    return definitions


def sympy_locals(ir: SymbolicQueryIR) -> dict[str, Any]:
    names = extract_symbols([*ir.constraints, *ir.expressions, ir.target]) | set(ir.variables)
    locals_map: dict[str, Any] = {name: sp.Symbol(name, real=True) for name in names if name not in ir.definitions}
    locals_map.update({"sqrt": sp.sqrt, "sin": sp.sin, "cos": sp.cos, "tan": sp.tan, "log": sp.log, "exp": sp.exp, "I": sp.I, "i": sp.I, "pi": sp.pi})
    return locals_map


def clean_math_segment(source: str) -> str:
    return source.strip().strip(".,;:?")


def split_math_statements(source: str) -> list[str]:
    return [part.strip() for part in re.split(r"\s*;\s*", source) if part.strip()]


def expression_requested_by_query(lower: str, expressions: list[str]) -> str:
    if not expressions:
        return ""
    # Display order is significant: in ``Determine T if C1,...,Cn`` the
    # observation precedes the constraints, while in ``compute T`` it is the
    # last (and usually only) non-relational span.
    if any(marker in lower for marker in ("determine", "求め", "値")):
        return expressions[0]
    return expressions[-1]


def is_closed_scalar_term(source: str) -> bool:
    names = extract_symbols([source])
    if names - {"i"}:
        return False
    try:
        expression = parse_expression(source, {"i": sp.I, "I": sp.I, "pi": sp.pi})
    except Exception:
        return False
    return not expression.free_symbols and not isinstance(expression, (sp.MatrixBase, sp.Set))


def extract_symbols(sources: list[str]) -> set[str]:
    ignored = {"sqrt", "sin", "cos", "tan", "log", "exp", "infinity"}
    return {name for source in sources for name in re.findall(r"\b[A-Za-z]\b", source) if name not in ignored}


def infer_symbol(source: str) -> str | None:
    names = extract_symbols([source])
    return sorted(names)[0] if names else None


def infer_query_variable(text: str, variables: list[str], source: str) -> str:
    match = re.search(r"(?:value|values)\s+of\s+([a-z])|solve\s+for\s+([a-z])", text)
    if match:
        return next(group for group in match.groups() if group)
    names = sorted(extract_symbols([source]))
    return names[0] if names else (variables[0] if variables else "x")


def last_expression(expressions: list[str]) -> str:
    return expressions[-1] if expressions else ""


def relation_operator(source: str) -> str | None:
    match = re.search(r"<=|>=|!=|=|<|>", source)
    return match.group(0) if match else None


def expand_chained_relation(source: str) -> list[str]:
    match = re.fullmatch(r"\s*(.+?)\s*(<=|>=|<|>)\s*(.+?)\s*(<=|>=|<|>)\s*(.+?)\s*", source)
    if not match:
        return [source]
    left, first_operator, middle, second_operator, right = match.groups()
    return [
        f"{left.strip()}{first_operator}{middle.strip()}",
        f"{middle.strip()}{second_operator}{right.strip()}",
    ]


def equation_operator(source: str) -> bool:
    return relation_operator(source) == "="


def inequality_operator(source: str) -> bool:
    return relation_operator(source) in {"<", ">", "<=", ">="}


def contains_word(text: str, word: str) -> bool:
    return bool(re.search(rf"\b{re.escape(word)}\b", text))


def query_requests_value(text: str) -> bool:
    return any(
        phrase in text
        for phrase in ("find", "what is", "evaluate", "compute", "calculate", "determine", "value", "求め", "計算")
    )


def query_requests_solution(text: str) -> bool:
    return any(phrase in text for phrase in ("solve", "possible values", "solutions", "value of", "values of", "解け")) or (
        "方程式" in text and "求め" in text
    )


def query_requests_solution_set(text: str) -> bool:
    return any(phrase in text for phrase in ("what values", "for what", "interval notation", "all real", "範囲", "すべて"))


def root_aggregate_query(text: str) -> tuple[str, str] | None:
    if re.search(r"product of (?:the )?squares of (?:the )?(?:solutions|roots)", text):
        return "root_square_product", "Scalar"
    if re.search(
        r"sum of (?:all )?(?:the )?(?:(?:real|complex|distinct|possible)\s+)*(?:solutions|roots|values)",
        text,
    ):
        return "root_sum", "Scalar"
    if re.search(r"product of (?:all )?(?:the )?(?:solutions|roots)", text):
        return "root_product", "Scalar"
    return None


def expression_for_extremum(text: str, expressions: list[str]) -> str:
    if not any(word in text for word in ("minimum", "maximum", "minimize", "maximize", "最小", "最大")):
        return ""
    candidates = [item for item in expressions if re.search(r"[A-Za-z]", item) and any(op in item for op in ("+", "-", "*", "**", "/"))]
    return candidates[-1] if candidates else ""


def asks_for_extremizer(text: str) -> bool:
    return bool(re.search(r"what\s+(?:value|number)\s+of\s+[a-z]|which\s+[a-z]|[a-z]\s*の値", text))


def function_call_present(source: str, name: str) -> bool:
    return bool(re.search(rf"\b{re.escape(name)}\*?\(", source))


def extract_named_roots(text: str) -> list[str]:
    match = re.search(
        r"\b([a-z])\s*(?:,|and)\s*([a-z])\s+(?:are|be)\s+(?:the\s+)?(?:solutions|roots)",
        text,
    )
    return [match.group(1), match.group(2)] if match else []


def extract_known_solution_substitution(
    text: str,
    expressions: list[str],
    equation: str,
    query_variable: str,
) -> dict[str, str]:
    if not any(phrase in text for phrase in ("is a solution", "is a root", "を解にもつ", "が解")):
        return {}
    equation_variables = sorted(extract_symbols([equation]) - {query_variable})
    constants = [item for item in expressions if re.fullmatch(r"[+-]?\d+(?:/\d+)?", item)]
    if len(equation_variables) != 1 or not constants:
        return {}
    return {equation_variables[0]: constants[0]}
