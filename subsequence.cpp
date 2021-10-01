#include <bits/stdc++.h>
using namespace std;

string getSequence(string s, int n) {
    string str;
    int sq=0;
    while(n) {
        if(n&1) {
            str+=s[sq];
        }
        sq++; n = n>>1;
    }
    return str;
}

vector<string> getAllSubsequence(string s) {
    int n = s.length();
    vector<string> v;
    for(int i=0;i<(1<<n);i++) {
        v.push_back(getSequence(s, i));
    }
    return v;
}

int main() {
    string s; cin>>s;
    vector<string> allSubsequences = getAllSubsequence(s);
    for(auto it : allSubsequences) {
        cout<<it<<endl;
    }
}
