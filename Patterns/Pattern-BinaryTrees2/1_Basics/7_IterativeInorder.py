class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        result = []

        curr = root

        while curr or stack:
            # Reach the leftmost node of the current subtree
            while curr:
                stack.append(curr)
                curr = curr.left

            # Pop the node at the top of the stack
            curr = stack.pop()
            result.append(curr.va
            # Move to the right subtree to process its left nodes
            curr = curr.right

        return result