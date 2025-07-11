class Solution:
    def numSquares(self, n: int) -> int:
        # Bottom up approach
        dp = [n] * (n+1)
        dp[0] = 0

        # Similar to combination sum 4
        # Its a similar pattern
        for target in range(1, n + 1):
            for s in range(1, target + 1):
                square = s * s
                if target - square < 0:
                    break
                dp[target] = min(dp[target], 1 + dp[target - square])
        
        return dp[target]
