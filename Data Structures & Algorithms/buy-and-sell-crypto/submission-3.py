class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = prices[0]
        maxr = 0
        daytobuy = 0
        daytosell = 0
        buyday = 0

        for i in range(len(prices)):
            profit = prices[i] - minp
            if profit > maxr:
                daytosell = i
                daytobuy = buyday
                maxr = profit
            if prices[i] < minp:
                minp = prices[i]
                buyday = i
        return maxr
        