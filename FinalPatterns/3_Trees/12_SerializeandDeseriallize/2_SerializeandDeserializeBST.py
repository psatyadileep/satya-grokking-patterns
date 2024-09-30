"""
https://leetcode.com/problems/serialize-and-deserialize-bst/description/
449. Serialize and Deserialize BST
Solved
Medium
Topics
Companies
Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.



Example 1:

Input: root = [2,1,3]
Output: [2,1,3]
Example 2:

Input: root = []
"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string."""
        res = []
        q = collections.deque([root])

        while q:
            node = q.popleft()
            if node is None:
                res.append("#")
            else:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)

        return ",".join(res)  # Corrected join with commas

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        if data == "#":
            return None

        data = collections.deque(data.split(","))
        root_val = data.popleft()

        if root_val == "#":
            return None

        root = TreeNode(int(root_val))
        q = collections.deque([root])

        while q:
            curr = q.popleft()

            left_val = data.popleft()
            if left_val != "#":
                curr.left = TreeNode(int(left_val))
                q.append(curr.left)

            right_val = data.popleft()
            if right_val != "#":
                curr.right = TreeNode(int(right_val))
                q.append(curr.right)

        return root

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans