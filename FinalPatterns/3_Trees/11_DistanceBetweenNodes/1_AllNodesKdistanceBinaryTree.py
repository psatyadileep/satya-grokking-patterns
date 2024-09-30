"""
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
LC863
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.



Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
Example 2:

Input: root = [1], target = 1, k = 3
Output: []

"""

from collections import defaultdict, deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        # Step 1: Build the graph (parent-child relationships in both directions)
        graph = defaultdict(list)

        def buildGraph(node: Optional[TreeNode], parent: Optional[TreeNode]):
            if node:
                if parent:
                    graph[node.val].append(parent.val)
                    graph[parent.val].append(node.val)
                buildGraph(node.left, node)
                buildGraph(node.right, node)

        # Build the graph by connecting each node with its parent
        buildGraph(root, None)

        # Step 2: Perform BFS starting from the target node
        q = deque([(target.val, 0)])  # Start BFS from the target node, with initial distance 0
        visited = set([target.val])
        result = []

        while q:
            node, dist = q.popleft()

            # If we've reached nodes at distance K, collect them
            if dist == K:
                result.append(node)

            # If distance exceeds K, no need to process further
            if dist < K:
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append((neighbor, dist + 1))

        # Return all nodes at distance K
        return result
