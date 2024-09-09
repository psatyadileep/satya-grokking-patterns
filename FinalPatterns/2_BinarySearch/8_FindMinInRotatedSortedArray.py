"""
153. Find Minimum in Rotated Sorted Array
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.


Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
"""

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1

        def condition(mid):
            return nums[mid] <= nums[R]  # Compare with nums[R] instead of nums[L]

        L = 0
        R = len(nums) - 1
        if nums[L] < nums[R]:
            return nums[0]

        while L < R:
            mid = (L + R) // 2

            if condition(mid):
                R = mid
            else:
                L = mid + 1

        return nums[L]

# Example usage
print(Solution().findMin([3, 4, 5, 1, 2]))  # Output should be 1
print(Solution().findMin([4, 5, 6, 7, 0, 1, 2]))  # Output should be 0
