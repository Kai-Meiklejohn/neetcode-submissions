class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def dp(i, arr, memo):
            if i >= len(arr):
                return 0
            if i in memo:
                return memo[i]

            memo[i] = max(arr[i] + dp(i+2, arr, memo), dp(i+1, arr, memo))
            return memo[i]

        nums1 = nums[:-1]
        nums2 = nums[1:]

        return max(dp(0, nums1, {}), dp(0, nums2, {}))