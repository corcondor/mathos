// Exact inverse rank sieve. Default: s<=1e6, ell<=1e8.
#include <cstdint>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using U=uint64_t;
struct P{U a,b;};
P mul(P x,P y,U l){return {(x.a*y.a+2*x.b*y.b)%l,(x.a*y.b+x.b*y.a)%l};}
P power(U s,U l){P x{1,0},y{3%l,2%l};while(s){if(s&1)x=mul(x,y,l);s>>=1;if(s)y=mul(y,y,l);}return x;}
bool proper(U s,U l){U a=1,b=1;for(U i=1;i<s;i+=2){U c=3*a+4*b,d=2*a+3*b;a=c;b=d;if(b>l)return true;}return b>l;}
int main(int argc,char**argv){
 U N=argc>1?std::stoull(argv[1]):1000000,L=argc>2?std::stoull(argv[2]):100000000;
 if(L<7||L>100000000||N<5||N>10000000||N>L)return 2;
 std::vector<uint32_t> spf(L/2+2);
 for(U p=3;p*p<=L;p+=2)if(!spf[p/2])for(U j=p*p;j<=L;j+=2*p)if(!spf[j/2])spf[j/2]=p;
 U ellcount=0,tests=0,hits=0,newhits=0;std::vector<bool> excluded(N+1);
 std::cout<<"s,side,ell,k,sign,real,radical\n";
 for(U l=3;l<=L;l+=2)if(!spf[l/2]){
  ++ellcount;U r=l%8;if(r==3)continue;
  int chi=(r==1||r==7)?1:-1;U m=(l-chi)/2;while(!(m&1))m>>=1;
  while(m>1){U s=spf[m/2]?spf[m/2]:m;while(m%s==0)m/=s;
   if(s<5||s>N||!proper(s,l))continue;
   ++tests;P p=power(s,l);if(p.b||(p.a!=1&&p.a!=l-1))continue;
   ++hits;if(!excluded[s]){excluded[s]=true;++newhits;}
   std::cout<<s<<','<<(p.a==1?'X':'Y')<<','<<l<<','<<(l-chi)/(2*s)<<','<<chi<<','<<p.a<<','<<p.b<<'\n';
   break;
  }
 }
 std::cerr<<"auxiliary_primes="<<ellcount<<" modular_tests="<<tests<<" proper_divisors="<<hits<<" excluded_indices="<<newhits<<'\n';
}
