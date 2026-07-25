# SemanticRepairLoop v1

- 公開問題数: 477
- split: {'calibration': 95, 'dev': 239, 'heldout': 143}
- calibrated threshold: 4.0
- 昇格した合成規則: 5

## 分割別結果

| split | total | baseline type-checked | baseline lift | repaired type-checked | CF pass | promoted certificate |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| dev | 239 | 33 | 4 | 239 | 194 | 19 |
| calibration | 95 | 11 | 0 | 95 | 79 | 7 |

## 昇格規則

| composition | dev evidence | domains | counterfactual pass |
| --- | ---: | ---: | ---: |
| `edge:Area->Maximum` | 3 | 2 | 100.0% |
| `edge:Area->Minimum` | 3 | 3 | 100.0% |
| `op:Cardinality` | 4 | 3 | 100.0% |
| `op:Maximum` | 5 | 4 | 100.0% |
| `op:Minimum` | 6 | 5 | 100.0% |

解答文・問題ID・完全な表層文型は規則に保存していない。証明書の昇格単位は型付き演算子または演算子間の射である。
