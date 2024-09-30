"""
https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/description/

865. Smallest Subtree with all the Deepest Nodes
Solved
Medium
Topics
Companies
Given the root of a binary tree, the depth of each node is the shortest distance to the root.

Return the smallest subtree such that it contains all the deepest nodes in the original tree.

A node is called the deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is a tree consisting of that node, plus the set of all descendants of that node.



Input: root = [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation: We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest nodes of the tree.
Notice that nodes 5, 3 and 2 contain the deepest nodes in the tree but node 2 is the smallest subtree among them, so we return it.
Example 2:

Input: root = [1]
Output: [1]
Explanation: The root is the deepest node in the tree.
Example 3:

Input: root = [0,1,3,null,2]
Output: [2]
Explanation: The deepest node in the tree is 2, the valid subtrees are the subtrees of nodes 2, 1 and 0 but the subtree of node 2 is the smallest.
"""
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        self.max_depth = 0  # Variable to track the maximum depth
        self.response = None  # This will hold the resulting subtree root

        # Helper DFS function to traverse the tree
        def dfs(node, depth):
            if not node:
                return depth  # Return current depth when reaching a leaf

            # Traverse the left and right subtrees
            left_depth = dfs(node.left, depth + 1)
            right_depth = dfs(node.right, depth + 1)

            # Current maximum depth of the node
            curr_depth = max(left_depth, right_depth)

            # Update the response if we find a node where both left and right subtrees are deepest
            self.max_depth = max(self.max_depth, curr_depth)

            if left_depth == self.max_depth and right_depth == self.max_depth:
                self.response = node

            # Update the maximum depth encountered so far

            return curr_depth  # Return the current maximum depth from this node

        dfs(root, 0)
        return self.response
