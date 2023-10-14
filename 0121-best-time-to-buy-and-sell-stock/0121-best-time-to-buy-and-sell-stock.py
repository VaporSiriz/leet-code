class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, max_price, profit = prices[0], prices[0], 0
        length = len(prices)
        for i in range(1, length):
            if min_price > prices[i]:
                min_price = prices[i]
                max_price = prices[i]
            max_price = prices[i] if max_price < prices[i] else max_price
            profit = max_price-min_price if max_price-min_price > profit else profit
        return profit