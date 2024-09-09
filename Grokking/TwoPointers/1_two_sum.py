"""
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

Explore
->is the input sorte d-> yes
-> do they have duplicates in the input : No


BrainSorm
-> Using Hashmap
-> Using bryte force - two loops

Plans
->



"""
from typing import List
#
#
# # Approach 1
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hash_map = {}
#
#         for index, val in enumerate(nums):
#             if target - val in hash_map:
#                 return [index, hash_map[target - val]]
#
#             hash_map[val] = index



# Approach 2 : Using Brute Force
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+ nums[j] == target:
                    return [i,j]


        return [-1,-1]

print(Solution().twoSum([1, 2, 3, 4, 6],6)==[1, 3])
print(Solution().twoSum([2, 5, 9, 11], target=11)==[0,2])


#approach 2:
"""
[2,7,11,15]
1.sort the numbers
2.
"""
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        L = 0 
        R = len(nums)-1

        while L<R:

            if nums[L]+ nums[R] == target:
               return [L,R]
            
            elif nums[L]+ nums[R] > target:
                R -=1
            
            else:
                L+=1
            

        return [-1,-1]
    

