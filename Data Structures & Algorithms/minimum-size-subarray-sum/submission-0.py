class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l, r = 0, 0
        cur = 0
        res = float('inf')

        while r < len(nums):
            cur += nums[r]

            while cur >= target:
                res = min(r - l + 1, res)
                cur -= nums[l]
                l += 1

            r += 1

        return 0 if res == float('inf') else res