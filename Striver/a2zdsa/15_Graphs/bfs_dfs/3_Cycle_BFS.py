"""
You are given a directed graph represented as an adjacency list and a source node. Write a function to determine if there is a cycle in the graph starting from the given source node. If a cycle exists, return True; otherwise, return False.

Example:

Consider the following directed graph represented as an adjacency list:
graph = {
    0: [1, 2],
    1: [2],
    2: [3],
    3: [4],
    4: [1]
}
"""
import collections


def has_cycle(graph: Dict[int, List[int]], source: int) -> bool:

    q = collections.deque()

    visited = set()

    q.append((source,-1))
    visited.add(source)




    while q:

        for _ in range(len(q)):
            source, parent = q.popleft()

            neighbors = graph.get(source)

            for neighbor in neighbors:

                if neighbor not in visited:
                    q.append((neighbor,source))
                    visited.add(neighbor)
                elif parent!= neighbor:
                    return True


    return False




