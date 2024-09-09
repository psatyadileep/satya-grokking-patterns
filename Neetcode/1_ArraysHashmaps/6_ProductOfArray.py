r"""
LC238: Product of array itself
https://leetcode.com/problems/product-of-array-except-self/description/
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Assumptions:
-> can the array be empty - yes

Brainstorm :
-> using prefix products and postfix products


Approach:
-> The idea is to calculate prfix product and Postfix Product
-> The value at any point with the index in poridt cwill be equal to
    -> response [i] = prefix[i-1]*postfix[i+1]
-> [1,2,3,4]
Prefix product = [1,2,6,24]
postfix product = [24,24,12,4]


Using two pass:
-> prefix = 1
    [1,1,2,6]

-> postfix starting from 1
    [       6] post fix = 1
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_product = 1
        postfix_product = 1
        result = [0]*n
        for i in range(n):
            result[i] = prefix_product
            prefix_product *= nums[i]
        for i in range(n-1,-1,-1):
            result[i] *= postfix_product
            postfix_product *= nums[i]
        return result