"""
https://leetcode.com/problems/climbing-stairs/
70. Climbing Stairs
Solved
Easy
Topics
Companies
Hint
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
"""


class Solution:
    def climbStairs(self, n: int) -> int:


        if n<=2:
            return n


        return self.climbStairs(n-1) + self.climbStairs(n-2)


class Solution:
    def climbStairs(self, n: int) -> int:

        def helper(n, lookup):

            if n in lookup:
                return lookup[n]

            if n <= 2:
                return n

            lookup[n] = helper(n - 1, lookup) + helper(n - 2, lookup)

            return lookup[n]

        return helper(n, {})


class Solution:
    def climbStairs(self, n: int) -> int:
        step1 = 1  # represents the number of ways to climb to the (n-1)th step
        step2 = 1  # represents the number of ways to climb to the (n-2)th step

        # Iterate for n-1 steps
        for i in range(n - 1):
            temp = step2
            step2 = step1 + step2  # ways to reach the current step (n) is sum of ways to reach (n-1) and (n-2)
            step1 = temp  # shift step1 to step2's previous value

        return step2
