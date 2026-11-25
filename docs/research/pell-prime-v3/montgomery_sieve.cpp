// Pell trial factors in the three progression classes. Exact Montgomery arithmetic.
// Derived from v2 progression_sieve.cpp; no external code copied.
// Inspired by PrimePath's separate candidate-progression sieve and modular powering.
#include <cstdint>
#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <string>
#include <stdexcept>
using U=uint64_t;using W=__uint128_t;
struct Mont {
 U m,inv,one;
 explicit Mont(U mod):m(mod),inv(1),one(((W)1<<64)%mod){
  if(m<3||!(m&1)||m>=(1ULL<<48))throw std::runtime_error("modulus out of proven range");
  for(int j=0;j<6;j++)inv*=2-m*inv;
  inv=0-inv;
 }
 U red(W a)const{U q=(U)a*inv;U r=(a+(W)q*m)>>64;return r>=m?r-m:r;}
 U norm(U a)const{while(a>=m)a-=m;return a;}
 std::pair<U,U> xy(U s)const{
  U x=one,y=0;
  for(int b=63-__builtin_clzll(s);b>=0;--b){
   U a=red((W)x*x+2*(W)y*y),c=red(2*(W)x*y);
   if((s>>b)&1){x=norm(a+2*c);y=norm(a+c);}else{x=a;y=c;}
  }return{x,y};
 }
};
U powmod(U a,U b,U p){U v=1;while(b){if(b&1)v=v*a%p;a=a*a%p;b>>=1;}return v;}
std::vector<int> primes(int n){std::vector<bool> a(n+1,true);std::vector<int> p;for(int i=2;i<=n;i++)if(a[i]){p.push_back(i);if(1LL*i*i<=n)for(int j=i*i;j<=n;j+=i)a[j]=false;}return p;}
struct Hit {U d=0,k=0;char c='?';U probes=0;};
Hit search(U s,U lo,U hi,const std::vector<int>& ps){
 U step=8*s,rX=s%4==1?6*s+1:2*s+1,rY=s%4==3?2*s-1:6*s-1;
 std::vector<std::pair<int,U>> inverses;for(int p:ps)if(step%p)inverses.push_back({p,powmod(step%p,p-2,p)});
 Hit h; for(U r:{U(1),rY,rX}){
  std::vector<uint8_t> live(hi-lo,1);
  for(auto [p,inv]:inverses){U k=((p-r%p)%p)*inv%p,first=(k+p-lo%p)%p;for(U j=first;j<hi-lo;j+=p)if(step*(lo+j)+r!=(U)p)live[j]=0;}
  for(U j=0;j<hi-lo;j++)if(live[j]){U k=lo+j,m=step*k+r;if(m<2)continue;++h.probes;auto [x,y]=Mont(m).xy(s);if(!x||!y){h.d=m;h.k=k;h.c=!x?'X':'Y';return h;}}
 }
 return h;
}
int main(int argc,char**argv){
 if(argc!=4)return 1;auto p=primes(1000);U lo=std::stoull(argv[2]),hi=std::stoull(argv[3]);
 if(lo>=hi||hi-lo>1000000)return 1;
 std::vector<U> ss;std::ifstream f(argv[1]);U s;while(f>>s){if(s<3||s>1000000||8*s*(hi+1)>=(1ULL<<48))return 2;ss.push_back(s);}
 std::cout<<"s,component,divisor,k,probes\n";
 #pragma omp parallel for schedule(dynamic)
 for(size_t i=0;i<ss.size();i++){U s=ss[i];Hit h=search(s,lo,hi,p);
 #pragma omp critical
 {std::cout<<s<<","<<h.c<<","<<h.d<<","<<h.k<<","<<h.probes<<"\n"<<std::flush;}}
}
