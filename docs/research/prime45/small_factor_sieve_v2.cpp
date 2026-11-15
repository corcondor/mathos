// Deterministic sieve + exact modular factor check for 45^n+n.
// g++ -std=c++17 -O3 small_factor_sieve_v2.cpp -o small_factor_sieve_v2
// ./small_factor_sieve_v2
#include <algorithm>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <vector>
using u64=std::uint64_t;
using u32=std::uint32_t;
static u64 powmod(u64 a,u64 n,u64 p){
 u64 r=1;
 while(n){if(n&1)r=(r*a)%p;a=(a*a)%p;n>>=1;}
 return r;
}
int main(){
 constexpr u32 LIMIT=1'000'000'000;
 constexpr u32 BLOCK_ODD_COUNT=1<<20;
 constexpr int N1=3878,N2=9424;
 u32 sq=(u32)std::sqrt((double)LIMIT)+1;
 std::vector<bool> sieve(sq+1);
 std::vector<u32> base_primes;
 for(u32 p=2;p<=sq;p++){
  if(sieve[p])continue;
  base_primes.push_back(p);
  if(1ULL*p*p<=sq)
   for(u32 q=p*p;q<=sq;q+=p) sieve[q]=true;
 }
 u64 count_primes=1;
 u64 factor_count1=0,factor_count2=0;
 for(u64 lo=3;lo<=LIMIT;lo+=2ULL*BLOCK_ODD_COUNT){
  u64 hi=std::min<u64>(LIMIT,lo+2ULL*BLOCK_ODD_COUNT-2);
  const size_t len=(hi-lo)/2+1;
  std::vector<std::uint8_t> marked(len,0);
  for(u32 p:base_primes){
   if(p==2)continue;
   u64 start=std::max<u64>(1ULL*p*p,((lo+p-1)/p)*p);
   if((start&1)==0)start+=p;
   if(start>hi)continue;
   for(u64 j=start;j<=hi;j+=2ULL*p)marked[(j-lo)/2]=1;
  }
  for(size_t i=0;i<len;i++){
   if(marked[i])continue;
   u64 p=lo+2ULL*i;
   count_primes++;
   if((powmod(45,N1,p)+N1)%p==0){std::printf("FACTOR n=%d p=%llu\n",N1,(unsigned long long)p);factor_count1++;}
   if((powmod(45,N2,p)+N2)%p==0){std::printf("FACTOR n=%d p=%llu\n",N2,(unsigned long long)p);factor_count2++;}
  }
 }
 std::printf("DONE limit=%u primes_checked=%llu factors_n3878=%llu factors_n9424=%llu\n",
  LIMIT,(unsigned long long)count_primes,(unsigned long long)factor_count1,(unsigned long long)factor_count2);
 return factor_count1==0 && factor_count2==0 && count_primes==50847534 ? 0 : 1;
}
