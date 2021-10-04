#include<bits/stdc++.h>
using namespace std;

/*
PROBLEM STATEMENT:
Given an array of strings, group anagrams together.
    
Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
    ["bat"],
    ["nat", "tan"],
    ["ate", "eat","tea"],
]
    
Explanation:
Note: bat -> no element in the group are anagram of this.
      tan is anagram of nat, and nat is anagram of tan.
      ate -> eat -> tea is anagram to each other.
*/

//Using Unordered Map - TC: O(n) SC: O(n)
class Solution
{
    public:
    vector<vector<string>>groupAnagrams(vector<string>&s)
    {
        unordered_map<string,vector<string>>mp;
        vector<vector<string>>ans;
        for(auto it:s)
        {
            string temp=it;
            sort(temp.begin(),temp.end());
            mp[temp].push_back(it);
        }
        for(auto i:mp)
        {
            ans.push_back(i.second);
        }
        return ans;
    }
};


int main()
{
    vector<string> s={"eat","tea","tan","ate","nat","bat"};
    Solution obj;
    vector<vector<string>>st=obj.groupAnagrams(s);
    for(auto it:st)
    {
        for(auto i:it)
        {
            cout<<i<<" ";
        }
        cout<<"\n";
    }
}

//--------------Hope you find this useful-------------//