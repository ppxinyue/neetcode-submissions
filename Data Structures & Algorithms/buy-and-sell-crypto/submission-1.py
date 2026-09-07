class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = prices[0]
        maxr = 0

        for i in range(len(prices)):
            maxr = max(maxr, prices[i] - minp)
            minp = min(minp, prices[i])
        return maxr
        