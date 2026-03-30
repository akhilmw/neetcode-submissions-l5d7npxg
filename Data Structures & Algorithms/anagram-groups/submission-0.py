class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        n = len(strs)
        ans = []
        myMap = {}

        for i in range(n):
            charArr = [0] * 26
            for j in range(len(strs[i])):
                charArr[ord(strs[i][j]) - ord('a')] += 1
            myMap[tuple(charArr)] = myMap.get(tuple(charArr), [])
            myMap[tuple(charArr)].append(strs[i])
        
        for key in myMap:
            ans.append(myMap[key])
        
        return ans
        



            



#   a1c1t1 - [0, 3]
#   p1o1t1s1 - [1, 2, 4]
#   h1a1t1 - [5]
#
#
#
#
#
#
#
#
#

        








        