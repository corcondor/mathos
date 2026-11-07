# v9：余因子2の全2,592件を Lean カーネルで検証

`CubeCertificates.lean` は、\(\ell=1,\ j=i-3,\ i=2P^a+2\) の
完全排除で最後に残る2,592個の整数が、すべて隣り合う二つの立方数の
間にあることを検証する。名前空間は `NestedBinomialV9`。

各記録は底 P、指数 a、整数商 t、下側の整数立方根 m を持つ。
この版で確認する値は

\[
V=\frac{t(2P^a+2)(2P^a+1)}3
\]

であり、v8 の値の定義から係数と分母を変更している。
Lean で直接確認した内容は

    3 ∣ (2*P^a+2)(2*P^a+1)
    m^3 < t(2*P^a+2)(2*P^a+1)/3 < (m+1)^3

である。50件ごとの52バッチを `by decide` で証明し、結合した
リストの長さが2592であることと、全記録の値が立方数でないことを証明した。
高さ評価の有理数定数と、整数が162と163の間に入れないことも確認した。

## 実際に実行した範囲

- `allRows_checked`：全2592記録の正確な整除・不等式。
- `allRows_count`：記録数が2592。
- `every_recorded_value_not_cube`：全記録の値が立方数でないこと。
- `numerical_gap_constant`：高さ評価に使う厳密な有理数比較。
- `quotient_interval_has_no_integer`：整数商による矛盾の算術部分。

Lean 4.35.0、mathlib コミット
`56a005855ea17e0b0958f73ec801ae140b0a1679` で実際に実行し、
**終了コード0**を確認した。実行済みソースの SHA-256 は

    59325b7757f9b4cd85ac6173c4ff74c370f44070dfac81664a86b12b83f436fb

である。`allRows_checked` の公理依存は `propext` のみ、
`allRows_count` は公理依存なし。最終の非立方数定理は `propext` と
`Quot.sound` を使う。これは実際の `#print axioms` の出力で確認した。
ログを `kernel_check.log` に、環境・コマンド・終了コード・ハッシュを
`kernel_check.json` に保存した。

`sorry`、独自公理、`native_decide` は使っていない。

## 形式化していない部分

元の方程式からこの有限領域へ帰着させる、解析的な区間評価、正確な
素数付値の分類、底2・底3と小指数の排除、整数商の導出、素数と指数の
領域の完全性は、この Lean ファイルでは形式化していない。
各記録のパラメータは自然数として扱い、底の素数性そのものを Lean
で認証するファイルでもない。

これらの前段は `../v9_cofactor_two.md` の数学的証明、担当外AIによる
独立監査、Pythonによる領域再構成と整数計算で確認している。
その監査は外部研究者の査読ではない。

従って、ここで形式検証済みなのは、**理論的に導いた全2,592件の
有限算術と、明示した共通補題**である。余因子2の無限族の定理全体や、
元の四変数方程式全体を Lean で解決済みとは主張しない。

## JSONとの一致と再生成

`generate_certificate_source.py` は親ディレクトリの凍結した
`v9_cofactor_two_certificates.json` を読み、次の SHA-256 を照合する。

    03e778865211a34c8f3a0caa42368839f9f0fdee97b595f4f04627a4ed59175d

その後、一般補題の断片 `CubeCertificateLemmas.txt` と全2592記録を
結合して Lean ソースを生成する。

    python3 generate_certificate_source.py

生成された Lean ソースの全2592組を正規表現で別途読み取り、JSONと
順序も含めて完全に一致することを照合した。52バッチの存在、禁止した
未証明の仮定や評価手段を使っていないことも点検した。
照合結果と両ファイルのハッシュは `source_mapping_check.json` にある。

## 再現方法と実行環境

標準の elan 環境では、このディレクトリの固定バージョン設定で依存を用意し、

    lake update
    lake exe cache get
    lake env lean CubeCertificates.lean

と実行できる。独立プロジェクトとしての `lake build` 自体を今回
実行したという意味ではない。

今回成功した方法は、既存の指定コミットの mathlib ディレクトリから

    lake env lean --root=/absolute/path/v9_formal -o /absolute/path/v9_formal/CubeCertificates.olean /absolute/path/v9_formal/CubeCertificates.lean

と直接呼ぶ方法である。実際には Lean 4.35.0 の bin ディレクトリを
PATH の先頭に指定し、この実行環境専用の `own_executable_path.so` を
LD_PRELOAD に指定した。具体的な絶対パスは `kernel_check.json` にある。
互換処理の内容とソースは `../v4_formal/README.md` を参照。
自プロセスの実行ファイル位置を解決する処理であり、Lean のカーネル・
推論規則・数学ライブラリを変更するものではない。

この環境では最初に標準出力をファイルへリダイレクトした起動が Lake
のインストール位置検出で失敗したため、既に成功実績のある直接起動に
戻した。成功した実行の出力を取得し、そのままログに保存している。

配布するのはソース、設定、生成器、照合結果、実行ログである。
Leanランタイム、mathlibチェックアウト、生成された `.olean` は配布に含めない。
