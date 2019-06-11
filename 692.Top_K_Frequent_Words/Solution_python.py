import heapq

class Solution:
    def topKFrequent(self, words, k):
        eles = list(set(words))
        arr = []
        for ele in eles:
            count = words.count(ele)
            heapq.heappush(arr,(-count,ele))
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(arr)[1])
            count+=1
        return ans
