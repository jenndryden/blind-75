class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        max = 0
        max_day = 0
        for price in prices:
            if price<min:
                min = price
            if price-min> max:
                max = price-min
        return max
