"""
https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
1161. Maximum Level Sum of a Binary Tree
Solved
Medium
Topics
Companies
Hint
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.
Example 1

Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation:
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
Example 2:

Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2


Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        self.max_sum = -sys.maxsize - 1
        self.max_level = -1

        q = collections.deque()

        q.append(root)
        level = 0

        while q:

            curr_sum = 0
            level += 1
            for _ in range(len(q)):
                node = q.popleft()
                curr_sum += node.val

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)
            print(curr_sum)

            if curr_sum > self.max_sum:
                self.max_sum = curr_sum
                self.max_level = level
            self.max_sum = max(self.max_sum, curr_sum)

        return self.max_level