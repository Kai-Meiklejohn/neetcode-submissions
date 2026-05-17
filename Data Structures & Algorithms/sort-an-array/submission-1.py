class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        heapq.heapify_max(nums)

        res = [0] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            res[i] = heapq.heappop_max(nums)

        return res
