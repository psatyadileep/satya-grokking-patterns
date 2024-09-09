'''
Given a BTree, find the lowest common ancestor of nodes A and B.


A
|
B

  3
 / \
1*   2 * (1)
/     \
0       5
        \
         6

lca(3, 2, 6) -> 3
lca(3, 0, 5) -> 3
lca(3, 0, 0) -> 0
lca(3, 0, 2)
3 -> 1 -> 0
3 -> 2


CLARIFICATION:
- not necessarily a BST
- the BTree is non-empty (have at least 1 node)
- values of the nodes can contain duplicatio
- function arguments are 3 BTrees, and return a BTree


OBSERVATIONS:
- 3 cases to consider

def lca(root, a, b)


IDEAS:
2) DFS - perform dfs on both left and right child.
3) Iterate through the left side , Iterate on the righ side
4) if  we find our root on either of the recursions - return the root
5) if left and right : return a root -> Ancestor
6) if nodes are on the same side - we return left if left returns a value else right


IDEA 2: Find the path to A, find the path to B. Find the intersection in the path. Find the problem Linked List Intersection on Leetcode.

'''


class BTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def lca(root, a, b):
    if not root:
        return None

    if root == a or root == b:
        return root

    left = lca(root.left, a, b)
    right = lca(root.right, a, b)

    if left and right:
        return root

    return left if left else right


"""
  3
 / \
1*   2 * (1)
/     \
0       5
        \
         6 

"""

root = BTree(3, BTree(1, BTree(0)), BTree(2, BTree(4), BTree(5, None, BTree(6))))
a = root.right.left
b = root.right.right.right
print(lca(root, a, b).value)

root = BTree(1)
a = b = root
print(lca(root, a, b).value)

'''
 3
  \
   999
'''
root = BTree(3, None, BTree(999))
a = root
b = root.right
print(lca(root, a, b))

print("root", root)
print("b", b)

'''
Given a BTree, find the LCA of 3 nodes A, B, and C.

1.
   A
 /  \
B    C

2. D
  / \
 A   B
      \
        C

3.   A
    /
   B
  /
 C

4. other cases reduces down the LCA for 2 nodes problem



'''


class BTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def lca(root, a, b):
    if not root:
        return None

    if root == a or root == b:
        return root

    left = lca(root.left, a, b)
    right = lca(root.right, a, b)

    if left and right:
        return root

    return left if left else right


def lca3(root, a, b, c):
    ab = lca(root, a, b)
    return lca(root, ab, c)


'''
Given a BTree and n nodes, find the LCA for those n nodes.



'''



def lca_generic(root, nodes):
    last_lca = nodes[0]
    for i in range(1, len(nodes)):
        last_lca = lca(root, last_lca, nodes[i])

    return last_lca
def lca_generic(root, nodes):
    last_lca = nodes[0]
    for i in range(1, len(nodes)):
        last_lca = lca(root, last_lca, nodes[i])

    return last_lca

"""
Given a binary tree and a,b ,. Find the distanc ebetween and b
"""
















