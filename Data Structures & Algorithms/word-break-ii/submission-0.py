class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        wordDict = set(wordDict)
        ans = []

        def solve(idx, curr):
            if idx == n:
                ans.append(" ".join(curr))
                return

            for j in range(idx, n):
                word = s[idx:j + 1]
                if word in wordDict:
                    curr.append(word)
                    solve(j + 1, curr)
                    curr.pop()


        solve(0, [])
        return ans
