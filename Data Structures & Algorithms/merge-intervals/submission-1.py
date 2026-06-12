class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()

        merged = []

        for interval in intervals:
            if not merged:
                merged.append([interval[0], interval[1]])
            else:
                if merged[-1][1] >= interval[0]:
                    merged[-1][1] = max(interval[1], merged[-1][1])
                else:
                    merged.append([interval[0], interval[1]])

        return merged