"""
https://leetcode.com/problems/combinations/description/
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.



Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:


        response = []

        def dfs(index,currlist):

            if len(currlist)==k:
                response.append(currlist.copy())
                return


            for i in range(index,n+1):
                currlist.append(i)
                dfs(i+1,currlist)
                currlist.pop()


        dfs(1,[])
        return response

print(Solution().combine(4,2))




