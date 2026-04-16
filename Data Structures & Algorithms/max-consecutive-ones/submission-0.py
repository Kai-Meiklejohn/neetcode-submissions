class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        res = 0
        i = 0

        while i < len(nums):
            counter = 0
            while i < len(nums) and nums[i] == 1:
                counter += 1
                i += 1
            else:
                i += 1
            res = max(res, counter)

        return res