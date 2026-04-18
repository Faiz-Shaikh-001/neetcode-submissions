class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        min_price = float('inf')
        max_profit = 0

        i = 0
        while i < len(prices) and prices[i] < min_price:
            min_price = prices[i]
            i += 1
        
        if i == len(prices):
            return 0

        max_price = prices[i]
        for j in range(i+1, len(prices)):
            if max_price < prices[j]:
                max_price = prices[j]
            else:
                curr_max_profit = max_price - min_price
                max_profit = max_profit if max_profit > curr_max_profit else curr_max_profit
                if prices[j] < min_price:
                    min_price = prices[j]
                    max_price = prices[j]
        
        return max_profit if max_price - min_price < max_profit else max_price - min_price
