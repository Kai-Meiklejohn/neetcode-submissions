class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        res = 0

        def backtrack(i, cur):
            if i == len(nums):
                if cur == target:
                    nonlocal res
                    res += 1
                return

            backtrack(i + 1, cur + nums[i])
            backtrack(i + 1, cur - nums[i])

        backtrack(0, 0)
        return res

        