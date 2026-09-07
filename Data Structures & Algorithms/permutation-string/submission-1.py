class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        n, m = len(s1), len(s2)
        if m < n:
            return False
        freq = Counter(s1)
        mpp = defaultdict(int)

        # fixed window
        i, j = 0, 0
        while j < n:
            mpp[s2[j]] += 1
            j += 1
    
        if mpp == freq:
            return True
        
        while j < m:

            mpp[s2[j]] += 1
            
            if j - i + 1 > n:
                mpp[s2[i]] -= 1
                if mpp[s2[i]] == 0:
                    del mpp[s2[i]]
                i += 1

            
            if mpp == freq:
                return True

            j += 1


        return False
        