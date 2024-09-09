"""
LC75
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.



Example 1:

Input: nums = [2,0,2,1,1,0]

Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]


Input: nums = [2,0,2,1,1,0]


[2,0,2,1,1,0]
L          R
"""
from typing import List


class Solution:
    def sortColors(self, nums: List[int]):
        def swap(l, r):
            nums[l], nums[r]  = nums[r], nums[l]

        L = 0
        R  = len(nums)-1
        i = 0
        while i<R:

            if nums[i]==0:
                swap(L,i)
                L+=1

            elif nums[i]==2:
                swap(R,i)
                R-=1
                i-=1

            i+=1


        return nums


print(Solution().sortColors([2,0,2,1,1,0]))


print(Solution().sortColors([2,0,1]))



