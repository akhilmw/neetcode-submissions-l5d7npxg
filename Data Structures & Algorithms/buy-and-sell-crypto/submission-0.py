class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev_min, max_profit = float("inf"), 0
        for x in prices:
            prev_min = min(prev_min, x)
            max_profit = max(max_profit, x - prev_min)
        

        return max_profit

        