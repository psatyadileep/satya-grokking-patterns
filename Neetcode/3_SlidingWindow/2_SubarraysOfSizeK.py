"""

LC1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshol

Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.

 xample 1:

Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3
Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).
Example 2:

Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
Output: 6
Explanation: The first 6 sub-arrays of size 3


 Eplore:
 -> can the array be emmpty : yes
 ->the array can be of length less than k so handle integers

 BrainSTorm:
 1. Using Two loops
    Time COmplexity = o(n)^2
    Space = O(1)

2. Using two pOinters
Time COmplexity = o(n)

 """


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if not arr:
            return 0

        subarray_sum = 0
        count = 0
        L = 0

        for index, value in enumerate(arr):
            subarray_sum += value

            # Check if the subarray length has reached 'k'
            if index - L + 1 == k:
                if subarray_sum // k >= threshold:
                    count += 1
                subarray_sum -= arr[L]
                L += 1

        return count