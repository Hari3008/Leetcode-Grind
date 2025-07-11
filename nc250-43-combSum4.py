class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {0:1}

        # Bottom up approach
        # For each total check how many combinations are possible
        # store them in the cache so that we can use it for the following totals
        for total in range(1, target + 1):
            dp[total] = 0
            for num in nums:
                dp[total] += dp.get(total - num, 0)
            
        return dp[target]



        # Top Down Approach
        # We are sorting the array since we are breaking from the nums loop (when total is lesser than the num)
        nums.sort()
        dp = {0:1}

        # same kinda logic as above
        def dfs(total):
            if total in dp:
                return dp[total]
            
            res = 0
            for num in nums:
                if total < num:
                    break
                res += dfs(total - num)
            
            dp[total] = res
            return res


        return dfs(target)
