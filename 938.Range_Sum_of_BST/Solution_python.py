class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self,root,L,R):
        stack = [root]
        total = 0
        while stack:
            node = stack.pop()
            if node:
                if L<=node.val<=R:
                    total+=node.val
                stack.append(node.left)
                stack.append(node.right)
        return total
