class Solution {
public:
    int maxProfit(vector<int>& prices) {
      int maxProfit = 0, minStockPrice = 1e9;
      for (int i = 0; i < prices.size(); ++i) {
          maxProfit = max(maxProfit, prices[i] - minStockPrice);
          minStockPrice = min(prices[i], minStockPrice);
      }
      return maxProfit; 
    }
};
