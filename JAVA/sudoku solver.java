Sudoku solver
krishan821

import java.util.*;
public class SUDOKUSOLVER {

	public static void main(String[] args) {
		
		    Scanner sc=new Scanner(System.in);
		    int n=sc.nextInt();
		    int[][]grid=new int[n][n];
		    for(int i=0;i<grid.length;i++)
		    {
		        for(int j=0;j<grid[0].length;j++)
		        {
		            grid[i][j]=sc.nextInt();
		        }
		    }
		    sudoko(grid,0,0);
		    }
		    public static boolean sudoko(int[][]grid,int row,int col)
		    {
		        if(col==9)
		        {
		            row++;
		            col=0;
		        }
		        if(row==9)
		        {
		            display(grid);
		            return true;
		        }
		        if(grid[row][col]!=0)
		        {
		            sudoko(grid,row,col+1);
		        }
		        else{
		            for(int val=1;val<=9;val++)
		            {
		                if(is_it_safe(grid,row,col,val))
		                {
		                    grid[row][col]=val;
		                    boolean ans=sudoko(grid,row,col+1);
		                    if(ans)
		                    {
		                        return true;
		                    }
		                    grid[row][col]=0;
		                }
		            }
		          
		        }
		        return false;
		    }
		    public static boolean is_it_safe(int[][]grid,int row,int col,int val)
		    {
		        int r=0;
		        int c=col;
		        while(r<grid.length)
		        {
		            if(grid[r][c]==val)
		            {
		                return false;
		            }
		            r++;
		        }
		        r=row;
		        c=0;
		        while(c<grid[0].length)
		        {
		            if(grid[r][c]==val)
		            {
		                return false;
		            }
		            c++;
		        }
		        r=(row/3)*3;
		        c=(col/3)*3;
		        for(int i=r;i<r+3;i++)
		        {
		            for(int j=c;j<c+3;j++)
		            {
		                if(grid[i][j]==val)
		                {
		                    return false;
		                }
		            }
		        }
		        return true;
		    }
		    public static void display(int[][]board)
		    {
		        for(int i=0;i<board.length;i++)
		        {
		            for(int j=0;j<board[0].length;j++)
		            {
		                System.out.print(board[i][j]+" ");
		            }
		            System.out.println();
		        }
		    }
		}