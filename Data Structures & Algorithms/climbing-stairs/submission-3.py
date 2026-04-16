class Solution:
    def climbStairs(self, n: int) -> int:

        def num_ways(n, dp={}):
            if n in dp:
                return dp[n]
            if n == 2:
                return 2
            if n == 1:
                return 1

            dp[n] = num_ways(n-1, dp) + num_ways(n-2, dp)
            return dp[n]

        return num_ways(n)
            

        