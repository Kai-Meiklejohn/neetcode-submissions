class Solution:
    def maxScore(self, s: str) -> int:

        res = 0
        length = len(s)

        for i in range(1, length):
            tmp = 0
            left = s[:i]
            right = s[i:]
            tmp += left.count('0')
            tmp += right.count('1')
            res = max(tmp, res)

        return res


        