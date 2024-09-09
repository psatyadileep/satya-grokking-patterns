"""
https://leetcode.com/problems/reverse-vowels-of-a-string/

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.



Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
"""

class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = set("aeiouAEIOU")

        if not s:
            return ""
        s = list(s)

        L = 0
        R = len(s) - 1
        while L < R:

            while L < R and s[L] not in vowels:
                L += 1

            while L < R and s[R] not in vowels:
                R -= 1

            s[L], s[R] = s[R], s[L]
            L += 1
            R -= 1

        return ''.join(s)
