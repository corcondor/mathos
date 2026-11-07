# 今回の Lean 検証範囲

`OffsetThree.lean` は前回の `v4_formal/Divisibility.lean` の定義・証明を
含め、今回の二つの整数論的推論を追加した自己完結したソースです。
前回のファイルは変更していません。

## 実際にカーネルで検証した内容

1. 元の式からの約数条件
   `i / gcd(i,j) ∣ min(k, C(i,j)-k)^3`（ell=1、両分岐）。
2. `q` が平方因子を持たず、`i=g*q`、`g<=3`、`q ∣ r^3`、
   `3*i<r`、`3*r<10*i` なら矛盾するという整数論の補題。
3. 2を `i=j+3` と元の二項係数方程式へ直接適用した定理。
4. 任意の自然数の三乗は、法9で4または5にならないという補題。

**区間評価 `3*i<r<10*i/3` は、2・3では明示的な仮定です。**
区間評価を元の式から導く解析的証明、素数冪ごとの付値計算、
3の冪の場合に正規化した式から法9の条件を導く積の計算は、
今回の Lean ファイルには形式化していません。
従って、このファイル単体で `i=3^a` 全体の排除や元の四変数方程式の
解なしを証明した、と主張するものではありません。

## 実行結果

- Lean 4.35.0、コミット `eb6cafb7290e8bd5f2937522d8d804f58f02bafc`。
- mathlib コミット `56a005855ea17e0b0958f73ec801ae140b0a1679`。
- 上記 mathlib のチェックアウトで `lake env lean` を実際に実行し、
  終了コード0。実行記録は `kernel_check.json` と `kernel_check.log`。
- `sorry`、独自公理、`native_decide` は使用していません。
- `#print axioms` の出力は標準の `propext`、`Classical.choice`、
  `Quot.sound` の範囲です。法9の補題は `propext` のみです。

## 再実行

標準の `elan` 環境では、同梱の `lean-toolchain` と `lakefile.toml` を
使って、このフォルダで次を実行できます。

```bash
lake update
lake exe cache get
lake build
lake env lean OffsetThree.lean
```

今回実際に成功した方法は、既存の指定コミットの mathlib の
ディレクトリから次の形式で実行する方法です。

```bash
lake env lean --root=/absolute/path/v5_formal /absolute/path/v5_formal/OffsetThree.lean
```

この実行環境に限った自己実行ファイルパス取得の互換処理については、
`../v4_formal/README.md` と `../v4_formal/own_executable_path.c` に
説明・ソースがあります。Lean のカーネルや推論規則を変える処理では
ありません。通常の環境では不要です。標準出力の記録は成功した直接
実行の返却値を保存しています。シェルで出力をリダイレクトした
別試行は Lake のインストール設定検出で失敗したため採用していません。

独立したこのフォルダでの `lake build` 自体は今回の実行方法ではありません。
