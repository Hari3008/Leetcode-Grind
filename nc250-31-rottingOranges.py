
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh = 0
        time = 0
        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh+=1
                elif grid[i][j] == 2:
                    q.append((i,j))
        
        directions= [[1,0],[0,1],[-1,0],[0,-1]]
        while fresh>0 and q:
            length = len(q)
            for i in range(length):
                row, col = q.popleft()
                for dr,dc in directions:
                    nx,ny = row+dr,col+dc
                    if (nx in range(len(grid)) and ny in range(len(grid[0])) and grid[nx][ny] == 1):
                        fresh-=1
                        q.append((nx,ny))
                        grid[nx][ny] = 2
            time+=1
        
        return time if fresh==0 else -1
