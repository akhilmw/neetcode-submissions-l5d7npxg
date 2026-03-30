class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        n = len(nums)
        myMap = {}
        for x in nums:
            if x in myMap:
                myMap[x] += 1
            else:
                myMap[x] = 1


        bucket = [[] for _ in range(n)]
        for key, value in myMap.items():
            bucket[value-1].append(key)
        
        for i in range(n-1, -1, -1):
            if len(ans) == k:
                break
            if len(bucket[i]):
                ans += bucket[i]
        

        return ans
        



        


