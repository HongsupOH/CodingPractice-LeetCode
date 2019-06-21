class Solution:
    def canPartition(self, nums):
        n = len(nums)
        if n == 1:
            return False
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        nums.sort(reverse=True)
        for i in range(n):
            tmp = 0
            for j in range(i, n):
                if tmp + nums[j] == target:
                    return True
                elif tmp + nums[j] < target:
                    tmp += nums[j]
        return False
