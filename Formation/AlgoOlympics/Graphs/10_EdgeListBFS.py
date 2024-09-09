
'''
❓ PROMPT
Given a vertex and edge list of nodes and a start node for an undirected graph return the sum of all the nodes IDs accessible from the start node. For practice's sake, do this in BFS order.

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
    if startNode not in vertexList:
        return 0


    graph = collections.defaultdict(list)

    for node, neighbor in edgeList:
        graph[node].append(neighbor)
        graph[neighbor].append(node)


    visited= set()
    total  =0
    q = collections.deque()
    q.append(startNode)
    visited.add(startNode)

    while q:
        curr_node = q.popleft()
        total += curr_node
        neighbors = graph.get(curr_node)

        if not neighbors or len(neighbors)==0:
            continue


        for neighbor in neighbors:

            if neighbor in visited:
                continue
            visited.add(neighbor)
            q.append(neighbor)

    return total


    #
    # for edge in graph.keys():
    #     if edge not in visited:
    #         q.append(edge)






vertexList=[1, 2, 3, 4, 5]
edgeList=  [(2, 1), (3, 2), (3, 1)]

print(sumNodes(vertexList, edgeList, 1))
print(sumNodes(vertexList, edgeList, 10000))==0
print(sumNodes(vertexList, edgeList, 4))