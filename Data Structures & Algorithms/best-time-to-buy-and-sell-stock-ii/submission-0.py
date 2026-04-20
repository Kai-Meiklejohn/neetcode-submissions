class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        res = 0
        left = 0
        right = 1

        while right < len(prices):
            if prices[left] < prices[right]:
                res += prices[right] - prices[left]
            left += 1
            right += 1

        return res
        