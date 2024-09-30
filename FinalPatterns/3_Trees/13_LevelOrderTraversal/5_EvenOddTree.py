from collections import deque


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = deque([root])
        level = 0  # Start from level 0

        while q:
            prev_val = None  # To keep track of the previous value at this level
            size = len(q)

            for i in range(size):
                node = q.popleft()

                # Check if the current level is even or odd
                if level % 2 == 0:
                    # At even levels, values must be odd and strictly increasing
                    if node.val % 2 == 0 or (prev_val is not None and node.val <= prev_val):
                        return False
                else:
                    # At odd levels, values must be even and strictly decreasing
                    if node.val % 2 != 0 or (prev_val is not None and node.val >= prev_val):
                        return False

                # Update prev_val for next comparison
                prev_val = node.val

                # Add children to the queue for the next level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level += 1  # Move to the next level

        return True
