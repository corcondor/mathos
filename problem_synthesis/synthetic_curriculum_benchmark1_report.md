# Synthetic Curriculum Solver Benchmark

## Summary

- dsl: 37/37 exact=1.0 precision=1.0 wrong=0 abstain=0
- full_tex: 37/37 exact=1.0 precision=1.0 wrong=0 abstain=0
- tex: 37/37 exact=1.0 precision=1.0 wrong=0 abstain=0
- tex_mutation: 37/37 exact=1.0 precision=1.0 wrong=0 abstain=0

## By Task

- dsl:envelope: 5/5 exact=1.0 wrong=0 abstain=0
- dsl:region: 32/32 exact=1.0 wrong=0 abstain=0
- full_tex:envelope: 5/5 exact=1.0 wrong=0 abstain=0
- full_tex:region: 32/32 exact=1.0 wrong=0 abstain=0
- tex:envelope: 5/5 exact=1.0 wrong=0 abstain=0
- tex:region: 32/32 exact=1.0 wrong=0 abstain=0
- tex_mutation:envelope: 5/5 exact=1.0 wrong=0 abstain=0
- tex_mutation:region: 32/32 exact=1.0 wrong=0 abstain=0

## Failure Layers

- none

## Interpretation

This benchmark checks whether generated, verified problems can be fed back to the ordinary MathOS solver.  The DSL mode isolates backend correctness; the TeX mode additionally tests LaTeX/NL parsing and lifting.  A correct answer requires algebraic normal-form equality, not string equality.
