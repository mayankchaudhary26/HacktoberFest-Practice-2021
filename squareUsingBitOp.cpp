#include <iostream>
using namespace std;
// cant handle negative numbers as of now
int power(int n) {
    if(n==0) return 0;
    int temp = n;
    int ans = 0; int i=0;
    while(temp) {
        if(temp&1) {
            ans += n;
        }
        temp=temp>>1;
        n=n<<1;
    }
    return ans;
}

int main() {
    int n; cin>>n;
    while(n>0) 
        cout<<power(n--)<<'\n';
    return -1;
}
