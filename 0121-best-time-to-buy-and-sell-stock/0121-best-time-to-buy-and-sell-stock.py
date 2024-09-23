class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        b = prices[0]
        if len(prices) >= 2:
            for i in range(len(prices)):
                maxp = max(maxp, prices[i] - b)
                b = min(b, prices[i])
        return maxp
        