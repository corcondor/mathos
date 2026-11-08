# v81：残差100003の最後の2繊維についてMordell–Weil階数1を完全認証

2026-11-08。対象は主枝の第一楕円商
\[
E_{b,\rho}:\quad Y^2+6bXY+b(8b^2+9\rho)Y=X^3,\qquad \rho=100003,\quad b=9,18.
\]

## 定理：両曲線の代数的階数は1

\[
\boxed{\operatorname{rank}E_{9,100003}(\mathbb Q)
=\operatorname{rank}E_{18,100003}(\mathbb Q)=1.}
\]

**証明**：SageMath 10.10 の導関数級数メソッド deriv_at1(k,prec=128) は、L(E,1)=0 の場合、L'(E,1)の数値と**数学的に保証された打切り誤差上界**を返す。[Sage公式仕様](https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/lseries_ell.html)。両曲線は関数等式の符号 -1 でL(E,1)=0。次の結果を得た：

| b | 導手 N | k項 | L'(E,1)計算値 | 絶対誤差上界 |
|--:|--:|--:|--:|--:|
| 9 | 486379090935 | 1496754 | 30.91601443548650724166 | 0.309019 |
| 18 | 9748577648556 | 7615742 | 21.95230362152261846200 | 0.219501 |

いずれも値の絶対値が誤差上界を大きく上回るので、L'(E,1)は厳密に非零。解析的階数は正確に1。楕円曲線のモジュラー性とGross–Zagier–Kolyvaginの定理から、代数的Mordell–Weil階数が1となる。\(\square\)

[実際の証明計算のGitHub Actionsログ](https://github.com/corcondor/mathos/actions/runs/42480661353)。BSD予想や未証明のShafarevich–Tate群有限性は仮定しない。

## まだ全整数点・自由生成元は認証していない

代数的階数1の認証は自由部分の飽和済み生成元の提示を意味しない。
- [v82直接点探索](v82_analytic_rank_one_integral_points.sage)：最小モデルで高さ12まで非捩れ生成元が見つからなかった。[失敗ログ](https://github.com/corcondor/mathos/actions/runs/42490161140)。
- [v84双対3-isogenyを使った点探索](v84_three_isogeny_free_point.sage)：核(0,0)の有理3-isogenyは構築できたが、探索した高さ12以内に非捩れ点が見つからず全整数点計算に進めなかった。[失敗ログ](https://github.com/corcondor/mathos/actions/runs/42490752140)。
- [v79〜v83の固定残差の立方核降下](V83_LOCAL_CUBIC_COVER_SIEVE_ja.md) はMW自由生成元に依存せず、必要な係数型を**21種類**に縮約した。しかし、その21本の三次曲線の整数点自体は未分類。

**結論**：残る2曲線の階数は両方とも1と証明済み。自由生成元・飽和・元モデルの全整数点は未認証。原の二項係数方程式全体は未解決。
