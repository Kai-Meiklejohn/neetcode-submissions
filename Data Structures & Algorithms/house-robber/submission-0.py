class Solution:
    def rob(self, nums: List[int]) -> int:

        length = len(nums)

        def dp(i, dmap={}):
            if i in dmap:
                return dmap[i]
            if i >= length:
                return 0

            dmap[i] = max(nums[i] + dp(i + 2, dmap), dp(i + 1, dmap))
            return dmap[i]

        return max(dp(0), dp(1))

        
        