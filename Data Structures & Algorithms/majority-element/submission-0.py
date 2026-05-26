class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        candidate = 0
        counter = 0

        for num in nums:
            if counter == 0:
                candidate = num

            if num == candidate:
                counter += 1
            else:
                counter -= 1

        return candidate
