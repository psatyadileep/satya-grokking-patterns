Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:


        self.tilt_sum = 0

        def helper(root):

            if not root:
                return 0

            left = helper(root.left)
            right = helper(root.right)

            v1 = left.val if left else 0
            v2 =  right.val if right else 0

            self.tilt_sum+= abs(v1-v2)

        helper(root)

        return self.tilt_sum