"""
https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
LC129
129. Sum Root to Leaf Numbers
Solved
Medium
Topics
Companies
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

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


            dfs(root.left, currSum)
            dfs(root.right, currSum)
            if not root:

            currSum = currSum*10 + root.val
            print(currSum)
            if not root.left and not root.right:
                self.total_sum +=currSum
                print("++++++++++++++")
                print(self.total_sum)
                return 0


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
