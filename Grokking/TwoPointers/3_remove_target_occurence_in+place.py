"""
LC27
https://leetcode.com/problems/remove-element/description/
Problem 1: Given an unsorted array of numbers and a target ‘key’, remove all instances of ‘key’ in-place and return the new length of the array.

Example 1:

Input: [3, 2, 3, 6, 3, 10, 9, 3], Key=3
Output: 4
Explanation: The first four elements after removing every 'Key' will be [2, 6, 10, 9].
Example 2:

Input: [2, 11, 2, 2, 1], Key=2
Output: 2
Explanation: The first two elements after removing every 'Key' will be [11, 1].

Assumptions:
1.can the array be empty : yes
2. Is the array sorted: No 


BrainSotrm:
1. Using Two pOinter Tecniqe:
    Time Complexity = O(n) 
    Spac e= constant Time



Approach :
-> we can use a two pointer technique to look for the the values that are to be replaced
"""


class Solution:
    def remove_element(self, arr, key):

        L = 0

        for R in range(len(arr)):

            if arr[R] != key:
                arr[L] = arr[R]
                L += 1

        return L


print(Solution().remove_element([3, 2, 3, 6,3, 10, 9, 3], 3))

print(Solution().remove_element([2, 11, 2, 2, 1], 2))