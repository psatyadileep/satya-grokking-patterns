import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:


        if not root1:
            return root2

        if not root2 :
            return root1


        v1 = root11.val if root1 else 0
        v2  = root2.val if root2 else 0


        q = deque([TreeNode(v1+v2), root1,root2])



        while q:
            curr, node1 , node2 = q.popleft()


            if node1.left and node2.left:

                v1 = node1.left
                v2 = node2.let

                curr.left = TreeNode(v1+v2)

            elif node1.left:

                curr.left = TreeNode(node.left.val)

            elif node2.left:
                curr.left  = TreeNode(node2.left.val)



