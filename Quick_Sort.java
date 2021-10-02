import java.util.*;

public class QuickSort{
    
    public static void swap(int [] arr,int i,int j){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    
    public static int partitionOverPivot(int [] arr,int si,int ei,int Pidx){
        int p = si - 1, itr = si;
        swap(arr,Pidx,ei);
        while(itr <= ei){
            if(arr[itr] <= arr[ei])
                swap(arr,++p,itr);
            itr++;
        }
        return p;
    }
    
    public static void Quicksort(int [] arr,int si,int ei){
        if(si >= ei)
            return;
        
        int Pidx = ei; // you can use si,ei,mid,or random as well
        int p = partitionOverPivot(arr,si,ei,Pidx);
        
        Quicksort(arr,si,p-1);
        Quicksort(arr,p+1,ei);
    }
    
    public static Scanner sc = new Scanner(System.in);
    public static void main(String [] args){
        int [] arr = {34,2,4,-30,34,2,6,45,-3};
        Quicksort(arr,0,arr.length-1);
        for(Integer i : arr)
            System.out.print(i + " ");
    }
}
