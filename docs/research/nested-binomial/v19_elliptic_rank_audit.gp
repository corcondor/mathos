\\ Optional, separately labelled PARI/GP 2.17.4 experiment.
\\ Its rank results are NOT an input to the standard-library certificate.
\\ No BSD/analytic rank call and no ellratpoints height search is used.
print("PARI/GP ",version());
print("b,rho,rank_lower,rank_upper,sha2_quotient_rank,torsion_order,T_has_order_3");
bs=[1,2,3,6,9,18,27,54,81,162,243,486];
for(i=1,#bs,b=bs[i];for(rho=1,10,if(gcd(b,rho)==1 && sum(a=1,b,(gcd(a,b)==1 && (a^2-rho)%b==0))>0,E=ellinit([0,0,0,48*b^2*(9*rho-b^2),1296*rho^2*b^2-2880*rho*b^4-128*b^6]);R=ellrank(E);T=elltors(E);P=[12*b^2,4*b*(9*rho+8*b^2)];print(b,",",rho,",",R[1],",",R[2],",",R[3],",",T[1],",",ellisoncurve(E,P)&&ellmul(E,P,3)==[0]))));
