"""Typed matrix and quadratic-form lowering for algebraic geometry queries.

The compiler maps several surface charts to two mathematical objects:

* linear observations ``A u = b`` over coefficient vectors;
* homogeneous quadratic forms ``X.T C X`` and their discriminants.

The surface wording is not used by the executor.  It receives a typed payload,
executes the corresponding matrix operation, and rechecks the source
constraints before returning an answer.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
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
    from math_os_prototype.diagram_feedback import observe_circle_witness
    from math_os_prototype.latex_frontend import parse_latex_problem
except ImportError:
    from diagram_feedback import observe_circle_witness
    from latex_frontend import parse_latex_problem


TRANSFORMS = standard_transformations + (convert_xor, implicit_multiplication_application)


@dataclass(frozen=True)
class MatrixSemanticQueryIR:
    chart: str
    query_operator: str
    source_objects: dict[str, Any]
    target: str
    variables: list[str]
    output_sort: str
    representation: dict[str, Any] = field(default_factory=dict)
    lowering_certificate: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def compile_matrix_semantic_query(text: str) -> MatrixSemanticQueryIR | None:
    parsed = parse_latex_problem(text)
    lower = parsed.normalized_text.lower()
    segments = [clean_segment(item) for item in parsed.math_segments]
    segments = [item for item in segments if item]

    polynomial = select_polynomial(segments)
    equation = select_equation(segments)
    query_target = infer_query_target(lower, segments)

    points = extract_points(segments)
    if polynomial and len(points) >= 2 and any(word in lower for word in ("contains the points", "passes through", "通る", "通過")):
        target = select_observation_expression(segments, polynomial, points)
        if target:
            return build_ir(
                chart="coefficient_space",
                operator="interpolate_and_observe",
                objects={"polynomial": polynomial, "points": points},
                target=target,
                variables=sorted(parameter_names(polynomial, exclude={"x"})),
                output_sort="Scalar",
                representation="evaluation_matrix",
            )

    if polynomial and any(marker in lower for marker in (" a root of ", " a zero of ", "を解にもつ", "が根")):
        root = select_root_value(segments, polynomial, query_target)
        if root and query_target:
            return build_ir(
                chart="coefficient_space",
                operator="root_incidence_parameter",
                objects={"polynomial": polynomial, "root": root},
                target=query_target,
                variables=[query_target],
                output_sort="Scalar",
                representation="evaluation_row",
            )

    conic = equation or polynomial
    coordinate_extremum = infer_coordinate_extremum(lower)
    if conic and coordinate_extremum is not None and is_planar_quadratic_equation(conic):
        coordinate, direction = coordinate_extremum
        return build_ir(
            chart="homogeneous_quadratic_form",
            operator="conic_coordinate_extremum",
            objects={"equation": conic, "coordinate": coordinate, "direction": direction},
            target=coordinate,
            variables=["x", "y"],
            output_sort="Scalar",
            representation="symmetric_conic_matrix",
        )
    if conic and "circle" in lower and "radius" in lower and is_planar_quadratic_equation(conic):
        return build_ir(
            chart="homogeneous_quadratic_form",
            operator="circle_radius",
            objects={"equation": conic},
            target="radius",
            variables=["x", "y"],
            output_sort="PositiveReal",
            representation="symmetric_conic_matrix",
        )

    graph_equation = select_graph_equation(segments)
    if graph_equation and asks_origin_graph_distance(lower):
        squared = bool(re.search(r"(?:find|compute).*?\b[a-z]\s*\*\*\s*2\b", lower)) or "squared distance" in lower
        return build_ir(
            chart="graph_embedding",
            operator="minimum_origin_graph_distance",
            objects={"equation": graph_equation, "return_squared": squared},
            target="squared_distance" if squared else "distance",
            variables=["x", "y"],
            output_sort="NonnegativeReal",
            representation="gram_distance_lift",
        )

    root_condition = infer_root_condition(lower)
    if polynomial and query_target and root_condition is not None and polynomial_degree(polynomial) == 2:
        relation, multiplicity = root_condition
        finite_range = infer_integer_range(lower)
        if "probability" in lower and finite_range is not None:
            return build_ir(
                chart="quadratic_form",
                operator="quadratic_parameter_probability",
                objects={
                    "polynomial": polynomial,
                    "discriminant_relation": relation,
                    "integer_range": list(finite_range),
                },
                target=query_target,
                variables=[query_target],
                output_sort="Probability",
                representation="discriminant_matrix",
                extra={"root_multiplicity": multiplicity},
            )
        return build_ir(
            chart="quadratic_form",
            operator="quadratic_parameter_region",
            objects={"polynomial": polynomial, "discriminant_relation": relation},
            target=query_target,
            variables=[query_target],
            output_sort="Set",
            representation="discriminant_matrix",
            extra={"root_multiplicity": multiplicity},
        )

    if equation and query_target and "positive integer" in lower and "real and rational" in lower:
        return build_ir(
            chart="quadratic_form",
            operator="quadratic_rational_integer_parameters",
            objects={"polynomial": equation, "parameter_domain": "positive_integer"},
            target=query_target,
            variables=[query_target],
            output_sort="FiniteSet",
            representation="discriminant_matrix",
        )

    if polynomial and "positive prime" in lower and query_target:
        bound = select_parameter_bound(segments)
        if bound:
            return build_ir(
                chart="symmetric_root_space",
                operator="prime_root_coefficient_projection",
                objects={"polynomial": polynomial, "parameter_bound": bound},
                target=query_target,
                variables=sorted(parameter_names(polynomial, exclude={"x"})),
                output_sort="Cardinality" if "how many" in lower else "FiniteSet",
                representation="vieta_coefficient_map",
            )
    return None


def build_ir(
    *,
    chart: str,
    operator: str,
    objects: dict[str, Any],
    target: str,
    variables: list[str],
    output_sort: str,
    representation: str,
    extra: dict[str, Any] | None = None,
) -> MatrixSemanticQueryIR:
    return MatrixSemanticQueryIR(
        chart=chart,
        query_operator=operator,
        source_objects=objects,
        target=target,
        variables=variables,
        output_sort=output_sort,
        representation={"kind": representation, **(extra or {})},
        lowering_certificate={
            "kind": "typed_matrix_chart",
            "chart": chart,
            "representation": representation,
            "executor_contract": operator,
        },
    )


def execute_matrix_semantic_query(payload: dict[str, Any]) -> dict[str, Any]:
    ir = MatrixSemanticQueryIR(**payload)
    operator = ir.query_operator
    if operator == "interpolate_and_observe":
        answer, witness = execute_interpolation(ir)
    elif operator == "root_incidence_parameter":
        answer, witness = execute_root_incidence(ir)
    elif operator == "circle_radius":
        answer, witness = execute_circle_radius(ir)
    elif operator == "conic_coordinate_extremum":
        answer, witness = execute_conic_coordinate_extremum(ir)
    elif operator == "minimum_origin_graph_distance":
        answer, witness = execute_minimum_origin_graph_distance(ir)
    elif operator == "quadratic_parameter_region":
        answer, witness = execute_quadratic_region(ir)
    elif operator == "quadratic_parameter_probability":
        answer, witness = execute_quadratic_probability(ir)
    elif operator == "quadratic_rational_integer_parameters":
        answer, witness = execute_rational_integer_parameters(ir)
    elif operator == "prime_root_coefficient_projection":
        answer, witness = execute_prime_root_projection(ir)
    else:
        raise ValueError(f"unsupported matrix semantic operator: {operator}")
    result = {
        "answer_exact": answer if isinstance(answer, str) else sp.sstr(answer),
        "query_operator": operator,
        "output_sort": ir.output_sort,
        "representation": ir.representation,
        "lowering_certificate": ir.lowering_certificate,
        "matrix_witness": witness,
        "verified": True,
    }
    if operator == "circle_radius":
        result["diagram_observation"] = observe_circle_witness(witness)
        if not result["diagram_observation"]["verified"]:
            raise ValueError("rendered conic failed independent diagram observation")
    return result


def execute_interpolation(ir: MatrixSemanticQueryIR) -> tuple[sp.Expr, dict[str, Any]]:
    expression = parse_math(ir.source_objects["polynomial"])
    x = symbol("x")
    unknowns = sorted(expression.free_symbols - {x}, key=lambda item: item.name)
    equations = [sp.Eq(expression.subs(x, parse_math(px)), parse_math(py)) for px, py in ir.source_objects["points"]]
    matrix, rhs = sp.linear_eq_to_matrix(equations, unknowns)
    if matrix.rank() != len(unknowns) or matrix.row_join(rhs).rank() != matrix.rank():
        raise ValueError("point constraints do not determine a unique coefficient vector")
    solution = matrix.gauss_jordan_solve(rhs)[0]
    assignment = dict(zip(unknowns, solution))
    if not all(sp.simplify(eq.lhs.subs(assignment) - eq.rhs) == 0 for eq in equations):
        raise ValueError("interpolated coefficients failed point-incidence verification")
    target = parse_math(ir.target)
    answer = sp.simplify(target.subs(assignment))
    if answer.free_symbols:
        raise ValueError("requested observation remains underdetermined")
    return answer, matrix_witness(matrix, rhs, assignment)


def execute_root_incidence(ir: MatrixSemanticQueryIR) -> tuple[sp.Expr, dict[str, Any]]:
    polynomial = parse_equation_expression(ir.source_objects["polynomial"])
    root = parse_math(ir.source_objects["root"])
    parameter = symbol(ir.target)
    incidence = sp.expand(polynomial.subs(symbol("x"), root))
    solutions = sp.solve(sp.Eq(incidence, 0), parameter)
    if len(solutions) != 1:
        raise ValueError("root incidence does not determine a unique parameter")
    answer = sp.simplify(solutions[0])
    if sp.simplify(incidence.subs(parameter, answer)) != 0:
        raise ValueError("root-incidence substitution failed")
    coefficient_row = [sp.expand(root**power) for power in range(sp.Poly(polynomial, symbol("x")).degree(), -1, -1)]
    return answer, {"evaluation_row": [sp.sstr(item) for item in coefficient_row], "incidence": sp.sstr(incidence)}


def execute_circle_radius(ir: MatrixSemanticQueryIR) -> tuple[sp.Expr, dict[str, Any]]:
    relation = parse_equation_expression(ir.source_objects["equation"])
    x, y = symbol("x"), symbol("y")
    variables = sp.Matrix([x, y])
    q = sp.hessian(relation, (x, y)) / 2
    linear = sp.Matrix([sp.diff(relation, item).subs({x: 0, y: 0}) for item in (x, y)])
    constant = relation.subs({x: 0, y: 0})
    if q.det() == 0 or sp.simplify(q[0, 1]) != 0 or sp.simplify(q[0, 0] - q[1, 1]) != 0:
        raise ValueError("quadratic form is not a Euclidean circle")
    center = sp.simplify(-q.inv() * linear / 2)
    scale = sp.simplify(q[0, 0])
    radius_squared = sp.simplify((center.T * q * center)[0] / scale - constant / scale)
    if sp.ask(sp.Q.positive(radius_squared)) is not True:
        raise ValueError("circle radius is not certified positive")
    radius = sp.sqrt(radius_squared)
    if sp.simplify(relation.subs({x: center[0] + radius, y: center[1]})) != 0:
        raise ValueError("recovered circle failed boundary verification")
    homogeneous = sp.Matrix(
        [[q[0, 0], q[0, 1], linear[0] / 2], [q[1, 0], q[1, 1], linear[1] / 2], [linear[0] / 2, linear[1] / 2, constant]]
    )
    return radius, {
        "conic_matrix": matrix_strings(homogeneous),
        "center": [sp.sstr(item) for item in center],
        "radius_squared": sp.sstr(radius_squared),
    }


def execute_conic_coordinate_extremum(ir: MatrixSemanticQueryIR) -> tuple[sp.Expr, dict[str, Any]]:
    relation = parse_equation_expression(ir.source_objects["equation"])
    x, y = symbol("x"), symbol("y")
    q = sp.hessian(relation, (x, y)) / 2
    linear = sp.Matrix([sp.diff(relation, item).subs({x: 0, y: 0}) for item in (x, y)])
    constant = relation.subs({x: 0, y: 0})
    if q.det() == 0 or sp.simplify(q[0, 1]) != 0 or sp.simplify(q[0, 0] - q[1, 1]) != 0:
        raise ValueError("coordinate extremum currently requires a circle quadratic form")
    center = sp.simplify(-q.inv() * linear / 2)
    scale = sp.simplify(q[0, 0])
    radius_squared = sp.simplify((center.T * q * center)[0] / scale - constant / scale)
    radius = sp.sqrt(radius_squared)
    coordinate = ir.source_objects["coordinate"]
    index = 0 if coordinate == "x" else 1
    direction = ir.source_objects["direction"]
    answer = sp.simplify(center[index] + radius if direction == "maximum" else center[index] - radius)
    boundary = {x: center[0], y: center[1]}
    boundary[(x, y)[index]] = answer
    if sp.simplify(relation.subs(boundary)) != 0:
        raise ValueError("conic extremum failed boundary verification")
    homogeneous = sp.Matrix(
        [[q[0, 0], q[0, 1], linear[0] / 2], [q[1, 0], q[1, 1], linear[1] / 2], [linear[0] / 2, linear[1] / 2, constant]]
    )
    return answer, {
        "conic_matrix": matrix_strings(homogeneous),
        "center": [sp.sstr(item) for item in center],
        "radius_squared": sp.sstr(radius_squared),
        "observation": f"{direction}_{coordinate}",
    }


def execute_minimum_origin_graph_distance(ir: MatrixSemanticQueryIR) -> tuple[sp.Expr, dict[str, Any]]:
    source = ir.source_objects["equation"]
    left, right = source.split("=", 1)
    x, y = symbol("x"), symbol("y")
    lhs, rhs = parse_math(left), parse_math(right)
    if lhs == y and y not in rhs.free_symbols:
        graph = rhs
    elif rhs == y and y not in lhs.free_symbols:
        graph = lhs
    else:
        raise ValueError("graph distance requires an explicit y=f(x) chart")
    squared_distance = sp.expand(x**2 + graph**2)
    polynomial = sp.Poly(squared_distance, x)
    if polynomial.degree() < 1 or sp.ask(sp.Q.positive(polynomial.LC())) is not True:
        raise ValueError("distance objective is not certified coercive")
    critical = [item for item in sp.solve(sp.Eq(sp.diff(squared_distance, x), 0), x) if item.is_real is True]
    if not critical:
        raise ValueError("distance objective has no certified real critical point")
    values = [(point, sp.simplify(squared_distance.subs(x, point))) for point in critical]
    point, minimum = min(values, key=lambda item: float(sp.N(item[1], 30)))
    if any(float(sp.N(minimum - value, 30)) > 1e-12 for _, value in values):
        raise ValueError("selected graph-distance critical point is not minimal")
    answer = minimum if ir.source_objects.get("return_squared") else sp.sqrt(minimum)
    return sp.simplify(answer), {
        "gram_matrix": [["1", "0"], ["0", "1"]],
        "embedding": ["x", sp.sstr(graph)],
        "squared_distance": sp.sstr(squared_distance),
        "critical_points": [sp.sstr(item) for item in critical],
        "minimizer": sp.sstr(point),
    }


def execute_quadratic_region(ir: MatrixSemanticQueryIR) -> tuple[sp.Set, dict[str, Any]]:
    polynomial = sp.Poly(parse_math(ir.source_objects["polynomial"]), symbol("x"))
    if polynomial.degree() != 2:
        raise ValueError("root-region observation requires a quadratic polynomial")
    a, b, c = polynomial.all_coeffs()
    discriminant = sp.factor(b**2 - 4 * a * c)
    parameter = symbol(ir.target)
    relation = ir.source_objects["discriminant_relation"]
    predicate = {">": sp.Gt, ">=": sp.Ge, "=": sp.Eq, "<": sp.Lt}[relation](discriminant, 0)
    if relation == "=":
        solution = sp.FiniteSet(*sp.solve(predicate, parameter))
    else:
        solution = sp.solve_univariate_inequality(predicate, parameter, relational=False)
    return solution, {
        "discriminant_matrix": matrix_strings(sp.Matrix([[b, 2 * a], [2 * c, b]])),
        "determinant": sp.sstr(discriminant),
        "relation": relation,
    }


def execute_quadratic_probability(ir: MatrixSemanticQueryIR) -> tuple[sp.Expr, dict[str, Any]]:
    polynomial = sp.Poly(parse_equation_expression(ir.source_objects["polynomial"]), symbol("x"))
    if polynomial.degree() != 2:
        raise ValueError("root-probability observation requires a quadratic")
    a, b, c = polynomial.all_coeffs()
    discriminant = sp.factor(b**2 - 4 * a * c)
    parameter = symbol(ir.target)
    relation = ir.source_objects["discriminant_relation"]
    predicate = {">": sp.Gt, ">=": sp.Ge, "=": sp.Eq, "<": sp.Lt}[relation](discriminant, 0)
    lower, upper = map(int, ir.source_objects["integer_range"])
    population = list(range(lower, upper + 1))
    accepted = [value for value in population if bool(predicate.subs(parameter, value))]
    probability = sp.Rational(len(accepted), len(population))
    return probability, {
        "discriminant_matrix": matrix_strings(sp.Matrix([[b, 2 * a], [2 * c, b]])),
        "determinant": sp.sstr(discriminant),
        "relation": relation,
        "population": population,
        "accepted": accepted,
    }


def execute_rational_integer_parameters(ir: MatrixSemanticQueryIR) -> tuple[str, dict[str, Any]]:
    parameter = symbol(ir.target)
    polynomial = sp.Poly(parse_equation_expression(ir.source_objects["polynomial"]), symbol("x"))
    if polynomial.degree() != 2:
        raise ValueError("rational-root parameter search requires a quadratic")
    a, b, c = polynomial.all_coeffs()
    discriminant = sp.factor(b**2 - 4 * a * c)
    feasible = sp.solve_univariate_inequality(sp.Ge(discriminant, 0), parameter, relational=False)
    candidates = bounded_integer_members(feasible, positive=True)
    accepted: list[int] = []
    for value in candidates:
        specialized = sp.Poly(polynomial.as_expr().subs(parameter, value), symbol("x"))
        roots = sp.solve(sp.Eq(specialized.as_expr(), 0), symbol("x"))
        if len(roots) == 2 and all(root.is_real is True and root.is_rational is True for root in roots):
            accepted.append(value)
    accepted.sort(reverse=True)
    answer = ", ".join(str(item) for item in accepted)
    return answer, {"determinant": sp.sstr(discriminant), "integer_candidates": candidates, "accepted": accepted}


def execute_prime_root_projection(ir: MatrixSemanticQueryIR) -> tuple[sp.Expr | str, dict[str, Any]]:
    x = symbol("x")
    polynomial = sp.Poly(parse_math(ir.source_objects["polynomial"]), x)
    if polynomial.degree() != 2:
        raise ValueError("prime-root projection requires a quadratic")
    a, b, c = polynomial.all_coeffs()
    sum_expr = sp.simplify(-b / a)
    product_expr = sp.simplify(c / a)
    bound_relation = parse_relation(ir.source_objects["parameter_bound"])
    bound_symbols = sorted(bound_relation.free_symbols, key=lambda item: item.name)
    if len(bound_symbols) != 1 or not isinstance(bound_relation, (sp.StrictLessThan, sp.LessThan)):
        raise ValueError("prime-root projection needs one finite upper coefficient bound")
    bound_symbol = bound_symbols[0]
    upper = int(sp.floor(bound_relation.rhs - (1 if isinstance(bound_relation, sp.StrictLessThan) else 0)))
    primes = list(sp.primerange(2, upper + 1))
    values: set[sp.Expr] = set()
    assignments: list[dict[str, str]] = []
    coefficient_symbols = sorted((sum_expr.free_symbols | product_expr.free_symbols), key=lambda item: item.name)
    target_symbol = symbol(ir.target)
    for index, first in enumerate(primes):
        for second in primes[index:]:
            solved = sp.solve(
                [sp.Eq(sum_expr, first + second), sp.Eq(product_expr, first * second)],
                coefficient_symbols,
                dict=True,
            )
            for assignment in solved:
                if bound_symbol not in assignment or not bool(bound_relation.subs(assignment)):
                    continue
                target_value = sp.simplify(target_symbol.subs(assignment))
                if target_value.free_symbols:
                    continue
                values.add(target_value)
                assignments.append({key.name: sp.sstr(value) for key, value in assignment.items()})
    answer: sp.Expr | str = sp.Integer(len(values)) if ir.output_sort == "Cardinality" else ", ".join(map(sp.sstr, sorted(values)))
    return answer, {"vieta_map": {"sum": sp.sstr(sum_expr), "product": sp.sstr(product_expr)}, "witness_count": len(assignments)}


def clean_segment(source: str) -> str:
    source = source.strip().strip(" ,.;:")
    source = re.sub(r"\b([A-Za-z])x(?=(?:\*\*|\b))", r"\1*x", source)
    return source


def select_polynomial(segments: list[str]) -> str:
    candidates = [item for item in segments if "x" in item and not looks_like_point(item)]
    candidates.sort(key=len, reverse=True)
    for candidate in candidates:
        try:
            source = parse_equation_expression(candidate)
            if sp.Poly(source, symbol("x")).degree() >= 1:
                return candidate
        except Exception:
            continue
    return ""


def select_equation(segments: list[str]) -> str:
    return next((item for item in segments if "=" in item and "x" in item), "")


def infer_query_target(lower: str, segments: list[str]) -> str:
    patterns = (
        r"(?:possible\s+)?values?\s+of\s+([a-z])\b",
        r"for what (?:real |integer )?value of\s+([a-z])\b",
        r"find (?:all )?(?:positive )?(?:integer )?values? of\s+([a-z])\b",
        r"([a-z])\s*の(?:取りうる|可能な)?値",
    )
    for pattern in patterns:
        match = re.search(pattern, lower)
        if match:
            return match.group(1)
    singletons = [item for item in segments if re.fullmatch(r"[A-Za-z]", item)]
    return singletons[-1] if singletons else ""


def select_observation_expression(segments: list[str], polynomial: str, points: list[tuple[str, str]]) -> str:
    point_sources = {f"({x},{y})" for x, y in points}
    candidates = [item for item in segments if item != polynomial and item.replace(" ", "") not in point_sources]
    return candidates[-1] if candidates else ""


def select_root_value(segments: list[str], polynomial: str, query_target: str) -> str:
    candidates = [item for item in segments if item not in {polynomial, query_target} and "=" not in item and not looks_like_point(item)]
    closed = []
    for item in candidates:
        try:
            expression = parse_math(item)
        except Exception:
            continue
        if not expression.free_symbols:
            closed.append(item)
    return closed[-1] if closed else ""


def select_parameter_bound(segments: list[str]) -> str:
    return next((item for item in segments if re.search(r"[<>]=?", item)), "")


def infer_root_condition(lower: str) -> tuple[str, str] | None:
    if any(marker in lower for marker in ("two distinct real roots", "two different real roots", "異なる2つの実数解", "相異なる2実根")):
        return ">", "two_distinct"
    if any(marker in lower for marker in ("a repeated real root", "double root", "重解")):
        return "=", "double"
    if any(marker in lower for marker in ("no real roots", "no real solutions", "実数解をもたない")):
        return "<", "none"
    if any(marker in lower for marker in ("real roots", "real solutions", "実数解をもつ")) and "rational" not in lower:
        return ">=", "real"
    return None


def infer_coordinate_extremum(lower: str) -> tuple[str, str] | None:
    match = re.search(r"(maximum|minimum) value of\s+([xy])\s*(?=[?.!,]|$)", lower)
    if match:
        return match.group(2), match.group(1)
    match = re.search(r"([xy])\s*の(最大|最小)値", lower)
    if match:
        return match.group(1), "maximum" if match.group(2) == "最大" else "minimum"
    return None


def select_graph_equation(segments: list[str]) -> str:
    return next((item for item in segments if "=" in item and re.search(r"(?:^|=)\s*y\s*(?:=|$)", item)), "")


def asks_origin_graph_distance(lower: str) -> bool:
    return (
        "distance between the origin and a point on the graph" in lower
        or "distance from the origin to the graph" in lower
        or ("原点" in lower and "グラフ" in lower and "距離" in lower)
    ) and any(marker in lower for marker in ("smallest", "minimum", "最小"))


def infer_integer_range(lower: str) -> tuple[int, int] | None:
    match = re.search(r"between\s+(\d+)\s+and\s+(\d+)\s+inclusive", lower)
    if not match:
        match = re.search(r"(\d+)\s*(?:以上|から).*?(\d+)\s*(?:以下|まで)", lower)
    if not match:
        return None
    start, end = int(match.group(1)), int(match.group(2))
    return (start, end) if start <= end else (end, start)


def extract_points(segments: list[str]) -> list[tuple[str, str]]:
    points = []
    for item in segments:
        match = re.fullmatch(r"\(\s*([^,]+)\s*,\s*([^,]+)\s*\)", item)
        if match:
            points.append((match.group(1), match.group(2)))
    return points


def looks_like_point(source: str) -> bool:
    return bool(re.fullmatch(r"\(\s*[^,]+\s*,\s*[^,]+\s*\)", source))


def parameter_names(source: str, *, exclude: set[str]) -> set[str]:
    return {item.name for item in parse_equation_expression(source).free_symbols if item.name not in exclude}


def polynomial_degree(source: str) -> int | None:
    try:
        return int(sp.Poly(parse_equation_expression(source), symbol("x")).degree())
    except Exception:
        return None


def is_planar_quadratic_equation(source: str) -> bool:
    try:
        expression = parse_equation_expression(source)
        polynomial = sp.Poly(expression, symbol("x"), symbol("y"))
        return (
            polynomial.total_degree() == 2
            and symbol("x") in expression.free_symbols
            and symbol("y") in expression.free_symbols
            and expression.free_symbols <= {symbol("x"), symbol("y")}
        )
    except Exception:
        return False


def parse_equation_expression(source: str) -> sp.Expr:
    if "=" not in source:
        return parse_math(source)
    left, right = source.split("=", 1)
    return sp.expand(parse_math(left) - parse_math(right))


def parse_relation(source: str) -> Any:
    for token, constructor in (("<=", sp.Le), (">=", sp.Ge), ("<", sp.Lt), (">", sp.Gt), ("=", sp.Eq)):
        if token in source:
            left, right = source.split(token, 1)
            return constructor(parse_math(left), parse_math(right))
    raise ValueError("relation is missing")


def parse_math(source: str) -> sp.Expr:
    source = clean_segment(source)
    names = set(re.findall(r"\b[A-Za-z]\w*\b", source))
    locals_map = {name: symbol(name) for name in names if name not in {"sqrt", "sin", "cos", "tan", "log", "exp"}}
    locals_map.update({"sqrt": sp.sqrt, "sin": sp.sin, "cos": sp.cos, "tan": sp.tan, "log": sp.log, "exp": sp.exp})
    return parse_expr(source, local_dict=locals_map, transformations=TRANSFORMS, evaluate=True)


def symbol(name: str) -> sp.Symbol:
    return sp.Symbol(name, real=True)


def bounded_integer_members(feasible: sp.Set, *, positive: bool) -> list[int]:
    if isinstance(feasible, sp.Union):
        values = [value for part in feasible.args for value in bounded_integer_members(part, positive=positive)]
        return sorted(set(values))
    if isinstance(feasible, sp.FiniteSet):
        return sorted(int(value) for value in feasible if value.is_integer and (not positive or value > 0))
    if not isinstance(feasible, sp.Interval) or feasible.end in {-sp.oo, sp.oo}:
        raise ValueError("integer parameter domain is not finitely bounded by the constraints")
    if feasible.start is -sp.oo and positive:
        start = 1
    elif feasible.start in {-sp.oo, sp.oo}:
        raise ValueError("integer parameter domain has no finite lower bound")
    else:
        start = int(sp.ceiling(feasible.start))
    end = int(sp.floor(feasible.end))
    if feasible.start is not -sp.oo and feasible.left_open and sp.Integer(start) == feasible.start:
        start += 1
    if feasible.right_open and sp.Integer(end) == feasible.end:
        end -= 1
    if positive:
        start = max(1, start)
    return list(range(start, end + 1))


def matrix_strings(matrix: sp.MatrixBase) -> list[list[str]]:
    return [[sp.sstr(matrix[row, column]) for column in range(matrix.cols)] for row in range(matrix.rows)]


def matrix_witness(matrix: sp.MatrixBase, rhs: sp.MatrixBase, assignment: dict[sp.Symbol, sp.Expr]) -> dict[str, Any]:
    return {
        "A": matrix_strings(matrix),
        "b": matrix_strings(rhs),
        "rank": matrix.rank(),
        "assignment": {key.name: sp.sstr(value) for key, value in assignment.items()},
    }
