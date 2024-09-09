"""
https://leetcode.com/problems/valid-palindrome/

ExplorE:
Can the string be empty : yes
is capital considered :  No
are space considered = No

Brain Strom :
1. Using Two Pointers O(n)
3. Using Two passes  = On(n) + O(n)

Plan:
1. initializ ledt and right pointers
2. Left to 0 and right last index
while L<r
    and the values at both the index are same
        increment left and decreent reight

    else
        return False

return True

"""


class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = [ch.lower() for ch in s if ch.isalnum()]

        L = 0
        R = len(s) - 1

        while L <= R:

            if s[L] != s[R]:
                return False

            L += 1
            R -= 1

        return True