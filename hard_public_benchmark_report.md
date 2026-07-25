# Hard Public Benchmark Snapshot

Date: 2026-07-04

## Scope

This run focuses on harder public benchmarks rather than the fixed 265-case slice.

- MATH: first 50 cases from each of 7 subsets, 350 total, with `--case-timeout 8`
- AQuA-RAT: 254 test cases

The full MATH 700 run still needs a resumable writer.  It timed out at the process level before writing a complete output file.

## Commands

```powershell
python math_os_prototype\public_benchmark.py --math-per-config 50 --case-timeout 8 --output math_os_prototype\hard_public_math_350_after_morphisms.json
python math_os_prototype\public_benchmark.py --aqua 254 --output math_os_prototype\hard_public_aqua_254.json
```

## Results

| Benchmark | Run | Exact | Comparable Rate | Answered |
|---|---|---:|---:|---:|
| MATH 350 | before extra morphisms | 20/252 | 7.94% | 74/350 |
| MATH 350 | after extra morphisms | 36/252 | 14.29% | 91/350 |
| AQuA-RAT 254 | current | 18/254 | 7.09% | 21/254 |

MATH 350 transitions after adding general morphisms:

- abstain -> correct: 16
- correct -> correct: 20
- correct -> wrong: 0
- abstain -> wrong: 1
- wrong -> wrong: 54
- abstain -> abstain: 259

Improved MATH areas:

- Algebra: arithmetic sequences, compound interest, pairwise-sum reconstruction, quadratic interval, coordinate distance, midpoint
- Number theory: base equations, modular products, modular powers, periodic wait, digit divisibility
- Prealgebra: arithmetic precedence, tip percentage, clock angle

## Interpretation

The harder public benchmarks are not solved yet.  The MATH 350 score doubled in relative terms, but remains low.  The main bottleneck is not CAS arithmetic; it is semantic compilation into the right typed chart.  Remaining failures are dominated by:

- `latex_to_cas_symbolic_algebra` abstaining because no semantic chart was compiled
- `quantity_reasoning` overfiring on problems that need theorem-level or multi-object constraints
- Geometry problems with diagrams or hidden incidence structure
- Combinatorics/probability requiring counting models rather than simple arithmetic

Next engineering target: resumable hard-benchmark runner plus stronger `TypedSemanticGraph -> backend` lifts for algebraic inequalities, combinatorics, coordinate geometry, and diagram-free geometry.
