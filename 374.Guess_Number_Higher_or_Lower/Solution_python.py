class Solution(object):
    def guessNumber(self, n):
        """
        solution using binary search
        guess(n) is installed API
        if guess(n)==-1: My number is lower
        if guess(n)== 1: My number is higher
        if guess(n)== 0: Answer
        """
        l = 1
        r = n
        while l<=r:
            mid = (l+r)//2
            if guess(mid)==-1:
                r=mid-1
            elif guess(mid)==1:
                l=mid+1
            elif guess(mid)==0:
                return mid
