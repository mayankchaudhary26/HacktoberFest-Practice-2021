import java.util.*;

public class MergeSort{
    
    public static int [] MergeTwoSortedArray(int [] arr1,int [] arr2){
        int n = arr1.length,m=arr2.length;
        
        if(n == 0 || m == 0)
            return n == 0 ? arr2 : arr1;
        
        int i=0,j=0,k=0,len = m+n;
        
        int [] arr = new int[len];
        while(i < n && j < m){
            if(arr1[i] < arr2[j])
                arr[k++] = arr1[i++];
            else
                arr[k++] = arr2[j++];
        }
        
        while(i < n){
            arr[k++] = arr1[i++];
        }
        
        while(j < m){
            arr[k++] = arr2[j++];
        }
        
        return arr;
    }
    
    // TC - Nlog(N) SC- Nlog(N)
    public static int [] Merge_Sort(int [] arr,int si,int ei){
        if(si == ei)
            return new int[] {arr[si]};
    
        int mid = (si + ei) / 2;   
        int [] left = Merge_Sort(arr,si,mid);
        int [] right = Merge_Sort(arr,mid+1,ei);
        
        return MergeTwoSortedArray(left,right);
    }
    
    public static Scanner sc = new Scanner(System.in);
    public static void main(String [] args){
        int [] arr = {34,2,4,-30,34,2,6,45,-3};
        arr = Merge_Sort(arr,0,arr.length-1);
        for(Integer i : arr)
            System.out.print(i + " ");
    }

}
