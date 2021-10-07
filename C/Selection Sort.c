#include <stdio.h>
#include <stdlib.h>
void selection_sort(int A[],int n);

int main()
{
  int a[50],i,j,n,t;

  printf("how many element you want to input: ");
  scanf("%d",&n);
  printf("Now enter %d element one by one\n:",n);
  for(i=0;i<n;i++)
  {
      scanf("%d",&a[i]);

  }
  printf("\n Your elements are:");
  for(i=0;i<n;i++)
  {
      printf("%d",a[i]);

  }
  for(i=0;i<n-1;i++)
  {
      for(j=i+1;j<n;j++)
      {
          if(a[i]>a[j])
          {
              t = a[i];
              a[i]=a[j];
              a[j]=t;
          }


      }
  }
  printf("\nThe sorted elements in asscending order are:\n");
  for(i=0;i<n;i++)
  {
      printf("%d",a[i]);

  }

}