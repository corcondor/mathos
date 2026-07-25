# Problem Phase Diagram Synthesis

Generated: 2026-07-03T16:05:29.015994+00:00

## Family

- Name: `floor_log_integral_limit`
- Theme: floor / integral / asymptotic limit
- Invariant: For alpha>0 and floor(alpha*x+beta)+gamma positive on [1,infty), integral_1^n log(floor(alpha*x+beta)+gamma) dx = n log n + n(log(alpha)-1) + O(log n).

## Phase Counts

- invalid_domain: 63
- divergent: 19
- finite_closed: 19
- vanishing: 19

## Label Counts

- degenerate: 101
- invalid_domain: 63
- rational_slope: 60
- numeric_supported: 57
- valid_domain: 57
- near_domain_boundary: 24
- clean_asymptotic: 19
- divergent_phase: 19
- finite_closed: 19
- good_candidate: 19
- hidden_shift: 19
- vanishing_phase: 19

## Top Candidates

### 1. floorlog-0062 score=96.0

- params: alpha=2, beta=-3, gamma=2, p=1
- labels: valid_domain, finite_closed, clean_asymptotic, near_domain_boundary, hidden_shift, numeric_supported, good_candidate
- answer: $\frac{2}{e}$
- problem:

```tex
以下，$[x]$で$x$以下の最大の整数を表す。正の整数$n$に対して
\[
a_n=\int_1^n \log\left([2x-3]+2\right)\,dx
\]
と定める。このとき
\[
\lim_{n\to\infty} \frac{e^{a_n/n}}{n}
\]
を求めよ。
```

- numeric probe:
  - {"n": 100, "integral": 426.3201825006, "value": 0.7103706797840517}
  - {"n": 200, "integral": 994.2601360096, "value": 0.7210717107631727}

### 2. floorlog-0105 score=95.2

- params: alpha=1/2, beta=-3, gamma=4, p=1
- labels: valid_domain, finite_closed, clean_asymptotic, near_domain_boundary, hidden_shift, rational_slope, numeric_supported, good_candidate
- answer: $\frac{1}{2e}$
- problem:

```tex
以下，$[x]$で$x$以下の最大の整数を表す。正の整数$n$に対して
\[
a_n=\int_1^n \log\left([\frac{1}{2}x-3]+4\right)\,dx
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

### 3. floorlog-0085 score=94.8

- params: alpha=3/2, beta=-3, gamma=3, p=1
- labels: valid_domain, finite_closed, clean_asymptotic, near_domain_boundary, hidden_shift, rational_slope, numeric_supported, good_candidate
- answer: $\frac{3}{2e}$
- problem:

```tex
以下，$[x]$で$x$以下の最大の整数を表す。正の整数$n$に対して
\[
a_n=\int_1^n \log\left([\frac{3}{2}x-3]+3\right)\,dx
\]
と定める。このとき
\[
\lim_{n\to\infty} \frac{e^{a_n/n}}{n}
\]
を求めよ。
```

- numeric probe:
  - {"n": 100, "integral": 400.0063137036, "value": 0.5460159730730619}
  - {"n": 200, "integral": 939.4680449803, "value": 0.548275631307173}

### 4. floorlog-0106 score=94.4

- params: alpha=2/3, beta=-3, gamma=4, p=1
- labels: valid_domain, finite_closed, clean_asymptotic, near_domain_boundary, hidden_shift, rational_slope, numeric_supported, good_candidate
- answer: $\frac{2}{3e}$
- problem:

```tex
以下，$[x]$で$x$以下の最大の整数を表す。正の整数$n$に対して
\[
a_n=\int_1^n \log\left([\frac{2}{3}x-3]+4\right)\,dx
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

### 5. floorlog-0039 score=94.0

- params: alpha=3, beta=-3, gamma=1, p=1
- labels: valid_domain, finite_closed, clean_asymptotic, near_domain_boundary, hidden_shift, numeric_supported, good_candidate
- answer: $\frac{3}{e}$
- problem:

```tex
以下，$[x]$で$x$以下の最大の整数を表す。正の整数$n$に対して
\[
a_n=\int_1^n \log\left([3x-3]+1\right)\,dx
\]
と定める。このとき
\[
\lim_{n\to\infty} \frac{e^{a_n/n}}{n}
\]
を求めよ。
```

- numeric probe:
  - {"n": 100, "integral": 465.9348434702, "value": 1.0556727576964102}
  - {"n": 200, "integral": 1074.3631844574, "value": 1.0762669822601139}

### 6. floorlog-0107 score=93.6

- params: alpha=3/4, beta=-3, gamma=4, p=1
- labels: valid_domain, finite_closed, clean_asymptotic, near_domain_boundary, hidden_shift, rational_slope, numeric_supported, good_candidate
- answer: $\frac{3}{4e}$
- problem:

```tex
以下，$[x]$で$x$以下の最大の整数を表す。正の整数$n$に対して
\[
a_n=\int_1^n \log\left([\frac{3}{4}x-3]+4\right)\,dx
\]
と定める。このとき
\[
\lim_{n\to\infty} \frac{e^{a_n/n}}{n}
\]
を求めよ。
```

- numeric probe:
  - {"n": 100, "integral": 335.853869613, "value": 0.28747151846567837}
  - {"n": 200, "integral": 806.6934744659, "value": 0.2822816368422938}

### 7. floorlog-0016 score=92.0

- params: alpha=4, beta=-3, gamma=0, p=1
- labels: valid_domain, finite_closed, clean_asymptotic, near_domain_boundary, hidden_shift, numeric_supported, good_candidate
- answer: $\frac{4}{e}$
- problem:

```tex
以下，$[x]$で$x$以下の最大の整数を表す。正の整数$n$に対して
\[
a_n=\int_1^n \log\left([4x-3]\right)\,dx
\]
と定める。このとき
\[
\lim_{n\to\infty} \frac{e^{a_n/n}}{n}
\]
を求めよ。
```

- numeric probe:
  - {"n": 100, "integral": 494.1374709333, "value": 1.3996252515782333}
  - {"n": 200, "integral": 1131.3049486871, "value": 1.4307622967486842}

### 8. floorlog-0084 score=91.0

- params: alpha=1, beta=-3, gamma=3, p=1
- labels: valid_domain, finite_closed, clean_asymptotic, near_domain_boundary, hidden_shift, numeric_supported, good_candidate
- answer: $\frac{1}{e}$
- problem:

```tex
以下，$[x]$で$x$以下の最大の整数を表す。正の整数$n$に対して
\[
a_n=\int_1^n \log\left([x-3]+3\right)\,dx
\]
と定める。このとき
\[
\lim_{n\to\infty} \frac{e^{a_n/n}}{n}
\]
を求めよ。
```

- numeric probe:
  - {"n": 100, "integral": 359.1342053696, "value": 0.3628273664733239}
  - {"n": 200, "integral": 857.9336698259, "value": 0.3647113655962666}

## Repair Examples

- floorlog-0001 phase=invalid_domain params={'candidate_id': 'floorlog-0001', 'alpha': '1/2', 'beta': '-3', 'gamma': 0, 'p': '0', 'lower': '1', 'expression': 'floor(1/2*x + -3) + 0'}
  - fix_domain: Make the logarithm positive on the whole integration interval. patch={'gamma': 4}
  - move_to_finite_phase: Set p=1 to land on the finite nonzero asymptotic boundary. patch={'p': '1'}
- floorlog-0002 phase=invalid_domain params={'candidate_id': 'floorlog-0002', 'alpha': '2/3', 'beta': '-3', 'gamma': 0, 'p': '0', 'lower': '1', 'expression': 'floor(2/3*x + -3) + 0'}
  - fix_domain: Make the logarithm positive on the whole integration interval. patch={'gamma': 4}
  - move_to_finite_phase: Set p=1 to land on the finite nonzero asymptotic boundary. patch={'p': '1'}
- floorlog-0003 phase=invalid_domain params={'candidate_id': 'floorlog-0003', 'alpha': '3/4', 'beta': '-3', 'gamma': 0, 'p': '0', 'lower': '1', 'expression': 'floor(3/4*x + -3) + 0'}
  - fix_domain: Make the logarithm positive on the whole integration interval. patch={'gamma': 4}
  - move_to_finite_phase: Set p=1 to land on the finite nonzero asymptotic boundary. patch={'p': '1'}
- floorlog-0004 phase=invalid_domain params={'candidate_id': 'floorlog-0004', 'alpha': '1', 'beta': '-3', 'gamma': 0, 'p': '0', 'lower': '1', 'expression': 'floor(1*x + -3) + 0'}
  - fix_domain: Make the logarithm positive on the whole integration interval. patch={'gamma': 3}
  - move_to_finite_phase: Set p=1 to land on the finite nonzero asymptotic boundary. patch={'p': '1'}
- floorlog-0005 phase=invalid_domain params={'candidate_id': 'floorlog-0005', 'alpha': '3/2', 'beta': '-3', 'gamma': 0, 'p': '0', 'lower': '1', 'expression': 'floor(3/2*x + -3) + 0'}
  - fix_domain: Make the logarithm positive on the whole integration interval. patch={'gamma': 3}
  - move_to_finite_phase: Set p=1 to land on the finite nonzero asymptotic boundary. patch={'p': '1'}
- floorlog-0006 phase=invalid_domain params={'candidate_id': 'floorlog-0006', 'alpha': '2', 'beta': '-3', 'gamma': 0, 'p': '0', 'lower': '1', 'expression': 'floor(2*x + -3) + 0'}
  - fix_domain: Make the logarithm positive on the whole integration interval. patch={'gamma': 2}
  - move_to_finite_phase: Set p=1 to land on the finite nonzero asymptotic boundary. patch={'p': '1'}
- floorlog-0007 phase=invalid_domain params={'candidate_id': 'floorlog-0007', 'alpha': '3', 'beta': '-3', 'gamma': 0, 'p': '0', 'lower': '1', 'expression': 'floor(3*x + -3) + 0'}
  - fix_domain: Make the logarithm positive on the whole integration interval. patch={'gamma': 1}
  - move_to_finite_phase: Set p=1 to land on the finite nonzero asymptotic boundary. patch={'p': '1'}
- floorlog-0008 phase=divergent params={'candidate_id': 'floorlog-0008', 'alpha': '4', 'beta': '-3', 'gamma': 0, 'p': '0', 'lower': '1', 'expression': 'floor(4*x + -3) + 0'}
  - move_to_finite_phase: Set p=1 to land on the finite nonzero asymptotic boundary. patch={'p': '1'}

## Interpretation

The finite nonzero phase appears at `p=1`.  This is the first useful problem-making boundary: `p<1` diverges, `p>1` vanishes, while `p=1` keeps a simple closed form `alpha/e` despite the floor-function perturbation.
Good candidates are deliberately close to a domain boundary or include a harmless shift.  Those parameters create proof work without making the final answer ugly.
