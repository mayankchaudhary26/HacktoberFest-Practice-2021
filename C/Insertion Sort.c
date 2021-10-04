#include <stdio.h>

int main(){
    int arr[10],n,temp=0;
    printf("Enter the size of array: ");
    scanf("%d",&n);
    printf("Enter array elements: ");
    for(int i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    printf("Your original array:\n");
    for(int i=0;i<n;i++){
        printf("| %d |",arr[i]);
    }
    for (int i=1; i<n; i++){
        for(int j = i-1;j>=0;j--){
            if(arr[j]>arr[i]){
                temp = arr[j];
                arr[j] = arr[i];
                arr[i] = temp;
                i--;
            }
        }
    }
    printf("\nYour sorted array:\n");
    for(int i=0;i<n;i++){
        printf("| %d |",arr[i]);
    }
}
