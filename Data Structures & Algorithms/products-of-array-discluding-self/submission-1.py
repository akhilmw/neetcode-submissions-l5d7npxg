class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        prod1, prod2 = 1 , 1
        
        for i in range(n):
            result[i] *= prod1
            prod1 *= nums[i]

        for i in range(n-1, -1, -1):
            result[i] *= prod2
            prod2 *= nums[i]
        

        return result



        





        