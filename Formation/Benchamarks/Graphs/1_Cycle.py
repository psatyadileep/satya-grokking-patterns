import collections


def solution(adjacency):

    graph = collections.defaultdict(list)

    for row in range(len(adjacency)):
        for col in range(len(adjacency[row])):
            if adjacency[row][col] == True:
                graph[row].append(col)


    print(graph)


adj = [
  [False, True],
  [False, False]
]

print(solution(adj))