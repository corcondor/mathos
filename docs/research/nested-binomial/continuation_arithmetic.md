# Uniform structural exclusions after the N=20 certificate

We retain the original squared-index equation

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}.
\]

Write

\[
A=\binom ij,\quad B=\binom{k}{\ell},\quad
X=\binom{i^2}{j^2},\quad Y=\binom{k^2}{\ell^2},\quad
M=\max(j,\ell),\quad t=A-B,\quad r=\min(B,t).
\]

The following previously proved facts are the only prerequisites:

\[
1\le j\le i-2,\qquad 1\le\ell\le k-1,\qquad 1<B<A,
\]

\[
j+2\le r<12M,\qquad t\ge M+2,
\]

and the fully verified exclusion of all solutions with \(M\le20\).
Thus a hypothetical remaining solution has \(M\ge21\).
All deductions below exclude infinite families; they do not extend an arbitrary numerical cutoff.

## 1. Equal lower indices are impossible

**Theorem.** There is no solution with \(j=\ell\).

**Proof.** Put \(j=\ell=m\). We need only consider \(m\ge21\).
The inequality \(A>B\) forces \(i>k\). Since \(B\ge m+2\),
the possibility \(k=m+1\), which would give \(B=m+1\), is excluded.
Hence \(k\ge m+2\), and

\[
B\ge\binom{m+2}{2}.
\]

Pascal's identity gives

\[
t=\binom im-\binom km
\ge\binom{k}{m-1}
\ge\binom{m+2}{3}.
\]

For \(m\ge21\), both lower bounds exceed \(12m\). Indeed

\[
\binom{m+2}{2}-12m
=\frac{m^2-21m+2}{2}>0,
\]

and \(\binom{m+2}{3}\ge\binom{m+2}{2}\) for \(m\ge3\).
Thus \(r>12m\), a contradiction. The range \(m\le20\) was already excluded. \(\square\)

## 2. Complete classification of the lower branch

Assume \(B\le t\), so \(r=B<12M\).
Every remaining solution lies in exactly one of the following two types.

### Type L1: the second lower index is larger

\[
\boxed{\ell>j,\qquad k=\ell+1,\qquad B=\ell+1.}
\]

To see this, suppose \(\ell\ge j\), so \(M=\ell\ge21\).
If \(k\ge\ell+2\), then

\[
B\ge\binom{\ell+2}{2}>12\ell,
\]

contrary to the gap bound. Hence \(k=\ell+1\).
Now \(B=\ell+1\ge j+2\), so \(\ell>j\).

### Type L2: the first lower index is larger

\[
\boxed{j>\ell,\qquad k\ge\ell+2,
\qquad j+2\le\binom{k}{\ell}<12j.}
\]

If \(j\ge\ell\), the possibility \(k=\ell+1\) would give
\(B=\ell+1\le j+1\), impossible. Equal lower indices have just been excluded,
so \(j>\ell\).

For \(\ell=1\), the condition is explicitly

\[
\boxed{j+2\le k<12j.}
\]

For \(\ell\ge2\), both lower arguments \(\ell\) and \(k-\ell\) are at least 2.
Unimodality therefore yields

\[
\binom{k}{2}\le\binom{k}{\ell}<12j,
\]

or equivalently

\[
\boxed{k(k-1)<24j,\qquad 2\le\ell\le k-2.}
\]

In particular, \(k<1+\sqrt{24j}\) in this subcase.
The more general bound \(\binom{k}{\ell}\ge(k/\ell)^\ell\) also gives
\(k<\ell(12j)^{1/\ell}\).

## 3. Equal complements in the upper branch reduce to complement 2

**Theorem.** If \(i-j=k-\ell=d\) and \(t\le B\), a remaining solution must have \(d=2\).

**Proof.** The endpoint exclusions give \(d\ge2\).
By symmetry,

\[
A=\binom id>\binom kd=B,
\]

so \(i>k\), \(j>\ell\), and \(M=j=i-d\).
If \(d\ge3\), the final increment in the binomial row sequence gives

\[
t\ge\binom{i-1}{d-1}
=\binom{M+d-1}{d-1}
\ge\binom{M+2}{2}>12M.
\]

But \(t=r<12M\) in this branch. Thus \(d=2\). \(\square\)

### 3.1 Complement 2: an analytic bound for every \(i\ge256\)

Put \(i=n\), \(j=n-2\), \(k=n-s\), and \(\ell=k-2\).
Here \(n>k\ge3\), \(M=n-2\ge21\), and

\[
A=\frac{n(n-1)}2,\quad B=\frac{k(k-1)}2,\quad
t=\frac{s(2n-s-1)}2,
\]

\[
X=\binom{n^2}{4n-4},\qquad Y=\binom{k^2}{4k-4}.
\]

The function \(\binom{k^2}{4k-4}\) is strictly increasing for \(k\ge3\).
An injection proves this directly: on increasing \(k\) to \(k+1\), there
are \(2k+1\ge4\) new objects, and the lower argument increases by 4;
adjoin four fixed new objects to each old subset. There are also new subsets
not containing those four objects. Consequently \(Y<X\).

If \(s\le4\), then

\[
t\le4n-10<4n-4\le n^2/2
\]

for \(n\ge23\). Thus

\[
\binom At<\binom{n^2}{t}<\binom{n^2}{4n-4}=X,
\]

which already contradicts the equation.

Suppose \(s\ge5\). Put \(t_0=5n-15\), \(q=4n-4\), and \(N=n^2\).
The function \(t(s)=s(2n-s-1)/2\) is increasing for \(1\le s\le n-3\),
so \(t\ge t_0\). Since \(t\le B=A-t\) in the upper branch, \(t\le A/2\).
Therefore

\[
\binom At\ge\binom A{t_0}.
\]

We prove \(\binom A{t_0}>2\binom Nq\) for every \(n\ge256\).
The product formula and \(\log(1-x)\ge-x/(1-x)\), for \(0\le x<1\), give

\[
\binom A{t_0}\ge\frac{A^{t_0}}{t_0!}
\exp\left(-\frac{t_0(t_0-1)}{2(A-t_0+1)}\right).
\]

Using \(\binom Nq\le N^q/q!\) and
\(t_0!/q!\le t_0^{t_0-q}\), together with \(t_0-q=n-11\), yields

\[
\frac{\binom A{t_0}}{\binom Nq}
\ge\left(\frac A N\right)^q
\left(\frac A{t_0}\right)^{n-11}
\exp\left(-\frac{t_0(t_0-1)}{2(A-t_0+1)}\right).
\]

For \(n\ge256\), the loss in the exponential is bounded by

\[
\frac{t_0(t_0-1)}{2(A-t_0+1)}
\le\frac{25n^2}{n^2-11n+32}
\le\frac{25}{1-11/256}<27.
\]

Also \(A/t_0>n/10\), \(A/N=(1-1/n)/2\), and
\((1-1/n)^{4n-4}>e^{-4}\). Hence

\[
\frac{\binom A{t_0}}{\binom Nq}
>e^{-31}2^{-4n+4}\left(\frac n{10}\right)^{n-11}
=e^{-31}2^{-40}\left(\frac n{160}\right)^{n-11}
\ge e^{-31}2^{-40}\left(\frac85\right)^{245}.
\]

The last quantity exceeds 2 by elementary estimates: \(e<3\),
\(8/5>3/2\), and \(3^2>2^3\) imply

\[
e^{-31}2^{-40}\left(\frac85\right)^{245}
>\frac{3^{214}}{2^{285}}>2^{36}>2.
\]

Thus \(\binom At>2X>X+Y\), another contradiction.
This excludes every \(n\ge256\), without numerical approximation.

### 3.2 The remaining finite interval, checked exactly

The only remaining possibilities have \(23\le n\le255\),
\(3\le k<n\), and

\[
M+2\le t=A-B<12M,\qquad t\le B,\qquad M=n-2.
\]

The accompanying `verify_equal_complement_upper.py` enumerates exactly this
finite set and evaluates both sides using Python's arbitrary-precision
`math.comb`. Its executed result is:

| Quantity | Count |
|---|---:|
| Pairs checked | 2,522 |
| Left side smaller than right side | 946 |
| Left side larger than right side | 1,576 |
| Equalities | 0 |

The machine-readable result is in `verification_equal_complement_upper.json`.
This computation has a proved finite scope: \(M\le20\) was covered by the
earlier certificate; \(d\ge3\) is excluded by the theorem above; and
\(n\ge256\) is excluded analytically in Section 3.1.

**Complete conclusion.** There is no solution in the upper branch with

\[
\boxed{i-j=k-\ell.}
\]

Equivalently, every hypothetical solution with equal complements must lie
in the lower branch \(B<A-B\).

## 4. A gap lemma for a single binomial row

**Lemma.** Let \(n\ge12\). Any two distinct values of
\(\binom ns\), with their effective lower indices
\(\min(s,n-s)\) both at least 2, differ by at least \(\binom n2\).

**Proof.** Put \(h=\lfloor n/2\rfloor\). By symmetry, it is enough to bound
the adjacent positive differences

\[
D_s=\binom ns-\binom n{s-1},\qquad 3\le s\le h.
\]

They satisfy

\[
D_s=\binom n{s-1}\frac{n-2s+1}{s},
\qquad
\frac{D_{s+1}}{D_s}
=\frac{(n-s+1)(n-2s-1)}{(s+1)(n-2s+1)}.
\]

The ratio is at least 1 exactly when \((n-2s)^2\ge n+2\).
As \(s\) increases, this condition changes at most once, from true to false.
Thus the difference sequence first increases and then decreases, and its
minimum on the specified interval occurs at an endpoint.

The first endpoint satisfies

\[
D_3=\binom n2\frac{n-5}{3}\ge\binom n2.
\]

For the central endpoint, write
\(C_m=\binom{2m}{m}/(m+1)\) for the Catalan number.
For \(m\ge6\),

\[
C_m\ge m(2m-1).
\]

This follows from \(C_6=132\ge66\) and induction: the Catalan ratio
\(C_{m+1}/C_m=2(2m+1)/(m+2)\) exceeds 3, whereas
\((m+1)(2m+1)/(m(2m-1))<2\).

If \(n=2m\ge12\), then \(D_h=C_m\ge\binom n2\).
If \(n=2m+1\ge13\), then

\[
D_h=\frac{2(2m+1)}{m+2}C_m
\ge m(2m+1)=\binom n2.
\]

The last inequality follows from \(2C_m\ge m(m+2)\), which is weaker
than the displayed Catalan bound. Thus every adjacent gap, and hence every
larger gap, has the required lower bound. \(\square\)

## 5. Equal upper indices force the second lower index to an endpoint

**Theorem.** Every remaining solution with \(i=k=n\) satisfies

\[
\boxed{\ell\in\{1,n-1\},\quad B=n,\quad 2\le j\le n-2,\quad r=n.}
\]

**Proof.** Suppose instead \(2\le\ell\le n-2\).
The already known bound \(j\le n-2\) gives \(M\le n-2\).
Since \(M\ge21\), we have \(n\ge23\).

The inequality \(A>B\), together with \(B\ge\binom n2\), means that
the effective lower index of \(A\) is larger than that of \(B\), and both
are at least 2. The row-gap lemma therefore gives

\[
B\ge\binom n2,\qquad t=A-B\ge\binom n2.
\]

For \(n\ge23\),

\[
\binom n2\ge12(n-2)\ge12M.
\]

Indeed the first inequality is \(n^2-25n+48\ge0\), which is already
positive at \(n=23\) and increasing thereafter. Thus \(r\ge12M\),
a contradiction.

Therefore \(\ell=1\) or \(n-1\), and \(B=n\).
Since \(A>B\), necessarily \(2\le j\le n-2\), and
\(A\ge\binom n2\). Since \(n\ge22\), \(A-n>n\), so \(r=B=n\).
\(\square\)

## 6. Prime and twice-prime equal upper indices are entirely excluded

The congruences used here follow from
\((1+z)^p\equiv1+z^p\pmod p\). Comparing coefficients yields Lucas's
digit formula; only the explicitly displayed special cases are needed.

### 6.1 A prime-power necessary condition

**Theorem.** If a remaining solution has \(i=k=p^a\), with \(p\) prime,
then \(p\mid j\).

**Proof.** The preceding theorem gives \(B=n=p^a\) and
\(\ell=1\) or \(n-1\). Suppose \(p\nmid j\).
The product identity

\[
\binom{p^a}{j}=\frac{p^a}{j}\binom{p^a-1}{j-1}
\]

and Lucas's formula imply \(v_p(A)=a\), since
\(\binom{p^a-1}{j-1}\not\equiv0\pmod p\).
Write \(A=p^a u\), with \(p\nmid u\). Then

\[
\binom A{p^a}\equiv u\not\equiv0\pmod p.
\]

On the other hand, \(p\nmid j\) and \(p\nmid\ell\), so
the identity \(b\binom Nb=N\binom{N-1}{b-1}\) shows that both
\(X\) and \(Y\) are divisible by \(p\). This contradicts the equation.
\(\square\)

For \(a=1\), the allowed \(j\)'s are \(2\le j\le p-2\), so none is
divisible by \(p\). Consequently **there is no solution with \(i=k=p\)**.

### 6.2 Twice a prime

**Theorem.** There is no solution with \(i=k=2p\), with \(p\) prime.

**Proof.** The range \(M\le20\), including \(p=2\), was already excluded.
For any hypothetical remaining solution, \(p\) is odd and the preceding
classification gives \(\ell\in\{1,2p-1\}\), \(B=2p\), and
\(2\le j\le2p-2\).

First suppose \(j\ne p\), and put \(q=\min(j,2p-j)\).
Then \(2\le q\le p-1\), \(A=\binom{2p}{q}\), and

\[
\frac A p
=\frac2q\binom{2p-1}{q-1}
\equiv\frac{2(-1)^{q-1}}q\pmod p.
\]

Let \(a\in\{1,\ldots,p-1\}\) be this nonzero residue.
Lucas's formula gives

\[
\binom A{2p}\equiv\binom a2\pmod p.
\]

Both \(X\) and \(Y\) are divisible by \(p\), because their upper arguments
are \(4p^2\) and their lower arguments are not divisible by \(p\).
Hence \(\binom a2\equiv0\pmod p\), which forces \(a=1\).
It follows that

\[
q\equiv2(-1)^{q-1}\pmod p.
\]

If \(q\) is odd, this requires \(q=2\), a contradiction.
If \(q\) is even, this requires \(q=p-2\), also a contradiction because
\(p-2\) is odd.

Finally suppose \(j=p\). The elementary congruence

\[
A=\binom{2p}{p}
=2\prod_{h=1}^{p-1}\left(1+\frac p h\right)
\equiv2\left(1+p\sum_{h=1}^{p-1}h^{-1}\right)
\equiv2\pmod{p^2}
\]

holds because inversion permutes the nonzero residues and their sum is
0 modulo an odd prime. Lucas therefore gives

\[
\binom A{2p}\equiv0\pmod p,
\qquad
X=\binom{4p^2}{p^2}\equiv4\pmod p,
\qquad Y\equiv0\pmod p.
\]

Since \(p\) is odd, this is a contradiction. All cases are excluded.
\(\square\)

## Scope

These deductions prove complete exclusions for equal lower indices,
equal upper indices that are prime or twice prime, and several structural
restrictions on the remaining lower and upper branches. They do not prove
global nonexistence of the original equation.

The numerical constant 12 is used to keep the proofs independent of any
subsequent improvement of the global gap bound. A proved smaller constant
can only strengthen these conclusions.
