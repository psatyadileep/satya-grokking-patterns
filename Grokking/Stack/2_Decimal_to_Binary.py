"""
Given a positive integer n, write a function that returns its binary equivalent as a string. The function should not use any in-built binary conversion function.

Examples
Example 1:

Input: 2
Output: "10"
Explanation: The binary equivalent of 2 is 10.
Example 2:

Input: 7
Output: "111"
Explanation: The binary equivalent of 7 is 111.

Explore:
1. If not number return -1
2.if the number always greater than 0

Brain  Storm


Example:
    1. Give number = 7
        7%2 =1
        7//2 = 3
"""



class Solution:
    def decimalToBinary(self, num):


        if num<0:
            return -1

        res = []
        while num>0:
            res.append(num%2)
            num //=2


        return "".join(res[::-1])



