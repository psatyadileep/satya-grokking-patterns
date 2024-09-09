"""
LC125: Valid Palindrome

https://leetcode.com/problems/valid-palindrome/

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.


Assumptoms:
-> Can the input be empty : yes

BrainStorm:
1. Apporach 1
    . remove all the alphanumerics
    . Using Two arrays
    . Use  1 st array from left to right
    . Use secodn array from right to left
    . Check if both arrays are same

    Timme Complexity  = o(n) + o (n)
    Space COmplexity = o(n)

2. Approach 2 : Two Pointers : Optimal
    .remove all the alphanumeric ccharacters
    . Using left and right Pointers
    . Check if both the left and right pointers are same
    . Move the pointers accoirdingly
    . If Not return False Else True

"""


class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = ''.join(ch for ch in s if ch.isalnum()).lower()

        L = 0
        R = len(s) - 1

        while L <= R:
            if s[L] == s[R]:
                L += 1
                R -= 1

            else:
                return False

        return True


