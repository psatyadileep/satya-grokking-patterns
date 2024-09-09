"""
Given a string , find the subsets

abcd


Approach :
-> use pick and not pick method for subsets
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


print(Solution().subsets("abc"))