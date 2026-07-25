# MathOS 新作問題集: 連続生成バッチ1

## 生成結果

- 生成: 21問
- 採用: 20問
- 構造族: 20種
- 分野: algebra, algebraic_geometry, analytic_geometry, combinatorics, combinatorics_analysis, combinatorics_number_theory, complex_geometry, linear_algebra, linear_algebra_number_theory, number_theory, probability, real_analysis
- 採用条件: 型検査、厳密計算、独立反例探索、コーパス重複検査

## 問題

### 問題1

実数 \(t\) に対し，方程式 \(x^3-3x+t=0\) が相異なる3実根をもつとする。各実根 \(r\) に点 \((r,r^2)\) を対応させて得られる三角形の面積の最大値を求めよ。

### 問題2

整数 \(n\ge2\) と \(-1<t<1\) に対し，方程式 \(z^{2n}-2tz^n+1=0\) の全ての根を複素数平面上の点とみなす。それらの凸包の面積を \(A_n(t)\) とするとき，\(\max_{-1<t<1}A_n(t)\) を求めよ。

### 問題3

素数 \(p\) に対し，\(0\le x,y,z<p\) かつ \(x+y+z\equiv x^2+y^2+z^2\equiv0\pmod p\) を満たす組 \((x,y,z)\) の個数を求めよ。

### 問題4

次数が \( 2026 \) 以下の実係数多項式 \(P(x)\) が \(P(k)=1/k\;(k=1,2,\ldots,2027)\) を満たすとき，\(P(0)\) の値を求めよ。

### 問題5

整数 \(n\ge3\) に対し，\(n\) 頂点の閉路グラフのラプラシアン行列を \(L_n\) とする。\(L_n\) の \(0\) でない固有値を重複度込みですべて掛けた値を求めよ。

### 問題6

\(+1\) を \(n\) 個，\(-1\) を \(n\) 個並べてできる列を一様に選ぶ。第 \(k\) 項までの和を \(S_k\) とし，\(N=\#\{k\in\{1,\ldots,2n\}\mid S_k=0\}\) とおく。\(N\) の期待値 \(\operatorname{E}[N]\) を求めよ。

### 問題7

正の整数 \(n\) に対し，\(\displaystyle\sum_{k=0}^{n}(-1)^k\binom{n}{k}\frac1{n+k+1}\) を求めよ。

### 問題8

第1象限で双曲線 \(xy=1\) に接する直線が正の \(x\) 軸，\(y\) 軸と交わる点をそれぞれ \(A,B\) とする。三角形 \(OAB\) の重心 \(G\) について，\(OG\) の最小値を求めよ。

### 問題9

奇素数 \(p\) に対し，\(\mathbb F_p\) における積 \(\displaystyle P_p=\prod_{k=1}^{p-1}(1+k^{-2})\) を求めよ。

### 問題10

\((i,j)\) 成分が \(\gcd(i,j)\) である \(n\) 次正方行列 \(A_n\) の行列式を求めよ。

### 問題11

数列 \((a_n)\) を \(a_1=1,\ a_{n+1}=a_n+2/a_n\) で定める。\(\displaystyle\lim_{n\to\infty}a_n/\sqrt n\) を求めよ。

### 問題12

\(I_n=\displaystyle\int_0^1\frac{dx}{1+x^n}\) とおく。\(\displaystyle\lim_{n\to\infty}n(1-I_n)\) を求めよ。

### 問題13

正の整数 \(n\) に対し，\(\displaystyle\sum_{k=1}^{n}\frac1{k(k+1)(k+2)}\) を求めよ。

### 問題14

正の整数 \(n\) に対し，\(\displaystyle\sum_{3\mid k}\binom{n}{k}\)（\(k\) は \(3\) の倍数を走る）を \(n\) の式で表せ。

### 問題15

正の整数 \(n\) に対し，\(\displaystyle I_n=\int_0^{\pi/2}\frac{\sin^n x}{\sin^n x+\cos^n x}\,dx\) を求めよ。

### 問題16

整数 \(n\ge1\) に対し，主対角成分が \(2\)，隣接成分が \(-1\)，他が \(0\) の \(n\) 次三重対角行列を \(T_n\) とする。\(\det T_n\) を求めよ。

### 問題17

\(1,2,\ldots,n\) の順列を一様に選ぶ。左から見てそれまでの最大値を更新する項の個数（左から右への最大値の個数）の期待値を求めよ。

### 問題18

正の整数 \(n\) に対し，\(\displaystyle\sum_{d\mid n}\frac{\mu(d)}{d}\)（\(\mu\) はメビウス関数）を求めよ。

### 問題19

フィボナッチ数列を \(F_1=F_2=1,\ F_{n+2}=F_{n+1}+F_n\) で定める。\(n\ge2\) に対し \(F_{n-1}F_{n+1}-F_n^2\) を求めよ。

### 問題20

格子点 \((0,0)\) から \((n,n)\) へ，右または上へ 1 ずつ進む最短経路のうち，直線 \(y=x\) を越えない（常に \(y\le x\) を保つ）ものの総数を求めよ。

## 答と解法概略

### 問題1

**答**: \(3\sqrt3\)

3実根を \(\alpha,\beta,\gamma\) とする。放物線上の3点の面積 \(S\) はVandermonde行列式から \(2S=|(\alpha-\beta)(\beta-\gamma)(\gamma-\alpha)|\)。一方 \(x^3-3x+t\) の判別式は \(108-27t^2\) だから \(4S^2=108-27t^2\)。3実根をもつ範囲は \(|t|<2\) であり，\(t=0\) のとき \(\boxed{S=3\sqrt3}\)。

検証: `symbolic_discriminant_plus_direct_root_area_scan` / 最大表層類似度 `0.5614`

### 問題2

**答**: \(n\sin\frac{\pi}{n}\)

\(t=\cos\theta\;(0<\theta<\pi)\) とおく。根の偏角の間隔は \(2\theta/n,\ 2(\pi-\theta)/n\) と交互に並ぶので，\(A_n(t)=\frac n2\{\sin(2\theta/n)+\sin(2(\pi-\theta)/n)\}\)。加法定理よりこれは \(n\sin(\pi/n)\cos((2\theta-\pi)/n)\) であり，\(\theta=\pi/2\)，すなわち \(t=0\) のとき最大となる。

検証: `trigonometric_normal_form_plus_grid_search` / 最大表層類似度 `0.1356`

### 問題3

**答**: \(\begin{cases}4&(p=2),\\3&(p=3),\\2p-1&(p\equiv1\pmod3),\\1&(p>2,\ p\equiv2\pmod3).\end{cases}\)

\(p\ne2\) では \(z=-x-y\) を代入して \(x^2+xy+y^2=0\) を得る。\(y\ne0\) なら \(r=x/y\) は \(r^2+r+1=0\) を満たす。これは \(p=3\) では重根をもち，\(p\ne3\) では \(\mathbb F_p\) に非自明な3乗根がある場合，すなわち \(p\equiv1\pmod3\) に限り2根をもつ。\(y=0\) の零解と \(p=2\) を別に数えれば答を得る。

検証: `finite_field_elimination_plus_exhaustive_prime_scan` / 最大表層類似度 `0.0892`

### 問題4

**答**: \(\displaystyle\sum_{k=1}^{2027}\frac1k\)

\(Q(x)=xP(x)-1\) とおくと，\(\deg Q\le 2027\) かつ \(Q(1)=\cdots=Q(2027)=0\) である。\(Q(0)=-1\) より \(Q(x)=\frac1{2027!}\prod_{k=1}^{2027}(x-k)\)。一方 \(Q'(0)=P(0)\) だから，対数微分を用いて \(P(0)=\sum_{k=1}^{2027}1/k\)。

検証: `symbolic_interpolation_family_check` / 最大表層類似度 `0.0775`

### 問題5

**答**: \(n^2\)

\(\zeta=e^{2\pi i/n}\) とおくと固有値は \(\lambda_k=2-\zeta^k-\zeta^{-k}=4\sin^2(\pi k/n)\)\((k=0,\ldots,n-1)\)。したがって零でない固有値の積は \(\left(\prod_{k=1}^{n-1}2\sin(\pi k/n)\right)^2=n^2\)。

検証: `exact_principal_cofactor_plus_rank_check` / 最大表層類似度 `0.1205`

### 問題6

**答**: \(\displaystyle\frac{4^n}{\binom{2n}{n}}-1\)

\(S_{2j}=0\) となる列は \(\binom{2j}{j}\binom{2n-2j}{n-j}\) 個である。指示関数の線形性から期待値はこれを \(\binom{2n}{n}\) で割って\(j=1,\ldots,n\) について足したものになる。母関数 \((1-4x)^{-1/2}\) の係数比較により \(\sum_{j=0}^n\binom{2j}{j}\binom{2n-2j}{n-j}=4^n\)だから結論を得る。

検証: `exhaustive_path_enumeration_plus_binomial_convolution` / 最大表層類似度 `0.0792`

### 問題7

**答**: \(\displaystyle\frac{(n!)^2}{(2n+1)!}\)

\((1-x)^n=\sum_{k=0}^n(-1)^k\binom nkx^k\) に \(x^n\) を掛けて \(0\) から \(1\) まで積分する。左辺はベータ積分 \(B(n+1,n+1)=(n!)^2/(2n+1)!\)，右辺は問題の和になる。

検証: `exact_finite_sum_plus_beta_integral_identity` / 最大表層類似度 `0.1131`

### 問題8

**答**: \(\frac{2\sqrt2}{3}\)

\(A=(a,0),B=(0,b)\) とおく。直線 \(x/a+y/b=1\) が \(xy=1\) に接する条件は \(ab=4\)。重心は \(G=(a/3,b/3)\) なので \(OG^2=(a^2+b^2)/9\ge2ab/9=8/9\)。等号は \(a=b=2\)のとき成立する。

検証: `tangency_discriminant_plus_global_AMGM_check` / 最大表層類似度 `0.1265`

### 問題9

**答**: \(P_p=\begin{cases}0&(p\equiv1\pmod4),\\4&(p\equiv3\pmod4).\end{cases}\)

\(p\equiv1\pmod4\) なら \(k^2=-1\) となる因子があり積は0。\(p\equiv3\pmod4\) では \(\mathbb F_{p^2}\) で \(i^2=-1\)とおく。\(\prod_{k\in\mathbb F_p^\times}(X-k)=X^{p-1}-1\)を \(X=\pm i\) に代入すると \(\prod(k^2+1)=(-2)^2=4\)。Wilsonの定理より \(\prod k^2=1\) だから \(P_p=4\)。

検証: `extension_field_factorization_plus_modular_enumeration` / 最大表層類似度 `0.1404`

### 問題10

**答**: \(\displaystyle\det A_n=\prod_{k=1}^{n}\varphi(k)\)

\(\gcd(i,j)=\sum_{d\mid i,\ d\mid j}\varphi(d)\) を用いる。\(E_{id}=1_{d\mid i}\)，\(D=\operatorname{diag}(\varphi(1),\ldots,\varphi(n))\) とおけば \(A_n=EDE^T\)。\(E\) は対角成分1の下三角行列なので \(\det E=1\)。よって \(\det A_n=\det D=\prod_{k=1}^n\varphi(k)\)。

検証: `exact_integer_determinants_plus_incidence_factorization` / 最大表層類似度 `0.0789`

### 問題11

**答**: \(2\)

\(a_n>0\) かつ単調増加なので \(a_n\to\infty\)。\(a_{n+1}^2-a_n^2=4+4/a_n^2\to4\) である。Stolz--Cesaroの定理から \(a_n^2/n\to4\)。\(a_n>0\) より求める極限は \(2\)。

検証: `increment_limit_proof_plus_long_horizon_simulation` / 最大表層類似度 `0.3036`

### 問題12

**答**: \(\log 2\)

\(1-I_n=\int_0^1x^n/(1+x^n)\,dx\) である。\(u=x^n\) とおけば \(n(1-I_n)=\int_0^1u^{1/n}/(1+u)\,du\)。被積分関数は \(1/(1+u)\) に収束し，1で支配されるので，極限は \(\int_0^1du/(1+u)=\log2\)。

検証: `exact_substitution_plus_high_precision_quadrature` / 最大表層類似度 `0.2321`

### 問題13

**答**: \(\displaystyle\frac{n(n+3)}{4(n+1)(n+2)}\)

部分分数分解 \(\frac1{k(k+1)(k+2)}=\frac12\!\left(\frac1{k(k+1)}-\frac1{(k+1)(k+2)}\right)\) を用いる。和は望遠鏡的に打ち消し合い，\(\frac12\!\left(\frac12-\frac1{(n+1)(n+2)}\right)=\frac{n(n+3)}{4(n+1)(n+2)}\) となる。

検証: `symbolic_summation_plus_numeric_partial_sums` / 最大表層類似度 `0.4684`

### 問題14

**答**: \(\displaystyle\frac{2^n+2\cos\frac{n\pi}3}{3}\)

\(\omega=e^{2\pi i/3}\) とおくと，\(1+\omega+\omega^2=0\) より \(\frac13\sum_{j=0}^{2}(1+\omega^j)^n\) が \(3\mid k\) の項だけを取り出す。\((1+1)^n=2^n\)，\((1+\omega)^n+(1+\omega^2)^n=2\cos(n\pi/3)\) だから，和は \(\dfrac{2^n+2\cos(n\pi/3)}3\)。

検証: `exact_binomial_sum_vs_root_of_unity_filter` / 最大表層類似度 `0.3131`

### 問題15

**答**: \(\dfrac{\pi}{4}\)

\(x\mapsto \frac\pi2-x\) と置換すると \(\sin\) と \(\cos\) が入れ替わり，\(I_n=\int_0^{\pi/2}\frac{\cos^n x}{\sin^n x+\cos^n x}\,dx\)。元の \(I_n\) と辺々加えると被積分関数は \(1\) になるので \(2I_n=\int_0^{\pi/2}dx=\frac\pi2\)，すなわち \(I_n=\frac\pi4\)（\(n\) によらない）。

検証: `reflection_symmetry_proof_plus_high_precision_quadrature` / 最大表層類似度 `0.2421`

### 問題16

**答**: \(n+1\)

最終行で余因子展開すると \(D_n=2D_{n-1}-D_{n-2}\)（\(D_1=2,\ D_2=3\)）を得る。これは公差 \(1\) の等差数列で \(D_n=n+1\)。

検証: `exact_integer_determinant_plus_cofactor_recurrence` / 最大表層類似度 `0.25`

### 問題17

**答**: \(\displaystyle\sum_{k=1}^{n}\frac1k\)

第 \(i\) 項が左からの最大値になるのは，最初の \(i\) 項の中で第 \(i\) 項が最大のときで，その確率は \(1/i\)。指示関数の期待値の線形性より，求める期待値は \(\sum_{i=1}^{n}\frac1i=H_n\)。

検証: `exhaustive_position_indicator_plus_total_expectation` / 最大表層類似度 `0.119`

### 問題18

**答**: \(\displaystyle\frac{\varphi(n)}{n}=\prod_{p\mid n}\left(1-\frac1p\right)\)

\(f(n)=\sum_{d\mid n}\mu(d)/d\) は乗法的関数のディリクレ畳み込みで与えられる。素数冪 \(p^a\) では \(f(p^a)=1-1/p\) だから，乗法性より \(f(n)=\prod_{p\mid n}(1-1/p)=\varphi(n)/n\)。

検証: `exact_divisor_sum_vs_totient_and_euler_product` / 最大表層類似度 `0.3218`

### 問題19

**答**: \((-1)^n\)

\(A=\begin{pmatrix}1&1\\1&0\end{pmatrix}\) とおくと \(A^n=\begin{pmatrix}F_{n+1}&F_n\\F_n&F_{n-1}\end{pmatrix}\)。両辺の行列式をとると \(\det(A^n)=(\det A)^n=(-1)^n\)，左辺は \(F_{n+1}F_{n-1}-F_n^2\) だから \(F_{n-1}F_{n+1}-F_n^2=(-1)^n\)。

検証: `exact_fibonacci_identity_plus_matrix_determinant` / 最大表層類似度 `0.1901`

### 問題20

**答**: \(\displaystyle\frac1{n+1}\binom{2n}{n}\)

対角線を越える経路を鏡像原理で数える。全 \(\binom{2n}{n}\) 通りから，境界を越える経路（\((-1,1)\) を始点とする経路と一対一対応し \(\binom{2n}{n-1}\) 通り）を引くと，\(\binom{2n}{n}-\binom{2n}{n-1}=\frac1{n+1}\binom{2n}{n}\)。

検証: `exhaustive_dyck_enumeration_plus_reflection_formula` / 最大表層類似度 `0.0685`

## 注意

ここでの「新作」は、公開問題・自作問題・既生成問題からなる比較コーパス内で衝突しなかったという意味である。世界全体で未出であることは主張しない。
