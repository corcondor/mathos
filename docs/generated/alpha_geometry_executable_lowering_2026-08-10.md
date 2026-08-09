# AlphaGeometry reverse engineering and executable lowering audit (2026-08-10)

## Scope

This cycle tested whether MathOS's typed objects and morphisms actually lower to executable constraints. It did not add benchmark IDs, stored answers, or problem-family answer templates.

## AlphaGeometry findings transferred

The transferable mechanism is not a large geometry vocabulary. AlphaGeometry and AlphaGeometry 2 lower geometric predicates into a few exact elimination coordinates:

- additive distance;
- multiplicative distance represented additively after a logarithmic encoding;
- directed angle;
- separate side conditions for orientation, order, overlap, and non-degeneracy;
- provenance-carrying elimination and dependency traceback.

MathOS now has an exact rational elimination kernel with the same execution shape for `additive`, `log_multiplicative`, and `angle` coordinates. Alpha-renaming, underdetermination, inconsistency, and unproved side conditions are tested. This is a reusable backend kernel, not yet a complete lowerer for every Worker semantic object.

## Implemented lowering repairs

1. Preserved LaTeX structure in the TeX corpus runner. The previous runner destroyed binding structure such as `\cos\frac{2\pi}{11}` before parsing.
2. Corrected false interval extraction from prose containing the substring `in`.
3. Added executable symbolic observations for closed terms, systems with a unique observation, floor/ceiling, nearest integer, positive square root, and units digit.
4. Added typed vector constraints for cross products, affine-subspace intersections, and direction-vector equivalence.
5. Lifted vector execution into `TypedSemanticGraph` as objects, constraints, morphisms, and a query.
6. Added a query-to-term dependency gate. A number appearing in a word problem is no longer executed merely because the prose contains `what is`.
7. Split measurement units from measured objects: for example, `7 cups of sugar` is `unit=cup, object=sugar`, not just `object=cup`.
8. Added per-case timeout and numbered-PDF extraction to the corpus benchmark, so one hard CAS path cannot stop the remaining corpus.

## Quantitative results

### Public 3,574 diagnostic run

Before the query dependency gate, executable lowering changed exact matches from 663 to 672 (18.55% to 18.80%). It also increased wrong answers from 561 to 582, reducing answer precision from 54.17% to 53.59%. This run identified over-execution and is not treated as a final frozen result.

### Calibration after the query dependency gate

On the fixed 358-case calibration partition:

| metric | before | after |
|---|---:|---:|
| answered | 111 | 112 |
| exact | 58 | 59 |
| wrong | 53 | 53 |
| precision | 52.25% | 52.68% |

The one gain was a vector-direction problem. No new calibration error was introduced.

### MATH 700 development audit

This set was inspected during development and is not frozen held-out evidence.

| metric | before | after |
|---|---:|---:|
| answered | 109 | 129 |
| exact | 58 | 73 |
| wrong | 51 | 56 |
| precision | 53.21% | 56.59% |

Fifteen previously unsolved cases became exact and no previously exact case regressed in this audit. Gains came from the same generic operators under changed expressions, including vector operations and closed-term projections.

### Hard Japanese corpora

- Latest local `全問題.tex`: 83 extracted problems. The preserved-TeX run initially labelled three answers as verified, but audit found two generic-CAS false positives. After closing those gates, only the known support-function geometry problem remains a verified answer: effectively 1/83.
- Google Drive contest sample: JMO preliminary mock 12, Tokyo Science mock 5, Tokyo Tech problem-writing-circle mock 5.
- The initial 22-problem Drive run classified every problem but produced zero verified answers. This is direct evidence that long Japanese multi-condition elaboration remains the dominant gap.

The Drive corpus also contains structurally richer paired problem/solution documents, including `素数三角形`, `双曲線とディオファントス`, `積分不等式`, and `三角形と床関数`. Their reusable structures were audited as finite-shape edge quantification, Pell-norm orbits, determinant invariants, integral inequalities, projectivized recurrences, and floor stability. These are typed capability gaps, not stored answer templates.

## Corpus-derived typed vocabulary

The typed kernel now retains `EdgeLength`, `Circumradius`, `Inradius`, `Irrational`, `Floor`, `QuadraticCurve`, and `LinearRecurrence`. For the prime-triangle theorem, it now emits:

```text
constraints:
  Polygon(3,P)
  forall i:Fin(3), Prime(EdgeLength(P,i))
query:
  prove Irrational(Circumradius(P))
```

Previously the same statement compiled to `prove True`. The integer-geometry search variant compiles to an enumeration query over `P`, including `Prime(Circumradius(P) * Inradius(P))`.

## Remaining architectural gap

The production Worker and the Python benchmark are still separate semantic systems. The Worker owns typed hypermorphism search and autonomous synthesis; Python owns most executable public-benchmark lowerers. Backend names in the Worker Atlas are often capability declarations rather than calls into one shared executor. The next structural task is a shared backend contract schema with concrete input terms, side conditions, result terms, and proof provenance.

## Acceptance criteria for the next cycle

1. Cluster corpora by normalized constraint/query signature, not by source or problem ID.
2. Learn or implement a lowerer only on dev clusters.
3. Require alpha-renaming and numeric perturbation invariance.
4. Require side-condition closure before execution.
5. Run a new source- and structure-clustered frozen partition once.
6. Report exact, precision, wrong, abstention, timeout, and first failure layer.
