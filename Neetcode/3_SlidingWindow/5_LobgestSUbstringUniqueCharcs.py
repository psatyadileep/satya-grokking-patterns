"""
LC3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Explore:
-> can the array be empty : yes


Brainstorm:
1. Using two Loops O(n)^2
2. Using two pointers


"abcabcbb"
Approacj:
1.Hava two pointe L , R
2. have hash set
3. Iterate through the array and elements of R as you move.
4. if at any point the set contains duplicate , pop left until set doesn conatin anymore duplicates
5. Keep updateing the max length and return it

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        max_length = 0
        lookup = set()
        for R in range(len(s)):

            while s[R] in lookup:
                lookup.remove(s[L])
                L += 1


            lookup.add(s[R])
            max_length = max(max_length, R - L + 1)
        return max_length