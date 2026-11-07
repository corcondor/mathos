import Mathlib.Tactic


namespace NestedBinomialV10
theorem defect_dvd_r (Q r : ℕ) (h : Q ∣ r ^ 3) : Q / Nat.gcd Q (r ^ 2) ∣ r := by
  by_cases hg0 : Nat.gcd Q (r ^ 2) = 0
  · have hr20 : r ^ 2 = 0 := by
      have h1 : Nat.gcd Q (r ^ 2) ∣ r ^ 2 := Nat.gcd_dvd_right Q (r ^ 2)
      rw [hg0] at h1
      rcases h1 with ⟨k, hk⟩
      simpa using hk
    have hr0 : r = 0 := by
      rcases r with _ | k
      · rfl
      · exfalso
        have hpos : 0 < (k + 1) ^ 2 := pow_pos (Nat.succ_pos k) 2
        exact absurd hr20 (ne_of_gt hpos)
    rw [hr0]
    exact dvd_zero _
  · have h4 : Nat.gcd Q (r ^ 2) * r = Nat.gcd (Q * r) (r ^ 3) := by
      have h5 := Nat.gcd_mul_right Q r (r ^ 2)
      exact h5.symm
    have hQdvd : Q ∣ Nat.gcd Q (r ^ 2) * r := by
      have h1 : Q ∣ Q * r := ⟨r, rfl⟩
      have h2 : Q ∣ r ^ 3 := h
      have h3 : Q ∣ Nat.gcd (Q * r) (r ^ 3) := Nat.dvd_gcd h1 h2
      rw [← h4] at h3
      exact h3
    have hQeq : Nat.gcd Q (r ^ 2) * (Q / Nat.gcd Q (r ^ 2)) = Q :=
      Nat.mul_div_cancel' (Nat.gcd_dvd_left Q (r ^ 2))
    have h' : Nat.gcd Q (r ^ 2) * (Q / Nat.gcd Q (r ^ 2)) ∣ Nat.gcd Q (r ^ 2) * r := by
      rw [hQeq]
      exact hQdvd
    exact (Nat.mul_dvd_mul_iff_left (Nat.pos_of_ne_zero hg0)).mp h'

theorem defect_cube_dvd (Q r : ℕ) (h : Q ∣ r ^ 3) : (Q / Nat.gcd Q (r ^ 2)) ^ 3 ∣ Q := by
  by_cases hQ0 : Q = 0
  · subst Q
    simp
  · have hQpos : 0 < Q := Nat.pos_of_ne_zero hQ0
    let g := Nat.gcd Q (r ^ 2)
    let δ := Q / g
    change δ ^ 3 ∣ Q
    have hgdvd : g ∣ Q := Nat.gcd_dvd_left Q (r ^ 2)
    have hgdvd2 : g ∣ r ^ 2 := Nat.gcd_dvd_right Q (r ^ 2)
    have hgpos : 0 < g := by
      by_cases hg0 : g = 0
      · exfalso
        have hdiv : g ∣ Q := hgdvd
        rw [hg0] at hdiv
        rcases hdiv with ⟨k, hk⟩
        have hQzero : Q = 0 := by simpa using hk
        exact hQ0 hQzero
      · exact Nat.pos_of_ne_zero hg0
    have hQeq : g * δ = Q := Nat.mul_div_cancel' hgdvd
    obtain ⟨s, hs⟩ := hgdvd2
    have hgcd : Nat.gcd δ s = 1 := by
      have hg_eq : g = g * Nat.gcd δ s := by
        calc
          g = Nat.gcd Q (r ^ 2) := rfl
          _ = Nat.gcd (g * δ) (g * s) := by rw [← hQeq, ← hs]
          _ = g * Nat.gcd δ s := Nat.gcd_mul_left g δ s
      have h : g * 1 = g * Nat.gcd δ s := by
        simpa using hg_eq
      exact (Nat.mul_left_cancel hgpos h).symm
    have hcop : Nat.Coprime δ s := hgcd
    have hcop2 : Nat.Coprime (δ ^ 2) s := hcop.pow_left 2
    have hδdvd : δ ∣ r := defect_dvd_r Q r h
    obtain ⟨u, hu⟩ := hδdvd
    have hdvd : δ ^ 2 ∣ g * s := by
      refine ⟨u ^ 2, ?_⟩
      rw [← hs, hu]
      ring
    have hδ2dvdg : δ ^ 2 ∣ g := hcop2.dvd_of_dvd_mul_right hdvd
    obtain ⟨v, hv⟩ := hδ2dvdg
    refine ⟨v, ?_⟩
    rw [← hQeq, hv]
    ring

theorem defect_gt_one (Q r : ℕ) (h3 : Q ∣ r ^ 3) (h2 : ¬ Q ∣ r ^ 2) : 1 < Q / Nat.gcd Q (r ^ 2) := by
  have hδdvd : Q / Nat.gcd Q (r ^ 2) ∣ r := defect_dvd_r Q r h3
  have hδ0 : Q / Nat.gcd Q (r ^ 2) ≠ 0 := by
    intro h
    have hr : r = 0 := by
      have h' := hδdvd
      rw [h] at h'
      rcases h' with ⟨k, hk⟩
      simpa using hk
    apply h2
    rw [hr]
    simp
  have hδ1 : Q / Nat.gcd Q (r ^ 2) ≠ 1 := by
    intro h
    have hm := Nat.mul_div_cancel' (Nat.gcd_dvd_left Q (r ^ 2))
    rw [h, Nat.mul_one] at hm
    apply h2
    rw [← hm]
    exact Nat.gcd_dvd_right Q (r ^ 2)
  have hle : 1 ≤ Q / Nat.gcd Q (r ^ 2) := Nat.one_le_iff_ne_zero.mpr hδ0
  exact lt_of_le_of_ne hle (Ne.symm hδ1)

theorem defect_cube_dvd_choose_three (Q r i : ℕ) (h3 : Q ∣ r ^ 3) (hA : Q ∣ Nat.choose i 3) : (Q / Nat.gcd Q (r ^ 2)) ^ 3 ∣ Nat.choose i 3 := by
  exact dvd_trans (defect_cube_dvd Q r h3) hA

#print axioms defect_dvd_r
#print axioms defect_cube_dvd
#print axioms defect_gt_one
#print axioms defect_cube_dvd_choose_three

end NestedBinomialV10
