class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []

        def dfs(open, close, curr):
            nonlocal ans
            if close > open:
                return 

            if open == close == n:
                s = "".join(curr)
                ans.append(s)
                return
            if open < n:
                curr.append("(")
                dfs(open + 1, close, curr)
                curr.pop()
            if close < n:
                curr.append(")")
                dfs(open, close + 1, curr)
                curr.pop()
        
        dfs(1, 0, ["("])

        return ans
