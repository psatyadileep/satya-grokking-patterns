"""
Given a array
find the subsequcnes whose sum is equal to the target

Example 1:

Input: nums = [1,2,3]  ,3
Output: [[1,2],[3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
"""
from typing import List
from typing import List

class Solution:
    def subsets(self, nums: List[int], target: int) -> List[List[int]]:
        response = []

        def backtrack(index, subset, current_sum):
            if index == len(nums):
                if current_sum == target:
                    response.append(subset[:])
                return

            subset.append(nums[index])
            backtrack(index + 1, subset, current_sum + nums[index])

            subset.pop()
            backtrack(index + 1, subset, current_sum)

        backtrack(0, [], 0)
        return response

result = Solution().subsets([1, 2, 3, 4], 3)
print(result)


#Variation2

from typing import List

class Solution:
    def subsets(self, nums: List[int], target: int) -> List[List[int]]:
        response = []

        def backtrack(index, subset, current_sum):
            if current_sum == target:
                response.append(subset[:])

            for i in range(index, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1, subset, current_sum + nums[i])
                subset.pop()

        backtrack(0, [], 0)
        return response

result = Solution().subsets([1, 2, 3, 4], 3)
print(result)
