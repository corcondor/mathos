#!/usr/bin/env python3
"""Independent exact certificate for specialized E_{T=100003}(Q).

Proves full rational torsion=0, R is nontorsion and is not 2- or
3-divisible in E(Q). Also eliminates the residual rho=100003
for original-binomial solutions, assuming the v20/v21 necessary bounds.
It does NOT compute the full Mordell-Weil free basis.
"""
from math import gcd, isqrt

rho=100003
b=1
T=rho
A=-T*T*(4*T+3)
B=12*(T*T+5*T+3)
C=12*(2-T)
Delta=-62208*T**5*(4*T+3)**2*(9*T+8)**3
R=(8*T*(4*T+3),6*T*(4*T+3)*(9*T+8))
assert R[1]*R[1]==R[0]**3+B*R[0]**2+A*C*R[0]+4*A*A

def ec_points(p):
    assert Delta%p,("not good reduction",p)
    pts=[None]
    for x in range(p):
        v=(x**3+B*x*x+A*C*x+4*A*A)%p
        pts.extend((x,y) for y in range(p) if (y*y-v)%p==0)
    return pts

def add(P,Q,p):
    if P is None:return Q
    if Q is None:return P
    x,y=P;u,v=Q
    if x==u and (y+v)%p==0:return None
    if x==u:
        slope=(3*x*x+2*B*x+A*C)*pow(2*y,-1,p)
    else:
        slope=(v-y)*pow(u-x,-1,p)
    slope%=p
    xx=(slope*slope-B-x-u)%p
    return (xx,(slope*(x-xx)-y)%p)

def order(P,p,group_size):
    curr=None
    for n in range(1,group_size+1):
        curr=add(curr,P,p)
        if curr is None:
            return n
    raise AssertionError("point order did not divide group order")

for prime,cardinality in ((13,9),(17,16)):
    pts=ec_points(prime)
    assert len(pts)==cardinality,(prime,len(pts))
    red=(R[0]%prime,R[1]%prime)
    assert red in pts
    assert order(red,prime,cardinality)==cardinality
    print("FINITE FIELD",prime,"#E",cardinality,"order(R)",cardinality)
# The rational torsion group injects into groups of coprime orders
# at two good primes (using prime-to-p torsion injectivity).
assert gcd(9,16)==1
print("PROVED: E_100003(Q)_tors = 0 and R infinite")
# If R=l*P over Q, reduction mod good prime preserves multiplication.
# R generates E(F_17) of order 16 and is not twice another point;
# R generates E(F_13) of order 9 and is not three times another.
print("PROVED: R not divisible by 2 or by 3 in E_100003(Q)")

# First elliptic quotient in an integral Tate normal form when b=1:
# y^2+6xy+(8+9T)y=x^3. P=(0,0) is exact order 3 (the line y=0
# has triple contact there). Good reductions p=7 and 13 have group
# orders 6 and 15, so the full rational torsion group is Z/3.
first_a3=8+9*T
first_delta=-243*T*first_a3**3
def first_points(p):
    assert first_delta%p!=0
    count=1
    for x in range(p):
        disc=((6*x+first_a3)**2+4*x**3)%p
        count+=1 if disc==0 else 2 if pow(disc,(p-1)//2,p)==1 else 0
    return count
assert first_points(7)==6 and first_points(13)==15
assert gcd(6,15)==3
print("PROVED: first elliptic quotient E1_100003(Q)_tors = Z/3, via #E(F7)=6 and #E(F13)=15")

def sextic(a,b,r):
    x=a*a; v=b*b
    return 4*x**3+12*(2*v-r)*x*x+12*(3*v*v+5*v*r+r*r)*x-r*r*(3*v+4*r)

# At b=1, k=v_5(4T+3)=1 and d=v_5(9T+8)=1.
# v32 criterion gives precisely the following forbidden a (mod25).
bad={0,5,10,12,13,15,20}
def square_q5(n):
    if n==0:return True
    e=0
    while n%5==0:
        n//=5;e+=1
    return e%2==0 and n%5 in (1,4)
for a in range(25):
    assert square_q5(sextic(a,1,rho)) == (a not in bad),(a,square_q5(sextic(a,1,rho)))
print("PROVED: b=1 forbidden a residues modulo25 =",sorted(bad))

BVAL=(1,2,3,6,9,18,27,54,81,162,243,486)
amax=isqrt(152*rho*rho.bit_length())
assert amax==16075
survivors=0
squares=[]
for den in BVAL:
    amin=max(den+1,isqrt(den*den+rho)+1)
    for a in range(amin,amax+1):
        if (a*a-rho)%den or (rho-a-den)%2:continue
        if gcd(a,den)!=1 or gcd(a,rho)!=gcd(a,3):continue
        survivors+=1
        f=sextic(a,den,rho)
        if f<0:continue
        root=isqrt(f)
        if root*root==f:squares.append((den,a,root))
assert survivors==26198,(survivors,squares)
assert squares==[],squares
assert rho%9 in (1,4,6,7) and 100004%9 not in (1,4,6,7)
print("PROVED CONDITIONAL ON v20/v21: rho=100003 gives no original integer lift")
print("All admissible (a,b) tested",survivors,"sextic squares",len(squares))
print("NEW RHO LOWER BOUND (conditional on preceding 1..100000 proof): 100005")
