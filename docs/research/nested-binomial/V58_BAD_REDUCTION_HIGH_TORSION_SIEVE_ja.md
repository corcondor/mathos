# v58：第一楕円商の9・12位数捩れを、残差の素因数の付値から無限族ごと制限

2026-11-08。元の枝 \(\ell=1,j=i-3\) に由来する第一楕円商
\[
E_{1,T}: y^2+6xy+(8+9T)y=x^3,\qquad T=\rho/b^2>0,\ b\mid486
\]
を扱う。**楕円曲線の全有理点の分類ではない**。ただし、従来未処理だった捩れ9・12に対して、残差 \(\rho\) の大小に依存しない算術的な必要条件を得る。

## 定理1：有理捩れの候補は3、6、9、12のみ

\[
\Delta=-243T(8+9T)^3<0,\qquad c_4=144(1-9T).
\tag{58.1}
\]
\(P=(0,0)\) は正確に位数3。Mazurの有理捩れ群分類より、3を含む有理捩れ群は
\[
\mathbb Z/3,\ \mathbb Z/6,\ \mathbb Z/9,\ \mathbb Z/12,\ 
\mathbb Z/2\oplus\mathbb Z/6
\]
のいずれか。最後は2位数点が3個あり、短いWeierstrass方程式の3つの有理2位数 \(x\)-座標を与えるため、実判別式が正になる。しかし (58.1) は負なので不可能。
\[
\boxed{E_{1,T}(\mathbb Q)_{\rm tors}\in
\{\mathbb Z/3,\mathbb Z/6,\mathbb Z/9,\mathbb Z/12\}.}
\tag{58.2}
\]

## 定理2：p|rhoでの乗法的悪い還元が高次捩れを拘束

\(p\ge5\) を \(\rho\) の素因数とし \(e=v_p(\rho)\ge1\) とする。\(b\mid486\) より \(p\nmid b\)。このとき \(T\equiv0\pmod p\) なので
\[
v_p(\Delta)=e,\qquad c_4\equiv144\not\equiv0\pmod p.
\]
従ってこのモデルは \(p\) で最小な乗法的還元 \(I_e\) を持つ。

\[
c_6=-216(81T^2-180T-8),\quad
-c_6\equiv-1728=-3\cdot24^2\pmod p.
\]
\(\chi_p=\left(\frac{-3}{p}\right)\in\{\pm1\}\) とおくと、分裂／非分裂の別がこの平方指標で決まり、滑らかな特殊繊維の \(\mathbb F_p\) 上の点数は
\[
\boxed{\#\widetilde E_{\rm ns}(\mathbb F_p)=p-\chi_p.}
\tag{58.3}
\]

Néronモデルの還元列から \(E(\mathbb Q_p)\) の \(p\)-prime-to torsionは核がpro-\(p\)の部分を通じて、成分群と滑らかな還元群の拡大へ単射となる。\(I_e\) 型の幾何学的成分群の位数は \(e\) なので、任意の \(N\in\{9,12\}\) の有理捩れ点が存在すれば、\(p\ge5\) では \(p\nmid N\) であり
\[
\boxed{N\mid e\,(p-\chi_p).}\tag{58.4}
\]
これが**残差全域に対する必要条件**である。

ここで \(p\equiv1\pmod3\) なら \(\chi_p=1\)、\(p\equiv2\pmod3\) なら \(\chi_p=-1\)。そのため \(p-\chi_p\) は常に3の倍数である。式 (58.4) から次を得る：

**9位数の必要条件：**
\[
\boxed{
p\mid\rho,\ p\ge5,\ p\not\equiv\pm1\pmod9
\Longrightarrow 3\mid v_p(\rho).
}
\tag{58.5}
\]

**12位数の必要条件：**
\[
\boxed{
p\mid\rho,\ p\ge5,\ p\not\equiv\pm1\pmod{12}
\Longrightarrow 2\mid v_p(\rho).
}
\tag{58.6}
\]
実際、条件を満たす \(p\) に対して \(p-\chi_p\) は3の倍数で9の倍数でない、あるいは4の倍数でないので、式(58.4)によってそれぞれ \(3\mid e\)、\(2\mid e\) を強制する。

## 系：rank0を除外する残差の無限族

\(p\equiv5,7,29,31\pmod{36}\) なら、法9・法12両方の上記高次捩れ条件に反する。特に
\[
\boxed{
v_p(\rho)=1,\quad p\equiv5,7,29,31\pmod{36}
\Longrightarrow
E_{1,\rho/b^2}(\mathbb Q)_{\rm tors}\in\{\mathbb Z/3,\mathbb Z/6\}
\quad(\forall b\mid486).
}\tag{58.7}
\]
v50とv56の全称排除定理より、**そのような素因数を持つ \(\rho\) に元の主枝の整数解があるなら、第一楕円商のMordell–Weil階数は必ず正**である。逆にrank0であれば元の解は存在しない。この結論は \(\rho\) を有限区間に制限しない。

例：\(\rho=100003\) は素数で
\[
100003\equiv31\pmod{36},\quad e=1,\quad\chi=1,\quad
p-\chi=100002.
\]
\(9\nmid100002,\ 12\nmid100002\) より、全12種類の \(b\mid486\) の第一楕円商では9位数・12位数捩れが**局所理論だけで排除**される。以前の12繊維の有限体点数検査と整合する。

## 検証と今後

[v58_bad_reduction_torsion_verify.py](v58_bad_reduction_torsion_verify.py) は判別式・\(c_4,c_6\) の恒等式、法 \(p\) 特異点 \((-4,8)\) の二次接線、5以上103未満の全素数での \(\#\widetilde E_{\rm ns}=p-\chi_p\) の完全点数計数、法36の全許容剰余類と \(100003\) の例を厳密に照合する。

**証明依存と限界**：Mazurの有理捩れ群定理、Kodaira/Néronの乗法的還元列、平方指標の局所還元という外部一般定理を入力とする記述証明。これらは有限計算だけで代替したわけではない。Lean形式証明・外部査読なし。正階数の全有理点、捩れ9/12の全てのパラメータ、一般の \(\rho\) の全整数解は依然未解決。

参考：Mazurの捩れ分類、Silverman *Advanced Topics in the Arithmetic of Elliptic Curves* の乗法的還元・Néron成分群、[v56整数復元障害](V56_UNIFORM_TORSION_SIX_OBSTRUCTION_ja.md)、[v50第一楕円商](V50_FIRST_QUOTIENT_ALL_GENUS2_RATIONAL_POINTS_ja.md)。
