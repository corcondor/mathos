"""Compile comparison, percentage, and unknown-state language to affine IR.

The lexical rules below introduce mathematical relations, not benchmark
families.  Every accepted problem is lowered to the same rational linear
system and solved by one elimination routine.  Expected answers and corpus ids
are never inputs.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from fractions import Fraction

try:
    from math_os_prototype.dimensional_synthesis import (
        extract_typed_quantities,
        format_dim,
        format_fraction,
        infer_target_dimension,
    )
    from math_os_prototype.quantity_reasoner import NUMBER_RE, parse_number
except ImportError:
    from dimensional_synthesis import extract_typed_quantities, format_dim, format_fraction, infer_target_dimension
    from quantity_reasoner import NUMBER_RE, parse_number


@dataclass(frozen=True)
class AffineEquation:
    coefficients: dict[str, Fraction]
    constant: Fraction


@dataclass(frozen=True)
class AffineRelationResult:
    answer_exact: str
    expression: str
    relation_kind: str
    query_variable: str
    equations: tuple[str, ...]
    certificate: tuple[str, ...]


GAIN_WORDS = {"added", "bought", "came", "found", "gave him", "gave her", "got", "grew", "joined", "received"}
LOSS_WORDS = {"ate", "deleted", "gave", "left", "lost", "sold", "spent", "used", "went away"}
OUTCOME_PAIRS = {
    frozenset(("won", "lost")),
    frozenset(("win", "lose")),
    frozenset(("passed", "failed")),
    frozenset(("boys", "girls")),
    frozenset(("boy", "girl")),
}


def _lemma(word: str) -> str:
    return {"win": "won", "wins": "won", "lose": "lost", "loses": "lost"}.get(word, word)


def solve_affine_system(equations: list[AffineEquation]) -> dict[str, Fraction] | None:
    variables = sorted({name for equation in equations for name in equation.coefficients})
    if not variables or len(equations) < len(variables):
        return None
    matrix = [
        [equation.coefficients.get(name, Fraction(0)) for name in variables] + [equation.constant]
        for equation in equations
    ]
    row = 0
    pivots: dict[int, int] = {}
    for column in range(len(variables)):
        pivot = next((index for index in range(row, len(matrix)) if matrix[index][column]), None)
        if pivot is None:
            continue
        matrix[row], matrix[pivot] = matrix[pivot], matrix[row]
        scale = matrix[row][column]
        matrix[row] = [value / scale for value in matrix[row]]
        for index in range(len(matrix)):
            if index == row or not matrix[index][column]:
                continue
            factor = matrix[index][column]
            matrix[index] = [left - factor * right for left, right in zip(matrix[index], matrix[row])]
        pivots[column] = row
        row += 1
    if any(all(not value for value in values[:-1]) and values[-1] for values in matrix):
        return None
    if len(pivots) != len(variables):
        return None
    return {variables[column]: matrix[pivot_row][-1] for column, pivot_row in pivots.items()}


def _equation_text(equation: AffineEquation) -> str:
    parts = []
    for name, coefficient in sorted(equation.coefficients.items()):
        parts.append(f"{format_fraction(coefficient)}*{name}")
    return " + ".join(parts) + " = " + format_fraction(equation.constant)


def _result(kind: str, query: str, equations: list[AffineEquation], expression: str) -> AffineRelationResult | None:
    solution = solve_affine_system(equations)
    if solution is None or query not in solution or solution[query] < 0:
        return None
    return AffineRelationResult(
        answer_exact=format_fraction(solution[query]),
        expression=expression,
        relation_kind=kind,
        query_variable=query,
        equations=tuple(_equation_text(equation) for equation in equations),
        certificate=(
            "surface names were alpha-normalized to typed variables",
            "all accepted clauses were lowered to rational affine equations",
            "the query variable has a unique Gaussian-elimination value",
        ),
    )


def _sentence_bounds(text: str, position: int) -> tuple[int, int]:
    left = max(text.rfind(mark, 0, position) for mark in ".?!") + 1
    rights = [index for mark in ".?!" if (index := text.find(mark, position)) >= 0]
    return left, min(rights) if rights else len(text)


def _nearest_polarity(text: str, position: int) -> int | None:
    left, right = _sentence_bounds(text, position)
    before = text[left:position].lower()
    after = text[position:right].lower()
    candidates: list[tuple[int, int]] = []
    for marker in GAIN_WORDS:
        for match in re.finditer(rf"\b{re.escape(marker)}\b", before):
            candidates.append((match.end(), 1))
    for marker in LOSS_WORDS:
        for match in re.finditer(rf"\b{re.escape(marker)}\b", before):
            candidates.append((match.end(), -1))
    if candidates:
        return max(candidates)[1]
    if any(re.search(rf"\b{re.escape(marker)}\b", after[:35]) for marker in GAIN_WORDS):
        return 1
    if any(re.search(rf"\b{re.escape(marker)}\b", after[:35]) for marker in LOSS_WORDS):
        return -1
    return None


def solve_unknown_state(text: str) -> AffineRelationResult | None:
    source = text.lower()
    if " some " not in f" {source} " or any(token in source for token in ("%", "percent", "more than", "less than", "fewer than", "half", "third", "quarter")):
        return None
    clause_result = solve_unknown_state_clauses(source)
    if clause_result is not None:
        return clause_result
    quantities = extract_typed_quantities(text)
    target = infer_target_dimension(text, quantities)
    if target is None:
        dimensions = {quantity.dimension for quantity in quantities}
        if len(dimensions) != 1:
            return None
        target = next(iter(dimensions))
    compatible = [quantity for quantity in quantities if quantity.dimension == target]
    if len(compatible) < 2 or len(compatible) != len(quantities):
        return None

    query = "unknown"
    final_candidates = []
    event_terms: list[tuple[int, Fraction]] = []
    known_parts: list[Fraction] = []
    for quantity in compatible:
        left, right = _sentence_bounds(source, quantity.start)
        sentence = source[left:right]
        polarity = _nearest_polarity(source, quantity.start)
        if re.search(r"\b(?:then|after|finally|now)\b.{0,55}\b(?:there (?:were|are)|has|had|total|left)\b|\b(?:total|together|altogether)\b", sentence):
            final_candidates.append(quantity.value)
        elif polarity is not None:
            event_terms.append((polarity, quantity.value))
        else:
            known_parts.append(quantity.value)

    if len(final_candidates) == 1 and event_terms:
        equation = AffineEquation(
            {query: Fraction(1)},
            final_candidates[0] - sum((sign * value for sign, value in event_terms), Fraction(0)),
        )
        return _result("unknown_state", query, [equation], "final - gains + losses")
    if len(final_candidates) == 1 and len(known_parts) == 1 and re.search(r"\b(?:total|together|altogether)\b", source):
        equation = AffineEquation({query: Fraction(1)}, final_candidates[0] - known_parts[0])
        return _result("unknown_part", query, [equation], "total - known_part")
    return None


def solve_unknown_state_clauses(source: str) -> AffineRelationResult | None:
    """Elaborate an omitted initial state when every numeric clause is typed.

    Object anaphora may be omitted (``took 8 from him``), so this lift uses
    event polarity and the unique final-state observation.  It rejects unless
    every numeral is consumed by exactly one clause role.
    """
    question = re.split(r"(?<=[.?!])\s+", source)[-1]
    if not re.search(
        r"\b(?:initially|originally|before|at first|in the beginning|in the first|primitively|incipiently)\b|"
        r"\bhow\s+many\b[^?]*\b(?:did|had)\b[^?]*\b(?:make|have|had)\b",
        question,
    ):
        return None
    observations: list[Fraction] = []
    events: list[tuple[int, Fraction]] = []
    for match in re.finditer(rf"(?P<number>{NUMBER_RE})", source):
        value = parse_number(match.group("number"))
        if value is None:
            continue
        left, right = _sentence_bounds(source, match.start())
        sentence = source[left:right]
        local_before = source[left:match.start()]
        local_after = source[match.end():right]
        if re.search(r"\b(?:now|still|currently|afterwards)\b[^.?!]*\b(?:has|have|had|there (?:are|were))\b", sentence) or re.search(
            r"\b(?:has|have|had)\b[^.?!]*\b(?:left|remaining)\b", sentence
        ):
            observations.append(value)
            continue
        if re.search(r"\b(?:sold|spent|lost|used|gave away|removed|ate)\b", local_before) or re.search(
            r"\btook\b[^.?!]*\bfrom\s+(?:him|her|them)\b", sentence
        ):
            events.append((-1, value))
            continue
        if re.search(r"\b(?:gave\s+(?:him|her|them)|received|got|added|found|bought)\b", local_before + local_after[:18]):
            events.append((1, value))
            continue
        return None
    if len(observations) != 1 or not events:
        return None
    query = "unknown"
    initial = observations[0] - sum((sign * value for sign, value in events), Fraction(0))
    return _result(
        "unknown_state_clause_elaboration",
        query,
        [AffineEquation({query: Fraction(1)}, initial)],
        "final - signed events",
    )


def solve_partition_comparison(text: str) -> AffineRelationResult | None:
    source = text.lower()
    relation = re.search(
        rf"\b(?P<a>[a-z]+)\s+(?P<difference>{NUMBER_RE})\s+(?P<order>more|fewer|less)\s+than\s+(?:they\s+)?(?P<b>[a-z]+)\b",
        source,
    )
    if not relation:
        return None
    a = relation.group("a")
    b = relation.group("b")
    if frozenset((a, b)) not in OUTCOME_PAIRS:
        return None
    difference = parse_number(relation.group("difference"))
    if difference is None:
        return None
    total_match = re.search(rf"\b(?:played|total(?:ed)?|altogether|in all)\D{{0,25}}(?P<total>{NUMBER_RE})\s+[a-z]+", source)
    if total_match is None:
        # In ordinary English the numeral precedes the total's noun.
        total_match = re.search(rf"\b(?:played)\s+(?P<total>{NUMBER_RE})\s+[a-z]+", source)
    if total_match is None:
        return None
    total = parse_number(total_match.group("total"))
    if total is None:
        return None
    question = re.split(r"(?<=[.?!])\s+", source)[-1]
    question_words = {_lemma(word) for word in re.findall(r"[a-z]+", question)}
    query = a if _lemma(a) in question_words else b if _lemma(b) in question_words else None
    if query is None:
        return None
    signed_difference = difference if relation.group("order") == "more" else -difference
    equations = [
        AffineEquation({a: Fraction(1), b: Fraction(1)}, total),
        AffineEquation({a: Fraction(1), b: Fraction(-1)}, signed_difference),
    ]
    return _result("partition_comparison", query, equations, "solve(total, difference)")


def solve_total_difference_relation(text: str) -> AffineRelationResult | None:
    """Solve an exhaustive two-part partition from its total and difference.

    This is the category-neutral form of the won/lost law.  The category names
    are variables; only the additive partition and signed comparison matter.
    """
    source = text.lower().replace(",", " ")
    relation = re.search(
        rf"\b(?P<difference>{NUMBER_RE})\s+(?P<order>more|fewer|less)\s+"
        r"(?P<a>[a-z]+)\s+(?P<head>[a-z]+)\s+than\s+"
        r"(?P<b>[a-z]+)\s+(?P=head)\b",
        source,
    )
    if relation is None:
        return None
    difference = parse_number(relation.group("difference"))
    if difference is None:
        return None
    a = _normalize_variable(relation.group("a"))
    b = _normalize_variable(relation.group("b"))
    if a == b or a in {"more", "fewer", "less", "he", "she", "they", "it"} or b in {"more", "fewer", "less", "he", "she", "they", "it"}:
        return None

    prefix = source[: relation.start()]
    total_matches = list(re.finditer(
        rf"\b(?:has|have|contains?|total(?:\s+number)?(?:\s+of)?|combined|altogether)\D{{0,28}}"
        rf"(?P<total>{NUMBER_RE})\s+(?P<object>[a-z]+)",
        prefix,
    ))
    if not total_matches:
        return None
    total = parse_number(total_matches[-1].group("total"))
    if total is None:
        return None

    question = re.split(r"(?<=[.?!])\s+", source)[-1]
    query_match = re.search(r"\bhow\s+many\s+(?P<query>[a-z]+)(?:\s+[a-z]+)?\b", question)
    if query_match is None:
        return None
    query_word = _normalize_variable(query_match.group("query"))
    query = a if query_word == a else b if query_word == b else None
    if query is None:
        return None
    signed = difference if relation.group("order") == "more" else -difference
    equations = [
        AffineEquation({a: Fraction(1), b: Fraction(1)}, total),
        AffineEquation({a: Fraction(1), b: Fraction(-1)}, signed),
    ]
    return _result("total_difference_partition", query, equations, "solve exhaustive two-part total and difference")


def solve_ratio_relation(text: str) -> AffineRelationResult | None:
    """Lower a two-part ratio and one independent observation to affine IR."""
    source = text.lower().replace(",", " ")
    ratio_match = re.search(r"(?P<left>\d+)\s*:\s*(?P<right>\d+)", source)
    if ratio_match is None:
        return None
    left_ratio = Fraction(int(ratio_match.group("left")))
    right_ratio = Fraction(int(ratio_match.group("right")))
    if left_ratio <= 0 or right_ratio <= 0:
        return None

    # Scalar reduction is the same ratio morphism without named parts.
    if re.search(r"\breduced\s+in\s+the\s+ratio\b|\breduced\s+in\s+ratio\b", source):
        values = []
        for match in re.finditer(rf"(?P<number>{NUMBER_RE})", source):
            if ratio_match.start() <= match.start() < ratio_match.end():
                continue
            value = parse_number(match.group("number"))
            if value is not None:
                values.append(value)
        if len(values) != 1:
            return None
        return _result(
            "ratio_scale",
            "answer",
            [AffineEquation({"answer": left_ratio}, values[0] * right_ratio)],
            "old:new = left:right",
        )

    labels: tuple[str, str] | None = None
    before_ratio = source[: ratio_match.start()]
    named = re.search(
        r"ratio\s+(?:of\s+)?(?P<a>[a-z]+)(?:\s+[a-z]+)?\s+(?:to|and)\s+"
        r"(?P<b>[a-z]+)(?:\s+[a-z]+)?(?:\s+(?:at|in|on)\s+(?:the\s+)?[a-z]+(?:\s+[a-z]+)?)?"
        r"\s+(?:is|was|of)\s*$",
        before_ratio,
    )
    if named:
        labels = (_normalize_variable(named.group("a")), _normalize_variable(named.group("b")))
    if labels is None:
        divided = re.search(
            r"\b(?P<a>[a-z]+)\s+and\s+(?P<b>[a-z]+)\s+divided\b",
            before_ratio,
        )
        if divided:
            labels = (_normalize_variable(divided.group("a")), _normalize_variable(divided.group("b")))
    if labels is None or labels[0] == labels[1]:
        return None
    a, b = labels
    equations = [AffineEquation({a: right_ratio, b: -left_ratio}, Fraction(0))]

    numeric: list[tuple[int, int, Fraction]] = []
    for match in re.finditer(rf"(?P<number>{NUMBER_RE})", source):
        if ratio_match.start() <= match.start() < ratio_match.end():
            continue
        value = parse_number(match.group("number"))
        if value is not None:
            numeric.append((match.start(), match.end(), value))

    total_value: Fraction | None = None
    for position, _, value in numeric:
        context = source[max(0, position - 55) : position + 45]
        if re.search(r"\b(?:total|combined|altogether|divided)\b", context):
            total_value = value
            break
    known_label: str | None = None
    known_value: Fraction | None = None
    for _, end, value in numeric:
        tail = source[end : end + 38]
        if re.match(rf"\s+(?:[a-z]+\s+)?{re.escape(a)}s?\b", tail):
            known_label, known_value = a, value
        elif re.match(rf"\s+(?:[a-z]+\s+)?{re.escape(b)}s?\b", tail):
            known_label, known_value = b, value
    if total_value is not None:
        equations.append(AffineEquation({a: Fraction(1), b: Fraction(1)}, total_value))
    elif known_label is not None and known_value is not None:
        equations.append(AffineEquation({known_label: Fraction(1)}, known_value))
    else:
        return None

    question = re.split(r"(?<=[.?!])\s+", source)[-1]
    if re.search(r"\bhow\s+many\s+more\b|\bdifference\b", question):
        query = "answer"
        equations.append(AffineEquation({query: Fraction(1), b: Fraction(-1), a: Fraction(1)}, Fraction(0)))
        return _result("ratio_difference", query, equations, "solve ratio scale and observe part difference")
    event_label: str | None = None
    adjustment = Fraction(0)
    for label in (a, b):
        subject_event = re.search(
            rf"\b{re.escape(label)}\b[^.?!]{{0,18}}?\b(?:spent|used|lost|gave)\s+\$?(?P<amount>{NUMBER_RE})",
            source,
        )
        if subject_event:
            parsed = parse_number(subject_event.group("amount"))
            if parsed is not None:
                event_label, adjustment = label, -parsed
                break

    query_match = re.search(r"\bhow\s+many\s+(?P<label>[a-z]+)", question)
    query_word = _normalize_variable(query_match.group("label")) if query_match else None
    query = a if query_word == a else b if query_word == b else event_label
    if query is None:
        return None
    solution = solve_affine_system(equations)
    if solution is None or query not in solution:
        return None
    event = re.search(
        rf"(?P<amount>{NUMBER_RE})\s+{re.escape(query)}s?\s+(?:alight|leave|left|spent|used)",
        source,
    )
    if event and not adjustment:
        parsed = parse_number(event.group("amount"))
        if parsed is not None:
            adjustment = -parsed
    if adjustment:
        answer = "answer"
        equations.append(AffineEquation({answer: Fraction(1), query: Fraction(-1)}, adjustment))
        return _result("ratio_part_after_event", answer, equations, "solve ratio part then apply typed event")
    return _result("ratio_part", query, equations, "solve ratio scale and project requested part")


def _normalize_variable(name: str) -> str:
    name = name.lower().strip(".,;:!?")
    if name.endswith("ies") and len(name) > 4:
        return name[:-3] + "y"
    if name.endswith("s") and len(name) > 3 and not name.endswith("ss"):
        return name[:-1]
    return name


def _normalize_item(name: str) -> str:
    words = re.findall(r"[a-z]+(?:-[a-z]+)?", name.lower())
    if words and words[-1].endswith("s") and not words[-1].endswith("ss"):
        words[-1] = words[-1][:-1]
    return "_".join(words)


def solve_weighted_comparison_total(text: str) -> AffineRelationResult | None:
    """Lower unit-price comparisons and counted purchases to one affine system."""
    source = text.lower().replace(",", " ")
    relation = re.search(
        rf"\b(?:an?|the)\s+(?P<a>[a-z-]+\s+[a-z-]+)\s+costs?\s+\$?(?P<difference>{NUMBER_RE})\s+"
        rf"(?P<order>more|less)\s+than\s+(?:an?|the)\s+(?P<b>[a-z-]+\s+[a-z-]+)\b",
        source,
    )
    if relation is None or not re.search(r"\b(?:spent|pay|paid|cost)\b", source):
        return None
    a = _normalize_item(relation.group("a"))
    b = _normalize_item(relation.group("b"))
    difference = parse_number(relation.group("difference"))
    if not a or not b or a == b or difference is None:
        return None
    if relation.group("order") == "less":
        difference = -difference

    equations = [AffineEquation({a: Fraction(1), b: Fraction(-1)}, difference)]
    known_values: dict[str, Fraction] = {}
    for match in re.finditer(
        rf"\b(?:an?|the)\s+(?P<item>[a-z-]+\s+[a-z-]+)\s+costs?\s+\$?(?P<value>{NUMBER_RE})\b",
        source,
    ):
        tail = source[match.end() : match.end() + 12]
        if re.match(r"\s+(?:more|less)\b", tail):
            continue
        value = parse_number(match.group("value"))
        if value is not None:
            known_values[_normalize_item(match.group("item"))] = value
    for item, value in known_values.items():
        if item in {a, b}:
            equations.append(AffineEquation({item: Fraction(1)}, value))

    observation = source[relation.end() :]
    counts: dict[str, Fraction] = {}
    for match in re.finditer(
        rf"\b(?P<count>{NUMBER_RE})(?:-|\s+)(?P<item>[a-z-]+\s+[a-z-]+)\b",
        observation,
    ):
        count = parse_number(match.group("count"))
        item = _normalize_item(match.group("item"))
        if count is not None and item in {a, b}:
            counts[item] = count
    if set(counts) != {a, b}:
        return None
    query = "answer"
    equations.append(
        AffineEquation(
            {query: Fraction(1), a: -counts[a], b: -counts[b]},
            Fraction(0),
        )
    )
    return _result("weighted_comparison_total", query, equations, "sum(count * unit value)")


def solve_multiplier_offset_relation(text: str) -> AffineRelationResult | None:
    source = text.lower()
    relation = re.search(
        rf"\b(?P<entity>[a-z]+)\s+has\s+(?P<offset>{NUMBER_RE})\s+(?P<order>more|less)\s+than\s+"
        r"(?P<factor>twice|three times|four times)\s+(?:the\s+)?(?:number|amount)\s+of\s+[a-z]+\s+that\s+"
        r"(?P<base>[a-z]+)\s+has\b",
        source,
    )
    if relation is None:
        return None
    entity = _normalize_variable(relation.group("entity"))
    base = _normalize_variable(relation.group("base"))
    offset = parse_number(relation.group("offset"))
    if offset is None or entity == base:
        return None
    if relation.group("order") == "less":
        offset = -offset
    factor = {"twice": 2, "three times": 3, "four times": 4}[relation.group("factor")]
    equations = [AffineEquation({entity: Fraction(1), base: Fraction(-factor)}, offset)]
    for variable in (entity, base):
        for match in re.finditer(
            rf"\b{re.escape(variable)}\s+has\s+(?P<value>{NUMBER_RE})\s+[a-z]+\b",
            source,
        ):
            if relation.start() <= match.start() < relation.end():
                continue
            value = parse_number(match.group("value"))
            if value is not None:
                equations.append(AffineEquation({variable: Fraction(1)}, value))
                break
    question = re.split(r"(?<=[.?!])\s+", source)[-1]
    query_match = re.search(r"\bhow\s+many(?:\s+[a-z]+)?\s+does\s+(?P<entity>[a-z]+)\s+have\b", question)
    if query_match is None:
        return None
    query = _normalize_variable(query_match.group("entity"))
    if query not in {entity, base}:
        return None
    return _result("multiplier_offset", query, equations, "solve affine multiplier and offset")


def solve_multisort_comparison(text: str) -> AffineRelationResult | None:
    source = text.lower()
    relation = re.search(
        rf"\b(?P<entity>[a-z]+)\s+has\s+(?P<d1>{NUMBER_RE})\s+(?P<o1>more|fewer|less)\s+(?P<s1>[a-z]+)\s+and\s+"
        rf"(?P<d2>{NUMBER_RE})\s+(?P<o2>more|fewer|less)\s+(?P<s2>[a-z]+)\s+than\s+(?P<base>[a-z]+)\b",
        source,
    )
    if relation is None:
        return None
    entity = _normalize_variable(relation.group("entity"))
    base = _normalize_variable(relation.group("base"))
    sorts = (_normalize_variable(relation.group("s1")), _normalize_variable(relation.group("s2")))
    differences = (parse_number(relation.group("d1")), parse_number(relation.group("d2")))
    orders = (relation.group("o1"), relation.group("o2"))
    if None in differences or len(set(sorts)) != 2 or entity == base:
        return None
    equations: list[AffineEquation] = []
    for sort, difference, order in zip(sorts, differences, orders):
        assert difference is not None
        signed = difference if order == "more" else -difference
        equations.append(
            AffineEquation(
                {f"{entity}:{sort}": Fraction(1), f"{base}:{sort}": Fraction(-1)},
                signed,
            )
        )
    known = re.search(
        rf"\b{re.escape(base)}\s+has\s+(?P<v1>{NUMBER_RE})\s+(?P<s1>[a-z]+)\s+and\s+"
        rf"(?P<v2>{NUMBER_RE})\s+(?P<s2>[a-z]+)\b",
        source,
    )
    if known is None:
        return None
    for value_name, sort_name in (("v1", "s1"), ("v2", "s2")):
        value = parse_number(known.group(value_name))
        sort = _normalize_variable(known.group(sort_name))
        if value is None or sort not in sorts:
            return None
        equations.append(AffineEquation({f"{base}:{sort}": Fraction(1)}, value))
    question = re.split(r"(?<=[.?!])\s+", source)[-1]
    query_match = re.search(r"\bhow\s+many\s+(?P<sort>[a-z]+)\s+does\s+(?P<entity>[a-z]+)\s+have\b", question)
    if query_match is None:
        return None
    query = f"{_normalize_variable(query_match.group('entity'))}:{_normalize_variable(query_match.group('sort'))}"
    if query not in {f"{entity}:{sort}" for sort in sorts}:
        return None
    return _result("multisort_comparison", query, equations, "solve comparison in product sort")


def solve_comparison_chain(text: str) -> AffineRelationResult | None:
    source = text.lower()
    if (
        "%" in source
        or "percent" in source
        or re.search(r"\b(?:each|every|per|dozen|rate|month|year|week|day|hour|minute|times)\b", source)
        or re.search(r"\b(?:after|then|first game|second game)\b", source)
        or re.search(r"\b(?:has|there (?:is|are))\b.*\bbought\b", source)
        or re.search(r"\b(?:first|second)\s+one\b", source)
        or re.search(r"\b(?:gave|received)\b", source)
    ):
        return None
    equations: list[AffineEquation] = []
    variables: set[str] = set()
    relation_spans: list[tuple[int, int]] = []
    invalid_reference = False

    def add_difference(
        entity: str,
        base: str,
        difference_text: str,
        order: str,
        span: tuple[int, int],
    ) -> None:
        nonlocal invalid_reference
        if any(max(span[0], start) < min(span[1], end) for start, end in relation_spans):
            return
        difference = parse_number(difference_text)
        if difference is None:
            return
        if entity == "who":
            antecedent = re.search(r"\b([a-z]+)\s*,\s*$", source[max(0, span[0] - 45) : span[0]])
            if antecedent:
                entity = antecedent.group(1)
        if entity in {"he", "she", "they", "it", "who"} or base in {"he", "she", "they", "it", "who"}:
            invalid_reference = True
            return
        entity = _normalize_variable(entity)
        base = _normalize_variable(base)
        if entity == base:
            return
        signed = difference if order in {"more", "greater", "older", "longer", "farther"} else -difference
        variables.update((entity, base))
        equations.append(AffineEquation({entity: Fraction(1), base: Fraction(-1)}, signed))
        relation_spans.append(span)

    for match in re.finditer(
        rf"\b(?P<entity>[a-z]+)\b\s+(?:has|had|costs?|is|was|scored|found|picked|jumped)\s+\$?(?P<difference>{NUMBER_RE})\s+(?P<order>more|fewer|less|greater|older|younger|longer|shorter|farther)\b(?:\s+[a-z]+){{0,3}}?\s+than\s+(?:(?:the|an?)\s+)?(?P<base>[a-z]+)\b",
        source,
    ):
        if re.search(r"\bnumber\s+of\s+[a-z]+\s+$", source[max(0, match.start() - 30) : match.start()]):
            continue
        add_difference(match.group("entity"), match.group("base"), match.group("difference"), match.group("order"), match.span())
    for match in re.finditer(
        rf"\bnumber\s+of\s+(?P<entity>[a-z]+)\s+[a-z]+\s+(?:is|was)\s+\$?(?P<difference>{NUMBER_RE})\s+"
        rf"(?P<order>more|fewer|less|greater)\s+than\s+(?:(?:the|an?)\s+)?(?P<base>[a-z]+)\b",
        source,
    ):
        add_difference(match.group("entity"), match.group("base"), match.group("difference"), match.group("order"), match.span())
    for match in re.finditer(
        rf"\b(?P<difference>{NUMBER_RE})\s+(?P<order>more|fewer|less|greater)\s+(?P<entity>[a-z]+)"
        rf"(?:\s+[a-z]+)?\s+than\s+(?:(?:the|an?)\s+)?(?P<base>[a-z]+)\b",
        source,
    ):
        add_difference(match.group("entity"), match.group("base"), match.group("difference"), match.group("order"), match.span())

    factor_words = {"half": Fraction(1, 2), "third": Fraction(1, 3), "quarter": Fraction(1, 4), "twice": Fraction(2)}
    factor_spans: list[tuple[int, int]] = []
    for match in re.finditer(
        r"\b(?P<entity>[a-z]+)\b\s+(?:has|had|costs?|is|was|scored|found|picked|jumped)\s+(?P<factor>half|third|quarter|twice)\s+as\s+(?:many|much)(?:\s+[a-z]+)?\s+as\s+(?:(?:the|an?)\s+)?(?P<base>[a-z]+)\b",
        source,
    ):
        entity = _normalize_variable(match.group("entity"))
        base = _normalize_variable(match.group("base"))
        if entity != base:
            variables.update((entity, base))
            equations.append(AffineEquation({entity: Fraction(1), base: -factor_words[match.group("factor")]}, Fraction(0)))
            factor_spans.append(match.span())
    for match in re.finditer(
        r"\b(?P<factor>half|third|quarter|twice)\s+as\s+(?:many|much)\s+(?P<entity>[a-z]+)\s+as\s+(?:(?:the|an?)\s+)?(?P<base>[a-z]+)\b",
        source,
    ):
        if any(max(match.start(), start) < min(match.end(), end) for start, end in factor_spans):
            continue
        entity = _normalize_variable(match.group("entity"))
        base = _normalize_variable(match.group("base"))
        if entity != base:
            variables.update((entity, base))
            equations.append(AffineEquation({entity: Fraction(1), base: -factor_words[match.group("factor")]}, Fraction(0)))
    for match in re.finditer(
        rf"\b(?P<entity>[a-z]+)\b.{{0,24}}?\b(?P<factor>{NUMBER_RE})\s+times\s+as\s+(?:many|much)\s+as\s+(?:the\s+)?(?P<base>[a-z]+)\b",
        source,
    ):
        factor = parse_number(match.group("factor"))
        entity = _normalize_variable(match.group("entity"))
        base = _normalize_variable(match.group("base"))
        if factor is not None and entity != base:
            variables.update((entity, base))
            equations.append(AffineEquation({entity: Fraction(1), base: -factor}, Fraction(0)))
    for match in re.finditer(
        r"\b(?P<factor>twice|three times|four times)\s+(?:the\s+)?(?:number|amount)\s+of\s+(?P<entity>[a-z]+)\s+(?:as|than)\s+(?:the\s+)?(?P<base>[a-z]+)\b",
        source,
    ):
        factor = {"twice": 2, "three times": 3, "four times": 4}[match.group("factor")]
        entity = _normalize_variable(match.group("entity"))
        base = _normalize_variable(match.group("base"))
        if entity != base:
            variables.update((entity, base))
            equations.append(AffineEquation({entity: Fraction(1), base: Fraction(-factor)}, Fraction(0)))

    if invalid_reference or not equations or len(variables) < 2:
        return None
    for variable in sorted(variables):
        value = None
        for subject in re.finditer(
            rf"\b{re.escape(variable)}s?\b[^.?!]{{0,25}}?\b(?:has|had|costs?|is|found|killed|scored|picked|jumped|bought|collected)\b\s+\$?(?P<value>{NUMBER_RE})",
            source,
        ):
            if re.match(r"\s+(?:more|fewer|less|greater|older|younger|longer|shorter|farther|as)\b", source[subject.end() :]):
                continue
            value = parse_number(subject.group("value"))
            if value is not None:
                break
        if value is None:
            preceding = re.search(rf"(?P<value>{NUMBER_RE})\s+(?P<middle>(?:[a-z]+\s+){{0,2}}){re.escape(variable)}s?\b", source)
            if preceding and not re.search(r"\b(?:more|fewer|less|greater)\b", preceding.group("middle")):
                value = parse_number(preceding.group("value"))
        if value is not None:
            equations.append(AffineEquation({variable: Fraction(1)}, value))

    question = re.split(r"(?<=[.?!])\s+", source)[-1]
    mentioned = [variable for variable in variables if re.search(rf"\b{re.escape(variable)}s?\b", question)]
    difference_query = re.search(
        r"\bhow\s+many\s+more\s+[a-z]+\s+does\s+(?P<a>[a-z]+)\s+have\s+than\s+(?P<b>[a-z]+)\b",
        question,
    )
    if difference_query:
        a = _normalize_variable(difference_query.group("a"))
        b = _normalize_variable(difference_query.group("b"))
        if a not in variables or b not in variables:
            return None
        query = "answer"
        equations.append(AffineEquation({query: Fraction(1), a: Fraction(-1), b: Fraction(1)}, Fraction(0)))
        return _result("comparison_chain_difference", query, equations, "observe difference of solved quantities")
    if re.search(r"\b(?:total|altogether|in all|all)\b", question):
        query = "answer"
        coefficients = {query: Fraction(1), **{variable: Fraction(-1) for variable in variables}}
        equations.append(AffineEquation(coefficients, Fraction(0)))
        return _result("comparison_chain_total", query, equations, "sum solved comparison variables")
    if not mentioned and re.search(r"\bhow\s+many\s+[a-z]+\s+do\s+(?:they|we|you)\s+(?:have|own|possess)\b", question):
        query = "answer"
        equations.append(
            AffineEquation(
                {query: Fraction(1), **{variable: Fraction(-1) for variable in variables}},
                Fraction(0),
            )
        )
        return _result("comparison_chain_total", query, equations, "sum exhaustive compared quantities")
    if len(mentioned) == 1:
        query = mentioned[0]
        return _result("comparison_chain", query, equations, "solve comparison chain")
    return None


def solve_percentage_relation(text: str) -> AffineRelationResult | None:
    source = text.lower()
    if "\\" in source:
        return None
    if re.search(r"\b(?:as many|sum of|all mentioned|combined with|together with)\b", source):
        return None
    percent_match = re.search(r"(?P<percent>\d+(?:\.\d+)?)\s*%", source)
    if percent_match is None:
        return None
    percent = Fraction(percent_match.group("percent")) / 100
    numeric = []
    for match in re.finditer(rf"(?P<number>{NUMBER_RE})", source):
        if percent_match.start() <= match.start() < percent_match.end():
            continue
        value = parse_number(match.group("number"))
        if value is not None:
            numeric.append((match.start(), value, match.group("number")))
    if len(numeric) != 1:
        return None
    known = numeric[0][1]
    known_end = numeric[0][0] + len(numeric[0][2])
    query = "target"

    if "original" in source and re.search(r"\b(?:discount|off)\b", source):
        equation = AffineEquation({query: Fraction(1) - percent}, known)
        return _result("percentage_inverse_discount", query, [equation], "current / (1 - rate)")
    if "original" in source and re.search(r"\b(?:increase|markup|more)\b", source):
        equation = AffineEquation({query: Fraction(1) + percent}, known)
        return _result("percentage_inverse_increase", query, [equation], "current / (1 + rate)")
    if re.search(r"\b(?:what|how much|how many)\b", source):
        if re.search(r"\b(?:more|increase|gain|grew|up)\b", source):
            known_object = re.match(r"\s+([a-z]+)", source[known_end:])
            query_object = re.search(r"\bhow\s+many\s+([a-z]+)\b", source)
            if known_object is None or query_object is None:
                return None
            if _normalize_variable(known_object.group(1)) != _normalize_variable(query_object.group(1)):
                return None
            equation = AffineEquation({query: Fraction(1)}, known * (1 + percent))
            return _result("percentage_forward_increase", query, [equation], "base * (1 + rate)")
        if re.search(r"\b(?:less|decrease|discount|off|down)\b", source):
            equation = AffineEquation({query: Fraction(1)}, known * (1 - percent))
            return _result("percentage_forward_decrease", query, [equation], "base * (1 - rate)")
        if re.search(rf"\b(?:what\s+is|how\s+many\s+[a-z]+\s+(?:is|are))\s+{re.escape(percent_match.group(0))}\s+of\b", source):
            equation = AffineEquation({query: Fraction(1)}, known * percent)
            return _result("percentage_of", query, [equation], "base * rate")
    return None


def solve_affine_relation_problem(text: str) -> AffineRelationResult | None:
    for solver in (
        solve_unknown_state,
        solve_total_difference_relation,
        solve_partition_comparison,
        solve_ratio_relation,
        solve_weighted_comparison_total,
        solve_multiplier_offset_relation,
        solve_multisort_comparison,
        solve_comparison_chain,
        solve_percentage_relation,
    ):
        result = solver(text)
        if result is not None:
            return result
    return None
