# v101：全探索を使わない非アルキメデス × 実数漸近の一様排除

2026-11-11。原の添字二乗二項係数方程式
\[
\binom{\binom{i}{j}}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}
\]
のうち、既存v100で重要となった **j=1, ell=k−1** の無限枝を研究する。主目的は有限範囲 k≤N の全探索でなく、任意の素数p・指数aに一括適用できる定理。元の四変数問題の全解は未決定。

## 定義と全域整除

対象の等式は
\[
\binom ik=i^2+R_k,\qquad R_k=\binom{k^2}{2k-1},\qquad i\ge k.
\tag{101.1}
\]
恒等式
\((2k-1)R_k=k^2\binom{k^2-1}{2k-2}\) と
\(\gcd(2k-1,k^2)=1\) から **任意のk≥2で \(k^2\mid R_k\)**。
これはv100の全シフト整除定理の特殊化と両立する。

## 定理1：全k≥3で、解は i<k³ を満たす

v100の単調性補題：\(F_k(i)=\binom ik-i^2-R_k\) はi≤2kで負、i≥2kで厳密増加。ここで**厳密な比較**
\[
\boxed{\binom{k^3}{k}>k^6+\binom{k^2}{2k-1}}\quad(k\ge3)
\tag{101.2}
\]
を証明する。

\(R_k=\binom{k^2}{2k-1}\) とする。k≥3で
\[
\frac{\binom{k^3}{k}}{R_k}
>\frac{(k^3-k)^k}{k!}\frac{(2k-1)!}{(k^2)^{2k-1}}
=k^{2-k}\Bigl(1-\frac1{k^2}\Bigr)^k
\prod_{s=k+1}^{2k-1}s
>k\Bigl(1-\frac1{k^2}\Bigr)^k
\ge k-1.
\]
最初の不等式は分子の落下階乗を各項 k³−k で下から抑え、R側の落下階乗を各項k²で上から抑えたもの。次に全s≥k+1なのでその積はk^{k-1}より大きく、最後はBernoulli不等式。

k≥6では \(2k-1\le k^2/2\) から
\[
R_k\ge\binom{k^2}{k}\ge(k^2/k)^k=k^k\ge k^6.
\]
k=4ではR_4=11440>4^6=4096、k=5ではR_5=2042975>5^6=15625。よってk≥4で \(\binom{k^3}{k}>(k-1)R_k\ge3R_k\ge R_k+k^6\)。k=3は \(\binom{27}3=2925>126+729\) を直接確認。これで(101.2)が得られる。i≥k³ならv100のF単調性と(101.2)からF(i)>0、元式に反する。従って**\(i<k^3\)**（さらに i>2k）。これは大域的な不等式であり、実数Stirling近似を仮定しない。

## 定理2：kが素数冪なら k|i は不可能（完全無限族排除）

\[
\boxed{k=p^a,\ a\ge1,\ k\mid i\quad\Longrightarrow\quad(101.1)\text{は成立しない}.}
\tag{101.3}
\]
証明：b=v_p(i)≥aを仮定。k=p^aなので、1≤t<kならv_p(i−t)=v_p(t)。従って
\[
\binom{i}{p^a}=\frac{i}{p^a}\binom{i-1}{p^a-1},\quad
v_p\left(\binom{i-1}{p^a-1}\right)=0
\quad\Longrightarrow\quad
v_p\left(\binom{i}{k}\right)=b-a.
\]
一方 \(k^2\mid R_k,\ k\mid i\) により(101.1)の右辺はp^{2a}で割れる。従ってb−a≥2a、すなわちp^{3a}=k³|i。定理1のi<k³に矛盾。k=2はそもそも(101.1)が不可能。**どのa、pにも一括で通用**。

特にk=p素数の場合は、元式の解なら \(\gcd(i,p)=1\)。以前の「p|iかつp²∤iなら排除」から大幅に強化され、**p|iの全指数を排除**した。

## 定理3：より精密なp進桁の恒等式

素数p、k=p^a、i≥k、\(q=\lfloor i/k\rfloor\ge1\) とする。Legendreの階乗付値公式またはKummerのcarry定理により
\[
\boxed{v_p\left(\binom{i}{p^a}\right)=v_p(q).}\tag{101.4}
\]
詳しくはi=kq+r,0≤r<kとし、Legendre公式の各p^m項を比較する。m≤aの寄与は0、m>aの寄与は \(p^{m-a}\mid q\) のときだけ1。これを全mで足すとv_p(q)になる。

さらに
\[
\boxed{v_p(R_k)=2a.}\tag{101.5}
\]
理由は \(R_k=\binom{p^{2a}}{2p^a-1}\) で、1≤t<p^{2a}に対して
\(v_p\binom{p^{2a}}t=2a-v_p(t)\)、t=2p^a−1がp-unitであるため。

(101.1)の仮定下で定理2により \(b=v_p(i)<a\)。ゆえにi²のp進付値は2b、Rのそれは2aで厳密に異なる。したがって
\[
\boxed{0\le b<a,\qquad v_p\!\left(\left\lfloor\frac i{p^a}\right\rfloor\right)=2b.}
\tag{101.6}
\]
例えばa=1ならb=0かつp∤q、そしてLucasから \(q\equiv(i\bmod p)^2\pmod p\)。a≥2でb≥1ならqは**必ずp²で割れる**。これらは任意p,aで成立し、全探索は不要。

## 定理4：eの無理数度を使った「共通素因数の指数の一様削減」

ここでは既知の実数解析と数論の定理を明示して使う。v100のStirling展開・逆曲線の近似から、(101.1)の任意の候補について
\[
\boxed{\frac i{k^3}=\frac e4+O\left(\frac{\log k}{k}\right),}
\tag{101.7}
\]
で、Oの定数はp,aによらない。これは \(\log R_k=2k\log k+2k(1-\log2)+O(\log k)\)、
\(\log\binom ik=k\log i-\log(k!)+O(k^2/i)\)、\(i\asymp k^3\)から出る。i²/R_kは超指数的に小さく、対数の主項には影響しない。

\(b=v_p(i)<a,\ d=a-b>0\)、\(q=\lfloor i/k\rfloor=p^{2b}u\) と書くと、i=kq+r、0≤r<kにより
\[
\frac i{k^3}=\frac u{p^{2d}}+\frac r{k^3},\qquad 0\le r/k^3<1/k^2.
\]
従って
\[
\boxed{\left|\frac e4-\frac u{p^{2d}}\right|
=O\left(\frac{\log k}{k}\right).}
\tag{101.8}
\]

古典的な**Euler数eの無理数度が \(\mu(e)=2\)** という既知定理を使う：
任意のε>0に対し定数c_ε>0が存在し、全有理数P/Qについて
\[
|e/4-P/Q|\ge c_\varepsilon Q^{-2-\varepsilon}.
\]
この定理はEulerのeの正規連分数 \([2;1,2,1,1,4,1,1,6,\ldots]\) から導け、Davis (1978)、Adamczewski (2012)でも扱う。

任意のη∈(0,1/4)を取り、十分小さいε>0を選んで
\(\gamma=(4+2\varepsilon)(1/4-\eta)<1\) とする。
もしb≥(3/4+η)aならd≤(1/4−η)aだから \(p^{(4+2ε)d}\le k^\gamma\)。
すると(101.8)は
\[
c_\varepsilon k^{-\gamma}\le C\frac{\log k}{k},
\]
を強制するが、γ<1なのでk→∞で不可能。

**全素数p・全指数aで一様な結論：**
\[
\boxed{\forall\eta>0\ \exists K_\eta\
\forall\,k=p^a\ge K_\eta,\quad
(101.1)\Longrightarrow v_p(i)<\left(\frac34+\eta\right)a.}
\tag{101.9}
\]
η≥1/4は定理2から自明。これにより、たとえ「kはiを割らない」という初等的障害を回避しても、**iとkに共通するpの指数は、kの指数の高々約3/4**に抑えられる。ここがv100の実数漸近とp進付値を実際に結合した新しい点。帰着と係数の検算は本ノートの証明で示すが、eの無理数度の定理そのものは既知の外部定理であり新規証明したとは主張しない。K_etaは現段階で数値化していない。

**初等的で更に分かりやすい系：** pとd≥1を任意に固定する。\(v_p(i)=a-d\) とする解は、aが十分大きければ存在しない。これはμ(e)=2の定量評価さえ不要で、(101.8)とe/4の無理性、および分母p^{2d}の有理数が有限個の区間にしか存在しないことだけで従う。

## 定理5：ell=k-c の漸近分岐は c=1 を境に相転移する

上のp進論法は **c=1**、すなわちell=k−1に特有。旧v4のj=1上側枝に接続するため、固定整数c≥2でell=k−cを考える。

\[
B=\binom{k}{c}\sim k^c/c!,\qquad
R=\binom{k^2}{2ck-c^2},\qquad
i=B+t.
\]
元式は \(\binom{B+t}{t}=(B+t)^2+R\)。固定λ>0についてStirlingから
\[
\log\binom{B+\lfloor\lambda k\rfloor}{\lfloor\lambda k\rfloor}
=\lambda(c-1)k\log k+O(k),\quad
\log R=2ck\log k+O(k).
\]
前者はtと共に（t≥3では元式の差も）単調に増えるので、仮に元式の解の列が存在するなら
\[
\boxed{t=i-\binom{k}{c}\sim\frac{2c}{c-1}k\qquad(c\ge2,\ c\text{固定}).}
\tag{101.10}
\]
特にc=2ではt∼4k、c=3ではt∼3k。一方**c=1ではtはO(k)ではなくi∼(e/4)k³**。これは旧v4の上側・v100の下側を解析的に区別する根拠。c=2の個別枝は旧v4で既に排除されているため、(101.10)は存在主張ではない。

## 外部一次資料・証明の境界

- C. S. Davis, *Rational Approximations to e*, Journal of the Australian Mathematical Society Ser. A 25 (1978), 497–502, https://doi.org/10.1017/S1446788700021480 。eの連分数近似の定量評価。
- Boris Adamczewski, *On the expansion of some exponential periods in an integer base* (2012), https://arxiv.org/abs/1205.0961 。Euler連分数からµ(e)=2を用いる。
- Kummerの定理、Legendreの階乗付値公式（古典定理）。(101.4)の具体的p^aの場合は上に自力で証明した。
- [旧v4素数支持・Pell結果](v4_upper_j1_smooth_pell.md)、[v99全曲線・Lucas例外](V99_CROSS_VERSION_LEMMA_AUDIT_ja.md)、[v100整数格子・全シフト整除](V100_INVERSE_BINOMIAL_LATTICE_AND_SHIFTED_DIVISORS_ja.md)。

**結論**：新たに、(A) 無制限のk=p^a|i全排除、(B) p進桁の全称的な付値恒等式、(C) \(\mu(e)=2\) を使った全素数・全指数に一様な3/4指数制限、(D) c=1とc≥2の漸近スケール分離を得た。元の4変数全解、および残るb<aでiが条件を満たす場合の全排除は未証明。単なる有限Nの探索には依存していない。
