# MathOS-CreativeBench Protocol v0.2

## Research question

Can a system pose mathematically valid, structurally novel, difficult, elegant,
and educationally useful problems, and can measured features explain why blind
human raters perceive some generated problems as unnatural?

Problem solving and problem posing are reported as separate abilities.  A hard
problem is not automatically a creative problem.

## Required output from an authoring system

Each submission must contain:

```text
problem statement in TeX
domain and task
answer or theorem statement
solution or verification artifact
structural family / IR when available
generation and repair trace when available
tool and compute budget
```

Systems are architecture-neutral.  LLMs, symbolic systems, search programs,
and human authors use the same output schema.

## Evaluation layers

### Layer 0: rights and provenance gate

Human problems require one of:

```text
self_authored
permission
licensed
public_domain
research_excerpt
```

Bulk collection from a public website is not accepted as permission.  A site
export supplied by its operator or consent from the authors is preferred.
`research_excerpt` is limited to method-development pilots and cannot satisfy
the 60-problem final-corpus requirement.

### Layer 1: mathematical validity gate

A problem passes only if it is well posed and its claimed result is supported
by at least one independent verifier.  Accepted evidence includes exact CAS
normal forms, exhaustive finite certificates, proof-assistant kernels, or blind
expert verification.  Solver agreement alone is not proof of validity.

Invalid problems receive no creative composite, regardless of difficulty.
Validity is reported as `valid`, `invalid`, or `unknown`.  Missing independent
verification is `unknown`, not evidence that a human problem is invalid.  The
validity rate is computed only over adjudicated (`valid + invalid`) records,
while unknown coverage is reported separately.

### Layer 2: structural novelty

Novelty is measured against a frozen, rights-cleared reference corpus at two
levels:

```text
surface distance: wording and notation
structural distance: family, morphism chain, constraint skeleton, query
```

Changing constants, variable names, or prose while preserving the same
structural signature is counted as a variation, not a new structure.

Novelty is corpus-relative.  It is not a claim that no equivalent problem has
ever appeared in mathematical history.

### Layer 3: challenge

Every valid problem is attempted by the same solver panel under equal tool,
token, and wall-clock budgets.  Human solve rates and times are collected on a
matched subset.  Problem difficulty and solver ability should be jointly fit
with an item-response model after enough observations are available.

Purely expensive arithmetic, excessive casework, and verifier timeouts are
reported separately from conceptual challenge.

### Layer 4: blind human quality

At least five independent ratings per problem are required for a provisional
human-quality score.  Raters do not see author provenance.  The primary fields
are rated from 1 to 5:

```text
naturalness
elegance
surprise
pedagogical_value
```

Source guesses and confidence are collected separately.  A system problem may
be recognizable as synthetic yet still be preferred; source detection is not
the quality score.

### Layer 5: usefulness and transfer

Generated problems are used as a curriculum only after evaluation.  Utility is
the improvement on a frozen held-out solver benchmark, not performance on the
generated family itself.  Training and test structural signatures must be
separated to prevent same-family leakage.

## Blind comparison design

Human and system problems are matched on:

```text
domain
query/output type
ambient dimension
declared syllabus
target difficulty
statement length band
answer format
```

The executable `match_group` encodes domain, query/output type, and ambient
dimension.  For example, `geometry:2d:region` and
`geometry:3d:solid_volume` are not eligible for pairing even when both surface
descriptions use the phrase "passing region".  A missing group match is
reported as a coverage gap rather than forced into a misleading pair.

Pair orientation is randomized.  The evaluator receives only a pair ID and the
two TeX statements.  The source key remains private until ratings are frozen.

## Explaining perceived unnaturalness

The observational stage correlates blind naturalness ratings with preregistered
features:

```text
statement length
number of numeric literals
number of explicit conditions
number of subproblems
proof-obligation count
repair-step count
structural novelty
```

Correlations are descriptive.  Causal claims require matched interventions:

```text
remove one redundant condition
replace arbitrary constants with structurally meaningful constants
reorder or remove scaffolding subproblems
shorten the statement without changing the IR
change a forward-generated problem into an inverse-designed problem
```

Only one feature is changed per intervention.  Raters compare the original and
edited versions blind.

## Splits and contamination control

Reference retrieval, generator development, calibration, and final evaluation
use separate structural-family clusters.  The final human corpus is opened only
once after metrics and thresholds are frozen.  Exact and near-duplicate
structures remain in the same split.

## Reporting

The benchmark reports separate axes:

```text
validity rate
structural novelty
surface novelty
author difficulty rating
naturalness
elegance
surprise
pedagogical value
held-out transfer
valid unique problems per compute budget
```

A single creative composite is withheld until validity and blind human ratings
are present.  Raw axes, confidence intervals, exclusions, and missing-data
coverage remain visible even when a composite is reported.

## v0 observation

The first run contains 37 verified MathOS geometry problems and no human
baseline.  All 37 pass the normal-form validity gate, but they collapse to only
three structural signatures.  This establishes reliable same-family variation,
not broad mathematical creativity.  Human-vs-MathOS conclusions are therefore
explicitly unavailable in v0.

## Minimum v1 acceptance criteria

```text
60 rights-cleared human problems
60 matched MathOS problems
at least 5 blind ratings per problem
at least 3 mathematical domains
independent validity verification
frozen structural reference corpus
public blind-pair file separated from the private source key
solver and author scores reported separately
expected-count gate passes exactly (no silent 54/60 substitution)
```

## Related work used to shape the protocol

- DeepMath-Creative: https://arxiv.org/abs/2505.08744
- MathDuels: https://arxiv.org/abs/2604.21916
- Can LLM generate interesting mathematical research problems?:
  https://arxiv.org/abs/2603.18813
- SAND-Math: https://openreview.net/forum?id=wiXdskuyq9
