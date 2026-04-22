class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        n = len(nums)
        memo = defaultdict(int)
        
        def dfs(i, total_sum):
            if (i, total_sum) in memo:
                return memo[(i, total_sum)]

            if i == n:
                if total_sum == target:
                    return 1
                return 0

            memo[(i, total_sum)] += dfs(i + 1, total_sum + nums[i])
            memo[(i, total_sum)] += dfs(i + 1, total_sum - nums[i])


            return memo[(i, total_sum)]


        return dfs(0, 0)