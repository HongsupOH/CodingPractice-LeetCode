class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
         
from collections import defaultdict
class Solution:
    def findMode(self, root):
        if root is None:
            return []
        arr = self.bfs(root)
        info = defaultdict(list)
        ch = list(set(arr))
        for ele in ch:
            count = arr.count(ele)
            info[count].append(ele)
        best = max(info)
        return info[best]
        
    def bfs(self,root):
        queue = [root]
        res = []
        while queue:
            node = queue.pop()
            if node:
                res.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        return res
