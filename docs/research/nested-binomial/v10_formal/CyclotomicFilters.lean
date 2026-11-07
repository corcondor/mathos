import Mathlib.Tactic

set_option maxRecDepth 1000000
set_option maxHeartbeats 0

/-!
Finite arithmetic certificates for the v10 cyclotomic auxiliary-ring note.
These certify the explicitly listed residue-ring calculations only.
They do not formalize the Eisenstein factorization, the unbounded exponent
reductions, or the complete original binomial equation.
-/
namespace NestedBinomialV10.Cyclotomic

abbrev EPair := ℤ × ℤ

def rawMul (z w : EPair) : EPair :=
  (z.1 * w.1 - z.2 * w.2,
   z.1 * w.2 + z.2 * w.1 - z.2 * w.2)

def mul (m : ℕ) (z w : EPair) : EPair :=
  ((rawMul z w).1 % (m : ℤ), (rawMul z w).2 % (m : ℤ))

def pow (m : ℕ) (z : EPair) : ℕ → EPair
  | 0 => (1, 0)
  | n + 1 => mul m (pow m z n) z

def norm (z : EPair) : ℤ := z.1 ^ 2 - z.1 * z.2 + z.2 ^ 2

def trace (z : EPair) : ℤ := 2 * z.1 - z.2

def gamma2 : EPair := (2, -1)
def gamma4 : EPair := (-1, 2)

def finPair {m : ℕ} (x y : Fin m) : EPair :=
  ((x.val : ℤ), (y.val : ℤ))

/-- All three nonzero elements of the four-element residue field have cube 1. -/
theorem mod2_nonzero_cube :
    ∀ x y : Fin 2, (x.val ≠ 0 ∨ y.val ≠ 0) →
      pow 2 (finPair x y) 3 = (1, 0) := by decide

/-- Neither exact cofactor has the required residue when pi^a is 1. -/
theorem mod2_scalar_obstruction :
    mul 2 gamma2 (1, 0) ≠ (1, 1) ∧
    mul 2 gamma4 (1, 0) ≠ (1, 1) := by decide

/-- Complete exponent residues modulo 3, including the scalar-prime obstruction. -/
theorem mod2_complete_residues :
    ∀ x y : Fin 2, ∀ a : Fin 3,
      (mul 2 gamma2 (pow 2 (finPair x y) a.val) = (1, 1) ∨
       mul 2 gamma4 (pow 2 (finPair x y) a.val) = (1, 1)) →
      a.val ≠ 0 ∧ finPair x y ≠ (1, 0) := by decide

/-- All 24 nonzero elements in R/(5) have order dividing 24. -/
theorem mod5_nonzero_period :
    ∀ x y : Fin 5, (x.val ≠ 0 ∨ y.val ≠ 0) →
      pow 5 (finPair x y) 24 = (1, 0) := by decide

/-- For trace zero, the h=2 branch cannot have omega-coordinate -1
    in any exponent residue not divisible by 4. -/
theorem mod5_trace_zero_branch_two :
    ∀ x y : Fin 5, ∀ a : Fin 24,
      trace (finPair x y) % 5 = 0 → a.val % 4 ≠ 0 →
      (mul 5 gamma2 (pow 5 (finPair x y) a.val)).2 ≠ 4 := by decide

/-- For trace zero and odd exponent, the h=4 branch has constant coordinate 0. -/
theorem mod5_trace_zero_branch_four :
    ∀ x y : Fin 5, ∀ a : Fin 24,
      trace (finPair x y) % 5 = 0 → a.val % 2 = 1 →
      (mul 5 gamma4 (pow 5 (finPair x y) a.val)).1 = 0 := by decide

/-- The scalar cases give the extra condition when 5 divides m. -/
theorem mod5_scalar_branch_two :
    ∀ x : Fin 5, ∀ a : Fin 24,
      x.val ≠ 0 → a.val % 4 ≠ 0 →
      (mul 5 gamma2 (pow 5 ((x.val : ℤ), 0) a.val)).2 = 4 →
      (x.val * x.val) % 5 = 1 := by decide

theorem mod5_scalar_branch_four :
    ∀ x : Fin 5, ∀ a : Fin 24,
      (mul 5 gamma4 (pow 5 ((x.val : ℤ), 0) a.val)).2 = 4 →
      (x.val * x.val) % 5 = 4 := by decide

/-- All units in the split ring R/(7) have order dividing 6. -/
theorem mod7_unit_period :
    ∀ x y : Fin 7, norm (finPair x y) % 7 ≠ 0 →
      pow 7 (finPair x y) 6 = (1, 0) := by decide

theorem mod7_trace_branch_two :
    ∀ x y : Fin 7, ∀ a : Fin 6,
      norm (finPair x y) % 7 ≠ 0 → a.val % 3 ≠ 0 →
      mul 7 gamma2 (pow 7 (finPair x y) a.val) = (2, 6) →
      (trace (finPair x y) ^ 2 - (norm (finPair x y) + 1) ^ 2) % 7 = 0 := by decide

theorem mod7_trace_branch_four :
    ∀ x y : Fin 7, ∀ a : Fin 6,
      norm (finPair x y) % 7 ≠ 0 →
      mul 7 gamma4 (pow 7 (finPair x y) a.val) = (4, 6) →
      (a.val = 1 ∧
        (trace (finPair x y) - (3 + 5 * norm (finPair x y))) % 7 = 0) ∨
      (a.val = 5 ∧
        (trace (finPair x y) - (5 + 3 * norm (finPair x y))) % 7 = 0) := by decide

theorem concrete_primary_norms :
    norm (-5, -3) = 19 ∧ trace (-5, -3) = -7 ∧
    norm (1, 6) = 31 ∧ trace (1, 6) = -4 ∧
    norm (-2, -9) = 67 ∧ trace (-2, -9) = 5 ∧
    norm (13, -9) = 367 ∧ trace (13, -9) = 35 := by
  norm_num [norm, trace]

theorem q19_exact_products :
    rawMul gamma4 (-5, -3) = (11, -1) ∧
    rawMul (rawMul (-5, -3) (-5, -3))
      (rawMul (-5, -3) (-5, -3)) = (-185, 231) := by
  norm_num [rawMul, gamma4]

theorem q19_mod5_forces_a_one_mod4 :
    ∀ a : Fin 12, a.val % 6 = 1 →
      (mul 5 gamma4 (pow 5 (-5, -3) a.val)).2 = 4 →
      a.val % 4 = 1 := by decide

theorem q19_mod11_constants :
    pow 11 (-5, -3) 4 = (2, 0) ∧
    mul 11 gamma4 (-5, -3) = (0, 10) := by decide

/-- Complete 120-period certificate for the two small auxiliary moduli. -/
theorem q19_complete_combined_period :
    ∀ a : Fin 120, a.val % 6 = 1 →
      (mul 5 gamma4 (pow 5 (-5, -3) a.val)).2 = 4 →
      (mul 11 gamma4 (pow 11 (-5, -3) a.val)).1 = 0 := by decide

theorem q19_period_identities :
    pow 5 (-5, -3) 12 = (1, 0) ∧
    pow 11 (-5, -3) 40 = (1, 0) := by decide

theorem q31_mod2_constants :
    mul 2 gamma4 (1, 6) = (1, 0) ∧
    pow 2 (1, 6) 1 = (1, 0) := by decide

theorem q67_mod5_constants :
    pow 5 (-2, -9) 2 = (3, 0) ∧
    mul 5 gamma2 (-2, -9) = (2, 0) := by decide

theorem next_shape_examples :
    (223 : ℤ) = 14 ^ 2 + 27 ∧
    (229 : ℤ) = 11 ^ 2 + 27 * 2 ^ 2 ∧
    4 * (367 : ℤ) = 35 ^ 2 + 27 * 3 ^ 2 ∧
    4 * (379 : ℤ) = 29 ^ 2 + 27 * 5 ^ 2 ∧
    4 * (439 : ℤ) = (-28) ^ 2 + 27 * 6 ^ 2 ∧
    (379 : ℕ) % 5 = 4 ∧
    (391 : ℕ) = 17 * 23 ∧ (403 : ℕ) = 13 * 31 ∧
    (415 : ℕ) = 5 * 83 ∧ (427 : ℕ) = 7 * 61 ∧
    (451 : ℕ) = 11 * 41 := by norm_num

#print axioms mod2_nonzero_cube
#print axioms mod2_complete_residues
#print axioms mod5_nonzero_period
#print axioms mod5_trace_zero_branch_two
#print axioms mod5_trace_zero_branch_four
#print axioms mod7_trace_branch_two
#print axioms mod7_trace_branch_four
#print axioms q19_complete_combined_period
#print axioms q19_exact_products

end NestedBinomialV10.Cyclotomic
