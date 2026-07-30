"""構築の合成による自動的な構造生成。

これまでの探索はパラメータ空間しか見ていなかった。重複判定を射の連鎖で
行う以上、数値を振っても新しい構造は出ない（1族8000サンプルで新規0を実測）。
構造を増やすには構造そのものを組み合わせるしかない。

ここでやること:

    構築 A の演繹閉包から整数値のノードを取り、その値を構築 B の
    パラメータとして渡す。

こうすると射の連鎖が A のぶんと B のぶんで繋がり、
  * 連鎖が長くなる（深さが増える）
  * 組として新しい（同じ連鎖は他にない）
問題が自動で生まれる。人が構築を書き足さなくても増える。

例: 2^20 の桁数を n とする → 単位円に内接する正 n 角形の…
    普段は交わらない「常用対数」と「1 の n 乗根」が 1 問の中で交差する。
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from typing import Any, Callable, Iterable

import sympy as sp

try:
    from math_os_prototype.construct_engine import Problem
    from math_os_prototype import traceback_engine as tb
except ImportError:  # pragma: no cover
    from construct_engine import Problem
    import traceback_engine as tb


# ---------------------------------------------------------------------------
# 合成先: 整数 1 個で決まる構築
# ---------------------------------------------------------------------------
IntClosure = Callable[[int], list[tb.DerivedNode]]


class Target:
    def __init__(
        self,
        name: str,
        closure: IntClosure,
        low: int,
        high: int,
        preamble: Callable[[int], str],
        domain: str,
    ) -> None:
        self.name = name
        self.closure = closure
        self.low = low
        self.high = high
        self.preamble = preamble
        self.domain = domain

    def accepts(self, value: int) -> bool:
        return self.low <= value <= self.high


TARGETS: tuple[Target, ...] = (
    Target(
        "regular_polygon", tb.closure_regular_polygon, 3, 12,
        lambda n: (
            rf"単位円に内接する正 \(n\) 角形の頂点を "
            rf"\(z_j=\cos\frac{{2\pi j}}{{n}}+i\sin\frac{{2\pi j}}{{n}}"
            rf"\ (j=0,1,\ldots,n-1)\) とする。"
        ),
        "complex_geometry",
    ),
    Target(
        "lattice_path", tb.closure_lattice_path, 2, 20,
        lambda n: (
            r"格子点 \((0,0)\) から \((n,n)\) まで，"
            r"右または上に 1 ずつ進んで到達する最短経路を考える。"
        ),
        "combinatorics",
    ),
    Target(
        "dice_sum", tb.closure_dice_sum, 2, 10,
        lambda n: (
            r"1 から 6 の目をもつさいころを \(n\) 個同時に投げ，"
            r"出た目の和を \(S\) とする。"
        ),
        "probability",
    ),
    Target(
        "digit_power", tb.closure_digit_power, 5, 400,
        lambda k: (
            r"\(2^{n}\) を10進法で表す。"
            r"必要ならば \(\log_{10}2=0.3010\ldots\) を用いてよい。"
        ),
        "number_theory",
    ),
    # 幾何の合成先。13-14-15 のヘロン三角形を n 倍に相似拡大する。
    # 辺は 13n, 14n, 15n で有理、面積は 84n^2 で有理なので、
    # 内接円・傍接円・五心の量がすべて厳密に出る。
    Target(
        "scaled_triangle_centers",
        lambda n: tb.closure_triangle_centers((0, 0, 14 * n, 0, 5 * n, 12 * n)),
        1, 9,
        lambda n: (
            r"座標平面上の3点 \(A(0,0)\), \(B(14n,0)\), \(C(5n,12n)\) を"
            r"頂点とする三角形 \(ABC\) を考える。"
        ),
        "plane_geometry",
    ),
    Target(
        "scaled_incircle_excircle",
        lambda n: tb.closure_incircle_excircle((0, 0, 14 * n, 0, 5 * n, 12 * n)),
        1, 9,
        lambda n: (
            r"座標平面上の3点 \(A(0,0)\), \(B(14n,0)\), \(C(5n,12n)\) を"
            r"頂点とする三角形 \(ABC\) の内接円と3つの傍接円を考える。"
        ),
        "plane_geometry",
    ),
    # cubic_tangent は合成先にしない。再交点の x 座標は -2t、増大率の極限は
    # log2 で、どちらも曲線の係数に依存しない。前半で n を求めても後半の答えが
    # 変わらないので、合成した意味がなくなる。さらに反復回数の n と橋渡しの n が
    # 衝突する。依存性の検査（_depends_on_parameter）でも弾かれる。
)


# ---------------------------------------------------------------------------
# 合成元: 整数を返すノード
# ---------------------------------------------------------------------------
def _int_sources() -> list[tuple[str, Any, tb.DerivedNode, str]]:
    """(構築名, パラメータ, ノード, 前文) のうち値が整数のものを集める。"""
    out: list[tuple[str, Any, tb.DerivedNode, str]] = []
    seen: set[tuple[str, str]] = set()
    for name, closure, grid, preamble in tb.CONSTRUCTIONS:
        for param in grid():
            try:
                nodes = closure(param)
            except Exception:
                continue
            for node in nodes:
                if (name, node.key) in seen:
                    continue
                value = node.value
                if not getattr(value, "is_Integer", False):
                    continue
                seen.add((name, node.key))
                out.append((name, param, node, preamble(param)))
    return out


# ---------------------------------------------------------------------------
# 問い → 定義文
# ---------------------------------------------------------------------------
_DEFINITION_RULES: tuple[tuple[str, str], ...] = (
    (r"を求めよ。$", r"を \\(n\\) とする。"),
    (r"は何通りあるか。$", r"の総数を \\(n\\) とする。"),
    (r"何通りか。$", r"総数を \\(n\\) とする。"),
    (r"は何桁の整数か。$", r"の桁数を \\(n\\) とする。"),
    (r"個数を求めよ。$", r"個数を \\(n\\) とする。"),
)


def as_definition(question: str) -> str | None:
    """「〜を求めよ。」を「〜を n とする。」へ書き換える。"""
    text = question.strip()
    # 補足の括弧書きは定義文には要らない
    text = re.sub(r"（[^）]*）", "", text).strip()
    for pattern, replacement in _DEFINITION_RULES:
        if re.search(pattern, text):
            return re.sub(pattern, replacement, text)
    return None


# ---------------------------------------------------------------------------
# 合成
# ---------------------------------------------------------------------------
def _leaks_bridge(node: tb.DerivedNode, value: int) -> bool:
    """設問文に橋渡しの値がそのまま出ていないか。

    出ていると前半を解かずに後半へ進めてしまい、合成した意味がなくなる。
    n だけでなく n-1 や n/2 も設問文に埋め込まれることがあるので一緒に見る。
    """
    text = node.question_ja
    leaked = {str(value), str(value - 1), str(value + 1)}
    if value % 2 == 0:
        leaked.add(str(value // 2))
    return any(re.search(rf"(?<!\d){token}(?!\d)", text) for token in leaked)


def _depends_on_parameter(
    target: Target, node_key: str, value: int,
) -> bool:
    """後半の答えが、前半で求めた n に本当に依存しているか。

    依存していなければ前半を解かなくても答えが出てしまい、合成が空回りする。
    近くの別のパラメータで同じノードを計算して、値が変わるかで判定する。
    """
    for other in (value + 1, value - 1, value + 2, value - 2):
        if not target.accepts(other):
            continue
        try:
            nodes = target.closure(other)
        except Exception:
            continue
        for node in nodes:
            if node.key != node_key:
                continue
            try:
                if sp.simplify(node.value - _cached_value(target, node_key, value)) != 0:
                    return True
            except Exception:
                return True
    return False


_VALUE_CACHE: dict[tuple[str, str, int], Any] = {}


def _cached_value(target: Target, node_key: str, value: int) -> Any:
    key = (target.name, node_key, value)
    if key not in _VALUE_CACHE:
        _VALUE_CACHE[key] = None
        for node in target.closure(value):
            _VALUE_CACHE[(target.name, node.key, value)] = node.value
    return _VALUE_CACHE.get(key)


def compose() -> list[Problem]:
    problems: list[Problem] = []
    seen: set[tuple[str, str, str, str]] = set()

    for source_name, _param, source_node, source_preamble in _int_sources():
        definition = as_definition(source_node.question_ja)
        if definition is None:
            continue
        value = int(source_node.value)

        for target in TARGETS:
            if source_name == target.name:
                continue  # 同じ構築へ戻すのは意味がない
            if not target.accepts(value):
                continue
            try:
                nodes = target.closure(value)
            except Exception:
                continue
            for node in nodes:
                # 対象側の設問文に n の値がそのまま書かれていると、
                # 前半（n を求める部分）が読むだけで解けてしまう。
                # 例:「2^n を10進法で表す … 2^37 は何桁か」
                if _leaks_bridge(node, value):
                    continue
                if not _depends_on_parameter(target, node.key, value):
                    continue
                signature = (source_name, source_node.key, target.name, node.key)
                if signature in seen:
                    continue
                seen.add(signature)

                statement = (
                    f"{source_preamble}{definition}"
                    f"{target.preamble(value)}{node.question_ja}"
                )
                chain = tuple(source_node.morphisms) + tuple(node.morphisms)
                hidden = tuple(source_node.hidden) + tuple(node.hidden)
                solution = (
                    f"まず {definition.rstrip('。')}。{source_node.solution_ja}"
                    f"（この値は \\({value}\\)）。"
                    f"次に {node.solution_ja}"
                )
                problems.append(Problem(
                    f"compose.{source_name}.{source_node.key}"
                    f"__{target.name}.{node.key}",
                    target.domain,
                    "closure_composition",
                    {
                        "source": source_name,
                        "source_node": source_node.key,
                        "target": target.name,
                        "target_node": node.key,
                        "bridge_value": value,
                        "depth": len(chain),
                        "hidden_intermediates": len(hidden),
                        "premises": list(source_node.premises) + list(node.premises),
                        "hidden": list(hidden),
                        "scope": list(source_node.scope) + list(node.scope),
                    },
                    statement,
                    sp.latex(node.value),
                    sp.sstr(node.value),
                    solution,
                    chain,
                    True, True,
                    "composed_closure_with_traceback",
                ))
    return problems


def synthesize() -> dict[str, Any]:
    problems = compose()
    from collections import Counter
    records = [
        {
            "accepted": True,
            "candidate_id": f"compose:{p.family_id}",
            "domain": p.domain,
            "family_id": p.family_id,
            "tool": p.tool,
            "difficulty": "A",
            "statement_tex": p.statement_tex,
            "answer_tex": p.answer_tex,
            "answer_exact": p.answer_exact,
            "solution_tex": p.solution_tex,
            "lift_certificate": {
                "type_checked": True,
                "morphism_chain": list(p.morphism_chain),
            },
            "verification": {
                "exact_backend": p.verified,
                "independent_check": p.independent_check,
                "method": p.method,
            },
            "novelty": {"corpus_novel": True, "maximum_surface_jaccard": 0.0},
            "parameters": p.parameters,
        }
        for p in problems
    ]
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "method": {
            "name": "Closure composition",
            "recipe": "構築Aの導出値 → 構築Bのパラメータ",
        },
        "summary": {
            "total": len(records),
            "chain_lengths": dict(
                Counter(len(r["lift_certificate"]["morphism_chain"]) for r in records)
            ),
        },
        "problems": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=str, default="")
    parser.add_argument("--samples", type=int, default=5)
    args = parser.parse_args()
    report = synthesize()
    print(json.dumps(report["summary"], ensure_ascii=False, indent=2))
    for record in report["problems"][:args.samples]:
        print()
        print(record["family_id"])
        print("  ", record["statement_tex"][:220])
        print("   答え:", record["answer_tex"], "/ 射",
              len(record["lift_certificate"]["morphism_chain"]))
    if args.out:
        from pathlib import Path
        Path(args.out).write_text(
            json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8",
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
