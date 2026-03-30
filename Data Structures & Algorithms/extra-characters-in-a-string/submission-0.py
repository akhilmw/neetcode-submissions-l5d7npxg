class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        wordDict = set(dictionary)
        dp = [-1] * n

        def dfs(idx):

            if idx >= n:
                return 0

            if dp[idx] != -1:
                return dp[idx]

            extras = float('inf')
            for j in range(idx, n):
                word = s[idx:j + 1]
                if word in wordDict:
                    extras = min(dfs(j + 1), extras)
                else:
                    extras = min(len(word) + dfs(j + 1) , extras)

            dp[idx] =  extras
            return dp[idx]

        return dfs(0)