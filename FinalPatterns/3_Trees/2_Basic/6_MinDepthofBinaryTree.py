"""
https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

111. Minimum Depth of Binary Tree
Easy
Topics
Companies
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.


"""


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        min_num = sys.maxsize

        def dfs(node, num):
            nonlocal min_num
            if not node:
                return
            if not node.left and not node.right:
                min_num = min(num, min_num)
                return

            if node.left:
                dfs(node.left, num + 1)
            if node.right:
                dfs(node.right, num + 1)

        dfs(root, 1)

        return min_num