"""
https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
LC111

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root):
        if not root:
            return 0

        # Use a queue to perform BFS
        queue = deque([(root, 1)])  # (node, current depth)

        while queue:
            node, depth = queue.popleft()

            # If this node is a leaf, return the depth
            if not node.left and not node.right:
                return depth

            # Add children to the queue with incremented depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

        return 0

"""

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root):
        if not root:
            return 0

        # Use a queue to perform BFS
        queue = deque([(root, 1)])  # (node, current depth)

        while queue:
            node, depth = queue.popleft()

            # If this node is a leaf, return the depth
            if not node.left and not node.right:
                return depth

            # Add children to the queue with incremented depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

        return 0
