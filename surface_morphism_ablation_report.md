# Surface Morphism Ablation

## 目的

Problem Phase Diagram Synthesis で得た解法部品を、表層文型から直接答える solver として混ぜないため、通常経路と表層射アブレーションを分離した。

## 実装上の分離

- cold path: `detect_allfield_curriculum_patterns` を呼ばない。
- ablation path: `allow_specialized=True` または `--allow-surface-morphisms` のときだけ `detect_allfield_curriculum_patterns` を呼ぶ。
- kernel path: 数列、距離、中点、合同、基数表記、割合、時計角を `SemanticObject / SemanticMorphism / Constraint / SemanticQuery` として記録する。

## 小ベンチ結果

同一条件:

```powershell
python -B math_os_prototype\public_benchmark.py --math-per-config 5 --case-timeout 8 --output math_os_prototype\hard_public_math35_cold_graph_path.json
python -B math_os_prototype\public_benchmark.py --math-per-config 5 --case-timeout 8 --allow-surface-morphisms --output math_os_prototype\hard_public_math35_surface_morphism_ablation.json
```

| mode | total | comparable | answered | exact |
|---|---:|---:|---:|---:|
| cold graph path | 35 | 22 | 18 | 8 |
| surface morphism ablation | 35 | 22 | 30 | 20 |

## 解釈

追加正答は主に `arithmetic_nl_allfield_*` 由来なので、これは MathOS 核の汎化改善ではなく、表層射アブレーションの効果として扱う。次のPDCAでは、この差分を直接 solver ではなく、核の対象・射・制約・query と backend の一般射に移植する。

## 回帰テスト

```powershell
python -B -m unittest math_os_prototype.test_math_os math_os_prototype.test_problem_phase_synthesis math_os_prototype.test_term_synthesis
```

結果: 104 tests OK.
