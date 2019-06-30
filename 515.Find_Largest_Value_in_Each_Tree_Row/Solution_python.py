from collections import defaultdict

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        info = defaultdict(list)
        queue = [(0,root)]
        while queue:
            lev,node = queue.pop(0)
            if node:
                info[lev].append(node.val)
                queue.append((lev+1,node.left))
                queue.append((lev+1,node.right))
        res = []
        for lev in info:
            res.append(max(info[lev]))
        return res
