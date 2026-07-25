"""Run MathOS against small public benchmark samples.

The runner deliberately separates three metrics:
1. typed_kernel_ok: the problem compiles into typed definitions.
2. answered: MathOS returned any answer.
3. exact_match: returned answer matches the dataset answer by simple exact/numeric checks.
"""

from __future__ import annotations

import argparse
import json
import multiprocessing as mp
import queue
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

try:
    import sympy as sp
except ImportError:  # pragma: no cover
    sp = None

try:
    from math_os_prototype.reasoning_pipeline import run_reasoning_pipeline
    from math_os_prototype.typed_definition_kernel import compile_typed_definition_ir
    from math_os_prototype.web_app import extract_answer_from_pipeline_data
except ImportError:
    from reasoning_pipeline import run_reasoning_pipeline
    from typed_definition_kernel import compile_typed_definition_ir
    from web_app import extract_answer_from_pipeline_data


MATH_CONFIGS = (
    "algebra",
    "counting_and_probability",
    "geometry",
    "intermediate_algebra",
    "number_theory",
    "prealgebra",
    "precalculus",
)


@dataclass
class PublicBenchmarkCase:
    benchmark: str
    subset: str
    index: int
    problem: str
    expected: str | None


@dataclass
class PublicBenchmarkRecord:
    benchmark: str
    subset: str
    index: int
    domain: str
    intent: str
    typed_status: str
    verification: str
    expected: str | None
    answer: str | None
    exact_match: bool | None
    error: str | None
    problem_preview: str


def fetch_hf_rows(dataset: str, config: str, split: str, length: int, offset: int = 0) -> list[dict[str, Any]]:
    if length > 100:
        rows: list[dict[str, Any]] = []
        remaining = length
        cursor = offset
        while remaining > 0:
            batch_length = min(100, remaining)
            batch = fetch_hf_rows(dataset, config, split, batch_length, cursor)
            rows.extend(batch)
            if len(batch) < batch_length:
                break
            cursor += batch_length
            remaining -= batch_length
        return rows
    query = urllib.parse.urlencode(
        {
            "dataset": dataset,
            "config": config,
            "split": split,
            "offset": offset,
            "length": length,
        }
    )
    url = f"https://datasets-server.huggingface.co/rows?{query}"
    cache_dir = Path("math_os_prototype/.hf_rows_cache")
    cache_dir.mkdir(parents=True, exist_ok=True)
    cache_key = re.sub(r"[^A-Za-z0-9_.-]+", "_", f"{dataset}_{config}_{split}_{offset}_{length}")
    cache_path = cache_dir / f"{cache_key}.json"
    if cache_path.exists():
        payload = json.loads(cache_path.read_text(encoding="utf-8"))
    else:
        last_error: Exception | None = None
        for attempt in range(5):
            try:
                with urllib.request.urlopen(url, timeout=60) as response:
                    payload = json.loads(response.read().decode("utf-8"))
                cache_path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
                break
            except urllib.error.HTTPError as error:
                last_error = error
                if error.code not in {429, 500, 502, 503, 504}:
                    raise
                time.sleep(2**attempt)
        else:
            assert last_error is not None
            raise last_error
    return [item["row"] for item in payload.get("rows", [])]


def load_gsm8k_cases(limit: int) -> list[PublicBenchmarkCase]:
    rows = fetch_hf_rows("openai/gsm8k", "main", "test", limit)
    cases = []
    for index, row in enumerate(rows):
        cases.append(
            PublicBenchmarkCase(
                benchmark="GSM8K",
                subset="test",
                index=index,
                problem=row["question"],
                expected=extract_gsm8k_answer(row["answer"]),
            )
        )
    return cases


def load_math_cases(per_config: int) -> list[PublicBenchmarkCase]:
    cases: list[PublicBenchmarkCase] = []
    for config in MATH_CONFIGS:
        rows = fetch_hf_rows("EleutherAI/hendrycks_math", config, "test", per_config)
        for index, row in enumerate(rows):
            cases.append(
                PublicBenchmarkCase(
                    benchmark="MATH",
                    subset=config,
                    index=index,
                    problem=row["problem"],
                    expected=extract_boxed_answer(row.get("solution", "")),
                )
            )
    return cases


def load_svamp_cases(limit: int) -> list[PublicBenchmarkCase]:
    rows = fetch_hf_rows("ChilleD/SVAMP", "default", "test", limit)
    cases = []
    for index, row in enumerate(rows):
        cases.append(
            PublicBenchmarkCase(
                benchmark="SVAMP",
                subset=str(row.get("Type") or "test"),
                index=index,
                problem=row.get("question_concat") or f"{row.get('Body', '')} {row.get('Question', '')}".strip(),
                expected=normalize_answer(row.get("Answer")),
            )
        )
    return cases


def load_asdiv_cases(limit: int) -> list[PublicBenchmarkCase]:
    rows = fetch_hf_rows("yimingzhang/asdiv", "default", "test", limit)
    cases = []
    for index, row in enumerate(rows):
        cases.append(
            PublicBenchmarkCase(
                benchmark="ASDiv",
                subset="test",
                index=index,
                problem=normalize_asdiv_prompt(row["text"]),
                expected=normalize_answer(row.get("label")),
            )
        )
    return cases


def load_aqua_cases(limit: int) -> list[PublicBenchmarkCase]:
    rows = fetch_hf_rows("hails/agieval-aqua-rat", "default", "test", limit)
    cases = []
    for index, row in enumerate(rows):
        gold = row.get("gold") or []
        choices = row.get("choices") or []
        expected = None
        if gold and choices:
            expected = normalize_aqua_choice(choices[int(gold[0])])
        cases.append(
            PublicBenchmarkCase(
                benchmark="AQuA-RAT",
                subset="test",
                index=index,
                problem=row["query"],
                expected=expected,
            )
        )
    return cases


def load_multiarith_cases(limit: int) -> list[PublicBenchmarkCase]:
    rows = fetch_hf_rows("ChilleD/MultiArith", "default", "test", limit)
    cases = []
    for index, row in enumerate(rows):
        cases.append(
            PublicBenchmarkCase(
                benchmark="MultiArith",
                subset="test",
                index=index,
                problem=row["question"].strip(),
                expected=normalize_answer(row.get("final_ans")),
            )
        )
    return cases


def load_mawps_cases(limit: int) -> list[PublicBenchmarkCase]:
    rows = fetch_hf_rows("MU-NLPC/Calc-mawps", "default", "test", limit)
    cases = []
    for index, row in enumerate(rows):
        cases.append(
            PublicBenchmarkCase(
                benchmark="MAWPS",
                subset="test",
                index=index,
                problem=row["question"],
                expected=normalize_answer(row.get("result")),
            )
        )
    return cases


def run_public_benchmark(
    *,
    gsm8k: int = 0,
    math_per_config: int = 0,
    svamp: int = 0,
    asdiv: int = 0,
    aqua: int = 0,
    multiarith: int = 0,
    mawps: int = 0,
    live_retrieval: bool = False,
    external_tools: bool = False,
    allow_surface_morphisms: bool = False,
    case_timeout: float | None = None,
) -> dict[str, Any]:
    cases: list[PublicBenchmarkCase] = []
    if gsm8k:
        cases.extend(load_gsm8k_cases(gsm8k))
    if math_per_config:
        cases.extend(load_math_cases(math_per_config))
    if svamp:
        cases.extend(load_svamp_cases(svamp))
    if asdiv:
        cases.extend(load_asdiv_cases(asdiv))
    if aqua:
        cases.extend(load_aqua_cases(aqua))
    if multiarith:
        cases.extend(load_multiarith_cases(multiarith))
    if mawps:
        cases.extend(load_mawps_cases(mawps))

    records: list[PublicBenchmarkRecord] = []
    for case in cases:
        if case_timeout and case_timeout > 0:
            records.append(
                run_case_with_timeout(
                    case,
                    live_retrieval=live_retrieval,
                    external_tools=external_tools,
                    allow_surface_morphisms=allow_surface_morphisms,
                    timeout=case_timeout,
                )
            )
        else:
            records.append(
                run_case(
                    case,
                    live_retrieval=live_retrieval,
                    external_tools=external_tools,
                    allow_surface_morphisms=allow_surface_morphisms,
                )
            )
    return summarize(records)


def run_case(
    case: PublicBenchmarkCase,
    *,
    live_retrieval: bool = False,
    external_tools: bool = False,
    allow_surface_morphisms: bool = False,
) -> PublicBenchmarkRecord:
    try:
        typed_ir = compile_typed_definition_ir(case.problem)
        result = run_reasoning_pipeline(
            case.problem,
            external_tools=external_tools,
            live_retrieval=live_retrieval,
            allow_specialized=allow_surface_morphisms,
        )
        data = json.loads(result.to_json())
        answer = extract_answer_from_pipeline_data(data)
        match = answers_match(answer, case.expected) if case.expected is not None else None
        return PublicBenchmarkRecord(
            benchmark=case.benchmark,
            subset=case.subset,
            index=case.index,
            domain=data["domain_ir"]["domain"],
            intent=data["parser"]["intent"],
            typed_status=typed_ir.status,
            verification=data["verification"]["status"],
            expected=case.expected,
            answer=answer,
            exact_match=match,
            error=None,
            problem_preview=case.problem[:220],
        )
    except Exception as exc:
        return error_record(case, str(exc))


def run_case_with_timeout(
    case: PublicBenchmarkCase,
    *,
    live_retrieval: bool = False,
    external_tools: bool = False,
    allow_surface_morphisms: bool = False,
    timeout: float,
) -> PublicBenchmarkRecord:
    result_queue: mp.Queue = mp.Queue(maxsize=1)
    process = mp.Process(
        target=_case_worker,
        args=(case, live_retrieval, external_tools, allow_surface_morphisms, result_queue),
    )
    process.start()
    process.join(timeout)
    if process.is_alive():
        process.terminate()
        process.join(2)
        return error_record(case, f"case_timeout_after_{timeout:g}s", verification="timeout")
    try:
        payload = result_queue.get_nowait()
    except queue.Empty:
        return error_record(case, "case_worker_returned_no_record")
    return PublicBenchmarkRecord(**payload)


def _case_worker(
    case: PublicBenchmarkCase,
    live_retrieval: bool,
    external_tools: bool,
    allow_surface_morphisms: bool,
    result_queue: mp.Queue,
) -> None:
    record = run_case(
        case,
        live_retrieval=live_retrieval,
        external_tools=external_tools,
        allow_surface_morphisms=allow_surface_morphisms,
    )
    result_queue.put(asdict(record))


def error_record(case: PublicBenchmarkCase, error: str, *, verification: str = "error") -> PublicBenchmarkRecord:
    return PublicBenchmarkRecord(
        benchmark=case.benchmark,
        subset=case.subset,
        index=case.index,
        domain="error",
        intent="error",
        typed_status="error",
        verification=verification,
        expected=case.expected,
        answer=None,
        exact_match=False if case.expected is not None else None,
        error=error,
        problem_preview=case.problem[:220],
    )


def summarize(records: list[PublicBenchmarkRecord]) -> dict[str, Any]:
    total = len(records)
    typed_ok = sum(record.typed_status == "type_checked" for record in records)
    answered = sum(bool(record.answer) for record in records)
    comparable = [record for record in records if record.expected is not None]
    exact = sum(record.exact_match is True for record in comparable)
    by_benchmark: dict[str, dict[str, int]] = {}
    for record in records:
        bucket = by_benchmark.setdefault(record.benchmark, {"total": 0, "typed_ok": 0, "answered": 0, "exact": 0})
        bucket["total"] += 1
        bucket["typed_ok"] += int(record.typed_status == "type_checked")
        bucket["answered"] += int(bool(record.answer))
        bucket["exact"] += int(record.exact_match is True)
    return {
        "total": total,
        "typed_kernel_ok": typed_ok,
        "typed_kernel_ok_rate": typed_ok / total if total else 0.0,
        "answered": answered,
        "answered_rate": answered / total if total else 0.0,
        "comparable": len(comparable),
        "exact_match": exact,
        "exact_match_rate": exact / len(comparable) if comparable else 0.0,
        "by_benchmark": by_benchmark,
        "records": [asdict(record) for record in records],
    }


def extract_gsm8k_answer(answer: str) -> str | None:
    match = re.search(r"####\s*([^\n]+)", answer)
    return normalize_answer(match.group(1)) if match else None


def extract_boxed_answer(solution: str) -> str | None:
    match = re.search(r"\\boxed\{([^{}]+)\}", solution)
    if match:
        return normalize_answer(match.group(1))
    return None


def normalize_asdiv_prompt(text: str) -> str:
    text = re.sub(r"^\s*Question:\s*", "", text.strip())
    text = re.sub(r"\s*Answer:\s*$", "", text.strip())
    return text.strip()


def normalize_aqua_choice(choice: str) -> str:
    choice = re.sub(r"^\([A-E]\)\s*", "", choice.strip())
    return normalize_answer(choice) or choice.strip()


def answers_match(answer: str | None, expected: str | None) -> bool:
    if not answer or expected is None:
        return False
    answer_norm = normalize_answer(answer)
    expected_norm = normalize_answer(expected)
    if answer_norm == expected_norm:
        return True
    if sp is None:
        return False
    try:
        a = sp.sympify(clean_for_sympy(answer_norm))
        b = sp.sympify(clean_for_sympy(expected_norm))
        return bool(sp.simplify(a - b) == 0)
    except Exception:
        return False


def normalize_answer(value: str | None) -> str | None:
    if value is None:
        return None
    raw = str(value).strip()
    value = raw
    value = value.strip("$ ")
    value = value.replace(",", "")
    if "," in raw and re.fullmatch(r"[-\d\s]+", value):
        value = re.sub(r"\s+", "", value)
    value = value.replace("\\%", "%")
    value = value.replace("Бу", "sqrt")
    value = re.sub(r"^\\boxed\{(.+)\}$", r"\1", value)
    value = re.sub(r"^\([A-E]\)\s*", "", value)
    return value.strip()


def clean_for_sympy(value: str) -> str:
    value = value.replace("–", "-").replace("−", "-")
    value = value.replace("^", "**")
    value = value.replace("\\frac", "frac")
    value = re.sub(r"frac\{([^{}]+)\}\{([^{}]+)\}", r"(\1)/(\2)", value)
    value = re.sub(r"frac(-?\d+)(-?\d+)", r"(\1)/(\2)", value)
    value = value.replace("\\sqrt", "sqrt")
    value = re.sub(r"sqrt\{([^{}]+)\}", r"sqrt(\1)", value)
    value = value.replace("√", "sqrt")
    value = value.replace("Бу", "sqrt")
    value = re.sub(r"sqrt\s*([0-9]+)", r"sqrt(\1)", value)
    value = value.replace("\\pi", "pi")
    value = re.sub(r"(?<=\d)(?=\()", "*", value)
    value = re.sub(r"(?<=\d)(?=[abcxyz])", "*", value)
    value = re.sub(r"(?<=[abcxyz])(?=[abcxyz])", "*", value)
    value = re.sub(r"(?<=\d)(?=sqrt)", "*", value)
    return value


def write_outputs(result: dict[str, Any], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    with output.with_suffix(".jsonl").open("w", encoding="utf-8") as handle:
        for record in result["records"]:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run MathOS on public benchmark samples.")
    parser.add_argument("--gsm8k", type=int, default=0)
    parser.add_argument("--math-per-config", type=int, default=0)
    parser.add_argument("--svamp", type=int, default=0)
    parser.add_argument("--asdiv", type=int, default=0)
    parser.add_argument("--aqua", type=int, default=0)
    parser.add_argument("--multiarith", type=int, default=0)
    parser.add_argument("--mawps", type=int, default=0)
    parser.add_argument("--live-retrieval", action="store_true")
    parser.add_argument("--external-tools", action="store_true")
    parser.add_argument(
        "--allow-surface-morphisms",
        action="store_true",
        help="Enable direct surface-morphism adapters as an ablation, not as the cold MathOS path.",
    )
    parser.add_argument("--case-timeout", type=float, default=None, help="Optional per-problem timeout in seconds.")
    parser.add_argument("--output", type=Path, default=Path("math_os_prototype/public_benchmark_results.json"))
    return parser


def main() -> int:
    args = build_arg_parser().parse_args()
    result = run_public_benchmark(
        gsm8k=args.gsm8k,
        math_per_config=args.math_per_config,
        svamp=args.svamp,
        asdiv=args.asdiv,
        aqua=args.aqua,
        multiarith=args.multiarith,
        mawps=args.mawps,
        live_retrieval=args.live_retrieval,
        external_tools=args.external_tools,
        allow_surface_morphisms=args.allow_surface_morphisms,
        case_timeout=args.case_timeout,
    )
    write_outputs(result, args.output)
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    print(f"records: {args.output}")
    print(f"jsonl: {args.output.with_suffix('.jsonl')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
