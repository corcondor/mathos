"""SMT search for a universal valuation consequence, with replayable proof.

This does not encode or solve the entire original Diophantine equation.
For ell=1, a putative solution yields the six integer valuations below.
We search the optimal integer coefficient C in c <= C*rho under these
necessary valuation constraints. No finite bound is imposed on valuations.
The corresponding elementary lemma is also submitted to Lean separately.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'v4_mathdeps'))
import z3

def minimum_repeated(x, y, z):
    return z3.Or(z3.And(x == y, x <= z),
                 z3.And(x == z, x <= y),
                 z3.And(y == z, y <= x))

def main():
    z3.set_param(proof=True)
    c, alpha, rho, beta, chi, lam = z3.Ints('c alpha rho beta chi lambda')
    vs = [c, alpha, rho, beta, chi, lam]
    assumptions = [v >= 0 for v in vs] + [
        alpha >= c,                 # q | A
        chi >= 2 * c,               # q^2 | X
        alpha <= rho + lam,         # A | r*L
        z3.Implies(alpha > rho, beta == rho),  # B= r or B=A-r
        minimum_repeated(lam, chi, 2 * beta),  # L=X+B^2
    ]
    results = []
    for coefficient in range(1, 4):
        solver = z3.Solver()
        solver.add(*assumptions, c > coefficient * rho)
        result = solver.check()
        entry = {'coefficient': coefficient, 'result': str(result)}
        if result == z3.sat:
            model = solver.model()
            entry['countermodel_to_valuation_bound'] = {
                str(v): model.eval(v, model_completion=True).as_long() for v in vs}
        elif result == z3.unsat:
            (ROOT / 'v4_valuation_bound.smt2').write_text(solver.to_smt2())
            (ROOT / 'v4_valuation_bound.z3proof').write_text(str(solver.proof()))
        else:
            raise RuntimeError(solver.reason_unknown())
        results.append(entry)
    assert [x['result'] for x in results] == ['sat', 'sat', 'unsat']
    report = {
        'solver_version': z3.get_version_string(),
        'domain': 'all nonnegative integer valuations, no upper bound',
        'equation_fully_encoded': False,
        'claim': 'The valuation constraints imply c <= 3*rho; coefficients 1 and 2 do not follow.',
        'countermodels_are_not_solutions_of_original_equation': True,
        'results': results,
    }
    (ROOT / 'v4_valuation_synthesis.json').write_text(json.dumps(report, indent=2))
    print(json.dumps(report, indent=2))

if __name__ == '__main__':
    main()
