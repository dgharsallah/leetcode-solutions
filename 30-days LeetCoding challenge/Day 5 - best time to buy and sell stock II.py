class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(len(prices)):
            if i > 0 and prices[i] - prices[i - 1] > 0:
                maxProfit += prices[i] - prices[i - 1]
        return maxProfit
