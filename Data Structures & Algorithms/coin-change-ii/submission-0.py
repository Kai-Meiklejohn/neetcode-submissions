class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        memo = {}

        def combination(i, total):
            if total == amount:
                return 1
            if total > amount:
                return 0
            if (i, total) in memo:
                return memo[(i, total)]

            ways = 0
            for j in range(i, len(coins)):
                ways += combination(j, total + coins[j])

            memo[(i, total)] = ways
            return ways

        return combination(0, 0)