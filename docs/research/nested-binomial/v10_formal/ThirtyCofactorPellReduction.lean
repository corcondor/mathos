import Mathlib.Tactic
import ThirtyCofactorPellCovering


namespace NestedBinomialV10
theorem pell_parametrization (M L n r s d : ℕ) (hM : 0 < M) (hL : 0 < L) (hs : 0 < s) (hd : 0 < d) (hdSq : Squarefree d) (hn : 2 ≤ n) (hML : M * L = s ^ 2 * d) (h : M * r ^ 2 = L * n * (n - 1)) : ∃ y : ℕ, 2 * M * r = s * d * y ∧ (2 * n - 1) ^ 2 = d * y ^ 2 + 1 := by
  have hn0 : 0 < n := by omega
  have hn1pos : 0 < n - 1 := by omega
  have hRpos : 0 < L * n * (n - 1) := by
    exact mul_pos (mul_pos hL hn0) hn1pos
  have hMr0 : M * r ≠ 0 := by
    intro hz
    have hz2 : L * n * (n - 1) = 0 := by
      rw [← h]
      calc
        M * r ^ 2 = (M * r) * r := by ring
        _ = 0 := by rw [hz, zero_mul]
    exact (ne_of_gt hRpos) hz2
  have hkey : (M * r) ^ 2 = s ^ 2 * (d * n * (n - 1)) := by
    calc
      (M * r) ^ 2 = M ^ 2 * r ^ 2 := by ring
      _ = M * (M * r ^ 2) := by ring
      _ = M * (L * n * (n - 1)) := by rw [h]
      _ = (M * L) * n * (n - 1) := by ring
      _ = (s ^ 2 * d) * n * (n - 1) := by rw [hML]
      _ = s ^ 2 * (d * n * (n - 1)) := by ring
  have hdiv : s ^ 2 ∣ (M * r) ^ 2 := ⟨d * n * (n - 1), hkey⟩
  have hs_dvd : s ∣ M * r := by
    rw [← Nat.factorization_prime_le_iff_dvd hs.ne' hMr0]
    intro p hp
    have hle : (s ^ 2).factorization p ≤ ((M * r) ^ 2).factorization p :=
      (Nat.factorization_prime_le_iff_dvd (pow_ne_zero 2 hs.ne') (pow_ne_zero 2 hMr0)).mpr hdiv p hp
    have hsq_s : (s ^ 2).factorization p = 2 * s.factorization p := by
      rw [pow_two, Nat.factorization_mul hs.ne' hs.ne', Finsupp.add_apply]
      ring
    have hsq_Mr : ((M * r) ^ 2).factorization p = 2 * (M * r).factorization p := by
      rw [pow_two, Nat.factorization_mul hMr0 hMr0, Finsupp.add_apply]
      ring
    rw [hsq_s, hsq_Mr] at hle
    omega
  obtain ⟨t, ht⟩ := hs_dvd
  have ht_sq : t ^ 2 = d * n * (n - 1) := by
    have h1 : s ^ 2 * t ^ 2 = s ^ 2 * (d * n * (n - 1)) := by
      calc
        s ^ 2 * t ^ 2 = (s * t) ^ 2 := by ring
        _ = (M * r) ^ 2 := by rw [ht]
        _ = s ^ 2 * (d * n * (n - 1)) := hkey
    first
      | exact (Nat.mul_left_cancel (pow_pos hs 2)).mp h1
      | exact Nat.mul_left_cancel (pow_pos hs 2) h1
  have hd_dvd_t2 : d ∣ t ^ 2 := ⟨n * (n - 1), by rw [ht_sq]; ring⟩
  have hd_dvd_t : d ∣ t := (hdSq.dvd_pow_iff_dvd (by norm_num : (2 : ℕ) ≠ 0)).mp hd_dvd_t2
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
  refine ⟨2 * u, ?_, ?_⟩
  · calc
      2 * M * r = 2 * (M * r) := by ring
      _ = 2 * (s * t) := by rw [ht]
      _ = 2 * (s * (d * u)) := by rw [hu]
      _ = s * d * (2 * u) := by ring
  · have hn1le : 1 ≤ n := by omega
    have hdu_sq' : d * u ^ 2 = ((n - 1) + 1) * (n - 1) := by
      simpa [Nat.sub_add_cancel hn1le] using hdu_sq
    have h2n : 2 * n - 1 = 2 * (n - 1) + 1 := by omega
    calc
      (2 * n - 1) ^ 2 = (2 * (n - 1) + 1) ^ 2 := by rw [h2n]
      _ = 4 * (((n - 1) + 1) * (n - 1)) + 1 := by ring
      _ = 4 * (d * u ^ 2) + 1 := by rw [← hdu_sq']
      _ = d * (2 * u) ^ 2 + 1 := by ring

theorem covering_to_pell (n r L : ℕ) (hn : 104 ≤ n) (hrlo : 3 * n < r) (hrhi : 3 * r < 10 * n) (hL : L * ((n / Nat.gcd n 3) * ((n - 1) / Nat.gcd (n - 1) 6)) = r ^ 2) : ∃ s d y : ℕ, 0 < s ∧ 0 < d ∧ 0 < y ∧ Squarefree d ∧ (Nat.gcd n 3 * Nat.gcd (n - 1) 6) * L = s ^ 2 * d ∧ 2 * (Nat.gcd n 3 * Nat.gcd (n - 1) 6) * r = s * d * y ∧ (2 * n - 1) ^ 2 = d * y ^ 2 + 1 := by
  have hrpos : 0 < r := by omega
  have hM : 0 < Nat.gcd n 3 * Nat.gcd (n - 1) 6 := by
    apply mul_pos
    · exact Nat.pos_of_dvd_of_pos (Nat.gcd_dvd_right n 3) (by norm_num)
    · exact Nat.pos_of_dvd_of_pos (Nat.gcd_dvd_right (n - 1) 6) (by norm_num)
  have hLpos : 0 < L := by
    apply Nat.pos_of_ne_zero
    intro hL0
    have hzero : L * ((n / Nat.gcd n 3) * ((n - 1) / Nat.gcd (n - 1) 6)) = 0 := by
      rw [hL0]
      simp
    rw [hL] at hzero
    exact (ne_of_gt (pow_pos hrpos 2)) hzero
  obtain ⟨s, d, hsd, hdSq⟩ :=
    exists_sq_mul_squarefree (Nat.gcd n 3 * Nat.gcd (n - 1) 6 * L)
  have hprod : 0 < Nat.gcd n 3 * Nat.gcd (n - 1) 6 * L := mul_pos hM hLpos
  have hs : 0 < s := by
    apply Nat.pos_of_ne_zero
    intro hs0
    have hzero : s ^ 2 * d = 0 := by
      rw [hs0]
      simp
    rw [hsd] at hzero
    exact (ne_of_gt hprod) hzero
  have hd : 0 < d := by
    apply Nat.pos_of_ne_zero
    intro hd0
    have hzero : s ^ 2 * d = 0 := by
      rw [hd0]
      simp
    rw [hsd] at hzero
    exact (ne_of_gt hprod) hzero
  have hML : Nat.gcd n 3 * Nat.gcd (n - 1) 6 * L = s ^ 2 * d := hsd.symm
  have hEq : Nat.gcd n 3 * Nat.gcd (n - 1) 6 * r ^ 2 = L * n * (n - 1) :=
    NestedBinomialV10.cofactor_M_mul_sq n r L hL
  have hpell := NestedBinomialV10.pell_parametrization
    (Nat.gcd n 3 * Nat.gcd (n - 1) 6) L n r s d
    hM hLpos hs hd hdSq (by omega : 2 ≤ n) hML hEq
  obtain ⟨y, hy1, hy2⟩ := hpell
  have h2Mr : 0 < 2 * (Nat.gcd n 3 * Nat.gcd (n - 1) 6) * r := by
    exact mul_pos (mul_pos (by norm_num) hM) hrpos
  have hy : 0 < y := by
    apply Nat.pos_of_ne_zero
    intro hy0
    have hzero : s * d * y = 0 := by
      rw [hy0]
      simp
    rw [← hy1] at hzero
    exact (ne_of_gt h2Mr) hzero
  exact ⟨s, d, y, hs, hd, hy, hdSq, hML, hy1, hy2⟩

#print axioms pell_parametrization
#print axioms covering_to_pell

end NestedBinomialV10
