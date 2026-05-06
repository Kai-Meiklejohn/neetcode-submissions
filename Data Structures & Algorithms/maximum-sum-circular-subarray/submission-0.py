class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        total_sum = sum(nums)

        current_max = nums[0]
        best = nums[0]

        current_min = nums[0]
        worst = nums[0]

        for i in range(1, len(nums)):

            current_max = max(nums[i], current_max + nums[i])
            best = max(best, current_max)

            current_min = min(nums[i], current_min + nums[i])
            worst = min(worst, current_min)

        if best < 0:
            return best

        return max(best, total_sum - worst)