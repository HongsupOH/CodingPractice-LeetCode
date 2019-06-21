from bisect import bisect_right as bs
class Solution(object):
    def advantageCount(self, A, B):
        A.sort()
        r = []
        for n in B[:-1]:
            i = bs(A, n)
            if i == len(A):
                r.append(A.pop(0))
            else:
                r.append(A.pop(i))
        r.append(A[0])
        return r
