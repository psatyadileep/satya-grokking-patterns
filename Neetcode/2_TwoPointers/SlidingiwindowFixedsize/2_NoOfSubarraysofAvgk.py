"""
https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/
"""
"""
Explore:
1. If K > len(arr) return 0 
2. if not arra return 0 


BrainStorm: 
 Brute Forcr  = two lOop s

 Optimal two Pointers 






"""


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0

        if k > len(arr) or not arr:
            return 0

        curr_sum = 0
        count = 0
        for R in range(len(arr)):

            curr_sum += arr[R]

            if R - L + 1 == k:

                if curr_sum // k >= threshold:
                    count += 1

                curr_sum -= arr[L]
                L += 1

        return count







