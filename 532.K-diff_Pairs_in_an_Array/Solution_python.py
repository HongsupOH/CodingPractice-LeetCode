from collections import Counter

class Solution:
    def findPairs(self, nums, k):
        if k < 0:
            return 0
        if k == 0:
            counter = Counter(nums)
            return sum(1 for n, c in counter.most_common() if c > 1)
        nums = set(nums)
        diffs = set(x - k for x in nums)
        return sum(1 for x in nums if x in diffs)
