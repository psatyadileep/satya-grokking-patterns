"""
https://leetcode.com/problems/trapping-rain-water/
42. Trapping Rain Water
Solved
Hard
Topics
Companies
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.


"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0

        l = 0
        r = len(height) - 1

        lmax = 0
        rmax = 0
        response = 0

        while l <= r:

            if height[l] <= height[r]:

                if height[l] >= lmax:
                    lmax = height[l]
                else:
                    response += lmax - height[l]

                l += 1

            else:

                if height[r] >= rmax:
                    rmax = height[r]

                else:
                    response += rmax - height[r]

                r -= 1

        return response