class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [0] * n
        dp[n-1] = grid[m-1][n-1]  
        
        for j in range(n-2, -1, -1):
            dp[j] = grid[m-1][j] + dp[j+1]
        
        for i in range(m-2, -1, -1):
            dp[n-1] += grid[i][n-1]
            
            for j in range(n-2, -1, -1):
                dp[j] = grid[i][j] + min(dp[j], dp[j+1])
        
        return dp[0]