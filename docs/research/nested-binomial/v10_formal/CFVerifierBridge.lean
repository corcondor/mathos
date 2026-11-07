import Mathlib.Tactic
import CFCurveInstantiation


namespace NestedBinomialV10
theorem int_cross_mul_opposite_signs_implies_hbetween (alpha : ℝ) (P Q Pm Qm : ℤ) (T S : ℕ) (hQ : 0 < Q) (hQsum : 0 < Q + Qm) (hS : 0 < S) (halpha : alpha ^ 3 = (T : ℝ) / (6 * (S : ℝ))) (h : (P ^ 3 * (6 * (S : ℤ)) - (T : ℤ) * Q ^ 3) * ((P + Pm) ^ 3 * (6 * (S : ℤ)) - (T : ℤ) * (Q + Qm) ^ 3) < 0) : (alpha - (P : ℝ) / (Q : ℝ)) * (alpha - ((P + Pm : ℤ) : ℝ) / ((Q + Qm : ℤ) : ℝ)) < 0 := by
  let A : ℤ := P ^ 3 * (6 * (S : ℤ)) - (T : ℤ) * Q ^ 3
  let B : ℤ := (P + Pm) ^ 3 * (6 * (S : ℤ)) - (T : ℤ) * (Q + Qm) ^ 3
  have hAB : A * B < 0 := by simpa [A, B] using h
  let x : ℝ := (P : ℝ) / (Q : ℝ)
  let y : ℝ := ((P + Pm : ℤ) : ℝ) / ((Q + Qm : ℤ) : ℝ)
  have hQpos : (0 : ℝ) < (Q : ℝ) := by exact_mod_cast hQ
  have hSpos : (0 : ℝ) < (S : ℝ) := by exact_mod_cast hS
  have h6Spos : (0 : ℝ) < 6 * (S : ℝ) := mul_pos (by norm_num) hSpos
  have h6Sne : 6 * (S : ℝ) ≠ 0 := ne_of_gt h6Spos
  have hQne : (Q : ℝ) ≠ 0 := ne_of_gt hQpos
  have hQnpos' : (0 : ℝ) < (Q : ℝ) + (Qm : ℝ) := by
    have h' : (0 : ℝ) < ((Q + Qm : ℤ) : ℝ) := by exact_mod_cast hQsum
    push_cast at h'
    exact h'
  have hQnne' : (Q : ℝ) + (Qm : ℝ) ≠ 0 := ne_of_gt hQnpos'
  have hD : (0 : ℝ) < 6 * (S : ℝ) * (Q : ℝ) ^ 3 :=
    mul_pos h6Spos (pow_pos hQpos 3)
  have hDn : (0 : ℝ) < 6 * (S : ℝ) * ((Q : ℝ) + (Qm : ℝ)) ^ 3 :=
    mul_pos h6Spos (pow_pos hQnpos' 3)
  have hden : 6 * (S : ℝ) * (Q : ℝ) ^ 3 ≠ 0 := ne_of_gt hD
  have hdenn : 6 * (S : ℝ) * ((Q : ℝ) + (Qm : ℝ)) ^ 3 ≠ 0 := ne_of_gt hDn
  have hxA : x ^ 3 - alpha ^ 3 =
      (A : ℝ) / (6 * (S : ℝ) * (Q : ℝ) ^ 3) := by
    dsimp [x, A]
    rw [halpha]
    push_cast
    field_simp [hQne, h6Sne, pow_ne_zero 3 hQne, hden]
  have hyB : y ^ 3 - alpha ^ 3 =
      (B : ℝ) / (6 * (S : ℝ) * ((Q : ℝ) + (Qm : ℝ)) ^ 3) := by
    dsimp [y, B]
    rw [halpha]
    push_cast
    field_simp [hQnne', h6Sne, pow_ne_zero 3 hQnne', hdenn]
  rcases mul_neg_iff.mp hAB with ⟨hApos, hBneg⟩ | ⟨hAneg, hBpos⟩
  · have hxpos : 0 < x ^ 3 - alpha ^ 3 := by
      rw [hxA]
      exact div_pos (by exact_mod_cast hApos) hD
    have hyneg : y ^ 3 - alpha ^ 3 < 0 := by
      rw [hyB]
      exact div_neg_of_neg_of_pos (by exact_mod_cast hBneg) hDn
    have hcube : (x ^ 3 - alpha ^ 3) * (y ^ 3 - alpha ^ 3) < 0 :=
      mul_neg_of_pos_of_neg hxpos hyneg
    have hmain := NestedBinomialV10.cube_between_implies_hbetween alpha x y hcube
    simpa [x, y] using hmain
  · have hxneg : x ^ 3 - alpha ^ 3 < 0 := by
      rw [hxA]
      exact div_neg_of_neg_of_pos (by exact_mod_cast hAneg) hD
    have hypos : 0 < y ^ 3 - alpha ^ 3 := by
      rw [hyB]
      exact div_pos (by exact_mod_cast hBpos) hDn
    have hcube : (x ^ 3 - alpha ^ 3) * (y ^ 3 - alpha ^ 3) < 0 :=
      mul_neg_of_neg_of_pos hxneg hypos
    have hmain := NestedBinomialV10.cube_between_implies_hbetween alpha x y hcube
    simpa [x, y] using hmain

theorem verifier_certificate_to_coverage (a : ℕ → ℤ) (ha : ∀ i, 1 ≤ a i) (ha1 : 2 ≤ a 1) (alpha : ℝ) (M : ℕ) (S T n r g p q : ℕ) (hS : 0 < S) (hn : 104 ≤ n) (hr : 3 * n < r) (hcurve : 6 * S * r ^ 3 = T * n * (n - 1) * (n - 2)) (hTlow : 162 * S < T) (hThigh : T < 229 * S) (halpha : alpha ^ 3 = (T : ℝ) / (6 * (S : ℝ))) (hg : 0 < g) (hgeq : g = Nat.gcd r (n - 1)) (hrg : r = g * p) (hxg : n - 1 = g * q) (hcubes : ((contsZ a (M + 1)).1 ^ 3 * (6 * (S : ℤ)) - (T : ℤ) * (contsZ a (M + 1)).2 ^ 3) * (((contsZ a (M + 1)).1 + (contsZ a M).1) ^ 3 * (6 * (S : ℤ)) - (T : ℤ) * ((contsZ a (M + 1)).2 + (contsZ a M).2) ^ 3) < 0) (hqB : (q : ℤ) < (2 : ℤ) ^ (192 * S)) (hBQ : (2 : ℤ) ^ (192 * S) ≤ (contsZ a (M + 1)).2) : ∃ i : ℕ, i < M ∧ (contsZ a (i + 1)).2 ≤ (q : ℤ) ∧ (q : ℤ) < (contsZ a (i + 2)).2 ∧ ∃ a' b c : ℤ, (p : ℤ) = a' * (contsZ a (i + 1)).1 + b * (contsZ a i).1 ∧ (q : ℤ) = a' * (contsZ a (i + 1)).2 + b * (contsZ a i).2 ∧ c = a' - b * a (i + 1) ∧ (p : ℤ) = b * (contsZ a (i + 2)).1 + c * (contsZ a (i + 1)).1 ∧ (q : ℤ) = b * (contsZ a (i + 2)).2 + c * (contsZ a (i + 1)).2 ∧ (a', b) ∈ coefficientCandidates (a (i + 1)) := by
  have hord := NestedBinomialV10.contsZ_den_ordering a ha ha1 M
  have hQpos : (0 : ℤ) < (contsZ a (M + 1)).2 :=
    lt_of_le_of_lt hord.1 hord.2
  have hQsumpos : (0 : ℤ) < (contsZ a (M + 1)).2 + (contsZ a M).2 := by
    omega
  have hbetween :
      (alpha - ((contsZ a (M + 1)).1 : ℝ) / ((contsZ a (M + 1)).2 : ℝ)) *
        (alpha - (((contsZ a (M + 1)).1 + (contsZ a M).1 : ℤ) : ℝ) /
          (((contsZ a (M + 1)).2 + (contsZ a M).2 : ℤ) : ℝ)) < 0 := by
    exact NestedBinomialV10.int_cross_mul_opposite_signs_implies_hbetween
      alpha (contsZ a (M + 1)).1 (contsZ a (M + 1)).2
      (contsZ a M).1 (contsZ a M).2 T S hQpos hQsumpos hS halpha hcubes
  exact NestedBinomialV10.curve_data_to_coverage
    a ha ha1 alpha M S T n r g p q hS hn hr hcurve hTlow hThigh halpha
    hg hgeq hrg hxg hbetween hqB hBQ

#print axioms int_cross_mul_opposite_signs_implies_hbetween
#print axioms verifier_certificate_to_coverage

end NestedBinomialV10
