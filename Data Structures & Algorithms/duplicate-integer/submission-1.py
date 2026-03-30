class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myMap = set()
        for i in range(len(nums)):
            if nums[i] in myMap:
                return True
            else:
                myMap.add(nums[i])


        return False
        



         