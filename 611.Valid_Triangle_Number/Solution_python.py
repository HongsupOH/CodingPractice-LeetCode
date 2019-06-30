class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                s = nums[i]+nums[j]
                k = bisect.bisect_left(nums[j+1:],s)
                count+=k
        return count
