# v61：有理9位数捩れを持つ第一楕円商のパラメータを完全分類

2026-11-08。対象は主枝の第一楕円商
\[
E_{1,T}:\ y^2+6xy+(8+9T)y=x^3,\quad T=\rho/b^2>0,\quad b\mid486.
\]

## 定理

\[
\boxed{E_{1,T}(\mathbb Q)\text{ に有理9位数点が存在}\iff T=46648/9.}\tag{61.1}
\]
許される全ての整数 \((\rho,b)\) は
\[
\boxed{b=3d,\quad \rho=46648d^2,\quad d\mid162.}\tag{61.2}
\]

### 証明1：Kubertの9位数パラメータと立方数の条件

KubertのTate正規形では、9位数点を \((0,0)\) に取り、
\[
y^2+(1-c)xy-By=x^3-Bx^2,\qquad
c=z^2(z-1),\ B=c(z^2-z+1).
\]
3倍点は \((c,B-c)\)、その接線の傾きは \((z-1)(z+1)\)。3倍点と接線を原点に移すと
\[
a'_1=-(z^3-3z^2+1),\quad a'_3=-z^3(z-1)^3.
\]
\(a_1=6\) に重み付き変換で正規化すると、元の第一楕円商の係数に
\[
\boxed{8+9T=\left(\frac{6z(z-1)}{z^3-3z^2+1}\right)^3}
\tag{61.3}
\]
が必要。[独立SymPy検算](v61_kubert_thue_reduction_verify.py)で恒等式を再現。

### 証明2：b|486で20本のThue方程式に縮約

\(z=x/y\) を既約分数とし、
\[
D=x^3-3x^2y+y^3,\quad q=6xy(x-y)/D=r/s,\quad \gcd(r,s)=1.
\]
\(8b^2+9\rho=b^2q^3\) は整数なので \(s^3\mid b^2\)。\(b\mid486=2\cdot3^5\) から \(s\mid27\)。

\(\gcd(x,y)=1\) なら、法 \(x,y,x-y\) のそれぞれで \(D\equiv y^3,x^3,-x^3\) となるため
\[
\gcd(D,xy(x-y))=1.
\]
\(rD=6sxy(x-y)\) から \(D\mid6s\mid162\)。従って
\[
\boxed{x^3-3x^2y+y^3=d,\quad d\in\{\pm1,\pm2,\pm3,\pm6,\pm9,\pm18,\pm27,\pm54,\pm81,\pm162\}}
\tag{61.4}
\]
という**20本の三次Thue方程式の全整数解**だけが必要。

### 証明3：PARIによるGRH非依存の完全解

[PARI/Sageスクリプト](v61_nine_torsion_thue.sage)をSageMath 10.10で実行した。[完全ログ](https://github.com/corcondor/mathos/actions/runs/42462323854)と[証明アーティファクト](https://github.com/corcondor/mathos/actions/runs/42462323854/artifacts/13609903469)を参照。PARIのthueinit(P,1)はGRH非依存の完全認証モード。

\(q>2\) となる全原始整数解はちょうど6組：
\[
\begin{array}{c|c}
D=-1&(-3,-1),\ (1,-2),\ (2,3)\\
D=1&(-2,-3),\ (-1,2),\ (3,1)
\end{array}
\]
であり、**6組すべて \(q=36\)**。従って
\[
8+9T=q^3=36^3=46656,\qquad T=46648/9.
\]
逆方向は明示的9位数点
\[
P_9=(-648,-7776)\in E_{1,46648/9}(\mathbb Q),\quad
3P_9=(0,0),\quad9P_9=O
\]
で確認できる。整数 \(\rho=b^2T\) は \(3\mid b\) を必要とし、\(b=3d,d\mid162\) で(61.2)を得る。

## 元の二項係数方程式への全域的帰結

v20で証明された元の解の必要条件 \(\gcd(a,b)=1,\ a^2\equiv\rho\pmod b\) を用いる。

- \(d\) 偶数なら \(2\mid b,\rho\)、従って \(a\) も偶数となり原始性に矛盾。
- \(3\mid d\) なら \(3\mid b,\rho\)、従って \(3\mid a\) となり矛盾。
- \(d\mid162=2\cdot3^4\) なので \(d>1\) は必ず上記どちらか。唯一残る \(d=1\) は \((b,\rho)=(3,46648)\) だが、これは[v44の全残差10万以下の完全排除](V44_ALL_RATIONAL_INTEGER_LIFTS_ja.md)で既に排除。

従って
\[
\boxed{
\text{元の主枝に整数解があるなら、その第一楕円商に有理9位数捩れは存在しない}.
}\tag{61.5}
\]
この排除は**rank(E1)に依存せず、残差 \(\rho\) の上限も設けない**。ただし最後の \((3,46648)\) の排除はv44のv20/v21解析的必要条件を継承する。

### 全有理点への接続

唯一の \(T=46648/9\) では、9個の捩れ点の有限 \(x\) 座標は \(-648,3888,0,864\)。どれも \(x+1+T\) が有理平方ではないため、種数2曲線の有限有理点は第一楕円商の**無限位数点**にしか写れない。第一楕円商のrankが0かを追加の[v62 Sage検査](https://github.com/corcondor/mathos/actions/workflows/v62-nine-torsion-rank.yml)で確認する。

**限界**：元の四変数方程式全体、12位数捩れ、正階数の第一楕円商の全有理点は未解決。PARIのThue部分は無条件認証、その他は記述証明＋SymPy検算であり、Lean形式化・外部査読は未実施。

参考：Kubertの9位数Tate正規形、https://www.math.ubc.ca/~bennett/torsineq.pdf ；PARI公式Thueソルバー、https://pari.math.u-bordeaux.fr/dochtml/html-stable/Polynomials_and_power_series.html。
