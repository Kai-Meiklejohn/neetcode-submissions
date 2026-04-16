class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        arr_sum = sum(nums)
        if arr_sum % 2 != 0:
            return False

        target = arr_sum // 2
        n = len(nums)
        memo = {}

        def dfs(i, cur_sum):
            if cur_sum == target:
                return True
            if cur_sum > target or i >= n:
                return False
            if (i, cur_sum) in memo:
                return memo[(i, cur_sum)]

            take = dfs(i + 1, cur_sum + nums[i])
            skip = dfs(i + 1, cur_sum)

            memo[(i, cur_sum)] = take or skip
            return memo[(i, cur_sum)]

        return dfs(0, 0)



        