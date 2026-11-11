# v97: v95平方因子分解のLean形式化と最終証明書の境界

2026-11-11。元の証明書 v9/v96 のPython算術検証に依存しない、**すべての曲線上の原始点について成り立つ新しいLean論理橋**を追加した。凍結済み `goal.json` の2最終定理の本文は変更していない。

## 1. 実施済みのLean追加

- [CFV97PrimitiveGcd.lean](v10_formal/CFV97PrimitiveGcd.lean)：`S ∣ n-2` と `q ∣ n-1` から `S.Coprime q`。原始性と `D+6Sp³=Tq³` から `gcd(D,q)=gcd(6S,q)=gcd(6,q)`。原始剰余 `e` が `T` を割ることも導出。
- [CFV97CurvePrimitive.lean](v10_formal/CFV97CurvePrimitive.lean)：前記結果を `CFCurveRecovery.lean` の原曲線恒等式へ接続。各候補に `h>0, h|6, e|T, D=h*e, q=h*v, gcd(e,v)=1` が**存在する**ことを証明。
- [CFV97SquarefreeBridge.lean](v10_formal/CFV97SquarefreeBridge.lean)：固定mathlibの `exists_sq_mul_squarefree` を使って `T/e=s*A²` の平方自由係数を構成。さらに `g²=(A²*s)*v` かつ `Squarefree s` なら `g=A*s*z, v=s*z²` と導く一般補題。
- [CFV97CompleteParameters.lean](v10_formal/CFV97CompleteParameters.lean)：上記を結び、**元の曲線方程式から** `q=h*s*z², g=A*s*z, n-1=h*A*s²*z³` の存在まで帰着。

最初の2モジュールについては、固定Lean 4.35.0・mathlib `56a005855ea17e0b0958f73ec801ae140b0a1679` の実行 [Actions #42987486901](https://github.com/corcondor/mathos/actions/runs/42987486901) で `exit=0`・`no proof holes=True` を確認した。残る2モジュールは **当該モジュールを含むActionsログを確認するまでLean証明成功と認定しない**。

## 2. 数学的導出

(D=Tq^3-6Sp^3) に対し、(D+6Sp^3=Tq^3)、(gcd(p,q)=1) から
[
h:=gcd(D,q)=gcd(6S,q).
]
(Smid n-2, qmid n-1) により (gcd(S,q)=1) なので
[
h=gcd(6,q)mid 6.
]
(D=he, q=hv) で (gcd(e,v)=1)。(g^2D=Tq) を (h) で除くと (g^2e=Tv)、したがって (emid T)。
(T/e=sA^2) を平方自由分解して
[
g^2=A^2sv.
]
(A^2mid g^2) だから (Amid g)。(g=Au) とすると (u^2=sv)。`Squarefree s` から (smid u) であり、(u=sz) とすれば (v=sz^2)。従って
[
oxed{q=hsz^2,quad g=Asz,quad n-1=hAs^2z^3.}
]
立方等式と合同式の末端は既存 `CFTwistedCubeAlgebra.lean` に存在する。

## 3. 形式証明で未解決の部分

**v97で完全には閉じていない。**

- **全5214曲線の有限連分数証明書**：v9/v96の4,877,566個の係数と候補排除をLeanが検査可能なデータ形式で渡し、各`S,T`のprefixの全域性、終端分母境界、平方・立方フィルターの網羅性をLeanで証明する。Pythonでの独立再現とLeanカーネルによる計算証明は別。
- **CFSmallDefectGoal**：一般近似被覆（既存Lean）・v97の必要条件（今回追加）・全係数有限証明書・最後の5点排除（既存Lean）をつなぐ正確な全称定理。
- **ThirtyCofactorGoal**：上記と、原二項係数等式から小不足分または有限例外へ到るv10の素因数・付値・有限983組の補題を形式証明する。

証明データを外部の未証明定理として仮定したり、Pythonの成功を `decide` の成功と読み替えたりしない。`sorry`, `axiom`, `native_decide` の埋め込みで最終定理を見せかけ上閉じることもしない。

## 4. 次の最短実装経路

`CFVerifierBridge.lean` / `CFCandidateCoverage.lean` は連分数の**一般的な**候補被覆をすでにLeanで証明している。従って新しい形式化の中心は、(i) 連分数prefixのチェック可能な符号・分母境界、(ii) 43,922係数のチェック、(iii) 5点分類の有限演算に分け、各段をLean側の`Bool`検証器とその健全性補題でつなぐこと。5,214曲線全部をLean証明本文に手書きで羅列することは避ける。

**判定基準：** 最終2定理の *元の文字列* が固定Leanで穴なしに通り、実CIログが残るまで、全問解決やLean形式化完了を主張しない。
