"""
https://leetcode.com/problems/reverse-string/
344. Reverse String
"""


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # # if not s:
        # #     return []

        # return s[::-1]

        L = 0
        R = len(s) - 1

        while L <= R:
            s[L], s[R] = s[R], s[L]
            L += 1
            R -= 1

        return s
