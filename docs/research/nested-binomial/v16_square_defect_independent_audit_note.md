# Independent audit of the v16 intrinsic square-denominator exclusion

Date: 2026-11-06 JST. Internal mathematical and software audit, not
external peer review or Lean kernel verification.

## Audited mathematical reduction

Put delta=Q/gcd(Q,r^2), where Q=n(n-1)/M and
M=gcd(n,3)gcd(n-1,6). The following deductions were checked independently:

- Q|r^3 gives delta|r and delta^3|Q prime by prime. If alpha=v_p(Q)
  and e=v_p(r), then the delta exponent is max(alpha-2e,0), which is
  at most e and at most floor(alpha/3).
- K=delta*r^2/Q is an integer and gcd(K,delta)=1. The original branch
  bounds imply 9M*delta<K<10400M*delta/927.
- The integer-gap proof from v15 applies to delta directly: assuming
  log(n)>=28delta yields 0<K-9Mdelta<50111163/51380224<1. Thus
  n<exp(28delta)<2^(42delta).
- Writing C=Mdelta and CK=s^2*d gives x^2-dy^2=1,
  n=(x+1)/2, r=s*d*y/(2C). The integer reconstruction conditions and
  the d=1 exception are necessary and sufficient for this quadratic
  relation, before the other branch conditions are imposed.
- Every positive Pell solution x/y satisfies
  |x/y-sqrt(d)|=1/[y^2(x/y+sqrt(d))]<1/(2y^2), so the ordinary
  Legendre convergent criterion applies to these Pell solutions.
  This does not modify the separate old 3/(2q^2) approximation problem.
- The first norm-one convergent is the minimal positive-y unit. The
  norm-one descent argument proves that all positive Pell solutions
  are powers of it.
- Summing the open coefficient intervals gives fewer than
  12delta*(2057/927)<27delta coefficient triples for fixed delta.
- The minimal unit is at least 2+sqrt(3)>2^(3/2), so a Pell point
  x<2^(42delta+1)-1 has power index at most 28delta+1.

These are written deductions. Their complete Lean formalization was
not run in this environment.

## Executed independent reconstruction

The separate source `v16_square_defect_independent_audit.py` does not
import or call the producer. It was executed against the final
`v16_square_defect_pell_results.json` and returned PASS.

The independent choices are:

- Coefficients: enumerate K<=12Mdelta and impose the two strict integer
  inequalities and gcd(K,delta)=1 directly.
- Square part: seek the largest square divisor by descending integer
  divisor checks, instead of the producer's prime factorization.
- Fundamental unit: generate the complete period of sqrt(d), evaluate
  each finite continued fraction in reverse, verify every floor, and
  reject all earlier convergent norms.
- Pell points: a second-order recurrence, rather than multiplication
  by the fundamental unit as in the producer.
- Modular exclusions: factorial-table Lucas digits at the actual
  k and the original squared lower index j^2=(n-3)^2. The producer's
  short zero-digit certificates, including all null cases, are also
  checked independently.

All 1,223 coefficient triples, 570 distinct fundamental units, and
every recurrence disposition and first omitted point agree.

| Stage | Reproduced count |
|---|---:|
| Coefficient triples | 1,223 |
| Square radicands, with no positive Pell point | 8 |
| Pell points below the proved height | 34,010 |
| Integral n,r | 24,114 |
| n>=104 | 23,920 |
| Actual M | 9,324 |
| Actual delta | 9,324 |
| Q divides r^3 | 1,929 |
| Strict coarse interval | 1,762 |
| Strict rational logarithmic interval | 123 |
| Original branches checked and excluded | 246 |
| Survivors | 0 |

The maximum witness prime is 23. Of the 246 modular witnesses,
242 have both binomials zero and k^2 nonzero. The four other witnesses
were checked by their full residues:

| delta | n | r | branch | p | left | first right binomial | k^2 | total right |
|---:|---:|---:|---|---:|---:|---:|---:|---:|
| 2 | 5329 | 16206 | k=r | 5 | 0 | 3 | 1 | 4 |
| 2 | 5329 | 16206 | k=A-r | 5 | 0 | 3 | 4 | 2 |
| 3 | 9801 | 30030 | k=r | 13 | 6 | 0 | 0 | 0 |
| 3 | 9801 | 30030 | k=A-r | 13 | 6 | 0 | 1 | 1 |

For delta=1, the final eleven pairs agree with v15. The stronger
height now includes 181 Pell points, compared with the earlier 188;
the final pair set is unchanged.

## Reproduction and provenance

The full input is stored losslessly in `v16_square_defect_pell_results.json.gz`.
With all the files in one directory, decompress and run:

```sh
gzip -dc v16_square_defect_pell_results.json.gz > v16_square_defect_pell_results.json
python3 v16_square_defect_independent_audit.py --input v16_square_defect_pell_results.json --generator v16_square_defect_pell.py --v15 v15_pell_square_divisor_results.json --output reproduced_square_defect_audit.json
```

The report `v16_square_defect_independent_audit.json` records all
original-index modular evidence, per-delta counts, the fundamental-unit
table, hashes of complete reconstructed traces, and these input hashes:

- Producer source: `6488b2419f08be60ed92267df78a44387728b4e93f27633ddeb100a27610d79c`.
- Input certificate: `f2001eaef853c0fe4dd5a13fe331b6890e08bd793b3e55f388099a781df546a2`.
- Auditor source: `b6330a0a5b3279bb3982fd2747c8c90b55e28022efaa302953441d9108dcd337`.

The certificate and sources remained unchanged during the audit. No
original-equation solution was found, and no complete solution of the
original four-variable problem is claimed.
