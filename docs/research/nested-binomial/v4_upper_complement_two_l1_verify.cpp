// Independent verifier for v4_upper_complement_two_l1.bin.
// Differences from generator: Q=2^52, 28 terms, outward interval
// propagation of every atanh power, separate binomial bounds,
// integer-only square roots, Pascal recurrence for Lucas digit values.
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <cstring>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using u64=uint64_t;
using u128=__uint128_t;
using i128=__int128_t;
const u128 SCALE=u128(1)<<52;
const unsigned TERMS=28;
struct Bound { i128 low,high; };

u128 up_div(u128 a,u128 b) { assert(b>0);return a/b+(a%b!=0); }

// SCALE times 2*atanh(numerator/denominator).
Bound atanh_interval(u64 numerator,u64 denominator) {
    assert(3*u128(numerator)<=denominator);
    u128 z_low=SCALE*numerator/denominator;
    u128 z_high=up_div(SCALE*numerator,denominator);
    u128 z2_low=z_low*z_low/SCALE;
    u128 z2_high=up_div(z_high*z_high,SCALE);
    u128 power_low=z_low,power_high=z_high;
    u128 sum_low=0,sum_high=0;
    for(unsigned a=0;a<TERMS;++a) {
        sum_low+=power_low/(2*a+1);
        sum_high+=up_div(power_high,2*a+1);
        power_low=power_low*z2_low/SCALE;
        power_high=up_div(power_high*z2_high,SCALE);
    }
    // 2 sum_{a>=28} z^(2a+1)/(2a+1)
    // <=9/(4*57*3^57)<1/SCALE, checked once in main.
    return {i128(2*sum_low),i128(2*sum_high+1)};
}

const Bound LN2=atanh_interval(1,3);

Bound natural_log_integer(u64 n) {
    assert(n>0);
    unsigned exponent=0;
    u64 base=1;
    while(base<=n/2) {base*=2;++exponent;}
    Bound rest=atanh_interval(n-base,n+base);
    return {i128(exponent)*LN2.low+rest.low,
            i128(exponent)*LN2.high+rest.high};
}

// Twice SCALE times [log C(n,r) + 1/2 log(2*pi)].
// The same constant cancels when two such intervals are subtracted.
Bound shifted_log_binomial(u64 n,u64 r) {
    assert(0<r && r<n);
    Bound ln=natural_log_integer(n),lr=natural_log_integer(r);
    i128 low=2*i128(r)*ln.low-(2*i128(r)+1)*lr.high+2*i128(SCALE)*r;
    i128 high=2*i128(r)*ln.high-(2*i128(r)+1)*lr.low+2*i128(SCALE)*r;
    u128 linear=u128(r)*(r-1)*SCALE;
    u128 remainder=u128(r)*(r-1)*(2*r-1)*SCALE;
    u128 denominator=6*u128(n)*(n-r+1);
    low-=i128(up_div(2*SCALE,12*r));
    high-=i128(2*SCALE/(12*r+1));
    low-=i128(up_div(linear,n));
    high-=i128(linear/n);
    low-=i128(up_div(remainder,denominator));
    assert(low<=high);
    return {low,high};
}

Bound logarithmic_ratio(u64 k,u64 t) {
    u64 B=k*(k-1)/2;
    Bound left=shifted_log_binomial(B,t);
    Bound right=shifted_log_binomial(k*k,4*k-4);
    return {left.low-right.high,left.high-right.low};
}

u64 integer_sqrt(u64 n) {
    assert(n>0);
    unsigned bits=0;
    for(u64 t=n;t;t>>=1)++bits;
    u64 x=u64(1)<<((bits+1)/2);
    while(true) {
        u64 y=(x+n/x)/2;
        if(y>=x)break;
        x=y;
    }
    assert(u128(x)*x<=n && u128(x+1)*(x+1)>n);
    return x;
}

uint32_t read32(std::istream &input) {
    uint32_t value=0;
    for(unsigned position=0;position<4;++position) {
        int c=input.get();assert(c!=EOF);
        value|=uint32_t(uint8_t(c))<<(8*position);
    }
    return value;
}

struct PascalPrime {
    unsigned p;
    std::vector<std::vector<unsigned>> choose;
    explicit PascalPrime(unsigned prime):p(prime),choose(prime,std::vector<unsigned>(prime,0)) {
        for(unsigned n=0;n<p;++n) {
            choose[n][0]=choose[n][n]=1;
            for(unsigned r=1;r<n;++r)
                choose[n][r]=(choose[n-1][r-1]+choose[n-1][r])%p;
        }
    }
    unsigned binomial(u64 n,u64 r) const {
        unsigned answer=1;
        while(n || r) {
            unsigned a=n%p,b=r%p;
            if(b>a)return 0;
            answer=answer*choose[a][b]%p;
            n/=p;r/=p;
        }
        return answer;
    }
};

int main(int argc,char **argv) {
    std::string input_path="v4_upper_complement_two_l1.bin";
    std::string output_path="v4_upper_complement_two_l1_verification.json";
    if(argc>1)input_path=argv[1];
    if(argc>2)output_path=argv[2];
    std::ifstream input(input_path,std::ios::binary);assert(input.good());
    char magic[8];input.read(magic,8);assert(input.gcount()==8);
    assert(std::memcmp(magic,"V4JC2L1\0",8)==0);
    u64 first=read32(input),last=read32(input),small=read32(input);
    assert(first==23 && (last==(u64(1)<<20) || last==(u64(1)<<21)) && small==1024);
    u128 power_of_three=1;
    for(unsigned n=0;n<57;++n)power_of_three*=3;
    assert(9*SCALE < 4*u128(57)*power_of_three);
    std::vector<unsigned> prime_list;
    std::vector<bool> composite(1000,false);
    for(unsigned p=2;p<1000;++p) {
        if(composite[p])continue;
        prime_list.push_back(p);
        for(unsigned multiple=2*p;multiple<1000;multiple+=p)composite[multiple]=true;
    }
    std::vector<PascalPrime*> lookup(prime_list.size(),nullptr);
    u64 witnesses=0,lower_checks=0,upper_checks=0,max_prime=0;
    u64 max_width=0,retained_all=0,coincident_branches=0;
    for(u64 k=first;k<last;++k) {
        u64 m=k-2,B=k*(k-1)/2;
        u64 minimum=std::max(k,(m+integer_sqrt(5*m*m))/2+1);
        u64 maximum=std::min(B/2,(k<802?10:5)*m-1);
        u64 lower=read32(input),upper=read32(input);
        assert(minimum-1<=lower && lower<upper && upper<=maximum+1);
        if(k<small) {
            assert(lower==minimum-1 && upper==maximum+1);
            ++retained_all;
        }
        if(lower>=minimum) {
            Bound D=logarithmic_ratio(k,lower);
            assert(D.high<0);
            ++lower_checks;
        }
        if(upper<=maximum) {
            Bound D=logarithmic_ratio(k,upper);
            assert(D.low>2*LN2.high);
            ++upper_checks;
        }
        max_width=std::max(max_width,upper-lower-1);
        for(u64 t=lower+1;t<upper;++t) {
            u64 A=B;
            if(2*t==A)++coincident_branches;
            for(unsigned side=0;side<2;++side) {
                int index=input.get();assert(index!=EOF);
                assert(unsigned(index)<prime_list.size());
                unsigned q=prime_list[index];
                if(lookup[index]==nullptr)lookup[index]=new PascalPrime(q);
                const PascalPrime &P=*lookup[index];
                u64 original_k=(side==0?t:A-t);
                unsigned L=P.binomial(A,t);
                unsigned X=P.binomial(k*k,4*k-4);
                unsigned rhs=((original_k%q)*(original_k%q)+X)%q;
                assert(L!=rhs);
                ++witnesses;
                max_prime=std::max(max_prime,u64(q));
            }
        }
        if(k%262144==0)
            std::cerr<<"verified i="<<k<<" witnesses="<<witnesses<<"\n";
    }
    assert(input.get()==EOF);
    assert(!input.bad());
    for(auto pointer:lookup)delete pointer;
    std::ofstream out(output_path);assert(out.good());
    out<<"{\n  \"status\": \"all_endpoints_and_congruence_witnesses_verified\",\n"
       <<"  \"i_min\": "<<first<<",\n  \"i_exclusive_max\": "<<last<<",\n"
       <<"  \"covered_i_count\": "<<last-first<<",\n"
       <<"  \"certified_branch_records\": "<<witnesses<<",\n"
       <<"  \"coincident_branch_pairs\": "<<coincident_branches<<",\n"
       <<"  \"distinct_equations\": "<<witnesses-coincident_branches<<",\n"
       <<"  \"unresolved\": 0,\n"
       <<"  \"lower_endpoint_checks\": "<<lower_checks<<",\n"
       <<"  \"upper_endpoint_checks\": "<<upper_checks<<",\n"
       <<"  \"small_i_full_intervals\": "<<retained_all<<",\n"
       <<"  \"max_interval_width\": "<<max_width<<",\n"
       <<"  \"max_witness_prime\": "<<max_prime<<",\n"
       <<"  \"independent_log_scale_power_of_two\": 52,\n"
       <<"  \"independent_atanh_terms\": 28,\n"
       <<"  \"floating_point_operations_in_verifier\": false,\n"
       <<"  \"lucas_digit_method\": \"Pascal recurrence\",\n"
       <<"  \"formal_proof_assistant_executed\": false\n}\n";
    out.close();assert(out.good());
    std::cout<<"VERIFIED "<<last-first<<" consecutive i and "<<witnesses<<" exact modular witnesses.\n";
}
