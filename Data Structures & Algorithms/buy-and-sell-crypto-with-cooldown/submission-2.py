class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        memo = {}
        
        def profit_calc(buying, i):
            if i >= len(prices):
                return 0

            if (buying, i) in memo:
                return memo[(buying, i)]

            if buying is True:
                memo[(buying, i)] = max(
                    profit_calc(False, i+1) - prices[i], # Buying
                    profit_calc(True, i+1) # Skipping
                )
            else:
                memo[(buying, i)] = max(
                    profit_calc(True, i+2) + prices[i], # Selling
                    profit_calc(False, i+1) # Holding
                )

            return memo[(buying, i)]

        return profit_calc(True, 0)