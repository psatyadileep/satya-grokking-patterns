class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize the maximum path sum with the smallest possible integer
        max_sum = float('-inf')

        def max_gain(node):
            nonlocal max_sum
            if not node:
                return 0

            # Recursively get the maximum contribution from left and right subtrees
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            # Calculate the path sum that passes through the current node
            current_path_sum = node.val + left_gain + right_gain

            # Update the global maximum path sum if needed
            max_sum = max(max_sum, current_path_sum)

            # Return the maximum gain the current node can contribute to its parent
            return node.val + max(left_gain, right_gain)

        max_gain(root)
        return max_sum
