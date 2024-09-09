"""
https://www.geeksforgeeks.org/problems/rotation4723/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=rotation
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
            return 0

        while L < R:
            mid = (L + R) // 2

            if condition(mid):
                R = mid
            else:
                L = mid + 1

        return L

# Example usage
print(Solution().findMin([3, 4, 5, 1, 2]))  # Output should be 1
print(Solution().findMin([4, 5, 6, 7, 0, 1, 2]))  # Output should be 0
