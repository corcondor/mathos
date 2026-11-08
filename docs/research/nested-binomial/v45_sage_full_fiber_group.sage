# v45: certification-focused specialised Mordell-Weil computation in SageMath.
# Runs under 'sage -python' (explicit sage.all imports); no hidden Sage preparser.
#   sage -python docs/research/nested-binomial/v45_sage_full_fiber_group.sage RHO B
# Exits status 0 only after provably complete rank + generators + saturation.
# On incomplete proof, emits INCOMPLETE_NOT_CERTIFIED and exits nonzero.
from sage.all import QQ, ZZ, EllipticCurve, version
import json
import sys
import traceback


def run(rho, b):
    if rho <= 0 or b <= 0 or 486 % b != 0:
        raise ValueError("Expected rho > 0 and a positive divisor b of 486")
    T = QQ(rho) / (b*b)
    A = -T*T*(4*T+3)
    B = 12*(T*T+5*T+3)
    C = 12*(2-T)
    E = EllipticCurve(QQ, [0,B,0,A*C,4*A*A])
    R = E([8*T*(4*T+3),6*T*(4*T+3)*(9*T+8)])
    report = {
        "rho":int(rho),
        "b":int(b),
        "T":str(T),
        "sage_version":str(version()),
        "curve_a_invariants":[str(z) for z in E.a_invariants()],
        "discriminant":str(E.discriminant()),
        "explicit_section_R":str(R),
        "scope":"Full MW group of this ONE rational specialization E_(rho/b^2)(QQ); not all rho"
    }
    # Sage's proof flag is mandatory. Analytic rank heuristics are prohibited.
    rank = ZZ(E.rank(proof=True))
    report["proven_rank"] = int(rank)
    basis = list(E.gens(proof=True))
    if not E.gens_certain():
        raise RuntimeError("Rank may be proved but Sage says generators are NOT certain")
    if len(basis) != rank:
        raise RuntimeError("Proven rank and certified generator count disagree")
    # max_prime=-1 forces complete saturation, not a user-supplied cutoff.
    saturated, index, regulator = E.saturation(basis, max_prime=-1)
    if len(saturated) != rank:
        raise RuntimeError("Saturation output has incorrect rank")
    tors = E.torsion_subgroup()
    report.update({
        "status":"CERTIFIED_BY_SAGE_PROOF",
        "free_generators":[str(z) for z in saturated],
        "full_torsion_invariants":[int(z) for z in tors.invariants()],
        "torsion_order":int(tors.order()),
        "saturation_index_of_input_generators":int(index),
        "saturated_regulator":str(regulator),
        "generator_certainty":True,
        "original_equation_solved":False
    })
    return report


if __name__ == "__main__":
    rho = ZZ(sys.argv[1]) if len(sys.argv) > 1 else ZZ(1)
    b = ZZ(sys.argv[2]) if len(sys.argv) > 2 else ZZ(1)
    try:
        result = run(rho,b)
        print(json.dumps(result, ensure_ascii=False, indent=2), flush=True)
    except Exception as exc:
        print(json.dumps({
            "status":"INCOMPLETE_NOT_CERTIFIED",
            "rho":int(rho), "b":int(b),
            "error_type":type(exc).__name__,
            "error":str(exc)[:1500],
            "original_equation_solved":False
        }, ensure_ascii=False, indent=2), flush=True)
        sys.exit(2)
