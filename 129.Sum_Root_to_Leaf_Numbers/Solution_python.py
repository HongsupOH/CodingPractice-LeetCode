class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def sumNumbers(self, root):
        if root==None:
            return 0
        stack = [(root,str(root.val))]
        res = []
        while stack:
            node,total = stack.pop()
            if node and not node.left and not node.right:
                res.append(int(total))
            if node.left:
                stack.append((node.left,total+str(node.left.val)))
            if node.right:
                stack.append((node.right,total+str(node.right.val)))
        return sum(res)
        
