"""
https://leetcode.com/problems/combinations/description/
LC77: Combinations
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.



Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
"""
from typing import List


# from typing import List
#
#
# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#
#
#         res =[]
#
#         def helper(index, subset):
#
#
#             if len(subset)==k:
#                 res.append(subset.copy())
#                 return
#             #     return
#
#             if index>n:
#                 return
#
#             for i in range(1,n+1):
#                 subset.append(i)
#                 helper(i+1,subset)
#                 subset.pop()
#
#
#         helper(1,[])
#         return res
#
# from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def helper(index, subset):
            if len(subset) == k:
                res.append(subset[:])
                return


            for i in range(index, n+1):  # Adjusted the range to start from the current index
                subset.append(i)
                helper(i + 1, subset)  # Pass i + 1 as the new index
                subset.pop()

        helper(1, [])  # Start with index 1
        return res

print(Solution().combine(n=4, k=2))
#
# print(Solution().combine(n = 4, k = 2))