class Solution:
    def imageSmoother(self, M):
        m = len(M)
        n = len(M[0])
        ans = [[0 for x in range(n)] for x in range(m)]
        for i in range(m):
            for j in range(n):
                count = 1
                total = M[i][j]
                for y,x in (i+1,j),(i-1,j),(i,j+1),(i,j-1),(i-1,j-1),(i-1,j+1),(i+1,j-1),(i+1,j+1):
                    if 0<=y<m and 0<=x<n:
                        total += M[y][x]
                        count += 1
                ans[i][j]=total//count
        return ans
                        
        
