# v25 — 3-捩れを持つ極値有理楕円曲面への同型・二重三次降下の接続

日付：2026-11-07 JST  
研究対象：
\[
\binom{\binom{i}{j}}{\binom{k}{\ell}}=
\binom{i^2}{j^2}+\binom{k^2}{\ell^2},\qquad
\ell=1,\ j=i-3
\]
の枝。**元の四変数方程式や \(\rho\ge32770\) の全域排除は未完成。**

## 0. 使用する前提と独立に証明した事項

v24 に従い \(a,b,\rho\) を正整数（\(b\mid486\)）とし、
\[
F(a,b,\rho)=4a^6+(24b^2-12\rho)a^4+
(36b^4+60b^2\rho+12\rho^2)a^2-3b^2\rho^2-4\rho^3
\]
を考える。補助整数候補には \(S^2=F\)、\(a^2>b^2+\rho\)、\(\gcd(a,b)=1\)、
\[
\rho=a^2+ab(9n-t-6)-b^2(t^2+3t+3),\quad
81an(n-1)=b[9n(t^2+3t+3)+t^3]
\tag{0.1}
\]
が必要である。

**任意の有理数 \(b\ne0\) とパラメータ \(\rho\)** に関する曲線・曲面の定理（§1〜4）は、補助整数候補の存在や(0.1)には依存しない。

## 1. 一様な位数3の有理捩れ点

v24の楕円曲線
\[
E_{b,\rho}:Y^2=X^3+A X+B,\quad
A=48b^2(9\rho-b^2),\quad
B=16b^2(81\rho^2-180b^2\rho-8b^4)
\tag{1.1}
\]
に対し
\[
P=(12b^2,4b(8b^2+9\rho))
\tag{1.2}
\]
は恒等的に点である。\(\rho>0,b>0\) では \(Y_P\ne0\) であり、接線勾配
\[
(3X_P^2+A)/(2Y_P)=6b
\]
から \(X_{2P}=(6b)^2-2(12b^2)=12b^2=X_P\)。従って \(2P=-P\) で、**位数は正確に3**。

判別式は
\[
\Delta=-995328b^4\rho(8b^2+9\rho)^3,
\tag{1.3}
\]
正整数 \(b,\rho\) で非零である。

## 2. 標準的な極値有理楕円曲面への明示的同型

次の恒等式を展開だけで示せる：
\[
\begin{aligned}
z&=a^2-b^2-\rho,\\
H&=b(6a^2+2b^2+3\rho)=6bz+C,\\
C&=b(8b^2+9\rho),\\
F(a,b,\rho)&=H^2+4z^3.
\end{aligned}
\tag{2.1}
\]
\(S^2=F\) に対し \(v=(S+H)/2\) とおけば
\[
v(v-6bz-C)=z^3.
\tag{2.2}
\]
\(S,H\) が整数なら、両者の平方は mod 4 で一致するため \(v\in\mathbb Z\) である。

さらに
\[
\xi=\frac{z}{36b^2},\qquad
\eta=-\frac{v}{216b^3},\qquad
\lambda=\frac{8b^2+9\rho}{216b^2}
\tag{2.3}
\]
とすれば**逆も含む有理変数変換**によって
\[
\boxed{\eta^2+\xi\eta+\lambda\eta=\xi^3}.
\tag{2.4}
\]
となる。固定 \(b\in\mathbb Q^\times\) では \(\lambda\leftrightarrow\rho\) は一次の有理変換で、\(\mathbb Q(\rho)=\mathbb Q(\lambda)\)。

このモデルは Schütt--Shioda, *Elliptic Surfaces*, §7.10.1 に現れる既知の**極値有理楕円曲面**そのものである（独立の新しい曲面分類を主張しない）。
参照: https://www.researchgate.net/publication/45860044_Elliptic_Surfaces ;
https://link.springer.com/article/10.1007/s12215-023-00922-3 .

### 特異ファイバーの検算

(2.4) の \(a_1=1,a_3=\lambda\) から
\[
c_4=1-24\lambda,\qquad
\Delta_\lambda=\lambda^3(1-27\lambda).
\tag{2.5}
\]
\(\lambda=0\) は \(I_3\)（\(v\Delta=3,c_4\ne0\)）、\(\lambda=1/27\) は \(I_1\)（\(v\Delta=1,c_4\ne0\)）。
\(\mu=1/\lambda\) とし \(\xi=\mu^{-2}x_\infty,\eta=\mu^{-3}y_\infty\) とすれば、無限遠の局所最小モデルは
\[
y_\infty^2+\mu x_\infty y_\infty+\mu^2y_\infty=x_\infty^3,
\]
\(\Delta_\infty=\mu^8(\mu-27)\)、\(c_{4,\infty}=\mu^3(\mu-24)\)。Tate のアルゴリズムで \(IV^*\) となる。

有理性は \(\lambda=(\xi^3-\eta^2-\xi\eta)/\eta\) （\(\eta\ne0\)）からもわかる。相対的極小化した有理楕円曲面の Picard 数は10。\(I_3\) の \(A_2\) の階数2、\(IV^*\) の \(E_6\) の階数6より、Shioda--Tate公式で
\[
\mathrm{rank}\,E(\overline{\mathbb Q}(\lambda))
=10-2-2-6=0.
\tag{2.6}
\]
さらに既知の極値曲面の分類（または自明格子の行列式9と単模なNS）より
\[
\boxed{E_{b,\rho}(\mathbb Q(\rho))=\{\mathcal O,P,-P\}\cong\mathbb Z/3\mathbb Z.}
\tag{2.7}
\]
あくまで**関数体**の階数0であり、個々の \(\rho\in\mathbb Z\) への特殊化における楕円曲線の階数0は含意しない。

補助検証：\(\lambda=2\) の良い還元 \(p=5,7\) で \(\#E_2(\mathbb F_5)=3,\ \#E_2(\mathbb F_7)=6\)。\(\lambda=2\) での有理捩れがちょうど3であることと整合する。

### 有理関数としての解の族の不存在

\(a(\rho),S(\rho)\in\mathbb Q(\rho)\) で \(S(\rho)^2=F(a(\rho),b,\rho)\) とすると、\(X=4(a^2+2b^2-\rho),Y=4S\) は(1.1)の有限有理関数点。
(2.7)から \(\pm P\) に等しく、\(X=12b^2\)、従って \(a(\rho)^2=\rho+b^2\) が必要。右辺には \(\rho=-b^2\) に位数1の零点があるから、\(\mathbb Q(\rho)\) 内の平方にならない。矛盾。

\[
\boxed{\text{任意の固定 }b\in\mathbb Q^\times\text{ に対して、六次式 }S^2=F\text{ のアフィン有理関数解は存在しない。}}
\tag{2.8}
\]
なお6次曲線の射影滑らか化には2個の有理無限遠点があり、それらは(1.1)の \(\mathcal O\) に写る。**有限特殊化における整数解や、\(\rho=\rho(t)\) と非一次の基底変換をした解は排除しない。**

## 3. v19の三次被覆が同じ3捩れ降下と判明

補助整数点では (0.1) によって \(b\mid(a^2-\rho)\)、ゆえに \(z=bZ\)（\(Z\in\mathbb Z_{>0}\)）。(2.1)から \(b^2\mid S^2\)、ゆえに \(b\mid S\)。
\(s=S/b,\ H_0=H/b=6a^2+2b^2+3\rho\) と置けば
\[
s^2-H_0^2=4bZ^3,
\]
により \(s\equiv H_0\pmod2\)。従って
\[
U=\frac{s-H_0}{2},\qquad V=\frac{s+H_0}{2}
\tag{3.1}
\]
は整数、\(Z>0,S=\sqrt{F}>0\) より正整数である。そして
\[
\boxed{UV=bZ^3,\qquad V-U+3bZ=9a^2-b^2.}
\tag{3.2}
\]
**これはv19の三次被覆と同一の式**であり、v19とv24が偶然別々の曲線を得ていたわけではない。

\(N=9a^2-b^2=(3a-b)(3a+b)>0\) と置く。もし素数 \(p\mid\gcd(U,V)\) なら \(p\mid UV=bZ^3\) により \(p\mid bZ\)、さらに \(p\mid V-U+3bZ=N\) より
\[
\boxed{\operatorname{rad}(\gcd(U,V))\mid\operatorname{rad}(N).}
\tag{3.3}
\]
（先に得た \(\operatorname{rad}(bN)\) による制約を強める。）

\(p\nmid bN\) なら \(p\) が \(U,V\) を共に割ることはなく、かつ \(UV=bZ^3\) なので、それぞれの \(p\)-付値は3の倍数。従って、\(U,V\) の各三乗でない部分は \(bN\) の素数のみで構成され、各係数対は高々 \(3^{\omega(bN)}\) 通り（v19の既存上界の3捩れによる再解釈）。\(b\mid486\) なら \(p\ge5\) に対する例外素数は \(N\) の素因数だけ。

## 4. **新しい二重三次降下の素因数交差定理**

v22 の既知恒等式（以下では \(n,t,a,b\) の補助関係(0.1)を利用）
\[
U=\frac{b^2(t^2-9n)^3}{729n^2(n-1)},\quad
V=\frac{b^2(t^2+6t+9n)^3}{729n(n-1)^2}
\tag{4.1}
\]
を使う。正整数性を満たす補助点に限って適用する。

\(p\ge5\) なら \(p\nmid729b\) であり、\(e=v_p(n)\) とすれば
\[
\begin{aligned}
 p\mid n:&\quad v_p(U)\equiv e,\quad v_p(V)\equiv2e\pmod3,\\
 p\mid n-1:&\quad v_p(U)\equiv2e,\quad v_p(V)\equiv e\pmod3.
\end{aligned}
\tag{4.2}
\]
従って \(e\not\equiv0\pmod3\) なら \(p\mid U,V\)（付値が非零剰余なので正）。

逆に \(p\ge5,\ p\nmid n(n-1)\) で \(p\mid U,V\) とすると、(4.1)から
\(p\mid(t^2-9n)\) と \(p\mid(t^2+6t+9n)\) であり、その差から \(p\mid 6(t+3n)=6r\)。\(p\ge5\) なので \(t\equiv-3n\pmod p\) となり、最初の式は
\(t^2-9n\equiv9n(n-1)\not\equiv0\pmod p\) となって矛盾。

この2方向と(3.3)を合わせると
\[
\boxed{
\begin{gathered}
\{p\ge5:v_p(n(n-1))\not\equiv0\pmod3\}\\
\subseteq\{p\ge5:p\mid\gcd(U,V)\}\\
\subseteq\{p\ge5:p\mid\gcd(n(n-1),9a^2-b^2)\}.
\end{gathered}}
\tag{4.3}
\]
これは **n,n−1の三乗核** と **残差側3捩れの立方因子** を素数ごとに結び付ける新しい形の必要条件である。現時点で前後集合が等しいとは主張しない。

## 5. 明示的3-isogenyと双楕円商

(1.1) の核 \(\{\mathcal O,P,-P\}\) に対する Vélu の3-isogeny の像曲線を短いWeierstrass形で書くと
\[
\boxed{E':Y'^2=X'^3+A'X'+B'}
\]
\[
A'=-3888b^2(b^2+\rho),\quad
B'=-11664b^2(8b^4+12b^2\rho+3\rho^2),
\tag{5.1}
\]
\[
\boxed{\Delta'=-58773123072b^4\rho^3(8b^2+9\rho).}
\tag{5.2}
\]
例えば \(g=3X_P^2+A\) とおけば
\[
X'=X+\frac{2g}{X-X_P}+\frac{4Y_P^2}{(X-X_P)^2}
\tag{5.3}
\]
である（\(X=X_P\) は核に相当）。本記録の16補助点について Vélu の有理点演算で像曲線の式を厳密照合した。

さらに \(f(q)=4q^3+(24b^2-12\rho)q^2+(36b^4+60b^2\rho+12\rho^2)q-\rho^2(3b^2+4\rho)\) と置くと
\[
C_{b,\rho}: S^2=f(a^2)
\]
は任意の正整数 \(b,\rho\) について滑らかな種数2曲線：\(\mathrm{disc}(f)=-3888b^4\rho(8b^2+9\rho)^3\ne0\) かつ \(f(0)\ne0\)。

二つの互いに異なる位数2自己同型から、二つの種数1商を得る：

1. \((a,S)\mapsto(-a,S)\) の商：\(q=a^2,y=S\) で \(E_1:y^2=f(q)\)（v24の楕円曲線）。
2. \((a,S)\mapsto(-a,-S)\) の商：\(u=a^{-2},v=S/a^3\) で
\[
E_2:v^2=4+(24b^2-12\rho)u+(36b^4+60b^2\rho+12\rho^2)u^2-\rho^2(3b^2+4\rho)u^3.
\tag{5.4}
\]
\(E_2\) は \((u,v)=(0,2)\) という有理点を持ち、判別式が非零なので楕円曲線。\(E_1,E_2\) の異なる微分の引き戻しが独立なため、\(\mathrm{Jac}(C)\) は \(E_1\times E_2\) に有理同種になる（一般に \((2,2)\)-分解）。

**計算的な意味**：固定 \((b,\rho)\) では一つの楕円曲線の整数点だけでなく、2つの商への整合性、3-isogenyの降下、元の整数復元を組み合わせられる。これらの道具だけでは \(\rho\) を無限域で有界化しない。

## 6. 数値・検証範囲

`python v25_exact_verify.py` を実行。SymPyの記号恒等式（Fの因数化、位数3、標準形、Véluの像曲線と判別式、種数2の商）、法5・7での点数、v24付属の16個の補助整数点の全数整数確認、分数による楕円曲線の加法法則とVélu像、v19・v22との等式と新しいp進合同式が**PASS**。

代表例：\((n,t,a,b,\rho)=(6859,1140,43,2,67)\) は
\[
Z=889,\ S=151638,\ U=32258,\ V=43561,\quad UV=2\cdot889^3,
\]
\(V-U+6\cdot889=9\cdot43^2-2^2\) を満たす。しかし**元の二項係数方程式の解ではない**。

Shioda--Tateの一般公式・古典的曲面分類は、既知論文を利用した数学的証明の部分。SageMath・Magmaの全整数点計算、外部査読、Lean形式化を実行済みとは主張しない。

**到達点**：\(\rho\) をパラメータとする楕円曲面の \(\mathbb Q(\rho)\)-有理点は3捩れのみ、六次曲線にアフィン有理関数解は存在しない。またv19の3次被覆とv22の連続3乗核が同一の素数支持を通じて交差することを証明。\(\rho\ge32770\) の領域は引き続き未解決。