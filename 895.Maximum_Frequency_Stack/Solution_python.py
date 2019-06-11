from collections import defaultdict
import heapq

class FreqStack:
    """
    solution using priority queue and dictionary
    """

    def __init__(self):
        self.h = []
        self.count = defaultdict(int)
        self.ind = 0
        
    def push(self, x: int) -> None:
        self.count[x]+=1
        heapq.heappush(self.h,(-self.count[x],-self.ind,x))
        self.ind +=1
            
    def pop(self) -> int:
        info = heapq.heappop(self.h)
        self.count[info[2]]-=1
        return info[2]
