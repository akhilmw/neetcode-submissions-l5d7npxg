class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        def dfs(idx, curr):
            nonlocal ans
            if idx == n:
                ans.append(curr.copy())
                return
            
            curr.append(nums[idx])
            dfs(idx + 1, curr)
            curr.pop()
            while idx < n - 1 and nums[idx] == nums[idx + 1]:
                idx += 1
            dfs(idx + 1, curr)

        dfs(0, [])

        return ans
