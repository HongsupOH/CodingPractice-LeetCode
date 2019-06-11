import random

class Solution:

    def __init__(self, nums):
        self.nums = nums
        
    def pick(self, target):
        candi = []
        for i in range(len(self.nums)):
            if self.nums[i]==target:
                candi.append(i)
        ans = random.choice(candi)
        return ans
