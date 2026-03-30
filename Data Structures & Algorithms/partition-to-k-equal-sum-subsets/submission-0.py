class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        used = [False] * n
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k

        def solve(idx, k, currSum):
            if k == 0:
                return True
            
            if currSum == target:
                return solve(0, k - 1, 0)
            
            for j in range(idx, n):
                if used[j] or currSum + nums[j] > target:
                    continue

                used[j] = True
                if solve(j + 1, k, currSum + nums[j]):
                    return True

                used[j] = False

            return False

        return solve(0, k, 0)


