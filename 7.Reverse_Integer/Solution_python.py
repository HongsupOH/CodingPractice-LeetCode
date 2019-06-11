class Solution:
    def reverse(self, x):
        Minus = False
        if x<0:
            Minus = True
        tmp = str(abs(x))
        ans = ""
        for i in range(len(tmp)-1,-1,-1):
            ans+=tmp[i]
        if Minus:
            res = -int(ans)
            if res<-2**31:
                return 0
            return res
        else:
            res = int(ans)
            if res>=2**31:
                return 0
            return res
