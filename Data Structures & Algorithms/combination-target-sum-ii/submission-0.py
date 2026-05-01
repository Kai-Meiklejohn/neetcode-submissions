class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        candidates.sort()

        def backtrack(start, path, total):
            if total == target:
                result.append(path.copy())
                return

            if total > target:
                return

            for i in range(start, len(candidates)):
                # skip duplicates at the same tree level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                path.append(candidates[i])

                # i + 1 because each number can only be used once
                backtrack(i + 1, path, total + candidates[i])

                path.pop()

        backtrack(0, [], 0)
        return result


        