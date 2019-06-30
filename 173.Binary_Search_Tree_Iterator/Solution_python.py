class BSTIterator:

    def __init__(self, root):
        stack = [(False,root)]
        self.inorder = []
        while stack:
            visit,node = stack.pop()
            if visit:
                self.inorder.append(node.val)
            else:
                if node:
                    stack.append((False,node.right))
                    stack.append((True,node))
                    stack.append((False,node.left))

    def next(self):
        """
        @return the next smallest number
        """
        return self.inorder.pop(0)

    def hasNext(self):
        """
        @return whether we have a next smallest number
        """
        if len(self.inorder)>=1:
            return True
        return False
