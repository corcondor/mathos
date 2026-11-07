import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith


namespace NestedBinomialV10
theorem defect_K_lower_bound (C K n r : ℕ) (hC : 0 < C) (h : C * r ^ 2 = K * n * (n - 1)) (hn : 2 ≤ n) (hr : 3 * n < r) : 9 * C + 1 ≤ K := by
  let m := n - 1
  have hnpos : 0 < n := by omega
  have hmn : m < n := by omega
  have h' : C * r ^ 2 = K * n * m := by
    dsimp [m]
    exact h
  have h3 : (3 * n) ^ 2 < r ^ 2 := Nat.pow_lt_pow_left hr (by norm_num)
  have hr2 : 9 * n ^ 2 < r ^ 2 := by
    calc
      9 * n ^ 2 = (3 * n) ^ 2 := by ring
      _ < r ^ 2 := h3
  have hmain : 9 * C * n ^ 2 < K * n * m := by
    calc
      9 * C * n ^ 2 = C * (9 * n ^ 2) := by ring
      _ < C * r ^ 2 := mul_lt_mul_of_pos_left hr2 hC
      _ = K * n * m := h'
  have hK : 9 * C < K := by
    by_contra hnot
    have hle : K ≤ 9 * C := by omega
    have h1 : K * n * m ≤ 9 * C * n * m := by
      calc
        K * n * m = K * (n * m) := by ring
        _ ≤ (9 * C) * (n * m) := Nat.mul_le_mul_right (n * m) hle
        _ = 9 * C * n * m := by ring
    have hpos : 0 < 9 * C * n := by
      exact Nat.mul_pos (Nat.mul_pos (by norm_num : 0 < 9) hC) hnpos
    have h2 : 9 * C * n * m < 9 * C * n ^ 2 := by
      calc
        9 * C * n * m = m * (9 * C * n) := by ring
        _ < n * (9 * C * n) := mul_lt_mul_of_pos_right hmn hpos
        _ = 9 * C * n ^ 2 := by ring
    exact (lt_irrefl (9 * C * n ^ 2)) (lt_trans hmain (lt_of_le_of_lt h1 h2))
  omega

theorem defect_K_upper_bound (C K n r : ℕ) (hC : 0 < C) (h : C * r ^ 2 = K * n * (n - 1)) (hn : 104 ≤ n) (hr : 3 * r < 10 * n) : 927 * K < 10400 * C := by
  have hsq : 9 * r ^ 2 < 100 * n ^ 2 := by
    have h3 : (3 * r) ^ 2 < (10 * n) ^ 2 := Nat.pow_lt_pow_left hr (by norm_num)
    calc
      9 * r ^ 2 = (3 * r) ^ 2 := by ring
      _ < (10 * n) ^ 2 := h3
      _ = 100 * n ^ 2 := by ring
  have hn1 : 103 * n ≤ 104 * (n - 1) := by omega
  have hsq103 : 927 * r ^ 2 < 10300 * n ^ 2 := by
    calc
      927 * r ^ 2 = 103 * (9 * r ^ 2) := by ring
      _ < 103 * (100 * n ^ 2) := mul_lt_mul_of_pos_left hsq (by norm_num : 0 < 103)
      _ = 10300 * n ^ 2 := by ring
  have h2n : 103 * n ^ 2 ≤ 104 * n * (n - 1) := by
    calc
      103 * n ^ 2 = (103 * n) * n := by ring
      _ ≤ (104 * (n - 1)) * n := Nat.mul_le_mul_right n hn1
      _ = 104 * n * (n - 1) := by ring
  have h2n100 : 10300 * n ^ 2 ≤ 10400 * n * (n - 1) := by
    calc
      10300 * n ^ 2 = 100 * (103 * n ^ 2) := by ring
      _ ≤ 100 * (104 * n * (n - 1)) := Nat.mul_le_mul_left 100 h2n
      _ = 10400 * n * (n - 1) := by ring
  have hcross : 927 * r ^ 2 < 10400 * n * (n - 1) := lt_of_lt_of_le hsq103 h2n100
  have hcrossC : 927 * C * r ^ 2 < 10400 * C * n * (n - 1) := by
    calc
      927 * C * r ^ 2 = C * (927 * r ^ 2) := by ring
      _ < C * (10400 * n * (n - 1)) := mul_lt_mul_of_pos_left hcross hC
      _ = 10400 * C * n * (n - 1) := by ring
  have hleft : 927 * C * r ^ 2 = 927 * K * n * (n - 1) := by
    calc
      927 * C * r ^ 2 = 927 * (C * r ^ 2) := by ring
      _ = 927 * (K * n * (n - 1)) := by rw [h]
      _ = 927 * K * n * (n - 1) := by ring
  have hmain : 927 * K * n * (n - 1) < 10400 * C * n * (n - 1) := by
    rw [← hleft]
    exact hcrossC
  have hmain' : (927 * K) * (n * (n - 1)) < (10400 * C) * (n * (n - 1)) := by
    calc
      (927 * K) * (n * (n - 1)) = 927 * K * n * (n - 1) := by ring
      _ < 10400 * C * n * (n - 1) := hmain
      _ = (10400 * C) * (n * (n - 1)) := by ring
  exact Nat.lt_of_mul_lt_mul_right hmain'

#print axioms defect_K_lower_bound
#print axioms defect_K_upper_bound

end NestedBinomialV10
