package com.company;

public class SortedElementOfInfiniteLength {
    public static void main(String[] args)
    {
        int [] arr ={1, 3, 4, 5, 6, 7, 8, 9,10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20};
        int target = 1;
        int index = startend(arr, target);
        System.out.println(index);
    }

    public  static int startend(int [] a, int t)
    {
        int start = 0;
        int end = 1;
        while (a[end] < t)
        {
            int temp = end + 1;
            end = end + (end - start+1)*2;
            start = temp;
        }
        return binarysearch(a, t, start, end);
    }

    public static int binarysearch(int [] a, int t, int s, int e)
    {
        while (s <= e)
        {
            int mid = s + (e-s)/2;
            if(t < a[mid])
            {
                e = mid - 1;
            }
            else if(t > a[mid]){
                s = mid+1;
            }
            else{
                return mid;
            }
        }
        return -1;
    }
}
