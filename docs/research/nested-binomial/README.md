# 入れ子の二項係数方程式の研究記録

> **v96（2026-11-09）— v95のねじれ立方数で全5214曲線の有限完全証明書を再構成**：**5214曲線・4877566連分数項の全prefix**を厳密dyadic立方根から再生成し、v95の \(q=hsz^2,\ n-1=hAs^2z^3,\ (6S/h)p^3+e=Th^2s^3z^6\) を使って**43922個の必要係数**を検算。**17370910既約近似候補→26258ねじれ平方一致→5個の完全整数復元点→必要条件を全て満たす点0個**。5点は \((S,T,n,r)=(1,225,10,30),(2,450,10,30),(4,900,10,30),(8,1800,10,30),(10,1681,82,246)\) のみで、全て \(n<104\) かつ \(r=3n\)。[v96全文と正確な証明射程](V96_TWISTED_CUBE_CF_COMPLETE_CERTIFICATE_ja.md)、[保存prefix不使用の再現Python](v96_twisted_cube_cf_complete.py)、[GitHub Actions全5214実行成功](https://github.com/corcondor/mathos/actions/runs/42632418243)。v9のCF網羅性補題は書面上の証明を継承するが、**全prefixと整数復元は再計算**。Lean形式化では[CFBoundedDivisorBridge](v10_formal/CFBoundedDivisorBridge.lean)、[CFTwistedCubeAlgebra](v10_formal/CFTwistedCubeAlgebra.lean)、[CFFiveRecoveredPoints](v10_formal/CFFiveRecoveredPoints.lean)を追加したが、**CF完全性と巨大有限証明書のLean内の網羅性はまだ未形式化、凍結最終2定理は未証明**。PythonのPASSをLean最終証明と混同しない。\n\n> **v95（2026-11-09）— CF小不足分の「ねじれ立方数」必要条件を強化し有限約数係数を89%削減**：原始曲線 \(6Sr^3=Tn(n-1)(n-2)\)（\(S\mid n-2\)）で \(g=\gcd(r,n-1),r=gp,n-1=gq,D=Tq^3-6Sp^3>0,g^2D=Tq\) とすると、\(h=\gcd(D,q)=\gcd(6,q)\mid6\)、\(e=D/h\mid T\)、\(T/e=sA^2\)（s平方因子なし）で、**\(q=hsz^2,\ g=Asz,\ n-1=hAs^2z^3\equiv1\pmod S\)**。さらに \(\gcd(h,S)=\gcd(e,s)=\gcd(T/e,S)=\gcd(s,6/h)=1\)、\((6S/h)p^3+e=Th^2s^3z^6\)。[v95記述証明](V95_TWISTED_CUBE_CF_CERTIFICATE_ja.md)、[完全必要係数監査](v95_twisted_cube_parameter_verify.py)・[実行成功ログ](https://github.com/corcondor/mathos/actions/runs/42568777616)により \(1\le S\le12,162S<T<229S\) の全5214曲線で**409728→43922**の有限係数絞り込みを検算。ただし43,922は実整数点数ではなく**必要パラメータ数**。[Lean CFBoundedDivisorBridge](v10_formal/CFBoundedDivisorBridge.lean) は既存v11のD∣6ST補題をDeepSeekのCF曲線回復系列へ接続する作業中で、Lean通過は実ログで確認するまでは宣言しない。あわせてv94の反転点の多項式検証で符号を修正し、[正しい10→6有理Kummer軌道の検算に成功](https://github.com/corcondor/mathos/actions/runs/42569005650)。**元の整数解候補10型は6型には減っていない**。DeepSeekの最終2目標、全ρの原方程式は未解決。\n\n> **最新監査 v91〜v93（2026-11-09）— v83/v86の誤推論を訂正、残る立方核10型の局所可解性を確定**：以前の「b=18で法100291の3型を排除」は、v=zuの置換でuを落とした誤り。具体的な平方リフト反例で**撤回済み**。[v91訂正](V91_REPAIR_FALSE_F100291_EXCLUSION_ja.md)・[独立検算](v91_corrected_local_descent_verify.py)。正しい係数型数は、v80の30→有効なF7で24→v90の三次ノルム障害で**10型（b=9で6、b=18で4）**。[訂正版v90](V90_CUBIC_NORM_RESIDUAL_OBSTRUCTION_ja.md)。v86のFrobenius–Bézout証明書は多項式の無根性として正しいが、**被覆型を排除する証明としては使えない**。[訂正済v86](V86_FROBENIUS_BEZOUT_LOCAL_CERTIFICATE_ja.md)。

> **v92：残差を割る素数でのノルム障害は必要十分**。cが三次剰余なら、u=2b/α、v=4b/β、a=−3b（α³=c, αβ=t）の滑らかな有限体点からHenselで三次・平方の真の局所解を復元。ρ=100003の残存10型全部でp=100003の局所t,n整除も成立。[v92証明](V92_SHARP_RESIDUAL_NORM_LOCAL_SOLUBILITY_ja.md)・[完全検算](v92_sharp_residual_cubic_local_verify.py)。

> **v93：残存10型は2・3・Mの関連素数でも局所可解**。強い3進Hensel（元のt,nの3進整数性を含む）、2進平方条件、Mを割る5・4003・100291の滑らかな局所点を具体的に構成。これらの局所計算だけでは残りを排除できない。[v93証明](V93_BAD_PRIME_HENSEL_CERTIFICATES_ja.md)・[全証明書](v93_bad_prime_hensel_verify.py)。**正階数の全整数点、全有理点、原の四変数方程式の全解は未解決**。

> **v81〜v86の有効部分**：ρ=100003, b=9・18 のMordell–Weil階数は厳密なL'非零＋Gross–Zagier–Kolyvaginから両方**1**と証明。[v81証明](V81_CERTIFIED_ANALYTIC_RANK_ONE_ja.md)・[ログ](https://github.com/corcondor/mathos/actions/runs/42480661353)。b=9で法7の6型の無解は[LocalCubeCover7.lean](v10_formal/LocalCubeCover7.lean)に形式化済み。[Lean成功](https://github.com/corcondor/mathos/actions/runs/42491178040)。v82/v84の小さい高さの非捩れ点探索とv87/v88の限定計算は完了しておらず、自由生成元の認証と全整数点の列挙は未達。


> **v74〜v77（2026-11-08）— 元問題の整数解は通常の第一楕円商の整数点に還元できる**：v20の六次式を \(\boxed{S^2=(6bX+b(8b^2+9\rho))^2+4X^3,\ X=a^2-b^2-\rho}\) と再編し、\(Y=(S-6bX-b(8b^2+9\rho))/2\in\mathbb Z\) により**整数係数の楕円曲線 \(Y^2+6bXY+b(8b^2+9\rho)Y=X^3\)** の整数点に全包含。このモデルではさらに \(b\mid X,Y\) と \(\gcd(\rho,b)=1\) を証明。[v74研究ノート](V74_INTEGRAL_FIRST_QUOTIENT_AND_RATIONAL_PARAMETERS_ja.md)。ユーザーの全有理リフトの2変数表示 \((k,q)\) の恒等式も検証し、唯一の例外 \(\Delta=0\) が原整数解ではgcd条件で排除されると証明。[v74 SymPy監査](v74_integral_model_and_parameter_verify.py)・[成功CI](https://github.com/corcondor/mathos/actions/runs/42473712378)。SageMathの **proof=True / gens_certain / integral_points** による実計算で、\(\rho=100003\) の12繊維中**10繊維を解析的高さ上界に依存せず完全排除**（b=1,27,54,486は既存v50の全有理点認証、b=2,3,6,81,162,243は今回の全整数点認証）。[v74](https://github.com/corcondor/mathos/actions/runs/42473712378)・[v75追加](https://github.com/corcondor/mathos/actions/runs/42474177013)・[v76のb=2成功](https://github.com/corcondor/mathos/actions/runs/42474514787)。**b=9,18のv77時点の階数0〜1は、その後v81で両方正確に1と証明**。ただし自由生成元と全整数点の認証は依然必要（[失敗＝未認証ログ](https://github.com/corcondor/mathos/actions/runs/42474744172)）。全 \(\rho\) の元式全解は未解決。\n\n> **v61〜v64（2026-11-08）— 第一楕円商の有理捩れ群を全分類、階数0の場合を残差無制限で排除**：v61はKubertの9位数Tate正規形とb∣486を結合し、**20本の三次Thue方程式の無条件PARI証明**から、9位数点が存在するTを **T=46648/9の1種類**に完全分類。[v61証明](V61_UNCONDITIONAL_NINE_TORSION_THUE_CLASSIFICATION_ja.md)・[PARI認証成功](https://github.com/corcondor/mathos/actions/runs/42462323854)。[v62 Sage認証](https://github.com/corcondor/mathos/actions/runs/42462716966) でその唯一の繊維の第一楕円商rank0・torsion9、種数2曲線の全有理点が無限遠の**2点のみ**と証明。v63は第一楕円商の2位数点を半分にする条件を6本の四次Thueへ縮約し、**全てを無条件PARIで解いた結果、12位数点は許される全Tで存在しない**。[v63証明](V63_UNIFORM_TWELVE_TORSION_EXCLUSION_ja.md)・[PARI完全認証](https://github.com/corcondor/mathos/actions/runs/42463177794)。[v64統一定理](V64_UNIFORM_POSITIVE_RANK_NECESSITY_ja.md) より、**元の主枝に整数解があるなら必ず第一楕円商 \(E_{1,\rho/b^2}(\mathbb Q)\) の階数≥1**（**残差の上限なし**）。[全捩れ場合分けの証明書](v64_uniform_rank_certificate.json)。**正階数の種数2全有理点と原方程式全解は未解決**。Lean新定理の形式化・外部査読未実施。\n\n> **v58〜v60（2026-11-08）— 残差の二つの悪い還元因子から高次捩れを一様制限**：第一楕円商の判別式は \(\Delta=-243T(8+9T)^3<0\)、Mazur分類より捩れ群は3,6,9,12のみ。\(p\ge5\mid\rho\)、\(e=v_p(\rho)\) に対し9/12捩れはそれぞれ \(N\mid e(p-\chi_p)\)、\(\chi_p=(-3/p)\) を要求。[v58定理](V58_BAD_REDUCTION_HIGH_TORSION_SIEVE_ja.md)・[検算](v58_bad_reduction_torsion_verify.py)。さらに \(M=8b^2+9\rho\) の素因数 \(p\ge5\) では分裂乗法的還元 \(I_{3v_p(M)}\) なので、高次捩れには \(N\mid3v_p(M)(p-1)\) が必要。[v59定理](V59_DUAL_MULTIPLICATIVE_TORSION_SIEVE_ja.md)・[検算](v59_two_bad_fibres_torsion_verify.py)。**\(v_p(\rho)=1,\ p\bmod36\in\{5,7,29,31\}\)**、または **\(v_p(M)=1,\ p\equiv11\bmod12\)** なら9位数・12位数を両方排除。既存v50/v56と合わせ、その場合の元の整数解には第一楕円商の**正階数**が必要。[v60統合実行可能ふるい](v60_unified_first_quotient_torsion_sieve_verify.py)。**正階数の全有理点と原方程式全体は未解決**。新しいSage mwrank_lib再試行は時間上限で終了、未証明として保存。\n\n> **v54〜v56（2026-11-08）— 捩れ6の例外を一様排除**：\(T=24\) の第一楕円商はSageMathで **rank0、torsion \(\mathbb Z/6\)** を認証し、種数2曲線の全有理点が **無限遠2点＋有限10点＝12点**と完全分類。[v54全有理点の証明](V54_TORSION_SIX_COMPLETE_RATIONAL_POINTS_ja.md)・[v55 Sage証明ログ](https://github.com/corcondor/mathos/actions/runs/42459489183)。さらに **[v56無限領域の排除定理](V56_UNIFORM_TORSION_SIX_OBSTRUCTION_ja.md)**：元の枝の整数解を与える第一楕円商がrank0・torsion6という可能性を、**すべての \(\rho>0\)** について排除。2位数パラメータ \(v=m/d>1\) に対して \(d^3\mid2b^2\)、\(b\mid486\) を導き、元の \(t,n\) 復元式から \(1<v<5\) に限定。588個の構造的候補（異なるvは215個）のうち平方条件を満たすのは \(v=4\) のみで、\(n=0,28<104\)。[v56実行検算](v56_uniform_torsion_six_exclusion_verify.py)・[GitHub Actions成功](https://github.com/corcondor/mathos/actions/runs/42459815542)。**v50の捩れ3の場合と合わせ、第一楕円商がrank0・torsion3または6なら元の主枝に整数解はない**。rank正、捩れ9/12、元の全四変数式は未解決。Lean形式化・査読未完了。\n\n> **v50〜v52（2026-11-08）— 特定の種数2繊維の全有理点を完全決定**：第一楕円商への写像 \(x=u^2-1-T,\ y=(s-6x-8-9T)/2\) を用い、第一楕円商の階数0・捩れ群 \(\mathbb Z/3\) なら \(C_T(\mathbb Q)\) は無限遠2点と、\(1+T\) が有理平方のときの境界4点だけと証明。[v50全有理点定理](V50_FIRST_QUOTIENT_ALL_GENUS2_RATIONAL_POINTS_ja.md)。\(\rho=100003,\ b\mid486\) の**12繊維すべて**をSageで実行し、**b=1,27,54,486の4繊維では全有理点が無限遠2点のみ**と完全認証。[12繊維Sage証明ログ](https://github.com/corcondor/mathos/actions/runs/42458789976)。[v51有限体検算](v51_first_quotient_torsion_all_b_verify.py) で全12繊維の第一楕円商の捩れ群を正確に \(\mathbb Z/3\) と決定。[v52高努力再試行](https://github.com/corcondor/mathos/actions/runs/42458994249) で b=2の階数1も証明、b=9,18は階数0〜1で未確定。b=3は階数3、b=6,81,162,243は階数1。**[正確な全12繊維の証明マニフェスト](v50_v52_fibre_proof_manifest.json)**。残りの種数2繊維・第二楕円商の全有理点・原方程式全体は未解決。\n\n> **v44（2026-11-08）— 全ての元解候補を対象にする検査**：既知のMordell–Weil部分群に属するとは仮定せず、v21の解析的高さ上界 \(a^2<152\rho\log\rho\) により、残差 \(32770\le\rho\le100000\) の**全ての元の整数解に対応し得る有理点**を有限整数復元として網羅。**685,305,097組**の必要合同・大小条件、987件の六次平方点、9件の枝候補を検査し、両k分岐ともLucas反証。結果 \(\boxed{\rho\ge100003}\)。[v44証明](V44_ALL_RATIONAL_INTEGER_LIFTS_ja.md)・[数値検証器](v44_all_integer_lifts_verify.py)・[9件の反証証明書](v44_certificate_summary.json)。**楕円曲線の全有理点そのものを列挙したわけではない／全てのρを排除したわけではない**。解析的上界と復元公式は既存v20/v21に依存。

> **v40〜v43（2026-11-08）：二次K3の全切断に対する高さ下限を8/3へ改善**。v40で未処理の3R±H、4R±H、5R±Hを16,866件の構造的候補（整除条件で事前に有限化）から全排除。[v40証明](V40_FULL_LOW_ODD_H_SIEVE_ja.md)・[検算](v40_odd_H_extended_verify.py)。v41では飽和MW基底R,HのShioda高さが **h(mR+nH)=((2m+n)²+9n²)/60** という正定値2次形式を持つことから、係数の事前上限なしに**h<13/6の高さ球全体**を一括排除。[v41証明](V41_CANONICAL_HEIGHT_BALL_ja.md)・[検算](v41_height_ball_verify.py)。v42では高さ13/6の全境界3方向を多項式結果式で74,664約数へ厳密有限化して排除、下限を12/5へ。[v42証明](V42_RESULTANT_HEIGHT_BOUNDARY_ja.md)・[検算](v42_height_boundary_verify.py)。v43では6Rと2Q,±R+2Qをさらに排除し、**全整数係数(m,n)のうちh<8/3の全切断**から元問題の許容整数候補を除外。[v43証明](V43_UNIFORM_HEIGHT_EIGHT_THIRDS_ja.md)・[検算](v43_height_8_over_3_verify.py)。**高さは関数体上の切断高さであり、個別Tで増える有理点や元の四変数方程式全体には適用しない。** 証明は既存のShioda理論と記述証明＋CAS/整数全検算に基づき、Lean形式化と外部査読は未実施。

> **v39（2026-11-08）**：v38で確定した真の飽和MW基底 R,H に対し、これまで未解析だった **奇数H係数の点 P=mR±H（|m|≤2）** からも原問題の許容整数候補は生じない。H,R+H,2R+H は大きさで全排除。R−Hは **(4p+3b)²−(4a)²=b²** の因数対78組を完全分類し、ただ1つの初期候補をgcdで排除。2R−Hは **p−3b∣80b³** による1326候補・38平方候補を厳密検査し、全て既存条件に反する。[v39証明](V39_ODD_HALF_SECTION_EXCLUSION_ja.md)・[GitHub検算プログラム](v39_odd_H_integral_sieve_verify.py)。全ての整数係数 m,n の点・個別Tの全有理点・元の方程式全体は未解決。

> **v38（2026-11-08）— 二次K3の幾何学的Mordell–Weil飽和を完全認証**：v34の2点 R,Q は真の基底ではない。明示的な半分点 H=(-2(q−1)(q+1)²(2q+1), 6(q−1)(q+1)²(2q+1)(3q−1)) を発見し **2H=R+Q** を証明。Shioda高さ h(R)=1/15, h(Q)=3/5、幾何学的捩れ0、NS判別式整数性で残る飽和指数を3に限定し、**q=2,3・有限体F41,F17での4方向の非3可除性**ですべて排除。結果：**E(Q̄(q))=E(Q(q))=ℤR⊕ℤH**、高さ行列 [[1/15,1/30],[1/30,1/6]]、|disc NS|=27。[v38証明全文](V38_SATURATED_K3_MW_LATTICE_ja.md)・[自動検算プログラム](v38_saturated_mw_verify.py)。[v37](V37_FIFTH_K3_SECTION_ja.md)では5R±Qも全排除し、既存の二次族で |m|≤5 の mR±Q を完全に排除。**個々の有理数Tへの特殊化群全体・原方程式全体は未解決**。Lean形式化・外部査読未実施。

> **v36〜v37（2026-11-08）**：二次K3族 T=(p/b)²−1、b∣486 で、非巡回点 mR±Q を **|m|≤5 の全ての整数 m** について排除。v36は m=2,3,4 を整除条件により 819+391+2457=3667候補に厳密有限化し、2方法で照合。[v36証明](V36_EXTENDED_K3_INTEGRAL_SIEVE_ja.md)・[再現](v36_noncyclic_sieve_verify.py)。v37は **5R+Q** の分母二次式 D に対して Bézout 恒等式で **D∣2592000b⁵** を証明し9660約数を完全検査、**5R−Q** は p<5b に限定して3141候補を全検査。どちらも整数平方条件を満たさない。[v37証明](V37_FIFTH_K3_SECTION_ja.md)・[再現](v37_fifth_section_verify.py)。元の方程式全体・一般の mR+nQ・特殊化群全体は未解決。新しい結果はLean未形式化・未査読。

> **v33〜v35（2026-11-08）— 楕円曲面の階数の決定と非巡回点の排除**：v33で第二楕円商の **E(Q̄(T))=ℤR**（幾何学的階数1・捩れ0・R primitive）をShioda–Tateと高さで導き、種数2補助曲線に有限のQ̄(T)-有理点がないことを証明。[v33証明](V33_GEOMETRIC_MORDELL_WEIL_ja.md)・[演算監査](v33_generic_mw_verify.py)。v34は **T=q²−1** で独立な新切断Qを構成、二次基底変換K3の **幾何学的/算術階数2・Picard数20** を証明。[v34証明](V34_QUADRATIC_K3_RANK_ja.md)・[有限体検算](v34_quadratic_k3_verify.py)。v35は **Q, R±Q** の整数復元を剰余定理 d∣45b³ で630候補に縮約し、厳密な条件を満たす整数候補がないことを完全検算。[v35証明](V35_BOUNDARY_K3_EXCLUSION_ja.md)・[再現](v35_boundary_combination_verify.py)。適用範囲は一般関数体と指定された二次基底変換族であり、原方程式全体の無解証明ではない。新定理はLean未形式化・外部査読なし。

> **v32（2026-11-08）**：種数2補助曲線の **T≡3 (mod5) 全5進衝突**について、\(a\) に上限のない平方判定を完成。v31で残った **T≡18 (mod25)** も含み、零点は0・2・4個と分類、平方を満たす \(a\) の厳密Haar密度を6枝に分けて算出。零点のない場合は有限法で完全判定できる一方、単純5進零点がある場合は **どの固定の法5の冪でも一様な平方判定が不可能** と証明。[v32数学的証明](V32_PADIC_SQUARE_COMPLETION_ja.md)・[287,500件の完全検算](v32_padic_complete_verify.py)・[独立SymPy恒等式監査](v32_symbolic_verify.py)・[証明書](v32_certificate.json)。これらは元の整数点問題の必要条件であり、元問題の無解証明やLean形式証明ではない。

> **自動研究連携**：[公開時のGitHub Actions検証とDeepSeek仮説生成](AUTORESEARCH_PIPELINE_ja.md)。新しいvNNノートのPR時は数値検査、master公開時はActions APIキーがあれば独立した新規仮説を生成（**UNVERIFIEDのドラフトPR**）。Lean証明は別の固定環境で再検証。Codespacesの既存97アクション状態や固定Lean最終2目標は変更しない。


> **v31（2026-11-08）**：六次平方条件 \(S²=F(a,b,ρ)\) について、**T=ρ/b²≡13 (mod25) ⇒ 5∤a** を巡回部分群の仮定なしに証明。さらに ℓ=v₅(8+9T) が奇数の場合、5進平方性と **5^((3ℓ+1)/2)∤(6a²+2b²+3ρ)** の同値条件を完全導出。別に、10素数の局所合同条件を厳密CRTで結合し、⟨R⟩ に写る候補の残存合同類密度を **1.48474%→1.20905%** に改善（元の四変数問題の全候補の密度ではない）。[v31証明](V31_PADIC_AND_WEIGHTED_SIEVE_ja.md)・[標準Python検算](v31_weighted_local_sieve.py)・[SymPy照合](v31_symbolic_crosscheck.py)・[証明書](v31_certificate.json)・[ハッシュ](v31_manifest.json)。深い5進衝突の全排除、特殊化のMordell–Weil基底認証、元の問題全体は未解決。\n\n> **v30追補（2026-11-07）**：v28・v29の局所公式を再検算し、**7∣ρ ⇒ m≡12,13,17,18 (mod 30)** を導出。5進条件とCRT結合して、元の補助整数点が **⟨R⟩ に写る**場合の残存合同類密度を **304/20475 ≈ 1.4847%** と算定（一般の四変数解の98.5%排除という意味ではない）。[v30証明追補](V30_LOCAL_CRT_NOTE_ja.md)・[再現Python](v30_local_crt_verify.py)・[DeepSeekへの研究引継ぎ](DEEPSEEK_V30_HANDOFF_ja.md)。DeepSeek依頼は[Issue #3](https://github.com/corcondor/mathos/issues/3)に登録済み。深い5進衝突とMordell–Weil基底は未解決。元の固定Lean最終2目標は変更していない。

> **v29（2026-11-07）**：[5進特異ファイバーの証明](V29_PROOFS_ja.md)で T≡3 (mod25) の巡回部分群の解候補を排除。T≡13,18 (mod25) の深い衝突と非巡回有理点は未解決。

> **v21（2026-11-07）**：v20 の対数差と残差の式から **a²<152ρ logρ** を証明し、固定ρの **n<2²⁴√ρ(logρ)^(5/2)** に改善。δ側の原始係数 (c,h) に対する厳密な二次式 **ℒh²−18𝒯hc+81𝒲²c²=0** を導出し、**c|ℒ, h|81𝒲²** と明示的なδ上界を得た。さらに全 **13≤ρ≤4096** を二実装で完全監査（36,892,376入力、最終8組、δ≥25で3組、元の両分岐の合同式で0組）して **ρ≥4099** を証明。詳しくは [v21日本語進捗](PROGRESS_v21_ja.md)、[証明と恒等式](v21_proofs.md)、[監査生成器](v21_residual_audit.py)、[独立検査器](v21_residual_verify.py)、[完全証明書](v21_residual_certificate.json)。枝全体も元の四変数問題も未解決。

> **v20（2026-11-07）**：元の二項係数の大小から **r−3n > 2n/(5 log n)**（n≥1024）を証明し、補分岐の **canonical J≥33** を全δ・全nで確定。全5,323係数族の約数証明書を独立再構成した。固定Jの高さを小分岐 **n<2¹²J^(3/2)(1+log J)**、補分岐 **n<2²⁵J³(1+log J)²** へ改善し、固定δも **log n<17δ、n<2^(24δ)** へ。整数復元から **gcd(a,ρ)=gcd(a,3)、ρ mod9∈{1,4,6,7}、ρ≥13** と3次被覆の全指数の制限を追加。固定(δ,J)の実装・2クエリ31,682方程式の独立検証も収録。詳細は [v20日本語進捗](PROGRESS_v20_ja.md)、[検証範囲](v20_review_ja.md)、[再現手順](v20_reproduction.md)、[全成果物](v20_manifest.json)。元の四変数問題は未解決。

> **v19追補（2026-11-07）**：消去イデアルから共通約数Gの全素数冪を制限し、**n²<2¹⁸δ³J／2³³δ⁵J**（小／補分岐）の結合高さを証明。全3,571係数族を**2,818,386区間の格子縮小**で完全に再生成し、Pell法・別実装と照合。残差の明示的な3次被覆と、**ρ/b²だけの法素数検査では法5の例外が唯一**という全素数の結果を追加。旧δ≥25・ρ≥11・小分岐J≥17は維持。詳細は [v19追補](PROGRESS_v19_supplement_ja.md)、[レビュー](v19_supplement_review_ja.md)、[証明書・ハッシュ](v19_supplement_manifest.json)。元の四変数問題は未解決。

> **v19本文（2026-11-07）**：主対象 ell=1, j=i−3 で **δ≥25、ρ≥11**、小分岐 **canonical J≥17** を証明。新しい一様条件 **J≢2 mod4**、小分岐 **v₂(J)∈{0,2}**、**ρ≢b² mod5** を追加。固定(a,b)残差曲線の明示点が、唯一の例外(3,1)を除き**無限位数**であることも証明し、例外を原式の残差条件で排除。種数2の曲線と別の楕円商、3ねじれ点と平方根境界の対応を整理。全145,195 Pell点、110 Bézout恒等式、ρ≤10の全有限領域を独立検証。2025〜2026年の楕円曲線・暗号・RUR文献の仮定と実行範囲を記録。詳細は [PROGRESS_v19_ja.md](PROGRESS_v19_ja.md)、[検証範囲](v19_review_ja.md)、[全記録](v19_manifest.json)。新結果のLean形式化・元問題全体の解決は未完了。

> **v18（2026-11-07）**：主対象 ell=1, j=i−3 で、**r−3n+3>n^(5/8)/40、n^(7/11)/96** を証明。小さい分岐では全適用二次式 **n²−c | lcm(1,…,r)²**、全奇数指数に **p<12w**。既約分子Jにより **n<16J⁶、J≥2**（小分岐）、固定Jごとに **n=O(J^(33/14))／O(J^11)**（小／補分岐）。さらに **gcd(δ,J)|25／72**、明示的二次式への素因数移送と条件付きδ⁴高さを追加。全830例外・四方向の独立点検がPASS。詳細は [PROGRESS_v18_ja.md](PROGRESS_v18_ja.md)、[検証範囲](v18_review_ja.md)、[全記録](v18_manifest.json)。新結果のLean形式化・元問題全体の解決は未完了。

> **v17（2026-11-06）**：主対象 ell=1, j=i−3 の両分岐で、**r>3n+3√n** と **h≥93M、r−3n+3>√(31n/3)** を証明。平方根境界の全13組を557係数・94,710残差へ帰着し、元式の26分岐を独立再現して排除。さらに **P⁺(n)<3√n、P⁺(n−1)²≤6n−9**、**(n²+2)/p≥65**、最大12二次式の反復素因数の同時制限を追加。n≡3 mod6ではn²+1がlcm(1,…,6n−9)²を割る。詳細は [PROGRESS_v17_ja.md](PROGRESS_v17_ja.md)、[検証範囲](v17_review_ja.md)、[全記録](v17_manifest.json)。新結果のLean形式化と元問題全体の解決は未完了。

> **v16（2026-11-06）**：主対象 ell=1, j=i−3 の両分岐で、実際の不足約数 **δ=Q/gcd(Q,r²)≥13** と **log n<28δ** を証明。1,223係数族・全34,010 Pell点を独立再現し、残る246分岐を23以下の素数で全排除。さらに **r−3n+3>n^(3/5)/64**、**P⁺(n²−10)<r**、重複する大きな素因数の指数・分岐制限を追加。δと旧来のHは互いに素。詳細は [PROGRESS_v16_ja.md](PROGRESS_v16_ja.md) と [全記録](v16_manifest.json)。記述証明・整数検証の結果であり、新結果のLean形式化と全問題の解決は未完了。

> **v15（2026-11-06）**：主対象 ell=1, j=i−3 の両分岐で、第一添字の個数を **O(√X log X)** に改善。**n²+2 が素数の場合を一様に排除**し、各素因数にも上限を証明。さらに **Q∤r²** を25本のPell方程式と独立計算で示し、**n または n−1 に素数の三乗が必要**と判明。Qに含まれる最大の立方因子κ³について **log n<28κ** も得た。詳細は [PROGRESS_v15_ja.md](PROGRESS_v15_ja.md) と [全記録](v15_manifest.json)。新規Lean実行はなく、元の四変数問題は未解決。

> **v14（2026-11-06）**：主対象 ell=1, j=i−3 で、**n,n−1,n−2 の異なる二つに、11以上の素数が3の倍数でない指数で必要**と証明。従って **HT=2^a3^b5^c7^d p^e u³ を、任意の素数 p≥11・全指数・全Hで一括排除**。二因子の立方剰余部分が2・3・5・7だけで支えられる第一添字は正確に57個、最大13720。既存 n≥104 に残る18個も全排除。新規125本の完全Thue計算と二つの整数検証を記録。詳細は [PROGRESS_v14_ja.md](PROGRESS_v14_ja.md)、[証明](v14_two_factor_support.md)、[全実行記録](v14_manifest.json)。T単独で二素数が必要とは限らず、元の四変数問題は未解決。

> **v13（2026-11-06）**：主対象 ell=1, j=i−3 において、**T=2^a3^b5^c7^d u³ の全族を、H に上限を置かず排除**。立方因子を除いた係数を625本の Thue 方程式にまとめ、全24第一添字を取得し、残る5個を整除・厳密区間で排除した。従って **ある素数 p≥11 で v_p(T) が3の倍数でないことが必要**。一般の固定素数集合 S では Bennett の既知定理から第一添字の個数を (5^|S|−1)/2 以下に抑えた。全証明・計算の範囲は [PROGRESS_v13_ja.md](PROGRESS_v13_ja.md)、[一様排除の証明](v13_uniform_cube_support.md)、[実行記録](v13_manifest.json) を参照。新しい Lean 実行・元の四変数問題の完全解決はしていない。

> **v12（2026-11-06）**：原始不足分 H=14〜20 を全4,690曲線・57,160,284既約分数の厳密計算で排除し、H≥21へ。楕円曲線の3位数点、正の階数を持つ補助曲線の例、三連続整数のcube-free必要条件を追加。詳細は [PROGRESS_v12_ja.md](PROGRESS_v12_ja.md)、[算術幾何ノート](v12_three_descent.md)、[独立再現コード](v12_independent_dyadic_verifier.py)、[検証値と証明書SHA](v12_results_manifest.json)。元の四変数問題は未解決です。

\[
\boxed{\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}}
\]

右辺は上下の添字を二乗した二項係数。通常の非負整数の範囲で扱う。

**状態：全体の解の分類は未完了。具体的な解も未発見。**
部分的な無限族の排除と必要条件を記録する。
必要条件を満たすことを、元の式の解であることとは扱わない。

## 読み始める場所

- **[最新：v20 日本語概要](PROGRESS_v20_ja.md)**
- [対数幅と固定Jの新しい高さ](v20_logarithmic_gap.md)
- [補分岐J≤32の完全排除](v20_complement_J_exclusion.md)
- [固定δの二進高さ24δ](v20_binary_height_24.md)
- [整数復元・ρ≥13・2進3進の被覆制限](v20_residual_integrality.md)
- [固定(δ,J)の完全再構成と正符号根の一意性](v20_fixed_parameter_reconstruction.md)
- [v20の検証範囲](v20_review_ja.md)
- [v19追補](PROGRESS_v19_supplement_ja.md)
- [v19 日本語概要](PROGRESS_v19_ja.md)
- [残差楕円曲線の一様な無限位数点](v19_residual_positive_rank.md)
- [種数2と楕円商・3ねじれ境界・ρ≥11](v19_elliptic_residual.md)
- [canonical J≥17と110本のBézout証明書](v19_canonical_J_elimination.md)
- [最新小根法の条件検査・δ≥25の完全Pell排除](v19_crypto_methods.md)
- [v19の独立検証と適用範囲](v19_review_ja.md)
- [v18 日本語概要](PROGRESS_v18_ja.md)
- [5/8・7/11の下限と固定残差の高さ](v18_residual_gap.md)
- [全指数の短いLCM条件・全830例外](v18_short_lcm.md)
- [任意共通約数と既約J・両分岐の多項式高さ](v18_neighbor_cofactor_height.md)
- [不足約数δへの消去式・条件付き四次の高さ](v18_defect_resultants.md)
- [v18の証明と独立検算の範囲](v18_review_ja.md)
- [v17 日本語概要](PROGRESS_v17_ja.md)
- [平方根境界の13組の完全分類・新しい楕円曲線と高さ](v17_square_root_gap.md)
- [主添字と二次式の素因数・全指数の同時制限](v17_quadratic_prime_powers.md)
- [n²+2の補因子64以下の全排除・δとの接続](v17_neighbor_defect.md)
- [平方根境界の別符号化による完全監査](v17_square_root_gap_independent_audit.md)
- [補因子の別の約数生成による完全監査](v17_neighbor_defect_independent_audit_note.md)
- [v17の記述証明・完全検算・支持検算の範囲](v17_review_ja.md)
- [v16 日本語概要](PROGRESS_v16_ja.md)
- [実際の不足約数δの構造・高さ・一般Pell帰着とδ≤12の完全排除](v16_square_defect_pell.md)
- [r−3nの五分の三の下側評価：全素数・全Hに一様](v16_lower_gap.md)
- [n²−10など複数の二次式に対する最大素因数制限](v16_quadratic_neighbors.md)
- [重複する大きな素因数の正確な指数と分岐の分類](v16_repeated_neighbor_primes.md)
- [Pell全証明書の独立再現と検証範囲](v16_square_defect_independent_audit_note.md)
- [並行するDeepSeekのv16研究・形式化の作業記録](DEEPSEEK_V16_WORK.md)
- [v15 日本語概要](PROGRESS_v15_ja.md)
- [第一添字の個数を O(√X log X) に改善する一様な証明](v15_cubic_defect_sparsity.md)
- [n²+2 の素数値を全排除し、任意の素因数を制約](v15_neighbor_prime_obstruction.md)
- [Q∤r² と必須の立方因子：完全なPell帰着と独立検証](v15_pell_square_divisor.md)
- [立方因子の大きさからの高さ上限 log n<28κ](v15_cube_height.md)
- [v14 日本語概要](PROGRESS_v14_ja.md)
- [大きな非立方指数の素数は三連続整数の二か所に必要：任意の追加素数を一括排除](v14_two_factor_support.md)
- [v13 日本語概要](PROGRESS_v13_ja.md)
- [H に依存しない立方因子の型による一括排除と一般の候補数定理](v13_uniform_cube_support.md)
- [三連続整数の正確な立方降下と素数冪の配分](v13_exact_three_factor_descent.md)
- [v12 日本語概要](PROGRESS_v12_ja.md)
- [v11 日本語概要](PROGRESS_v11_ja.md)
- [平方値のCRT：固定したiの各素因数分配で平方値が最大4候補、E≥512なら最大1候補](v11_simultaneous_square_interval.md)
- [実際の不足分H=13を完全排除：新しい約数ふるいと二方式の連分数](v11_effective_defect_cf.md)
- [二進付値による192の改善と、全94余因子の排除](v11_cofactor_extension.md)
- [指数に依存しない局所平方条件と、無制限の余因子を持つ族の排除](v11_local_square_filters.md)
- [i−3の素数冪に対する三次上限と四余因子の全排除](v11_mixed_structure.md)
- [v11の実行済みLean証明8定理と未形式化の範囲](v11_formal/README.md)
- [v10 日本語概要](PROGRESS_v10_ja.md)
- [元の等式からの付値回復、混合素因数のCRT条件、一般の高さ上限](v10_valuation_recovery.md)
- [w/gcd(w,6)≤12 の全30余因子を全素数・全指数で排除](v10_small_cofactors.md)
- [一般の付値回復補題と円分の有限合同計算の実行済みLean検証](v10_formal/README.md)
- [円分因子の小さい剰余環による排除と外部定理依存の縮小](v10_cyclotomic_auxiliary_rings.md)
- [v9 日本語概要](PROGRESS_v9_ja.md)
- [連分数による GCD 不足分 S≤12 の全排除](v9_gcd_defect_continued_fractions.md)
- [任意の固定余因子に対する正確な GCD 公式と有限上限](v9_gcd_structure.md)
- [i=2P^a+2 の全素数・全指数の排除](v9_cofactor_two.md)
- [新しい2,592件の有限算術証明書の Lean 検証](v9_formal/README.md)
- [円分因子の primary trace による全指数の制約](v9_cyclotomic_primary_trace.md)
- [v8 日本語概要](PROGRESS_v8_ja.md)
- [シフト素数冪 i=P^a+2 の完全排除](v8_shifted_prime_power_completion.md)
- [全2,903件の有限算術証明書の Lean 検証](v8_formal/README.md)
- [大きい素数冪因子の一様な分類](v8_composite_dominant_prime_powers.md)
- [一般の共通約数の不足分による高さ上限](v8_gcd_defect_height.md)
- [円分因子7q^aの偶数指数・高次付値の制限](v8_cyclotomic_even_exponents.md)
- [v7 日本語概要](PROGRESS_v7_ja.md)
- [v6 日本語概要](PROGRESS_v6_ja.md)
- [版ごとの研究記録](RESEARCH_LOG.md)
- [新しい共通約数と i-1 が平方自由な場合の完全排除](v6_common_divisor.md)
- [対数幅、R≤12 の排除、候補の疎性](v6_offset_composite.md)
- [素数冪に必要な Wieferich 因子](v6_offset_prime_powers_wieferich.md)
- [円分因子による制限と p²+p+1=7q の完全排除](v6_large_prime_cyclotomic.md)
- [v6 の Lean 検証範囲・実行方法](v6_formal/README.md)
- [v5 日本語概要](PROGRESS_v5_ja.md)
- [v4 日本語概要](PROGRESS_v4_ja.md)
- [ell=1、j=i-3 の区間・付値の証明](v5_offset_three_structure.md)
- [i=3^a の全指数の排除](v5_offset_three_three_power.md)
- [i=jp^3 の一候補への絞り込みと高次合同式](v5_large_prime_localization.md)
- [v5 の Lean 検証範囲・実行方法](v5_formal/README.md)

## 2026年11月5日の追加：v11

ell=1、j=i−3 の枝で、各候補iに対してEを零剰余側Zと残存側Hに分け、
平方の値を先にCRTでまとめた。K=F³/B、u=Zv、J=KZ²とすると、
162H<Jv³<229H と v²=R+mH の同時条件になる。mの区間幅は
8/(EK²Z³)^(1/3)未満で、各分配につき最大4個、E≥512なら最大1個の整数検査。
第一添字iそのものの個数を4個に限定したという意味ではない。

H=A/gcd(A,r³)=13の804曲線を新しいD|6HTの約数ふるいで全排除し、H≥14へ強化。
完全な1,173,389項の連分数証明書と、三次多項式を直接変換する別実装が一致した。
二進桁の3回の繰り上がりからE|(i−2)/gcd(i−2,192)を証明し、
w/gcd(w,192)≤13の全94余因子を全素数・全正指数で排除した。
主領域28,316組・別の広域69,223組を、元のiやrの全区間走査なしで完全検証した。
一般の高さもlog i<128w/gcd(w,192)へ改善。

奇素数の正規化単元を指数に依存しない式へ還元し、4w<p<6wで特定の小二項係数が
非平方ならi=wp^(3t+1)+2を全tで排除。余因子19、23、41など94種類外の具体族も得た。
さらにi−3側ではA−1の因子とr(r−1)の整除を使い、p≥7、p≡3 mod4に対して
i=wp^a+3ならi<4000w³/3+1、w=1..4ではp=2またはp≡3 mod4を全指数排除した。

一般の整除・整数区間・定数に関する8定理をLeanで実際に実行し終了0。
全CRT・CF完全性・94族の全証明まで形式化済みとはしない。
詳しくは [v11 日本語概要](PROGRESS_v11_ja.md) と
[v11_manifest.json](v11_manifest.json) を参照。

## 2026年11月5日の追加：v10

ell=1、j=i-3 の枝で、元の等式から A|r(X+r²) を保つと、
α=v_p(A)、x=v_p(X)、e=v_p(r) に対し 3e<α⇒x=2e が必要になる。
特にxが奇数なら、Aのその素数成分は全てr³へ回復する。
回復後の不足分Eは旧Sの約数で、既存の完全なCF結果を移すことで E≥13 が必要となる。
さらに残る各素数について平方合同と零剰余の二択を作り、CRTで同時に扱う。
r=Fu とした商の範囲は u³<229E に収まる。

任意の i=wp^a+2 に対し、底pの大きさを仮定せず、
log i<128w/gcd(w,6)、i<2^(192w/gcd(w,6)) まで一般上限を改善した。
w/gcd(w,6)≤12 の全30余因子は、全素数・全指数で排除を完了した。
理論から得た全983組・955添字を厳密に排除し、別実装でも証明された広い領域
2,423組・2,393添字を証明書なしで再現した。
任意の正確な素数冪因子 q|i−2 について、q≤(i−2)/13 が必要となる。

円分枝では法2・5・7の一様な条件を導き、v9で残ったq=19,31,67を全指数で排除。
q≥241、偶数指数ではq≥463が必要になった。素数pのこの枝での3|a排除は
4元体の短い証明で代替でき、当該結論のThomas–Mignotte依存を除去した。
v7の一般の整数に対する、より広い定理の外部依存はそのまま保持している。

今回は局所付値回復の一般補題自体をLeanで実際に実行し終了0を確認。
円分枝の20個の有限算術定理も実行済み。積全体、平方合同、CRT、CF移植、
解析的高さ評価、30余因子の有限領域全体まで全形式化したとはしない。
詳しくは [v10 日本語概要](PROGRESS_v10_ja.md) と
[v10_manifest.json](v10_manifest.json) を参照。

## 2026年11月5日の追加：v9

ell=1、j=i-3 の枝全体に対し、A=C(i,3)、X=C(i²,6i−9)、
S=A/gcd(A,X) とすると S≥13 が必要だと証明した。
S≤12 なら理論的に残る全5,214曲線を連分数の完全な近似分類で扱い、
全係数を保存した証明書と別実装の再計算で候補0件を確認した。
第一添字の上限まで整数を順番に走査していない。

一般の i=wp^a+2 では、p∤w、p^a>4w のとき
D_w=C(6w,2w)/gcd(C(6w,2w),6)、c_w=w/gcd(w,6) を用いて
v_p(S)=v_p(D_w)、S|c_w p^v_p(D_w) を証明した。
これにより全ての固定余因子 w について、明示的に有限化できる。

i=2P^a+2 は全素数・全指数で完全排除した。
別の付値と整数商による証明で残る全2,592件は Lean で実際に検証済み。
一般 GCD 公式と S≤12 の排除からも、v8 の i=P^a+2 と併せて再証明できる。

円分因子7q^aの枝は、Eisenstein整数の primary trace から指数に依存する
合同式を導き、q≤211の全21底のうち18底を全指数で排除した。
偶数指数では q≥367 が必要で、4q=1+27m²（q≠7素数）の形も全指数で排除。
奇数指数の付値と二項係数の縮約も強めた。

証明・全証明書・検算・監査と未形式化の範囲は
[v9 日本語概要](PROGRESS_v9_ja.md) と [v9_manifest.json](v9_manifest.json) に記録する。
元の四変数方程式の全体は引き続き未解決である。

## 2026年11月5日の追加：v8

ell=1、j=i-3、i=P^a+2 を、任意の素数 P・正整数 a について完全排除した。
共通約数から整数商を取り出し、対数幅と合わせて i<2^192 を証明。
さらに底の素数を合同条件で有限化し、残る全2,903件の値が立方数でないことを
厳密整数計算と Lean カーネルで確認した。底3には別の短い全指数の証明がある。
v7 と合わせて i=3P^a+2 も P=3 を含む全ての素数について排除した。

同じ ell=1、j=i-3 の枝の一般の合成数では、i=wp^a+2、p>6w の指数を分類し、3|w のときは
a=2、i<961η²w³+2（η=1または2）へ還元した。
また A=C(i,3)、X=C(i²,6i−9)、S=A/gcd(A,X) とすると、
S|i−2、log i<128S、i<2^(192S) が必要であることを証明した。

i=jp³ の円分因子7q^aの枝では、4の倍数の指数を全排除し、
偶数指数の素数合同条件と、外側二項係数の正確な q-adic 付値を追加した。
全体の解の分類は未完了。解析・付値から有限領域への帰着は数学的証明であり、
全証明の Lean 形式化を主張していない。詳細は
[v8 日本語概要](PROGRESS_v8_ja.md) と [v8_manifest.json](v8_manifest.json) を参照。

## 2026年11月5日の追加：v7

ell=1、d=i-j に対して、d≥7 なら i<172d^36、d≥9 なら
さらに i<27d^35 を証明した。固定したオフセットごとの上限であり、
残りの有限範囲を全排除した主張ではない。

ell=1、j=i-3 では i-2 の最大素因数に P⁺(i-2)²≤6(i-2) が必要。
さらに i=3p^a+2、p≠3 の全素数・全指数を、正確な付値と
共通約数により40+16組へ還元し、完全な証明書で排除した。
i=P^a+2 の指数条件・立方剰余条件・Wieferich 因子の必要条件も追加した。

i=jp³ の円分因子7q^aについては全指数に合同条件を拡張し、
Thomas–Mignotte の既知の三次 Thue 方程式の定理へ帰着して
3の倍数の指数を排除した。詳細な仮定と外部定理への依存、
未形式化の範囲は [v7 日本語概要](PROGRESS_v7_ja.md) と
[v7_manifest.json](v7_manifest.json) に記録する。

## 2026年11月5日の追加：v6

ell=1、j=i-3、n=i、r=min(k,C(n,3)-k) の枝では、

\[
\frac n{\gcd(n,3)}\frac{n-1}{\gcd(n-1,6)}\mid r^3
\]

という新しい共通約数の条件を証明した。これにより n-1 が
平方自由な場合を全範囲で排除し、2・5の冪には特定の有限集合の
外にある Wieferich 素因数が必要だと示した。

また n≥1024 では

\[
3n<r<3n+\frac{3n}{4\log n}
\]

を証明。c₃(z)=∏p^ceil(v_p(z)/3)、R=n/c₃(n/gcd(n,3)) とすると
R≤12 の全範囲を理論的に有限化し、全2,180組・4,360式を排除した。
両隣の平方約数を使い、この枝で可能な第一添字 n≤X の個数が
O(X^(3/4)) 以下であることも証明した。

別の残存形 i=jp³、k=p、ell=1 では、p²+p+1 が3以外の
素因数を少なくとも二つ持つことが必要になった。
さらに p²+p+1=7q、q素数の場合は、合同式からの二次方程式と
実数評価を組み合わせ、証明された17候補をすべて排除した。

詳細な仮定・証明・残る範囲は [v6 日本語概要](PROGRESS_v6_ja.md)、
ファイルハッシュと検証範囲は [v6_manifest.json](v6_manifest.json) に記録する。

## 2026年11月5日の基準点：v5

ell=1、j=i-3、r=min(k,C(i,3)-k) について、
3i<r<10i/3 を証明した。その上で、
i/gcd(i,3) が平方因子を持たない場合、i=3^a、13^a、19^a、
および任意の素数 p に対する i=p^2,p^4 を排除した。

別の残存形 i=jp^3、k=p、ell=1 は、明示的な実関数の根の近傍へ
j を絞り、各素数 p につき高々一候補にした。さらに調和数の
法 p^5 の必要条件を導いた。この族の全排除はまだできていない。

ell>j の下側 k=ell+1=b の分岐でも、8j/3<=b<=4j を排除し、
隣接する 5j/2<=b<8j/3 では i=j+4 の形だけに絞った。
各主張の仮定・依存する前段階の証明は、それぞれのノートに明記している。

## 証明と検証の区別

1. 数学的証明：Markdown の各ノートに、無限範囲を含む議論を記す。
2. 有限証明書：まず理論的に有限範囲へ還元し、各候補を排除する
   素数・剰余等を生成する。独立した列挙・計算法で検証する。
3. Lean：実際に実行したソース・ログ・バージョンを記録する。
   明示的な仮定として残している解析評価まで形式化済みとはしない。
4. 実験・未完了の方向：必要条件と観察だけで、解なしの定理にしない。

過去の版の元ファイルは、その時点の記録として保存している。
後続の結果は新しい版名で追加し、訂正が必要になった場合は
旧主張と訂正理由を明示する。

## 再計算

v18の四生成器と四独立監査器はPython標準ライブラリだけで動く。cofactor生成器は先に生成したresidual報告と保存済みv17証明書を読む。

    python3 v18_residual_gap_checks.py
    python3 v18_residual_independent_audit.py
    python3 v18_short_lcm_checks.py
    python3 v18_short_lcm_independent_audit.py
    python3 v18_neighbor_cofactor_checks.py
    python3 v18_neighbor_cofactor_independent_review.py
    python3 v18_defect_resultants_checks.py
    python3 v18_defect_resultants_independent_audit.py

v17では平方根境界・補因子の全領域と、素因数例外表を理論で有限化し、別実装で再現した。主要コードはPython標準ライブラリだけで動く。

    python3 v17_square_root_gap.py
    python3 v17_square_root_gap_independent_audit.py
    python3 v17_quadratic_prime_powers_checks.py
    python3 v17_quadratic_independent_audit.py
    python3 v17_neighbor_defect_checks.py
    python3 v17_neighbor_defect_independent_audit.py

追加の記号展開監査 `python3 v17_symbolic_audit.py` だけはSymPyを使う。完全な整数点ソルバーではなく、5恒等式の係数照合である。

v16では、任意の固定δに対する有限帰着と、δ≤12の完全な証明書を追加した。
全証明書は省略なく [gzip形式](v16_square_defect_pell_results.json.gz) で保存。
下側評価・二次式の一般定理の補助検査と、理論的な全候補の検証を区別している。

    python3 v16_lower_gap_checks.py --limit 100000 --output reproduced_v16_lower_gap.json
    python3 v16_quadratic_neighbors_checks.py
    python3 v16_repeated_neighbor_primes_checks.py
    python3 v16_square_defect_pell.py --limit 12 --output reproduced_v16_square_defect.json --v15-certificate v15_pell_square_divisor_results.json
    python3 v16_square_defect_independent_audit.py --input reproduced_v16_square_defect.json --generator v16_square_defect_pell.py --v15 v15_pell_square_divisor_results.json --output reproduced_v16_pell_audit.json

v15 の再計算には Python 標準ライブラリだけを使用する。
Pellの計算は証明された全有限領域の排除、他の有限検査は一般証明の整合性確認。
詳細な範囲と元の必要条件は [v15の日本語説明](PROGRESS_v15_ja.md) を参照。

    python3 v15_cubic_defect_sparsity_checks.py --limit 100000 --output reproduced_sparsity_checks.json
    python3 v15_neighbor_prime_checks.py
    python3 v15_pell_square_divisor.py --output reproduced_pell.json
    python3 v15_pell_independent_audit.py --input reproduced_pell.json --generator v15_pell_square_divisor.py --output reproduced_pell_audit.json
    python3 v15_theory_constants.py --output reproduced_theory_audit.json

v14 の完全Thue計算は PARI/GP を使用する。保存済み全解からの係数・整除・区間の監査は Python 標準ライブラリだけで再実行できる。

    python3 v14_pair_support_verifier.py --adjacent v13_thue_support_results.json --odd-gap v14_gap2_results.json --output reproduced_v14_pairs.json
    python3 v14_independent_audit.py --gap1 v13_thue_support_results.json --gap2 v14_gap2_results.json --output reproduced_v14_audit.json

ソルバーの再実行と全ての前提は [v14の証明ノート](v14_two_factor_support.md) を参照。

このディレクトリを作業場所にする。代表的な検証は Python の
標準ライブラリだけで実行できる。

    python3 v11_simultaneous_square_interval_checks.py
    python3 v11_effective_defect_cf_checks.py verify
    python3 v11_effective_defect_cf_reproduction.py
    python3 v11_cofactor_extension_checks.py verify
    python3 v11_cofactor_extension_independent_reproduction.py
    python3 v11_local_square_filters_checks.py
    python3 v11_mixed_structure_checks.py

前の版：

    python3 v10_valuation_recovery_checks.py
    python3 v10_small_cofactors_checks.py verify
    python3 v10_small_cofactors_independent_reproduction.py
    python3 v10_cyclotomic_auxiliary_rings_checks.py

前の版：

    python3 v9_gcd_structure_checks.py
    python3 v9_cofactor_two_checks.py
    python3 v9_gcd_defect_cf_checks.py verify
    python3 v9_gcd_defect_cf_reproduction.py 12
    python3 v9_cyclotomic_primary_trace_checks.py

前の版：

    python3 v8_shifted_base_three_checks.py
    python3 v8_shifted_prime_power_completion_checks.py
    python3 v8_composite_shifted_completion_audit.py
    python3 v8_composite_dominant_prime_powers_checks.py
    python3 v8_cyclotomic_even_exponents_checks.py

前の版：

    python3 v7_fixed_offset_checks.py
    python3 v7_offset_cofactor_three_checks.py
    python3 v7_offset_shifted_prime_powers_checks.py
    python3 v7_large_prime_prime_power_extensions_checks.py

前の版：

    python3 v6_common_divisor_checks.py
    python3 v6_offset_composite_checks.py all
    python3 v6_offset_prime_powers_checks.py
    python3 v6_large_prime_cyclotomic_checks.py

前の版：

    python3 v5_offset_three_checks.py
    python3 v5_large_prime_localization_checks.py

v5 の有限証明書を再生成して独立検証する場合：

    python3 v5_l1_expanded_band.py generate
    python3 v5_l1_expanded_band.py verify
    python3 v5_l1_offset_four.py generate
    python3 v5_l1_offset_four.py verify

前段階の再計算方法は各証明ノート、スクリプトの説明、
v4_formal/README.md と v5_formal/README.md を参照。

## 大きい生成済み証明書

Git には証明、生成器、独立検証器、小さい結果記録を収録した。
v6〜v11 の有限証明書は全件含む。v9・v11の大きい連分数係数列とv11の余因子証明書は、
完全な内容を圧縮テキストと再検証器で収録している。v5 までの基準アーカイブにあった
100 KB を超える生成済み証明書やバイナリ出力の一部は収録していない。
省略した16ファイルの名前・サイズ・SHA-256、および基準アーカイブとの
対応は [ARCHIVE_MANIFEST.json](ARCHIVE_MANIFEST.json) にある。

完全な生成済み証明書を含む以前のアーカイブ：
[nested_binomial_progress_v2.zip](https://chatgpt.com/library?file_id=libfile_77d5da929dd481918744ac98b12a8e70&account_id=personal)。
リンク先の利用には所有者のアクセス権が必要。再生成器はこのディレクトリにある。
Lean の実行環境本体と mathlib の依存チェックアウトは Git に含めない。

## 現在残る主な課題

- v18の5/8・7/11下限、全素数冪の短いLCM条件、既約Jとδの共通因子制限、条件付きδ⁴高さを同時に満たす候補。固定a、ρ、Jごとの多項式高さは得たが、各パラメータ全域の上限は未証明。補分岐全体も未解決。
- v17ではr−3n>3√n、h≥93M、P⁺(n)<3√n、P⁺(n−1)²≤6n−9、(n²+2)/p≥65も必要。最大12二次式の反復素因数とLCMによる全指数制限を同時に満たす候補が残る。固定した残差パラメータごとの多項式高さは得たが、全パラメータへの上限は未証明。
- ell=1、j=i-3 で、実際の不足分H≥21、回復後のE≥21と平方値CRTの短い区間を全て通過する混合素因数。v13ではTに11以上の非立方指数の素数が必要。v14ではさらに、n,n−1,n−2 の異なる二因子にそのような素数が必要で、HTには異なる二素数以上が必要。
- v15では同じ枝にQ∤r²、κ≥2、log n<28κ、n²+2が合成数という条件も必要。大きな素因数での平方剰余条件と各素因数の上界も同時に満たす構造が残る。第一添字の個数はO(√X log X)だが、全体を有限個にした結果ではない。
- v16ではδ=Q/gcd(Q,r²)≥13、log n<28δ、gcd(δ,H)=1、δ³|A/Hも必要。r−3nの五分の三の下限、P⁺(n²−10)<r、各剰余に応じた他の二次式の条件、重複する大きな素因数の分岐制限も同時に課される。無制限δの場合は未解決。
- 同じ枝の各正確な素数冪qに対し、補因子w=(i−2)/qがw/gcd(w,192)≥14かつlog i/128より大きい未排除の値。
- i−3側の新しい三次高さ条件も通過する値。i=wp^a+3、w=1..4、p=2またはp≡3 mod4の族はv11で完了。
- i 自身が素数冪になる旧来の残存族とその Wieferich 条件。i=P^a+2 の族は v8 で完了。
- i=jp^3 で、p²+p+1 の未排除の因数構造と、実数評価・合同条件の両立。
- 下側 i=j+4 の残存区間、およびその他の未排除分岐。

これらはこの研究記録の未完了部分であり、既知の未解決問題であると
分類したという意味ではない。

## 追加のLean形式化と研究委任

v10で未形式化だった回復約数の積、正規化平方合同式、局所非平方条件、
CRTの一般部分、連分数の係数評価を追加し、三次曲線から楕円曲線への
有理座標変換も形式検証した。

- [追加形式化と実行記録](v10_formal/ADDITIONAL_FORMALIZATION.md)
- [幾何学的還元と残る計算](GEOMETRIC_APPROACH.md)
- [DeepSeekへ共有した公開研究リポジトリ](AI_RESEARCH_REFERENCES.md)
- [研究状態と引継ぎ](DEEPSEEK_STATE.md)
- [再利用する委任スキル](../../../.agents/skills/deepseek-math-research/SKILL.md)

元の四変数方程式全体の解決や、全連分数証明書のLean検証が
完了したという主張ではない。以前の版のログ・manifestは当時の記録として保持する。


