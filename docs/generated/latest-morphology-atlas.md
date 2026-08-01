# MathOS モルフォロジー・アトラス

- 型付き表現ノード: **26**
- 許可された隣接射: **25**
- 裸の数値代入による接続: **0**

## 採用条件

異分野候補は隣接する型付き射だけをたどり、各射で数学対象または不変量を明示的に輸送する。
経路の各辺は実際の解法射列と同じ順序で現れ、複数条件が合流する証明DAGを持たなければならない。
条件付き射は必要な前提の証明も要求する。分野名や数値型が一致するだけでは接続と認めない。

## 検証済み経路

二次式の係数から条件付きモーメントまで:

`QuadraticCoefficientFamily -> CoefficientLattice -> DiscriminantFeasibleLattice -> SemialgebraicRegion -> MeasureObservable -> ConditionalMomentObservable`

複素幾何から確率の期待値まで:

`ComplexConfiguration -> CyclicGroupAction -> ResidueClassStructure -> CharacterSum -> GeneratingFunction -> CombinatorialClass -> ProbabilitySpace -> ExpectationObservable`

根の対称式から軌跡と極値まで:

`EuclideanConfiguration -> CoordinateConfiguration -> PolynomialFamily -> RootConfiguration -> SymmetricInvariant -> LocusFamily -> GeometricObservable`

単位根の対蹠点分解から数え上げまで（条件付き）:

`ComplexConfiguration -> RootConfiguration -> SymmetricInvariant -> AntipodalOrbitStructure -> CombinatorialClass -> CardinalityObservable`

遠い分野への直結辺は置かない。条件付きの近道は、その条件を証明した問題だけが利用できる。

## 隣接射一覧

| 始域 | 射 | 終域 | 輸送される意味 | 必要条件 |
|---|---|---|---|---|
| `EuclideanConfiguration` | `CoordinateRealization` | `CoordinateConfiguration` | incidence, metric | - |
| `EuclideanConfiguration` | `ComplexRealization` | `ComplexConfiguration` | incidence, angle, cyclic_order | - |
| `CoordinateConfiguration` | `EquationEncoding` | `PolynomialFamily` | solution_set, multiplicity | - |
| `ComplexConfiguration` | `ComplexRootEncoding` | `RootConfiguration` | point_set, multiplicity, cyclic_order | - |
| `PolynomialFamily` | `RootExtraction` | `RootConfiguration` | solution_set, multiplicity | - |
| `RootConfiguration` | `InvariantQuotient` | `SymmetricInvariant` | symmetry_orbit, multiplicity | - |
| `SymmetricInvariant` | `InvariantLocus` | `LocusFamily` | elementary_symmetric_values, parameter | - |
| `LocusFamily` | `ExtremalObservation` | `GeometricObservable` | locus, feasible_parameter, objective | - |
| `SymmetricInvariant` | `AntipodalFactorization` | `AntipodalOrbitStructure` | root_set, even_polynomial, cyclic_order | unit_roots, four_distinct_roots, vanishing_odd_coefficients |
| `AntipodalOrbitStructure` | `CompatibilityClass` | `CombinatorialClass` | opposite_pairs, compatibility_relation | - |
| `CombinatorialClass` | `CardinalityObservation` | `CardinalityObservable` | class_membership, cardinality | - |
| `QuadraticCoefficientFamily` | `CoefficientInstantiation` | `CoefficientLattice` | coefficients, discriminant | - |
| `CoefficientLattice` | `DiscriminantFilter` | `DiscriminantFeasibleLattice` | coefficients, real_root_existence | - |
| `DiscriminantFeasibleLattice` | `ScalingLimit` | `SemialgebraicRegion` | membership, boundary, density | - |
| `SemialgebraicRegion` | `RegionMeasure` | `MeasureObservable` | membership, boundary | - |
| `MeasureObservable` | `RestrictedMoment` | `ConditionalMomentObservable` | measure, normalization | - |
| `RecurrenceSystem` | `CompanionRepresentation` | `MatrixDynamics` | orbit, initial_state | - |
| `MatrixDynamics` | `SpectralDecomposition` | `SpectralData` | orbit_growth, periodicity | - |
| `ComplexConfiguration` | `CyclicOrbit` | `CyclicGroupAction` | cyclic_order, orbit | - |
| `CyclicGroupAction` | `OrbitResidues` | `ResidueClassStructure` | orbit, period | - |
| `ResidueClassStructure` | `FiniteFourierTransform` | `CharacterSum` | class_membership, period | - |
| `CharacterSum` | `CoefficientEncoding` | `GeneratingFunction` | coefficient_constraint, period | - |
| `GeneratingFunction` | `CoefficientClass` | `CombinatorialClass` | coefficient, size | - |
| `CombinatorialClass` | `UniformMeasure` | `ProbabilitySpace` | sample_space, cardinality | - |
| `ProbabilitySpace` | `Expectation` | `ExpectationObservable` | sample_space, observable | - |
