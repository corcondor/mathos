# One outer-top value for an entire lower-branch family

## Scope

The original equation is

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}.
\]

This note concerns the previously classified lower-branch type L1:

\[
\ell>j,\quad k=\ell+1=B=b,\quad B\le A/2,
\quad A=\binom ij,
\quad X=\binom{i^2}{j^2},
\quad Y_b=\binom{b^2}{2b-1}.
\]

Earlier proved reductions give \(b\ge22\), \(i-j\ge4\),
\(A>b^3/4\), and \(X<16A^{2j}\). If \(b\ge3j\), they also give
\(A<b^3\). These prerequisites are recorded in
`lower_branch_reduction.md` and `sharp_q_bounds.md`.

This note proves a new uniform reduction, not global nonexistence.

## Theorem

For an integer \(b\ge22\), define the integer

\[
N_b=\min\{N\ge b:\ \binom Nb>Y_b\}.
\]

Every solution in L1 with \(b\ge3j\) must satisfy

\[
\boxed{\binom ij=N_b.}
\]

Thus every possible lower index \(j\le b/3\), taken together, shares
one outer-top value. This is stronger than having at most one upper index
\(i\) for each pair \((b,j)\).

### A factorial inequality

Put

\[
e_b=b-1-2\lfloor b/3\rfloor,
\qquad H_b=\frac{32(b-1)!4^{e_b}}{b^{3e_b}}.
\]

We prove \(H_b<1\) for all integers \(b\ge22\), entirely by exact
inequalities. For \(b=22,23,24\), one has \(e_b\ge7\), so

\[
H_b\le\frac{32\cdot23!}{(22^3/4)^7}
=\frac{53413257724968960000}{61159090448414546291}<1.
\]

For the induction step, \(e_{b+3}=e_b+1\) and
\(3e_b\ge b-3\). Therefore

\[
\frac{H_{b+3}}{H_b}
=\frac{4b(b+1)(b+2)}{(b+3)^3}
  \left(\frac b{b+3}\right)^{3e_b}
<4\left(\frac b{b+3}\right)^{b-3}<1.
\]

For the final strict inequality, the first three terms of the binomial
expansion imply

\[
\begin{aligned}
\left(1+\frac3b\right)^{b-3}
&\ge1+\frac{3(b-3)}b+
      \frac{9(b-3)(b-4)}{2b^2}\\
&\ge1+\frac{57}{22}+
      \frac92\frac{19}{22}\frac{18}{22}>4.
\end{aligned}
\]

This completes induction in each residue class modulo 3. In particular,
for \(j\le b/3\) and \(A>b^3/4\),

\[
\boxed{32(b-1)!<A^{b-1-2j}.} \tag{1}
\]

### Comparing the residual with a single binomial increment

Since \(X>0\), any solution has \(\binom Ab>Y_b\), hence \(A\ge N_b\).
Suppose instead \(A\ge N_b+1\). Then

\[
\begin{aligned}
X&=\binom Ab-Y_b\\
&\ge\binom Ab-\binom{A-1}b
=\binom{A-1}{b-1}.
\end{aligned}
\]

The inequality is actually strict when \(\binom{A-1}b>Y_b\), but strictness
here is not needed. A product estimate and \(A>b^3/4\) give

\[
\begin{aligned}
\binom{A-1}{b-1}
&=\frac{A^{b-1}}{(b-1)!}
  \prod_{h=1}^{b-1}\left(1-\frac hA\right)\\
&\ge\frac{A^{b-1}}{(b-1)!}
 \left(1-\frac{b(b-1)}{2A}\right)\\
&>\frac{A^{b-1}}{2(b-1)!}
>16A^{2j}>X.
\end{aligned}
\]

The penultimate step is (1), and the last step is the previously proved
bound on \(X\). This contradiction proves \(A=N_b\).

## Exact decision procedure for any fixed b

The theorem permits the following complete procedure in this subfamily.

1. Calculate \(Y_b\), and find the unique \(N_b\) with
   \(\binom{N_b-1}b\le Y_b<\binom{N_b}b\). The previously proved
   bounds put \(N_b\) between \(b^3/4\) and \(b^3\); integer binary
   search suffices.
2. Enumerate all binomial representations \(N_b=\binom ij\) with
   \(1\le j\le\lfloor b/3\rfloor\) and \(i-j\ge4\).
3. Test the one residual
   \(D_b=\binom{N_b}b-Y_b\) against \(\binom{i^2}{j^2}\) for these
   representations. A single unequal congruence is already a valid
   exclusion certificate.

Step 2 does not require a cutoff on \(i\). Set
\(m=\min(j,i-j)\). Then \(i\ge2m\) and

\[
\binom{2m}m\le\binom im=N_b.
\]

The central coefficients strictly increase with \(m\), so only finitely
many \(m\) occur. For each \(m\), \(\binom im\) strictly increases in
\(i\ge2m\), so integer binary search finds its sole possible solution.
The two orientations \(j=m\) and \(j=i-m\) are then both checked against
the required inequalities. This exhausts all representations.

The search interval for \(N_b\) does not assume that a solution already
exists. The product comparisons from `lower_branch_reduction.md` apply
directly to this threshold: \(\binom{b^3/4}{b}<Y_b\), and

\[
\frac{\binom{b^3-1}b}{Y_b}
>b(1-b^{-2})^b\ge b-1>1.
\]

For the latter inequality, bound the \(b\) numerator factors of the
outer coefficient below by \(b^3-b\), and use
\((2b-1)!/b!>b^{b-1}\). Consequently
\(b^3/4<N_b\le b^3-1\) independently of the existence of an original
solution.

The generator and verifier in `v4_lower_l1_single_top.py` implement this
procedure. Their binomial-representation searches use different bounds,
and their Lucas congruence calculations use different implementations.
The verifier also checks the exact base inequalities for the universal
factorial lemma. The written induction remains part of the mathematical
proof; these Python checks are not a Lean formalization.

## Executed finite application

For every \(22\le b\le1000\), the exact generator and independent
verifier excluded every L1 solution with \(b\ge3j\). This covers
979 complete \(b\)-families with no arbitrary cutoff on \(i\).

There were 981 candidate binomial representations in total. The only
representations with \(j\ne1\) were

\[
b=50,\quad N_b=76076=\binom{78}{3},
\qquad
b=138,\quad N_b=1703016=\binom{218}{3}.
\]

Every candidate was excluded by a congruence at a prime at most 11.
The verifier reported zero unresolved cases. Its report and the
certificate are `v4_lower_l1_single_top_verification.json` and
`v4_lower_l1_single_top_certificates.json`. The certificate SHA256 is
`f54f1fc428b39974ebeffcce7f252f6cfb41088acddb0cf110468a9dc5264e05`.

Reproduction:

```bash
python3 v4_lower_l1_single_top.py generate --stop 1000
python3 v4_lower_l1_single_top.py verify
```

## Limit

There is always a representation \(N_b=\binom{N_b}{1}\), so finding a
single value \(N_b\) does not by itself prove nonexistence. The residual
test still matters. Nor does verifying a finite range of \(b\) remove
the need for a uniform argument for all \(b\). The part \(b<3j\) is not
covered by this new theorem.
