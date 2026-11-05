# v6 の Lean 検証範囲

CommonDivisor.lean は v4 の定義・証明を含む独立したファイル。
今回追加した定理は次の二つ。

- 元の ell=1 の方程式から、
  gcd(C(i,j),C(i^2,j^2)) が min(k,C(i,j)-k)^3 を割ること。
- C(i,j) と C(i^2,j^2) の二つの互いに素な共通約数は、
  その積も上の三乗を割ること。

これらは解析的な区間や素因数分解を仮定しない。
一方、i-1 から新しい共通約数を取り出す choose-pair の計算、
i-1 が平方自由な場合の完全排除、対数幅の評価、疎性評価、
Wieferich 条件、円分因子を使う別の枝の排除は未形式化。
その全体が Lean で解決済みだとは主張しない。

Lean 4.35.0、コミット eb6cafb7290e8bd5f2937522d8d804f58f02bafc、
mathlib コミット56a005855ea17e0b0958f73ec801ae140b0a1679で実行し、
終了コード0を確認。ソースのハッシュと実行ログを同梱する。
sorry、独自公理、native_decide は使用していない。
公理依存は標準の propext、Classical.choice、Quot.sound の範囲。

標準の elan 環境では同梱の設定を使う。

    lake update
    lake exe cache get
    lake build
    lake env lean CommonDivisor.lean

今回実際に成功した実行方法は、既存の指定コミットの mathlib の
ディレクトリから次の形で呼び出す方法。

    lake env lean --root=/absolute/path/v6_formal /absolute/path/v6_formal/CommonDivisor.lean

この実行環境だけに必要な自己実行ファイルパスの互換処理は
../v4_formal/README.md と own_executable_path.c に説明がある。
Lean のバイナリ、カーネル、定理、推論規則を変更する処理ではない。
独立したこのフォルダでの lake build 自体は今回の実行方法ではない。
