# 入れ子の二項係数方程式：厳密な絞り込みと検証データ

対象は

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}
\]

です。右辺は「添字を二乗した二項係数」であり、二項係数の値の二乗ではありません。
通常の非負整数の範囲
\(0\le j\le i\)、\(0\le\ell\le k\)、\(\binom{k}{\ell}\le\binom ij\)
を対象にします。

## 得られた数学的な絞り込み

\[
A=\binom ij,\quad B=\binom{k}{\ell},\quad
M=\max(j,\ell),\quad r=\min(B,A-B)
\]
とすると、非自明な解は必ず

\[
j+2\le r<12M
\]

を満たします。さらに \(t=A-B\le B\) の場合には
\(M+2\le t<12M\) です。

この上限は、特定の数値範囲を試して推測したものではありません。
二項係数のエントロピー評価から、すべての正整数 \(M\) に対して証明しています。
証明の全体は `proof_reduction.md` にあります。

## N=20 の証明データ

次の全ケースについて排除証明を生成し、生成プログラムをインポートしない別実装の検証プログラムで全件の再検証に成功しました。

| 分類 | ケース数 | 証明方法 |
|---|---:|---|
| \(B\le A-B\) の \((j,\ell,k)\) | 3,207 | ある素数を法として、一変数の多項式に根がないこと |
| \(A-B\le B\) の \((j,\ell,t)\) | 43,784 | ある素数を法として、二つの多項式に共通の根がないこと |
| 同上で法 \(p\) だけでは残るケース | 16,246 | 証明済みの上限と、ヘンゼル持ち上げによる剰余条件の両立不能 |
| 合計 | 63,237 | 未排除ケース 0 |

これらの有限リストが全候補を覆うことも `proof_reduction.md` で証明しています。
独立検証では、初期の合同式の根 1,292,235 個と、持ち上げの計算 220,799 回を確認しました。
候補の全体を再生成し、漏れ・重複、素数の条件、根の全リスト、理論上の上限、各排除を検証しています。
最終結果は `verification_result_N20.json` にあり、`verification_passed` は `true`、未排除の族は 0 です。
したがって、

\[
\boxed{1\le j,\ell\le20\text{ の範囲には解が存在しない}}
\]

と結論できます。この主張は **\(i,k\) に任意の大きさを許した上での不存在** です。
\(i,k\le N\) のような任意の打ち切りによる四変数探索とは範囲が異なります。
上側の添字の有限上限は、各多項式族について数式から導出しています。

この結果から任意の \(j,\ell\) に対する不存在までは結論できません。
全体として解が存在するかどうかは、この成果物では決着していません。

## ファイル

- `proof_reduction.md`: 境界条件、全体に対する \(r<12M\)、各多項式族の上限、ヘンゼル持ち上げ、証明データの完全性の証明。
- `modular_reduction_experiment.py`: 多項式合同式に根がないことを示す素数を探し、証明データを生成するプログラム。
- `hensel_upper_experiment.py`: 残る二変数の合同式を厳密整数演算で持ち上げるプログラム。
- `modular_obstructions_N20.json`: 法 \(p\) での排除データと、次段階に渡すケース。
- `hensel_certificates_N20.json`: その全残余ケースについて、初期の共通根、用いた素数、終端の指数を記録したデータ。
- `verify_certificate_bundle.py`: Python 標準ライブラリだけで動作する独立検証プログラム。生成コードをインポートせず、階乗表、積の微分、桁ごとの持ち上げを別の形で実装しています。
- `verification_result_N20.json`: 全件の独立検証の結果、件数、証明データの SHA-256。
- `independent_verification_N20.log`: 独立検証の実行ログ。

`certified` という文字列自体を証拠にするのではなく、検証器が計算をやり直します。

## 同梱データの独立検証

ZIP を展開し、同じディレクトリ内で次を実行してください。こちらは NumPy を必要としません。

```bash
python verify_certificate_bundle.py 20
```

Python の `assert` による検証を使うため、`-O` オプションは付けないでください。
この実行では全件の検証に約278秒かかりました。実行環境によって時間は変わります。

## 生成計算の再実行

Python 3 と NumPy を用います。浮動小数点数による根の近似は用いません。

```bash
python modular_reduction_experiment.py 20 100 12
python hensel_upper_experiment.py 20 30
```

第1コマンドで作られた未排除リストを、第2コマンドが処理します。
特異な根を根拠なく捨てる処理はありません。区間条件で排除できない特異根があれば別の素数を試し、処理が完了しなければ未解決として残します。

## 具体例：\((j,\ell,t)=(2,3,5)\)

上側の枝 \(t=A-B\le B\) で、この族は

\[
\binom i2-\binom k3=5,\qquad
\binom{\binom i2}{5}=\binom{i^2}{4}+\binom{k^2}{9}
\]

となります。証明した上限から

\[
A\le46,448,640,\quad i\le13,632,\quad k\le1,080
\]

が必要です。法13での共通根は二つだけで、どちらもヤコビ行列式は法13で12です。
そのため、各根は13の累乗を法として一意に持ち上がります。

| 法 | 第1の根 \((i,k)\) | 第2の根 \((i,k)\) |
|---:|---:|---:|
| \(13\) | \((8,5)\) | \((12,11)\) |
| \(13^2=169\) | \((8,57)\) | \((168,167)\) |
| \(13^4=28,561\) | \((5247,9521)\) | \((28560,28559)\) |

両方とも \(k\) の最小非負剰余が1,080を超えます。
したがって、上限を満たす正整数 \(k\) は存在せず、この族全体に解はありません。
ここでは任意の探索打ち切りではなく、数式から証明した上限を使っています。

## 調査した公開資料と今回の使い方

調査日：2026年11月5日（日本時間）。スター数はこの時点の目安です。

| 公開プロジェクト | スター数の目安 | 調べた内容 |
|---|---:|---|
| [OpenAI math](https://github.com/openai/math) | 約17,300 | 公開論文の目録、証明資料、形式化の有無と検証状態 |
| [Anthropic formal-math](https://github.com/anthropics/formal-math) | 約460 | 問題文・証明・検証対象の固定と、独立した検証 |
| [Anthropic Fermat's Last Theorem](https://github.com/anthropics/fermats-last-theorem) | 約1,300 | `FinalCheck.lean` による最終命題と公理依存性の確認 |
| [SageMath](https://github.com/sagemath/sage) | 約2,600 | `hensel_lift` の実装とニュートン反復 |
| [mathlib4](https://github.com/leanprover-community/mathlib4) | 約4,400 | Kummer・Lucas の定理、ヘンゼルの補題の定式化 |
| [Danus](https://github.com/frenzymath/Danus) | 約500 | 補題と依存関係を保存し、探索と独立検証を分ける構成 |
| [MathCode](https://github.com/math-ai-org/mathcode) | 約750 | 証明候補と検証済みの結果の管理 |

これらのリポジトリに、この方程式そのものの完全解が掲載されているという主張ではありません。
今回の計算は同梱の Python コードで行いました。Claude の非公開研究モデル、SageMath、Lean を実行したという意味ではありません。

数学的な根拠として特に直接的なのは、次の資料です。

- Keith Conrad, [A Multivariable Hensel's Lemma](https://kconrad.math.uconn.edu/blurbs/gradnumthy/multivarhensel.pdf), Theorem 3.3。二変数・二方程式に用いる局所的一意性の条件に対応します。
- Herbert Robbins, [A Remark on Stirling's Formula](https://dornsife.usc.edu/sergey-lototsky/wp-content/uploads/sites/211/2024/02/Stirling-Robbins.pdf), 1955。エントロピー評価の定数を正確に扱うために使っています。
- [SageMath の hensel_lift の説明](https://doc.sagemath.org/html/en/reference/polynomial_rings/sage/rings/polynomial/polynomial_element_generic.html)。ニュートン反復による持ち上げの実装例です。

Anthropicの公式報告も確認しました。

- [Learning more about Claude's mathematical capabilities](https://www.anthropic.com/research/riemann-zeta)
- [Formalizing Fermat's Last Theorem](https://www.anthropic.com/research/formalizing-fermats-last-theorem)

本件で必要なのは、素数を法とする条件と整数解の上限を結び付けることです。
ヘンゼルの補題だけでは整数解の不存在は結論できず、上限と完全な初期根リストがそろって初めて今回の排除が成立します。
