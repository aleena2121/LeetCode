class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        day = set(days)
        n = max(day)
        dp = [0]*(n+1)
        val = 0
        for i in range (1,n+1):
            if i not in day:
                dp[i] = dp[i-1]
            elif i in day:
                 dp[i] = min(dp[i - 1] + costs[0],dp[max(0, i - 7)] + costs[1],dp[max(0, i - 30)] + costs[2] )
        print(dp)
        return dp[n]