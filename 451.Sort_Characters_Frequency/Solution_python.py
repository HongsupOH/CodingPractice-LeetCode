import heapq

class Solution(object):
    def frequencySort(self, s):
        """
        solution using priority queue
        """
        word = set(s)
        h = []
        for al in word:
            count = s.count(al)
            heapq.heappush(h,(-count,al))
        ans = ""
        while h:
            info = heapq.heappop(h)
            ans+= info[1]*abs(info[0])
        return ans
