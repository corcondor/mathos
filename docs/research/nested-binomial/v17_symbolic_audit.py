#!/usr/bin/env python3
"""Supplementary independent coefficient checks; requires SymPy.

The primary generators and complete independent auditors use only the
standard library. This audit expands identities, not integral-point solvers.
"""
from pathlib import Path
import hashlib
import json
import sympy as s

a,b,j,t,n,u=s.symbols('a b j t n u')
N=b**2*(t*t+3*t+3)+a*b*(t+6)-a*a+j
qa=j*b*b
qb=j*(3*b*b+2*a*b)-2*a*b*(a*a+3*b*b)
qc=j*(3*b*b+3*a*b-2*a*a+j)-a*(9*b**3+21*a*b*b+3*a*a*b-a**3)
F=4*a**6+24*a**4*b*b-12*a**4*j+36*a*a*b**4+60*a*a*b*b*j+12*a*a*j*j-3*b*b*j*j-4*j**3
X=4*a*a-b*b-4*j
ca=-3*b*b*(72*a*a+b*b)
cb=2*b*b*(648*a**4+180*a*a*b*b-b**4)
E=(9*u*u-27*u+27)*n+(u-3)**3-93*n*(n-1)
bound=n*(120-s.Rational(50,3)*u)-9*u*u+27*u-27
expressions={
 'quadratic_reconstruction':N*N-(9*a*b+b*b*(t*t+3*t+3))*N-a*b**3*t**3-(qa*t*t+qb*t+qc),
 'reduced_discriminant':qb*qb-4*qa*qc-b*b*F,
 'elliptic_coordinate':X**3+ca*X+cb-16*F,
 'elliptic_discriminant':-16*(4*ca**3+27*cb**2)+995328*a*a*b**4*(3*a-b)**3*(3*a+b)**3,
 'shifted_square_root_bound':3*(bound-E)-(9*n+u)*(31*n-3*u*u),
}
for name,value in expressions.items():
    assert s.expand(value)==0,name
here=Path(__file__).resolve().parent
note=here/'v17_square_root_gap.md'
report={
 'status':'PASS','identities':{name:'all coefficients vanish' for name in expressions},
 'sympy_version':s.__version__,
 'producer_imported_or_called':False,
 'complete_CAS_solver_called':False,
 'new_lean_execution':False,
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'proof_note_sha256':hashlib.sha256(note.read_bytes()).hexdigest(),
}
(here/'v17_symbolic_audit.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report))
