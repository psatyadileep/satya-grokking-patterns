"""
LC2461
2461. Maximum Sum of Distinct Subarrays With Length KYou are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

The length of the subarray is k, and
All the elements of the subarray are distinct.
Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

A subarray is a contiguous non-empty sequence of elements within an array.



Example 1:

Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15
Explanation: The subarrays of nums with length 3 are:
- [1,5,4] which meets the requirements and has a sum of 10.
- [5,4,2] which meets the requirements and has a sum of 11.
- [4,2,9] which meets the requirements and has a sum of 15.
- [2,9,9] which does not meet the requirements because the
"""
"""
Aprorachh 1 :
Using two loops :
-> You can use two loops
-> Time COmpleixty = O (N^2)

[1,5,4,2,9,9,9]
i 
j 


[1,5,4,2,9,9,9]
 i 
     j 
     
[1,5,4,2,9,9,9]
   i 
   j 


"""
from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = float("-inf")
        for i in range(len(nums)-k+1):
            sum = 0
            for j in range(i,i+k):
                sum+=nums[j]
                max_sum = max(max_sum,sum)

        return max_sum
# print(Solution().maximumSubarraySum([2, 1, 5, 1, 3, 2],3))
# print(Solution().maximumSubarraySum( [2, 3, 4, 1, 5], 2 ))


"""
Aporach 1: 
Using SLding window
[1,5,4,2,9,9,9]
 i 
     j 
     
[1,5,4,2,9,9,9]
   i 
   j 
"""


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        L = 0

        max_sum = float("-inf")
        current_sum = 0
        for R in range(len(nums)):
            current_sum += nums[R]

            if R-L+1>k :
                current_sum-=nums[L]
                L +=1

            max_sum = max(current_sum, max_sum)

        return max_sum


print(Solution().maximumSubarraySum([2, 1, 5, 1, 3, 2],3))
print(Solution().maximumSubarraySum( [2, 3, 4, 1, 5], 2 ))
