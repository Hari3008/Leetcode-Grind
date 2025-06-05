class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i,curr,total):
            if total == target: # when you reach the target, add the subset to the result
                res.append(curr.copy())
                return
            
            if i>=len(candidates) or total>target: # If the total is higher than target/ if index greater than len of candidates
                return
            
            curr.append(candidates[i])
            dfs(i,curr,total + candidates[i]) # Include the same element
            curr.pop() # Pop the element
            dfs(i+1,curr,total) # Include the other elements

        dfs(0,[],0)
        return res
