# MathOS PDCA Snapshot

Date: 2026-06-26

## Benchmark

Fixed 1000 public problems:

- GSM8K: 300
- MATH: 210
- SVAMP: 150
- ASDiv: 150
- AQuA-RAT: 50
- MultiArith: 70
- MAWPS: 70

Comparable: 942

## Before / After

| metric | baseline | after case-frame layer |
|---|---:|---:|
| correct | 272 | 299 |
| wrong | 202 | 175 |
| abstain | 526 | 526 |
| exact_rate | 28.87% | 31.74% |
| precision | 57.38% | 63.08% |

Transitions:

- wrong -> correct: 27
- correct -> wrong: 0
- abstain -> abstain: 526

## Change

Added a case-frame arithmetic layer and a Japanese particle/case-frame parser.

The new layer compiles relations such as:

- fixed cost + yearly net income -> break-even inequality
- average speed target -> remaining distance / remaining time
- ratio + total -> part value
- total bill - known items -> unknown count
- percentage fee + fixed fees -> final total
- particles like が/を/に/から/まで -> typed slots

This is still far from general mathematical reasoning.  The main remaining errors are over-firing in `quantity_reasoning` and weak symbolic/CAS handling for MATH.  Next target is to replace ad hoc quantity candidates with a stricter typed state/equation solver.

## X Draft

MathOS PDCA snapshot:

Fixed 1000 public benchmark problems.

Baseline:
272 correct / 202 wrong / 526 abstain
exact 28.87%, precision 57.38%

After adding a case-frame arithmetic layer + Japanese particle parser:
299 correct / 175 wrong / 526 abstain
exact 31.74%, precision 63.08%

27 wrong->correct, 0 correct->wrong.

The improvement came from compiling relations like fixed cost + yearly net income, average speed, ratio+total, total bill - known items, package price, and percentage fees into explicit equations.

Still not solved:
`quantity_reasoning` still over-fires, and MATH/CAS coverage is weak.

Next: replace loose quantity candidates with a stricter typed state/equation solver.
