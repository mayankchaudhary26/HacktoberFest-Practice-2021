// https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1

class Solution {
    public static ArrayList<String> findPath(int[][] m, int n) {
        String [] dir = {"U","D","L","R"};
        int [][] dirS = {{-1,0},{1,0},{0,-1},{0,1}};
        ArrayList<String> ans = new ArrayList<>();
        if(n == 0 || m[0][0] == 0 || m[n-1][n-1] == 0)    return ans;
        maze(0,0,ans,"",m,dir,dirS);
        Collections.sort(ans); // As Ques Asked for the lexographical order
        return ans;
    }
    
    public static int maze(int sr,int sc,ArrayList<String> ans,String res,int [][] board,String [] dir,int [][] dirS){
        int n = board.length;
        if(sr == n-1 && sc == n-1){
            ans.add(res);
            return 1;
        }
        
        int count = 0;
        board[sr][sc] = 0;
        
        for(int d=0;d<dir.length;d++){
            int r = sr + dirS[d][0];
            int c = sc + dirS[d][1];
            if(r >= 0 && c >= 0 && r < n && c < n && board[r][c] == 1 ){
                count += maze(r,c,ans,res + dir[d],board,dir,dirS);    
            }
        }
        board[sr][sc] = 1;
        return count;
    }
}

// If you want only one path // This method will be used in Tree
    public static boolean floodfill_jumps(int sr,int sc,int [][] board,String ans,String [] dirS,int [][] dir){
        int m=board[0].length,n=board.length;
        if(sr == n-1 && sc == m-1){
            System.out.println(ans);
            return true;
        }
        
        boolean res = false;
        board[sr][sc] = 1;
        
        for(int d=0;d<dir.length;d++){
            for(int rad=1;rad<=Math.max(n,m);rad++){
                int r = sr + rad*dir[d][0];
                int c = sc + rad*dir[d][1];
                
                if(r >= 0 && c >= 0 && r < board.length && c < board[0].length){
                    if(board[r][c] == 0)
                         res = res || floodfill_jumps(r,c,board,ans + rad + dirS[d],dirS,dir);
                }
            }
        }
        board[sr][sc] = 0;
        return res;
    }
