class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        dp = []
        for i in range(numRows):
            dp.append([1]*(i+1))
        
        for i in range(len(dp)):
            for j in range(len(dp[i])):
                if i>1:
                    if j==0:
                        dp[i][j] = dp[i-1][j]
                    elif j==len(dp[i])-1:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
        return dp
        
