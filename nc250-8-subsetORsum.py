class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        # Bit Manipulation - HARD logic
        # basically when you XOR subsets you always have to take the half of the OR result
        res = 0
        for num in nums:
            res = res | num
        
        return res << (len(nums)-1) # Basically multiplying with half of the number of subsets

        # DFS or Recursive approach
        # def ædfs(i,total):
            
        #     if i == len(nums):
        #         return total
            
        #     return dfs(i+1,total ^ nums[i]) + dfs(i+1,total) # Basically include nums[i] and not nums[i]
        # return dfs(0,0)
