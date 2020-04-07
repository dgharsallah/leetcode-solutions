class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(len(prices)):
            if i > 0 and prices[i] - prices[i - 1] > 0:
                maxProfit += prices[i] - prices[i - 1]
        return maxProfit
    
    # peak valley approach
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        valley = 0
        i = 0
        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            valley = prices[i]
            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i]
            maxProfit += peak - valley
        return maxProfit
