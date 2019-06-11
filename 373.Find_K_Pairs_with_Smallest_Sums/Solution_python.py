import heapq

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        """
        solution using priority queue
        """
        #Exceptional Case
        if nums1==[] or nums2==[]:
            return []
        #Main Algorithm
        h = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                heapq.heappush(h,(nums1[i]+nums2[j],[nums1[i],nums2[j]]))
        #if k is larger than length of h array
        if k>=len(h):
            ans = []
            while h:
                info =heapq.heappop(h)
                ans.append(info[1])
        #Main Algorithm
        else:
            ans = []
            for _ in range(k):
                info = heapq.heappop(h)
                ans.append(info[1])
        return ans
        
        
