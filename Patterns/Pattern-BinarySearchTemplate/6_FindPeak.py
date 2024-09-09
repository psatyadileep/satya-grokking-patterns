"""
https://leetcode.com/problems/find-peak-element/
LC162

"""

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        L = 0
        R = len(nums) - 1

        def isCondition(mid):

            if nums[mid] > nums[mid + 1]:
                return True
            else:
                return False

        while L < R:

            mid = (L + R) // 2

            if isCondition(mid):
                R = mid

            else:
                L = mid + 1

        return L

        # if len(nums)==1:
        #     return 0

        # if nums[0]>nums[1]:
        #     return 0

        # if nums[len(nums)-1] > nums[len(nums)-2]:
        #     return len(nums)-1

        # L = 1
        # R =len(nums)-2

        # while L<=R:

        #     mid = (L+R)//2

        #     if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
        #         return mid

        #     elif  nums[mid]>nums[mid-1] :
        #         L = mid +1

        #     else:
        #         R = mid-1

        # return -1