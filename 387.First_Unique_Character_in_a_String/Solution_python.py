class Solution:
    def firstUniqChar(self, s):
        if s is None:
            return -1
        word = set(s)
        h = []
        for ele in word:
            count = s.count(ele)
            if count==1:
                heapq.heappush(h,s.index(ele))
        if len(h)==0:
            return -1
        return heapq.heappop(h)
        
