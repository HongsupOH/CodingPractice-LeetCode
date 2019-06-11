class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = [[]]
        for num in nums:
            newSet = []
            for res in subsets:
                newRes = res + [num]
                newSet.append(newRes)
            subsets+=newSet
        return subsets
