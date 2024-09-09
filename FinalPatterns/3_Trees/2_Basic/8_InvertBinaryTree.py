from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: If the root is None, return None
        if root is None:
            return None

        # Recursively invert the left and right subtrees
        left_inverted = self.invertTree(root.left)
        right_inverted = self.invertTree(root.right)

        # Swap the left and right children
        root.left = right_inverted
        root.right = left_inverted

        return root
