class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
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
                dfs(idx, curr, target - nums[idx])
                curr.pop()
            dfs(idx + 1, curr, target)

        dfs(0, [], target)
        return ans
    