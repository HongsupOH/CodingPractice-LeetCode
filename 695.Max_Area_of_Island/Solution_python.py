class Solution:
    def maxAreaOfIsland(self, grid: 'List[List[int]]') -> 'int':
        """
        solution using bfs
        """
        m = len(grid)
        n = len(grid[0])
        visit = set()
        best = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    count = 1
                    queue = [(i,j)]
                    visit.add((i,j))
                    while queue:
                        y,x = queue.pop(0)
                        for y2,x2 in (y-1,x),(y+1,x),(y,x-1),(y,x+1):
                            if 0<=y2<m and 0<=x2<n and grid[y2][x2]==1 and (y2,x2) not in visit:
                                queue.append((y2,x2))
                                visit.add((y2,x2))
                                count+=1
                    best = max(best,count)
        return best
