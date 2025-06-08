class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit = set() # keep track of the visited cells

        def dfs(i,j):
            # Check if the cell is in bound and within the island -> Base case
            if i>=len(grid) or j>=len(grid[0]) or i<0 or j<0 or grid[i][j]==0:
                return 1
            # Check if the cell is already visited
            if (i,j) in visit:
                return 0
            
            visit.add((i,j))
            # Explore all directions
            perimeter = dfs(i+1,j)
            perimeter += dfs(i,j+1)
            perimeter += dfs(i,j-1)
            perimeter += dfs(i-1,j)
            
            return perimeter
        
        # first find the first evidence of land so that we can spot our island
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return dfs(i,j)


