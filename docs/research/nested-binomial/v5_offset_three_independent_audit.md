# Independent audit of the offset-three results

## Scope

This audit was performed independently of the author of
`v5_offset_three_structure.md` and `v5_offset_three_three_power.md`.
It checks ordinary mathematical proofs and exact integer calculations;
it is not a Lean formalization.

Both notes retain the original equation

\[
\binom{\binom ij}{\binom{k}{\ell}}
=\binom{i^2}{j^2}+\binom{k^2}{\ell^2}.
\]

In the audited family, \(i=n\), \(j=n-3\), \(\ell=1\),
\(A=\binom n3\), and \(r=\min(k,A-k)\). Both choices
\(k=r\) and \(k=A-r\) are retained.

## Structure note: passed

The following arguments were checked algebraically:

- The comparison \(\binom{n^2}{6n-9}>A^2>k^2\), hence
  \(X<L<2X\), in the previously reduced domain \(n\ge104\).
- The AM--GM product estimate giving the lower gap \(r>3n\),
  including the shifted positive polynomial at \(n=64\), the
  bound \((7/8)^8<3/8\), and the decreasing comparison function.
- The factorial integral estimate giving \(r<10n/3\), including
  the integer constant
  \(125\cdot2^{38}\cdot104^2-216\cdot33^{10}
    =40813869371167016>0\).
- The squarefree and radical consequences of
  \(n/\gcd(n,3)\mid r^3\).
- The Kummer block identity used for the prime-power cases.
- Every valuation case for \(p=2,3,5\) and \(p\ge7\), including
  the normalized cubic residue condition
  \((9v)^3\equiv(-1)^u120\pmod p\).

The hypotheses on the lower bound for \(n\), the integer endpoints,
and the possibility of either outer branch were checked. No
correction was needed.

## Powers of three: passed

The sharper gap \(r<28n/9\) for \(n\ge2^{15}\) was checked,
including the exact comparison

\[
2^{103}-3^{37}5^{19}
=1552720879039172862272697908633>0.
\]

The valuation condition reduces all candidates to
\(a=3h+1\), \(h\ge2\), so this sharper gap covers every
remaining exponent except \(a=7\).

For \(\alpha=3h\), \(q=3^\alpha\), and \(A=qT\), the proof
separates the nine factors with indices divisible by \(q\) before
normalizing their valuation. This yields

\[
\binom{T-1}{9}/3^\alpha\equiv4\pmod9.
\]

Every other factor is a 3-adic unit. The only factors that can affect
their product modulo 9 have index valuation \(\alpha-1\).
Under the sharper gap there are exactly eighteen such indices,
nine in each nonzero class modulo 3 after division by \(q/3\).
Their factors pair to \(7\cdot4\equiv1\pmod9\).
This confirms that no precision is lost by normalizing only the
separated factor.

After the equation is divided by \(3^{2d}\), the first summand
vanishes modulo 9. The second summand becomes \(v^2\) for
both \(k=r\) and \(k=A-r\), because \(h\ge2\). The left
side gives \(4(-1)^r/v\), forcing a unit cube to be \(4\) or
\(-4\) modulo 9. This is impossible.

## Direct integer cross-check of the six exceptional values

For \(a=7\), the six possible values of \(r\) follow from
the proved broad gap and the valuation condition. The table in the
proof was independently checked by calculating the complete integers
\(\binom A r\), not by reusing the normalized product algorithm.

```python
from math import comb

n = 3**7
A = comb(n, 3)
d = 4
scale = 3**(2*d)
for v in range(82, 90):
    if v % 3:
        r = 81*v
        L = comb(A, r)
        assert L % scale == 0
        assert r*r % scale == 0
        assert (A-r)**2 % scale == 0
        print(v, L//scale % 9, r*r//scale % 9,
              (A-r)**2//scale % 9)
```

The exact output is

```text
82 4 1 1
83 7 4 4
85 2 7 7
86 2 7 7
88 7 4 4
89 4 1 1
```

Here \(v_3(X)=12\), while the normalization exponent is 8, so
\(X/3^8\) vanishes modulo 9. Every row therefore contradicts
the equation in either branch.

The audited conclusion is the full infinite-family exclusion

\[
\boxed{i=3^a,\quad j=i-3,\quad\ell=1
\quad\Longrightarrow\quad\text{no solution}.}
\]

The result uses the explicitly cited previous endpoint and small-index
exclusions. It does not assert a solution of the full four-variable
problem.
