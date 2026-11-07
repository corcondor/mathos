# Lean で実際に検証した範囲

このフォルダの `Divisibility.lean` は、元の方程式

\[
\binom{\binom ij}{\binom{k}{\ell}}=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}
\]

を `Equation` として定義し、次の必要条件を証明する。

1. `original_other_term_divisibility`: \(q=i/\gcd(i,j)\), \(r=\min(B,A-B)\) とおくと、\(q\mid r\binom{k^2}{\ell^2}\)。
2. `original_ell_one_cube_divisibility`: \(\ell=1\) では \(q\mid r^3\)。
3. `valuation_cubic_cap`: Z3 で調べた付値の必要条件から \(c\le3\rho\) が従う。

1 と 2 は元の方程式、\(i>0\)、外側の下の数が上の数以下であることから直接従う形式化である。有限探索の結果や解析的な上限を仮定しない。ファイルは `sorry`、独自の公理、`native_decide` を使用しない。`#print axioms` の実際の出力を `kernel_check.log` に記録した。そこで使われる `propext`, `Classical.choice`, `Quot.sound` は Lean/mathlib の標準の公理である。

**元の四変数方程式全体の解決を形式化したものではない。** 別資料の不等式、\(r<2j\) の上限、Pell 方程式による列挙、合同式の有限証明書の網羅性は、この Lean ファイルでは証明していない。それぞれの検証範囲を混同しないこと。

## 実行済みの環境

- Lean 4.35.0、コミット `eb6cafb7290e8bd5f2937522d8d804f58f02bafc`。
- mathlib4、コミット `56a005855ea17e0b0958f73ec801ae140b0a1679`。
- `lake env lean --root=... -o .../Divisibility.olean .../Divisibility.lean` を、上記 mathlib のチェックアウトで実行した。終了コードは 0。
- 実行日時、ソースの SHA256、実際のコマンドを `kernel_check.json` に記録した。

ここで用いた AI の作業は、証明を生成し、Lean のエラーを読み、証明を修正して再実行するループである。AlphaProof、LeanCopilot、その他の学習済み数学モデルをこの実行で動かしたという意味ではない。

## 再現方法

Lean の標準の `elan` 環境があれば、このフォルダで次を実行できるよう `lean-toolchain` と `lakefile.toml` を同梱した。

```sh
lake update
lake exe cache get
lake build
lake env lean Divisibility.lean
```

この独立プロジェクト用の `lake build` そのものは今回の実行方法ではない。実際に成功した方法をそのまま再現するには、指定コミットの mathlib をチェックアウトし、必要なキャッシュを取得した上で、そのディレクトリから次の形で実行する。

```sh
lake exe cache get Mathlib/Tactic.lean
lake env lean --root=/absolute/path/v4_formal /absolute/path/v4_formal/Divisibility.lean
```

## この実行環境だけの補助

今回の Linux 実行環境では `/proc/<自プロセスのPID>/exe` が見つからず、同じ対象を指す `/proc/self/exe` は利用できた。Lean の実行ファイル位置の取得を可能にするため、前者の `readlink` が ENOENT になった場合に限って後者へ読み替える `own_executable_path.c` を使用した。

これは自プロセスの実行ファイル位置を取得するためだけの互換処理で、Lean のバイナリ、証明カーネル、定理、ライブラリ、証明規則を変更していない。通常の Linux 環境では不要である。必要な場合だけ次のようにコンパイルし、Lean/Lake 実行時の `LD_PRELOAD` に設定する。

```sh
cc -shared -fPIC -O2 own_executable_path.c -o own_executable_path.so -ldl
LD_PRELOAD=/absolute/path/own_executable_path.so lake env lean Divisibility.lean
```

配布物には巨大な Lean ランタイム、取得済み mathlib、`.olean` は含めていない。必要なソースとバージョン指定、実行記録を含めている。
