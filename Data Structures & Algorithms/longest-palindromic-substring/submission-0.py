class Solution:
    def longestPalindrome(self, s: str) -> str:

        longest_current_substring = ""
        longest_current_substring_length = 0

        def search_substring(sub_string, memo):
            nonlocal longest_current_substring
            nonlocal longest_current_substring_length

            if sub_string in memo:
                return memo[sub_string]

            if len(sub_string) == 0:
                return False

            if self.is_substring(sub_string):
                if len(sub_string) > longest_current_substring_length:
                    longest_current_substring_length = len(sub_string)
                    longest_current_substring = sub_string
                memo[sub_string] = True
                return True

            left = search_substring(sub_string[1:], memo)
            right = search_substring(sub_string[:-1], memo)

            memo[sub_string] = left or right
            return memo[sub_string]

        search_substring(s, {})

        return longest_current_substring

    def is_substring(self, sub_string):
        l, r = 0, len(sub_string) - 1

        while l < r:
            if sub_string[l] == sub_string[r]:
                l += 1
                r -= 1
            else:
                return False

        return True

        