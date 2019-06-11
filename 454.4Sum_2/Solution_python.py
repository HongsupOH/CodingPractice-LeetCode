#Sol.1(Brute Force)
#Time Limit Error
class Solution:
    def fourSumCount(A,B,C,D):
        res = 0
        for i in range(len(A)):
            for j in range(len(B)):
                for k in range(len(C)):
                    for l in range(len(D)):
                        if A[i]+B[j]+C[k]+D[l]==0:
                            res+=1
        return res

#Sol.2 (BFS)
#TIme Limit Error
class Solution:
    def fourSumCount(self, A, B, C, D):
        if A==[] and B==[] and C==[] and D==[]:
            return 0
        count = 0
        arr = [A,B,C,D]
        m = len(arr)
        queue = [([-1],0)]
        while queue:
            path,total = queue.pop(0)
            if len(path)==5 and total==0:
                count+=1
            point = path[-1]
            new_point = point+1
            if new_point<m:
                for ele in arr[new_point]:
                    new_path = path + [new_point]
                    new_t = total+ele
                    queue.append((new_path,new_t))
        return count

#Sol.3 (Dictionary)
#Pass
class Solution:
    def fourSumCount(self, A, B, C, D):
        res = 0
        counter = {}
        for a in A:
            for b in B:
                counter[a+b] = counter.get(a+b, 0) + 1
        for c in C:
            for d in D:
                res += counter.get(-c-d, 0)
        return res
