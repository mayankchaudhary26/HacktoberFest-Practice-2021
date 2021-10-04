#include <stdio.h>
#include <string.h>
#define N 6

int isSafe(char mat[][N], int r, int c)
{
    for (int i = 0; i < r; i++)
    {
        if (mat[i][c] == 'Q') {
            return 0;
        }
    }
 

    for (int i = r, j = c; i >= 0 && j >= 0; i--, j--)
    {
        if (mat[i][j] == 'Q') {
            return 0;
        }
    }
 
    for (int i = r, j = c; i >= 0 && j < N; i--, j++)
    {
        if (mat[i][j] == 'Q') {
            return 0;
        }
    }
 
    return 1;
}
 
void printSolution(char mat[][N])
{  
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++) {
            printf("%c ", mat[i][j]);
        }
        printf("\n");
    }
    printf("\n");
   
}
 
void nQueen(char mat[][N], int r)
{
    if (r == N)
    {
        printSolution(mat);
        return;
    }
    for (int i = 0; i < N; i++)
    {
       
        if (isSafe(mat, r, i))
        {
            
            mat[r][i] = 'Q';
 
             nQueen(mat, r + 1);
            mat[r][i] = '#';
        }
    }
}


	

	

 
int main()
{
    char mat[N][N];
    int result=0;
    memset(mat, '#', sizeof mat);
    int fact,num;
    fact=factorial(N);
    nQueen(mat, 0);
   
 
    
}


