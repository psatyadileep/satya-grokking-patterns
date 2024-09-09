"""
LC27: Remove Element
https://leetcode.com/problems/remove-element/description/
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.




Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).


 Assumptions:
 ->can there be an empty array : yes
 -> the array array legth can be less than one

 BrainSotrm:

    Approach 1:  Two new List
        . Iterate through the  array
        . append elemnets into array except the target element
        . Not optimal since they we want something in place
        Space Complecity = O(n) Time Complexity = O(N)


    Approach 2: Using Two Pointers: optimal
        . We have a left pointer starting at 0 ,
        . We have a right pointer R starting at 0
        .if R != target , then replace element at left pointer  incerement L
        .else do nothing
        .return L




"""


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        L = 0

        for R, num in enumerate(nums):
            if num != val:
                nums[L] = num
                L += 1

        return L + 1