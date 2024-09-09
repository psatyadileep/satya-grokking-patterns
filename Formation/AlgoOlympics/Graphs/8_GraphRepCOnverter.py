from collections import defaultdict

'''
❓ PROMPT
Create a class that takes a vertex/edge list of a directed graph in the constructor. Suppose the inputted nodes are arbitrary strings.

Have 2 public methods:

(Map<string, int>, Array<Array<int>>) GraphConverter::getAsAdjacencyMatrix()

Return a tuple where the first value is a mapping to a row number and the second value is the VxV size matrix.

Map<string, List<string>> GraphConverter::getAsAdjacencyList()

Return a mapping from node ID to neighboring node IDs.

Example(s)
Suppose we have the following vertex list and edge list:
vertexList = ["n1", "n2", "n3"]
edgeList = [("n1", "n2")]

getAsAdjacencyList(vertexList, edgeList) should return
{
  "n1": ["n2"],
  "n2": [],
  "n3": [],
}

getAsAdjacencyMatrix(vertexList, edgeList) should return a tuple with the following values.

First value (IDs can be arbitrarily assigned in any order):
{
  "n1": 0,
  "n2": 1,
  "n3": 2,
}

Second value:
[
  [0, 1, 0],
  [0, 0, 0],
  [0, 0, 0],
]


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
class GraphConverter {
  getAsAdjacencyList(vertexList, edgeList) {}
  getAsAdjacencyMatrix(vertexList, edgeList) {}
}

class GraphConverter:
  def getAsAdjacencyList(self, vertexList: list[str], edgeList: list) -> dict[str, list[str]]:
  def getAsAdjacencyMatrix(self, vertexList: list[str], edgeList: list):


🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''


class GraphConverter:
  def getAsAdjacencyList(self, vertexList: list[str], edgeList: list) -> dict[str, list[str]]:


      graph = {}
      if not edgeList:
          return {}

      for vertex in vertexList:
          graph[vertex]=[]

      for edge , neighbor in edgeList:
          graph[edge].append(neighbor)

      return graph

print(GraphConverter().getAsAdjacencyList(vertexList = ["n1", "n2", "n3"],
edgeList = [("n1", "n2")]))


def getAsAdjacencyMatrix(self, vertexList: list[str], edgeList: list):
    vertexToIndex = {}

    for index, vertex in enumerate(vertexList):
        vertexToIndex[vertex] = index

    adjMatrix = []
    # make a matrix of zeros
    for _ in range(len(vertexList)):
        row = []
        for _ in range(len(vertexList)):
            row.append(0)
        adjMatrix.append(row)

    for edge in edgeList:
        outVertex, inVertex = edge
        adjMatrix[vertexToIndex[outVertex]][vertexToIndex[inVertex]] = 1

    return (vertexToIndex, adjMatrix)
