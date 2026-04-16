class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram_s = defaultdict(int) # char to count
        anagram_t = defaultdict(int) # char to count


        for char_s in s:
            anagram_s[char_s] += 1

        for char_t in t:
            anagram_t[char_t] += 1

        if anagram_s == anagram_t:
            return True
        return False



        