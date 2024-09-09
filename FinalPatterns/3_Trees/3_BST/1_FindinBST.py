"""
LC700
https://leetcode.com/problems/search-in-a-binary-search-tree/?envType=problem-list-v2&envId=mgo98zfm&
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def helper(node: Optional[TreeNode]) -> Optional[TreeNode]:
            # Base case: node is None
            if not node:
                return None

            # If the current node's value is the target value, return the current node
            if node.val == val:
                return node

            # If the target value is greater than the current node's value, search in the right subtree
            if val > node.val:
                return helper(node.right)

            # If the target value is less than the current node's value, search in the left subtree
            else:
                return helper(node.left)

        # Start the recursion with the root node
        return helper(root)