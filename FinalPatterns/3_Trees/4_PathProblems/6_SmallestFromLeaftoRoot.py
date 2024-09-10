"""
https://leetcode.com/problems/smallest-string-starting-from-leaf/
LC8=988

988. Smallest String Starting From Leaf
Solved
Medium
Topics
Companies
You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.

Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

As a reminder, any shorter prefix of a string is lexicographically smaller.

For example, "ab" is lexicographically smaller than "aba".
A leaf of a node is a node that has no children.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        # Initialize the smallest string with a high lexicographical value.
        self.smallest_string = "~"  # '~' is lexicographically larger than any lowercase letter.

        def dfs(node, current_path):
            if not node:
                return

            # Prepend the character for the current node to the path.
            current_path = chr(node.val + ord('a')) + current_path

            # If it's a leaf node, update the smallest string if this path is smaller.
            if not node.left and not node.right:
                self.smallest_string = min(self.smallest_string, current_path)
                return

            # Continue the DFS traversal on left and right children.
            dfs(node.left, current_path)
            dfs(node.right, current_path)

        # Start DFS with an empty path.
        dfs(root, "")

        return self.smallest_string
