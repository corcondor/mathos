import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith


namespace NestedBinomialV10
theorem defect_pell_dy_sq (n d y : ℕ) (hn : 1 ≤ n) (h : (2 * n - 1) ^ 2 = d * y ^ 2 + 1) : d * y ^ 2 = 4 * (n * (n - 1)) := by
  let m := n - 1
  have hn' : n = m + 1 := by
    dsimp [m]
    omega
  have hm : n - 1 = m := rfl
  have h2 : 2 * n - 1 = 2 * m + 1 := by
    dsimp [m]
    omega
  have hsq : (2 * n - 1) ^ 2 = 4 * (n * (n - 1)) + 1 := by
    calc
      (2 * n - 1) ^ 2 = (2 * m + 1) ^ 2 := by rw [h2]
      _ = 4 * ((m + 1) * m) + 1 := by ring
      _ = 4 * (n * (n - 1)) + 1 := by rw [hm, hn']
  have h' : d * y ^ 2 + 1 = 4 * (n * (n - 1)) + 1 := by
    rw [← h]
    exact hsq
  exact Nat.add_right_cancel h'

theorem defect_pell_coefficient_eq (C K s d : ℕ) (hs : 0 < s) (h : s ^ 2 * d = C * K) : d = C * K / s ^ 2 := by
  rw [← h]
  exact (Nat.div_eq_of_eq_mul_left (pow_pos hs 2) (mul_comm (s ^ 2) d)).symm

theorem defect_pell_d_bound (C K s d : ℕ) (hC : 0 < C) (hs : 0 < s) (h : s ^ 2 * d = C * K) (hK : 927 * K < 10400 * C) : 927 * d < 10400 * C * C := by
  have hs1 : 1 ≤ s := by omega
  have hs2 : 1 ≤ s ^ 2 := by
    calc
      1 = 1 * 1 := by ring
      _ ≤ s * s := Nat.mul_le_mul hs1 hs1
      _ = s ^ 2 := by ring
  have hd_le : d ≤ C * K := by
    calc
      d = 1 * d := by ring
      _ ≤ s ^ 2 * d := Nat.mul_le_mul_right d hs2
      _ = C * K := h
  have h1 : 927 * d ≤ 927 * (C * K) := Nat.mul_le_mul_left 927 hd_le
  have h2 : 927 * (C * K) < 10400 * C * C := by
    calc
      927 * (C * K) = C * (927 * K) := by ring
      _ < C * (10400 * C) := mul_lt_mul_of_pos_left hK hC
      _ = 10400 * C * C := by ring
  exact lt_of_le_of_lt h1 h2

theorem defect_pell_linear (C K s d n r y : ℕ) (hC : 0 < C) (hs : 0 < s) (hCK : s ^ 2 * d = C * K) (hK : K * n * (n - 1) = C * r ^ 2) (hn : 1 ≤ n) (hpell : (2 * n - 1) ^ 2 = d * y ^ 2 + 1) : K * y = 2 * s * r := by
  have hdy : d * y ^ 2 = 4 * (n * (n - 1)) :=
    defect_pell_dy_sq n d y hn hpell
  have h1 : s ^ 2 * (d * y ^ 2) = C * K * y ^ 2 := by
    calc
      s ^ 2 * (d * y ^ 2) = (s ^ 2 * d) * y ^ 2 := by ring
      _ = (C * K) * y ^ 2 := by rw [hCK]
      _ = C * K * y ^ 2 := by ring
  rw [hdy] at h1
  have h2 : K * (s ^ 2 * (4 * (n * (n - 1)))) = 4 * s ^ 2 * (C * r ^ 2) := by
    calc
      K * (s ^ 2 * (4 * (n * (n - 1)))) = 4 * s ^ 2 * (K * n * (n - 1)) := by ring
      _ = 4 * s ^ 2 * (C * r ^ 2) := by rw [hK]
  rw [h1] at h2
  have h3 : C * (K ^ 2 * y ^ 2) = C * (4 * s ^ 2 * r ^ 2) := by
    calc
      C * (K ^ 2 * y ^ 2) = K * (C * K * y ^ 2) := by ring
      _ = 4 * s ^ 2 * (C * r ^ 2) := h2
      _ = C * (4 * s ^ 2 * r ^ 2) := by ring
  have h4 : K ^ 2 * y ^ 2 = 4 * s ^ 2 * r ^ 2 :=
    Nat.mul_left_cancel hC h3
  have hsq : (K * y) ^ 2 = (2 * s * r) ^ 2 := by
    calc
      (K * y) ^ 2 = K ^ 2 * y ^ 2 := by ring
      _ = 4 * s ^ 2 * r ^ 2 := h4
      _ = (2 * s * r) ^ 2 := by ring
  apply le_antisymm
  · by_contra hle
    have hlt : 2 * s * r < K * y := by omega
    have hlt2 : (2 * s * r) ^ 2 < (K * y) ^ 2 := Nat.pow_lt_pow_left hlt (by norm_num)
    rw [hsq] at hlt2
    exact (lt_irrefl _) hlt2
  · by_contra hle
    have hlt : K * y < 2 * s * r := by omega
    have hlt2 : (K * y) ^ 2 < (2 * s * r) ^ 2 := Nat.pow_lt_pow_left hlt (by norm_num)
    rw [hsq] at hlt2
    exact (lt_irrefl _) hlt2

#print axioms defect_pell_dy_sq
#print axioms defect_pell_coefficient_eq
#print axioms defect_pell_d_bound
#print axioms defect_pell_linear

end NestedBinomialV10
