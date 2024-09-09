import sys
from typing import List
https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def isCondition(mid):
            # Check if mid element is in the same part (left or right) as the target
            if (nums[mid] >= nums[0]) == (target >= nums[0]):
                return nums[mid]
            else:
                # If target is in the right part and nums[mid] is in the left part
                if target >= nums[0]:
                    return sys.maxsize
                else:
                    return -sys.maxsize - 1

        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if isCondition(mid) >= target:
                r = mid
            else:
                l = mid + 1

        # Final check to see if the found index `l` actually contains the target
        return l if nums[l] == target else -1
#
# Example usage:
sol = Solution()
result = sol.search([4,5,6,7,0,1,2], 0)
print(result)  # Output: 4
