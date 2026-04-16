class Solution:
    def isHappy(self, n: int) -> bool:

        numbers = [int(digit) for digit in str(n)]
        visited = set()

        while True:
            answer = 0
            for i in range(len(numbers)):
                answer += numbers[i] ** 2
            
            if answer == 1:
                return True

            if answer in visited:
                return False
            visited.add(answer)

            numbers = [int(digit) for digit in str(answer)]
