class Solution:
    def getRow(self, rowIndex):
        dp = []
        for i in range(rowIndex+1):
            dp.append([1 for x in range(i+1)])
        
        for i in range(rowIndex+1):
            for j in range(len(dp[i])):
                if i>1:
                    if j==0:
                        dp[i][j]=dp[i-1][j]
                    elif j==len(dp[i])-1:
                        dp[i][j]=dp[i-1][j-1]
                    else:
                        dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
        
        return dp[-1]
        
