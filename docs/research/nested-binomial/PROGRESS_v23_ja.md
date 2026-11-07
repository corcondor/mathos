# v23：三乗核への整除降下と、残差下限ρ≥32770

2026-11-07 JST。前回 v21 `6074b2018ab1d147d3c27a1c20cc93cd065d2915` で得た残差高さを継承。v22 で提案した \(\delta^3\mid4Q\)・二項三次Thue方程式への降下を、素数2・3を含めて証明し直した。対象は引き続き \(\ell=1,j=i-3\)。

## 主結論

- \(n=d_+x^3,n-1=d_-y^3\) と三乗核を取ると、**\(xy\mid r\)、\(\delta\mid2xy\)**。証明は \(81an(n-1)=b\{9n(t^2+3t+3)+t^3\}\) の素数冪付値を、\(n\) と \(n-1\) で別々に評価する。例外素数 2 と 3 を全指数について処理する。
- \(\delta^3\mid4Q\) を独立に導出し、v21 の \(n\) の高さを用いて **\(\delta<2^{17}\rho^{1/3}(\log\rho)^{5/3}\)**。従来の \(O(\rho^2(\log\rho)^2)\) より強い。
- 三乗核係数は \(d_+\mid\mathrm{rad}(6(3a+b))^2\)、\(d_-\mid\mathrm{rad}(6(3a-b))^2\)。固定(a,b)における二項三次Thue係数を絞る。Bennettの既知の一意性定理を利用できるが、未だ一様(a,b)上限はない。
- **4097≤ρ≤32768 を完全有限監査で排除。** 高さによる935,154,540候補→平方129→復元枝8→δ≥25の5組→元式の両k分岐を小素数で排除。これまでのρ≥4099から **ρ≥32770** へ。両実装は異なる順序・異なる六次式で全件数・候補集合が一致。

## 再現

```bash
c++ -std=c++17 -O3 v23_residual_extension.cpp -o producer
c++ -std=c++17 -O3 v23_independent_checker.cpp -o verifier
./producer 4097 8192 > v23_residual_extension_4097_8192.log
./producer 8193 16384 > v23_residual_extension_8193_16384.log
./producer 16385 24576 > v23_residual_extension_16385_24576.log
./producer 24577 32768 > v23_residual_extension_24577_32768.log
./verifier 4097 32768 > v23_independent_4097_32768.log
python3 v23_validate_certificate.py
```

`v23_proofs_ja.md` に全素数付値・Thue降下・有限監査・限界を記載。`v23_certificate.json` に8補助点と合同式証拠を収録。

**未解決：** ρの一様上界、Thue係数(a,b)の全域制御、全枝の除去、元の四変数問題。今回は有限の整数演算と記述証明の検証であり、Lean形式化や外部査読は未実施。