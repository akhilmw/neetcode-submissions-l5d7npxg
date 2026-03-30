class Solution:
    def trap(self, height: List[int]) -> int:
        left, right, n = [height[0]], [height[-1]], len(height)
        maxLeft, maxRight = left[0], right[0]
        total = 0

        for i in range(1, n):
            maxLeft = max(maxLeft, height[i])
            left.append(maxLeft)

        for i in range(n-2, -1, -1):
            maxRight = max(maxRight, height[i])
            right.append(maxRight)
        
        for i in range(n):
            total += min(left[i], right[n - i - 1]) - height[i]

    
        return total



