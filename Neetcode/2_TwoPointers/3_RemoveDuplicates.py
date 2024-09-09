"""
LC26: Remove Duplicates from a Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).


Assumptions:
-> can the ararra bem empty : yes

Brainstorm:
-> Approach1: Using sorted : Not optimall
    . Sort the numbers
    . get the set of the numbers are retun the length
    Time COmpleixty = O(n) Space = 0(n) , we need to use constant Space

-> APproach 2 : Using two pointers
    . L = 0 , R = 1 . L is the SLow pointer ,  R is the fast pointer
    . if L == R , we move  l to the next element


[1,2,2,3,4]
 l R

[1,2,2,3,4]
   l R

[1,2,2,3,4]
    l   R

[1,2,3,2,4]
     l   R

"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = 0

        for R in range(1,len(nums)):
            if nums[R]!= nums[L]:
                nums[L+1] = nums[R]
                L+=1

        return L+1
