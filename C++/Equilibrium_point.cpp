#include<bits/stdc++.h>
using namespace std;

int equilibriumPoint(int arr[], int n)
{
    if(n==1)
     return 1;

    int Ls=0,Rs=0,sum=0;
    for(int i=0;i<n;i++)
    {sum+=arr[i];}
    Rs=sum;
    for(int i=1;i<n;i++)
    {
        Ls+=arr[i-1];
        Rs=sum-Ls-arr[i];
        if(Ls==Rs)
        {
            return i+1;
        }
    }
    return -1;
}

int main()
{
    int n;
    cin>>n;
    int arr[n];
    for(auto&x:arr)
    {
        cin>>x;
    }
    cout<<equilibriumPoint(arr,n);
}
