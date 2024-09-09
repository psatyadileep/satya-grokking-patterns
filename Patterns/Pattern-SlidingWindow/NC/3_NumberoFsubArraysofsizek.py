"""
https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/
Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.



Example 1:

Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3
Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).
Example 2:

Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
Output: 6
Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.

Epxlore:
1.Can the array be empty
2. Sike should be less than  or eqaul to lengt of array

Brain Storm :
1. Brute Force : Using Two loop so(n)^2
2. Optimized : using To pOinters

Approach:
1. Have two Poitter L =0 , R = 0
2. Move R pointer  until the distance <= Threshold
3. As iterate
"""


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        L = 0
        R = 0
        avg_sum = 0
        count = 0

        if not arr or k > len(arr):
            return 0

        for R in range(len(arr)):

            avg_sum += arr[R]

            if R - L + 1 == k:

                if avg_sum // k >= threshold:
                    count += 1

                avg_sum -= arr[L]

                L += 1

        return count






