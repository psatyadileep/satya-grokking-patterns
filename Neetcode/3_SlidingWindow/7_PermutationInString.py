"""

LC567. Permutation in String
https://leetcode.com/problems/permutation-in-string/description/

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.



Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false


Explore:
-> one or both the strings maybe missing

BrainStorm:
-> using Two Loops : O(N)^2
-> using Sliding of fixed size
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        lookup_1 = {}

        lookup_2 = {}
        for ch in s1:

            if ch not in lookup_1:
                lookup_1[ch] = 1
            else:
                lookup_1[ch] += 1
        L = 0
        for R, val in enumerate(s2):

            if val not in lookup_2:
                lookup_2[val] = 1
            else:
                lookup_2[val] += 1

            if R - L + 1 > len(s1):
                lookup_2[s2[L]] -= 1

                if lookup_2[s2[L]] == 0:
                    del lookup_2[s2[L]]
                L += 1

            if lookup_1 == lookup_2:
                return True

        return False


print(Solution().checkInclusion("adc", "dcda"))
