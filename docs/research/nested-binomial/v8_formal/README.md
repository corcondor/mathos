# v8：2,903件の有限算術証明書を Lean カーネルで検証

`CubeCertificates.lean` は、シフト素数冪の完全排除で最後に残る
2,903個の整数が、すべて隣り合う二つの立方数の間にあることを検証する。

各記録は素数の底 P、指数 a、整数商 t、下側の整数立方根 m を持つ。
Lean で直接確認した内容は

    6 ∣ (P^a+2)(P^a+1)
    m^3 < t(P^a+2)(P^a+1)/6 < (m+1)^3

である。50件ごとの59バッチを `by decide` で証明し、結合したリストの
長さが2903であることと、記録された全値が立方数でないことも証明した。
有理数の高さ評価の定数、および整数が162と163の間に入れないことも確認した。

## 今回実行した範囲

- `allRows_checked`：全2903記録の正確な整除・不等式。
- `allRows_count`：記録数が2903。
- `every_recorded_value_not_cube`：全記録について立方数でないこと。
- `numerical_gap_constant`：高さ評価の厳密な有理数定数。
- `quotient_interval_has_no_integer`：整数商による矛盾の算術部分。

実際に Lean 4.35.0、mathlib コミット
`56a005855ea17e0b0958f73ec801ae140b0a1679` で実行し、終了コード0。
`allRows_checked` の公理依存は `propext` のみ、
`allRows_count` は公理依存なし。最終の非立方数定理は
`propext` と `Quot.sound` を使う。ログを同梱する。

`sorry`、独自公理、`native_decide` は使っていない。

## まだ形式化していない部分

元の二項係数方程式からこの有限領域へ帰着させる、解析的な区間評価、
正確な素数付値の分類、整数商の導出、素数と指数の範囲の完全性は、
この Lean ファイルでは形式化していない。これらは証明ノートと
独立した数学監査、Pythonによる領域再構成で確認している。

従って「元の問題全体が Lean で解決済み」や
「シフト素数冪定理の全証明が Lean 形式化済み」とは主張しない。

## 再現方法

`generate_certificate_source.py` は親ディレクトリの凍結したJSON証明書を
読み、SHA-256を照合してから全記録をLeanソースへ変換する。
一般補題のソース断片は `CubeCertificateLemmas.txt` にある。

    python3 generate_certificate_source.py

標準の elan 環境では、同梱の設定で指定コミットの mathlib を用意し、

    lake update
    lake exe cache get
    lake env lean CubeCertificates.lean

と実行できる。この独立ディレクトリでの `lake build` 自体を今回
実行したという意味ではない。今回成功したコマンドは、既存の
指定コミットの mathlib ディレクトリから

    lake env lean --root=/absolute/path/v8_formal -o /absolute/path/v8_formal/CubeCertificates.olean /absolute/path/v8_formal/CubeCertificates.lean

で呼ぶ方法である。実際の絶対パス、ソースと証明書のハッシュ、
実行セッションは `kernel_check.json` に記録する。
この実行環境でのみ必要だった自己実行ファイルパスの互換処理は
`../v4_formal/README.md` を参照。Lean のカーネルや推論規則の変更ではない。
