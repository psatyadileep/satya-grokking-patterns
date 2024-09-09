class Solution:
    def maxProfit(self, prices) -> int:

        L = 0
        max_profit = float("-inf")
        for R in range(len(prices)):

            if prices[R]<prices[L]:
                L = R

            else:
                max_profit = max(max_profit, prices[R]- prices[L])

        return max_profit





