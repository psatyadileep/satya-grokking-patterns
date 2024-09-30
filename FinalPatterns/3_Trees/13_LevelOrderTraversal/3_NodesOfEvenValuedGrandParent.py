from collections import deque


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.result_sum = 0
        q = deque([root])

        while q:
            node = q.popleft()

            # Check if the current node is an even-valued grandparent
            if node.val % 2 == 0:
                # Add the grandchildren (left-left, left-right, right-left, right-right)
                if node.left:
                    if node.left.left:
                        self.result_sum += node.left.left.val
                    if node.left.right:
                        self.result_sum += node.left.right.val
                if node.right:
                    if node.right.left:
                        self.result_sum += node.right.left.val
                    if node.right.right:
                        self.result_sum += node.right.right.val

            # Add children to the queue
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return self.result_sum
