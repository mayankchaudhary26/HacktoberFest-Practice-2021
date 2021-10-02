'''
QUESTION : N-QUEEN
==================
You are given N, and for a given N x N chessboard, find a way to place N queens such that no queen can attack any other queen on the chess board. A queen can be killed when it lies in the same row, or same column, or the same diagonal of any of the other queens. You have to print all such configurations.
--------------------------------------
Input Format :
    line1 : integer N
--------------------------------------
Output Format :
    One Line for every board configuration. 
    Every line will have N*N board elements printed row wise and are separated by space
'''

def isSafe(row,col,ans,n):
    #check for vertical direction
    i=row-1
    while i>=0:
        if ans[i][col]==1:
            return False
        i-=1

    i=row-1
    j=col-1
    while i>=0 and j>=0:
        if ans[i][j]==1:
            return False
        i-=1
        j-=1

    i=row-1
    j=col+1
    while i>=0 and j<n:
        if ans[i][j]==1:
            return False
        i-=1
        j+=1 
    # if everything is fine then return True
    return True

def nQueenHelper(row,n,ans):
    if row==n:
        for ele in ans:
            for elem in ele:
                print(elem,end=" ")
        print()
        return
    
    for col in range(n):
        if isSafe(row,col,ans,n):
            ans[row][col]=1
            nQueenHelper(row+1,n,ans)
            ans[row][col]=0
    return

def nQueen(n):
    ans=[[0 for i in range(n)] for j in range(n)]
    nQueenHelper(0,n,ans)


n = int(input())
nQueen(n)
