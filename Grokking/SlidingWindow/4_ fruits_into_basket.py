"""

LC904
https://leetcode.com/problems/fruit-into-baskets/description/
You are visiting a farm to collect fruits. The farm has a single row of fruit trees. You will be given two baskets,
and your goal is to pick as many fruits as possible to be placed in the given baskets.

You will be given an array of characters where each character represents a fruit tree. The farm has following restrictions:

Each basket can have only one type of fruit. There is no limit to how many fruit a basket can hold.
You can start with any tree, but you can’t skip a tree once you have started.
You will pick exactly one fruit from every tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
Write a function to return the maximum number of fruits in both baskets.

Example 1:

Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
Example 2:

Input: Fruit = ['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
"""

"""
This is very similar to the question This problem follows the Sliding Window pattern and is quite similar to Longest Substring with K Distinct Characters. In this problem, we need to find the length of the longest subarray with no more than two distinct characters (or fruit types!).
 This transforms the current problem into Longest Substring with K Distinct Characters where K=2.
"""

class Solution:
    def findLength(self, fruits):
        L = 0
        hash_map = {}
        max_len = float("-inf")

        for R in range(len(fruits)):
            fruit = fruits[R]
            hash_map[fruit] = hash_map.get(fruit, 0) + 1

            while len(hash_map) > 2:
                hash_map[fruits[L]] -= 1
                if hash_map[fruits[L]] == 0:
                    del hash_map[fruits[L]]
                L += 1

            max_len = max(max_len, R - L + 1)
        return max_len


print(Solution().findLength(['A', 'B', 'C', 'A', 'C']))
