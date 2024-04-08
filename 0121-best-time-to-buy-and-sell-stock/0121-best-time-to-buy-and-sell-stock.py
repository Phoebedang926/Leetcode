class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        max_profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                max_profit =  max(max_profit, prices[r] - prices[l])
            else:
                l=r
            r += 1 
        return max_profit




#         max_profit = 0
#         min_price = prices[0]

#         for price in prices:
#             min_price = min (price, min_price)
#             max_profit = max(max_profit, price - min_price)

#         return max_profit 

        