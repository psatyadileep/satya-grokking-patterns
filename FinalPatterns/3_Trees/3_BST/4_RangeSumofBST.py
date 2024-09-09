from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




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

print(Solution().rangeSumBST(a,7,15))