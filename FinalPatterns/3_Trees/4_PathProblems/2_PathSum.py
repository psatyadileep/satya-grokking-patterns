# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node, current_sum):
            if not node:
                return False

            current_sum += node.val

            # Check if we have reached a leaf node and the sum matches targetSum
            if not node.left and not node.right:
                return current_sum == targetSum

            # Continue to search in the left and right subtrees
            return dfs(node.left, current_sum) or dfs(node.right, current_sum)

        return dfs(root, 0)




