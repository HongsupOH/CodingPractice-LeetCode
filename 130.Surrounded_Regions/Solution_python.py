class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        if board:
            m = len(board)
            n = len(board[0])
            queue = []
            for i in range(m):
                for j in range(n):
                    if (i==0 or i==m-1 or j==0 or j==n-1) and board[i][j]=='O':
                        queue.append((i,j))
            while queue:
                node = queue.pop(0)
                y,x = node
                for y2,x2 in (y+1,x),(y-1,x),(y,x+1),(y,x-1):
                    if 0<=y2<m and 0<=x2<n and board[y2][x2]=='O':
                        queue.append((y2,x2))
                board[y][x]='Alive'
        
            for i in range(m):
                for j in range(n):
                    if board[i][j]=='O':
                        board[i][j]='X'
                    if board[i][j]=='Alive':
                        board[i][j]='O'
