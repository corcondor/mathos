# v102：未処理だった p∤i を直接解析 — 法p²の一意復元・eの無理数度・p進局所可解性

日付 2026-11-11。原方程式は添字を二乗する入れ子二項係数
\[
\binom{\binom{i}{j}}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}.
\]
本ノートはv100/v101の枝 j=1, ell=k-1 で k=p が素数の場合の **p∤i** を解析し、無限族の新たな厳密排除と、単独のp進法では決着しない理由を証明する。以前のSに有限上限を設ける探索とは独立。原の全四変数方程式を解いたとは主張しない。

## 記号と既存の解析的な高さ

p≥5 を素数、R_p=C(p²,2p−1) とする。元の式は
\[
\boxed{\binom{i}{p}=i^2+R_p,\qquad i\ge p.}\tag{102.1}
\]
v101の全称不等式により、(102.1) が成立するなら
\[
2p<i<p^3.
\]
従って i=pq+r, 0≤r<p と書けば 0≤q<p²。v101で r=0（p|i）は全域排除済みなので、以後1≤r<p。

v100のStirling展開・正の逆二項曲線の唯一交差から、仮に(102.1)の解が存在するなら、素数pが増大する際、
\[
\boxed{\frac{q}{p^2}=\frac e4+O\left(\frac{\log p}{p}\right).}\tag{102.2}
\]
O定数はpとrに依存しない。（i/p³ と q/p² の差はr/p³=O(p^-2)。）

## 定理1：mod p² の一意桁復元

H_0=0, H_r=∑_{t=1}^r 1/t とする（r<pなのでp進整数）。任意の整数q≥0、0≤r<pに対して
\[
\boxed{\binom{pq+r}{p}\equiv q(1+pH_r)\pmod{p^2}.}\tag{102.3}
\]

証明：Vandermondeで
\[
\binom{pq+r}{p}=\sum_{s=0}^r\binom rs\binom{pq}{p-s}.
\]
pは奇素数。階乗積と H_{p−1}≡0 (mod p) から
\[
\binom{pq}{p}=q\binom{pq-1}{p-1}\equiv q\pmod{p^2}.
\]
一方 1≤s≤r<p では
\[
\binom{pq}{p-s}=\frac{pq}{p-s}\binom{pq-1}{p-s-1}
\equiv pq\frac{(-1)^{s-1}}s\pmod{p^2}.
\]
従って有限二項恒等式
\(\sum_{s=1}^r(-1)^{s-1}\binom rs/s=H_r\)
を使えば(102.3)が出る。全ての分母はp単元なので厳密なZ_(p)合同式。

また \(p^2\mid R_p\) は \((2p-1)R_p=p^2\binom{p^2-1}{2p-2}\) とgcd(2p−1,p)=1から分かる。元の式と(102.3)より
\[
q(1+pH_r)\equiv r^2+2pqr\pmod{p^2}.
\]
係数 \(1+p(H_r-2r)\) は法p²で逆元を持つから
\[
\boxed{q\equiv r^2\{1+p(2r-H_r)\}\pmod{p^2}.}\tag{102.4}
\]
0≤q<p²により、**rを1個選べばqもiも完全に一意**。ここには任意の数値探索上限なし。これで「非p整除のi」を全てp−1剰余クラス（その各クラスで高々1候補）へ転換した。

特に q≡r² (mod p)、よってqは0でない平方剰余。p∤qは既存v101のKummer付値に一致。

## 定理2：さらに全素数p≥5で i≡1 (mod p) は無解

r=1ならH_1=1、(102.4)から
\[
q\equiv1+p\pmod{p^2},\quad0≤q<p²
\Longrightarrow q=p+1,\quad \boxed{i=p^2+p+1}.
\]
だが任意のp≥5について
\[
\boxed{\binom{p^2+p+1}{p}<\binom{p^2}{2p-1}=R_p.}\tag{102.5}
\]
以下、全pに通用する厳密な不等式で証明する。
\[
\frac{R_p}{\binom{p^2}{p}}
=\frac{\binom{p^2-p}{p-1}}{\binom{2p-1}{p}}
=\prod_{h=0}^{p-2}\frac{p^2-p-h}{2p-1-h}
>2^{p-1}\ge16,
\]
なぜならp²−p≥4pで各因子が2より大きい。一方
\[
\frac{\binom{p^2+p+1}{p}}{\binom{p^2}{p}}
=\prod_{h=0}^{p-1}\left(1+\frac{p+1}{p^2-h}\right)
\le(1+2/p)^p<e^2<8.
\]
従って(102.5)。元の等式は左辺 >R_p でなければならないので矛盾。
\[
\boxed{\forall p\ge5\ \text{prime},\quad
j=1,\ \ell=k-1,\ k=p,\ i\equiv1\bmod p
\Longrightarrow\text{解なし}.}\tag{102.6}
\]
これは旧v101の p|i 全排除と**互いに異なる**新しい無限族を解決した。

## 定理3：両端の剰余類は、対数幅にわたり全素数で排除

**主張：任意の実数0<η<1/2についてP_ηが存在し、p>P_ηなる素数pで(102.1)の整数解が存在するなら**
\[
\boxed{\min\{r,p-r\}>
\left(\frac12-\eta\right)\log p.}\tag{102.7}
\]
ここでr=i mod p∈{1,...,p−1}。pやiに任意の数値探索上限は置かない。証明は(102.4)、Euler数の無理数度µ(e)=2（既知定理）、素数定理の同値形式 \(\log\operatorname{lcm}(1,\ldots,n)\sim n\) を用いる。

【左端 r≪log p】
D_r=lcm(1,...,r), A_r=D_r H_r∈Z とおく。
(102.4)にD_rを掛けると整数mについて
\[
D_rq=D_rr^2+p r^2(2rD_r-A_r)+p^2m.
\]
従って
\[
\frac q{p^2}=\frac m{D_r}+\frac{r^2}{p^2}
+\frac{r^2(2r-H_r)}p.
\]
(102.2)と \(0\le H_r\le r\) から、もしr≤(1/2−η)log pなら
\[
\left|\frac e4-\frac m{D_r}\right|
=O\left(\frac{(\log p)^3}{p}\right).\tag{102.8}
\]
しかし素数定理による \(\log D_r\le(1+o(1))r\) から、十分大きいpでは
\[
D_r\le p^{1/2-\eta/2}.
\]
µ(e/4)=2なので任意のδ>0に対してcδ>0が存在し、
\[
\left|\frac e4-\frac m{D_r}\right|
\ge c_\delta D_r^{-2-\delta}.
\]
δを \((1/2-\eta/2)(2+\delta)<1\) となるよう小さく選ぶ。すると下界はp^{-β}（β<1）以上、上界はO(log³p/p)で矛盾。

【右端 s=p−r≪log p】
H_{p−1}≡0 (mod p)なので H_{p-s}≡H_{s-1} (mod p)。(102.4)から
\[
q\equiv s^2-p(2s+2s^3+s^2H_{s-1})\pmod{p^2}.
\]
E_s=lcm(1,...,s−1)とすると適当な整数mで
\[
\frac q{p^2}=\frac m{E_s}+\frac{s^2}{p^2}
-\frac{2s+2s^3+s^2H_{s-1}}p.
\]
よってs≤(1/2−η)log pを仮定すると同じ無理数度・PNTの矛盾。両端が排除され、(102.7)を得る。

**追加系**：任意に固定した正整数cに対し、十分大きなpで
i≡c または i≡−c (mod p) となる解はない。より強く cを(1/2−η)logp以内で増やしても排除できる。

素数定理を使いたくない場合は \(D_r\le r!\le r^r\) のみで同じ議論が動き、弱いながら完全に初等的な
\[
\boxed{\min(r,p-r)>
\left(\frac12-\eta\right)\frac{\log p}{\log\log p}}
\]
を十分大きなpに対して得る（µ(e)=2は既知の外部定理として残す）。

## 定理4：局所的p進法だけで全解を排除するのは不可能

任意の素数p≥5と0≤r<pについて、qのp進多項式
\[
F_r(Q)=Q\,\frac{\prod_{0\le j<p,\ j\ne r}(pQ+r-j)}{(p-1)!}
-(pQ+r)^2-R_p\in\mathbb Z_p[Q]
\]
を定義。非負整数qなら厳密に
\(F_r(q)=\binom{pq+r}p-(pq+r)^2-R_p\)。
積の係数をmod pで見ると
\[
\frac{\prod_{j\ne r}(r-j)}{(p-1)!}
=\frac{(-1)^{p-1-r}}{\binom{p-1}r}
\equiv1\pmod p,
\]
なので
\[
\boxed{F_r(Q)\equiv Q-r^2\pmod p,\qquad
F'_r(Q)\equiv1\pmod p.}
\]
Henselの補題により **どのrに対しても、唯一のq_r∈Z_pが存在し、F_r(q_r)=0**。したがって任意のm≥1に対して全ての法p^mの方程式は（qを自由に選べば）解を持つ。p進合同条件**だけ**をどれほど深めても、整数の大きさ0≤q<p²を加えない限り、全rの排除は不可能。この証明は外側の楕円曲線・K3構造を全く使わない、現行研究方針の**明示的な局所・大域障害**である。

重要な注意：p進解 q_r が存在しても自然数範囲 q∈[0,p²)に解があることを意味しない。局所可解性を元の方程式の大域可解性と混同しない。

## 次の課題・方法論

- k=p（a=1）の残りは (102.4) から r∈[(1/2−η)logp,\ p−(1/2−η)logp] のp−O(logp)通りに縮約した。ただし各pについて有限でもp自身に上限がないため、**全解なしの証明は未達**。
- b=v_p(i)>0のときはv101の3/4指数障害が使用できる。b=0のケースは今回のmod p²一意復元と対数幅を追加。
- k=p^a（a≥2）への拡張は一般のp^aブロック二項係数のmod p^{2a}構造が必要であり、単純に(102.3)のpをp^aへ置換するのは誤り（例：C(50,25)はmod625で2でない）。誤った一般化は行わない。
- p進根が常に存在するため、次の有望な対象は **一意なp進リフトq_rと実数曲線のq≈(e/4)p²との同時一致不能**を示す新しい大域的近似定理。普通の有限格子探索や局所合同の繰返しは避ける。

## 先行数学

Euler数eの無理数度µ(e)=2はEulerの連分数表示から導かれる既知の結果。Adamczewski, On the expansion of some exponential periods in an integer base (2012), arXiv:1205.0961, Section 3を参照。素数定理の同値形式 \(\log\operatorname{lcm}(1,\dots,n)\sim n\) は標準理論。二項係数のmod p²と有限調和数はWolstenholme/Babbage型古典合同式に属する。今回の(102.4)〜(102.7)はそれらを**元の二項係数方程式の必要条件へ結合した結果**であり、新規性の外部査読はまだない。

STATUS: 記述証明。Lean形式検証未実施。数値照合は独立した sanity check であって全p証明の代用ではない。原の四変数方程式全解は未解決。
