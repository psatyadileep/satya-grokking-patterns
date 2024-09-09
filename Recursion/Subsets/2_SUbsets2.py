"""
https://leetcode.com/problems/subsets/
Given an integer array nums of unique elements, return all possible
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]

Appaorach:
-> Use pick and not pick patterb
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        response = []

        def subsets_helper(ind,current_set):
            if ind >= len(nums):
                response.append(current_set.copy())
                return

            current_set.append(nums[ind])
            subsets_helper(ind + 1,current_set)

            current_set.pop()
            subsets_helper(ind + 1,current_set)

        subsets_helper(0,[])
        return response
from datetime import datetime
start_time = datetime.now()
print(Solution().subsets("abcd"))
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
