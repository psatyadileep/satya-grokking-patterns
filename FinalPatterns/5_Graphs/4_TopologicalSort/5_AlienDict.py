from collections import defaultdict, deque
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Step 1: Create the graph
        adj_list = defaultdict(set)  # Adjacency list representation
        indegree = defaultdict(int)  # Indegree of each node

        # Initialize indegree for each character
        for word in words:
            for char in word:
                indegree[char] = 0

        # Step 2: Build the graph from the word list
        for i in range(len(words) - 1):
            first, second = words[i], words[i + 1]
            min_length = min(len(first), len(second))

            # Check if second word is a prefix of first word, which is invalid
            if len(first) > len(second) and first[:min_length] == second[:min_length]:
                return ""

            # Find the first difference and create an edge
            for j in range(min_length):
                if first[j] != second[j]:
                    if second[j] not in adj_list[first[j]]:
                        adj_list[first[j]].add(second[j])
                        indegree[second[j]] += 1
                    break

        # Step 3: Topological Sort using BFS (Kahn's Algorithm)
        queue = deque([char for char in indegree if indegree[char] == 0])
        topo_order = []

        while queue:
            char = queue.popleft()
            topo_order.append(char)

            for neighbor in adj_list[char]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # If the topological sort includes all characters, we have a valid order
        if len(topo_order) == len(indegree):
            return "".join(topo_order)
        else:
            return ""
