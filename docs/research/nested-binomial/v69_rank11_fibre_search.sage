# v69: certified search for genus-two bielliptic fibres whose
# FIRST and SECOND elliptic quotients both have rank one.
#
# This searches rational parameters T in a specified finite list; the
# results are NOT a classification of all positive T, nor all rational
# points on the genus-two curve. Rank is recorded as PROVED only when
# E.rank(proof=True,algorithm="pari") returns.
#
# SageMath 10.10:
# sage -python .../v69_rank11_fibre_search.sage "2,3,..."
from sage.all import QQ, ZZ, EllipticCurve, PolynomialRing
from sage.env import SAGE_VERSION
import json,sys,time

parameters=[QQ(t.strip()) for t in sys.argv[1].split(",")] if len(sys.argv)>1 else [QQ(t) for t in range(1,21)]
assert all(t>0 for t in parameters)
print("SEARCH_START",json.dumps({"sage":SAGE_VERSION,"Ts":[str(T) for T in parameters]}),flush=True)
results=[]
for T in parameters:
    tic=time.time()
    A=QQ(4); B=24-12*T; C=36+60*T+12*T*T; D=-T*T*(4*T+3)
    E1=EllipticCurve(QQ,[0,B,0,A*C,A*A*D])
    E2=EllipticCurve(QQ,[0,C,0,B*D,A*D*D])
    assert E1.discriminant() and E2.discriminant()
    row={"T":str(T),"E1_rank":None,"E2_rank":None,"qc_precondition":False}
    for name,E in (("E1",E1),("E2",E2)):
        try:
            rank=ZZ(E.rank(proof=True,algorithm="pari",pari_effort=1))
            row[name+"_rank"]=int(rank)
        except Exception as ex:
            row[name+"_error"]=type(ex).__name__+": "+str(ex)[:250]
    if row["E1_rank"]==1 and row["E2_rank"]==1:
        for p in (5,7,11,13,17,19,23,29,31,37,41,43):
            try:
                if E1.has_good_reduction(p) and E2.has_good_reduction(p) and E1.is_ordinary(p) and E2.is_ordinary(p):
                    row.setdefault("good_ordinary_primes",[]).append(int(p))
            except Exception:pass
        row["qc_precondition"]=bool(row.get("good_ordinary_primes"))
        print("RANK11_MATCH",json.dumps(row),flush=True)
    else:
        print("PROVED_OR_INCOMPLETE",json.dumps(row),flush=True)
    row["seconds"]=round(time.time()-tic,2)
    results.append(row)
matches=[x for x in results if x["qc_precondition"]]
print("SEARCH_COMPLETE",json.dumps({"count":len(results),"rank11_preconditions_met":len(matches),"matches":matches,"all_results":results,
    "LIMIT":"precheck only; NOT a quadratic Chabauty nor MW sieve completion"},ensure_ascii=False),flush=True)
