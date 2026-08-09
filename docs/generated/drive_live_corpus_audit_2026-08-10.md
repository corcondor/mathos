# Google Drive live mathematics corpus audit (2026-08-10)

## Purpose

Use real contest and problem-writing documents to discover reusable typed objects, morphisms, side conditions, and query contracts. Never branch on a file ID, title, problem number, coefficient, or stored answer.

## Located corpora

- 模試10回分
- 京大模試 2023年度 秋 and its answer document
- 東工大作問サークル模試 (multiple editions)
- 素数三角形
- 双曲線とディオファントス
- 積分不等式
- 三角形と床関数
- 三重三角関数
- 一様分布と相加相乗平均の相関

The repository does not vendor these PDFs. Drive file IDs remain corpus provenance only.

## Four inspected live structures

| document | object/constraint lift | missing executable chain |
|---|---|---|
| 素数三角形 | finite triangle, quantified prime edge lengths, circumradius, irrationality | Heron identity -> square obstruction -> congruence cases -> proof certificate |
| 双曲線とディオファントス | Pell conic, ordered integral points, unit action, arc/chord area | norm orbit -> adjacency proof -> determinant invariant -> exact integral |
| 積分不等式 | definite integral, composed trigonometric term, order goal | range propagation -> inequality selection -> strictness side conditions -> integral bound |
| 三角形と床関数 | positive recurrence, projective ratio, fixed point, triangle inequalities, floor query | recurrence quotient -> convergence -> strict interval -> floor stability |

## Scientific split policy

1. Normalize notation, then cluster by typed constraint/query signature.
2. Keep whole near-duplicate clusters in one partition.
3. Use solution text only to identify missing reusable morphisms and to verify certificates.
4. Do not compile prose fragments, file titles, numerical constants, or final answers into dispatch rules.
5. Run source- and structure-clustered held-out data once after a lowerer is fixed.

## Current result

The corpus exposed an elaboration failure, not a lack of CAS packages. The prime-triangle statement now retains its quantified assumptions and typed conclusion. The other three structures are recognized as capability gaps but are not yet lowered end-to-end, so they remain abstentions rather than fabricated answers.
