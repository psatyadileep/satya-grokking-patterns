"""
https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/description/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        # Initialize the lookup array to count frequencies of node values
        lookup = [0] * 10

        def helper(node):
            if not node:
                return 0

            # Update the frequency of the current node's value
            lookup[node.val] += 1

            # If it's a leaf node, check if the path is pseudo-palindromic
            if not node.left and not node.right:
                # Count how many values have an odd frequency
                odd_count = sum(1 for count in lookup if count % 2 == 1)

                # A path is pseudo-palindromic if at most one value has an odd count
                result = 1 if odd_count <= 1 else 0
            else:
                # Continue DFS on left and right children
                left = helper(node.left)
                right = helper(node.right)
                result = left + right

            # Backtrack by decrementing the current node's value in the lookup array
            lookup[node.val] -= 1

            return result

        # Start the DFS traversal from the root
        return helper(root)