"""
LC11: Container with most amount of water
https://leetcode.com/problems/container-with-most-water/description/


You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Explore:
-> can the input be empty : yes
-> if the array is less than 1 return None

Brainstorm:
-> Brute Force using two loops
    Time Complixty  0 (n)^2
    Space =  O(1)

-> Using Two pointers :
    Space = O(1)
    Time = O(N)

Plans:
Brute Force:
-> Have two loops i , j .
-> I is th eouter loops
-> J is the inner loop with starts from element next to i
-> calculate the area at every iteration s, store the max are and return the valu e


Two Pointer:
-> Left pointer is on the left
-. right pointer is on the irght
-> calculate the are at every pint  : area = (R-L) * min(R,L)
-> store the highest area
-> move the pointer , left +=1 if left is msaller ,  R-=1 if right is smaller
-> return the response

"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height or len(height) < 2:
            return 0
        area = 0
        L = 0
        R = len(height) - 1
        max_area = float("-inf")
        while L < R:
            max_area = (R - L) * min(height[R], height[L])
            area = max(area, max_area)
            if height[L] < height[R]:
                L += 1

            else:
                R -= 1

        return area

