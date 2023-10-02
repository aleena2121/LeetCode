class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = []
        for i in range (0,n+1):
            if i == 0 or i == 1:
                dp.append(1)
            else :
                x = dp[i-2] + dp[i-1]
                dp.append(x)
            
        return dp[n]
                