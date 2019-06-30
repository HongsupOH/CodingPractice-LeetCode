import math
from itertools import combinations

class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        combis = list(combinations(points,3))
        best = 0
        for combi in combis:
            p1 = combi[0]; p2 = combi[1]; p3 = combi[2]
            a = self.distance(p1,p2); b = self.distance(p1,p3); c = self.distance(p2,p3)
            sides = [a,b,c]
            sides.sort()
            if sides[0]+sides[1]>sides[2]:
                best = max(best,self.calculArea(sides[0],sides[1],sides[2]))
        return best
    
    def calculArea(self,a,b,c):
        s = (a+b+c)/2
        return math.sqrt((s*(s-a)*(s-b)*(s-c)))
    
    def distance(self,p1,p2):
        return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
