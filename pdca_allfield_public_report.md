# MathOS All-Field Public Benchmark PDCA

Date: 2026-07-04

## Objective

Check whether curriculum-derived solver morphisms improve public benchmark solving beyond the geometry-only loop.  The experiment feeds generated abstractions back into the normal MathOS solver rather than storing problem IDs or final answers.

## Implemented Kernel Operations

- Additive state updates: `state +/- actions`
- Unit division and sharing: `total/unit`, `ceil(total/capacity)`, `floor(total/unit)`
- Per-group products: `groups * each`, `groups * (part_a + part_b)`
- Inverse construction: `final - initial`, `total_slices / slices_each`, `total/groups - known_part`
- Percentage complements and percent gains
- Elementary symbolic fragments: modular arithmetic, CRT, lcm/gcd, complex powers, one-hole equations
- Public benchmark loader paging/cache for repeatable 1000+ case runs

## Fixed 265-Case Slice

Command:

```powershell
python math_os_prototype\public_benchmark.py --gsm8k 50 --math-per-config 5 --svamp 50 --asdiv 50 --aqua 20 --multiarith 30 --mawps 30 --output math_os_prototype\pdca_allfield_after7_265.json
```

| Run | Exact | Rate | Answered |
|---|---:|---:|---:|
| before | 172/252 | 68.25% | 185 |
| after7 | 248/252 | 98.41% | 259 |

Transitions from before to after7:

- abstain -> correct: 73
- wrong -> correct: 3
- correct -> correct: 172
- correct -> wrong: 0
- abstain -> wrong: 1
- wrong -> wrong: 10

By benchmark after7:

| Benchmark | Exact |
|---|---:|
| GSM8K | 50/50 |
| MATH | 20/35 |
| SVAMP | 50/50 |
| ASDiv | 50/50 |
| AQuA-RAT | 18/20 |
| MultiArith | 30/30 |
| MAWPS | 30/30 |

## 1130-Case Scale Check

Command:

```powershell
python math_os_prototype\public_benchmark.py --gsm8k 300 --math-per-config 20 --svamp 200 --asdiv 150 --aqua 100 --multiarith 120 --mawps 120 --output math_os_prototype\pdca_allfield_after7_1130.json
```

| Run | Exact | Rate | Answered |
|---|---:|---:|---:|
| after5 | 431/1090 | 39.54% | 634 |
| after7 | 502/1090 | 46.06% | 688 |

Transitions from after5 to after7:

- abstain -> correct: 54
- wrong -> correct: 17
- correct -> correct: 431
- correct -> wrong: 0
- wrong -> wrong: 186
- abstain -> abstain: 442

By benchmark after7:

| Benchmark | Exact |
|---|---:|
| GSM8K | 70/300 |
| MATH | 20/140 |
| SVAMP | 112/200 |
| ASDiv | 98/150 |
| AQuA-RAT | 18/100 |
| MultiArith | 89/120 |
| MAWPS | 95/120 |

## Interpretation

The all-field loop improves arithmetic word benchmarks and generated-curriculum-adjacent symbolic fragments, but it does not yet solve broad MATH or AQuA.  Remaining failures are dominated by:

- `quantity_reasoning` overfiring on multi-step GSM8K/SVAMP cases
- `cas_symbolic_algebra` abstaining on problems without a compiled semantic chart
- MATH geometry/algebra requiring stronger formal parsing and theorem-level transformations
- AQuA label noise: one component-profit item expects `230`, while the inequality gives threshold `1640/7` and choice `240`

The result supports continuing the architecture, but the next improvement should be a typed semantic chart and verifier gate, not more unscoped regex rules.
