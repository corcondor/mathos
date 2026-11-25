import Mathlib
import V4Trace

/-! Exact rank-of-apparition criterion in an arbitrary field containing a
root of the quadratic T^2 - 6T + 1. The characteristic-two case is excluded
for the cross-sign result. No finiteness theorem is assumed. -/
namespace PellOrderV44
open PellTraceV4

theorem H_zero_iff_pow {K : Type*} [Field K] (w : K) (hw : w ≠ 0)
    (h1 : w ≠ 1) (n : ℕ) :
    H (w+w⁻¹) n = 0 ↔ w^(2*n+1) = 1 := by
  constructor
  · intro h
    have hh := H_geometric w hw n
    rw [h, mul_zero] at hh
    exact sub_eq_zero.mp hh.symm
  · exact trace_root_of_unity w n hw h1

theorem order_eq_prime_of_pow {K : Type*} [Field K] {w : K} {s : ℕ}
    (hs : s.Prime) (hw : w ≠ 1) (h : w^s = 1) :
    orderOf w = s := by
  rcases (Nat.dvd_prime hs).mp (orderOf_dvd_of_pow_eq_one h) with h1 | hp
  · exact False.elim (hw (orderOf_eq_one_iff.mp h1))
  · exact hp

theorem H_zero_iff_order {K : Type*} [Field K] (w : K) (hw : w ≠ 0)
    (h1 : w ≠ 1) (n : ℕ) (hs : (2*n+1).Prime) :
    H (w+w⁻¹) n = 0 ↔ orderOf w = 2*n+1 := by
  rw [H_zero_iff_pow w hw h1]
  exact ⟨order_eq_prime_of_pow hs h1, fun h => by
    rw [← h]; exact pow_orderOf_eq_one w⟩

theorem cross_sign_impossible {K : Type*} [Field K] (w : K)
    (h2 : (2:K) ≠ 0) (m n : ℕ)
    (ha : w^(2*m+1) = 1) (hb : (-w)^(2*n+1) = 1) : False := by
  have ho : Odd (2*n+1) := ⟨n, by omega⟩
  rw [ho.neg_pow] at hb
  have hb' : w^(2*n+1) = -1 := by
    calc
      w^(2*n+1) = -(-w^(2*n+1)) := by ring
      _ = -1 := by rw [hb]
  have hm : Odd (2*m+1) := ⟨m, by omega⟩
  have hh : (1:K) = -1 := by
    calc
      1 = (w^(2*m+1))^(2*n+1) := by rw [ha, one_pow]
      _ = (w^(2*n+1))^(2*m+1) := by rw [← pow_mul, ← pow_mul, mul_comm]
      _ = -1 := by rw [hb', hm.neg_one_pow]
  apply h2
  linear_combination hh

-- Fixed w cannot annihilate the same sign for two distinct prime indices.
theorem same_sign_unique {K : Type*} [Field K] (w : K) (hw : w ≠ 0)
    (h1 : w ≠ 1) (m n : ℕ) (hm : (2*m+1).Prime)
    (hn : (2*n+1).Prime)
    (ha : H (w+w⁻¹) m = 0) (hb : H (w+w⁻¹) n = 0) :
    m = n := by
  have hma := (H_zero_iff_order w hw h1 m hm).mp ha
  have hnb := (H_zero_iff_order w hw h1 n hn).mp hb
  omega

theorem H_intCast {K : Type*} [Field K] (z : ℤ) (n : ℕ) :
    ((H z n : ℤ) : K) = H (z : K) n := by
  match n with
  | 0 => simp [H]
  | 1 => simp [H]
  | n+2 =>
    simp only [H, Int.cast_sub, Int.cast_mul, H_intCast z n, H_intCast z (n+1)]
termination_by n

-- The root w = 3+2sqrt(2) has trace 6. Use an abstract trace hypothesis so
-- the same result works for both split and inert residue characteristics.
theorem A_zero_iff_order {K : Type*} [Field K] (w : K) (hw : w ≠ 0)
    (h1 : w ≠ 1) (htrace : w+w⁻¹ = 6)
    (n : ℕ) (hs : (2*n+1).Prime) :
    (A n : K) = 0 ↔ orderOf w = 2*n+1 := by
  unfold A
  rw [H_intCast]
  norm_num only [Int.cast_ofNat]
  rw [← htrace]
  exact H_zero_iff_order w hw h1 n hs

theorem B_zero_iff_order {K : Type*} [Field K] (w : K) (hw : w ≠ 0)
    (hm : -w ≠ 1) (htrace : w+w⁻¹ = 6)
    (n : ℕ) (hs : (2*n+1).Prime) :
    (B n : K) = 0 ↔ orderOf (-w) = 2*n+1 := by
  have ht : -w+(-w)⁻¹ = (-6:K) := by
    rw [inv_neg, ← neg_add, htrace]
  have hb : (B n : K) = (-1:K)^n * H (-6:K) n := by
    unfold B
    push_cast
    simpa using congrArg (fun x : K => (-1:K)^n * x) (H_intCast (K:=K) (-6) n)
  rw [hb]
  have hne : (-1:K)^n ≠ 0 := pow_ne_zero _ (neg_ne_zero.mpr one_ne_zero)
  rw [mul_eq_zero, or_iff_right hne, ← ht]
  exact H_zero_iff_order (-w) (neg_ne_zero.mpr hw) hm n hs

#print axioms H_zero_iff_pow
#print axioms order_eq_prime_of_pow
#print axioms H_zero_iff_order
#print axioms cross_sign_impossible
#print axioms same_sign_unique
#print axioms H_intCast
#print axioms A_zero_iff_order
#print axioms B_zero_iff_order
end PellOrderV44
