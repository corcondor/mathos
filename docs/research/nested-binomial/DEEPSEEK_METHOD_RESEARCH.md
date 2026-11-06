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
- finite-cover-certificate / ThirtyCofactorValuation-4ecb3364: 10試行、新規検証 4定理、報告出力 350029トークン。判断: keep。
  DeepSeekの評価: Trial complete and accepted: all four frozen obligations verified by real Lean (exit 0, only propext/Classical.choice/Quot.sound, no hand edits). The method's decomposition principle transferred only partially, because this job is a valuation identity rather than a finite interval-cover certificate. Goals 1-3 (factorization_mul_prime_pow, factorization_two_of_odd, six_mul_choose_three) closed in 1-2 attempts each, consistent with the small-arithmetic-fact prediction. Goal 4 (factorization_choose_three), the substantive v10 §4 (14) identity with the p=2 parity split, needed 5 attempts, including one full 131072-token reasoning exhaustion (incomplete output) and three proof-gap failures. Reported candidate completion tokens 350029 (reasoning 340091); recorded Lean time 25.439s over 9 timed attempts (1 untimed). No matched baseline exists for this job; the trial is sequential and non-randomized; the method card was designed for finite-cover certificates. This does not establish causal superiority or general effectiveness, and it proves only the valuation identity, not the exponent domain, Q∤r², or either frozen target.
