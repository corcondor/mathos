import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith


namespace NestedBinomialV10
theorem cube_denominator_dvd (S T u v : ℕ) (hv : 0 < v) (hcop : Nat.Coprime u v) (h : 6 * S * u ^ 3 = T * v ^ 3) : v ^ 3 ∣ 6 * S := by
  have hcop3 : Nat.Coprime (v ^ 3) (u ^ 3) := by
    simpa using hcop.symm
  have hdvd : v ^ 3 ∣ 6 * S * u ^ 3 := by
    rw [h]
    exact ⟨T, mul_comm T (v ^ 3)⟩
  exact hcop3.dvd_of_dvd_mul_right hdvd

theorem cube_ratio_bound (S T u v : ℕ) (hS : 0 < S) (hT : T < 229 * S) (hv : 0 < v) (h : 6 * S * u ^ 3 = T * v ^ 3) : 2 * u < 7 * v := by
  have hmain : 6 * u ^ 3 < 229 * v ^ 3 := by
    have hmul : T * v ^ 3 < (229 * S) * v ^ 3 := by
      have hV : 0 < v ^ 3 := pow_pos hv 3
      have h0 := Nat.mul_lt_mul_of_pos_right hT hV
      simpa [mul_comm] using h0
    have hmul' : S * (6 * u ^ 3) < S * (229 * v ^ 3) := by
      calc
        S * (6 * u ^ 3) = 6 * S * u ^ 3 := by ring
        _ = T * v ^ 3 := h
        _ < (229 * S) * v ^ 3 := hmul
        _ = S * (229 * v ^ 3) := by ring
    exact (Nat.mul_lt_mul_left hS).mp hmul'
  apply Nat.lt_of_not_le
  intro hge
  have hcube : (7 * v) ^ 3 ≤ (2 * u) ^ 3 := Nat.pow_le_pow_left hge 3
  have hcube' : 343 * v ^ 3 ≤ 8 * u ^ 3 := by
    calc
      343 * v ^ 3 = (7 * v) ^ 3 := by ring
      _ ≤ (2 * u) ^ 3 := hcube
      _ = 8 * u ^ 3 := by ring
  have h1 : 24 * u ^ 3 < 916 * v ^ 3 := by linarith [hmain]
  have h2 : 1029 * v ^ 3 ≤ 24 * u ^ 3 := by linarith [hcube']
  have h3 : 1029 * v ^ 3 < 916 * v ^ 3 := lt_of_le_of_lt h2 h1
  have h4 : 916 * v ^ 3 < 1029 * v ^ 3 := by
    have hV : 0 < v ^ 3 := pow_pos hv 3
    have h0 := Nat.mul_lt_mul_of_pos_right (by decide : 916 < 1029) hV
    simpa [mul_comm] using h0
  exact Nat.lt_asymm h3 h4

theorem cube_elimination (S T n r u v : ℕ) (hn : 2 ≤ n) (hT : 0 < T) (hcube : 6 * S * u ^ 3 = T * v ^ 3) (hcurve : 6 * S * r ^ 3 = T * n * (n - 1) * (n - 2)) : (v * r) ^ 3 + u ^ 3 * (n - 1) = (u * (n - 1)) ^ 3 := by
  have h1 : (6 * S) * (r ^ 3 * u ^ 3) = T * (n * (n - 1) * (n - 2) * u ^ 3) := by
    calc
      (6 * S) * (r ^ 3 * u ^ 3) = (6 * S * r ^ 3) * u ^ 3 := by ring
      _ = (T * n * (n - 1) * (n - 2)) * u ^ 3 := by rw [hcurve]
      _ = T * (n * (n - 1) * (n - 2) * u ^ 3) := by ring
  have h2 : (6 * S) * (r ^ 3 * u ^ 3) = T * (v ^ 3 * r ^ 3) := by
    calc
      (6 * S) * (r ^ 3 * u ^ 3) = ((6 * S) * u ^ 3) * r ^ 3 := by ring
      _ = (T * v ^ 3) * r ^ 3 := by rw [hcube]
      _ = T * (v ^ 3 * r ^ 3) := by ring
  have h3 : T * (n * (n - 1) * (n - 2) * u ^ 3) = T * (v ^ 3 * r ^ 3) := by
    calc
      T * (n * (n - 1) * (n - 2) * u ^ 3) = (6 * S) * (r ^ 3 * u ^ 3) := h1.symm
      _ = T * (v ^ 3 * r ^ 3) := h2
  have h4 : n * (n - 1) * (n - 2) * u ^ 3 = v ^ 3 * r ^ 3 :=
    Nat.eq_of_mul_eq_mul_left hT h3
  have hvr : (v * r) ^ 3 = u ^ 3 * (n * (n - 1) * (n - 2)) := by
    calc
      (v * r) ^ 3 = v ^ 3 * r ^ 3 := by ring
      _ = n * (n - 1) * (n - 2) * u ^ 3 := h4.symm
      _ = u ^ 3 * (n * (n - 1) * (n - 2)) := by ring
  have hn2 : n - 2 + 2 = n := Nat.sub_add_cancel hn
  have hB : n * (n - 1) * (n - 2) + (n - 1) = (n - 1) ^ 3 := by
    obtain ⟨k, rfl⟩ : ∃ k, n = k + 2 := ⟨n - 2, hn2.symm⟩
    have hk1 : k + 2 - 1 = k + 1 := by
      have e : k + 2 = (k + 1) + 1 := by ring
      rw [e]
      exact Nat.add_sub_cancel (k + 1) 1
    have hk2 : k + 2 - 2 = k := Nat.add_sub_cancel k 2
    rw [hk1, hk2]
    ring
  calc
    (v * r) ^ 3 + u ^ 3 * (n - 1) = u ^ 3 * (n * (n - 1) * (n - 2)) + u ^ 3 * (n - 1) := by rw [hvr]
    _ = u ^ 3 * (n * (n - 1) * (n - 2) + (n - 1)) := by ring
    _ = u ^ 3 * (n - 1) ^ 3 := by rw [hB]
    _ = (u * (n - 1)) ^ 3 := by ring

theorem rational_cube_root_excluded (S T n r u v : ℕ) (hS1 : 1 ≤ S) (hS : S ≤ 12) (hn : 104 ≤ n) (hT : 0 < T) (hTlt : T < 229 * S) (hv : 0 < v) (hcop : Nat.Coprime u v) (hcube : 6 * S * u ^ 3 = T * v ^ 3) (hcurve : 6 * S * r ^ 3 = T * n * (n - 1) * (n - 2)) : False := by
  have hSpos : 0 < S := by omega
  have hn2 : 2 ≤ n := by omega
  have hxpos : 0 < n - 1 := by omega
  have hu_pos : 0 < u := by
    by_contra h
    have hu0 : u = 0 := by omega
    rw [hu0] at hcube
    simp at hcube
    have hTv : 0 < T * v ^ 3 := Nat.mul_pos hT (pow_pos hv 3)
    omega
  have hr_pos : 0 < r := by
    by_contra h
    have hr0 : r = 0 := by omega
    rw [hr0] at hcurve
    simp at hcurve
    have hnpos : 0 < n := by omega
    have hn1 : 0 < n - 1 := by omega
    have hn2pos : 0 < n - 2 := by omega
    have hR : 0 < T * n * (n - 1) * (n - 2) := by
      exact Nat.mul_pos (Nat.mul_pos (Nat.mul_pos hT hnpos) hn1) hn2pos
    omega
  have hE := cube_elimination S T n r u v hn2 hT hcube hcurve
  let A := u * (n - 1)
  let B := v * r
  let C := u ^ 3 * (n - 1)
  have hE' : B ^ 3 + C = A ^ 3 := by
    simpa [A, B, C] using hE
  have hAB : B < A := by
    by_contra h
    have hle : A ≤ B := Nat.le_of_not_lt h
    have hcubele : A ^ 3 ≤ B ^ 3 := Nat.pow_le_pow_left hle 3
    have hCpos : 0 < C := by
      dsimp [C]
      exact Nat.mul_pos (pow_pos hu_pos 3) hxpos
    have hlt : B ^ 3 < A ^ 3 := by
      calc
        B ^ 3 < B ^ 3 + C := Nat.lt_add_of_pos_right hCpos
        _ = A ^ 3 := hE'
    exact Nat.not_lt_of_ge hcubele hlt
  let d := A - B
  have hdpos : 0 < d := by
    dsimp [d]
    exact Nat.sub_pos_of_lt hAB
  have hd1 : 1 ≤ d := Nat.succ_le_of_lt hdpos
  have hAeq : A = B + d := by
    dsimp [d]
    exact (Nat.add_sub_of_le (le_of_lt hAB)).symm
  have hE'' : B ^ 3 + C = (B + d) ^ 3 := by
    simpa [hAeq] using hE'
  have hfactor : d * ((B + d) ^ 2 + (B + d) * B + B ^ 2) = C := by
    have hpow : (B + d) ^ 3 = B ^ 3 + d * ((B + d) ^ 2 + (B + d) * B + B ^ 2) := by
      ring
    have h : B ^ 3 + C = B ^ 3 + d * ((B + d) ^ 2 + (B + d) * B + B ^ 2) := by
      calc
        B ^ 3 + C = (B + d) ^ 3 := hE''
        _ = B ^ 3 + d * ((B + d) ^ 2 + (B + d) * B + B ^ 2) := hpow
    exact (Nat.add_left_cancel h).symm
  have hBpos : 0 < B := by
    dsimp [B]
    exact Nat.mul_pos hv hr_pos
  have hQpos : 0 < (B + d) * B + B ^ 2 := by
    have h1 : 0 < (B + d) * B := Nat.mul_pos (by omega) hBpos
    have h2 : 0 < B ^ 2 := pow_pos hBpos 2
    omega
  have hQgt : A ^ 2 < (B + d) ^ 2 + (B + d) * B + B ^ 2 := by
    rw [hAeq]
    have h : (B + d) ^ 2 < (B + d) ^ 2 + ((B + d) * B + B ^ 2) :=
      Nat.lt_add_of_pos_right hQpos
    simpa [add_assoc] using h
  have hQleC : (B + d) ^ 2 + (B + d) * B + B ^ 2 ≤ C := by
    calc
      (B + d) ^ 2 + (B + d) * B + B ^ 2
          = 1 * ((B + d) ^ 2 + (B + d) * B + B ^ 2) := by rw [one_mul]
      _ ≤ d * ((B + d) ^ 2 + (B + d) * B + B ^ 2) :=
          Nat.mul_le_mul_right ((B + d) ^ 2 + (B + d) * B + B ^ 2) hd1
      _ = C := hfactor
  have hA2ltC : A ^ 2 < C := lt_of_lt_of_le hQgt hQleC
  have hA2ltC' : (u * (n - 1)) ^ 2 < u ^ 3 * (n - 1) := by
    simpa [A, C] using hA2ltC
  have hu_gt_x : n - 1 < u := by
    have h1 : u ^ 2 * (n - 1) ^ 2 < u ^ 3 * (n - 1) := by
      calc
        u ^ 2 * (n - 1) ^ 2 = (u * (n - 1)) ^ 2 := by ring
        _ < u ^ 3 * (n - 1) := hA2ltC'
    have h2 : u ^ 2 * (n - 1) ^ 2 < (u ^ 2 * (n - 1)) * u := by
      calc
        u ^ 2 * (n - 1) ^ 2 < u ^ 3 * (n - 1) := h1
        _ = (u ^ 2 * (n - 1)) * u := by ring
    have h3 : (u ^ 2 * (n - 1)) * (n - 1) < (u ^ 2 * (n - 1)) * u := by
      calc
        (u ^ 2 * (n - 1)) * (n - 1) = u ^ 2 * (n - 1) ^ 2 := by ring
        _ < (u ^ 2 * (n - 1)) * u := h2
    have hc : 0 < u ^ 2 * (n - 1) := Nat.mul_pos (pow_pos hu_pos 2) hxpos
    exact (Nat.mul_lt_mul_left hc).mp h3
  have hdvd : v ^ 3 ∣ 6 * S := cube_denominator_dvd S T u v hv hcop hcube
  have h6Spos : 0 < 6 * S := by omega
  have hv3le : v ^ 3 ≤ 6 * S := Nat.le_of_dvd h6Spos hdvd
  have h6Sle : 6 * S ≤ 72 := by omega
  have hv3le72 : v ^ 3 ≤ 72 := le_trans hv3le h6Sle
  have hvle4 : v ≤ 4 := by
    by_contra h
    have hv5 : 5 ≤ v := by omega
    have h125 : 125 ≤ v ^ 3 := by
      calc
        125 = 5 ^ 3 := by decide
        _ ≤ v ^ 3 := Nat.pow_le_pow_left hv5 3
    omega
  have hratio : 2 * u < 7 * v := cube_ratio_bound S T u v hSpos hTlt hv hcube
  have hu_le : u ≤ 13 := by omega
  have hxge : 103 ≤ n - 1 := by omega
  have hu_ge : 104 ≤ u := by omega
  omega

#print axioms cube_denominator_dvd
#print axioms cube_ratio_bound
#print axioms cube_elimination
#print axioms rational_cube_root_excluded

end NestedBinomialV10
