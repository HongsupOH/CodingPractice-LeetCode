class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        """
        North:0, East:1, South:2, West:3
        Move[North] = [1,0], Move[East] = [0,1], Move[South] = [0,-1], Move[West] = [-1,0]
        """
        instructions *= 4
        pos = [0,0]
        d = 0
        dy = [1,0,-1,0]
        dx = [0,1,0,-1]
        for i in range(len(instructions)):
            if instructions[i]=='G':
                pos[0]+=dy[d]
                pos[1]+=dx[d]
            elif instructions[i]=='L':
                d = self.left(d)
            elif instructions[i]=='R':
                d = self.right(d)
        return pos == [0,0]
    
    def left(self,d):
        if d==0:
            return 3
        else:
            return d-1
    
    def right(self,d):
        if d==3:
            return 0
        else:
            return d+1
        
