class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)

        def dp(i, memo = {}):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]

            memo[i] = cost[i] + min(dp(i + 1, memo), dp(i + 2, memo))
            return memo[i]


        return min(dp(0), dp(1))

        