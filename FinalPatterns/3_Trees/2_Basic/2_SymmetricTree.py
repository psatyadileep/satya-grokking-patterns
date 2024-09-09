# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False


        q = collections.deque()

        if root:
            q.append(root)


        while q:
            level = []
            for i in range(len(q)):

                curr = q.popleft()


                if curr:
                    level.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)
                else:
                    q.append(None)


            L = 0
            R = len(level)-1
            while L<R:
                if level[L]!=level[R]:
                    return False

        return True



