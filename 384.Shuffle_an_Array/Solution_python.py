class Solution:

    def __init__(self, nums):
        self.arr = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        return self.arr

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        shuffled = self.arr[:]
        for i in range(len(shuffled)-1,0,-1):
            j = random.randint(0,i)
            shuffled[i],shuffled[j]= shuffled[j],shuffled[i]
        return shuffled

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
