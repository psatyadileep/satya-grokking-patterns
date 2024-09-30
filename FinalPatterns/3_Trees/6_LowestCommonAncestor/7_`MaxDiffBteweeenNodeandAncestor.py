# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxDiff = float('-inf')

    def findMaxUtil(self, root, child):
        if not root or not child:
            return

        self.maxDiff = max(self.maxDiff, abs(root.val - child.val))

        self.findMaxUtil(root, child.left)
        self.findMaxUtil(root, child.right)

    def findMaxDiff(self, root):
        if not root or (not root.left and not root.right):
            return

        # Find max differences of this root with all its children
        self.findMaxUtil(root, root.left)
        self.findMaxUtil(root, root.right)

        # Further move left and right
        self.findMaxDiff(root.left)
        self.findMaxDiff(root.right)

    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.findMaxDiff(root)
        return self.maxDiff


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(root, max_val, min_val):
            if not root:
                return abs(max_val - min_val)

            max_val = max(root.val, max_val, min_val)

            min_val = min(root.val, min_val, max_val)

            left = dfs(root.left, max_val, min_val)
            right = dfs(root.right, max_val, min_val)

            return max(left, right)

        return dfs(root, root.val, root.val)


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        self.amx_diff = -sys.maxsize - 1

        def dfs(root, max_val, min_val):

            if not root:
                return
                # return abs(max_val-min_val)

            max_val = max(root.val, max_val, min_val)

            min_val = min(root.val, min_val, max_val)

            if not root.left and not root.right:
                self.amx_diff = max(self.amx_diff, abs(max_val - min_val))

            left = dfs(root.left, max_val, min_val)
            right = dfs(root.right, max_val, min_val)

        dfs(root, root.val, root.val)

        return self.amx_diff
