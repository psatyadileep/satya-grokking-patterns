"""
https://leetcode.com/problems/validate-binary-search-tree/description/
LC98

98. Validate Binary Search Tree
Solved
Medium
Topics
Companies
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper(root, left, right):
            if not root:
                return True

            if not (left < root.val < right):
                return False

            return (
                    helper(root.left, left, root.val)
                    and helper(root.right, root.val, right)
            )

        return helper(root, float("-inf"), float("inf"))
