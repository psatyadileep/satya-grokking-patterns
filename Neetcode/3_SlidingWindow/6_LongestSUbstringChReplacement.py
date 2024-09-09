"""

LC424. Longest Repeating Character Replacement
https://leetcode.com/problems/longest-repeating-character-replacement/

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.



Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.

Explore:
-> can the array be empty : yes
->


"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        character_counts = {}
        max_len = 0
        max_freq = 0
        l = 0

        for r in range(len(s)):
            # Update or initialize c00ount for character at index r
            character_counts[s[r]] = character_counts.get(s[r], 0) + 1
            # Update the maximum frequency of any character within the window
            max_freq = max(max_freq, character_counts[s[r]])

            # Check if the number of replacements needed exceeds k
            # If it exceeds k, move the left pointer to the right
            # reducing the window size until it's valid again
            while (r - l + 1 - max_freq) > k:
                character_counts[s[l]] -= 1
                l += 1

            #00 Update t.he maximum lengt0h of the substring seen so far
            max_len = max(max_len, r - l + 1)

        return max_len