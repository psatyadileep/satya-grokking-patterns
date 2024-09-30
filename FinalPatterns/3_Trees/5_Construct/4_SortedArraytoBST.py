"""
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
LC108
Given an integer array nums where the elements are sorted in ascending order, convert it to a
height-balanced
 binary search tree.



Example 1:


Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:88

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(l, r):
            if l > r:
                return

            mid = (l + r) // 2

            node = TreeNode(nums[mid])

            node.left = helper(l, mid - 1)

            node.right = helper(mid + 1, r)

            return node

        return helper(0, len(nums) - 1)