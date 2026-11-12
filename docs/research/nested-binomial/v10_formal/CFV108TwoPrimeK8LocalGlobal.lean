import Mathlib.Tactic
import Mathlib.Data.Nat.Choose.Lucas

/-!
# v108: full finite-field root / CRT rejection for the k=8 original branch

Mathematical scope:
* Original fixed branch j=1, ell=k-1, k=8:
  Nat.choose i 8 = i^2 + Nat.choose 64 15.
* The previous v101 real-height theorem supplies 0<i<8^3=512.
* This Lean module formally checks ALL those height-admissible integers at
  once, from Lucas modulo 19 and 59 and a Chinese remainder contradiction.
* It also checks that modulus 17^3 alone has a spurious in-range root
  at i=68, so a claimed universal one-prime exclusion would be false.

Registered in goal_verified_modules.json for the pinned Lean 4.35.0 CI.
The general k-height theorem, the all-k count of large primes, and the
3/5-prime root-free criterion are NOT formalized here.
The proof terms are checked in the pinned Lean toolchain without any proof gaps.
-/

namespace NestedBinomialV108

private theorem choose_mod_19 (i : ℕ) :
    (Nat.choose i 8) % 19 = (Nat.choose (i % 19) 8) % 19 := by
  haveI : Fact (Nat.Prime 19) := ⟨by norm_num⟩
  have h := Choose.choose_modEq_choose_mod_mul_choose_div_nat
    (n := i) (k := 8) (p := 19)
  change (Nat.choose i 8) % 19 =
    (Nat.choose (i % 19) (8 % 19) *
     Nat.choose (i / 19) (8 / 19)) % 19 at h
  simpa using h

private theorem choose_mod_59 (i : ℕ) :
    (Nat.choose i 8) % 59 = (Nat.choose (i % 59) 8) % 59 := by
  haveI : Fact (Nat.Prime 59) := ⟨by norm_num⟩
  have h := Choose.choose_modEq_choose_mod_mul_choose_div_nat
    (n := i) (k := 8) (p := 59)
  change (Nat.choose i 8) % 59 =
    (Nat.choose (i % 59) (8 % 59) *
     Nat.choose (i / 59) (8 / 59)) % 59 at h
  simpa using h

private theorem roots_mod_19 :
    ∀ x : Fin 19,
      (Nat.choose (x : ℕ) 8) % 19 = (x : ℕ) ^ 2 % 19 →
      (x : ℕ) = 0 ∨ (x : ℕ) = 18 := by
  decide

private theorem roots_mod_59 :
    ∀ x : Fin 59,
      (Nat.choose (x : ℕ) 8) % 59 = (x : ℕ) ^ 2 % 59 →
      (x : ℕ) = 0 ∨ (x : ℕ) = 58 := by
  decide

private theorem choose_64_15_mod_19 : (Nat.choose 64 15) % 19 = 0 := by
  decide

private theorem choose_64_15_mod_59 : (Nat.choose 64 15) % 59 = 0 := by
  decide

/-- No positive integer below 8^3=512 satisfies the ORIGINAL equation
for (j,k,ell)=(1,8,7). Uses two modular primes, with no scan over i. -/
theorem k8_original_equation_impossible_below_cubic_height
    (i : ℕ) (hi0 : 0 < i) (hi512 : i < 512)
    (heq : Nat.choose i 8 = i ^ 2 + Nat.choose 64 15) : False := by
  have h19 : (Nat.choose i 8) % 19 = (i ^ 2) % 19 := by
    have h := congrArg (fun t : ℕ => t % 19) heq
    simpa [Nat.add_mod, choose_64_15_mod_19] using h
  have h59 : (Nat.choose i 8) % 59 = (i ^ 2) % 59 := by
    have h := congrArg (fun t : ℕ => t % 59) heq
    simpa [Nat.add_mod, choose_64_15_mod_59] using h
  have h19' : (Nat.choose (i % 19) 8) % 19 =
      ((i % 19) ^ 2) % 19 := by
    calc
      _ = (Nat.choose i 8) % 19 := (choose_mod_19 i).symm
      _ = (i ^ 2) % 19 := h19
      _ = ((i % 19) ^ 2) % 19 := by simp [Nat.pow_mod]
  have h59' : (Nat.choose (i % 59) 8) % 59 =
      ((i % 59) ^ 2) % 59 := by
    calc
      _ = (Nat.choose i 8) % 59 := (choose_mod_59 i).symm
      _ = (i ^ 2) % 59 := h59
      _ = ((i % 59) ^ 2) % 59 := by simp [Nat.pow_mod]
  have hres19 : i % 19 = 0 ∨ i % 19 = 18 := by
    exact roots_mod_19 ⟨i % 19, Nat.mod_lt i (by decide)⟩ h19'
  have hres59 : i % 59 = 0 ∨ i % 59 = 58 := by
    exact roots_mod_59 ⟨i % 59, Nat.mod_lt i (by decide)⟩ h59'
  rcases hres19 with h190 | h191
  · rcases hres59 with h590 | h591 <;> omega
  · rcases hres59 with h590 | h591 <;> omega

/-- Counterexample to the *false* universal assertion that a one-prime
q^3 Hensel lift must automatically lie outside the real height window.
The q=17 local condition is true at i=68, but the original equation is false. -/
theorem k8_spurious_one_prime_root :
    (Nat.choose 68 8) % (17 ^ 3) =
      (68 ^ 2 + Nat.choose 64 15) % (17 ^ 3) ∧
    Nat.choose 68 8 ≠ 68 ^ 2 + Nat.choose 64 15 := by
  decide

#print axioms NestedBinomialV108.k8_original_equation_impossible_below_cubic_height
#print axioms NestedBinomialV108.k8_spurious_one_prime_root

end NestedBinomialV108
