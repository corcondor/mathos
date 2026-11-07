import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Data.Nat.Squarefree
import Mathlib.Data.Nat.Factorization.Basic
import Mathlib.Data.Nat.GCD.Basic
import ThirtyCofactorDefectBridge


namespace NestedBinomialV10
theorem defect_to_pell (M Q n r s d : ℕ) (hM : 0 < M) (hMQ : M * Q = n * (n - 1)) (hn : 104 ≤ n) (hr : 3 * n < r) (hs : 0 < s) (hd : 0 < d) (hdSq : Squarefree d) (hML : (M * (Q / Nat.gcd Q (r ^ 2))) * (r ^ 2 / Nat.gcd Q (r ^ 2)) = s ^ 2 * d) : ∃ y : ℕ, 0 < y ∧ 2 * (M * (Q / Nat.gcd Q (r ^ 2))) * r = s * d * y ∧ (2 * n - 1) ^ 2 = d * y ^ 2 + 1 := by
  let A : ℕ := M * (Q / Nat.gcd Q (r ^ 2))
  let B : ℕ := r ^ 2 / Nat.gcd Q (r ^ 2)
  have hQpos : 0 < Q := by
    have hprod : 0 < M * Q := by
      rw [hMQ]
      exact mul_pos (by omega : 0 < n) (by omega : 0 < n - 1)
    rcases Nat.eq_zero_or_pos Q with hQ0 | hQpos'
    · rw [hQ0, mul_zero] at hprod
      exact (lt_irrefl 0 hprod).elim
    · exact hQpos'
  have hrpos : 0 < r := by omega
  have hg_dvd_Q : Nat.gcd Q (r ^ 2) ∣ Q := Nat.gcd_dvd_left Q (r ^ 2)
  have hg_dvd_r2 : Nat.gcd Q (r ^ 2) ∣ r ^ 2 := Nat.gcd_dvd_right Q (r ^ 2)
  have hgpos : 0 < Nat.gcd Q (r ^ 2) := Nat.pos_of_dvd_of_pos hg_dvd_Q hQpos
  have hgleR : Nat.gcd Q (r ^ 2) ≤ r ^ 2 := Nat.le_of_dvd (pow_pos hrpos 2) hg_dvd_r2
  have hBpos : 0 < B := by
    dsimp [B]
    exact Nat.div_pos hgleR hgpos
  have hAB : A * B = s ^ 2 * d := by
    dsimp [A, B]
    exact hML
  have hAr : A * r ^ 2 = B * n * (n - 1) := by
    dsimp [A, B]
    exact NestedBinomialV10.defect_pell_identity M Q n r hMQ
  have hn0 : 0 < n := by omega
  have hn1pos : 0 < n - 1 := by omega
  have hRpos : 0 < B * n * (n - 1) := by
    exact mul_pos (mul_pos hBpos hn0) hn1pos
  have hAr0 : A * r ≠ 0 := by
    intro hz
    have hz2 : B * n * (n - 1) = 0 := by
      rw [← hAr]
      calc
        A * r ^ 2 = (A * r) * r := by ring
        _ = 0 := by rw [hz, zero_mul]
    exact (ne_of_gt hRpos) hz2
  have hkey : (A * r) ^ 2 = s ^ 2 * (d * n * (n - 1)) := by
    calc
      (A * r) ^ 2 = A ^ 2 * r ^ 2 := by ring
      _ = A * (A * r ^ 2) := by ring
      _ = A * (B * n * (n - 1)) := by rw [hAr]
      _ = (A * B) * n * (n - 1) := by ring
      _ = (s ^ 2 * d) * n * (n - 1) := by rw [hAB]
      _ = s ^ 2 * (d * n * (n - 1)) := by ring
  have hdiv : s ^ 2 ∣ (A * r) ^ 2 := ⟨d * n * (n - 1), hkey⟩
  have hs_dvd : s ∣ A * r := by
    rw [← Nat.factorization_prime_le_iff_dvd hs.ne' hAr0]
    intro p hp
    have hle : (s ^ 2).factorization p ≤ ((A * r) ^ 2).factorization p :=
      (Nat.factorization_prime_le_iff_dvd (pow_ne_zero 2 hs.ne') (pow_ne_zero 2 hAr0)).mpr hdiv p hp
    have hsq_s : (s ^ 2).factorization p = 2 * s.factorization p := by
      rw [pow_two, Nat.factorization_mul hs.ne' hs.ne', Finsupp.add_apply]
      ring
    have hsq_Ar : ((A * r) ^ 2).factorization p = 2 * (A * r).factorization p := by
      rw [pow_two, Nat.factorization_mul hAr0 hAr0, Finsupp.add_apply]
      ring
    rw [hsq_s, hsq_Ar] at hle
    omega
  obtain ⟨t, ht⟩ := hs_dvd
  have ht_sq : t ^ 2 = d * n * (n - 1) := by
    have h1 : s ^ 2 * t ^ 2 = s ^ 2 * (d * n * (n - 1)) := by
      calc
        s ^ 2 * t ^ 2 = (s * t) ^ 2 := by ring
        _ = (A * r) ^ 2 := by rw [ht]
        _ = s ^ 2 * (d * n * (n - 1)) := hkey
    first
      | exact (Nat.mul_left_cancel (pow_pos hs 2)).mp h1
      | exact Nat.mul_left_cancel (pow_pos hs 2) h1
  have hd_dvd_t2 : d ∣ t ^ 2 := ⟨n * (n - 1), by rw [ht_sq]; ring⟩
  have hd_dvd_t : d ∣ t := (hdSq.dvd_pow_iff_dvd (by decide : (2 : ℕ) ≠ 0)).mp hd_dvd_t2
  obtain ⟨u, hu⟩ := hd_dvd_t
  have hdu_sq : d * u ^ 2 = n * (n - 1) := by
    have h1 : d * (d * u ^ 2) = d * (n * (n - 1)) := by
      calc
        d * (d * u ^ 2) = (d * u) ^ 2 := by ring
        _ = t ^ 2 := by rw [hu]
        _ = d * n * (n - 1) := ht_sq
        _ = d * (n * (n - 1)) := by ring
    first
      | exact (Nat.mul_left_cancel hd).mp h1
      | exact Nat.mul_left_cancel hd h1
  have hu_pos : 0 < u := by
    rcases Nat.eq_zero_or_pos u with hu0 | hupos
    · rw [hu0] at hdu_sq
      simp at hdu_sq
      have hnn : 0 < n * (n - 1) := mul_pos hn0 hn1pos
      omega
    · exact hupos
  refine ⟨2 * u, by omega, ?_, ?_⟩
  · have hEq : 2 * A * r = s * d * (2 * u) := by
      calc
        2 * A * r = 2 * (A * r) := by ring
        _ = 2 * (s * t) := by rw [ht]
        _ = 2 * (s * (d * u)) := by rw [hu]
        _ = s * d * (2 * u) := by ring
    dsimp [A] at hEq
    exact hEq
  · have hn1le : 1 ≤ n := by omega
    have hdu_sq' : d * u ^ 2 = ((n - 1) + 1) * (n - 1) := by
      simpa [Nat.sub_add_cancel hn1le] using hdu_sq
    have h2n : 2 * n - 1 = 2 * (n - 1) + 1 := by omega
    calc
      (2 * n - 1) ^ 2 = (2 * (n - 1) + 1) ^ 2 := by rw [h2n]
      _ = 4 * (((n - 1) + 1) * (n - 1)) + 1 := by ring
      _ = 4 * (d * u ^ 2) + 1 := by rw [← hdu_sq']
      _ = d * (2 * u) ^ 2 + 1 := by ring

#print axioms defect_to_pell

end NestedBinomialV10
