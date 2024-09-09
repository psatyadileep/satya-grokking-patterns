"""
https://leetcode.com/problems/balanced-binary-tree/
Given a binary tree, determine if it is
height-balanced
.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:
"""


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_balance(node):
            if not node:
                return 0

            left = check_balance(node.left)

            right = check_balance(node.right)
            if right == -1 or right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return 1 + max(left, right)

        return check_balance(root) != -1