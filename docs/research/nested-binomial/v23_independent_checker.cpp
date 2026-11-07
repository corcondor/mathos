/* Independent v23 enumeration: b,a,rho order (not rho,b,a), modular rho progression,
 * direct expanded sextic, integer exact verification. No shared headers with producer.
 */
#include <algorithm>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;
using Int = __int128_t;
using ll = long long;
ll sqrt_exact(Int x){ if(x<0)return -1;
 long double approx=sqrtl((long double)x);
 ll k=(ll)approx;
 while((Int)k*k>x)k--;
 while((Int)(k+1)*(k+1)<=x)k++;
 return k;
}
int digits2(ll x){int n=0; while(x>0){n++; x/=2;}return n;}
string print_int(Int v){bool neg=v<0;if(neg)v=-v;string s;do{s.push_back('0'+v%10);v/=10;}while(v); if(neg)s.push_back('-'); reverse(s.begin(),s.end());return s;}
Int gcd_big(Int a, Int b){while(b){Int r=a%b;a=b;b=r;}return a;}
Int sextic_direct(ll a,ll b,ll rho){
 Int A=a, B=b, R=rho;
 Int aa=A*A,bb=B*B;
 return 4*aa*aa*aa +(24*bb-12*R)*aa*aa+(36*bb*bb+60*bb*R+12*R*R)*aa-3*bb*R*R-4*R*R*R;
}
bool sq_mod(int r, int p){for(int j=0;j<p;j++)if((j*j)%p==r)return true;return false;}
int main(int argc,char**argv){
 ll low=argc>1?stoll(argv[1]):4097;
 ll top=argc>2?stoll(argv[2]):32768;
 const ll divs[]={1,2,3,6,9,18,27,54,81,162,243,486};
 ll square=0,pos_t=0,int_n=0,branch=0,delta25=0;
 ll a_max=sqrt_exact((Int)152*top*digits2(top));
 for(ll b:divs){
  for(ll a=b+1;a<=a_max;a++){
   if(27*a<31*b || gcd(a,b)!=1) continue;
   ll a2=a*a,b2=b*b;
   ll rrmin=max(low, (a2+152*digits2(top)-1)/(152*digits2(top)));
   ll rrmax=min({top,a2-b2-1,(216*a2+760*b2-1)/1377});
   if(rrmax<rrmin)continue;
   ll cur=rrmin+((a2-rrmin)%b+b)%b;
   for(ll rho=cur;rho<=rrmax;rho+=b){
    int rem=rho%9;
    if(rem!=1&&rem!=4&&rem!=6&&rem!=7)continue;
    if(a2>152*rho*digits2(rho))continue;
    if(gcd(a,rho)!=gcd(a,3)||(rho-a-b)%2)continue;
    Int f=sextic_direct(a,b,rho);
    if(f<0)continue;
    if(!sq_mod((int)(f%16),16)||!sq_mod((int)(f%9),9))continue;
    ll root=sqrt_exact(f);
    if((Int)root*root!=f)continue;
    square++;
    for(int sg : {-1,+1}){
     Int top_t= 2*(Int)a*(a2+3*b2)-(Int)rho*(3*b+2*a)+(Int)sg*root;
     ll bot_t=2*b*rho;
     if(top_t%bot_t)continue;
     Int t=top_t/bot_t;
     if(t<=0)continue;
     pos_t++;
     Int q=t*t+3*t+3;
     Int numer_n=b2*q+(Int)a*b*(t+6)-a2+rho;
     Int denom_n=9*(Int)a*b;
     if(numer_n%denom_n)continue;
     Int n=numer_n/denom_n;
     int_n++;
     Int r=3*n+t;
     if(n<104||t*t<=9*n || 3*r>=10*n)continue;
     branch++;
     if(n>INT64_MAX||r>INT64_MAX){cerr<<"Overflow";return 3;}
     ll nn=(ll)n, rr=(ll)r;
     ll M=gcd(nn,3LL)*gcd(nn-1,6LL);
     Int Q=n*(n-1)/M;
     Int delta=Q/gcd_big(Q,r*r);
     if(delta>=25)delta25++;
     // Independent check of (1) and (2) for every branch point.
     if((Int)81*a*n*(n-1)!=(Int)b*(9*n*q+t*t*t))return 4;
     if(rho!=(Int)a*a+(Int)a*b*(9*n-t-6)-(Int)b*b*q)return 5;
     // Independent factorization-based v23 statements.
     // For finite samples only, full proof is mathematical.
     cout<<"POINT rho="<<rho<<" n="<<print_int(n)<<" t="<<print_int(t)
         <<" a="<<a<<" b="<<b<<" delta="<<print_int(delta)<<"\n";
    }
   }
  }
 }
 cout<<"RANGE "<<low<<" "<<top<<"\n";
 cout<<"COUNTS square="<<square<<" t="<<pos_t<<" n="<<int_n<<" branch="<<branch<<" delta25="<<delta25<<"\n";
}
