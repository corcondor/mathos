# MathOS Generalization Lift Contract

## 目的

MathOS で「汎化した」と言うための条件を固定する。問題文の表層語句や数値を覚えて答える経路は、汎化として扱わない。

## 汎化の定義

二つの問題が同じ構造に lift できたと言えるのは、次が一致するときだけ。

1. theory path  
   例: `Logic -> Set -> OrderedField -> VectorSpace -> InnerProductSpace`

2. typed morphism chain  
   例: `Difference -> Norm -> Distance`

3. constraint skeleton  
   数値・局所変数名をパラメータ化した後の制約形。

4. query signature  
   例: `compute_metric:Real:Distance(P,P)` のような、求める対象の型と射。

5. backend contract  
   同じ backend 射で検証可能であること。

この5条件が揃ったときだけ、数値や文面が変わっても同じ解法経路を使ってよい。

## 例

距離問題:

```text
Find the distance from the origin to the point (3,4).
Compute the distance from the origin to the point (5,12).
```

どちらも:

```text
Theory: InnerProductSpace
Objects: Point2
Morphisms: Difference -> Norm -> Distance
Query: Distance(O,P) : Real
Backend: coordinate norm simplification
```

なので同じ構造。

等差数列:

```text
What is the 100th term of the arithmetic sequence 6 10 14?
Find the 50th term of the arithmetic sequence 2 5 8.
```

どちらも:

```text
Theory: DiscreteDynamicalSystem over OrderedField
Morphisms: ArithmeticProgression -> CommonDifference -> NthTerm
Query: NthTerm(seq,N) : Real
Backend: affine recurrence solver
```

なので同じ構造。

## 汎化ではないもの

- `if "100th term" in text` のような語句分岐。
- 問題番号・ベンチマークID・既知答えへの分岐。
- 数値を変えると壊れる式直書き。
- `allfield_*` surface morphism adapter の正答数増加を、そのまま核の改善と呼ぶこと。

## 実装上の対応

- `theory_atlas.py`
  - `TheoryNode`
  - `MorphismSchema`
  - `LiftCertificate`
  - `canonical_graph_signature`
  - `compare_lift_structures`

- `category_semantics.py`
  - `TypedSemanticGraph.lift_certificates` に lift 証明書を出す。

## 次の実装原則

新しい解法部品を足すときは、先に `LiftCertificate` と backend contract を定義する。直接 solver を追加する場合は、`allow_specialized` 配下の ablation として扱い、cold path の汎化改善とは分けて報告する。
