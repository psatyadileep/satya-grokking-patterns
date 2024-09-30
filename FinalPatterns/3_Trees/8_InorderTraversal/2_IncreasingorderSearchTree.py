""""
https://leetcode.com/problems/increasing-order-search-tree/
LC897
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.



Example 1:


Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
Example 2:


Input: root = [5,1,7]
Output: [1,null,5,null,7]
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        # Helper function to perform in-order traversal
        def in_order(node):
            if not node:
                return
            in_order(node.left)  # Traverse left subtree
            nodes.append(node)  # Visit node
            in_order(node.right)  # Traverse right subtree

        nodes = []
        in_order(root)

        # Create a dummy node to serve as the new root
        dummy = TreeNode(0)
        current = dummy

        # Construct the new tree
        for node in nodes:
            node.left = None  # Ensure no left child
            current.right = node
            current = node

        return dummy.right  # The real root is the right child of the dummy node
