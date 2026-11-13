# v38：二次基底変換後のK3曲面のMordell–Weil群を飽和済み基底まで完全決定

2026-11-08。v33は第二楕円商の一般関数体上の幾何学的Mordell–Weil群を \(E(\overline{\mathbb Q}(T))=\mathbb ZR\) と決定した。v34は \(T=q^2-1\) への二次基底変換で階数が正確に2に上昇することと、独立点 \(Q\) の存在を証明したが、**R,Qが飽和済みの基底かは未解決**だった。本研究は新しい有理関数点 \(H=(R+Q)/2\) を明示し、**幾何学的飽和を完全に証明する**。特殊化した個々の \(E_T(\mathbb Q)\) の全有理点や元の入れ子二項係数方程式の全解決ではない。

## 定理（完全な群と高さ格子）

\[
T=q^2-1,\quad
A=-T^2(4T+3),\quad B=12(T^2+5T+3),\quad C=12(2-T),
\]
\[
E:\quad Y^2=X^3+BX^2+ACX+4A^2
\]
とし、
\[
R=(8T(4T+3),6T(4T+3)(9T+8)),
\qquad
Q=(A/q^2,\;A(9T+8)/q^3)
\]
をv34の独立点とする。次の点を導入する：
\[
\boxed{
H=\left(-2(q-1)(q+1)^2(2q+1),\
6(q-1)(q+1)^2(2q+1)(3q-1)\right).
}\tag{38.1}
\]
このとき
\[
\boxed{2H=R+Q,}\tag{38.2}
\]
\[
\boxed{
E(\overline{\mathbb Q}(q))
=E(\mathbb Q(q))
=\mathbb ZR\oplus\mathbb ZH,\quad E(\overline{\mathbb Q}(q))_{\rm tors}=0.
}\tag{38.3}
\]
すなわち \(R,H\) は**幾何学的に飽和済みの完全な基底**である。高さペアリングとNéron–Severi判別式の絶対値は
\[
\boxed{
\begin{pmatrix}
\langle R,R\rangle&\langle R,H\rangle\\
\langle H,R\rangle&\langle H,H\rangle
\end{pmatrix}
=
\begin{pmatrix}
1/15&1/30\\ 1/30&1/6
\end{pmatrix},\quad
|\det\operatorname{NS}|=27.
}\tag{38.4}
\]

## 証明1：明示的な半分点の発見と群法則の検証

曲線への(38.1)の代入は多項式恒等式であり、接線の群法則
\[
\lambda=\frac{3H_x^2+2BH_x+AC}{2H_y},\quad
X(2H)=\lambda^2-B-2H_x,\quad
Y(2H)=\lambda(H_x-X(2H))-H_y
\]
を代入すれば、**X座標とY座標の双方について**(38.2)が有理関数恒等式として成立する。
したがって \(\langle R,Q\rangle\) は飽和されておらず、
\[
\langle R,Q\rangle\subset\langle R,H\rangle,\qquad
[\langle R,H\rangle:\langle R,Q\rangle]=2,
\]
である（v34による \(R,Q\) の独立性を使用）。

## 証明2：高さ行列の完全計算

v34で確定したK3ファイバー配置は
\[
I_5^2\,I_3^2\,I_2^2\,IV,\qquad \chi(\mathcal O)=2,\quad \rho_{\rm NS}=20.
\]
Shiodaの高さ公式
\[
\langle P,P\rangle=4+2(P\cdot O)-\sum_v\operatorname{contr}_v(P)
\]
を適用する。

- \(R\) の高さ：v33の \(1/30\) を基底変換の次数2倍して
  \(\langle R,R\rangle=1/15\)。直接計算でも \(R\cdot O=0\)、2つずつの \(I_5,I_3,I_2\) における局所寄与 \(4/5,2/3,1/2\) を得る。
- \(Q\cdot O=1\)：\(q=0\) の良いファイバーで \(X(Q)=A/q^2\) が正確に2位の極を持ち、無限遠では最小モデルにおける \(q^{-4}X(Q)\to-4\) で極を持たない。
- \(Q\) の成分番号：\(q=\pm1\) の \(I_5\) では \(Y(Q)\) の付値2で第 \(\pm2\) 成分（寄与 \(6/5\) が各1回）；\(q=\pm1/2\) の \(I_2\) では付値1（寄与 \(1/2\) が各1回）；\(q=\pm1/3\) の \(I_3\) では付値1（寄与 \(2/3\) が各1回）。無限遠の \(IV\) では \(q^{-4}X(Q)\to-4,\ q^{-6}Y(Q)\to0\) なので、還元式 \(y^2=(x+4)^3\) の尖点へ入り、解消後の非単位成分（寄与 \(2/3\)）を通る。
- したがって
\[
\langle Q,Q\rangle
=6-2\cdot\frac65-2\cdot\frac12-2\cdot\frac23-\frac23
=\boxed{\frac35}.
\]
- 体自己同型 \(\sigma:q\mapsto-q\) に対して \(\sigma R=R,\ \sigma Q=-Q\)。高さペアリングは保存されるので \(\langle R,Q\rangle=-\langle R,Q\rangle=0\)。

\(\langle H,H\rangle=(1/15+3/5)/4=1/6\)、\(\langle R,H\rangle=1/30\)、高さ行列の行列式は \(1/100\)。これは(38.4)前半を与える。

## 証明3：幾何学的捩れ点は存在しない

型 \(I_5,I_3,I_2,IV\) の局所寄与の可能値は
\[
I_5:\{0,4/5,6/5\},\quad
I_3:\{0,2/3\},\quad
I_2:\{0,1/2\},\quad
IV:\{0,2/3\}.
\]
上の配置で最大寄与和は \(27/5<6\)。非零捩れ切断 \(P\) が存在すれば高さ0なので、\(P\cdot O=0\) かつ寄与和4を要する。全成分の可能値を厳密に組み合わせると、和4は以下の**2配置しかない**：
\[
(4/5,6/5;\;2/3,2/3;\;0,0;\;2/3)
\quad\text{または}\quad
(6/5,4/5;\;2/3,2/3;\;0,0;\;2/3).
\]
この配置の \(5P\) は \(I_5\) の成分番号が0、二つの \(I_3\) と \(IV\) の成分番号は非零のまま（5は3を法として可逆）、\(I_2\) は0。ゆえに \(5P\ne O\) だが、局所寄与和は \(2/3+2/3+2/3=2\) となる。これは \(5P\) が非零捩れで高さ0であることに矛盾する。従って捩れ群は自明である。

## 証明4：判別式の整数性によって飽和指数を2と3だけに限定

v34から幾何学的Mordell–Weil階数は2なので、\(I=[E(\overline{\mathbb Q}(q)):\langle R,Q\rangle]\) は有限。K3のtrivial latticeは
\[
U\oplus A_4^{\,2}\oplus A_2^{\,2}\oplus A_1^{\,2}\oplus A_2,
\quad |\det(\operatorname{Triv})|=5^2\,3^2\,2^2\,3=\boxed{2700}.
\]
Shiodaの判別式公式と捩れ0、\(\det\langle R,Q\rangle=1/25\) により
\[
|\det\operatorname{NS}|=\frac{2700}{25I^2}=\frac{108}{I^2}.
\]
\(\operatorname{NS}\) は整数格子なので \(I^2\mid108=2^2 3^3\)。従って
\[
\boxed{I\in\{1,2,3,6\}.}
\]
しかし \(2H=R+Q\) で \(\langle R,H\rangle/\langle R,Q\rangle\cong\mathbb Z/2\)、よって \(I\) は偶数。従って \(I=2\) または6。
残る \([E(\overline{\mathbb Q}(q)):\langle R,H\rangle]\) は**1または3だけ**。

## 証明5：有限体で3飽和を完全に認証

仮に後者の指数が3なら、互いに素な整数対 \((a,b)\) の係数を3で割った少なくとも一つの非零類について
\[
3S=aR+bH,\qquad S\in E(\overline{\mathbb Q}(q))
\]
が存在する。前段で幾何学的捩れ、特に3捩れを否定したので、3分点は**一意**であり、右辺が \(\mathbb Q(q)\) 上で定義されることからガロア不変性により \(S\in E(\mathbb Q(q))\)。

従って任意の良い有理特殊化 \(q=q_0\) と良い素数 \(p\) で、\(aR(q_0)+bH(q_0)\) の還元点は \(3E_{q_0}(\mathbb F_p)\) に属さなければならない。ところが、4つの射影剰余類 \([a:b]\in\mathbb P^1(\mathbb F_3)\) の**すべて**について反証が見つかる：

| \([a:b]\) | 特殊化 \(q_0\) | 良い素数 \(p\) | \(\#E_{q_0}(\mathbb F_p)\) | \(aR+bH\bmod p\) |
|--:|--:|--:|--:|---:|
| [1:0] | 2 | 41 | 54 | (32,20) |
| [1:1] | 2 | 41 | 54 | (17,4) |
| [1:2] | 2 | 41 | 54 | (4,39) |
| [0:1] | 3 | 17 | 21 | (11,8) |

各行の点は \(3E(\mathbb F_p)\) **に属さない**。これは有限体上の曲線の全点を列挙し、加法公式で3倍像の全てを作って照合した厳密な有限計算である。4つの方向で全非零係数類（スカラー倍を除く）を尽くすから、3除法は不可能。よって残る指数は1。

\[
\boxed{E(\overline{\mathbb Q}(q))=\mathbb ZR\oplus\mathbb ZH.}
\]
R,Hは有理係数の点なので \(E(\mathbb Q(q))\) も同じ群となる。高さ行列式は \(1/100\) なので
\[
|\det\operatorname{NS}|=2700/100=\boxed{27}.
\quad\square
\]

## 位置づけ・残る課題

1. **v34の未解決点「R,Qは飽和済みか」を解消**：答えは「否」であり、真の基底は \(\{R,H=(R+Q)/2\}\)。幾何学的な定数拡大も含めて飽和した。
2. v35〜v37で扱った \(mR\pm Q\) は、新しい完全基底では \( (m\mp1)R\pm2H\) に相当する。**Hを使うと、これまで調べていない奇数H係数の点も存在する**。したがって次は \(H, R\pm H,2R\pm H\) の整数復元・結果式・5進障害を扱うのが自然。
3. **限界**：これはパラメータ \(q\) を不定元とした関数体の全群決定。固定した整数 \(\rho\) への特殊化で、新しい有理点が加わる場合は依然として別途の検証が必要。元の入れ子二項係数方程式の一般解決でもない。
4. 証明はShiodaの高さ/判別式公式、Kodairaの還元分類、Néron局所成分の標準公式、K3のPicard数上界を利用した**記述証明**で、計算部分は再現可能。Lean形式化と外部査読は未実施。

**検算**：[v38_saturated_mw_verify.py](v38_saturated_mw_verify.py)。完全な群法則（2H=R+Q）、各有限ファイバーの付値、有限な局所寄与和、Shioda行列式の整数演算、良い還元を持つ2種類の有限体の全点・3倍写像の証明書を再計算する。

参考文献：
- Shioda, *On the Mordell–Weil Lattices*, 1990.
- Elkies–Kumar, *K3 surfaces and Hilbert modular surfaces*, 2014 (Néron–Severi判別式/高さ公式): https://msp.org/ant/2014/8-10/ant-v8-n10-p01-s.pdf
- Schütt–Shioda, *Elliptic Surfaces*, 2009: https://arxiv.org/abs/0907.0298
- 基礎資料：[v34](V34_QUADRATIC_K3_RANK_ja.md)、[v33](V33_GEOMETRIC_MORDELL_WEIL_ja.md)。
