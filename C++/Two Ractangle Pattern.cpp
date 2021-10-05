/*
Output:

1 2 3 4 5 4 3 2 1
1 2 3 4   4 3 2 1
1 2 3       3 2 1
1 2           2 1
1               1

*/

#include<iostream>
using namespace std;

int main(int argc, char *argv[]) {
int count = 0;
int i,j;
int rows = 5;
int temp = rows;
count = rows/2 +1;

for(i = 0 ; i<rows; i++)
{
    for(j=1; j<=temp; j++)
        cout<<j;
    for(j=0; j<i; j++)
        cout<<"  ";
    for(j=temp;j>=1;j--)
        cout<<j;
    cout<<"\n";
    temp--;
}
return 0;

}
