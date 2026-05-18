# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        upper = n
        lower = 1

        while upper >= 1 and lower <= n:
            cur_guess = (upper + lower) // 2

            result = guess(cur_guess)

            if result == 0:
                return cur_guess
            elif result == -1:
                upper = cur_guess - 1
            elif result == 1:
                lower = cur_guess + 1
        
        