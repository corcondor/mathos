# DeepSeekによる数学研究手法の研究

手法の仮説・実験・実測結果を保持する。手法の自己申告は証明ではなく、固定型のLean検証を必要とする。
同じ定理でも逐次試行は文脈が変わるため、因果効果や一般的優越性を証明したとは扱わない。

| 手法 | 種類 | 状態 |
| --- | --- | --- |
| Finite interval-cover certificate for the interrupted Pell covering job | certificate_design | experimental |
| Localize the remaining obstruction in the exact square defect before global Pell search | mathematical_strategy | hypothesis |

## 実測した試行

- finite-cover-certificate / ThirtyCofactorPellCovering-2987558f: 5試行、新規検証 4定理、報告出力 136700トークン。判断: keep。
  DeepSeekの評価: Trial complete and accepted: all four frozen obligations (cofactor_M_cases, L_lower_bound, L_upper_bound, Q_dvd_sq_pair_covering) now pass real Lean (exit 0, only propext/Classical.choice/Quot.sound, no hand edits). The compositional split predicted by the hypothesis held: the M∈{1,2,3,6} case analysis, the two integer inequalities from M·r²=L·n(n−1), and the exact 25-pair disjunction each closed as small arithmetic facts. Only one repair was needed (L_lower_bound attempt 1 failed on type-class synthesis, not on the mathematics; attempt 2 succeeded). The covering list is now machine-checked and is the documented input to the Pell reduction. Limitations: single sequential trial, no matched baseline (baseline was empty), reported tokens (~136.7k completion, ~130.9k reasoning) cover candidate responses only and exclude planner/scope/repair critics; this does not establish causal superiority of the method, and it proves only the covering disjunction, not Q∤r², Pell solvability, or either frozen target.
