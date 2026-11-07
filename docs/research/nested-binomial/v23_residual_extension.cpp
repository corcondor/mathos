#include <bits/stdc++.h>
using namespace std;
using i128 = __int128_t;
using u128 = __uint128_t;
using ll=long long;

string s128(i128 x){ if (x==0)return "0"; bool neg=x<0; if(neg)x=-x;string s="";while(x){s.push_back('0'+(int)(x%10));x/=10;}if(neg)s.push_back('-');reverse(s.begin(),s.end());return s; }
ll gc(ll a,ll b){return std::gcd(a,b);}
ll isqrt128(i128 n){
  if(n<0) return -1;
  long double z=(long double)n;
  ll x=(ll)sqrtl(z);
  while((i128)x*x>n)--x;
  while((i128)(x+1)*(x+1)<=n)++x;
  return x;
}
int bit_length(ll n){int c=0;while(n){c++;n>>=1;}return c;}
int combsmall(int n,int k){ if(k<0||k>n)return 0;ll ans=1;for(int i=1;i<=k;i++)ans=ans*(n-i+1)/i;return (int)ans; }
int lucas(i128 n,i128 k,int p){
  if(k<0||k>n)return 0;ll ret=1;
  while(n||k){int ni=(int)(n%p),ki=(int)(k%p);if(ki>ni)return 0;ret=(ret*combsmall(ni,ki))%p;n/=p;k/=p;}
  return (int)ret;
}
int modular_witness(ll n,ll r,int side){
  i128 A=(i128)n*(n-1)*(n-2)/6;
  i128 k=(side==0? (i128)r : A-r),m=6*(i128)n-9;
  const int ps[]={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97};
  for(int p:ps){
   int left=lucas(A,r,p);
   int right=(lucas((i128)n*n,m,p)+(int)((k%p)*(k%p)%p))%p;
   if(left!=right) return p;
  }
  return 0;
}
int main(int argc,char**argv){
  ll lo=argc>1?stoll(argv[1]):4097,hi=argc>2?stoll(argv[2]):8192;
  ll counts[7]={};
  const int bs[]={1,2,3,6,9,18,27,54,81,162,243,486};
  for(ll rho=lo;rho<=hi;rho++){
    int rr=rho%9;
    if(rr!=1&&rr!=4&&rr!=6&&rr!=7)continue;
    ll amax=isqrt128((i128)152*rho*bit_length(rho));
    for(ll b:bs)for(ll a=b+1;a<=amax;a++){
     counts[0]++;
     if(27*a<31*b||gc(a,b)!=1||gc(a,rho)!=gc(a,3)||(a*a-rho)%b!=0||(rho-a-b)%2!=0)continue;
     ll a2=a*a,b2=b*b;
     if(a2<=b2+rho || 1377*rho>=216*a2+760*b2)continue;
     counts[1]++;
     i128 z=(i128)a2-b2-rho;
     i128 F=(i128)b2*(6*a2+2*b2+3*rho)*(6*a2+2*b2+3*rho)+4*z*z*z;
     if(F<0)continue;
     // Modular square filters; 0,1,4,9,16,25,36,49 mod 64 etc.
     // safer dynamic test, since static table might omit residues modulo 64.
     int mod64=(int)(F%64); bool valid64=false;
     for(int yy=0;yy<64;yy++) if(yy*yy%64==mod64){valid64=true;break;}
     if(!valid64)continue;
     ll y=isqrt128(F);if((i128)y*y!=F)continue;
     counts[2]++;
     for(int sign:{-1,1}){
      i128 tnum=2*(i128)a*(a2+3*b2)-(i128)rho*(3*b+2*a)+(i128)sign*y;
      ll den=2*b*rho;
      if(tnum%den)continue;
      i128 t=tnum/den;
      if(t<=0)continue;
      counts[3]++;
      i128 q=t*t+3*t+3;
      i128 nnum=(i128)b2*q+(i128)a*b*(t+6)-a2+rho;
      if(nnum%(9*a*b))continue;
      i128 n=nnum/(9*a*b);
      counts[4]++;
      i128 r=3*n+t;
      if(n<104||t*t<=9*n||3*r>=10*n)continue;
      counts[5]++;
      if(n > LLONG_MAX || r>LLONG_MAX){cerr<<"overflow n/r\n";return 2;}
      ll N=(ll)n,R=(ll)r;
      ll M=gc(N,3)*gc(N-1,6);
      i128 Q=n*(n-1)/M;
      // gcd(i128, i128)
      auto gcd128=[](i128 x,i128 y){while(y){i128 t=x%y;x=y;y=t;}return x;};
      i128 delta=Q/gcd128(Q,r*r);
      int p1=modular_witness(N,R,0), p2=modular_witness(N,R,1);
      cout<<"POINT rho="<<rho<<" n="<<N<<" t="<<s128(t)<<" a="<<a<<" b="<<b<<" delta="<<s128(delta)<<" p1="<<p1<<" p2="<<p2<<"\n";
      if(delta>=25)counts[6]++;
     }
    }
  }
  cout<<"RANGE "<<lo<<" "<<hi<<"\n";
  cout<<"COUNTS attempts="<<counts[0]<<" primitive="<<counts[1]<<" square="<<counts[2]<<" t="<<counts[3]<<" n="<<counts[4]<<" branch="<<counts[5]<<" delta25="<<counts[6]<<"\n";
}
