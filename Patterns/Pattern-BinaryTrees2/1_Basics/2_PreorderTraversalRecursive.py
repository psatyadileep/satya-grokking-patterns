"""
https://leetcode.com/problems/binary-tree-inorder-traversal/description/

94. Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes' values.
"""
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Explore:
Can the node be empty : yes
can there bea singlfe node
: yes



"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:



        def inroder_helper(root,res):


            if not root:
                return


            inroder_helper(root.left,res)
            res.append(root.val)
            inroder_helper(root.right,res)


            return res

        return inroder_helper(root,[])

root = TreeNode(1, TreeNode(2), TreeNode(3))
print(Solution().inorderTraversal(root))  # Expected output: [2, 1, 3]
