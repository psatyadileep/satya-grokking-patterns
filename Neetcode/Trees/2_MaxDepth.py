"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.



Example 1:
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:


        if not root:
            return 0


        left = 1+ self. maxDepth(root.left)

        right = 1+ self.maxDepth(root.right)

        return max(left,right)

