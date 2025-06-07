class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        #  Backtracking - Inefficient m*4^n (Depth of the tree)
        rows, cols = len(board), len(board[0])
        path = set()

        def dfs(r,c,i):
            if i == len(word):  # if you reach the end of the word, then return true
                return True

            if (r<0 or c<0 or r>=rows or c>=cols or word[i]!=board[r][c] or (r,c) in path):
                # basically check if it is in bound and if it already exists in the path
                return False
            
            path.add((r,c)) # add this element to the path
            res = (dfs(r+1,c,i+1) or dfs(r,c+1,i+1) or dfs(r-1,c,i+1) or dfs(r,c-1,i+1)) # check if there is a path
            path.remove((r,c)) # To track back to the previous step and explore other paths
            return res
        
        for r in range(rows):
            for c in range(cols):
                if (dfs(r,c,0)):
                    return True
        
        return False
