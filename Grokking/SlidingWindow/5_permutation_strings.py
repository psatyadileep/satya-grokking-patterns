"""
567. Permutation in String
https://leetcode.com/problems/permutation-in-string/description/
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if not s1 or not s2:
            return True

        lookup = {}
        for ch in s1:
            lookup[ch] = lookup.get(ch, 0) + 1

        substring_map = {}
        L = 0
        for R in range(len(s2)):
            character = s2[R]

            substring_map[character] = substring_map.get(character, 0) + 1

            if R - L + 1 > len(s1):
                substring_map[s2[L]] -= 1
                if substring_map[s2[L]] == 0:
                    del substring_map[s2[L]]

                L += 1

            if substring_map == lookup:
                return True

        return False
