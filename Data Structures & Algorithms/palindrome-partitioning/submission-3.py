class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        def isPalindrome(i, j):
            
            if i >= j:
                return True

            if dp[i][j] != -1:
                return dp[i][j]

            if s[i] == s[j]:
                if isPalindrome(i + 1, j - 1):
                    dp[i][j] =  True
                else:
                    dp[i][j] =  False
            else:
                dp[i][j] =  False
            return dp[i][j]

        ans = []

        def dfs(idx, curr):
            nonlocal ans

            if idx == n:
                ans.append(curr.copy())
                return

            for j in range(idx, n):
                if isPalindrome(idx, j):
                    curr.append(s[idx:j + 1])
                    dfs(j + 1, curr)
                    curr.pop()

        dfs(0, [])
        return ans