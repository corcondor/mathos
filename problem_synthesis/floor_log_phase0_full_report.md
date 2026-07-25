# Problem Phase Diagram Synthesis

Generated: 2026-07-03T16:13:34.007145+00:00

## Family

- Name: `floor_log_integral_limit`
- Theme: floor / integral / asymptotic limit
- Invariant: For alpha>0 and floor(alpha*x+beta)+gamma positive on [1,infty), integral_1^n log(floor(alpha*x+beta)+gamma) dx = n log n + n(log(alpha)-1) + O(log n).

## Phase Counts

- divergent: 442
- finite_closed: 442
- vanishing: 442
- invalid_domain: 234

## Label Counts

- valid_domain: 1326
- numeric_supported: 1247
- degenerate: 1118
- rational_slope: 780
- clean_asymptotic: 442
- divergent_phase: 442
- finite_closed: 442
- good_candidate: 442
- vanishing_phase: 442
- hidden_shift: 437
- invalid_domain: 234
- near_domain_boundary: 189

## Top Candidates

### 1. floorlog-0321 score=111.0

- params: alpha=1/2, beta=-2, gamma=3, p=1
- labels: valid_domain, finite_closed, clean_asymptotic, near_domain_boundary, hidden_shift, rational_slope, numeric_supported, good_candidate
- answer: $\frac{1}{2e}$
- problem:

```tex
以下，$\lfloor x\rfloor$で$x$以下の最大の整数を表す。正の整数$n$に対して
\[
a_n=\int_1^n \log\left(\lfloor \frac{1}{2}x-2\rfloor+3\right)\,dx
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

### 2. floorlog-0322 score=110.2

- params: alpha=2/3, beta=-2, gamma=3, p=1
- labels: valid_domain, finite_closed, clean_asymptotic, near_domain_boundary, hidden_shift, rational_slope, numeric_supported, good_candidate
- answer: $\frac{2}{3e}$
- problem:

```tex
以下，$\lfloor x\rfloor$で$x$以下の最大の整数を表す。正の整数$n$に対して
\[
a_n=\int_1^n \log\left(\lfloor \frac{2}{3}x-2\rfloor+3\right)\,dx
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

### 3. floorlog-0181 score=109.4

- params: alpha=3/2, beta=-5/2, gamma=2, p=1
- labels: valid_domain, finite_closed, clean_asymptotic, near_domain_boundary, hidden_shift, rational_slope, numeric_supported, good_candidate
- answer: $\frac{3}{2e}$
- problem:

```tex
以下，$\lfloor x\rfloor$で$x$以下の最大の整数を表す。正の整数$n$に対して
\[
a_n=\int_1^n \log\left(\lfloor \frac{3}{2}x-\frac{5}{2}\rfloor+2\right)\,dx
\]
と定める。このとき
\[
\lim_{n\to\infty} \frac{e^{a_n/n}}{n}
\]
を求めよ。
```

- numeric probe:
  - {"n": 100, "integral": 398.3383316016, "value": 0.5369840591235796}
  - {"n": 200, "integral": 937.5678971225, "value": 0.5430912740854889}

### 4. floorlog-0301 score=108.6

- params: alpha=3/2, beta=-2, gamma=2, p=1
- labels: valid_domain, finite_closed, clean_asymptotic, near_domain_boundary, hidden_shift, rational_slope, numeric_supported, good_candidate
- answer: $\frac{3}{2e}$
- problem:

```tex
以下，$\lfloor x\rfloor$で$x$以下の最大の整数を表す。正の整数$n$に対して
\[
a_n=\int_1^n \log\left(\lfloor \frac{3}{2}x-2\rfloor+2\right)\,dx
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

### 5. floorlog-0417 score=108.6

- params: alpha=1/2, beta=-3/2, gamma=2, p=1
- labels: valid_domain, finite_closed, clean_asymptotic, near_domain_boundary, hidden_shift, rational_slope, numeric_supported, good_candidate
- answer: $\frac{1}{2e}$
- problem:

```tex
以下，$\lfloor x\rfloor$で$x$以下の最大の整数を表す。正の整数$n$に対して
\[
a_n=\int_1^n \log\left(\lfloor \frac{1}{2}x-\frac{3}{2}\rfloor+2\right)\,dx
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

### 6. floorlog-0418 score=107.8

- params: alpha=2/3, beta=-3/2, gamma=2, p=1
- labels: valid_domain, finite_closed, clean_asymptotic, near_domain_boundary, hidden_shift, rational_slope, numeric_supported, good_candidate
- answer: $\frac{2}{3e}$
- problem:

```tex
以下，$\lfloor x\rfloor$で$x$以下の最大の整数を表す。正の整数$n$に対して
\[
a_n=\int_1^n \log\left(\lfloor \frac{2}{3}x-\frac{3}{2}\rfloor+2\right)\,dx
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

### 7. floorlog-0419 score=107.0

- params: alpha=3/4, beta=-3/2, gamma=2, p=1
- labels: valid_domain, finite_closed, clean_asymptotic, near_domain_boundary, hidden_shift, rational_slope, numeric_supported, good_candidate
- answer: $\frac{3}{4e}$
- problem:

```tex
以下，$\lfloor x\rfloor$で$x$以下の最大の整数を表す。正の整数$n$に対して
\[
a_n=\int_1^n \log\left(\lfloor \frac{3}{4}x-\frac{3}{2}\rfloor+2\right)\,dx
\]
と定める。このとき
\[
\lim_{n\to\infty} \frac{e^{a_n/n}}{n}
\]
を求めよ。
```

- numeric probe:
  - {"n": 100, "integral": 332.9755442039, "value": 0.27931509994775444}
  - {"n": 200, "integral": 803.3530509365, "value": 0.27760609018995036}

### 8. floorlog-0539 score=106.2

- params: alpha=3/4, beta=-1, gamma=2, p=1
- labels: valid_domain, finite_closed, clean_asymptotic, near_domain_boundary, hidden_shift, rational_slope, numeric_supported, good_candidate
- answer: $\frac{3}{4e}$
- problem:

```tex
以下，$\lfloor x\rfloor$で$x$以下の最大の整数を表す。正の整数$n$に対して
\[
a_n=\int_1^n \log\left(\lfloor \frac{3}{4}x-1\rfloor+2\right)\,dx
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

### 9. floorlog-0062 score=106.0

- params: alpha=2, beta=-3, gamma=2, p=1
- labels: valid_domain, finite_closed, clean_asymptotic, near_domain_boundary, hidden_shift, numeric_supported, good_candidate
- answer: $\frac{2}{e}$
- problem:

```tex
以下，$\lfloor x\rfloor$で$x$以下の最大の整数を表す。正の整数$n$に対して
\[
a_n=\int_1^n \log\left(\lfloor 2x-3\rfloor+2\right)\,dx
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

### 10. floorlog-0182 score=105.2

- params: alpha=2, beta=-5/2, gamma=2, p=1
- labels: valid_domain, finite_closed, clean_asymptotic, near_domain_boundary, hidden_shift, numeric_supported, good_candidate
- answer: $\frac{2}{e}$
- problem:

```tex
以下，$\lfloor x\rfloor$で$x$以下の最大の整数を表す。正の整数$n$に対して
\[
a_n=\int_1^n \log\left(\lfloor 2x-\frac{5}{2}\rfloor+2\right)\,dx
\]
と定める。このとき
\[
\lim_{n\to\infty} \frac{e^{a_n/n}}{n}
\]
を求めよ。
```

- numeric probe:
  - {"n": 100, "integral": 427.6435087067, "value": 0.7198336762108173}
  - {"n": 200, "integral": 995.7573763638, "value": 0.726490055186097}

### 11. floorlog-0873 score=105.133

- params: alpha=1/2, beta=1/3, gamma=1, p=1
- labels: valid_domain, finite_closed, clean_asymptotic, near_domain_boundary, hidden_shift, rational_slope, numeric_supported, good_candidate
- answer: $\frac{1}{2e}$
- problem:

```tex
以下，$\lfloor x\rfloor$で$x$以下の最大の整数を表す。正の整数$n$に対して
\[
a_n=\int_1^n \log\left(\lfloor \frac{1}{2}x+\frac{1}{3}\rfloor+1\right)\,dx
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

### 12. floorlog-0300 score=104.8

- params: alpha=1, beta=-2, gamma=2, p=1
- labels: valid_domain, finite_closed, clean_asymptotic, near_domain_boundary, hidden_shift, numeric_supported, good_candidate
- answer: $\frac{1}{e}$
- problem:

```tex
以下，$\lfloor x\rfloor$で$x$以下の最大の整数を表す。正の整数$n$に対して
\[
a_n=\int_1^n \log\left(\lfloor x-2\rfloor+2\right)\,dx
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
