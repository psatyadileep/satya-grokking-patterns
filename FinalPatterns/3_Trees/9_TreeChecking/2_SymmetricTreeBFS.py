"""
https://leetcode.com/problems/symmetric-tree/submissions/1321502272/
101. Symmetric Tree
Solved
Easy
Topics
Companies
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).



Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false


Constraints:

The number of nodes in the tree is in the range [1, 1000].
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        q = collections.deque()

        q.append(root)

        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()

                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                else:
                    level.append(None)

            l = 0
            r = len(level) - 1

            while l <= r:
                if level[l] != level[r]:
                    return False
                l += 1
                r -= 1

        return True


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True  # An empty tree is symmetric

        q = deque([root])

        while q:
            level = []
            for _ in range(len(q)):
                curr = q.popleft()
                if curr:
                    level.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)
                else:
                    level.append(None)

            # Check if the current level is symmetric
            L = 0
            R = len(level) - 1
            while L <= R:
                if level[L] != level[R]:
                    return False
                L += 1
                R -= 1

        return True