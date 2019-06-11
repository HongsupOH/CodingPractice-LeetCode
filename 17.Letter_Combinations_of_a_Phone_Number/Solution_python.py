class Solution:
    def letterCombinations(self, digits):
        dic = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res = [""]
        if digits == "":
            return []
        for digit in digits:
            node = dic[digit]
            tmp = []
            for char in node:
                for Str in res:
                    tmp.append(Str+char)
            res = tmp
        return res
