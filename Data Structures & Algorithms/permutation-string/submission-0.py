class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map1, map2 = {}, {}
        l, r = 0, 0
        n, m = len(s1), len(s2)

        for i in range(n):
            if s1[i] in map1:
                map1[s1[i]] += 1
            else:
                map1[s1[i]] = 1
        
        while r < m:
            key = s2[r]
            if key in map2:
                map2[key] += 1
            else:
                map2[key] = 1
            
            while (r - l + 1)  > n:
                map2[s2[l]] -= 1
                if map2[s2[l]] == 0:
                    del map2[s2[l]]
                l += 1
            
            if map1 == map2:
                return True
            
            r += 1

        return False

        