class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) <= 1: # obvious exception
            return 0


        min_price = prices[0]
        max_price = 0

        for price in prices[1:]: # find the profit by finding the max and min of the list(sequentally)
            max_price = max(max_price, price - min_price)
            min_price = min(min_price, price)

        return max_price
