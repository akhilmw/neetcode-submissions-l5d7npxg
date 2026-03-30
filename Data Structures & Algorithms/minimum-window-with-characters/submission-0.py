class Solution:
    def isSubset(self, map1, map2):
        for key, value in map1.items():
            if key not in map2 or map2[key] < value:
                return False
        
        return True
    def minWindow(self, s: str, t: str) -> str:
        map1, map2 = {}, {}
        l, r = 0, 0
        n, m = len(s), len(t)
        ans, min_length = "", float("inf")

        for i in range(m):
            map1[t[i]] = map1.get(t[i], 0) + 1
        
        while r < n:
            key = s[r]
            map2[s[r]] = map2.get(s[r], 0) + 1

            while self.isSubset(map1, map2):
                dummy = s[l:r+1]
                if len(dummy) < min_length:
                    ans = dummy
                    min_length = len(ans)
                map2[s[l]] -= 1
                if map2[s[l]] == 0:
                    del map2[s[l]]
                l += 1
            
            r += 1

        return ans

        