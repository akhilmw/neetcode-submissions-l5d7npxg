class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        def solve(idx, curr):
            nonlocal ans
            if idx == n:
                ans.append(curr.copy())
                return

            curr.append(nums[idx])
            solve(idx + 1, curr)
            curr.pop()
            solve(idx + 1, curr)


        solve(0, [])
        
        return ans