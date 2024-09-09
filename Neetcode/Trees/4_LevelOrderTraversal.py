"""
https://leetcode.com/problems/binary-tree-level-order-traversal/description/
102. Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
"""
from collections import deque




class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        q = collections.deque()
        if root:
            q.append(root)

        while q:
            val = []

            for i in range(len(q)):
                node = q.popleft()
                val.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(val)
        return res

        return res

