class Solution:
    def clumsy(self, N):
        ops = self.op(N)
        nums = []
        for i in range(N,0,-1):
            nums.append(i)
        total = str(nums.pop(0))
        while nums:
            op = ops.pop(0)
            total+=op
            cur = str(nums.pop(0))
            total+=cur
        ans = eval(total)
        return ans
        
    def op(self,N):
        b = ['*',"//","+","-"]
        total = N-1
        it = total//len(b)
        re = total%len(b)
        ans = b*it + b[:re]
        return ans
