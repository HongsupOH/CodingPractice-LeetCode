class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
         
from collections import defaultdict

class Solution:
    def widthOfBinaryTree(self, root: TreeNode):
        stack = [(0,0,root)]
        info = defaultdict(list)
        while stack:
            lev,pos,node = stack.pop()
            info[lev].append(pos)
            if node:
                if node.right:
                    stack.append((lev+1,pos*2,node.right))
                if node.left:
                    stack.append((lev+1,pos*2+1,node.left))
        best = 0
        for key in info:
            best = max(best,max(info[key])-min(info[key])+1)
        return best
                
