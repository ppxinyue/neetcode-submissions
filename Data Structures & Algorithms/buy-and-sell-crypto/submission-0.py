class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        for i, p1 in enumerate(prices):
            for j, p2 in enumerate(prices):
                if j<= i:
                    continue
                r = p2 - p1
                res = max(r, res)
        return res  