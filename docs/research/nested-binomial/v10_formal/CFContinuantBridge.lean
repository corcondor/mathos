import Mathlib.Tactic
import CFCandidateCoverage
def contsZ (a : ℕ → ℤ) : ℕ → ℤ × ℤ
  | 0 => (1, 0)
  | 1 => (a 0, 1)
  | n + 2 => (a (n + 1) * (contsZ a (n + 1)).1 + (contsZ a n).1,
              a (n + 1) * (contsZ a (n + 1)).2 + (contsZ a n).2)

namespace NestedBinomialV10
theorem contsZ_det_coprime (a : ℕ → ℤ) (n : ℕ) : |(contsZ a (n + 1)).1 * (contsZ a n).2 - (contsZ a n).1 * (contsZ a (n + 1)).2| = 1 ∧ Nat.Coprime (Int.natAbs ((contsZ a (n + 1)).1)) (Int.natAbs ((contsZ a (n + 1)).2)) := by
  have det_coprime : ∀ P Q Pm Qm : ℤ, |P * Qm - Pm * Q| = 1 →
      Nat.Coprime (Int.natAbs P) (Int.natAbs Q) := by
    intro P Q Pm Qm h
    have hgP : Nat.gcd (Int.natAbs P) (Int.natAbs Q) ∣ Int.natAbs P :=
      Nat.gcd_dvd_left _ _
    have hgQ : Nat.gcd (Int.natAbs P) (Int.natAbs Q) ∣ Int.natAbs Q :=
      Nat.gcd_dvd_right _ _
    have hgP' : ((Nat.gcd (Int.natAbs P) (Int.natAbs Q) : ℕ) : ℤ) ∣ P :=
      Int.natAbs_dvd_natAbs.mp (by simpa using hgP)
    have hgQ' : ((Nat.gcd (Int.natAbs P) (Int.natAbs Q) : ℕ) : ℤ) ∣ Q :=
      Int.natAbs_dvd_natAbs.mp (by simpa using hgQ)
    have hgcomb : ((Nat.gcd (Int.natAbs P) (Int.natAbs Q) : ℕ) : ℤ) ∣
        P * Qm - Pm * Q :=
      dvd_sub (dvd_mul_of_dvd_left hgP' Qm) (dvd_mul_of_dvd_right hgQ' Pm)
    have hdiff : P * Qm - Pm * Q = 1 ∨ P * Qm - Pm * Q = -1 := by
      rcases lt_trichotomy (P * Qm - Pm * Q) 0 with hneg | hzero | hpos
      · right
        have habs : |P * Qm - Pm * Q| = -(P * Qm - Pm * Q) := abs_of_neg hneg
        rw [habs] at h
        linarith
      · exfalso
        rw [hzero, abs_zero] at h
        exact zero_ne_one h
      · left
        have habs : |P * Qm - Pm * Q| = P * Qm - Pm * Q :=
          abs_of_nonneg (le_of_lt hpos)
        rw [habs] at h
        exact h
    have hg1 : ((Nat.gcd (Int.natAbs P) (Int.natAbs Q) : ℕ) : ℤ) ∣ 1 := by
      rcases hdiff with hD | hD
      · rwa [hD] at hgcomb
      · rw [hD] at hgcomb
        exact dvd_neg.mp hgcomb
    have hg1nat : Nat.gcd (Int.natAbs P) (Int.natAbs Q) ∣ 1 := by
      have h := Int.natAbs_dvd_natAbs.mpr hg1
      simpa using h
    exact Nat.coprime_iff_gcd_eq_one.mpr (Nat.dvd_one.mp hg1nat)
  induction n with
  | zero =>
      have h0 : |(contsZ a (0 + 1)).1 * (contsZ a 0).2 -
          (contsZ a 0).1 * (contsZ a (0 + 1)).2| = 1 := by
        simp [contsZ]
      exact ⟨h0, det_coprime _ _ _ _ h0⟩
  | succ n ih =>
      obtain ⟨hdet, _⟩ := ih
      have hdet' : |(contsZ a (n + 1 + 1)).1 * (contsZ a (n + 1)).2 -
          (contsZ a (n + 1)).1 * (contsZ a (n + 1 + 1)).2| = 1 := by
        rw [show (contsZ a (n + 1 + 1)).1 =
              a (n + 1) * (contsZ a (n + 1)).1 + (contsZ a n).1 from rfl,
            show (contsZ a (n + 1 + 1)).2 =
              a (n + 1) * (contsZ a (n + 1)).2 + (contsZ a n).2 from rfl]
        rw [show
          (a (n + 1) * (contsZ a (n + 1)).1 + (contsZ a n).1) *
              (contsZ a (n + 1)).2 -
            (contsZ a (n + 1)).1 *
              (a (n + 1) * (contsZ a (n + 1)).2 + (contsZ a n).2)
          = -((contsZ a (n + 1)).1 * (contsZ a n).2 -
              (contsZ a n).1 * (contsZ a (n + 1)).2) by ring]
        rw [abs_neg, hdet]
      exact ⟨hdet', det_coprime _ _ _ _ hdet'⟩

theorem contsZ_den_ordering (a : ℕ → ℤ) (ha : ∀ i, 1 ≤ a i) (ha1 : 2 ≤ a 1) (n : ℕ) : 0 ≤ (contsZ a n).2 ∧ (contsZ a n).2 < (contsZ a (n + 1)).2 := by
  let d : Nat → Int := fun n => (contsZ a n).2
  have hrec : ∀ n : Nat, d (n + 2) = a (n + 1) * d (n + 1) + d n := by
    intro n
    dsimp [d]
    rfl
  have hQ : ∀ n : Nat,
      0 ≤ d n ∧ 0 ≤ d (n + 1) ∧ d n < d (n + 1) ∧ (n = 0 ∨ 0 < d n) := by
    intro n
    induction n with
    | zero =>
        have hd0 : d 0 = 0 := by
          dsimp [d]
          rfl
        have hd1 : d 1 = 1 := by
          dsimp [d]
          rfl
        simp [hd0, hd1]
    | succ n ih =>
        obtain ⟨hn0, hn1, hlt, hpos⟩ := ih
        have hpos_next : 0 < d (n + 1) := by linarith
        have hnonneg_next2 : 0 ≤ d (n + 2) := by
          rw [hrec n]
          have ha' : (1 : Int) ≤ a (n + 1) := ha (n + 1)
          have hmul : 0 ≤ a (n + 1) * d (n + 1) :=
            mul_nonneg (by linarith) hn1
          linarith
        have hlt_next : d (n + 1) < d (n + 2) := by
          by_cases hn : n = 0
          · subst n
            have hmain0 : d 1 < d 2 := by
              have hd0 : d 0 = 0 := by
                dsimp [d]
                rfl
              have hd1 : d 1 = 1 := by
                dsimp [d]
                rfl
              calc
                d 1 = 1 := hd1
                _ < a 1 := by linarith
                _ = a 1 * d 1 + d 0 := by rw [hd1, hd0]; ring
                _ = d 2 := by simpa using (hrec 0).symm
            simpa using hmain0
          · have hdnpos : 0 < d n := by
              rcases hpos with hnzero | hp
              · exact False.elim (hn hnzero)
              · exact hp
            have hdiff : d (n + 2) - d (n + 1) =
                (a (n + 1) - 1) * d (n + 1) + d n := by
              rw [hrec n]
              ring
            have ha_ge : (0 : Int) ≤ a (n + 1) - 1 := by
              have h := ha (n + 1)
              linarith
            have hterm : 0 ≤ (a (n + 1) - 1) * d (n + 1) :=
              mul_nonneg ha_ge hn1
            have hdiffpos : 0 < d (n + 2) - d (n + 1) := by
              rw [hdiff]
              linarith
            linarith
        exact ⟨hn1, hnonneg_next2, hlt_next, Or.inr hpos_next⟩
  have hmain := hQ n
  simpa [d] using (show 0 ≤ d n ∧ d n < d (n + 1) from ⟨hmain.1, hmain.2.2.1⟩)

theorem cylinder_error_bounds (a : ℕ → ℤ) (ha : ∀ i, 1 ≤ a i) (ha1 : 2 ≤ a 1) (alpha u : ℝ) (m : ℕ) (hu_lo : (a (m + 1) : ℝ) < u) (hu_hi : u < (a (m + 1) : ℝ) + 1) (hcyl : alpha * (((contsZ a (m + 1)).2 : ℝ) * u + ((contsZ a m).2 : ℝ)) = ((contsZ a (m + 1)).1 : ℝ) * u + ((contsZ a m).1 : ℝ)) : |((contsZ a (m + 1)).2 : ℝ) * alpha - ((contsZ a (m + 1)).1 : ℝ)| < 1 / ((contsZ a (m + 2)).2 : ℝ) ∧ |((contsZ a (m + 2)).2 : ℝ) * alpha - ((contsZ a (m + 2)).1 : ℝ)| < 1 / ((contsZ a (m + 2)).2 : ℝ) := by
  let P0 : ℤ := (contsZ a m).1
  let Q0 : ℤ := (contsZ a m).2
  let P1 : ℤ := (contsZ a (m + 1)).1
  let Q1 : ℤ := (contsZ a (m + 1)).2
  let P2 : ℤ := (contsZ a (m + 2)).1
  let Q2 : ℤ := (contsZ a (m + 2)).2
  have hord0 : 0 ≤ Q0 ∧ Q0 < Q1 := by
    simpa [Q0, Q1] using NestedBinomialV10.contsZ_den_ordering a ha ha1 m
  have hord1 : 0 ≤ Q1 ∧ Q1 < Q2 := by
    simpa [Q1, Q2] using NestedBinomialV10.contsZ_den_ordering a ha ha1 (m + 1)
  have hQ0_nonneg : (0 : ℤ) ≤ Q0 := hord0.1
  have hQ1_pos : (0 : ℤ) < Q1 := lt_of_le_of_lt hQ0_nonneg hord0.2
  have hQ2_pos : (0 : ℤ) < Q2 := lt_of_le_of_lt hord1.1 hord1.2
  have hQ1_posR : (0 : ℝ) < (Q1 : ℝ) := by exact_mod_cast hQ1_pos
  have hQ2_posR : (0 : ℝ) < (Q2 : ℝ) := by exact_mod_cast hQ2_pos
  have hQ0_nonnegR : (0 : ℝ) ≤ (Q0 : ℝ) := by exact_mod_cast hQ0_nonneg
  have hdet0 : |P1 * Q0 - P0 * Q1| = 1 := by
    have h := (NestedBinomialV10.contsZ_det_coprime a m).1
    simpa [P0, Q0, P1, Q1] using h
  have hcyl' : alpha * ((Q1 : ℝ) * u + (Q0 : ℝ)) = (P1 : ℝ) * u + (P0 : ℝ) := by
    simpa [P0, Q0, P1, Q1] using hcyl
  let D : ℝ := (Q1 : ℝ) * u + (Q0 : ℝ)
  have hD_pos : 0 < D := by
    have ha_ge : (1 : ℝ) ≤ (a (m + 1) : ℝ) := by exact_mod_cast ha (m + 1)
    have hu_pos : 0 < u := by linarith [ha_ge, hu_lo]
    dsimp [D]
    have hmul : 0 < (Q1 : ℝ) * u := mul_pos hQ1_posR hu_pos
    linarith [hmul, hQ0_nonnegR]
  have hQ2_eq : (Q2 : ℝ) = (Q1 : ℝ) * (a (m + 1) : ℝ) + (Q0 : ℝ) := by
    have hQ2def : Q2 = a (m + 1) * Q1 + Q0 := by
      dsimp [Q2, Q1, Q0]
      rfl
    rw [hQ2def]
    push_cast
    ring
  have hD_gt_Q2 : (Q2 : ℝ) < D := by
    dsimp [D]
    have hmul : (Q1 : ℝ) * (a (m + 1) : ℝ) < (Q1 : ℝ) * u :=
      mul_lt_mul_of_pos_left hu_lo hQ1_posR
    linarith [hQ2_eq, hmul]
  let E1 : ℝ := (Q1 : ℝ) * alpha - (P1 : ℝ)
  have hE1_eq : E1 = ((Q1 : ℝ) * (P0 : ℝ) - (P1 : ℝ) * (Q0 : ℝ)) / D := by
    have hD_ne : D ≠ 0 := ne_of_gt hD_pos
    rw [eq_div_iff hD_ne]
    dsimp [E1, D]
    calc
      ((Q1 : ℝ) * alpha - (P1 : ℝ)) * ((Q1 : ℝ) * u + (Q0 : ℝ))
          = (Q1 : ℝ) * (alpha * ((Q1 : ℝ) * u + (Q0 : ℝ))) -
              (P1 : ℝ) * ((Q1 : ℝ) * u + (Q0 : ℝ)) := by ring
      _ = (Q1 : ℝ) * ((P1 : ℝ) * u + (P0 : ℝ)) -
              (P1 : ℝ) * ((Q1 : ℝ) * u + (Q0 : ℝ)) := by rw [hcyl']
      _ = (Q1 : ℝ) * (P0 : ℝ) - (P1 : ℝ) * (Q0 : ℝ) := by ring
  have hnum_abs : |(Q1 : ℝ) * (P0 : ℝ) - (P1 : ℝ) * (Q0 : ℝ)| = 1 := by
    have hdetR : |((P1 * Q0 - P0 * Q1 : ℤ) : ℝ)| = 1 := by
      rw [← Int.cast_abs, hdet0]
      norm_num
    have hneg : (Q1 : ℝ) * (P0 : ℝ) - (P1 : ℝ) * (Q0 : ℝ) =
        -(((P1 * Q0 - P0 * Q1 : ℤ) : ℝ)) := by
      push_cast
      ring
    rw [hneg, abs_neg, hdetR]
  have hE1_abs : |E1| = 1 / D := by
    calc
      |E1| = |((Q1 : ℝ) * (P0 : ℝ) - (P1 : ℝ) * (Q0 : ℝ)) / D| := by rw [hE1_eq]
      _ = |(Q1 : ℝ) * (P0 : ℝ) - (P1 : ℝ) * (Q0 : ℝ)| / |D| := by rw [abs_div]
      _ = 1 / D := by rw [hnum_abs, abs_of_pos hD_pos]
  have hE1_lt : |E1| < 1 / (Q2 : ℝ) := by
    rw [hE1_abs]
    have hQ2D_ne : (Q2 : ℝ) * D ≠ 0 :=
      mul_ne_zero (ne_of_gt hQ2_posR) (ne_of_gt hD_pos)
    have hfrac_eq : 1 / (Q2 : ℝ) - 1 / D = (D - (Q2 : ℝ)) / ((Q2 : ℝ) * D) := by
      field_simp [ne_of_gt hQ2_posR, ne_of_gt hD_pos, hQ2D_ne]
    have hfrac_pos : 0 < 1 / (Q2 : ℝ) - 1 / D := by
      rw [hfrac_eq]
      exact div_pos (by linarith) (mul_pos hQ2_posR hD_pos)
    linarith
  have hE0_eq : (Q0 : ℝ) * alpha - (P0 : ℝ) = -u * E1 := by
    dsimp [E1]
    nlinarith [hcyl']
  have hP2_eq : (P2 : ℝ) = (a (m + 1) : ℝ) * (P1 : ℝ) + (P0 : ℝ) := by
    have hP2def : P2 = a (m + 1) * P1 + P0 := by
      dsimp [P2, P1, P0]
      rfl
    rw [hP2def]
    push_cast
    ring
  let E2 : ℝ := (Q2 : ℝ) * alpha - (P2 : ℝ)
  have hE2_eq : E2 = ((a (m + 1) : ℝ) - u) * E1 := by
    calc
      E2 = (a (m + 1) : ℝ) * E1 + ((Q0 : ℝ) * alpha - (P0 : ℝ)) := by
        dsimp [E2, E1]
        rw [hQ2_eq, hP2_eq]
        ring
      _ = ((a (m + 1) : ℝ) - u) * E1 := by
        rw [hE0_eq]
        ring
  have hAu_abs : |(a (m + 1) : ℝ) - u| < 1 := by
    rw [abs_lt]
    constructor <;> linarith
  have hE1_abs_pos : 0 < |E1| := by
    rw [hE1_abs]
    exact div_pos zero_lt_one hD_pos
  have hE2_abs_lt : |E2| < |E1| := by
    rw [hE2_eq, abs_mul]
    calc
      |(a (m + 1) : ℝ) - u| * |E1| < 1 * |E1| :=
        mul_lt_mul_of_pos_right hAu_abs hE1_abs_pos
      _ = |E1| := one_mul _
  have hE2_lt : |E2| < 1 / (Q2 : ℝ) := lt_trans hE2_abs_lt hE1_lt
  constructor
  · simpa [E1, P1, Q1, Q2] using hE1_lt
  · simpa [E2, P2, Q2] using hE2_lt

theorem certificate_coverage_bridge (a : ℕ → ℤ) (ha : ∀ i, 1 ≤ a i) (ha1 : 2 ≤ a 1) (alpha u : ℝ) (m : ℕ) (p q : ℤ) (hu_lo : (a (m + 1) : ℝ) < u) (hu_hi : u < (a (m + 1) : ℝ) + 1) (hcyl : alpha * (((contsZ a (m + 1)).2 : ℝ) * u + ((contsZ a m).2 : ℝ)) = ((contsZ a (m + 1)).1 : ℝ) * u + ((contsZ a m).1 : ℝ)) (hq : 0 < q) (hQm_le_q : (contsZ a (m + 1)).2 ≤ q) (hq_lt_Qn : q < (contsZ a (m + 2)).2) (hred : Nat.Coprime (Int.natAbs p) (Int.natAbs q)) (happrox : |alpha - (p : ℝ) / (q : ℝ)| < 3 / (2 * (q : ℝ) ^ 2)) : ∃ a' b c : ℤ, p = a' * (contsZ a (m + 1)).1 + b * (contsZ a m).1 ∧ q = a' * (contsZ a (m + 1)).2 + b * (contsZ a m).2 ∧ c = a' - b * a (m + 1) ∧ p = b * (contsZ a (m + 2)).1 + c * (contsZ a (m + 1)).1 ∧ q = b * (contsZ a (m + 2)).2 + c * (contsZ a (m + 1)).2 ∧ (a', b) ∈ coefficientCandidates (a (m + 1)) := by
  let P : ℤ := (contsZ a (m + 1)).1
  let Q : ℤ := (contsZ a (m + 1)).2
  let Pm : ℤ := (contsZ a m).1
  let Qm : ℤ := (contsZ a m).2
  let Pn : ℤ := (contsZ a (m + 2)).1
  let Qn : ℤ := (contsZ a (m + 2)).2
  have hordm : 0 ≤ Qm ∧ Qm < Q := by
    simpa [Qm, Q] using NestedBinomialV10.contsZ_den_ordering a ha ha1 m
  have hordn : 0 ≤ Q ∧ Q < Qn := by
    simpa [Q, Qn] using NestedBinomialV10.contsZ_den_ordering a ha ha1 (m + 1)
  have hQ : 0 < Q := lt_of_le_of_lt hordm.1 hordm.2
  have hQn_pos : 0 < Qn := lt_of_le_of_lt hordn.1 hordn.2
  have hQ_le_q : Q ≤ q := by
    simpa [Q] using hQm_le_q
  have hq_lt_Qn' : q < Qn := by
    simpa [Qn] using hq_lt_Qn
  have hdet : |P * Qm - Pm * Q| = 1 := by
    simpa [P, Q, Pm, Qm] using (NestedBinomialV10.contsZ_det_coprime a m).1
  have hcop : Nat.Coprime (Int.natAbs P) (Int.natAbs Q) := by
    simpa [P, Q] using (NestedBinomialV10.contsZ_det_coprime a m).2
  have hPnext : Pn = a (m + 1) * P + Pm := by
    dsimp [Pn, P, Pm]
    rfl
  have hQnext : Qn = a (m + 1) * Q + Qm := by
    dsimp [Qn, Q, Qm]
    rfl
  have hbounds := NestedBinomialV10.cylinder_error_bounds a ha ha1 alpha u m hu_lo hu_hi hcyl
  have hconv_cur : |(Q : ℝ) * alpha - (P : ℝ)| < 1 / (Qn : ℝ) := by
    simpa [P, Q, Qn] using hbounds.1
  have hconv_next : |(Qn : ℝ) * alpha - (Pn : ℝ)| < 1 / (Qn : ℝ) := by
    simpa [Pn, Qn] using hbounds.2
  obtain ⟨a', b, c, h1, h2, h3, h4, h5, h6⟩ :=
    NestedBinomialV10.reduced_approximation_mem_coefficientCandidates
      alpha p q P Q Pm Qm Pn Qn (a (m + 1))
      hq hQ hordm.1 hQn_pos (le_of_lt hordm.2) hQ_le_q hq_lt_Qn'
      hdet hPnext hQnext hred hcop happrox hconv_cur hconv_next
  refine ⟨a', b, c, ?_, ?_, ?_, ?_, ?_, ?_⟩
  · simpa [P, Pm] using h1
  · simpa [Q, Qm] using h2
  · exact h3
  · simpa [Pn, P] using h4
  · simpa [Qn, Q] using h5
  · exact h6

#print axioms contsZ_det_coprime
#print axioms contsZ_den_ordering
#print axioms cylinder_error_bounds
#print axioms certificate_coverage_bridge

end NestedBinomialV10
