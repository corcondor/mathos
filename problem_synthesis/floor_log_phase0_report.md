# Problem Phase Diagram Synthesis

Generated: 2026-07-03T16:04:42.366425+00:00

## Family

- Name: `floor_log_integral_limit`
- Theme: floor / integral / asymptotic limit
- Invariant: For alpha>0 and floor(alpha*x+beta)+gamma positive on [1,infty), integral_1^n log(floor(alpha*x+beta)+gamma) dx = n log n + n(log(alpha)-1) + O(log n).

## Phase Counts

- invalid_domain: 81
- divergent: 53
- finite_closed: 53
- vanishing: 53

## Label Counts

- rational_slope: 240
- degenerate: 187
- valid_domain: 159
- numeric_supported: 133
- invalid_domain: 81
- clean_asymptotic: 53
- divergent_phase: 53
- finite_closed: 53
- good_candidate: 53
- hidden_shift: 53
- vanishing_phase: 53
- near_domain_boundary: 42

## Top Candidates

### 1. floorlog-0041 score=101.0

- params: alpha=1/2, beta=-2, gamma=3, p=1
- labels: valid_domain, finite_closed, clean_asymptotic, near_domain_boundary, hidden_shift, rational_slope, numeric_supported, good_candidate
- answer: $\frac{1}{2e}$
- problem:

```tex
以下，$[x]$で$x$以下の最大の整数を表す。正の整数$n$に対して
\[
a_n=\int_1^n \log\left([\frac{1}{2}x-2]+3\right)\,dx
\]
と定める。このとき
\[
\lim_{n\to\infty} \frac{e^{a_n/n}}{n}
\]
を求めよ。
```

- numeric probe:
  - {"n": 100, "integral": 296.9555339035, "value": 0.19483254226981284}
  - {"n": 200, "integral": 727.4787511111, "value": 0.18996344672417162}

### 2. floorlog-0236 score=100.2

- params: alpha=2/3, beta=-2, gamma=3, p=1
- labels: valid_domain, finite_closed, clean_asymptotic, near_domain_boundary, hidden_shift, rational_slope, numeric_supported, good_candidate
- answer: $\frac{2}{3e}$
- problem:

```tex
以下，$[x]$で$x$以下の最大の整数を表す。正の整数$n$に対して
\[
a_n=\int_1^n \log\left([\frac{2}{3}x-2]+3\right)\,dx
\]
と定める。このとき
\[
\lim_{n\to\infty} \frac{e^{a_n/n}}{n}
\]
を求めよ。
```

- numeric probe:
  - {"n": 100, "integral": 324.5030548612, "value": 0.2566249400183547}
  - {"n": 200, "integral": 783.620680474, "value": 0.25152473001979847}

### 3. floorlog-0053 score=98.6

- params: alpha=1/2, beta=-3/2, gamma=2, p=1
- labels: valid_domain, finite_closed, clean_asymptotic, near_domain_boundary, hidden_shift, rational_slope, numeric_supported, good_candidate
- answer: $\frac{1}{2e}$
- problem:

```tex
以下，$[x]$で$x$以下の最大の整数を表す。正の整数$n$に対して
\[
a_n=\int_1^n \log\left([\frac{1}{2}x-\frac{3}{2}]+2\right)\,dx
\]
と定める。このとき
\[
\lim_{n\to\infty} \frac{e^{a_n/n}}{n}
\]
を求めよ。
```

- numeric probe:
  - {"n": 100, "integral": 293.0435108981, "value": 0.18735780829911236}
  - {"n": 200, "integral": 722.8735809251, "value": 0.1856393507599167}

### 4. floorlog-0110 score=95.133

- params: alpha=1/2, beta=1/3, gamma=1, p=1
- labels: valid_domain, finite_closed, clean_asymptotic, near_domain_boundary, hidden_shift, rational_slope, numeric_supported, good_candidate
- answer: $\frac{1}{2e}$
- problem:

```tex
以下，$[x]$で$x$以下の最大の整数を表す。正の整数$n$に対して
\[
a_n=\int_1^n \log\left([\frac{1}{2}x+\frac{1}{3}]+1\right)\,dx
\]
と定める。このとき
\[
\lim_{n\to\infty} \frac{e^{a_n/n}}{n}
\]
を求めよ。
```

- numeric probe:
  - {"n": 100, "integral": 299.576750992, "value": 0.20000704739742137}
  - {"n": 200, "integral": 730.5554981224, "value": 0.19290838807895405}

### 5. floorlog-0221 score=95.0

- params: alpha=2/3, beta=-5/2, gamma=3, p=1
- labels: valid_domain, finite_closed, clean_asymptotic, near_domain_boundary, hidden_shift, rational_slope, numeric_supported, good_candidate
- answer: $\frac{2}{3e}$
- problem:

```tex
以下，$[x]$で$x$以下の最大の整数を表す。正の整数$n$に対して
\[
a_n=\int_1^n \log\left([\frac{2}{3}x-\frac{5}{2}]+3\right)\,dx
\]
と定める。このとき
\[
\lim_{n\to\infty} \frac{e^{a_n/n}}{n}
\]
を求めよ。
```

- numeric probe:
  - {"n": 100, "integral": 321.3495353967, "value": 0.2486584944767183}
  - {"n": 200, "integral": 779.949173292, "value": 0.24694947940711084}

### 6. floorlog-0137 score=94.067

- params: alpha=1/2, beta=2/3, gamma=0, p=1
- labels: valid_domain, finite_closed, clean_asymptotic, near_domain_boundary, hidden_shift, rational_slope, numeric_supported, good_candidate
- answer: $\frac{1}{2e}$
- problem:

```tex
以下，$[x]$で$x$以下の最大の整数を表す。正の整数$n$に対して
\[
a_n=\int_1^n \log\left([\frac{1}{2}x+\frac{2}{3}]\right)\,dx
\]
と定める。このとき
\[
\lim_{n\to\infty} \frac{e^{a_n/n}}{n}
\]
を求めよ。
```

- numeric probe:
  - {"n": 100, "integral": 294.3475185666, "value": 0.18981696745186322}
  - {"n": 200, "integral": 724.4086376538, "value": 0.187069667453869}

### 7. floorlog-0056 score=91.2

- params: alpha=1/2, beta=-3/2, gamma=3, p=1
- labels: valid_domain, finite_closed, clean_asymptotic, hidden_shift, rational_slope, numeric_supported, good_candidate
- answer: $\frac{1}{2e}$
- problem:

```tex
以下，$[x]$で$x$以下の最大の整数を表す。正の整数$n$に対して
\[
a_n=\int_1^n \log\left([\frac{1}{2}x-\frac{3}{2}]+3\right)\,dx
\]
と定める。このとき
\[
\lim_{n\to\infty} \frac{e^{a_n/n}}{n}
\]
を求めよ。
```

- numeric probe:
  - {"n": 100, "integral": 300.8873595363, "value": 0.20264560969254253}
  - {"n": 200, "integral": 732.093871628, "value": 0.1943979352006197}

### 8. floorlog-0071 score=90.4

- params: alpha=1/2, beta=-1, gamma=3, p=1
- labels: valid_domain, finite_closed, clean_asymptotic, hidden_shift, rational_slope, numeric_supported, good_candidate
- answer: $\frac{1}{2e}$
- problem:

```tex
以下，$[x]$で$x$以下の最大の整数を表す。正の整数$n$に対して
\[
a_n=\int_1^n \log\left([\frac{1}{2}x-1]+3\right)\,dx
\]
と定める。このとき
\[
\lim_{n\to\infty} \frac{e^{a_n/n}}{n}
\]
を求めよ。
```

- numeric probe:
  - {"n": 100, "integral": 304.1260379884, "value": 0.20931608394711865}
  - {"n": 200, "integral": 736.0158449642, "value": 0.19824767587740597}

### 9. floorlog-0140 score=86.667

- params: alpha=1/2, beta=2/3, gamma=1, p=1
- labels: valid_domain, finite_closed, clean_asymptotic, hidden_shift, rational_slope, numeric_supported, good_candidate
- answer: $\frac{1}{2e}$
- problem:

```tex
以下，$[x]$で$x$以下の最大の整数を表す。正の整数$n$に対して
\[
a_n=\int_1^n \log\left([\frac{1}{2}x+\frac{2}{3}]+1\right)\,dx
\]
と定める。このとき
\[
\lim_{n\to\infty} \frac{e^{a_n/n}}{n}
\]
を求めよ。
```

- numeric probe:
  - {"n": 100, "integral": 301.9669190203, "value": 0.20484514085265662}
  - {"n": 200, "integral": 733.4011960734, "value": 0.19567280319066538}

### 10. floorlog-0239 score=85.8

- params: alpha=2/3, beta=-2, gamma=4, p=1
- labels: valid_domain, finite_closed, clean_asymptotic, hidden_shift, rational_slope, numeric_supported, good_candidate
- answer: $\frac{2}{3e}$
- problem:

```tex
以下，$[x]$で$x$以下の最大の整数を表す。正の整数$n$に対して
\[
a_n=\int_1^n \log\left([\frac{2}{3}x-2]+4\right)\,dx
\]
と定める。このとき
\[
\lim_{n\to\infty} \frac{e^{a_n/n}}{n}
\]
を求めよ。
```

- numeric probe:
  - {"n": 100, "integral": 330.1317616955, "value": 0.2714838653906965}
  - {"n": 200, "integral": 790.2780104827, "value": 0.260038049580179}

## Repair Examples

- floorlog-0001 phase=invalid_domain params={'candidate_id': 'floorlog-0001', 'alpha': '1/2', 'beta': '-3', 'gamma': 0, 'p': '0', 'lower': '1', 'expression': 'floor(1/2*x + -3) + 0'}
  - fix_domain: Make the logarithm positive on the whole integration interval. patch={'gamma': 4}
  - move_to_finite_phase: Set p=1 to land on the finite nonzero asymptotic boundary. patch={'p': '1'}
- floorlog-0002 phase=invalid_domain params={'candidate_id': 'floorlog-0002', 'alpha': '1/2', 'beta': '-3', 'gamma': 0, 'p': '1', 'lower': '1', 'expression': 'floor(1/2*x + -3) + 0'}
  - fix_domain: Make the logarithm positive on the whole integration interval. patch={'gamma': 4}
- floorlog-0003 phase=invalid_domain params={'candidate_id': 'floorlog-0003', 'alpha': '1/2', 'beta': '-3', 'gamma': 0, 'p': '2', 'lower': '1', 'expression': 'floor(1/2*x + -3) + 0'}
  - fix_domain: Make the logarithm positive on the whole integration interval. patch={'gamma': 4}
  - move_to_finite_phase: Set p=1 to land on the finite nonzero asymptotic boundary. patch={'p': '1'}
- floorlog-0004 phase=invalid_domain params={'candidate_id': 'floorlog-0004', 'alpha': '1/2', 'beta': '-3', 'gamma': 1, 'p': '0', 'lower': '1', 'expression': 'floor(1/2*x + -3) + 1'}
  - fix_domain: Make the logarithm positive on the whole integration interval. patch={'gamma': 4}
  - move_to_finite_phase: Set p=1 to land on the finite nonzero asymptotic boundary. patch={'p': '1'}
- floorlog-0005 phase=invalid_domain params={'candidate_id': 'floorlog-0005', 'alpha': '1/2', 'beta': '-3', 'gamma': 1, 'p': '1', 'lower': '1', 'expression': 'floor(1/2*x + -3) + 1'}
  - fix_domain: Make the logarithm positive on the whole integration interval. patch={'gamma': 4}
- floorlog-0006 phase=invalid_domain params={'candidate_id': 'floorlog-0006', 'alpha': '1/2', 'beta': '-3', 'gamma': 1, 'p': '2', 'lower': '1', 'expression': 'floor(1/2*x + -3) + 1'}
  - fix_domain: Make the logarithm positive on the whole integration interval. patch={'gamma': 4}
  - move_to_finite_phase: Set p=1 to land on the finite nonzero asymptotic boundary. patch={'p': '1'}
- floorlog-0007 phase=invalid_domain params={'candidate_id': 'floorlog-0007', 'alpha': '1/2', 'beta': '-3', 'gamma': 2, 'p': '0', 'lower': '1', 'expression': 'floor(1/2*x + -3) + 2'}
  - fix_domain: Make the logarithm positive on the whole integration interval. patch={'gamma': 4}
  - move_to_finite_phase: Set p=1 to land on the finite nonzero asymptotic boundary. patch={'p': '1'}
- floorlog-0008 phase=invalid_domain params={'candidate_id': 'floorlog-0008', 'alpha': '1/2', 'beta': '-3', 'gamma': 2, 'p': '1', 'lower': '1', 'expression': 'floor(1/2*x + -3) + 2'}
  - fix_domain: Make the logarithm positive on the whole integration interval. patch={'gamma': 4}

## Interpretation

The finite nonzero phase appears at `p=1`.  This is the first useful problem-making boundary: `p<1` diverges, `p>1` vanishes, while `p=1` keeps a simple closed form `alpha/e` despite the floor-function perturbation.
Good candidates are deliberately close to a domain boundary or include a harmless shift.  Those parameters create proof work without making the final answer ugly.
