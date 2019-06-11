class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        gas = [1,2,3,4,5]
        cost = [3,4,5,1,2]
        ans = 3 (index number)
        """
        #Make one array
        remain = []
        for i in range(len(gas)):
            remain.append(gas[i]-cost[i])
        #if sum of remain array is less than 0, then it is always false result
        if sum(remain)<0:
            return -1
        #DFS Solution
        stack = [([0],remain[0])]
        while stack:
            path,Gas = stack.pop()
            y = path[-1]
            if path[0]==path[-1] and len(path)>1 and Gas>=0:
                return path[-1]
            elif Gas<0:
                if y==len(cost)-1:
                    y2 = 0
                else:
                    y2 = y+1
                newPath = [y2]
                newGas = remain[y2]
                stack.append((newPath,newGas))
            else:
                if y==len(cost)-1:
                    y2 = 0
                else:
                    y2 = y+1
                newPath = path + [y2]
                newGas = Gas + remain[y2]
                stack.append((newPath,newGas))
        return -1
