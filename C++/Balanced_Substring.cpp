#include<bits/stdc++.h>
using namespace std;
#define ll                   long long

#define intmax               INT_MAX
#define intmin               INT_MIN
#define fo(i,n)              for(int i=0;i<n;i++)
#define fol(i,n)              for(ll i=0;i<n;i++)
#define Fo(i,k,n)            for(int i=k;k<n?i<n:i>n;k<n?i+=1:i-=1)
#define Fol(i,k,n)            for(ll i=k;k<n?i<n:i>n;k<n?i+=1:i-=1)
#define pb                   push_back
#define mp                   make_pair
#define F                    first
#define S                    second
#define endl                 "\n" 
#define all(x)               x.begin(), x.end()
#define sortall(x)           sort(all(x))
#define co(x)                cout<<x<<endl;
#define ci(x)                cin>>x;
typedef pair<int, int>	     pii;
typedef pair<ll, ll>	       pll;
typedef vector<int>	       	 vi;
typedef vector<ll>		       vl;
typedef vector<pii>		       vpii;
typedef vector<pll>		       vpll;
typedef vector<vi>		       vvi;
typedef vector<vl>		       vvl;
int mpow(int base, int exp);

const int mod = 1'000'000'007;
const int N = 3e5, M = N;
//=======================
int a[N];


void solve() {
    int n;
    cin>>n;
    string s;
    cin>>s;
    fo(i,n-1){
        if(((s[i] == 'a' && s[i+1] == 'b')) || ((s[i] == 'b' && s[i+1] == 'a'))){
            cout<<i+1<<" "<<i+2<<endl;
            return;
        }
        
    }
    cout<<-1<<" "<<-1<<endl;

}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); 
    cout.tie(NULL);    

    int t = 1;
    cin >> t;
    while(t--) {
      solve();
    }

    return 0;
}

int mpow(long long x, int y, int p)
{
    int res = 1; 
    x = x % p; 
    if (x == 0) return 0;
    while (y > 0)
    {
        if (y & 1)
            res = (res*x) % p;
 
        y = y>>1;
        x = (x*x) % p;
    }
    return res;
}
