
"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
Given an array of sorted numbers, move all non-duplicate number instances at the beginning of the array in-place. The relative order of the elements should be kept the same and you should not use any extra space so that the solution has constant space complexity i.e., .

Move all the unique number instances at the beginning of the array and after moving return the length of the subarray that has no duplicate in it.

Example 1:

Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after moving element will be [2, 3, 6, 9].
Example 2:

Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after moving elements will be [2, 11].
"""


class Solution:
    def remove(self, arr):

        if not arr:
            return 0

        non_duplicate_count = 1

        for i in range(1 ,len(arr)):

            if arr[ i -1 ]!=arr[i]:
                arr[non_duplicate_count] = arr[i]
                non_duplicate_count+=1
        print(arr)
        return non_duplicate_count

#
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#
#         L = 0
#0
#         for R in range(1, len(nums)):
#             if nums[R]! = nums[L]:
#                 nums[L + 1] = nums[R]
#                 L += 1
#
#         return L + 1


print(Solution().remove([2, 3, 3, 3, 6, 9, 9] )==4)
print(Solution().remove([2, 2, 2, 11] )==2)