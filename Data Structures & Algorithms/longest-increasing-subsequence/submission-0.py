class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]

            ans = 1
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    ans = max(ans, 1 + dfs(j))

            memo[i] = ans
            return ans

        return max(dfs(i) for i in range(n)) if nums else 0