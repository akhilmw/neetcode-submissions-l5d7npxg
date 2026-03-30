class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []

        def dfs(i):
            nonlocal ans
            if i == n:
                ans.append(nums.copy())
                return

            for j in range(i, n):
                nums[i], nums[j] = nums[j], nums[i]
                dfs(i + 1)
                nums[i], nums[j] = nums[j], nums[i]
        
        dfs(0)

        return ans
