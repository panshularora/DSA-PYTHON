class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        #sell = prices[0]
        maxprofit = 0
        for index, x in enumerate(prices):
            buy = min(buy, x)
            profit = x - buy
            maxprofit = max(maxprofit, profit)
        return maxprofit