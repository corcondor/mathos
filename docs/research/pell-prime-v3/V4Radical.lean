import Mathlib

open Polynomial
namespace PellPrimeV4

-- Newton power-sum polynomial, with the sum fixed and the product variable.
noncomputable def powerSum (t : ℚ) : ℕ → ℚ[X]
  | 0 => C 2
  | 1 => C t
  | n+2 => C t * powerSum t (n+1) - X * powerSum t n

theorem powerSum_degree (t : ℚ) (n : ℕ) :
    (powerSum t n).natDegree ≤ n / 2 := by
  match n with
  | 0 => simp [powerSum]
  | 1 => simp [powerSum]
  | n+2 =>
    rw [powerSum]
    have h₀ := powerSum_degree t n
    have h₁ := powerSum_degree t (n+1)
    apply (natDegree_sub_le _ _).trans
    apply max_le
    · have hh := natDegree_mul_le (p := C t) (q := powerSum t (n+1))
      simp only [natDegree_C, zero_add] at hh
      omega
    · have hh := natDegree_mul_le (p := (X : ℚ[X])) (q := powerSum t n)
      simp only [natDegree_X] at hh
      omega
termination_by n

theorem powerSum_eval (t : ℚ) (a b : ℝ) (ht : a+b=(t:ℝ)) (n : ℕ) :
    aeval (a*b) (powerSum t n) = a^n+b^n := by
  match n with
  | 0 => norm_num [powerSum]
  | 1 => simpa [powerSum] using ht.symm
  | n+2 =>
    simp only [powerSum, map_sub, map_mul, aeval_C, aeval_X]
    rw [powerSum_eval t a b ht (n+1), powerSum_eval t a b ht n]
    change (t:ℝ)*(a^(n+1)+b^(n+1))-a*b*(a^n+b^n)=a^(n+2)+b^(n+2)
    rw [← ht]
    simp only [pow_succ]
    ring
termination_by n

theorem powerSum_at_zero (t : ℚ) (n : ℕ) :
    (powerSum t (n+1)).eval 0 = t^(n+1) := by
  induction n with
  | zero => simp [powerSum]
  | succ n ih =>
    change (powerSum t (n+2)).eval 0 = t^(n+2)
    rw [powerSum]
    simp only [eval_sub, eval_mul, eval_C, eval_X, zero_mul, sub_zero, ih, pow_succ]
    ring

-- The substantive Capelli/minpoly bridge, not a conditional on the desired rationality.
theorem prime_power_small_degree_integral
    (u : ℝ) (s : ℕ) (hs : Nat.Prime s) (ho : Odd s) (c : ℤ)
    (hu : u^s = (c:ℝ)) (P : ℚ[X]) (hP : P ≠ 0)
    (hroot : aeval u P = 0) (hdeg : P.natDegree < s) :
    ∃ z : ℤ, u = (z:ℝ) := by
  classical
  have hq : ∃ q : ℚ, q^s = (c:ℚ) := by
    by_contra hn
    have hirr : Irreducible (X^s-C (c:ℚ)) :=
      X_pow_sub_C_irreducible_of_prime hs (by intro q h; exact hn ⟨q,h⟩)
    have hzero : aeval u (X^s-C (c:ℚ))=0 := by
      simp [hu]
    have hmin : X^s-C (c:ℚ) = minpoly ℚ u :=
      minpoly.eq_of_irreducible_of_monic hirr hzero (monic_X_pow_sub_C _ hs.ne_zero)
    have hle := natDegree_le_of_degree_le (minpoly.degree_le_of_ne_zero ℚ u hP hroot)
    rw [← hmin, natDegree_X_pow_sub_C] at hle
    omega
  obtain ⟨q,hq⟩ := hq
  have hqr : (q:ℝ)^s = (c:ℝ) := by exact_mod_cast hq
  have hqu : (q:ℝ)=u := ho.pow_injective (hqr.trans hu.symm)
  have hint : IsIntegral ℤ (q^s) := by
    rw [hq]
    exact isIntegral_algebraMap
  obtain ⟨z,hz⟩ := IsIntegrallyClosed.exists_algebraMap_eq_of_isIntegral_pow hs.pos hint
  have hz' : (z:ℚ)=q := hz
  exact ⟨z,hqu.symm.trans (by exact_mod_cast hz'.symm)⟩

theorem radical_product_integral (a b : ℝ) (s : ℕ) (hs : Nat.Prime s)
    (ho : Odd s) (t v : ℚ) (c : ℤ)
    (ht : a+b=(t:ℝ)) (hv : a^s+b^s=(v:ℝ))
    (hc : (a*b)^s=(c:ℝ)) (hne : t^s ≠ v) :
    ∃ z : ℤ, a*b=(z:ℝ) := by
  let P := powerSum t s - C v
  have hp : P ≠ 0 := by
    intro h
    have hh := congrArg (fun p : ℚ[X] => p.eval 0) h
    have se : s = (s-1)+1 := by have := hs.pos; omega
    have hz : (powerSum t s).eval 0 = t^s := by
      conv_lhs => rw [se]
      conv_rhs => rw [se]
      exact powerSum_at_zero t (s-1)
    apply hne
    simpa [P, hz, sub_eq_zero] using hh
  have hr : aeval (a*b) P = 0 := by
    simp [P, powerSum_eval t a b ht s, hv]
  have hd : P.natDegree < s := by
    have hh := powerSum_degree t s
    simp only [P, natDegree_sub_C]
    have := hs.pos
    omega
  exact prime_power_small_degree_integral (a*b) s hs ho c hc P hp hr hd

#print axioms powerSum_degree
#print axioms powerSum_eval
#print axioms prime_power_small_degree_integral
#print axioms radical_product_integral
end PellPrimeV4
