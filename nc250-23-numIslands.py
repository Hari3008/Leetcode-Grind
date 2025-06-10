class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Check if the grid is not empty
        if not grid:
            return 0
        
        island = 0
        rows = len(grid)
        cols = len(grid[0])
        visit = set()

        def bfs(r,c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                directions = [[1,0],[0,1],[-1,0],[0,-1]]
                for r_c, c_c in directions:
                    rd = row + r_c
                    cd = col + c_c
                    if (rd in range(rows) and cd in range(cols) and grid[rd][cd]=="1" and (rd,cd) not in visit):
                        q.append((rd,cd))
                        visit.add((rd,cd))


        # Traverse through the grid to find for land so that we can traverse the entire island
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]=="1" and (r,c) not in visit:
                    bfs(r,c)
                    island+=1
        
        return island


# DFS

# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         # Check if the grid is not empty
#         if not grid:
#             return 0
        
#         island = 0
#         rows = len(grid)
#         cols = len(grid[0])
#         directions = [[1,0],[0,1],[-1,0],[0,-1]]

#         def dfs(r,c):
#             if (r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or grid[r][c]=="0"):
#                 return

#             grid[r][c] = "0"
#             for dr, dc in directions:
#                 dfs(r + dr,c + dc)


#         # Traverse through the grid to find for land so that we can traverse the entire island
#         for r in range(len(grid)):
#             for c in range(len(grid[0])):
#                 if grid[r][c]=="1":
#                     dfs(r,c)
#                     island+=1
        
#         return island
        

        
        

        
