# Geometry Sweep Phase Synthesis

Generated: 2026-07-03T16:19:13.403539+00:00

## Family

- Name: `quadratic_sweep_region_envelope`
- Theme: passing region / envelope / parameter elimination
- Invariant: For b != 0, eliminating the real parameter t from y = a*t*x + b*t^2 + c*x + d gives a quadratic boundary.  Region queries use exists t in R; envelope queries use resultant(F, dF/dt).

## Phase Counts

- closed_envelope: 48
- closed_region: 48

## Label Counts

- geometry_sweep: 96
- nondegenerate: 96
- quadratic_parameter: 96
- sympy_supported: 96
- affine_shift: 84
- envelope: 48
- region: 48
- upper_bound: 30
- lower_bound: 18

## Top Candidates

### 1. geosweep-0022 score=94.0

- task: envelope; params: a=1, b=-2, c=0, d=1
- dsl: `task envelope; family y = t*x - 2*t**2 + 1; param t in R`
- phase: closed_envelope
- answer: `-2*(x**2 - 8*y + 8) = 0`
- difficulty: hard

```tex
実数$t$に対して，曲線
\[
y=tx - 2t^2 + 1
\]
が定まる。この曲線族の包絡線を求めよ。
```

### 2. geosweep-0026 score=94.0

- task: envelope; params: a=1, b=-2, c=1, d=0
- dsl: `task envelope; family y = t*x - 2*t**2 + x; param t in R`
- phase: closed_envelope
- answer: `-2*(x**2 + 8*x - 8*y) = 0`
- difficulty: hard

```tex
実数$t$に対して，曲線
\[
y=tx - 2t^2 + x
\]
が定まる。この曲線族の包絡線を求めよ。
```

### 3. geosweep-0032 score=94.0

- task: envelope; params: a=1, b=-2, c=-1, d=0
- dsl: `task envelope; family y = t*x - 2*t**2 - x; param t in R`
- phase: closed_envelope
- answer: `-2*(x**2 - 8*x - 8*y) = 0`
- difficulty: hard

```tex
実数$t$に対して，曲線
\[
y=tx - 2t^2 - x
\]
が定まる。この曲線族の包絡線を求めよ。
```

### 4. geosweep-0058 score=94.0

- task: envelope; params: a=1, b=2, c=0, d=1
- dsl: `task envelope; family y = t*x + 2*t**2 + 1; param t in R`
- phase: closed_envelope
- answer: `2*(x**2 + 8*y - 8) = 0`
- difficulty: hard

```tex
実数$t$に対して，曲線
\[
y=tx + 2t^2 + 1
\]
が定まる。この曲線族の包絡線を求めよ。
```

### 5. geosweep-0021 score=92.0

- task: region; params: a=1, b=-2, c=0, d=1
- dsl: `task region; family y = t*x - 2*t**2 + 1; param t in R`
- phase: closed_region
- answer: `y <= (x**2 + 8)/8`
- difficulty: hard

```tex
実数$t$に対して，曲線
\[
y=tx - 2t^2 + 1
\]
が定まる。この曲線族の通過領域を求めよ。
```

### 6. geosweep-0025 score=92.0

- task: region; params: a=1, b=-2, c=1, d=0
- dsl: `task region; family y = t*x - 2*t**2 + x; param t in R`
- phase: closed_region
- answer: `y <= x*(x + 8)/8`
- difficulty: hard

```tex
実数$t$に対して，曲線
\[
y=tx - 2t^2 + x
\]
が定まる。この曲線族の通過領域を求めよ。
```

### 7. geosweep-0031 score=92.0

- task: region; params: a=1, b=-2, c=-1, d=0
- dsl: `task region; family y = t*x - 2*t**2 - x; param t in R`
- phase: closed_region
- answer: `y <= x*(x - 8)/8`
- difficulty: hard

```tex
実数$t$に対して，曲線
\[
y=tx - 2t^2 - x
\]
が定まる。この曲線族の通過領域を求めよ。
```

### 8. geosweep-0057 score=92.0

- task: region; params: a=1, b=2, c=0, d=1
- dsl: `task region; family y = t*x + 2*t**2 + 1; param t in R`
- phase: closed_region
- answer: `y >= -(x**2 - 8)/8`
- difficulty: hard

```tex
実数$t$に対して，曲線
\[
y=tx + 2t^2 + 1
\]
が定まる。この曲線族の通過領域を求めよ。
```

## Interpretation

This theme uses the same generated curve family for two observations: `region` compiles to an existential real-parameter elimination problem, and `envelope` compiles to resultant(F, dF/dt).
The generator is still narrow, but it is now a second phase family: MathOS can propose geometry problems, execute the Geometry DSL backend, score closed-form outputs, and diversify by observation and curvature.
