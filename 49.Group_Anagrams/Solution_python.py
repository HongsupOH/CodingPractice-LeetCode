from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        count = defaultdict(list)
        for ele in strs:
            s = sorted(ele)
            word = ''.join(s)
            count[word].append(ele)
        res = []
        for key in count:
            res.append(count[key])
        return res
        
        
