"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
Given a string s, find the length of the longest
substring
 without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Explore:
1. can the array be emtpy -> yes
2. is the array sorted no


brain STorm :
1. Brute Force : using Two loops

2. using two Pointers and slidig widsdow
have two pointer L 0=0
have the Second inter in loop starting from 0





"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0

        for L in range(len(s)):

            unique_elements = set()

            for R in range(L, len(s)):

                if s[R] in unique_elements:
                    break

                max_length = max(max_length, R-L+1)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0

        L = 0
        unique_set = set()
        for R, val  in enumerate(s):

            while val in unique_set:
                unique_set.remove(s[L])

            unique_set.add(val)
            max_length = max(max_length, R-L+1)

        return max_length


