#include <bits/stdc++.h>
using namespace std;

/*
Input: ["vijay","vimal","vinoth"]
Output: "vi"
Code explanation: first taking --> vijay's - s[0][i] i=0 --> 'v'
                  Then comparing 1st indx with all other strings in the vector
                  If 'v' is common in all strings, then we return "v"

                  second taking --> vijay's - s[0][i] i=1 --> 'i'  
                  Then comparing 2nd indx with all other strings in the vector
                  If 'i' is common in all strings, then we return "vi"

                  third taking --> vijay's - s[0][i] i=2 --> 'j'
                  Then comparing 3rd indx with all other strings in the vector
                  If 'j' is common in all strings, then we return "vij"
                  else return upto the last common prefix

                  if none of the above is common, then return ""
*/

//Naive approach TC: O(n^2) SC: O(1)
string longestCommonPrefix(vector<string>s)
{
    int m=s[0].size();
    int n=s.size();
    string temp="";
    for(int i=0;i<m;i++)
    {
        for(int j=1;j<n;j++)
        {
            if(s[0][i]!=s[j][i])
                return temp;
        }
        temp+=s[0][i];
    }
    return temp;
}

//-----------------------------------------------------------------//

//Sorting the string array and compare 1st and last strings only  
//TC: O(nlogn) SC: O(1)
string longestCommonPrefix(vector<string>& strs) {
    if( strs.size() == 0 ) return "";
    sort(strs.begin(), strs.end());//sorting strings in the array
    string f = strs[0];//stores first string
    string l = strs[strs.size()-1];//stores last string
    string result="";//stores the resultant string-->common prefix
        int n = f.size(), m = l.size();
        for(int i =0; i < n && i < m && f[i] == l[i]; i++)
        {
            //char a=f[i]; Used for debugging
            //char b=l[i]; Used for debugging
            result += f[i];
        }
    return result;
}

int main()
{
    
    vector<string>s = {"vimal","vijay","vimnoth"};
    string res = longestCommonPrefix(s);    
    cout<<res<<endl;
    return 0;
}

//---------Thank You---------------//
//--------Hope this helpfull--------//
