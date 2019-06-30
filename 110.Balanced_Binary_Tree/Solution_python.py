class Solution:
    def isBalanced(self, root):
        if root is None:
            return True
        left = self.depth(root.left)
        right = self.depth(root.right)
        if abs(left-right)<=1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
        
    def depth(self,root):
        if root is None:
            return 0
        return max(self.depth(root.left),self.depth(root.right))+1
