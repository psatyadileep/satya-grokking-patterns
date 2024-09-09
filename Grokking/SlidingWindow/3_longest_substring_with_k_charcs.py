"""
Given a string, find the length of the longest substring in it with no more than K distinct characters.

You can assume that K is less than or equal to the length of the given string.

Example 1:

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".
Example 2:

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".


Assumptions

-> if not str or len(str)<=k return -1

Aprroach 1:
                araaci k = 2

Two pointer
                    set = a  , max_len = 2      max_len = 3    max_len = 4
 a r a a c i         a r a a c i                a r a a c i    a r a a c i
 l                   l R                        l   r          l     r
 R

-
>
"""


class Solution:
    def findLength(self, str1, k):
        if k <= 0:
            return 0

        max_length = 0
        left = 0
        char_count = {}  # Use a dictionary to keep track of character counts

        for right in range(len(str1)):
            char = str1[right]

            # Update the character count
            char_count[char] = char_count.get(char, 0) + 1

            while len(char_count) > k:
                left_char = str1[left]
                char_count[left_char] -= 1
                if char_count[left_char] == 0:
                    del char_count[left_char]
                left += 1


        return max_length
