class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        result = []

        curr = root

        while curr or stack:
            # Reach the leftmost node of the current subtree
            while curr:
                stack.append(curr)
                curr = curr.left
            else:
            # Pop the node at the top of the stack
                temp = stack.pop()

                if n
                result.append(curr.val)

            # Move to the right subtree to process its left nodes
            curr = curr.right

        return result