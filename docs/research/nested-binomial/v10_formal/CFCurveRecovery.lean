import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith


namespace NestedBinomialV10
theorem curve_recovery_identity (S T n r g p q : ℕ) (hn : 2 ≤ n) (hg : 0 < g) (hr : r = g * p) (hq : n - 1 = g * q) (h : 6 * S * r ^ 3 = T * n * (n - 1) * (n - 2)) : T * q + 6 * S * g ^ 2 * p ^ 3 = T * g ^ 2 * q ^ 3 := by
  have hn_eq : n = g * q + 1 := by omega
  have hgq1 : 1 ≤ g * q := by omega
  have hsub : n - 2 = g * q - 1 := by omega
  have hZ : (6 : ℤ) * (S : ℤ) * (r : ℤ) ^ 3 =
      (T : ℤ) * (n : ℤ) * ((n - 1 : ℕ) : ℤ) * ((n - 2 : ℕ) : ℤ) := by
    have hcast := congrArg (fun x : ℕ => (x : ℤ)) h
    simpa [Nat.cast_mul, Nat.cast_pow] using hcast
  have hrZ : (r : ℤ) = (g : ℤ) * (p : ℤ) := by
    rw [hr]
    simp [Nat.cast_mul]
  have hnZ : (n : ℤ) = (g : ℤ) * (q : ℤ) + 1 := by
    rw [hn_eq]
    simp [Nat.cast_mul]
  have hqZ : ((n - 1 : ℕ) : ℤ) = (g : ℤ) * (q : ℤ) := by
    rw [hq]
    simp [Nat.cast_mul]
  have hsubZ : ((n - 2 : ℕ) : ℤ) = (g : ℤ) * (q : ℤ) - 1 := by
    rw [hsub]
    rw [Nat.cast_sub hgq1]
    simp [Nat.cast_mul]
  have hZfac : (g : ℤ) * (6 * (S : ℤ) * (g : ℤ) ^ 2 * (p : ℤ) ^ 3) =
      (g : ℤ) * ((T : ℤ) * (q : ℤ) * ((g : ℤ) ^ 2 * (q : ℤ) ^ 2 - 1)) := by
    have e1 : (g : ℤ) * (6 * (S : ℤ) * (g : ℤ) ^ 2 * (p : ℤ) ^ 3) =
        (6 : ℤ) * (S : ℤ) * (r : ℤ) ^ 3 := by
      rw [hrZ]
      ring
    have e2 : (6 : ℤ) * (S : ℤ) * (r : ℤ) ^ 3 =
        (T : ℤ) * (n : ℤ) * ((n - 1 : ℕ) : ℤ) * ((n - 2 : ℕ) : ℤ) := hZ
    have e3 : (T : ℤ) * (n : ℤ) * ((n - 1 : ℕ) : ℤ) * ((n - 2 : ℕ) : ℤ) =
        (g : ℤ) * ((T : ℤ) * (q : ℤ) * ((g : ℤ) ^ 2 * (q : ℤ) ^ 2 - 1)) := by
      rw [hnZ, hqZ, hsubZ]
      ring
    calc (g : ℤ) * (6 * (S : ℤ) * (g : ℤ) ^ 2 * (p : ℤ) ^ 3)
        = (6 : ℤ) * (S : ℤ) * (r : ℤ) ^ 3 := e1
      _ = (T : ℤ) * (n : ℤ) * ((n - 1 : ℕ) : ℤ) * ((n - 2 : ℕ) : ℤ) := e2
      _ = (g : ℤ) * ((T : ℤ) * (q : ℤ) * ((g : ℤ) ^ 2 * (q : ℤ) ^ 2 - 1)) := e3
  have hgZ : (g : ℤ) ≠ 0 := by
    exact Nat.cast_ne_zero.mpr (ne_of_gt hg)
  have hcancelZ : (6 : ℤ) * (S : ℤ) * (g : ℤ) ^ 2 * (p : ℤ) ^ 3 =
      (T : ℤ) * (q : ℤ) * ((g : ℤ) ^ 2 * (q : ℤ) ^ 2 - 1) := by
    exact mul_left_cancel₀ hgZ hZfac
  have hfinalZ' : (T : ℤ) * (q : ℤ) + 6 * (S : ℤ) * (g : ℤ) ^ 2 * (p : ℤ) ^ 3 =
      (T : ℤ) * (g : ℤ) ^ 2 * (q : ℤ) ^ 3 := by
    have hc := hcancelZ
    ring_nf at hc ⊢
    linarith
  have hfinalZ : ((T * q + 6 * S * g ^ 2 * p ^ 3 : ℕ) : ℤ) =
      ((T * g ^ 2 * q ^ 3 : ℕ) : ℤ) := by
    simpa [Nat.cast_add, Nat.cast_mul, Nat.cast_pow] using hfinalZ'
  exact Nat.cast_injective hfinalZ

theorem curve_recovery_eq (S T n r g p q : ℕ) (hn : 2 ≤ n) (hg : 0 < g) (hr : r = g * p) (hq : n - 1 = g * q) (h : 6 * S * r ^ 3 = T * n * (n - 1) * (n - 2)) : T * q = g ^ 2 * (T * q ^ 3 - 6 * S * p ^ 3) := by
  have h1 := NestedBinomialV10.curve_recovery_identity S T n r g p q hn hg hr hq h
  have hB : T * g ^ 2 * q ^ 3 - 6 * S * g ^ 2 * p ^ 3 = T * q := by
    rw [← h1]
    simp
  have hfactor : T * g ^ 2 * q ^ 3 - 6 * S * g ^ 2 * p ^ 3 =
      g ^ 2 * (T * q ^ 3 - 6 * S * p ^ 3) := by
    have hA : T * g ^ 2 * q ^ 3 = g ^ 2 * (T * q ^ 3) := by ring
    have hB' : 6 * S * g ^ 2 * p ^ 3 = g ^ 2 * (6 * S * p ^ 3) := by ring
    calc
      T * g ^ 2 * q ^ 3 - 6 * S * g ^ 2 * p ^ 3
          = g ^ 2 * (T * q ^ 3) - g ^ 2 * (6 * S * p ^ 3) := by simp [hA, hB']
      _ = g ^ 2 * (T * q ^ 3 - 6 * S * p ^ 3) := by
        exact (Nat.mul_sub_left_distrib (g ^ 2) (T * q ^ 3) (6 * S * p ^ 3)).symm
  calc
    T * q = T * g ^ 2 * q ^ 3 - 6 * S * g ^ 2 * p ^ 3 := hB.symm
    _ = g ^ 2 * (T * q ^ 3 - 6 * S * p ^ 3) := hfactor

theorem curve_recovery_lt (S T n r g p q : ℕ) (hn : 2 ≤ n) (hg : 0 < g) (hT : 0 < T) (hr : r = g * p) (hq : n - 1 = g * q) (h : 6 * S * r ^ 3 = T * n * (n - 1) * (n - 2)) : 6 * S * p ^ 3 < T * q ^ 3 := by
  have hEq := curve_recovery_eq S T n r g p q hn hg hr hq h
  have hqpos : 0 < q := by
    rcases Nat.eq_zero_or_pos q with hq0 | hqpos
    · subst q
      simp at hq
      omega
    · exact hqpos
  have hTqpos : 0 < T * q := Nat.mul_pos hT hqpos
  have hDpos : 0 < T * q ^ 3 - 6 * S * p ^ 3 := by
    by_contra hnot
    have hDzero : T * q ^ 3 - 6 * S * p ^ 3 = 0 := by omega
    have hzero : T * q = 0 := by
      rw [hEq, hDzero]
      simp
    omega
  omega

theorem curve_recovery_D_dvd (S T n r g p q : ℕ) (hn : 2 ≤ n) (hg : 0 < g) (hT : 0 < T) (hr : r = g * p) (hq : n - 1 = g * q) (h : 6 * S * r ^ 3 = T * n * (n - 1) * (n - 2)) : (T * q ^ 3 - 6 * S * p ^ 3) ∣ T * q := by
  refine ⟨g ^ 2, ?_⟩
  rw [NestedBinomialV10.curve_recovery_eq S T n r g p q hn hg hr hq h]
  exact Nat.mul_comm _ _

#print axioms curve_recovery_identity
#print axioms curve_recovery_eq
#print axioms curve_recovery_lt
#print axioms curve_recovery_D_dvd

end NestedBinomialV10
