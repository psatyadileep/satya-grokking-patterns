from collections import deque
def validPath(n, edges, source, destination):
    # Create the adjacency matrix
    adj_matrix = [[0] * n for _ in range(n)]
    for u, v in edges:
        adj_matrix[u][v] = 1
        adj_matrix[v][u] = 1

    # Initialize visited array and BFS queue
    visited = [False] * n
    queue = deque([source])

    # Mark the source as visited
    visited[source] = True

    while queue:
        # Dequeue a vertex from the front
        node = queue.popleft()

        # If we have reached the destination, return True
        if node == destination:
            return True

        # Visit all neighbors of the current node
        for neighbor in range(n):
            if adj_matrix[node][neighbor] == 1 and not visited[neighbor]:
                # Mark as visited and add to the queue
                visited[neighbor] = True
                queue.append(neighbor)

    # If we exhaust the queue without finding the destination
    return False
