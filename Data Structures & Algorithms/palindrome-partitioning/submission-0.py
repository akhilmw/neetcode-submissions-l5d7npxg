class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        def isPalindrome(i, j):
            
            while i < j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    return False

            return True

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