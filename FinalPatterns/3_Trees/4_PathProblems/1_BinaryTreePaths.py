"""
LC257
https://leetcode.com/problems/binary-tree-paths/
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def helper(root, path):
            if not root:
                return
            if root.val:
                path.append(str(root.val))


            if not root.right and not  root.left:

                print(path)
                res.append("->".join(path))

            helper(root.left,path)
            helper(root.right,path)

            path.pop()


        helper(root, [])

        return res




a= TreeNode(10)
b= TreeNode(5)
c = TreeNode(3)
d= TreeNode(7)
e= TreeNode(15)
f = TreeNode(18)

a.left=b
b.left = c
b.right = d
a.right = e
e.right = f



new = TreeNode(1)
f = TreeNode(2)
g = TreeNode(5)
h = TreeNode(3)

new.left = f
f.right = g
new.right = h
print(Solution().binaryTreePaths(new))