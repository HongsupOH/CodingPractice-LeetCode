class Solution(object):

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.rects = rects
        self.areas = []
        for rect in rects:
            area = (rect[2]-rect[0]+1)*(rect[3]-rect[1]+1)
            self.areas.append(area)
        self.acc = []
        self.total = 0
        for area in self.areas:
            self.total += area
            self.acc.append(self.total)

    def pick(self):
        """
        :rtype: List[int]
        """
        x = random.randint(0,self.total)
        low = 0
        high = len(self.areas)-1
        while low<high:
            mid = low+(high-low)//2
            if x>self.acc[mid]:
                low = mid+1
            else:
                high = mid
        x1,y1,x2,y2 = self.rects[low]
        x = random.randint(x1,x2)
        y = random.randint(y1,y2)
        return [x,y]
        
