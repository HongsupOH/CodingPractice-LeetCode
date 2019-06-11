class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    """
    solution using inorder traverse of DFS (Left,Root,Right)
    Then output arrays must be ascending order
    """
    def isValidBST(self, root):
        output = self.Inorder_DFS(root)
        for i in range(len(output)-1):
            if output[i]>=output[i+1]:
                return False
        return True
    
    def Inorder_DFS(self,root):
        stack = [(False,root)]
        res = []
        while stack:
            visit,node = stack.pop()
            if node:
                if visit:
                    res.append(node.val)
                else:
                    stack.append((False,node.right))
                    stack.append((True,node))
                    stack.append((False,node.left))
        return res
