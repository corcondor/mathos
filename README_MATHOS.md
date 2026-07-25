# MathOS — 数学問題の生成・検証・新規性判定

小さなルーターが分類し、専門ツール(SymPy / Wolfram / Z3 / Shapely / Lean)が
仕事をする。LLM に全推論をさせず、**構造から問題を作り、ツールで解かせて検証**する。

## 難問生成の柱

- `construct_engine.py` — **対象構築エンジン**。難問のレシピ
  「[対象を構築] + [条件を課す] + [非自明を問う]」を実装。各族が別ツールで解く:
  - メビウス反復 ⇔ 2×2 行列のべき/固有値
  - Paley グラフ ⇔ 平方剰余の指標
  - 線形漸化式 mod m ⇔ 随伴行列の乗法的位数
  - 三次曲線の接線の再交点 ⇔ 記号的求解
  ツールが「構築した難しい対象」を計算可能にする。
- `world_novelty_check.py` — 難易度と新規性を客観評価。難易度はユーザー自作の
  難問 176 問(`problem_synthesis/local_hard_corpus.json`)で較正。
- `SIMILARITY.md` — 類似度・新規性の厳密な定義(文字 n-gram Jaccard + 完全一致
  ハッシュ + 構造署名)。表示値のハードコード(0.0)を廃し、必ず計算する。
- `build_construct_pool.py` — 生成 → 実類似度計算 → 世界新規のものを配信プールへ。
- `generate_and_curate.py` — 生成 → チェック → 難問かつ新規のものだけ残すループ。

## 解く骨格(既存)

`math_os.py --full-pipeline` で NL → 分野分類 → 型付き IR → ツール委譲 → 検証。
`--tool-status` で利用可能ツールを確認。

## 生成

```
python -m construct_engine                 # 対象構築問題を生成
python -m build_construct_pool --write-deploy   # 実類似度付きで配信プールへ
```

最新の問題数、難易度帯、検証ゲート、深層族の具体的な問題文は
[自律作問・検証レポート](docs/generated/latest-generation-report.md) に記録する。
この文書はプールから自動生成され、6時間ごとの自律生成でも更新される。

## 限界(正直に)

真の意味的新規性・難易度は「解法木の深さ」で測るのが理想で、これは解く網の
強化と一体。現状の難易度は構築/条件の表層特徴での較正近似。
