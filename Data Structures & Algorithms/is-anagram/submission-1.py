class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        n, m = len(s), len(t)

        if n != m :
            return False
        
        myMap = {}
        for i in range(n):
            key = s[i]
            # if key in myMap:
            #     myMap[key] += 1
            # else:
            #     myMap[key] = 1
            myMap[key] = myMap.get(key, 0) + 1
        
        for i in range(m):
            key = t[i]
            if key not in myMap:
                return False
            else:
                myMap[key] -= 1
                if myMap[key] < 0:
                    return False

        return True







        

        