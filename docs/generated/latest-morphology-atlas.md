# MathOS モルフォロジー・アトラス

- 型付き表現ノード: **22**
- 許可された隣接射: **20**
- 裸の数値代入による接続: **0**

## 採用条件

異分野候補は、隣接する型付き射だけをたどり、各射で数学対象または不変量を明示的に輸送し、さらに相互作用する証明DAGの検査を通らなければならない。分野名や数値型が一致するだけでは接続として認めない。

## 検証済み経路

二次式の係数から条件付きモーメントまで:

`QuadraticCoefficientFamily -> CoefficientLattice -> DiscriminantFeasibleLattice -> SemialgebraicRegion -> MeasureObservable -> ConditionalMomentObservable`

複素幾何から確率の期待値まで:

`ComplexConfiguration -> CyclicGroupAction -> ResidueClassStructure -> CharacterSum -> GeneratingFunction -> CombinatorialClass -> ProbabilitySpace -> ExpectationObservable`

後者には、巡回群作用、剰余類、指標和、母関数、組合せクラス、確率空間の中間表現が必要である。幾何から確率への直結辺は存在しない。

## 隣接射一覧

| 始域 | 射 | 終域 | 輸送される意味 |
|---|---|---|---|
| `EuclideanConfiguration` | `CoordinateRealization` | `CoordinateConfiguration` | incidence, metric |
| `EuclideanConfiguration` | `ComplexRealization` | `ComplexConfiguration` | incidence, angle, cyclic_order |
| `CoordinateConfiguration` | `EquationEncoding` | `PolynomialFamily` | solution_set, multiplicity |
| `ComplexConfiguration` | `ComplexRootEncoding` | `RootConfiguration` | point_set, multiplicity, cyclic_order |
| `PolynomialFamily` | `RootExtraction` | `RootConfiguration` | solution_set, multiplicity |
| `RootConfiguration` | `InvariantQuotient` | `SymmetricInvariant` | symmetry_orbit, multiplicity |
| `QuadraticCoefficientFamily` | `CoefficientInstantiation` | `CoefficientLattice` | coefficients, discriminant |
| `CoefficientLattice` | `DiscriminantFilter` | `DiscriminantFeasibleLattice` | coefficients, real_root_existence |
| `DiscriminantFeasibleLattice` | `ScalingLimit` | `SemialgebraicRegion` | membership, boundary, density |
| `SemialgebraicRegion` | `RegionMeasure` | `MeasureObservable` | membership, boundary |
| `MeasureObservable` | `RestrictedMoment` | `ConditionalMomentObservable` | measure, normalization |
| `RecurrenceSystem` | `CompanionRepresentation` | `MatrixDynamics` | orbit, initial_state |
| `MatrixDynamics` | `SpectralDecomposition` | `SpectralData` | orbit_growth, periodicity |
| `ComplexConfiguration` | `CyclicOrbit` | `CyclicGroupAction` | cyclic_order, orbit |
| `CyclicGroupAction` | `OrbitResidues` | `ResidueClassStructure` | orbit, period |
| `ResidueClassStructure` | `FiniteFourierTransform` | `CharacterSum` | class_membership, period |
| `CharacterSum` | `CoefficientEncoding` | `GeneratingFunction` | coefficient_constraint, period |
| `GeneratingFunction` | `CoefficientClass` | `CombinatorialClass` | coefficient, size |
| `CombinatorialClass` | `UniformMeasure` | `ProbabilitySpace` | sample_space, cardinality |
| `ProbabilitySpace` | `Expectation` | `ExpectationObservable` | sample_space, observable |
