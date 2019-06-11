class Solution:
    def largestOverlap(self, A, B) -> int:
        dic = dict()
        m = len(A)
        n = len(B)
        a,b = [],[]
        for i in range(m):
            for j in range(n):
                if A[i][j]==1:
                    a.append((i,j))
                if B[i][j]==1:
                    b.append((i,j))
        
        for pa in a:
            for pb in b:
                pc = (pa[0]-pb[0],pa[1]-pb[1])
                if pc not in dic:
                    dic[pc]=1
                else:
                    dic[pc]+=1
        best = 0
        for key in dic:
            best = max(best,dic[key])
        return best
