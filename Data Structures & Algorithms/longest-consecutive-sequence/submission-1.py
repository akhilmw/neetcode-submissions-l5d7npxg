class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_result = 0
        my_set = set(nums)

        for i in range(len(nums)):
            curr_max = 1
            x = nums[i] - 1
            while x in my_set:
                curr_max += 1
                x -= 1
            max_result = max(max_result, curr_max)



        return max_result
            



        
# [2, 20, 4, 10, 3, 5]

# curr = 1
# max = 1


# [2,20,4,10,3,4,5]