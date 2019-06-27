class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        n = len(nums)
        num_with_pos = zip(nums, range(n))
        num_with_pos = sorted(num_with_pos)
        i = 0
        j = 1
        while i < n and j < n:
            if num_with_pos[j][0] - num_with_pos[i][0] <= t:
                if abs(num_with_pos[j][1] - num_with_pos[i][1]) <= k and i != j:
                    return True
                j += 1
            else:
                i += 1
        return False
