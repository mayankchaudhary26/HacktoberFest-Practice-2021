#include <stdio.h>
void PrintArray(int *A, int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("%d ", A[i]);
    }
    printf("\n");
}
int partition(int A[], int low, int high)
{
    int pivot = A[low];
    int i = low + 1; 
    int j = high;
    int temp;
    do
    {
        while (A[i] <= pivot) 
        {
            i++;
        }
        while (A[j] > pivot) 
        {  
          j--;
        }
        if (i < j) 
        {
            temp = A[i];
            A[i] = A[j];
            A[j] = temp;
        }
    } while (i < j);
    temp = A[low];
    A[low] = A[j];
    A[j] = temp;
    return j;
}
void quickSort(int A[], int l, int h)
{
    int pIndex; 
    if (l < h)
    {
        pIndex = partition(A, l, h); 
        quickSort(A, l, pIndex - 1);  
        quickSort(A, pIndex + 1, h); 
        
    }
}
int main()
{
    int A[] = {9, 3, 2, 2, 7, 9, 13, 5};
    int n = 8;
    printf("***The given set of elements*** \n");
    printf("\n");
    PrintArray(A, n);
    quickSort(A, 0, n - 1);
    printf("\n");
    printf("***After running Quick Sort***\n");
    printf("\n");
    PrintArray(A, n);
}