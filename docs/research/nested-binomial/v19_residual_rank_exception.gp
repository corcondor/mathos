\\ Optional independent CAS experiment, not a prerequisite of the proof.
print("PARI version: ",version());
E=ellinit([0,0,0,-1947,108214]);
P=[35,288];
print("P0_on_curve: ",ellisoncurve(E,P));
print("P0_double: ",ellmul(E,P,2));
print("P0_order: ",ellorder(E,P));
print("rank_bounds: ",ellrank(E));
print("torsion: ",elltors(E));
quit;
