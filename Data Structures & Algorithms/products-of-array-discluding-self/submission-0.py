class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr1, arr2, result = [], [], []
        prod1, prod2 = 1 , 1
        
        for i in range(n):
            arr1.append(prod1)
            prod1 *= nums[i]

        for i in range(n-1, -1, -1):
            arr2.append(prod2)
            prod2 *= nums[i]
        
        for i in range(n):
            result.append(arr1[i] * arr2[n-i-1])
        

        return result



        





        