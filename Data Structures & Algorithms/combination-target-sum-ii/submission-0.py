class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []

        def dfs(idx, curr, target):
            nonlocal ans
            if target == 0:
                ans.append(curr.copy())
                return    

            if idx == n:
                return

            if target >= nums[idx]:
                curr.append(nums[idx])
                dfs(idx + 1, curr, target - nums[idx])
                curr.pop()
            
            while idx < n - 1 and nums[idx] == nums[idx + 1]:
                idx += 1
            dfs(idx + 1, curr, target)

        dfs(0, [], target)
        return ans