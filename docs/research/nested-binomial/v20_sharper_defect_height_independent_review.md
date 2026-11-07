# Separate review of the v20 upper gap and exact-defect height

Date: 2026-11-07 JST. The reviewer is a different internal AI task from
the author of `v20_sharper_defect_height.md`. This is not external human
peer review or a Lean-kernel verification.

Reviewed note SHA256:
`8f921aac18023e6f2d9209bfac1a293dbdf6f72a3bb11dabd8857be84d34e0e1`.

**No mathematical gap was found.** The conclusions

\[
t<47n/(100\log n)\quad(n\ge2^{256}),\qquad
\log n<17\delta,\quad n<2^{25\delta}
\]

follow with the stated inherited inputs. In particular, the existing
delta>=25 certificate is used only to handle the entire low-n range;
it does not assume the new upper bound and introduces no circularity.

## Binomial comparison and the integer endpoint

For `a=(3+x)n`, `b=ceil(a)`, the proof has `b<4n` and
`A>n^3/7>16n^2>b^2`. This justifies the product lower bound greater
than 1/2 and also places b strictly below A/2. The factorial integral
upper bound is in the right direction. When using monotonicity of
`y log(eA/y)`, only its numerator expression is replaced; the
denominator `2eb` remains fixed until it is bounded separately.

The independent expansion of the logarithmic comparison gives
exactly the constant `3log2-103/50`. The positive bracket estimate
retains the loss `-3x`, the `-4(3+x)` error, and `-log(4eb)`.
The lower bound `log2>56/81` follows from the stated positive
integrand inequality; all subsequent finite constants pass exact
rational checks.

The conclusion `r<ceil(a)` implies `r<a` for integer r, including
the case of integral a. Both original k branches have the same left
binomial coefficient at r; their inclusion was preserved.

## Exact defect and the change of height

Because `K-9C` is a positive integer, the inequality

\[
\frac{\log n}{C}\le\log n\left(\frac KC-9\right)
\]

is valid without cancelling any residue or assuming coprimality.
The following expression was rederived independently:

\[
\log n\left(\frac{r^2}{n(n-1)}-9\right)
<\frac{(6\alpha+\alpha^2/\log n)n+9\log n}{n-1}.
\]

Both the finite-n denominator correction and the extra `9log n`
are present. The exact resulting coefficient is
`16957941/1000000<17`. For n below `2^256`,
`log n<896/5<425<=17delta` follows from the inherited delta>=25.
Finally `25log2>1400/81>17` gives the binary height.

## Recorded verification

`v20_sharper_defect_height_independent_audit.py` imports neither the
author's checker nor any prior proof generator. It uses SymPy for
three independent coefficient/rational-function identities and exact
Fractions for all finite comparison margins. Its saved report is
`v20_sharper_defect_height_independent_audit.json`, with PASS and no
blocking findings. The universal integral and monotonicity arguments
were read and checked as written proofs; finite samples are not their
justification. No enumeration up to `2^256` was executed or needed.
