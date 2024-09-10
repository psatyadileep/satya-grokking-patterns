# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0  # To keep track of the number of paths that sum to targetSum

        # Helper function to explore all paths from the current node
        def helper(node, curr):
            if not node:
                return

            # Check if the current path sum equals targetSum
            if curr + node.val == targetSum:
                self.count += 1

            # Explore the left and right children
            helper(node.left, curr + node.val)
            helper(node.right, curr + node.val)

        # DFS function to traverse all nodes
        def dfs(node):
            if not node:
                return

            # From each node, check all paths starting from that node
            helper(node, 0)

            # Recursively do the same for left and right subtrees
            dfs(node.left)
            dfs(node.right)

        # Start DFS from the root
        dfs(root)
        return self.count


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        self.count = 0

        lookup = {0: 1}

        def dfs(root, curr_sum):
            if not root:
                return

            curr_sum += root.val

            target = curr_sum - targetSum

            if target in lookup:
                self.count += lookup[target]

            lookup[curr_sum] = lookup.get(curr_sum, 0) + 1

            dfs(root.left, curr_sum)
            dfs(root.right, curr_sum)

            lookup[curr_sum] -= 1

        dfs(root, 0)
        return self.count