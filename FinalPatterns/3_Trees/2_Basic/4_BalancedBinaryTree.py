# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_balance_and_height(node):
            if not node:
                return (True, 0)

            left_balanced, left_height = check_balance_and_height(node.left)
            right_balanced, right_height = check_balance_and_height(node.right)

            # Node is balanced if left and right subtrees are balanced and their heights differ by at most 1
            is_balanced = (left_balanced and right_balanced and
                           abs(left_height - right_height) <= 1)

            # Height of the current node is max height of its subtrees + 1
            height = max(left_height, right_height) + 1

            return (is_balanced, height)

        balanced, _ = check_balance_and_height(root)
        return balanced


# Example usage:
# Constructing the tree:
#       1
#      / \
#     2   2
#    / \
#   3   3
#  / \
# 4   4

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(2)
d = TreeNode(3)
e = TreeNode(3)
f = TreeNode(4)
g = TreeNode(4)

a.left = b
a.right = c
b.left = d
b.right = e
d.left = f
d.right = g

sol = Solution()
print(sol.isBalanced(a))  # Output: False


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_balance(node):
            if not node:
                return 0

            left = check_balance(node.left)
            if left == -1:
                return -1

            right = check_balance(node.right)
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return 1 + max(left, right)

        return check_balance(root) != -1