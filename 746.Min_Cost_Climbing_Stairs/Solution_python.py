class Solution:
    def minCostClimbingStairs(self, cost):
        """
        solution using dynamic programming
        """
        n = len(cost)
        dp = [0]*(n)
        for i in range(n):
            if i<=1:
                dp[i]=cost[i]
            else:
                dp[i]=min(dp[i-1],dp[i-2])+cost[i]
        return min(dp[-1],dp[-2])
