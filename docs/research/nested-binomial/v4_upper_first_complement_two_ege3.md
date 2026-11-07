# Complete finite certification of upper j=i-2, effective second index >=3

## Statement and analytic prerequisites

For the original squared-index equation

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2},
\]

there is no upper-branch solution with

\[
j=i-2,\qquad e=\min(\ell,k-\ell)\ge3.
\]

The analytic cutoff is proved in `v4_upper_first_complement_two.md`.
The earlier ordering, endpoint, and gap reductions imply that every
such solution would satisfy, with \(I=2^{22}\),

\[
23\le i<I,\qquad k+2\le i,\qquad 3\le e\le k/2,
\]

\[
A=\frac{i(i-1)}2,\qquad B=\binom ke=\binom{k}{\ell},
\qquad t=A-B,\qquad i\le t\le B,
\]

\[
t<\begin{cases}10(i-2)&i<802,\\5(i-2)&i\ge802.\end{cases}
\tag{1}
\]

In particular,

\[
B\le B_{\max}=\frac{(I-1)(I-2)}2-1=8796086730752.
\]

Since \(\binom k3\le\binom ke=B\), we have
\((k-2)^3<6B\). Thus an exact integer cube root gives the safe bound

\[
k\le\lfloor(6B_{\max})^{1/3}\rfloor+2=37511.
\]

These are proved necessary conditions with an explicit global cutoff.
Both orientations \(\ell=e\) and \(\ell=k-e\) are included.

## Exact certificates

Each candidate receives one of two certificates for

\[
L=\binom At,\qquad X=\binom{i^2}{4i-4},\qquad
Y=\binom{k^2}{\ell^2}.
\]

1. A prime \(p\) for which \(L\not\equiv X+Y\pmod p\).
2. A prime \(p\) for which the minimum of
   \(v_p(L),v_p(X),v_p(Y)\) occurs exactly once.

The second case contradicts the equation because, after division by
the smallest power of \(p\), one term is nonzero modulo \(p\)
and the other two vanish.

For residue certificates, generation uses factorial-table Lucas
formulas; independent verification uses exact `math.comb` on each
base-p digit. For valuation certificates, generation uses Legendre
factorial sums; independent verification uses Kummer carry counting.
Every modulus appearing in the certificate is checked for primality.

## Independent coverage check

The generator enumerates \(k\) first, increasing \(e\) and forming
\(B=\binom ke\) until the central coefficient or \(B_{\max}\)
is reached. It starts at the first triangular number strictly above
\(B\), respecting \(i\ge\max(23,k+2)\), and increments \(i\).
It stops only when the coarse condition \(t\ge10(i-2)\) holds:
\(A(i)-10(i-2)\) is strictly increasing for \(i\ge23\), so no
later candidate can qualify. The stronger condition for \(i\ge802\)
is applied as a filter.

The verifier uses a different ordering: it enumerates \(e\) first,
then increases \(k\) while \(\binom ke\le B_{\max}\). The entire
potential interval of \(i\) is found by separate integer binary
searches for

\[
A(i)>B,\qquad A(i)-10(i-2)<B.
\]

It applies all other conditions in (1), retains both orientations,
and requires exactly one matching certificate for every candidate.
Duplicate, missing, and extraneous certificate entries are errors.
The candidate set does not depend on any floating-point estimate.

## Executed result

The complete finite list contains **350,544 candidates**.
Ordinary residues exclude **350,352**; unique-minimum valuation
certificates exclude the remaining **192**. The largest obstruction
prime is 101. There are no unresolved candidates.

The largest indices in the actual candidate list are
\(i=4194142\), \(k=37510\), and \(\ell=37507\).
The independent verifier completed successfully in approximately
2.49 seconds.

Reproduction:

```bash
python3 v4_upper_first_complement_two_ege3.py generate
python3 v4_upper_first_complement_two_ege3.py verify
```

The script imports helpers from `v4_lower_l1_single_top.py` and
`v4_upper_complement_two_dge3.py`; those files must be present in the
same directory. The certificate and report are
`v4_upper_first_complement_two_ege3_certificates.json` and
`v4_upper_first_complement_two_ege3_verification.json`.

The certificate SHA256 is
`774acdba55f880684e4006bad38f7fac6bb3b16198eeab30d0fec2141e187560`.

The analytic cutoff and exact finite certification together exclude
the full stated infinite family. This part has not been formalized
in Lean; the report distinguishes its exact arithmetic verification
from the separately executed Lean lemmas.
