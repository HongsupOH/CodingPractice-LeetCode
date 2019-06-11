class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self,root):
        if root is None:
            return True
        stack = [[root.right,root.left]]
        while stack:
            node1,node2 = stack.pop()
            if node1 and node2:
                if node1.val != node2.val:
                    return False
                else:
                    stack.append([node1.left,node2.right])
                    stack.append([node1.right,node2.left])
            elif (node1 and not node2) or (node2 and not node1):
                return False
        return True
