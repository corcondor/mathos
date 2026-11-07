# Complete finite certification of upper ell=k-2, effective first index >=3

## Statement and analytic prerequisites

For the original squared-index equation, there is no upper-branch
solution satisfying

\[
\ell=k-2,\qquad d=\min(j,i-j)\ge3.
\]

The analytic part is proved in `v4_upper_complement_two.md` and its
sharpening `v4_upper_complement_two_sharper_bounds.md`. Together with
the earlier ordering and endpoint reductions, every such solution
would have

\[
23\le k<K:=2^{22},\quad i+2\le k,\quad d\ge3,
\]

\[
A=\binom id=\binom ij,\quad B=\frac{k(k-1)}2,
\quad t=A-B,\quad k\le t\le B,
\]

\[
t<\begin{cases}10(k-2)&k<802,\\5(k-2)&k\ge802.\end{cases}
\tag{1}
\]

The weaker bound \(t<10(k-2)\) holds throughout. Hence

\[
A\le A_{\max}
=\frac{(K-1)(K-2)}2+10(K-3)-1
=8796128673762.
\]

Because \(\binom i3\le\binom id=A\),
\((i-2)^3<6A\). Exact integer cube roots give the safe bound

\[
i\le\lfloor(6A_{\max})^{1/3}\rfloor+2=37512.
\]

The finite list is defined by these proved constraints, not by an
experimental search cutoff. Both orientations \(j=d\) and \(j=i-d\)
are retained.

## Certificate types

For each candidate write

\[
L=\binom At,\quad X=\binom{i^2}{j^2},
\quad Y=\binom{k^2}{4k-4}.
\]

The generator supplies one of two exact certificates.

1. **Residue certificate:** a prime \(p\) such that
   \(L\not\equiv X+Y\pmod p\).
2. **Valuation certificate:** a prime \(p\) for which the smallest of
   \(v_p(L),v_p(X),v_p(Y)\) occurs only once.

The second certificate also contradicts \(L-X-Y=0\): after dividing
by the smallest power of \(p\), exactly one term is nonzero modulo
\(p\), so cancellation is impossible.

Ordinary residues are generated with factorial-table Lucas formulas
and verified using exact `math.comb` on the base-p digits.
Valuations are generated using Legendre's factorial floor sums and
verified by counting the carries in Kummer's theorem. The two
valuation implementations do not call one another.

## Coverage verification

The generator enumerates \(i\) first, builds \(\binom id\) while it
is at most \(A_{\max}\), and walks down the few triangular numbers
immediately below \(A\). Its stopping condition deliberately uses
\(t\ge10(k-2)\), which remains monotone across \(k=802\); the
stronger bound for larger \(k\) is only a filter.

The independent verifier enumerates \(d\) first, increasing \(i\)
until \(\binom id>A_{\max}\). It obtains the whole triangular
interval by two separate integer binary searches:

\[
B(k)+10(k-2)>A,\qquad B(k)<A.
\]

It applies the remaining inequalities in (1), checks both
orientations, and requires a matching certificate for every candidate.
Duplicate entries, missing candidates, or extra candidates are errors.
Every certificate modulus is checked for primality, and every
residue or valuation contradiction is recalculated.

## Executed result

The generated complete finite list has **350,164 candidates**.
Residues modulo primes at most 101 exclude **350,011** of them.
For the remaining **153**, all three terms vanished modulo every
tested small prime, but their p-adic valuations gave contradictions
using primes at most 7.

For example, the candidate

\[
i=3460,\quad j=3456,\quad k=3452904
\]

has, at \(p=2\),

\[
\bigl(v_2(L),v_2(X),v_2(Y)\bigr)=(20,1,15).
\]

The unique minimum proves impossibility even though the three
ordinary residues modulo 2 all vanish.

This is an actual application of the p-adic/digit method to cases
left unresolved by ordinary small-prime congruences.

Reproduction:

```bash
python3 v4_upper_complement_two_dge3.py generate
python3 v4_upper_complement_two_dge3.py verify
```

The script imports helpers from `v4_lower_l1_single_top.py`; both
files must be in the same directory. The certificate and report are
`v4_upper_complement_two_dge3_certificates.json` and
`v4_upper_complement_two_dge3_verification.json`.

The independent verifier completed with zero unresolved candidates.
The certificate SHA256 is
`719f8090b51407e6bf7a8f9ad54b76489cb70fbfacb55843d47c243fd572910f`.

The written analytic proof and exact finite verification together
exclude the entire stated infinite family. They are not claimed
to have been formalized in Lean. The \(j=1\) part of upper
\(\ell=k-2\) is a separate certificate task.
