class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.min_diff = float('inf')

        def in_order_traversal(node):
            if not node:
                return

            # Traverse the left subtree
            in_order_traversal(node.left)

            # Process the current node
            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val

            # Traverse the right subtree
            in_order_traversal(node.right)

        in_order_traversal(root)
        return self.min_diff



