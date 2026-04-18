class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []

        def backtrack(i, subset):
            if i == len(nums):
                result.append(subset.copy())
                return

            subset.append(nums[i])         # include
            backtrack(i + 1, subset)
            subset.pop()

            backtrack(i + 1, subset)       # exclude

        backtrack(0, [])
        return result
        