class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        myMap = {}

        for i in range(len(nums)):
            key = target - nums[i]
            if key in myMap:
                return [myMap[key], i]
            else:
                myMap[nums[i]] = i
        
        