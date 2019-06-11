class Solution:
    def canCross(self, stones):
        """
        solution using dfs, bfs causes time limit error
        """
        #Exceptional case
        if len(stones)+stones[len(stones)-2]<stones[len(stones)-1]:
            return False
        #Check values between 0 index and 1 index
        if stones[0]+1!=stones[1]:
            return False
        #Main Algorithm
        stack = [(1,[stones[1]])]
        while stack:
            k,path = stack.pop()
            y = path[-1]
            if y == stones[len(stones)-1]:
                return True
            dks = [-1,0,1]
            for dk in dks:
                k2 = k+dk
                if k2>0:
                    y2 = y+k2
                    if y2 in stones:
                        new_path = path + [y2]
                        stack.append((k2,new_path))
        return False
        
