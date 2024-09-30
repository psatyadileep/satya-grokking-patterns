"""
https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/
LC530
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.



Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        # If the tree is empty, return 0 (edge case)
        if not root:
            return 0

            # Initialize the minimum difference as infinity
        self.min_diff = float("inf")

        # Initialize previous value to None
        self.prev = None

        # Helper function for DFS in-order traversal
        def dfs(node):
            if not node:
                return

            # Traverse the left subtree
            dfs(node.left)

            # Process the current node
            if self.prev is not None:
                # Calculate the difference between current node value and previous node value
                self.min_diff = min(self.min_diff, abs(node.val - self.prev))

            # Update prev to the current node's value
            self.prev = node.val

            # Traverse the right subtree
            dfs(node.right)

        # Start DFS from the root
        dfs(root)

        # Return the minimum difference found
        return self.min_diff
