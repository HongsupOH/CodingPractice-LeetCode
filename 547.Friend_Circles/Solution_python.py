class Solution:
    def findCircleNum(self, M):
        n = len(M)
        data = [x for x in range(n)]
        connections = []
        for i in range(n):
            for j in range(n):
                if M[i][j]==1:
                    connections.append((i,j))
        for i,j in connections:
            self.union(data,i,j)
        return len(set(self.find(data,i) for i in range(n)))
    
    def union(self,data,i,j):
        pi = self.find(data,i)
        pj = self.find(data,j)
        if pi!=pj:
            data[pi]=pj
            
    def find(self,data,i):
        if i!=data[i]:
            data[i] = self.find(data,data[i])
        return data[i]
