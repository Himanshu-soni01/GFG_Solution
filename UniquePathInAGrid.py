mod = 10**9 + 7
class Solution:
    def uniquePaths(self, n, m, grid):
        # code here 
        dp = [[-1 for i in range(n)] for j in range(m)]

        return self.dfs(0,0,n,m,grid,dp)
        
    def dfs(self,i,j,r,c,grid,dp):
        if (i>=r or j>=c or i<0 or j<0):
            return 0
            
        if (grid[i][j]==0):
            return 0
        
        if(i==r-1 and j==c-1):
            return 1
        
        if (dp[i][j]!=-1):
            return dp[i][j]
        
        dp[i][j] = (self.dfs(i,j+1,r,c,grid,dp)%mod + self.dfs(i+1,j,r,c,grid,dp)%mod )%mod
        return dp[i][j]
