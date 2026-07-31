"""Build the structurally diverse Japanese entrance-mathematics pool."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

try:
    from math_os_prototype.continuous_problem_generation import (
        build_batch_report,
    )
    from math_os_prototype.entrance_scope import certify_entrance_scope
    from math_os_prototype.geometry_fusion_synthesis import (
        synthesize as synthesize_geometry,
    )
except ImportError:  # pragma: no cover - direct script execution
    from continuous_problem_generation import build_batch_report
    from entrance_scope import certify_entrance_scope
    from geometry_fusion_synthesis import synthesize as synthesize_geometry


HERE = Path(__file__).resolve().parent
DEFAULT_CONSTRUCT = HERE / "problem_synthesis" / "construct_pool.json"
DEFAULT_OUTPUT = HERE / "problem_synthesis" / "entrance_exam_pool.json"
DEFAULT_REPORT = (
    HERE / "docs" / "generated" / "latest-entrance-pool-report.md"
)

# 配信に出す最低限の手数。操作数と難易度の実測から決めた閾値。
MIN_MORPHISMS = 3

# 難易度の下限。過去問 28,074 問の 90% 点が 8.38 なので、
# 「過去問の上位1割より難しい」を最低ラインにする。
# これを下回るものは、作れても配信しない。
MIN_DIFFICULTY = 8.4


def _structure_key(problem: dict[str, Any]) -> str:
    lift = problem.get("lift_certificate") or {}
    payload = {
        "family_id": problem.get("family_id"),
        "morphism_chain": lift.get("morphism_chain") or [],
        "constraint_skeleton": lift.get("constraint_skeleton") or [],
        "query_signature": lift.get("query_signature") or "",
    }
    encoded = json.dumps(
        payload,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def _verified(problem: dict[str, Any]) -> bool:
    verification = problem.get("verification") or {}
    lift = problem.get("lift_certificate") or {}
    novelty = problem.get("novelty") or {}
    return bool(
        problem.get("accepted")
        and verification.get("exact_backend")
        and verification.get("independent_check")
        and lift.get("type_checked")
        and novelty.get("corpus_novel")
    )


def _records(payload: dict[str, Any]) -> Iterable[dict[str, Any]]:
    for problem in payload.get("problems", []):
        if isinstance(problem, dict):
            yield problem


def _traceback_report() -> dict[str, Any]:
    """トレースバック方式（演繹閉包の各ノード）の生成物。"""
    try:
        from math_os_prototype.traceback_engine import synthesize as synthesize_traceback
    except ImportError:  # pragma: no cover
        try:
            from traceback_engine import synthesize as synthesize_traceback
        except ImportError:
            return {"problems": []}
    try:
        return synthesize_traceback()
    except Exception:
        return {"problems": []}


def _compose_report() -> dict[str, Any]:
    """構築の合成（構築Aの導出値を構築Bのパラメータへ渡す）。"""
    try:
        from math_os_prototype.compose_engine import synthesize as synthesize_compose
    except ImportError:  # pragma: no cover
        try:
            from compose_engine import synthesize as synthesize_compose
        except ImportError:
            return {"problems": []}
    try:
        return synthesize_compose()
    except Exception:
        return {"problems": []}


def _relation_report() -> dict[str, Any]:
    """厳密な関係証明書を持つ最大最小・不等式問題。"""
    try:
        from math_os_prototype.relation_engine import synthesize as synthesize_relation
    except ImportError:  # pragma: no cover
        try:
            from relation_engine import synthesize as synthesize_relation
        except ImportError:
            return {"problems": []}
    try:
        return synthesize_relation()
    except Exception:
        return {"problems": []}


def _novelty_checker():
    """過去問コーパスに対して実際に類似度を計算する検査を返す。

    生成器は novelty を True と 0.0 で直書きしていた（3つとも）。
    つまり「過去問に出たことがあるか」は一度も測られていなかった。
    ここで 28,000 問のコーパスと突き合わせて本当に測る。
    """
    try:
        from math_os_prototype.world_novelty_check import (
            load_jukenmath_hashes, load_world_corpus, surface_ngrams, world_novelty,
        )
    except ImportError:  # pragma: no cover
        from world_novelty_check import (
            load_jukenmath_hashes, load_world_corpus, surface_ngrams, world_novelty,
        )
    world = load_world_corpus()
    grams = [(row["source"], surface_ngrams(row["statement"])) for row in world]
    hashes = load_jukenmath_hashes()

    def check(statement: str) -> dict[str, Any]:
        return world_novelty(statement, grams, hashes)

    check.corpus_size = len(grams)  # type: ignore[attr-defined]
    return check


def _difficulty_score(problem: dict[str, Any]) -> float:
    try:
        from math_os_prototype.world_novelty_check import difficulty
    except ImportError:  # pragma: no cover
        from world_novelty_check import difficulty
    return float(difficulty(problem).get("score", 0.0))


def build_pool(
    construct_path: Path = DEFAULT_CONSTRUCT,
) -> dict[str, Any]:
    construct = json.loads(construct_path.read_text(encoding="utf-8"))
    sources = (
        ("construct_atlas", _records(construct)),
        (
            "typed_continuous",
            _records(build_batch_report([], [], [])),
        ),
        ("geometry_fusion", _records(synthesize_geometry())),
        ("traceback_closure", _records(_traceback_report())),
        ("closure_composition", _records(_compose_report())),
        ("relation_closure", _records(_relation_report())),
    )
    retained: dict[str, dict[str, Any]] = {}
    rejected = Counter()
    source_counts = Counter()
    novelty_check = _novelty_checker()
    for source, records in sources:
        for problem in records:
            if not _verified(problem):
                rejected["verification"] += 1
                continue
            # 操作数（射の連鎖の長さ）が短すぎるものは配信しない。
            # 113問で測ったところ、射の数と難易度スコアの相関は +0.469 で、
            # 操作数 2 のノードは平均難易度 3.90（他は 5〜14）だった。
            # 手数が少ない問題は実際に易しい。
            lift = problem.get("lift_certificate") or {}
            if len(lift.get("morphism_chain") or []) < MIN_MORPHISMS:
                rejected["too_few_operations"] += 1
                continue
            certificate = certify_entrance_scope(problem)
            if certificate is None:
                rejected["scope_lowering"] += 1
                continue

            # 実際に過去問コーパスと突き合わせる
            statement = str(problem.get("statement_tex") or "")
            novelty = novelty_check(statement)
            if not novelty["world_novel"]:
                rejected["seen_in_past_exams"] += 1
                continue

            # 易しい問題は残さない。難しさの下限はここで切る。
            score = _difficulty_score(problem)
            if score < MIN_DIFFICULTY:
                rejected["too_easy"] += 1
                continue
            key = _structure_key(problem)
            if key in retained:
                rejected["same_structure_variant"] += 1
                continue
            record = dict(problem)
            # 高校の語彙へ書き換えた文章を配信本文として採用する。
            if certificate.get("surface_rewritten"):
                record["statement_tex"] = certificate["statement_tex_lowered"]
                record["solution_tex"] = certificate["solution_tex_lowered"]
                record["statement_tex_original"] = problem.get("statement_tex")
            record["curriculum_certificate"] = certificate
            record["structure_key"] = key
            # 直書きの 0.0 を、実測した類似度で上書きする
            record["novelty"] = {
                "corpus_novel": True,
                "maximum_surface_jaccard": novelty["max_surface_jaccard"],
                "closest_source": novelty["closest_source"],
                "reference_corpus_size": novelty_check.corpus_size,
                "measured": True,
            }
            record["difficulty_score"] = score
            record["source_generator"] = source
            retained[key] = record
            source_counts[source] += 1

    problems = sorted(
        retained.values(),
        key=lambda item: (
            str(item.get("domain")),
            str(item.get("family_id")),
            str(item.get("candidate_id")),
        ),
    )
    family_counts = Counter(p["family_id"] for p in problems)
    domain_counts = Counter(p["domain"] for p in problems)
    geometry_algebra = sum(
        count
        for domain, count in domain_counts.items()
        if any(token in domain for token in ("geometry", "algebra", "complex"))
    )
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "method": {
            "name": "MathOS Japanese entrance-mathematics structural pool",
            "pipeline": (
                "typed object -> morphism composition -> exact backend -> "
                "independent check -> upper-secondary lowering -> "
                "structural quotient"
            ),
            "selection_unit": (
                "family_id + morphism_chain + constraint_skeleton + "
                "query_signature"
            ),
            "numeric_variants_count_as_new": False,
        },
        "summary": {
            "total_instances": len(problems),
            "certified_structures": len(retained),
            "families": len(family_counts),
            "family_counts": dict(family_counts),
            "domain_counts": dict(domain_counts),
            "geometry_algebra_structures": geometry_algebra,
            "surface_rewritten": sum(
                1
                for p in problems
                if (p.get("curriculum_certificate") or {}).get("surface_rewritten")
            ),
            "source_counts": dict(source_counts),
            "rejected": dict(rejected),
        },
        "problems": problems,
    }


def render_report(report: dict[str, Any]) -> str:
    summary = report["summary"]
    lines = [
        "# MathOS 大学受験数学プール監査",
        "",
        "この文書は受験用配信プールから機械的に生成した記録である。",
        "問題インスタンス数ではなく、数値変種を除いた構造数を数える。",
        "",
        "## 結果",
        "",
        f"- 検証済み構造: **{summary['certified_structures']}**",
        f"- 構造族: **{summary['families']}**",
        f"- 幾何・代数・複素数系: **{summary['geometry_algebra_structures']}**",
        f"- 高校の語彙へ書き換えた問題: "
        f"**{summary.get('surface_rewritten', 0)}**",
        f"- 同一構造の数値変種として除外: "
        f"**{summary['rejected'].get('same_structure_variant', 0)}**"
        "（生成時点で潰しているため通常は 0）",
        f"- 高校の語彙へ還元できず除外: "
        f"**{summary['rejected'].get('scope_lowering', 0)}**",
        "",
        "## 採用契約",
        "",
        "```text",
        "型付き数学対象",
        "  -> 射の合成",
        "  -> 厳密backend計算",
        "  -> 独立検算",
        "  -> 数I/A・II/B・III/Cの原始操作へのlowering",
        "  -> 構造署名で商を取り、数値違いを除外",
        "  -> Discord配信",
        "```",
        "",
        "判定は族の名前では行わない。射の連鎖が高校の原始操作へ還元できるか、",
        "そして問題文と解法が高校の語彙で書けるかだけを見る。",
        "内部探索で大学数学の概念を使うこと自体は禁止しない。",
        "行列で導いた一次分数変換も、平方剰余で作ったグラフも、",
        "問題文を高校の言葉で書き直せる限り受験用プールへ出す。",
        "書き直せない候補だけを研究キューに残す。",
        "",
        "## 構造一覧",
        "",
        "| 分野 | 構造族 | lowering |",
        "|---|---|---|",
    ]
    for problem in report["problems"]:
        certificate = problem["curriculum_certificate"]
        lines.append(
            f"| `{problem['domain']}` | `{problem['family_id']}` | "
            f"`{' -> '.join(certificate['lowering_chain'])}` |"
        )
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--construct", type=Path, default=DEFAULT_CONSTRUCT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()
    report = build_pool(args.construct)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(
            json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True)
        )
    args.report.parent.mkdir(parents=True, exist_ok=True)
    with args.report.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(render_report(report))
    print(json.dumps(report["summary"], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
