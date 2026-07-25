"""自律生成ループ: 誰も見ていない時も MathOS が問題を作り続ける。

GitHub Actions の cron から定期的に呼ばれ、1 回の実行で

  1. 全族から候補を生成（役割: 合成 composer）
  2. ツールで検証（役割: 検証 verifier）— 未検証は捨てる
  3. 世界コーパス + 既存プールと照合（役割: 新規性 novelty）
  4. 難易度を評価して記録（役割: 評価 grader）
  5. 既存プールに **蓄積** して書き戻す（置き換えではない）

を行う。プールは実行のたびに育つ。同じ問題は (family, answer) と正規化
問題文で重複排除されるので、何度回しても水増しにならない。
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    from math_os_prototype.construct_engine import synthesize as gen_construct
    from math_os_prototype.world_novelty_check import (
        difficulty,
        load_jukenmath_hashes,
        load_world_corpus,
        world_novelty,
    )
    from math_os_prototype.jukenmath_full_audit import canonical_surface, surface_ngrams
except ImportError:  # pragma: no cover
    from construct_engine import synthesize as gen_construct
    from world_novelty_check import (
        difficulty,
        load_jukenmath_hashes,
        load_world_corpus,
        world_novelty,
    )
    from jukenmath_full_audit import canonical_surface, surface_ngrams


HERE = Path(__file__).resolve().parent
POOL = HERE / "problem_synthesis" / "construct_pool.json"
# 1族が支配して水増しにならないための上限（多様性優先）
PER_FAMILY_CAP = 40
LOG = HERE / "problem_synthesis" / "autonomous_log.json"


def load_pool() -> dict[str, Any]:
    if POOL.exists():
        try:
            return json.loads(POOL.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            pass
    return {"problems": []}


def run_once(max_new: int | None = None) -> dict[str, Any]:
    pool = load_pool()
    existing = pool.get("problems", [])
    seen_answer = {
        (p.get("family_id"), canonical_surface(str(p.get("answer_tex", ""))))
        for p in existing
    }
    seen_stmt = {canonical_surface(str(p.get("statement_tex", ""))) for p in existing}

    # 1. 合成
    generated = gen_construct()["problems"]

    # 3. 新規性の材料
    world = load_world_corpus()
    world_grams = [(r["source"], surface_ngrams(r["statement"])) for r in world]
    juken = load_jukenmath_hashes()

    added: list[dict[str, Any]] = []
    stats = {"generated": len(generated), "dup": 0, "not_novel": 0, "unverified": 0}

    for p in generated:
        # 2. 検証（ツールが通していないものは捨てる）
        v = p.get("verification", {})
        if not (v.get("exact_backend") and v.get("independent_check")):
            stats["unverified"] += 1
            continue
        akey = (p["family_id"], canonical_surface(p["answer_tex"]))
        skey = canonical_surface(p["statement_tex"])
        if akey in seen_answer or skey in seen_stmt:
            stats["dup"] += 1
            continue
        nov = world_novelty(p["statement_tex"], world_grams, juken)
        if not nov["world_novel"]:
            stats["not_novel"] += 1
            continue
        d = difficulty(p)  # 4. 評価
        record = {
            "accepted": True,
            "candidate_id": p["candidate_id"],
            "domain": p["domain"],
            "family_id": p["family_id"],
            "tool": p.get("tool", ""),
            "difficulty": {
                "band": d["band"], "score": d["score"],
                "construct": d["construct"], "condition": d["condition"],
            },
            "statement_tex": p["statement_tex"],
            "answer_tex": p["answer_tex"],
            "solution_tex": p["solution_tex"],
            "lift_certificate": p["lift_certificate"],
            "verification": p["verification"],
            "novelty": {
                "corpus_novel": True,
                "maximum_surface_jaccard": nov["max_surface_jaccard"],
                "closest_source": nov["closest_source"],
            },
        }
        added.append(record)
        seen_answer.add(akey)
        seen_stmt.add(skey)
        if max_new is not None and len(added) >= max_new:
            break

    # 5. 蓄積。1族が支配して水増しにならないよう上限を設け、難易度上位を残す。
    merged = existing + added
    from collections import Counter, defaultdict

    by_family: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for r in sorted(merged, key=lambda r: -r.get("difficulty", {}).get("score", 0)):
        if len(by_family[r["family_id"]]) >= PER_FAMILY_CAP:
            continue
        by_family[r["family_id"]].append(r)
    interleaved: list[dict[str, Any]] = []
    queues = list(by_family.values())
    while any(queues):
        for q in queues:
            if q:
                interleaved.append(q.pop(0))

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "method": {
            "name": "MathOS autonomous pool",
            "loop": "compose -> verify -> novelty -> grade -> accumulate",
            "similarity_definition": "SIMILARITY.md",
        },
        "summary": {
            "total": len(interleaved),
            "added_this_run": len(added),
            "previous": len(existing),
            "world_corpus_size": len(world),
            "family_counts": dict(Counter(r["family_id"] for r in interleaved)),
            "band_counts": dict(
                Counter(r.get("difficulty", {}).get("band", "?") for r in interleaved)
            ),
            "run_stats": stats,
        },
        "problems": interleaved,
    }
    POOL.parent.mkdir(parents=True, exist_ok=True)
    POOL.write_text(
        json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8"
    )

    # 実行ログを追記（自律運転の履歴）
    history = []
    if LOG.exists():
        try:
            history = json.loads(LOG.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            history = []
    history.append(
        {
            "at": report["generated_at"],
            "added": len(added),
            "total": len(interleaved),
            **stats,
        }
    )
    LOG.write_text(json.dumps(history[-200:], ensure_ascii=False, indent=2), encoding="utf-8")
    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-new", type=int, default=None)
    parser.add_argument("--deploy", action="store_true", help="配信バンドルにも書き出す")
    args = parser.parse_args()
    report = run_once(max_new=args.max_new)
    if args.deploy:
        for target in (
            Path("C:/Users/81808/sakumon-station/data/mathos/continuous_verified_problem_batch1.json"),
            Path("C:/Users/81808/.openclaw/workspace/discord-bot/mathos_batches/continuous_verified_problem_batch1.json"),
        ):
            if target.parent.exists():
                target.write_text(
                    json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True),
                    encoding="utf-8",
                )
    print(json.dumps(report["summary"], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
