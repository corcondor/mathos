# v64：元の二項係数方程式に整数解があれば、第一楕円商のMordell–Weil階数は必ず正

2026-11-08。研究対象は主枝 \(\ell=1,\ j=i-3\) に限る。ここでいう楕円曲線の階数は固定された有理数 \(T=\rho/b^2\) に対する**有理点群 \(E_{1,T}(\mathbb Q)\)** の階数であり、v33〜v43で調べた**関数体上の幾何学的切断の階数とは異なる**。

## 統一定理（残差 \(\rho\) の上限なし）

\[
E_{1,T}:\quad y^2+6xy+(8+9T)y=x^3,\quad
T=\rho/b^2>0,\quad
\rho\in\mathbb Z_{>0},\quad b\mid486
\]
とする。主枝の元の二項係数方程式
\[
\binom{\binom ij}{\binom k\ell}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2},
\quad \ell=1,\quad j=i-3
\]
に整数解があれば、その解から構成される残差 \(\rho\)、原始係数 \(b\) について
\[
\boxed{\operatorname{rank}E_{1,\rho/b^2}(\mathbb Q)\ge1.}\tag{64.1}
\]
これは**必要条件**であり、正階数だから元の方程式に解があるとは主張しない。残差の巨大な数値探索や任意の高さ上限も使わない。

### 証明1：Mazur定理と判別式で捩れ群の型を限定

\(P=(0,0)\) は位数3の有理点で、
\[
\Delta=-243T(8+9T)^3<0.
\]
したがってMazurの有理捩れ分類と、非巡回な \(\mathbb Z/2\oplus\mathbb Z/6\) を負の判別式で排除することから、
\[
E_{1,T}(\mathbb Q)_{\mathrm{tors}}\cong
\mathbb Z/3,\quad\mathbb Z/6,\quad\mathbb Z/9,\quad\mathbb Z/12
\tag{64.2}
\]
の4種類のみとなる（[v58](V58_BAD_REDUCTION_HIGH_TORSION_SIEVE_ja.md)）。

### 証明2：12位数と9位数の全パラメータを分類

**12位数：** [v63](V63_UNIFORM_TWELVE_TORSION_EXCLUSION_ja.md) により、第一楕円商の有理12位数点は \(T=\rho/b^2>0,\ b\mid486\) の全てで**存在しない**。2位数点の4-除法を6本の四次Thue方程式へ落とし、無条件 PARI solver で全整数解を認証した。
**9位数：** [v61](V61_UNCONDITIONAL_NINE_TORSION_THUE_CLASSIFICATION_ja.md) により、存在するパラメータは
\[
\boxed{T=46648/9}
\tag{64.3}
\]
の1種類のみ。こちらも20本の三次Thue方程式の全整数解をPARI flag=1で認証した。独立の[v62 Sage rank証明](https://github.com/corcondor/mathos/actions/runs/42462716966)により
\[
E_{1,46648/9}(\mathbb Q)\cong\mathbb Z/9,\qquad
C_{46648/9}(\mathbb Q)=\{\infty_+,\infty_-\}.
\tag{64.4}
\]
従って、この特例では元の整数解に必要な**有限な種数2有理点が存在しない**。

### 証明3：残りの階数0群は3または6

(64.4)の特例を除けば、もし \(\operatorname{rank}E_{1,T}(\mathbb Q)=0\) なら、(64.2)とv63から全群は有限で \(\mathbb Z/3\) または \(\mathbb Z/6\) のみ。

- **捩れ3：** [v50](V50_FIRST_QUOTIENT_ALL_GENUS2_RATIONAL_POINTS_ja.md) で、種数2曲線からの像は \(x=0\) に限られるため、元の解の必要な**厳密不等式** \(u^2>1+T\) と矛盾する。
- **捩れ6：** [v56](V56_UNIFORM_TORSION_SIX_OBSTRUCTION_ja.md) は2位数の有理パラメータ \(v\) を使い、元の \(t,n\) 復元式から無限範囲を排除した。\(v>5\) は \(n<104\)、\(1<v<5\) は \(d^3\mid2b^2\) により588完全構造候補へ縮約、唯一の平方型 \(v=4\) でも \(n=0\) または28となり、\(n\ge104\) に反する。

よってrank0は全ての有理捩れ群の場合で排除された。主枝の元の解が存在すれば必ずrank≥1。定理(64.1)を得た。\(\square\)

## 明確な解釈と限界

**実際に一様に分類できたもの**は、第一楕円商の**有理捩れ群**：
\[
\boxed{
E_{1,\rho/b^2}(\mathbb Q)_{\rm tors}
\cong\begin{cases}
\mathbb Z/9,&\rho/b^2=46648/9,\\
\mathbb Z/3\ \text{または}\ \mathbb Z/6,&\text{それ以外}.
\end{cases}
}\tag{64.5}
\]
一方、**第一楕円商の全有理点は正階数の場合に無限個**であり、それらが種数2曲線へ持ち上がるかどうかは未解決。第二楕円商 \(E_{2,T}(\mathbb Q)\) の各有理数特殊化の飽和済みMW基底も未決定。元の四変数方程式全体の解は未解決。

また、(64.1)は二項係数問題の指定された主枝とv20の原始係数・整数復元条件に依存する。証明はKubert/Mazurの既知の一般定理、楕円群法則、局所代数計算と、無条件Thueの完全計算を組み合わせた**記述・計算機援用証明**であり、Lean形式化・外部査読はまだ実施していない。

## 完全計算の証拠

- [9位数を20三次Thueで完全分類した無条件PARIログ](https://github.com/corcondor/mathos/actions/runs/42462323854)
- [唯一の9位数曲線の階数0とCの全有理点2個のSage認証](https://github.com/corcondor/mathos/actions/runs/42462716966)
- [12位数を6四次Thueで無条件排除したPARIログ](https://github.com/corcondor/mathos/actions/runs/42463177794)
- [12位数パラメータと付値の独立SymPy監査](https://github.com/corcondor/mathos/actions/runs/42463260604)
- [6位数の全無限残差一様排除と588完全有限証明](https://github.com/corcondor/mathos/actions/runs/42459815542)

## 次の本質的課題

1. 正階数の第一楕円商の点 \(P=(x,y)\) が種数2曲線へ持ち上がるには、\(\boxed{x+1+T\in\mathbb Q^2}\) が必要。この平方被覆をChabauty・Mordell–Weil sieveなどで、実際の特殊化曲線のrank/基底と照合する。
2. 二つの楕円商を同時に使うMordell–Weilふるいを、\(\rho\) 無制限に適用できる形へ拡張する。
3. 本文の捩れ6および9/12のThue有限証明書の検査器、v20の原始整数復元条件をLean形式化する。
