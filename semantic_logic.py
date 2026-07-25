"""Logic-level semantic checks for MathOS quantity reasoning.

This module is intentionally small and structural.  It treats word-problem
quantities as typed terms, then checks equation candidates against a simple
many-sorted logic:

    Quantity(value, unit, owner, object, time/state)
      -> typed terms
      -> candidate sequent
      -> sort/role obligations

The goal is to keep generalization pressure on the representation instead of
adding benchmark-specific surface patterns.
"""

from __future__ import annotations

import re
from dataclasses import asdict, dataclass, field
from fractions import Fraction
from typing import Any


MONEY_OBJECTS = {"cent", "cents", "dollar", "dollars", "money", "price", "cost", "pay"}
TIME_OBJECTS = {"day", "days", "hour", "hours", "minute", "minutes", "week", "weeks", "month", "months"}
PRONOUN_OBJECTS = {"it", "one", "ones", "them", "rest", "quantity"}
SCALAR_OBJECTS = {"count", "number", "total", "quantity"}
CONTAINER_OBJECTS = {
    "bag",
    "basket",
    "box",
    "bus",
    "carton",
    "container",
    "folder",
    "group",
    "load",
    "package",
    "shelf",
    "shelve",
    "team",
    "wardrobe",
}

PRODUCT_KINDS = {
    "complement_count_times_unit",
    "count_sum_times_common_unit",
    "initial_from_each_removed_and_final",
    "net_rate_times_duration",
    "rate_times_duration",
    "remaining_count_times_rate",
    "sum_per_units_times_count",
    "unit_count_product",
}
DIVISION_KINDS = {
    "nested_container_division",
    "remainder_divided_by_unit",
    "split_total_by_group_count",
    "total_divided_by_rate",
}
SAME_SORT_KINDS = {
    "adjusted_category_difference",
    "category_difference",
    "complement_count",
    "difference_last_two",
    "gain_vs_inferred_loss_difference",
    "gain_vs_loss_difference",
    "initial_from_final_and_gain",
    "initial_from_final_and_loss",
    "partition_second_minus_first",
    "selected_sum",
    "state_update",
    "time_category_difference",
    "two_group_difference",
}


@dataclass(frozen=True)
class SemanticSort:
    base: str
    obj: str | None = None
    per: str | None = None

    def sexpr(self) -> str:
        if self.base == "Rate":
            return f"(Rate {self.obj or 'Unknown'} {self.per or 'Unknown'})"
        if self.obj:
            return f"({self.base} {self.obj})"
        return self.base

    def to_dict(self) -> dict[str, str | None]:
        return asdict(self)


@dataclass(frozen=True)
class SemanticTerm:
    name: str
    value: str
    sort: SemanticSort
    role: str
    source: str

    def sexpr(self) -> str:
        return f"(term {self.name} {self.value} {self.sort.sexpr()} :role {self.role})"

    def to_dict(self) -> dict[str, Any]:
        payload = asdict(self)
        payload["sort"] = self.sort.to_dict()
        return payload


@dataclass(frozen=True)
class SemanticCheck:
    status: str
    output_sort: SemanticSort
    sequent: str
    terms: list[SemanticTerm]
    obligations: list[str]
    checks: list[str]
    warnings: list[str] = field(default_factory=list)
    rejection: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "status": self.status,
            "output_sort": self.output_sort.to_dict(),
            "sequent": self.sequent,
            "terms": [term.to_dict() for term in self.terms],
            "obligations": self.obligations,
            "checks": self.checks,
            "warnings": self.warnings,
            "rejection": self.rejection,
        }


def verify_quantity_candidate_semantics(text: str, quantities: list[Any], candidate: Any) -> SemanticCheck:
    terms = compile_quantity_terms(quantities)
    evidence_terms = [terms[quantity_id] for quantity_id in candidate.evidence_ids if quantity_id in terms]
    target_sort = infer_candidate_output_sort(text, candidate, evidence_terms)
    obligations = build_obligations(candidate, evidence_terms, target_sort)
    rejection = reject_reason(candidate, evidence_terms, target_sort)
    status = "rejected" if rejection else "accepted"
    checks = ["semantic_sort_checked", "logic_sequent_built"]
    if target_sort.base != "Unknown":
        checks.append("target_sort_inferred")
    sequent = build_sequent(evidence_terms, candidate, target_sort)
    return SemanticCheck(
        status=status,
        output_sort=target_sort,
        sequent=sequent,
        terms=evidence_terms,
        obligations=obligations,
        checks=checks,
        warnings=[] if evidence_terms else ["candidate has no evidence terms"],
        rejection=rejection,
    )


def compile_quantity_terms(quantities: list[Any]) -> dict[int, SemanticTerm]:
    resolved_objects = resolve_objects(quantities)
    terms: dict[int, SemanticTerm] = {}
    for quantity in quantities:
        obj = resolved_objects.get(quantity.id, normalize_object(getattr(quantity, "obj", "")))
        sort = sort_for_quantity(quantity, obj)
        terms[quantity.id] = SemanticTerm(
            name=f"q{quantity.id}",
            value=format_value(quantity.value),
            sort=sort,
            role=getattr(quantity, "role", "unknown"),
            source=getattr(quantity, "text", ""),
        )
    return terms


def resolve_objects(quantities: list[Any]) -> dict[int, str]:
    resolved: dict[int, str] = {}
    latest_concrete: str | None = None
    for quantity in quantities:
        raw = normalize_object(getattr(quantity, "obj", ""))
        if raw in PRONOUN_OBJECTS:
            resolved[quantity.id] = latest_concrete or raw
            continue
        resolved[quantity.id] = raw
        if raw not in MONEY_OBJECTS | TIME_OBJECTS | SCALAR_OBJECTS:
            latest_concrete = raw
    return resolved


def sort_for_quantity(quantity: Any, resolved_object: str) -> SemanticSort:
    role = getattr(quantity, "role", "")
    text = getattr(quantity, "text", "")
    if role in {"per_unit", "rate"}:
        output = object_sort_name(resolved_object)
        per = infer_rate_denominator(text, getattr(quantity, "time", None))
        return SemanticSort("Rate", output, per)
    if resolved_object in MONEY_OBJECTS:
        return SemanticSort("Money", "money")
    if resolved_object in TIME_OBJECTS:
        return SemanticSort("Time", normalize_time(resolved_object))
    if resolved_object in SCALAR_OBJECTS:
        return SemanticSort("Scalar")
    return SemanticSort("Count", resolved_object)


def infer_candidate_output_sort(text: str, candidate: Any, evidence_terms: list[SemanticTerm]) -> SemanticSort:
    target = normalize_object(getattr(candidate, "target_object", "") or query_object(text) or "")
    kind = getattr(candidate, "kind", "")
    if target in {"money", "cost", "price", "pay"}:
        return SemanticSort("Money", "money")
    if target:
        return SemanticSort("Count", target)
    if kind in {"rate_minus_discount", "per_unit_category_difference", "count_sum_times_common_unit"}:
        return SemanticSort("Money", "money")
    if kind in PRODUCT_KINDS:
        for term in evidence_terms:
            if term.sort.base == "Rate":
                return sort_from_rate_output(term.sort)
    if kind in DIVISION_KINDS:
        container = first_target_container(text)
        if container:
            return SemanticSort("Count", container)
    if evidence_terms:
        return evidence_terms[0].sort if evidence_terms[0].sort.base != "Rate" else sort_from_rate_output(evidence_terms[0].sort)
    return SemanticSort("Unknown")


def build_obligations(candidate: Any, evidence_terms: list[SemanticTerm], output_sort: SemanticSort) -> list[str]:
    kind = getattr(candidate, "kind", "")
    obligations = [f"(typed answer {output_sort.sexpr()})"]
    if kind in PRODUCT_KINDS:
        obligations.append("(exists rate-term evidence)")
        obligations.append("(exists scalar-or-count multiplier evidence)")
    elif kind in DIVISION_KINDS:
        obligations.append("(denominator nonzero)")
        obligations.append("(division result has requested target sort)")
    elif kind in SAME_SORT_KINDS:
        obligations.append("(additive terms share a count/money/time super-sort)")
    else:
        obligations.append("(candidate kind has generic arithmetic semantics)")
    return obligations


def reject_reason(candidate: Any, evidence_terms: list[SemanticTerm], output_sort: SemanticSort) -> str | None:
    kind = getattr(candidate, "kind", "")
    if kind in PRODUCT_KINDS:
        if not any(term.sort.base == "Rate" for term in evidence_terms):
            return "product-like candidate has no rate/per-unit evidence"
        if not any(term.sort.base in {"Count", "Scalar", "Time"} for term in evidence_terms):
            return "product-like candidate has no multiplier evidence"
    if kind in DIVISION_KINDS:
        if not evidence_terms:
            return "division-like candidate has no evidence"
        if output_sort.base == "Unknown":
            return "division-like candidate has unknown output sort"
    if kind in SAME_SORT_KINDS:
        concrete_bases = {term.sort.base for term in evidence_terms if term.sort.base not in {"Scalar", "Rate"}}
        if len(concrete_bases) > 1 and not concrete_bases <= {"Count"}:
            return "additive candidate mixes incompatible semantic bases"
    return None


def build_sequent(evidence_terms: list[SemanticTerm], candidate: Any, output_sort: SemanticSort) -> str:
    assumptions = " ".join(term.sexpr() for term in evidence_terms) or "True"
    expression = getattr(candidate, "expression", "")
    value = format_value(getattr(candidate, "value", ""))
    return f"(sequent (assume {assumptions}) (prove (= answer {value}) :expr \"{expression}\" :sort {output_sort.sexpr()}))"


def query_object(text: str) -> str | None:
    patterns = (
        r"how many more (?P<object>[a-z-]+)",
        r"how many (?P<object>[a-z-]+) (?:did|does|do|will|would|are|is|were|was|needed|need)",
        r"how many (?P<object>[a-z-]+)",
        r"how much (?P<object>money|water|cost|distance|area|time)",
        r"how much (?P<object>[a-z-]+)",
    )
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            obj = normalize_object(match.group("object"))
            if obj not in {"do", "does", "many", "more", "much", "will", "would"}:
                return obj
    return None


def infer_rate_denominator(text: str, time_value: str | None) -> str | None:
    for pattern in (
        r"(?:for|in|on|from)\s+each\s+(?P<object>[a-z-]+)",
        r"each\s+(?P<object>[a-z-]+)",
        r"per\s+(?P<object>[a-z-]+)",
        r"in one\s+(?P<object>[a-z-]+)",
    ):
        match = re.search(pattern, text)
        if match:
            local = text[match.start() : match.start() + 80]
            for container in sorted(CONTAINER_OBJECTS, key=len, reverse=True):
                if re.search(rf"\b{re.escape(container)}s?\b", local):
                    return object_sort_name(container)
            return object_sort_name(normalize_object(match.group("object")))
    if time_value:
        return object_sort_name(normalize_object(time_value))
    return None


def first_target_container(text: str) -> str | None:
    normalized = normalize_object(query_object(text) or "")
    if normalized in CONTAINER_OBJECTS:
        return normalized
    for container in sorted(CONTAINER_OBJECTS):
        if re.search(rf"\b{re.escape(container)}s?\b", text):
            return container
    return None


def sort_from_rate_output(sort: SemanticSort) -> SemanticSort:
    if sort.obj == "money":
        return SemanticSort("Money", "money")
    if sort.obj in TIME_OBJECTS:
        return SemanticSort("Time", normalize_time(sort.obj or "time"))
    return SemanticSort("Count", sort.obj)


def object_sort_name(value: str | None) -> str | None:
    if not value:
        return None
    normalized = normalize_object(value)
    if normalized in MONEY_OBJECTS:
        return "money"
    if normalized in TIME_OBJECTS:
        return normalize_time(normalized)
    return normalized


def normalize_time(value: str) -> str:
    value = normalize_object(value)
    if value.endswith("s") and len(value) > 3:
        value = value[:-1]
    return value


def normalize_object(value: str | None) -> str:
    value = (value or "").lower().strip()
    value = re.sub(r"[^a-z]", "", value)
    if value.endswith("ses") and len(value) > 4:
        value = value[:-2]
    elif value.endswith("ies"):
        value = value[:-3] + "y"
    elif value.endswith("s") and len(value) > 3:
        value = value[:-1]
    return value


def format_value(value: Any) -> str:
    try:
        fraction = Fraction(value)
    except Exception:
        return str(value)
    if fraction.denominator == 1:
        return str(fraction.numerator)
    return f"{fraction.numerator}/{fraction.denominator}"
