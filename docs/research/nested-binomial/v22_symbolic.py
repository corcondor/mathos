#!/usr/bin/env python3
"""v22 denominator-cleared symbolic identity verifier, independent from finite scan.
Requires sympy. Complements (does not replace) the written valuation proofs.
"""
import sympy as sp
n,t,a,b,rho=sp.symbols('n t a b rho')
q=t*t+3*t+3
E=n*(n-1)
D=81*E
H=9*n*q+t**3
P=H**2+H*D*(9*n-t-6)-q*D**2
X=t*t-9*n; Y=t*t+6*t+9*n
checks={
  'Z_rational_cube': H**2-D**2-P-81*E*X*Y,
  'U_rational_cube':P*(t*D+H)-(H+D)**3-729*n*(n-1)**2*X**3,
  'V_rational_cube':P*((t+3)*D+H)-(H-D)**3-729*n*n*(n-1)*Y**3,
  'Z_recovery': (a*a-b*b-(a*a+a*b*(9*n-t-6)-b*b*q))
                -b*(b*(t+1)*(t+2)+a*(t+6-9*n)),
  'Z_minus': (b*(t+1)*(t+2)+a*(t+6-9*n))-2*b-6*a
                 -(t*(a+b*(t+3))-9*a*n),
  'Z_plus':(b*(t+1)*(t+2)+a*(t+6-9*n))-2*b+6*a
                 -((t+3)*(a+b*t)-9*a*(n-1)),
  'L_product': (a*a-6*a*b-rho-3*b*b)*(a*a+6*a*b-rho-3*b*b)
                 -((a*a-b*b-rho)**2 -4*b*b*(3*a*a+rho+b*b))  # likely check identity? 
}
# Use Z as independent integer, replacing rho=a²−b²−bZ.
z=sp.symbols('z')
checks.pop('L_product')
checks['L_factored']=sp.expand(
  ((a*a-6*a*b-rho-3*b*b)*(a*a+6*a*b-rho-3*b*b)
   -b*b*((z-2*b)**2-36*a*a)).subs(rho,a*a-b*b-b*z))
for name, expr in checks.items():
  expanded=sp.Poly(sp.expand(expr),n,t,a,b,rho,z)
  if not expanded.is_zero:
    print(name, 'FAILED', expanded.as_expr());raise AssertionError(name)
  print(name,'PASS')
print('v22 polynomial identities: PASS',len(checks))
