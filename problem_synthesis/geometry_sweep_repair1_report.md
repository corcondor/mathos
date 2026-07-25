# Geometry Sweep Repair Loop Report

Generated: 2026-07-03T16:37:22.495129+00:00

## Summary

- Attempted: 37
- Successful: 37
- Success rate: 1.0
- Mean score delta: 36.541
- Max score delta: 82.0

Transitions:
- closed_region -> closed_region: 17
- partial_region -> closed_region: 15
- closed_envelope -> closed_envelope: 5

## Top Repaired Candidates

### 1. geosweep-0037-gr1 score=92.0

- task: region
- dsl: `task region; family y = t*x - 2*t**2 + 1; param t in R`
- answer: `y <= (x**2 + 8)/8`
- normal form: `x**2 - 8*y + 8 >= 0`

```tex
実数$t$に対して，曲線
\[
y=tx - 2t^2 + 1
\]
が定まる。この曲線族の通過領域を求めよ。
```

### 2. geosweep-0073-gr1 score=92.0

- task: region
- dsl: `task region; family y = t*x + 2*t**2 + 1; param t in R`
- answer: `y >= -(x**2 - 8)/8`
- normal form: `x**2 + 8*y - 8 >= 0`

```tex
実数$t$に対して，曲線
\[
y=tx + 2t^2 + 1
\]
が定まる。この曲線族の通過領域を求めよ。
```

### 3. geosweep-0005-gr1 score=91.0

- task: region
- dsl: `task region; family y = t*x - 2*t**2 - 2; param t in R`
- answer: `y <= (x - 4)*(x + 4)/8`
- normal form: `x**2 - 8*y - 16 >= 0`

```tex
実数$t$に対して，曲線
\[
y=tx - 2t^2 - 2
\]
が定まる。この曲線族の通過領域を求めよ。
```

### 4. geosweep-0009-gr1 score=91.0

- task: region
- dsl: `task region; family y = t*x - 2*t**2 + x + 1; param t in R`
- answer: `y <= (x**2 + 8*x + 8)/8`
- normal form: `x**2 + 8*x - 8*y + 8 >= 0`

```tex
実数$t$に対して，曲線
\[
y=tx - 2t^2 + x + 1
\]
が定まる。この曲線族の通過領域を求めよ。
```

### 5. geosweep-0002-gr1 score=86.0

- task: envelope
- dsl: `task envelope; family y = t*x - t**2 + 1; param t in R`
- answer: `-x**2 + 4*y - 4 = 0`
- normal form: `x**2 - 4*y + 4 = 0`

```tex
実数$t$に対して，曲線
\[
y=tx - t^2 + 1
\]
が定まる。この曲線族の包絡線を求めよ。
```

### 6. geosweep-0056-gr1 score=86.0

- task: envelope
- dsl: `task envelope; family y = t*x + t**2 + 1; param t in R`
- answer: `x**2 + 4*y - 4 = 0`
- normal form: `x**2 + 4*y - 4 = 0`

```tex
実数$t$に対して，曲線
\[
y=tx + t^2 + 1
\]
が定まる。この曲線族の包絡線を求めよ。
```

### 7. geosweep-0015-gr1 score=91.0

- task: region
- dsl: `task region; family y = t*x - 2*t**2 - x + 1; param t in R`
- answer: `y <= (x**2 - 8*x + 8)/8`
- normal form: `x**2 - 8*x - 8*y + 8 >= 0`

```tex
実数$t$に対して，曲線
\[
y=tx - 2t^2 - x + 1
\]
が定まる。この曲線族の通過領域を求めよ。
```

### 8. geosweep-0059-gr1 score=91.0

- task: region
- dsl: `task region; family y = t*x + 2*t**2 - 2; param t in R`
- answer: `y >= -(x**2 + 16)/8`
- normal form: `x**2 + 8*y + 16 >= 0`

```tex
実数$t$に対して，曲線
\[
y=tx + 2t^2 - 2
\]
が定まる。この曲線族の通過領域を求めよ。
```

## Repair Traces

- geosweep-0001: closed_region(75.0) -> closed_region(84.0) success=True
  - step 1 add_affine_shift patch={'d': 1}: closed_region -> closed_region, score 75.0 -> 84.0
- geosweep-0002: closed_envelope(77.0) -> closed_envelope(86.0) success=True
  - step 1 add_affine_shift patch={'d': 1}: closed_envelope -> closed_envelope, score 77.0 -> 86.0
- geosweep-0005: closed_region(83.0) -> closed_region(91.0) success=True
  - step 1 increase_elimination_texture patch={'b': -2}: closed_region -> closed_region, score 83.0 -> 91.0
- geosweep-0009: closed_region(83.0) -> closed_region(91.0) success=True
  - step 1 increase_elimination_texture patch={'b': -2}: closed_region -> closed_region, score 83.0 -> 91.0
- geosweep-0011: closed_region(82.0) -> closed_region(90.0) success=True
  - step 1 increase_elimination_texture patch={'b': -2}: closed_region -> closed_region, score 82.0 -> 90.0
- geosweep-0015: closed_region(83.0) -> closed_region(91.0) success=True
  - step 1 increase_elimination_texture patch={'b': -2}: closed_region -> closed_region, score 83.0 -> 91.0
- geosweep-0017: closed_region(82.0) -> closed_region(90.0) success=True
  - step 1 increase_elimination_texture patch={'b': -2}: closed_region -> closed_region, score 82.0 -> 90.0
- geosweep-0019: partial_region(2.0) -> closed_region(84.0) success=True
  - step 1 restore_quadratic_parameter patch={'b': -1}: partial_region -> closed_region, score 2.0 -> 75.0
  - step 2 add_affine_shift patch={'d': 1}: closed_region -> closed_region, score 75.0 -> 84.0
- geosweep-0020: closed_envelope(78.0) -> closed_envelope(86.0) success=True
  - step 1 restore_quadratic_parameter patch={'b': -1}: closed_envelope -> closed_envelope, score 78.0 -> 77.0
  - step 2 add_affine_shift patch={'d': 1}: closed_envelope -> closed_envelope, score 77.0 -> 86.0
- geosweep-0021: partial_region(11.0) -> closed_region(84.0) success=True
  - step 1 restore_quadratic_parameter patch={'b': -1}: partial_region -> closed_region, score 11.0 -> 84.0
- geosweep-0023: partial_region(10.0) -> closed_region(91.0) success=True
  - step 1 restore_quadratic_parameter patch={'b': -1}: partial_region -> closed_region, score 10.0 -> 83.0
  - step 2 increase_elimination_texture patch={'b': -2}: closed_region -> closed_region, score 83.0 -> 91.0
- geosweep-0025: partial_region(11.0) -> closed_region(84.0) success=True
  - step 1 restore_quadratic_parameter patch={'b': -1}: partial_region -> closed_region, score 11.0 -> 84.0
- geosweep-0027: partial_region(10.0) -> closed_region(91.0) success=True
  - step 1 restore_quadratic_parameter patch={'b': -1}: partial_region -> closed_region, score 10.0 -> 83.0
  - step 2 increase_elimination_texture patch={'b': -2}: closed_region -> closed_region, score 83.0 -> 91.0
- geosweep-0029: partial_region(9.0) -> closed_region(90.0) success=True
  - step 1 restore_quadratic_parameter patch={'b': -1}: partial_region -> closed_region, score 9.0 -> 82.0
  - step 2 increase_elimination_texture patch={'b': -2}: closed_region -> closed_region, score 82.0 -> 90.0
- geosweep-0031: partial_region(11.0) -> closed_region(84.0) success=True
  - step 1 restore_quadratic_parameter patch={'b': -1}: partial_region -> closed_region, score 11.0 -> 84.0
- geosweep-0033: partial_region(10.0) -> closed_region(91.0) success=True
  - step 1 restore_quadratic_parameter patch={'b': -1}: partial_region -> closed_region, score 10.0 -> 83.0
  - step 2 increase_elimination_texture patch={'b': -2}: closed_region -> closed_region, score 83.0 -> 91.0
- geosweep-0035: partial_region(9.0) -> closed_region(90.0) success=True
  - step 1 restore_quadratic_parameter patch={'b': -1}: partial_region -> closed_region, score 9.0 -> 82.0
  - step 2 increase_elimination_texture patch={'b': -2}: closed_region -> closed_region, score 82.0 -> 90.0
- geosweep-0037: closed_region(82.0) -> closed_region(92.0) success=True
  - step 1 add_affine_shift patch={'d': 1}: closed_region -> closed_region, score 82.0 -> 92.0
- geosweep-0055: closed_region(75.0) -> closed_region(84.0) success=True
  - step 1 add_affine_shift patch={'d': 1}: closed_region -> closed_region, score 75.0 -> 84.0
- geosweep-0056: closed_envelope(77.0) -> closed_envelope(86.0) success=True
  - step 1 add_affine_shift patch={'d': 1}: closed_envelope -> closed_envelope, score 77.0 -> 86.0

## Curriculum Export

- Verified curriculum items: 37
These are the generated problems that can be fed back into the solver benchmark as parser/router/strategy regression cases without storing problem-specific answers in code.
