"""
https://leetcode.com/problems/binary-tree-postorder-traversal/description/

145. Binary Tree PostOrder Traversal

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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:



        def postorder_helper(root,res):


            if not root:
                return
            postorder_helper(root.left,res)

            postorder_helper(root.right,res)
            res.append(root.val)


            return res

        return postorder_helper(root,[])

root = TreeNode(1, TreeNode(2), TreeNode(3))
print(Solution().postrderTraversal(root))  # Expected output: [2, 1, 3]
