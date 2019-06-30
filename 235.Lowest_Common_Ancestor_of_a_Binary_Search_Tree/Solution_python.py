class Solution:
    
    def lowestCommonAncestor(self, root, p, q):
        path1 = self.path(root,p)
        path2 = self.path(root,q)
        anc = None
        count = 0
        while count<len(path1) and count<len(path2):
            if path1[count]==path2[count]:
                anc = path1[count]
            count+=1
        return anc
    
    def path(self,root,dst):
        stack = [[root]]
        while stack:
            path = stack.pop()
            node = path[-1]
            if node == dst:
                return path
            else:
                if node.left:
                    stack.append(path+[node.left])
                if node.right:
                    stack.append(path+[node.right])
        
