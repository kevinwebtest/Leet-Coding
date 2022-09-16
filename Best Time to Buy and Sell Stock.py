class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice, maxProfit = inf, 0
        for i in range(len(prices)-1):
            if prices[i] < minPrice:
                minPrice = prices[i]
            if prices[i+1]-minPrice > maxProfit:
                maxProfit = prices[i+1]-minPrice
        return maxProfit
      
# Fastest Solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice, maxProfit = inf, 0
        for price in prices:
            if price < minPrice:
                minPrice = price
            elif price-minPrice > maxProfit:
                maxProfit = price-minPrice
        return maxProfit
