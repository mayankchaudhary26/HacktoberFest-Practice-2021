/* Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

 

Example :

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.*/



//solution

class Solution {
    public int maxSubArray(int[] nums) {
        
        int l=nums.length;
        int i=0,s=0,max=nums[0];
        int[] b = new int[l];
        
        while(i!=l)
        {
            b[i]=nums[i];
            i++;
        }
        Arrays.sort(b);
        if(b[l-1]<=0)
            return b[l-1];
    
        i=0;
        while(i!=l)
        {
            s+=nums[i];
            if(s<0)
            {
                s=0;
            }
            else if(s>max)
                max=s;
            System.out.println(max);
            i++;
        }
        System.out.println(max);
        return max;
    }
}
