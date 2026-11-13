import Mathlib.Tactic

/-!
# v83 local F7 obstruction: a finite, kernel-checked covering argument

For rho=100003,b=9 the cube-core elliptic lift must satisfy
  d*v³-c*u³ = 54*t*u*v+8106075,
  a² = t*u*v+9²+100003.
Modulo 7, 54 ≡5, 8106075 ≡5, 9²+100003≡5.
For six v80 cube-core types, the residues (c,d,t) are one of
  (1,1,1), (6,1,6), (1,6,6).
The three theorem statements below enumerate ALL 7³ local triples.
This is a genuine finite congruence obstruction, not a complete
classification of the surviving cubic covers or the original equation.
-/

namespace NestedBinomialV10

/-- No mod-7 lift for the coefficient residues (c,d,t)=(1,1,1). -/
theorem no_cube_cover_mod7_caseA :
    ∀ (u v a : Fin 7),
      ¬ ((v.val ^ 3) % 7 =
          (u.val ^ 3 + 5 * u.val * v.val + 5) % 7 ∧
        (a.val ^ 2) % 7 =
          (u.val * v.val + 5) % 7) := by
  decide

/-- No mod-7 lift for the coefficient residues (c,d,t)=(6,1,6). -/
theorem no_cube_cover_mod7_caseB :
    ∀ (u v a : Fin 7),
      ¬ ((v.val ^ 3) % 7 =
          (6 * u.val ^ 3 + 5 * 6 * u.val * v.val + 5) % 7 ∧
        (a.val ^ 2) % 7 =
          (6 * u.val * v.val + 5) % 7) := by
  decide

/-- No mod-7 lift for the coefficient residues (c,d,t)=(1,6,6). -/
theorem no_cube_cover_mod7_caseC :
    ∀ (u v a : Fin 7),
      ¬ ((6 * v.val ^ 3) % 7 =
          (u.val ^ 3 + 5 * 6 * u.val * v.val + 5) % 7 ∧
        (a.val ^ 2) % 7 =
          (6 * u.val * v.val + 5) % 7) := by
  decide

#print axioms no_cube_cover_mod7_caseA
#print axioms no_cube_cover_mod7_caseB
#print axioms no_cube_cover_mod7_caseC

end NestedBinomialV10
