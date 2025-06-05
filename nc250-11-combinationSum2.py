class Solution:
    def combinationSum2(self, candidates):
        res = []
        candidates.sort()
        def dfs(i,curr,total):
            if total == target: # if the total is equal to target, then append the subset
                res.append(curr.copy())
                return
            
            if total > target or i == len(candidates): # if the total greater than target
                return

            curr.append(candidates[i])
            dfs(i+1,curr,total + candidates[i]) # include the duplicate element and keep adding it
            curr.pop()

            while i+1<len(candidates) and candidates[i]==candidates[i+1]: # ignore all the duplicates since you already covered it in the last dfs
                i+=1

            dfs(i+1,curr,total) # Add the other elements
        
        dfs(0,[],0)
        return res
