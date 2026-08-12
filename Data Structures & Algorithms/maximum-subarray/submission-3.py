class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_total = nums[0]
        best = nums[0]

        for num in nums[1:]:
            cur_total = max(cur_total + num, num)
            best = max(best, cur_total)

        return best
        