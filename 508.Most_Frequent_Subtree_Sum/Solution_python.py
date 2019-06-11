class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
         
from collections import defaultdict

class Solution:
    def findFrequentTreeSum(self, root: TreeNode):
        if root is None:
            return []
        self.arr = []
        self.sum_arr(root)
        info = defaultdict(list)
        for ele in self.arr:
            count = self.arr.count(ele)
            if ele not in info[count]:
                info[count].append(ele)
        best = max(info)
        return info[best]
        
    def sum_arr(self,root):
        total = self.bfs_sum(root)
        self.arr.append(total)
        if root.left:
            self.sum_arr(root.left)
        if root.right:
            self.sum_arr(root.right)
            
    def bfs_sum(self,root):
        queue = [root]
        total = 0
        while queue:
            node = queue.pop(0)
            if node:
                total+=node.val
                queue.append(node.left)
                queue.append(node.right)
        return total
