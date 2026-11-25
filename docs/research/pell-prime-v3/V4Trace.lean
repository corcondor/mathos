import Mathlib
namespace PellTraceV4

-- H_n = 1 + sum_{j=1}^n (w^j + w^-j) at z=w+w^-1.
def H {R : Type*} [Ring R] (z : R) : ℕ → R
  | 0 => 1
  | 1 => z+1
  | n+2 => z*H z (n+1)-H z n

theorem H_geometric {K : Type*} [Field K] (w : K) (hw : w ≠ 0) (n : ℕ) :
    (w-1)*w^n*H (w+w⁻¹) n = w^(2*n+1)-1 := by
  have hw' : w*w⁻¹=1 := mul_inv_cancel₀ hw
  have htrace : w*(w+w⁻¹)=w^2+1 := by rw [mul_add,hw']; ring
  match n with
  | 0 => simp [H]
  | 1 =>
    norm_num [H]
    calc
      (w-1)*w*(w+w⁻¹+1) = (w-1)*(w*(w+w⁻¹)+w) := by ring
      _ = w^3-1 := by rw [htrace]; ring
  | n+2 =>
    have h0 := H_geometric w hw n
    have h1 := H_geometric w hw (n+1)
    calc
      (w-1)*w^(n+2)*H (w+w⁻¹) (n+2)
          = (w*(w+w⁻¹))*((w-1)*w^(n+1)*H (w+w⁻¹) (n+1))
            - w^2*((w-1)*w^n*H (w+w⁻¹) n) := by
              rw [H, pow_succ w (n+1), pow_succ w n]
              ring
      _ = w^(2*(n+2)+1)-1 := by
        rw [htrace,h1,h0]
        rw [show 2*(n+2)+1=(2*n+1)+4 by omega,
          show 2*(n+1)+1=(2*n+1)+2 by omega]
        simp only [pow_add]
        ring
termination_by n

theorem trace_root_of_unity {K : Type*} [Field K] (w : K) (n : ℕ)
    (hw : w ≠ 0) (hw1 : w ≠ 1) (h : w^(2*n+1)=1) :
    H (w+w⁻¹) n = 0 := by
  have hh := H_geometric w hw n
  rw [h,sub_self] at hh
  exact (mul_eq_zero.mp hh).resolve_left
    (mul_ne_zero (sub_ne_zero.mpr hw1) (pow_ne_zero _ hw))

theorem H_primitive_root {K : Type*} [Field K] (w : K) (n : ℕ)
    (hw : IsPrimitiveRoot w (2*n+1)) (hn : 0<n) (h0 : w≠0) (h1 : w≠1) :
    H (w+w⁻¹) n = 0 :=
  trace_root_of_unity w n h0 h1 hw.pow_eq_one

def A (n : ℕ) : ℤ := H (6:ℤ) n
def B (n : ℕ) : ℤ := (-1)^n * H (-6:ℤ) n

theorem A_rec (n : ℕ) : A (n+2)=6*A (n+1)-A n := by
  simp [A,H]

theorem B_rec (n : ℕ) : B (n+2)=6*B (n+1)-B n := by
  simp only [B,H,pow_succ]
  ring

-- Two independent recurrences give the exact integer norm identity on odd indices.
theorem trace_negative_pell (n : ℕ) :
    A n ^ 2 - 2 * B n ^ 2 = -1 := by
  -- Strengthen to a cross term, since a second-order recurrence needs two initial states.
  suffices h : A n ^ 2 - 2 * B n ^ 2 = -1 ∧
      A (n+1)^2-2*B (n+1)^2 = -1 ∧
      A (n+1)*A n-2*B (n+1)*B n = -3 from h.1
  induction n with
  | zero => norm_num [A,B,H]
  | succ n ih =>
    rcases ih with ⟨h0,h1,hc⟩
    change A (n+1)^2-2*B (n+1)^2 = -1 ∧
      A (n+2)^2-2*B (n+2)^2 = -1 ∧
      A (n+2)*A (n+1)-2*B (n+2)*B (n+1) = -3
    rw [A_rec, B_rec]
    refine ⟨h1, ?_, ?_⟩
    · nlinarith
    · nlinarith

#print axioms H_geometric
#print axioms trace_root_of_unity
#print axioms trace_negative_pell
end PellTraceV4
