# 入れ子の二項係数方程式：全域に対する追加の絞り込み

更新日：2026年11月5日（日本時間）。

対象は、通常の二項係数が定義される非負整数についての

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}
\]

です。記号は

\[
A=\binom ij,\quad B=\binom{k}{\ell},\quad
M=\max(j,\ell),\quad t=A-B,\quad r=\min(B,t)
\]

とします。この追加検討では、前回の \(M\le20\) の検証範囲を広げることを主目的にせず、任意に大きい添字にも成り立つ評価と、無限個の候補を含む族の排除を導きました。

**全解の決定にはまだ至っていません。具体的な解も得ていません。以下は証明した必要条件と部分族の不存在です。**

## 1. 黄金比を含む新しい下限

\[
\varphi=\frac{1+\sqrt5}{2}
\]

とすると、すべての整数 \(1\le m<n\) で

\[
\boxed{\binom{n^2}{m^2}>\binom nm^{\varphi m}}
\]

を証明できます。二項エントロピー
\(h(x)=-x\log x-(1-x)\log(1-x)\)
に関するBoppanaの不等式
\(h(x^2)\ge\varphi xh(x)\)
を、Stirling公式の誤差まで含めて有限の二項係数に移したものです。

元の式には

\[
\boxed{r>\varphi j,\qquad t>\varphi M}
\]

が必要です。さらに

\[
(r-\varphi j)\log A>\log(r!)
\]

も必要です。したがって、上側の枝 \(t\le B\) では
\(t\ge\lfloor\varphi M\rfloor+1\) とできます。

係数 \(\varphi\) は、この単独の二項係数比較に対して最適です。
\(n\to\infty,\ m/n\to1/\varphi\) とすると対数の比が \(\varphi\) に近づきます。
これは、元の方程式の解がその境界に存在するという意味ではありません。

完全な証明：`entropy_phi_reduction.md`。

## 2. 比の単調性と上限の改善

\[
Q_m(n)=\frac{\binom{n^2}{m^2}}{\binom nm^{2m}},\qquad
q_m=\frac{(m!)^{2m}}{(m^2)!}
\]

とします。\(m\ge2\) では \(Q_m(n)\) は実数 \(n\ge m+1\) の範囲で厳密に減少します。
実数への拡張は、下側添字を固定した階乗多項式によります。
\(m=1\) では \(Q_1(n)=1\) です。

これにより

\[
\boxed{Q_m(n)\ge q_m},\qquad
\boxed{n\ge m+2\Longrightarrow Q_m(n)<16}
\]

が得られます。16という定数の評価は、\(m\) の有限表によらず解析的に証明しています。

前回の \(M\le20\) 排除と合わせ、残る全候補に

\[
\boxed{r<10M}
\]

が必要です。さらに \(M\ge800\) なら \(r<5M\) です。
最大の下側添字 \(M\) に対応する上側添字がそれぞれ \(M+3,M+4,M+5\) 以上なら、
\(M\ge21\) の全域で次の制限があります。

| 上側添字の条件 | 結論 |
|---|---|
| \(M+3\) 以上 | \(r<5M\) |
| \(M+4\) 以上 | \(r<4M\) |
| \(M+5\) 以上 | \(r<3M\) |

完全な証明：`sharp_q_bounds.md`。

## 3. ギャップが \(2M\) 以上なら、添字の差は対数程度に制限される

\(M\ge24\) とし、自然対数を用いて

\[
s=\lceil6\log(2M)\rceil
\]

と置くと、

\[
\boxed{r\ge2M\Longrightarrow A<\binom{M+s}{M}}
\]

を証明できます。右辺は

\[
\binom{M+s}{s}\le\left(\frac{e(M+s)}s\right)^s
=\exp\!\bigl(O((\log M)^2)\bigr)
\]

です。特に、\(j=M\) なら \(i<M+s\)、\(\ell=M\) なら \(k<M+s\) です。
例えば \(M=1000\) なら \(s=46\) なので、\(r\ge2000\) の候補では、その上側添字は1045以下です。

\(21\le M\le23\) については \(s=M\) とした
\(r\ge2M\Rightarrow A<\binom{2M}{M}\) が成り立ちます。
したがって全 \(M\ge21\) をまとめるには
\(s(M)=\min\{M,\lceil6\log(2M)\rceil\}\) と置けます。

完全な証明：`sharp_q_bounds.md`、第4・5節。

## 4. すべての枝に共通する厳密な高さの上限

全候補について

\[
\boxed{A(M!)^{2M}<(M^2)!}
\]

を証明しました。同じことを

\[
\boxed{A<H_M:=\frac{(M^2)!}{(M!)^{2M}}<e^{M^2}}
\]

とも書けます。\(H_M\) は一般には有理数であり、整数 \(A\) の範囲は
\(A\le\lceil H_M\rceil-1\) です。

この上限は \(B\le t\)、\(t\le B\) の両方を含みます。
特に、従来の評価で注意を要した \(\ell=M>j,\ k=M+1\) も残していません。
その場合は \(M+1\) と \(2j\) の大小を三つに分けて処理しています。

\[
i,k<e^{M^2},\qquad
i<j e^{M^2/j},\qquad k<\ell e^{M^2/\ell}
\]

も従います。\(M\) 自体にはまだ上限がないため、これで全域が有限探索になったわけではありません。

完全な証明：`global_height_bound.md`。新しい有限探索を用いない、全場合を含む解析的な証明です。

## 5. 全域で排除できた族

- **\(j=\ell\) はすべて不可能。** 小さい範囲は前回の証明データ、\(M\ge21\) は二項係数の増分とギャップ上限によって排除します。
- **\(t\le B\) かつ \(i-j=k-\ell\) はすべて不可能。** 共通の差が3以上なら二項係数の増分で排除します。差が2の場合は \(i\ge256\) を不等式で排除し、残る \(23\le i\le255\) の必要条件を満たす2,522組を厳密整数演算で確認しました。等式は0組です。
- **\(i=k=p\) または \(i=k=2p\)、\(p\) が素数、という族はすべて不可能。** 同じ二項係数の行における値の隔たりとLucasの合同式を使います。

一般の \(i=k=n\) でも、残る候補には

\[
\ell\in\{1,n-1\},\qquad B=r=n
\]

が必要です。さらに \(n=p^a\) なら \(p\mid j\) が必要です。

完全な証明：`continuation_arithmetic.md`。

有限部分の検証：

```bash
python verify_equal_complement_upper.py
```

実行済み結果は `verification_equal_complement_upper.json` に保存しています。
左辺が小さい946組、大きい1,576組、等しいもの0組でした。

## 6. 下側の枝の分類

\(B\le t\) では次のどちらかに限られます。

1. \(\ell>j\) の場合：
   \(k=\ell+1\)、\(B=\ell+1\)、\(j<(\ell+1)/\varphi\)。
2. \(j>\ell\) の場合：
   \(k\ge\ell+2\)、\(\varphi j<B<10j\)、\(\ell<\sqrt{20j}\)。
   \(\ell\ge2\) なら、さらに \(k(k-1)<20j\) です。
   \(\ell=1\) の場合の \(k\) は \(\varphi j<k<10j\) にあります。

`continuation_arithmetic.md` の分類に、第1・2節の新しい定数を適用したものです。

## 7. ファイルと検証の範囲

このZIPには、前回の \(M\le20\) の証明・コード・証明データ・独立検証結果も同梱しています。
前回の完全な証明データは次で再検証できます。

```bash
python verify_certificate_bundle.py 20
```

Python標準ライブラリのみで動きます。`assert` を使うため `-O` は付けないでください。
前回は63,237族をすべて検証し、未排除の族は0でした。

今回の新しい解析的な証明は、別担当による数学的な監査も行い、記載した評価と場合分けに問題は見つかりませんでした。
監査の記録とファイルのハッシュは `continuation_audit.json` にあります。
これはLeanによる形式検証の記録ではありません。今回Leanを実行してはいません。

## 8. 調査して実際に使った一次資料

- Ravi B. Boppana, [A Useful Inequality for the Binary Entropy Function](https://arxiv.org/abs/2301.09664), 2023。
  今回使った \(h(x^2)\ge\varphi xh(x)\) の証明。
- Boon Suan Ho, [A generalization of Boppana's entropy inequality](https://arxiv.org/html/2601.19327v1), 2026。
  同不等式の一般化。今回必要なのは、そのProposition 1に記載された二乗の場合です。
- [著者が公開したLeanコード](https://github.com/boonsuan/entropy-inequality)。
  2026年論文と対応するコードを確認しました。論文のRemarksにはAIによる証明支援と形式化への言及があります。
- Herbert Robbins, [A Remark on Stirling's Formula](https://doi.org/10.2307/2308012), 1955。
  有限の階乗に対する上下評価の定数を扱うために用いました。

これらの資料に元の方程式の完全解が掲載されているという主張ではありません。
二項係数への移行、ギャップ評価、高さの上限、部分族の排除は、同梱の証明で別途導出しています。
