//LARGEST SUBSTRING WITHOUT REPEATING CHARACTERS - 3 SOLUTIONS
#include<bits/stdc++.h>
using namespace std;

/*PROBLEM STATEMENT:
Given a string, find the length of the longest substring without repeating characters.
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
*/

// Using sliding window technique
//1.Using unordered_set TC: O(n) SC: O(n)
class Solution {
    public: 
        int lengthOfLongestSubstring(string s) {
        int n=s.size();
        int j=0;
        int maxx=0;
        int i=0;
        unordered_set<int> st;
        while(j<n)
            {       
            //char c=s[j]; //Just used for debugging
            if (st.find(s[j]) == st.end())
                st.insert(s[j++]);
            else
                st.erase(s[i++]);

            int stsize=st.size();
            maxx= max(maxx,stsize);
        }
        return maxx;
    }
};
//------------------------------------------------------//

//2.Using vector TC: O(n) SC: O(n)
class Solution {
public: 
    int lengthOfLongestSubstring(string s) {
        int len=0;
        int left=0,right=0;
        int n=s.size();
        vector<int>mpp(256,-1);//256 is the size of ascii and -1 is the default value
        
        while(right<n)
        {
            if(mpp[s[right]]!=-1)//if the character is already present in the substring
                left=max(mpp[s[right]]+1,left);//move left to the next possible position ignoring the repeating char
            
            mpp[s[right]]=right;//update the right position of the character
            len=max(len,right-left+1);//update the length of the substring
            right++;//move the right pointer
        }
        return len;//return the length of the longest substring
     }
};

//------------------------------------------------------//


//3.Using Hash-Map TC: O(n) SC: O(n)
class Solution {
public: 
    int lengthOfLongestSubstring(string s) {
        int len=0;
        int right=0,left=0;
        int n=s.size();
        map<char,int>mp;//map to store the index of the character
        for(int i=right;i<n;i++)//right pointer to traverse the string
        {
            if(mp.find(s[i])!=mp.end())//if the character is already present in the substring
                left=max(left,mp[s[i]]+1);//move left to the next possible position ignoring the repeating char
            mp[s[i]]=i;//update the right position of the character hashmap
            len=max(len,i-left+1);//update the length of the substring 
        }
        return len;//return the length of the longest substring
    }
};

int main()
{
    Solution s;
    int res=s.lengthOfLongestSubstring("abcabcbb");
    cout<<res<<endl;//Output: 3
    return 0;
}

//----THANK YOU-----//
