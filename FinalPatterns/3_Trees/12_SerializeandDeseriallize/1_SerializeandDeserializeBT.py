"""
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
LC297
erialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.



Example 1:


Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
Example 2:

Input: root = []
Output: []

"""

# Definition for a binary tree node.
# class TreeNode(object):
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
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
