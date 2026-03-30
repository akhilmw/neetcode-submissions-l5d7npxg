class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        myMap = {}
        for x in nums:
            if x in myMap:
                myMap[x] += 1
            else:
                myMap[x] = 1
        
        while k > 0:
            max_key = max(myMap, key=myMap.get)
            ans.append(max_key)
            del myMap[max_key]
            k -= 1
        

        return ans





#   1 - 1
#   2 - 2
#   3 - 3
#
#
#
#
#
#


        