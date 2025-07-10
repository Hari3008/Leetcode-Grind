class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Bottom up approach
        # Basically we need to check if each word in the word Dict is part of the string
        # Setting the last index of the memoization table true is crucial since we are able to use it later when we solve the same sub problem.
        dp = [False] * (len(s)+1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if i + len(word) <= len(s) and s[i:i+len(word)] == word:
                    dp[i] = dp[i + len(word)]
                if dp[i]:
                    break

        return dp[0]


        # Top Down Approach

        dp = {len(s): True}

        def dfs(i):
            if i in dp:
                return dp[i]
            for word in wordDict:
                if i + len(word) <= len(s) and s[i:i+len(word)] == word:
                    if dfs(i+len(word)):
                        dp[i] = True
                        return True
            dp[i] = False
            return False

        
        dfs(0)
