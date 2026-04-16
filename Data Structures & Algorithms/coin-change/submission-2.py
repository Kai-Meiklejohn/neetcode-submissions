class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}

        def dfs(cur):
            if cur < 0:
                return float('inf')
            if cur == 0:
                return 0
            if cur in memo:
                return memo[cur]

            res = float('inf')
            for coin in coins:
                res = min(res, 1 + dfs(cur - coin))
            
            memo[cur] = res
            return res

        res = dfs(amount)
        return res if res != float('inf') else -1