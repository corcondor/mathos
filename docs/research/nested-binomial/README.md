# 入れ子の二項係数方程式の研究記録

\[
\boxed{\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}}
\]

右辺は上下の添字を二乗した二項係数。通常の非負整数の範囲で扱う。

**状態：全体の解の分類は未完了。具体的な解も未発見。**
部分的な無限族の排除と必要条件を記録する。
必要条件を満たすことを、元の式の解であることとは扱わない。

## 読み始める場所

- [v5 日本語概要](PROGRESS_v5_ja.md)
- [v4 日本語概要](PROGRESS_v4_ja.md)
- [ell=1、j=i-3 の区間・付値の証明](v5_offset_three_structure.md)
- [i=3^a の全指数の排除](v5_offset_three_three_power.md)
- [i=jp^3 の一候補への絞り込みと高次合同式](v5_large_prime_localization.md)
- [v5 の Lean 検証範囲・実行方法](v5_formal/README.md)

## 2026年11月5日の基準点：v5

ell=1、j=i-3、r=min(k,C(i,3)-k) について、
3i<r<10i/3 を証明した。その上で、
i/gcd(i,3) が平方因子を持たない場合、i=3^a、13^a、19^a、
および任意の素数 p に対する i=p^2,p^4 を排除した。

別の残存形 i=jp^3、k=p、ell=1 は、明示的な実関数の根の近傍へ
j を絞り、各素数 p につき高々一候補にした。さらに調和数の
法 p^5 の必要条件を導いた。この族の全排除はまだできていない。

ell>j の下側 k=ell+1=b の分岐でも、8j/3<=b<=4j を排除し、
隣接する 5j/2<=b<8j/3 では i=j+4 の形だけに絞った。
各主張の仮定・依存する前段階の証明は、それぞれのノートに明記している。

## 証明と検証の区別

1. 数学的証明：Markdown の各ノートに、無限範囲を含む議論を記す。
2. 有限証明書：まず理論的に有限範囲へ還元し、各候補を排除する
   素数・剰余等を生成する。独立した列挙・計算法で検証する。
3. Lean：実際に実行したソース・ログ・バージョンを記録する。
   明示的な仮定として残している解析評価まで形式化済みとはしない。
4. 実験・未完了の方向：必要条件と観察だけで、解なしの定理にしない。

v4・v5 の元ファイルは、その時点の記録として保存している。
後続の結果は新しい版名で追加し、訂正が必要になった場合は
旧主張と訂正理由を明示する。

## 再計算

このディレクトリを作業場所にする。代表的な小さい検算は Python の
標準ライブラリだけで実行できる。

    python3 v5_offset_three_checks.py
    python3 v5_large_prime_localization_checks.py

v5 の有限証明書を再生成して独立検証する場合：

    python3 v5_l1_expanded_band.py generate
    python3 v5_l1_expanded_band.py verify
    python3 v5_l1_offset_four.py generate
    python3 v5_l1_offset_four.py verify

前段階の再計算方法は各証明ノート、スクリプトの説明、
v4_formal/README.md と v5_formal/README.md を参照。

## 大きい生成済み証明書

Git には証明、生成器、独立検証器、小さい結果記録を収録した。
100 KB を超える生成済み証明書やバイナリ出力の一部は収録していない。
省略した16ファイルの名前・サイズ・SHA-256、および基準アーカイブとの
対応は [ARCHIVE_MANIFEST.json](ARCHIVE_MANIFEST.json) にある。

完全な生成済み証明書を含む以前のアーカイブ：
[nested_binomial_progress_v2.zip](https://chatgpt.com/library?file_id=libfile_77d5da929dd481918744ac98b12a8e70&account_id=personal)。
リンク先の利用には所有者のアクセス権が必要。再生成器はこのディレクトリにある。
Lean の実行環境本体と mathlib の依存チェックアウトは Git に含めない。

## 現在残る主な課題

- ell=1、j=i-3 の未排除の合成数・素数冪。
- i=jp^3 の唯一の実数評価候補と、高い精度の合同条件の両立。
- 下側 i=j+4 の残存区間、およびその他の未排除分岐。

これらはこの研究記録の未完了部分であり、既知の未解決問題であると
分類したという意味ではない。
