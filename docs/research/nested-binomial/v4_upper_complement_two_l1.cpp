// Complete finite certificate for j=i-2, ell=1, 23 <= i < 2^20.
// Both outer branches are checked: k=r and k=A-r, where A=C(i,2).
// Floating point only proposes interval endpoints. Every endpoint is checked
// using exact integer inequalities; all remaining candidates get Lucas witnesses.
// See v4_upper_complement_two_l1_certification.md for the interval proof.
#include <algorithm>
#include <cassert>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using u64 = uint64_t;
using u128 = __uint128_t;
using i128 = __int128_t;
const u128 Q = u128(1) << 56;
struct Interval { i128 lo, hi; };

u128 ceildiv(u128 a, u128 b) { assert(b); return a / b + (a % b != 0); }

// All operations round down. Result/Q is a lower bound for 2*atanh(a/b).
u128 logseries(u64 a, u64 b) {
    assert(3*u128(a) <= b);
    u128 z = Q*a/b, z2 = z*z/Q, power = z, sum = 0;
    for (unsigned n=0;n<24;++n) {
        sum += power/(2*n+1);
        power = power*z2/Q;
    }
    return 2*sum;
}

const u128 LOG2_LO = logseries(1,3);
const u128 LOG2_HI = LOG2_LO + 256;

Interval logint(u64 n) {
    assert(n > 0);
    unsigned e = 63 - __builtin_clzll(n);
    u64 base = u64(1) << e;
    u128 lo = e*LOG2_LO + logseries(n-base,n+base);
    return {i128(lo), i128(lo+(e+1)*256)};
}

// Here k denotes the parameter i from the original equation, and t denotes
// the smaller outer index r. Returns 2Q*(log C(C(i,2),r)-log C(i*i,4*i-4)).
Interval difference(u64 k, u64 t) {
    u64 A=k*(k-1)/2, N=k*k, q=4*k-4;
    assert(t > 0 && t < A && q < N);
    Interval la=logint(A), lt=logint(t), ln=logint(N), lq=logint(q);
    i128 lo=2*t*la.lo-(2*t+1)*lt.hi-2*q*ln.hi+(2*q+1)*lq.lo
            +2*i128(Q)*(i128(t)-i128(q));
    i128 hi=2*t*la.hi-(2*t+1)*lt.lo-2*q*ln.lo+(2*q+1)*lq.hi
            +2*i128(Q)*(i128(t)-i128(q));
    u128 atnum=u128(t)*(t-1)*Q, aqnum=u128(q)*(q-1)*Q;
    u128 btnum=u128(t)*(t-1)*(2*t-1)*Q;
    u128 btden=6*u128(A)*(A-t+1);
    u128 bqnum=u128(q)*(q-1)*(2*q-1)*Q;
    u128 bqden=6*u128(N)*(N-q+1);
    lo-=i128(ceildiv(atnum,A));
    lo+=i128(aqnum/N);
    lo+=i128(2*Q/(12*q+1));
    lo-=i128(ceildiv(2*Q,12*t));
    lo-=i128(ceildiv(btnum,btden));
    hi-=i128(atnum/A);
    hi+=i128(ceildiv(aqnum,N));
    hi+=i128(ceildiv(2*Q,12*q));
    hi-=i128(2*Q/(12*t+1));
    hi+=i128(ceildiv(bqnum,bqden));
    assert(lo<=hi);
    return {lo,hi};
}

long double proposal(u64 k, u64 tmin, u64 tmax) {
    long double A=k*(k-1)/2, N=k*k, q=4*k-4;
    long double t=q+q*logl(2)/logl(k/8.0L);
    t=std::clamp(t,(long double)tmin,(long double)tmax);
    long double fixed=-q*logl(N)+lgammal(q+1)+q*(q-1)/(2*N);
    for(int it=0;it<8;++it) {
        long double f=t*logl(A)-lgammal(t+1)-t*(t-1)/(2*A)+fixed;
        t-=f/logl(A/t);
        t=std::clamp(t,(long double)tmin,(long double)tmax);
    }
    return t;
}

unsigned modpow(unsigned a,unsigned b,unsigned p) {
    unsigned out=1;
    while(b) { if(b&1) out=out*a%p; a=a*a%p; b>>=1; }
    return out;
}
struct Prime {
    unsigned p;
    std::vector<unsigned> fac,inv;
    explicit Prime(unsigned pp):p(pp),fac(pp,1),inv(pp,1) {
        for(unsigned a=1;a<p;++a)fac[a]=fac[a-1]*a%p;
        inv[p-1]=modpow(fac[p-1],p-2,p);
        for(unsigned a=p-1;a;--a)inv[a-1]=inv[a]*a%p;
    }
    unsigned binom(u64 n,u64 r) const {
        unsigned out=1;
        while(r) {
            unsigned a=n%p,b=r%p;
            if(b>a)return 0;
            out=out*fac[a]%p*inv[b]%p*inv[a-b]%p;
            n/=p; r/=p;
        }
        return out;
    }
};

void write32(std::ostream &s,uint32_t x) {
    for(unsigned a=0;a<4;++a)s.put(char((x>>(8*a))&255));
}
u64 isqrt(u64 n) {
    u64 r=sqrtl((long double)n);
    while(u128(r+1)*(r+1)<=n)++r;
    while(u128(r)*r>n)--r;
    return r;
}

int main(int argc,char**argv) {
    u64 first=23,last=u64(1)<<20,small=1024;
    std::string prefix="v4_upper_complement_two_l1";
    if(argc>=2)last=std::stoull(argv[1]);
    if(argc>=3)prefix=argv[2];
    // The theorem for ell=1 only needs 2^20. The optional extension through
    // 2^21 supplies the same certified r windows for other inner lower indices.
    assert(first<last && last<=u64(1)<<21);
    // Tail after 24 atanh terms is less than one unit/Q.
    u128 p3=1;for(unsigned a=0;a<49;++a)p3*=3;
    assert(9*Q < 196*p3);
    std::vector<Prime> primes;
    for(unsigned p=2;p<1000;++p) {
        bool prime=true;
        for(unsigned d=2;d*d<=p;++d)if(p%d==0){prime=false;break;}
        if(prime)primes.emplace_back(p);
    }
    assert(primes.size()<256);
    std::ofstream cert(prefix+".bin",std::ios::binary);
    cert.write("V4JC2L1\0",8);
    write32(cert,first);write32(cert,last);write32(cert,small);
    u64 candidates=0,maxwidth=0,maxprime=0,lowchecks=0,highchecks=0;
    u64 zero_width=0,adjustments=0;
    std::vector<u64> prime_counts(primes.size(),0);
    auto start=std::chrono::steady_clock::now();
    for(u64 k=first;k<last;++k) {
        u64 m=k-2,A=k*(k-1)/2;
        u64 tmin=std::max(k,(m+isqrt(5*m*m))/2+1);
        u64 tmax=std::min(A/2,(k>=802?5:10)*m-1);
        assert(tmin<=tmax);
        u64 lo=tmin-1,hi=tmax+1;
        if(k>=small) {
            u64 t0=(u64)floorl(proposal(k,tmin,tmax));
            lo=std::clamp(t0-1,tmin-1,tmax);
            hi=std::clamp(t0+2,tmin,tmax+1);
            while(lo>=tmin) {
                ++lowchecks;
                if(difference(k,lo).hi<0)break;
                --lo; ++adjustments;
            }
            while(hi<=tmax) {
                ++highchecks;
                if(difference(k,hi).lo>2*i128(LOG2_HI))break;
                ++hi; ++adjustments;
            }
        }
        assert(tmin-1<=lo && lo<hi && hi<=tmax+1);
        u64 width=hi-lo-1;
        maxwidth=std::max(maxwidth,width);
        if(!width)++zero_width;
        write32(cert,lo);write32(cert,hi);
        for(u64 t=lo+1;t<hi;++t) {
            // The original k equals t in the lower branch and A-t in the upper.
            // The record has two witness bytes per t, in that order.
            for(unsigned branch=0;branch<2;++branch) {
                u64 original_k=(branch==0?t:A-t);
                bool rejected=false;
                for(unsigned idx=0;idx<primes.size();++idx) {
                    const Prime& P=primes[idx];
                    unsigned p=P.p;
                    unsigned lhs=P.binom(A,t);
                    unsigned rhs=((original_k%p)*(original_k%p)+P.binom(k*k,4*k-4))%p;
                    if(lhs!=rhs) {
                        cert.put(char(idx)); ++prime_counts[idx];
                        maxprime=std::max(maxprime,u64(p));
                        rejected=true;break;
                    }
                }
                if(!rejected) {
                    std::cerr<<"SURVIVOR i="<<k<<" r="<<t<<" original_k="<<original_k<<"\n";
                    return 2;
                }
                ++candidates;
            }
        }
        if(k%65536==0) {
            double seconds=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
            std::cerr<<"i="<<k<<" candidates="<<candidates<<" seconds="<<seconds<<"\n";
        }
    }
    cert.close();assert(cert.good());
    double seconds=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
    std::ofstream report(prefix+"_report.json");
    report<<"{\n  \"status\": \"pass\",\n  \"i_min\": "<<first
          <<",\n  \"i_exclusive_max\": "<<last<<",\n  \"small_cutoff\": "<<small
          <<",\n  \"outer_branches\": 2"
          <<",\n  \"candidates\": "<<candidates<<",\n  \"survivors\": 0"
          <<",\n  \"max_interval_width\": "<<maxwidth<<",\n  \"max_witness_prime\": "<<maxprime
          <<",\n  \"low_endpoint_checks\": "<<lowchecks<<",\n  \"high_endpoint_checks\": "<<highchecks
          <<",\n  \"zero_width_intervals\": "<<zero_width<<",\n  \"endpoint_adjustments\": "<<adjustments
          <<",\n  \"elapsed_seconds\": "<<seconds<<",\n  \"prime_witness_counts\": {";
    bool comma=false;
    for(unsigned a=0;a<primes.size();++a)if(prime_counts[a]) {
        if(comma)report<<",";comma=true;
        report<<"\n    \""<<primes[a].p<<"\": "<<prime_counts[a];
    }
    report<<"\n  }\n}\n";
    report.close();
    std::cout<<"PASS: "<<last-first<<" values of i, both outer branches, "<<candidates<<" Lucas witnesses, "
             <<seconds<<" seconds.\n";
}
