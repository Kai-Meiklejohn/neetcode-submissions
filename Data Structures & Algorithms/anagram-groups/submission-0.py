class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = []
        anagrams = {} # { act : [act, cat], stop : ["stop", "pots", "tops"]}

        for string in strs:
            sorted_string = "".join(sorted(string))

            if sorted_string in anagrams:
                anagrams[sorted_string].append(string)
            else:
                anagrams[sorted_string] = [string]

        for anagram in anagrams.values():
            res.append(anagram)

        return res
        