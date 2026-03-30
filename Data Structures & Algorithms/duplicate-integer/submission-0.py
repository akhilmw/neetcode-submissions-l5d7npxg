class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myMap = {}
        for i in range(len(nums)):
            if nums[i] in myMap:
                return True
            else:
                myMap[nums[i]] = 1


        return False
        



         