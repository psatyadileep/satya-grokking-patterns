"""
LC1. Two Sum

https://leetcode.com/problems/two-sum/description/


Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Explore:
-> can there be an empty array : yes
-> are the numbers sorted nop

Brainstorm :
-> we can use two pointers technique , constant space
-> we can also use a hasmap  -> o(n) time and space

Approach :

Two pointers:
    sort the numbers
    use left and right pointers
    find the target

Using hashmap
-> iterate through th elements
-> add them to hashmap
-> at the same time look if the lement - target if found in hasmap
-> if yes return the repsonse
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        lookup ={}
        if not nums:
            return [-1,-1]

        for index, val in enumerate(nums):

            if val not in lookup:
                lookup[val] = index

            if target-val in lookup:
                return [lookup[target-val],index]


        return [-1,-1]




class Solution2:
    def twoSum2(self, nums: List[int], target: int) -> List[int]:

        nums.sort()

        L = 0
        R = len(nums)-1

        while L<R:

            if nums[L] + nums[R] > target:
                R-=1

            elif  nums[L] + nums[R] < target:
                L+=1

            else:
                return [L,R]


        return [-1,-1]





print(Solution().twoSum([2,7,11,15],9))
