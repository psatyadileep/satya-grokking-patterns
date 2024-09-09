"""
https://leetcode.com/problems/path-sum-ii/description/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        res = []

        if not root:
            return res

        def helper(node, currentSum, path):

            if not node:
                return
            currentSum = currentSum + node.val
            path.append(node.val)
            # if not node and target == 0:
            if not node.left and not node.right and currentSum == targetSum:
                res.append(path[::])

            helper(node.left, currentSum, path)
            helper(node.right, currentSum, path)
            path.pop()

        helper(root, 0, [])
        return res

