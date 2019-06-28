class UnionFind:
    def __init__(self,n):
        self.parents = list(range(n))
        self.ranks = [0]*n

    def find(self,x):
        if x!=self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def Union(self,x,y):
        rx = self.find(x)
        ry = self.find(y)
        if rx==ry:
            return True
        if self.ranks[rx]>self.ranks[ry]:
            self.parents[ry] = rx
        elif self.ranks[rx]<self.ranks[ry]:
            self.parents[rx] = ry
        else:
            self.parents[ry] = rx
            self.ranks[rx]+=1

class Solution:
    def findRedundantConnection(self,edges):
        uf = UnionFind(len(edges)+1)
        for e in edges:
            if uf.Union(e[0],e[1]):
                return e
                


if __name__=="__main__":
    edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
    s = Solution()
    print(s.findRedundantConnection(edges))
    """
    ANS: [1, 4]

    """
