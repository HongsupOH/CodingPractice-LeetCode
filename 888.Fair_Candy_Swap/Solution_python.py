class Solution:
    def fairCandySwap(self, A, B):
        sumA = sum(A)
        sumB = sum(B)
        diff = abs(sumA-sumB)
        diffe = int(diff/2)
        if sumA>sumB:
            for i in range(len(A)):
                if A[i]-diffe in B:
                    return [A[i],A[i]-diffe]
        elif sumA<sumB:
            for i in range(len(A)):
                if A[i]+diffe in B:
                    return [A[i],A[i]+diffe]
