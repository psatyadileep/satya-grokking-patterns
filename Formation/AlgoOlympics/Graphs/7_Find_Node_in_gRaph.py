
'''
❓ PROMPT
Given a starting node in a graph and a target, traverse the graph using BFS and return true if a node with the target value exists, and false otherwise.

Example(s)
1 --- 2
|
3
node.hasPathTo(3) == True
node.hasPathTo(4) == False 


🔎 EXPLORE
List your assumptions & discoveries:
1. are there any disconnected 7_Graphs : No
2. can I  assume the the graph is unidirectinal

Insightful & revealing test cases:


🧠 BRAINSTORM
O(n), where n = # of nodes in graph

📆 PLAN
You may assume this graph is implemented via a Node class data structure. This can be achieved with a BFS traversal but must keep track of nodes that have already been visited to avoid an infinite loop by revisiting nodes in a cycle.

🛠️ IMPLEMENT
class Node {
  constructor(val, children = []) {}
  hasPathTo(target) {}
}

class Node:
  def __init__(self, val, children=[]):
  def hasPathTo(self, target: int) -> bool:


🧪 VERIFY
Run tests. Methodically debug & analyze issues.
example_graph = Node(12, [
  Node(18, [Node(1), Node(4, [Node(3), Node(9)])]),
]);

'''


from collections import  deque


class Node:

    def __init__(self, val, children=[]):
        self.val = val
        self.children = children

    def hasPathTo(self, target: int) -> bool:

        if not self:
            return False

        if self.val == target :
            return True
        response = []
        q = deque()
        q.append(self)
        visited = set()
        while q:

            curr = q.popleft()

            if curr.val == target:
                return True

            visited.add(curr.val)

            for child in curr.children:

                if child.val not in visited:
                    q.append(child)


        return False

example_graph = Node(12, [
    Node(18, [Node(1), Node(4, [Node(3), Node(9)])]),
]);

tests = [
    (9, True),
    (14, False),
    (None, False),
    (3, True)
]

for params, expected in tests:
    actual = example_graph.hasPathTo(params)
    if actual != expected:
        print(f"Test failed for {params}. Expected: {expected}, Actual: {actual}")
    else:
        print(f"Works fine for {params}.")