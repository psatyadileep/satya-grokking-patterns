"""
https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/?envType=problem-list-v2&envId=mgo98zfm&
653. Two Sum IV - Input is a BST
Easy
Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        lookup = set()  # Use a set for O(1) lookups

        def helper(node: Optional[TreeNode]) -> bool:
            if not node:
                return False

            if k - node.val in lookup:
                return True

            lookup.add(node.val)
            print(f"Added {node.val} to lookup: {lookup}")

            return helper(node.left) or helper(node.right)

        return helper(root)




a= TreeNode(5)
b= TreeNode(3)
c = TreeNode(2)
d= TreeNode(4)
e= TreeNode(6)
f = TreeNode(7)

a.left=b
b.left = c
b.right = d
a.right = e
e.right = f

print(Solution().findTarget(a,9))