class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        memo = {}
        n = len(prices)

        def dp(i, buying: bool):
            if i >= n:
                return 0
                
            if (i, buying) in memo:
                return memo[(i, buying)]

            if buying is True:
                memo[(i, buying)] = max(
                    dp(i + 1, False) - prices[i], # buy
                    dp(i + 1, buying) # skip
                )
            else:
                memo[(i, buying)] = max(
                    dp(i + 2, True) + prices[i], # sell
                    dp(i + 1, buying) # hold
                )

            return memo[(i, buying)]

        return dp(0, True)
        