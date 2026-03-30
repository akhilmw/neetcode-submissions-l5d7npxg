class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_str = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        if digits == "":
            return []
        n = len(digits)
        ans = []

        def solve(idx, s):

            if idx == n:
                ans.append(s)
                return

            chars = num_to_str[digits[idx]]
            for j in range(len(chars)):
                s += chars[j]
                solve(idx + 1, s)
                s = s[:-1]
                

        
        solve(0, "")
        return ans
