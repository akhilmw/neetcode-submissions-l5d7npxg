class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charArr = [0] * 26
        l, r, n, = 0, 0, len(s)
        max_ans = 0

        while r < n:
            charArr[ord(s[r]) - ord('A')] += 1
            while (r -l + 1) - max(charArr) > k:
                charArr[ord(s[l]) - ord('A')] -= 1
                l += 1
            
            max_ans = max(max_ans, (r - l + 1))
            r += 1
        

        return max_ans
        
        
        