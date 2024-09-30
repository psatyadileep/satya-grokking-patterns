"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
LC103
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []

"""

from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []

        if not root:
            return res

        dq = deque()
        level = 0

        dq.append(root)

        while dq:
            l = len(dq)  # Size of the current level
            level += 1
            temp = []

            for i in range(l):
                if level % 2 == 0:  # Even levels (right to left)
                    node = dq.pop()  # Process from the back
                    if node.right:  # Add children to the front (reverse order)
                        dq.appendleft(node.right)
                    if node.left:
                        dq.appendleft(node.left)
                else:  # Odd levels (left to right)
                    node = dq.popleft()  # Process from the front
                    if node.left:  # Add children to the back (normal order)
                        dq.append(node.left)
                    if node.right:
                        dq.append(node.right)

                temp.append(node.val)  # Store the node's value

            res.append(temp)  # Add the current level to the result

        return res
