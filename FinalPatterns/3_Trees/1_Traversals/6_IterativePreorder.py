
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        stack = []
        result = []

        if root:
            stack.append(root)

        while stack:

            node = stack.pop()

            result.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result

