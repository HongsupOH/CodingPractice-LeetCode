class Solution:
    def numEnclaves(self, A):
        queue = []
        m = len(A)
        n = len(A[0])
        for i in range(m):
            for j in range(n):
                if A[i][j]==1 and (i==0 or i==m-1 or j==0 or j==n-1):
                    queue.append((i,j))
        visit = set()
        while queue:
            y,x = queue.pop(0)
            for y2,x2 in (y-1,x),(y+1,x),(y,x-1),(y,x+1):
                if 0<=y2<m and 0<=x2<n and A[y2][x2]==1 and (y2,x2) not in visit:
                    queue.append((y2,x2))
                    visit.add((y2,x2))
            A[y][x]=0
        count = 0
        for row in A:
            count+=row.count(1)
        return count
