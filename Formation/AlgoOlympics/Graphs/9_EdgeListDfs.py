'''
❓ PROMPT
Given a vertex and edge list of nodes and a start node for an undirected graph return the sum of all the nodes values accessible from the start node. For practice's sake, do this in DFS order.

Example(s)
vertexList: [1, 2, 3, 4, 5]
edgeList: [(1, 2), (2, 3), (1, 3)]

1--2
| /
3      4    5

sumNodes(vertexList, edgeList, 1) -> 6

Node 1 has access to 2 and 3. The sum of all these nodes is 6. Nodes 4 and 5 aren't accessible.


🔎 EXPLORE
List your assumptions & discoveries:


Insightful & revealing test cases:


🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()


📆 PLAN
Outline of algorithm #:


🛠️ IMPLEMENT
function sumNodes(vertexList, edgeList, startNode) {
def sumNodes(vertexList: list, edgeList: list, startNode: int) -> int:


🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
import collections
def sumNodes(vertexList: list, edgeList: list, startNode: int) -> int:

    graph = collections.defaultdict(list)
    visited= set()
    for edge, neighbour in edgeList:

        graph[edge] = neighbour
        graph[neighbour] = edge


    total= 0

    def dfs_helper(curr_node):
        nonlocal total
        visited.add(curr_node)
        neighbors = graph.get( curr_node)

        total+= curr_node

        if not neighbors or len(neighbors)==0:
            return

        for neighbor in neighbors:

            if neighbor in visited:
                continue

            dfs_helper(neighbor)

    dfs_helper(startNode)
    return total

print(sumNodes(
    [1,2,3,4,5],
    [(2,1),(3,2), (3,1)],
    4
) == 4)




