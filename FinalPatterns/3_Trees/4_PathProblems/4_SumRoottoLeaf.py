"""
https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        self.total_sum = 0

        def dfs(root, currSum):

            if not root:
                return 0

            currSum = currSum*10 + root.val
            print(currSum)
            if not root.left and not root.right:
                self.total_sum +=currSum
                print("++++++++++++++")
                print(self.total_sum)

            dfs(root.left, currSum)
            dfs(root.right, currSum)


        dfs(root, 0)
        return self.total_sum
""""
                 8 
                 / \
                5   6
               / \    \ 
             3     7   9
"""



a= TreeNode(8)
b= TreeNode(5)
c = TreeNode(3)
d= TreeNode(7)
e= TreeNode(6)
f = TreeNode(9)

a.left=b
b.left = c
b.right = d
a.right = e
e.right = f


print(Solution().sumNumbers(a))
