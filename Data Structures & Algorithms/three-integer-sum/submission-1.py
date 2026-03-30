class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate elements for the first element of the triplet
            x, y = i + 1, n - 1
            while x < y:
                sum = nums[i] + nums[x] + nums[y]
                if sum > 0:
                    y -= 1
                elif sum < 0:
                    x += 1
                else:
                    ans.append([nums[i], nums[x], nums[y]])
                    x += 1
                    y -= 1
                    # Skip duplicate elements for the second and third elements of the triplet
                    while x < y and nums[x] == nums[x - 1]:
                        x += 1
                    while x < y and nums[y] == nums[y + 1]:
                        y -= 1

        return ans
        